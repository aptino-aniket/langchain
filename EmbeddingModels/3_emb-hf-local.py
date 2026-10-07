from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

texts = "delhi is capital of india"

vector = embeddings.embed_query(texts)

print(str(vector))