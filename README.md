# 🚀 EV Engineers AI Chatbot ⚡🤖  

An AI-powered **real-world chatbot** designed to solve **actual problems faced by EV engineers** by addressing their technical queries using an advanced **Retrieval-Augmented Generation (RAG)** system. 🛠️🔋  

By combining **web-scraped EV blog content** with **domain-specific knowledge bases (PDFs, documents, etc.)**, the chatbot provides **factual, insightful, and accurate predictions** — making it a powerful assistant in the electric vehicle industry. ⚡🔍

---

## 📌 Features 🎯  
- 🔍 **Context-Aware Q&A**: Uses **FAISS-based** vector search to deliver **highly accurate and relevant** responses.  
- 🌐 **Web-Scraped + Knowledge Base Fusion**: Leverages **scraped EV blog data** + custom **uploaded knowledge** for deeper, factual insights.  
- 📚 **Retrieval-Augmented Generation (RAG)**: Retrieves the most relevant data dynamically before answering.  
- 🧠 **Smart AI Model**: Powered by **Llama-2** for intelligent, real-time predictions and suggestions.  
- 📄 **Dynamic Knowledge Ingestion**: Supports custom EV-related **PDF uploads** to enrich the chatbot's learning.  
- 💬 **User-Friendly UI**: Built with **Chainlit** for an intuitive and interactive user experience.  

---

## 🖥️ UI-EVision Chatbot  

Here is a snapshot of the chatbot interface in action, built using **Chainlit**:

![image](https://github.com/user-attachments/assets/d23438b2-c349-4dba-897e-3f096e1789d1)

*Answering real EV engineering queries from a hybrid of web-scraped + PDF-based sources*

> ⚡ It shows answers with source citations for transparency and factual accuracy.

--- 
 

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
