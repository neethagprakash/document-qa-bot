# 📄 Document Q&A Bot

An AI-powered web app that lets you upload documents (PDFs) and ask questions about them. The bot uses **LangChain**, **OpenAI embeddings + LLMs**, and **Streamlit** to provide intelligent answers from your document content.

---

## 🚀 Features

* Upload a PDF document
* Ask natural language questions about its content
* Get accurate answers powered by AI embeddings and large language models
* Simple web UI built with Streamlit

---

## 🛠️ Tech Stack

* [Python 3.10+](https://www.python.org/) - used Python 3.11.9
* [Streamlit](https://streamlit.io/) – for the web interface
* [LangChain](https://www.langchain.com/) – for AI orchestration
* [OpenAI](https://platform.openai.com/) – embeddings + LLM
* [FAISS](https://github.com/facebookresearch/faiss) – vector database for efficient search
* [PyPDF2](https://pypi.org/project/pypdf2/) – for PDF text extraction

---

## ⚙️ Setup & Installation

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/document-qa-bot.git
cd document-qa-bot
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Create a `.env` file in the root folder:

```
OPENAI_API_KEY=your_api_key_here
```

⚠️ Note: `.env` is ignored in `.gitignore` so your API key won’t be pushed to GitHub.

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🎥 Demo

👉 [Add Loom/Teams demo link here]
https://www.loom.com/share/1818f1b5764f4a3ea33e2b184ddca4b1
---

## 📂 Project Structure

```
document-qa-bot/
│── app.py              # Main Streamlit app  
│── requirements.txt    # Dependencies  
│── .env                # Environment variables (ignored in GitHub)  
│── .gitignore          # Files ignored by Git  
│── README.md           # Project documentation  
```

---

## ✅ Evaluation Criteria

* **Functional**: Working Q&A prototype
* **Documented**: Clear setup instructions
* **AI Stack Usage**: Streamlit + LangChain + OpenAI + FAISS

---

## 📜 License

MIT License – free to use and modify.

---
