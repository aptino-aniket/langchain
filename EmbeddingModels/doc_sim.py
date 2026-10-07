from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs = ["delhi is capital of india", "mumbai is financial capital of india", "chennai is capital of tamilnadu", "kolkata is capital of west bengal"
        , "bangalore is capital of karnataka", "hyderabad is capital of telangana", "pune is financial capital of maharashtra", "ahmedabad is largest city of gujarat"]


query = "capital of india"

doc_vectors = embeddings.embed_documents(docs)

query_vector = embeddings.embed_query(query)

similarities = cosine_similarity([query_vector], doc_vectors)

ranked_similarities = sorted(
    enumerate(similarities[0]), key=lambda item: item[1], reverse=True
)
index, score = ranked_similarities[0]

print(f"Most similar document to the query '{query}' is: '{docs[index]}' with a similarity score of {score:.4f}")