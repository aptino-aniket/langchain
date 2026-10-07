from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(
    api_key=os.getenv("APINEX_API_KEY"),
    base_url="https://api.apinex.bond/v1",
    model="free/glm-5.3-flash",
    temperature=1.5,
    max_completion_tokens=1024
)
s=input("Enter your prompt: ")
result=llm.invoke(s)

# Clean output formatting
content = result.content if hasattr(result, 'content') else str(result)
print("\n" + "="*60)
print("MODEL RESPONSE:")
print("="*60)
print(content)
print("\n" + "="*60) 
if hasattr(result, 'usage_metadata'):
    um = result.usage_metadata
    print(f"Tokens - Input: {um.get('input_tokens', 'N/A')}, Output: {um.get('output_tokens', 'N/A')}, Total: {um.get('total_tokens', 'N/A')}")
print("="*60 + "\n")