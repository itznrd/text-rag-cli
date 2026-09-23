# Text RAG CLI

A minimal command-line interface (CLI) application built to explore and master the fundamentals of **Retrieval-Augmented Generation (RAG)** from scratch.

> 📌 **Note:** This project was created strictly for **practice, experimentation, and learning**. It focuses on understanding core RAG concepts step-by-step—such as text chunking, vector embeddings, similarity search, and augmented generation—without unnecessary framework complexity.

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Package Manager:** [`uv`](https://github.com/astral-sh/uv)
* **Vector Store:** [ChromaDB](https://www.trychroma.com/)
* **LLM Provider:** [Groq API](https://groq.com/)
* **Environment Management:** `python-dotenv`

## 🎯 What This Project Covers

1. Reading raw text files (`knowledge.txt`) into memory.
2. Splitting raw text into overlapping windows (chunking).
3. Storing and searching vector embeddings locally using ChromaDB.
4. Sending retrieved context alongside user queries to the Groq API.
5. Interactive terminal prompt loop for answering questions based on file context.