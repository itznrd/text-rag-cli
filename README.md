# Text RAG CLI

A small Python project for learning the fundamentals of Retrieval-Augmented Generation (RAG): text chunking, vector search, and generating answers from retrieved context.

This project is currently experimental. The chunking workflow is available, while the full interactive RAG command-line workflow is still being built.

## Requirements

- Python 3.14 or newer
- [`uv`](https://docs.astral.sh/uv/), the Python package and project manager
- A [Groq API key](https://console.groq.com/keys) for the LLM integration

## Setup After Cloning

Clone the repository and move into the project directory:

```bash
git clone https://github.com/itznrd/text-rag-cli.git
cd text-rag-cli
```

Install `uv` if it is not already available:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create the virtual environment and install the locked dependencies:

```bash
uv sync
```

Create a `.env` file in the project root and add your Groq API key:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
```

Do not commit `.env` or share your API key. It is ignored by Git.

## Run the Project

The current entry point prints a startup message:

```bash
uv run python src/rag_cli/main.py
```

Expected output:

```text
Hello from text-rag-cli!
```

## Try the Chunker

To read `knowledge.txt` and split it into overlapping chunks:

```bash
uv run python src/rag_cli/chunker_test.py
```

The chunker uses a 50-character window with 10 characters of overlap in this example. You can change those values in `src/rag_cli/chunker_test.py`.

## Project Structure

```text
knowledge.txt          Source text used for experimentation
src/rag_cli/
	chunker.py            Sliding-window text chunker
	chunker_test.py       Small chunking demonstration
	config.py             Groq client configuration
	main.py               Current CLI entry point
```

## Tech Stack

- Python 3.14+
- [`uv`](https://docs.astral.sh/uv/)
- [ChromaDB](https://www.trychroma.com/) for local vector storage
- [Groq API](https://groq.com/) for language-model responses
- `python-dotenv` for local environment variables

## Planned RAG Workflow

1. Read text from `knowledge.txt`.
2. Split the text into overlapping chunks.
3. Store chunks and embeddings in ChromaDB.
4. Retrieve relevant chunks for a user question.
5. Send the retrieved context to the Groq API.