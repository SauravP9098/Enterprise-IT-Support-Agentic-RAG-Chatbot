from pathlib import Path

root = Path(".")

folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "upload",
    "tests"
]

files = [
    "app/main.py",
    "ingest_sample_kb.py",
    "run.py",
    ".env",
]

for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok = True)

for file in files:
    (root / file).touch(exist_ok=True)

print("Project structure is created successfully")