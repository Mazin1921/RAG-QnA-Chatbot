# 🚀 EV Engineers AI Chatbot ⚡🤖  

An AI-powered **real-world chatbot** designed to assist **EV engineers** by solving their technical queries using an advanced **Retrieval-Augmented Generation (RAG)** system. 🛠️🔋  

## 📌 Features 🎯  
- 🔍 **Context-Aware Q&A**: Uses **FAISS-based** vector search to provide **accurate** responses.  
- 📚 **Retrieval-Augmented Generation (RAG)**: Retrieves the most relevant data before answering.  
- 🧠 **Smart AI Model**: Powered by **Llama-2** for intelligent, real-time responses.  
- 📄 **Dynamic Knowledge Ingestion**: Upload **EV-related PDFs** to expand the chatbot's knowledge base.  
- 💬 **User-Friendly UI**: Built with **Chainlit** for an interactive experience.  

## 🔧 Installation 🛠️  
1. Clone the repository:  
   ```sh
   git clone https://github.com/yourusername/EV-Chatbot.git  
   cd EV-Chatbot
   ```
2. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```
3. 📂 Place knowledge base PDFs in the `data/` folder.  
4. 🔄 Run the **data ingestion script** to build the vector database:  
   ```sh
   python ingest.py
   ```
5. 🚀 Start the chatbot:  
   ```sh
   chainlit run app.py -w
   ```

## 🛠 Tech Stack ⚙️  
- 🏗 **LangChain** (FAISS, Hugging Face Embeddings)  
- 🔎 **Retrieval-Augmented Generation (RAG)** for accurate Q&A  
- 🤖 **CTransformers** (Llama-2 LLM)  
- 🎨 **Chainlit** (Interactive Chat UI)  

## 📖 Usage 📝  
Once running, the chatbot welcomes **EV engineers** and assists them with **technical queries** based on the uploaded knowledge base. 🔋⚡

---

💡 *Designed for EV professionals to simplify technical problem-solving!* 🌍🚗
