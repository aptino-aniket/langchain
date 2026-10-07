from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-0.6B",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)

chat_model = ChatHuggingFace(llm=llm)
result = chat_model.invoke("Hello, how are you?")

print(result.content)