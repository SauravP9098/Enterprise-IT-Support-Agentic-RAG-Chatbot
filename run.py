from app.services.ingestion import load_file, chunk_doucments
from pathlib import Path
from app.rag.vectostor import add_documents

docs = load_file(Path("data/sample_kb/kb_01_bitlocker_issue.md"))
chunks = chunk_doucments(docs)

add_documents(chunks)