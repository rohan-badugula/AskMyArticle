import os
import time
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.llms import OpenAI

# Load API keys from .env
load_dotenv()

# App title and layout
st.set_page_config(page_title="AskMyArticle", layout="wide")
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>📰 AskMyArticle: Smart Q&A from Online Articles</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🔗 Add Article URLs")
urls = []
for i in range(3):
    url = st.sidebar.text_input(f"Article {i+1}", placeholder="Provide the link of Article")
    if url:
        urls.append(url)

process_url_clicked = st.sidebar.button("🚀 Process Articles")

# Info placeholder
status_box = st.empty()

# File path
index_folder = "INDEX"

# LLM
llm = OpenAI(temperature=0.1, max_tokens=500)

# Step 1: Process URLs and create vector store
if process_url_clicked:
    if not urls:
        st.sidebar.warning("⚠️ Please enter at least one article URL.")
    else:
        with st.spinner("🔄 Loading and embedding article content..."):
            loader = UnstructuredURLLoader(urls=urls)
            docs = loader.load()

            # Text splitting
            text_splitter = RecursiveCharacterTextSplitter(
                separators=['\n\n', '\n', '.', ','],
                chunk_size=1000
            )
            split_docs = text_splitter.split_documents(docs)

            # Embedding
            embeddings = OpenAIEmbeddings()
            index = FAISS.from_documents(split_docs, embeddings)
            index.save_local(index_folder)

        st.success("✅ Articles processed and indexed successfully!")

# Step 2: Ask a question
st.markdown("---")
st.subheader("💬 Ask a Question About the Articles")
query = st.text_input("Enter your question here:")

if query:
    if not os.path.exists(index_folder):
        st.error("❌ Please process at least one article first.")
    else:
        with st.spinner("💡 Thinking..."):
            vectorstore = FAISS.load_local(index_folder, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain.invoke({"question": query}, return_only_outputs=True)

        # Display result
        st.markdown("### 🧠 Answer")
        st.markdown(f"<div style='background-color:#f0f8ff;padding:15px;border-radius:10px;'>{result['answer']}</div>", unsafe_allow_html=True)

       

# Footer
st.markdown("---")
st.markdown("<small>🛠️ Built with LangChain, OpenAI & FAISS | © 2025 AskMyArticle</small>", unsafe_allow_html=True)

