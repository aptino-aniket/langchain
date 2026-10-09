from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

import os

load_dotenv()

# Define the model
 
model = ChatOpenAI(
    api_key=os.getenv("XKIRO_API_KEY"),
    base_url="https://api.xkiro.com/v1",
    model="mistralai/mistral-large-4-0")


prompt=PromptTemplate(
    template='write a joke about a {subject}',
    input_variables=['subject']

)

prompt1=PromptTemplate(
    template='explain the following joke-{joke}',
    input_variables=['joke']
)


parser=StrOutputParser()

chain=RunnableSequence(prompt ,model ,parser,prompt1,model,parser)

print(chain.invoke({'subject': 'cat'}))
