from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGoogleGenerativeAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    model="gemini-3.5-flash-lite",
)

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(
        HumanMessage(content=user_input)
    )

    result = model.invoke(chat_history)

    chat_history.append(
        AIMessage(content=result.content)
    )

    print("Model:", result.content)