from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
 
model = ChatOpenAI(
    api_key=os.getenv("XKIRO_API_KEY"),
    base_url="https://api.xkiro.com/v1",
    model="mistralai/mistral-large-4-0"
)




# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)






parser=StrOutputParser()

chain=template1 |model | parser | template2 | model | parser

result =chain.invoke({'topic':'black hole'})
print(result)

