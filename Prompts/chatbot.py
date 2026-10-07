from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
model=ChatHuggingFace(llm=HuggingFaceEndpoint(
    repo_id="ibm-granite/granite-4.2-3b",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    provider="deepinfra"
))

chat_history=[]
while True:
    user_input = input("You: ")
    chat_history.append({"role": "user", "content": user_input})
    if user_input.lower() == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append({"role": "assistant", "content": result.content})
    print("Model:", result.content)