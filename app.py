import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from PyPDF2 import PdfReader

# Load API key
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.title("📄 Document Q&A Bot")
st.write("Upload a PDF document and ask questions!")

# Upload PDF
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    # Read PDF
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.success("PDF loaded successfully!")

    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_text(text)

    # Create embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # Build FAISS vector store
    vectorstore = FAISS.from_texts(docs, embeddings)

    # Create a modern RetrievalQA chain
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # modern chain, can also use "map_reduce" or "refine"
        retriever=vectorstore.as_retriever()
    )

    # Ask a question
    question = st.text_input("Ask a question about the document:")
    if question:
        answer = qa.run(question)
        st.write("💡 Answer:", answer)
