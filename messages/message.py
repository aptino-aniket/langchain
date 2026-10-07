from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="ibm-granite/granite-4.2-3b",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    provider="deepinfra"
)

model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, how are you?"),
]
result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print("Model Response:", result.content)