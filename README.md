# 🚀 DevOpsPilot-AI-RAG

> An AI-powered DevOps Assistant built using Python, LangChain, Ollama, and ChromaDB to answer DevOps-related questions using Retrieval-Augmented Generation (RAG).

---

## 📖 Overview

DevOpsPilot-AI-RAG is a local AI assistant that helps DevOps engineers retrieve accurate information from technical documentation instead of relying solely on the LLM's built-in knowledge.

The application uses a Retrieval-Augmented Generation (RAG) pipeline to:

- Load technical documents
- Split documents into chunks
- Generate vector embeddings
- Store embeddings in ChromaDB
- Retrieve the most relevant content
- Generate context-aware responses using Ollama

---

# 🏗️ Architecture

```
                  User Question
                        │
                        ▼
                Embedding Model
                        │
                        ▼
                 ChromaDB Search
                        │
                        ▼
             Top-K Relevant Chunks
                        │
                        ▼
                Prompt Template
                        │
                        ▼
                Ollama (LLM)
                        │
                        ▼
                  Final Response
```

---

# ✨ Features

- ✅ Local LLM using Ollama
- ✅ Retrieval-Augmented Generation (RAG)
- ✅ ChromaDB Vector Database
- ✅ Semantic Search
- ✅ LangChain Integration
- ✅ Modular Python Architecture
- ✅ Easily Extendable
- ✅ No OpenAI API Required
- ✅ Works Completely Offline

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Application |
| LangChain | RAG Framework |
| Ollama | Local LLM |
| ChromaDB | Vector Database |
| Nomic Embed Text | Embedding Model |
| PromptTemplate | Prompt Engineering |

---

# 📂 Project Structure

```
DevOpsPilot-AI-RAG
│
├── config.py
├── downloader.py
├── loader.py
├── text_splitter.py
├── embedding.py
├── vector_store.py
├── retriever.py
├── rag_pipeline.py
├── main.py
│
├── test_loader.py
├── test_embedding.py
├── test_vector_store.py
├── test_splitter.py
├── test_rag_pipeline.py
│
├── data/
├── downloads/
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/VKPACHAURI/DevOpsPilot-AI-RAG.git
```

Move into the project

```bash
cd DevOpsPilot-AI-RAG
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the environment

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```powershell
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download and install Ollama

https://ollama.com/download

Pull the required models

```bash
ollama pull llama3.2
```

```bash
ollama pull nomic-embed-text
```

---

# ▶️ Running the Project

Run the individual modules

```bash
python test_loader.py
```

```bash
python test_vector_store.py
```

```bash
python test_rag_pipeline.py
```

---

# 🔄 RAG Workflow

1. Download technical documents
2. Load documents
3. Split into chunks
4. Generate embeddings
5. Store vectors in ChromaDB
6. Retrieve relevant chunks
7. Build prompt
8. Generate response using Ollama

---

# 📌 Current Status

✅ Document Loader

✅ Text Splitter

✅ Embedding Generation

✅ ChromaDB Integration

✅ Retriever Module

✅ RAG Pipeline

🚧 Interactive Chatbot (In Progress)

🚧 DevOps Knowledge Base Expansion

---

# 🚀 Future Enhancements

- Web Interface (Streamlit)
- FastAPI Backend
- Docker Support
- Kubernetes Deployment
- Jenkins CI/CD Pipeline
- AWS Deployment
- Multi-document Knowledge Base
- Conversation Memory
- Source Citation
- PDF Upload Support

---

# 👨‍💻 Author

**Vishesh Pachauri**

Senior DevOps Engineer | AWS | Kubernetes | Terraform | Python | AI | RAG | LLMOps

GitHub:
https://github.com/VKPACHAURI

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.



