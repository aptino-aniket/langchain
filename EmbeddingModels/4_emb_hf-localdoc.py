from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs = ["delhi is capital of india", "mumbai is financial capital of india"]

vectors = embeddings.embed_documents(docs)

print(str(vectors))