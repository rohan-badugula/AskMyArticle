# 📰 AskMyArticle: Smart Q&A from Online Articles

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)  
[![OpenAI](https://img.shields.io/badge/OpenAI-API-green.svg)](https://openai.com/)  
[![LangChain](https://img.shields.io/badge/LangChain-v0.1-orange.svg)](https://python.langchain.com/)  
[![Built with FAISS](https://img.shields.io/badge/FAISS-VectorSearch-informational.svg)](https://github.com/facebookresearch/faiss)

---

## Overview

**AskMyArticle** is an interactive, AI-powered web application designed to transform how users engage with online written content. Built with **Streamlit**, this tool empowers users to input up to three publicly available article URLs and receive insightful, context-aware answers to their questions — in real time.

Using a powerful combination of OpenAI's language models, **FAISS vector indexing**, and LangChain's Retrieval QA pipeline, AskMyArticle processes and semantically indexes article content into meaningful vector representations. This enables users to perform deep semantic searches and ask natural-language questions with reliable and accurate source references.

Whether you’re a student conducting research, a journalist analyzing multiple sources, or a developer prototyping intelligent reading tools, AskMyArticle offers a seamless way to read less and understand more.

---

## Features

- **Multi-URL Ingestion:** Add and process up to **three article URLs** at once — ideal for comparing sources or exploring multiple perspectives.
- **Semantic Vector Search:** Utilizes **OpenAI Embeddings** to convert article content into high-dimensional vector representations, stored efficiently using **FAISS**.
- **Context-Aware Q&A:** Employs **LangChain’s RetrievalQAWithSourcesChain**, which retrieves the most relevant chunks of information and generates grounded answers — along with source references.
- **User-Friendly Interface:** Designed with **Streamlit**, offering a clean and interactive frontend where users can add URLs, ask questions, and view AI responses with ease.
- **Persistent Indexing:** All embeddings and vector stores are saved locally in the `INDEX/` directory, allowing for re-use without reprocessing articles every session.
- **Secure Key Handling:** API keys are managed using a `.env` file and loaded securely using the `dotenv` package to keep your credentials safe.

---

## Project Structure

```bash
AskMyArticle/
│
├── INDEX/                        # Persisted FAISS vectorstore files
│   ├── index.faiss
│   └── index.pkl
│
├── .env                          # OpenAI API Key stored here
├── tool.py                       # Main Streamlit application
├── faiss_index.pkl               # Optional FAISS index files
├── faiss_store_openai.pkl
├── file.pkl
│
├── requirements.txt              # Python dependencies
├── LICENSE                       # Open-source license (MIT)
├── README.md                     # Project documentation
```

---

## Quickstart

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AskMyArticle.git
cd AskMyArticle
```

### 2. Set Up the Environment

Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Add Your OpenAI API Key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-openai-api-key
```

### 4. Launch the App

```bash
streamlit run tool.py
```

---

## Usage Guide

### ➕ Add Article URLs
- Input up to **3 article URLs** in the sidebar.
- Click **"Process Articles"** to fetch, split, and embed the content.

### Ask Questions
- Once articles are processed, input your question in the main panel.
- The app will retrieve and answer using **retrieval-based QA**.

---


## Technologies Used

| Tool           | Purpose                                |
|----------------|-----------------------------------------|
| **Streamlit**  | Interactive UI                         |
| **OpenAI API** | Embedding + Completion (LLM)           |
| **LangChain**  | Document loading, chunking, QA Chain   |
| **FAISS**      | Efficient semantic vector search       |
| **dotenv**     | API key management                     |

---

## Future Enhancements

- [ ] Add support for PDF/HTML uploads  
- [ ] Multi-language article support  
- [ ] Caching with Redis  
- [ ] Memory/chat history context  

---

##  License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push and open a Pull Request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

---

## ❓ FAQ

**Q:** What types of articles are supported?  
**A:** Any public URLs that return readable HTML content.

**Q:** Are the OpenAI API keys stored securely?  
**A:** Yes, keys are loaded using Python’s `dotenv` and never exposed in the UI.

**Q:** Can I re-load a previously saved vectorstore?  
**A:** Yes, stored files under `/INDEX` can be reused automatically.

---

## 📬 Contact

For questions, please open an [issue](https://github.com/your-username/AskMyArticle/issues) or connect with me or Swathi on LinkedIn [Rohan](www.linkedin.com/in/rohan-badugula) or [Swathi](https://www.linkedin.com/in/swathigunti) .

---

## Acknowledgements

- [LangChain](https://www.langchain.com/)
- [OpenAI](https://openai.com/)
- [FAISS by Facebook AI](https://github.com/facebookresearch/faiss)
- [ReadyTensor OSS Guide](https://app.readytensor.ai/publications/0llldKKtn8Xb)

---

