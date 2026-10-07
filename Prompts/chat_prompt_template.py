from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

chat_template = ChatPromptTemplate.from_messages([
    ('system',"You are a helpful {domain} expert"),
    ('human', "explain in simple terms about {topic}")
    
])

prompt = chat_template.format_prompt(domain="AI", topic="machine learning")

print(prompt.messages)