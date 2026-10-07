from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    provider="featherless-ai"
)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("Hello, how are you?")

print(result.content)