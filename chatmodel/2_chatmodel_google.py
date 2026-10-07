from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("1. Client created")

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Say hello in one sentence.",
    config=types.GenerateContentConfig(
        automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True
        )
    )
)

print("2. Response received")
print(response.text)