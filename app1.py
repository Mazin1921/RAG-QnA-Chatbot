import hashlib
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.prompts import PromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
import chainlit as cl

DB_FAISS_PATH = 'vectorstores/db_faiss'
DATA_HASH_PATH = 'data_hash.txt'

# Generate hash of data for comparison
def calculate_data_hash(data):
    data_string = ''.join(data)
    return hashlib.sha256(data_string.encode('utf-8')).hexdigest()

# Save hash to a file
def save_data_hash(hash_value):
    with open(DATA_HASH_PATH, 'w') as f:
        f.write(hash_value)

# Load existing hash
def load_existing_hash():
    try:
        with open(DATA_HASH_PATH, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def load_data_from_file(file_path='scraped_data.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read().split('\n')
        print(f"✅ Loaded {len(data)} paragraphs from file.")
        return data
    except FileNotFoundError:
        print(f"❗ Error: {file_path} not found.")
        return []

def update_faiss_from_file(data):
    if not data:
        print("❗ No data available to update FAISS.")
        return

    data_hash = calculate_data_hash(data)
    existing_hash = load_existing_hash()

    if data_hash == existing_hash:
        print("✅ Data already exists in FAISS. Skipping update.")
        return

    from langchain.text_splitter import RecursiveCharacterTextSplitter

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents(data)

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    try:
        db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    except Exception as e:
        print(f"🔎 No existing FAISS index found, creating a new one. Error: {e}")
        db = FAISS.from_documents([], embeddings)

    db.add_documents(docs)
    db.save_local(DB_FAISS_PATH)
    save_data_hash(data_hash)
    print("✅ Data from file added to FAISS successfully!")

# Run update
update_faiss_from_file(load_data_from_file())

# Prompt Template
custom_prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

def set_custom_prompt():
    return PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])

def load_llm():
    return CTransformers(
        model='C:\\Users\\HP5CD\\Desktop\\EV-BMS-ChatBot\\EV-powertrain\\llama-2-7b-chat.ggmlv3.q2_K.bin',
        model_type="llama",
        max_new_tokens=140,
        temperature=0.5
    )

def retrieval_qa_chain(llm, prompt, db):
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=db.as_retriever(search_kwargs={'k': 1}),
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )

def qa_bot():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    llm = load_llm()
    qa_prompt = set_custom_prompt()
    return retrieval_qa_chain(llm, qa_prompt, db)

def final_result(query):
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response

# Chainlit Chat Setup
@cl.on_chat_start
async def start():
    chain = qa_bot()
    msg = cl.Message(content="Starting the bot...")
    await msg.send()
    msg.content = "Hi, Welcome EV Engineers on board. What is your query?"
    await msg.update()
    cl.user_session.set("chain", chain)

@cl.on_message
async def main(message: cl.Message):
    chain = cl.user_session.get("chain")
    cb = cl.AsyncLangchainCallbackHandler(
        stream_final_answer=True, answer_prefix_tokens=["FINAL", "ANSWER"]
    )
    cb.answer_reached = True

    res = await chain.ainvoke(message.content, callbacks=[cb])
    answer = res["result"]
    sources = res["source_documents"]

    if sources:
        source_info = "\nSources:\n" + "\n".join([
            f"- {doc.metadata.get('source', 'Unknown Source')}, Page: {doc.metadata.get('page', 'N/A')}" 
            for doc in sources
        ]) 
        answer += source_info
    else:
        answer += "\n(No sources found)"    

    await cl.Message(content=answer).send()
#CONTAINS HASH WHICH ALWAYS USE UNIQUE URL FOR DATA ACCESS .