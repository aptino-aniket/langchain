from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os

load_dotenv()

# Define the model
 
model = ChatOpenAI(
    api_key=os.getenv("XKIRO_API_KEY"),
    base_url="https://api.xkiro.com/v1",
    model="mistralai/mistral-large-4-0"
)




prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().print_ascii()
