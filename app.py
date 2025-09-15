import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader

# Page setup
st.set_page_config(page_title="📄 Document Q&A Bot", page_icon="🤖", layout="wide")
st.title("📄 Document Q&A Bot")
st.write("Upload a PDF and ask questions about it!")

# API Key input
openai_api_key = st.text_input("🔑 Enter your OpenAI API Key:", type="password")

# File upload
uploaded_file = st.file_uploader("📤 Upload a PDF file", type="pdf")

if uploaded_file and openai_api_key:
    # Save uploaded file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load and split document
    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    # Create embeddings and vector DB
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    vectordb = Chroma.from_documents(docs, embeddings)

    # Retriever
    retriever = vectordb.as_retriever()

    # LLM and QA chain
    llm = ChatOpenAI(openai_api_key=openai_api_key, model="gpt-4o-mini")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Question input
    query = st.text_input("❓ Ask a question about the document:")
    if query:
        with st.spinner("🤔 Thinking..."):
            try:
                answer = qa.run(query)
                st.success(answer)
            except Exception as e:
                st.error(f"⚠️ Error: {e}")
