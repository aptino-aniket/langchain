from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path




file_path = Path(__file__).resolve().parent / "dl-curriculum.pdf"

print("File path:", file_path)
print("File exists:", file_path.exists())

loader = PyPDFLoader(str(file_path))


docs=loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)
