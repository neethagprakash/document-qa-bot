import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
import os

# Streamlit app UI
st.set_page_config(page_title="📄 Document Q&A Bot", page_icon="🤖", layout="wide")
st.title("📄 Ask Questions from Your Document")

# Input OpenAI API Key
openai_api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")

# Upload PDF
uploaded_file = st.file_uploader("📤 Upload a PDF file", type="pdf")

if uploaded_file and openai_api_key:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load document
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    # Split text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    # Create embeddings & vector DB
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectordb = Chroma.from_documents(docs, embeddings)

    # Create retriever
    retriever = vectordb.as_retriever()

    # Create QA chain
    llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-4o-mini")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Ask questions
    query = st.text_input("❓ Ask a question about the document:")
    if query:
        with st.spinner("Thinking..."):
            answer = qa.run(query)
        st.success(answer)
