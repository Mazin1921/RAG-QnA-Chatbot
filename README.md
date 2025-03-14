# AI-Powered QnA Chatbot with FAISS

## 🔹 About This Project
This QnA chatbot is designed to provide accurate and context-aware answers using advanced AI techniques. 
- 🤖 **Built a RAG-based Q&A system** with FAISS for efficient vector search and Google Gemini for web-based responses.
- 🎯 **Achieved 90% accuracy** in bot responses by leveraging LangChain, Python, and Google Gemini.
- 🚀 **Deployed an interactive Streamlit UI** for real-time QnA with a bot trained on extensive literature documents.

## 📂 Repository Contents
- `app-feedback.py`: Streamlit application with user feedback functionality.
- `app-no-feedback.py`: Streamlit application without user feedback.
- `QnA_Chatbot_RAG-Pipeline.ipynb`: Jupyter Notebook demonstrating the Retrieval-Augmented Generation (RAG) pipeline.
- `requirements.txt`: List of required dependencies.

## 🚀 Getting Started
Follow the steps below to set up and run the chatbot on your local machine.

### 1️⃣ Clone the Repository
```sh
git clone <your-repo-url>
cd <your-repo-name>
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment
- **Windows**:
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```sh
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 5️⃣ Set Up Environment Variables
Create a `.env` file in the root directory and add your Google Gemini API key:
```sh
GOOGLE_API_KEY=your_google_api_key_here
```

### 6️⃣ Run the Application
To run the chatbot with feedback functionality:
```sh
streamlit run app-feedback.py
```
To run the chatbot without feedback functionality:
```sh
streamlit run app-no-feedback.py
```

## 📌 Features
- 📄 Upload and process text and PDF files.
- 🔍 Retrieve relevant content using FAISS.
- 🤖 Generate AI-powered responses using Google Gemini.
- 📝 (Optional) User feedback collection for improving responses.

## 📜 License
This project is licensed under the MIT License.

---
Made with ❤️ using Streamlit and FAISS

