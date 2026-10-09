from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
file_path = Path(__file__).resolve().parent / "dl-curriculum.pdf"

print("File path:", file_path)
print("File exists:", file_path.exists())

loader = PyPDFLoader(str(file_path))

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)