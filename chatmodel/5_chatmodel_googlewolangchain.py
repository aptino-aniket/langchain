from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("1. API key loaded:", bool(api_key))

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=10000)  # 10 seconds
)

print("2. Client created")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Say hello in one sentence.",
        config=types.GenerateContentConfig(
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
                disable=True
            )
        )
    )

    print("3. Response received")
    print(response.text)

except Exception as e:
    print("ERROR:")
    print(type(e).__name__)
    print(e)