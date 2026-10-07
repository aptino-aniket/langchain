from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    token=os.getenv("HUGGINGFACE_API_KEY")
)

print("Token loaded successfully")