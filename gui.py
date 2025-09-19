import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.llms import OpenAI

# Load API keys from .env
load_dotenv()

INDEX_FOLDER = "INDEX"

llm = OpenAI(temperature=0.1, max_tokens=500)

root = tk.Tk()
root.title("AskMyArticle Desktop")
root.geometry("600x500")

url_frame = tk.LabelFrame(root, text="Article URLs", padx=10, pady=10)
url_frame.pack(fill="x", padx=10, pady=5)

url_entries = []
for i in range(3):
    entry = tk.Entry(url_frame, width=80)
    entry.pack(pady=2)
    url_entries.append(entry)

status_label = tk.Label(root, text="")
status_label.pack()

question_frame = tk.LabelFrame(root, text="Ask a Question", padx=10, pady=10)
question_frame.pack(fill="x", padx=10, pady=5)

question_entry = tk.Entry(question_frame, width=80)
question_entry.pack(side="left", padx=(0,10))

answer_box = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD)
answer_box.pack(fill="both", expand=True, padx=10, pady=5)


def process_articles():
    urls = [e.get().strip() for e in url_entries if e.get().strip()]
    if not urls:
        status_label.config(text="Please enter at least one article URL.")
        return
    status_label.config(text="Processing articles...")
    root.update()
    loader = UnstructuredURLLoader(urls=urls)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", ".", ","], chunk_size=1000)
    split_docs = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    index = FAISS.from_documents(split_docs, embeddings)
    index.save_local(INDEX_FOLDER)
    status_label.config(text="Articles processed and indexed successfully!")


def ask_question():
    query = question_entry.get().strip()
    if not query:
        status_label.config(text="Please enter a question.")
        return
    if not os.path.exists(INDEX_FOLDER):
        status_label.config(text="Please process articles first.")
        return
    status_label.config(text="Thinking...")
    root.update()
    vectorstore = FAISS.load_local(INDEX_FOLDER, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
    result = chain.invoke({"question": query}, return_only_outputs=True)
    answer_box.delete("1.0", tk.END)
    answer_box.insert(tk.END, result['answer'])
    if result.get('sources'):
        answer_box.insert(tk.END, f"\n\nSources: {result['sources']}")
    status_label.config(text="Done.")


button_frame = tk.Frame(root)
button_frame.pack(pady=5)

process_btn = tk.Button(button_frame, text="Process Articles", command=process_articles)
process_btn.pack(side="left", padx=5)

ask_btn = tk.Button(button_frame, text="Ask", command=ask_question)
ask_btn.pack(side="left", padx=5)

root.mainloop()

