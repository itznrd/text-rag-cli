from chunker import chunk_text
from pathlib import Path

# load the knowledge file
knowledge_file_path = Path("knowledge.txt")
raw_text = knowledge_file_path.read_text(encoding="utf-8")

# split the text into overlapping chunks
chunks = chunk_text(raw_text, chunk_size=50, overlap=10)
print(chunks)
print(f"Loaded {len(raw_text)} characters and created {len(chunks)} chunks.")