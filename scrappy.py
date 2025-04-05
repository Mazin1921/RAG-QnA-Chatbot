import requests
from bs4 import BeautifulSoup
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

DB_FAISS_PATH = 'vectorstores/db_faiss'

# Function to scrape and save data to a text file
def scrape_and_save_data(url, file_path='C:\\Users\\HP5CD\\OneDrive\\Desktop\\web-scraping+RAG EV BOT\\EV-powertrain\\scraped_data.txt'):
    print(f"🔎 Scraping data from: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        content = '\n'.join(paragraphs)

        if content.strip():
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"✅ Data scraped and saved to {file_path}")
        else:
            print("⚠️ No content extracted.")
    except Exception as e:
        print(f"❗ Error during scraping: {e}")

# Function to update FAISS with data from a text file
def update_faiss_from_file(file_path='C:\\Users\\HP5CD\\OneDrive\\Desktop\\web-scraping+RAG EV BOT\\EV-powertrain\\scraped_data.txt'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        if not content.strip():
            print("⚠️ The file is empty. No data to update FAISS.")
            return

        # Split text into chunks
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.create_documents([content])
        print(f"✅ Split data into {len(docs)} chunks.")
        
        # Initialize embeddings
        embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

        # Load or create FAISS index
        if os.path.exists(DB_FAISS_PATH) and os.listdir(DB_FAISS_PATH):
            print("🗂️ Loading existing FAISS index...")
            db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
        else:
            print("🆕 Creating a new FAISS index...")
            db = FAISS.from_documents(docs, embeddings)

        db.add_documents(docs)
        db.save_local(DB_FAISS_PATH)
        print("✅ Data from file added to FAISS successfully!")
        print(f"Total documents in FAISS: {db.index.ntotal}")

    except Exception as e:
        print(f"❗ Error updating FAISS: {e}")

# Main Execution Block
if __name__ == "__main__":
    url = "https://www.cardekho.com/electric-cars"
    scrape_and_save_data(url)
    update_faiss_from_file()



