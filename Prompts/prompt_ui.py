from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

st.title("Chat with HuggingFace Model")
st.header("Enter your query below and click 'Submit' to get a response from the model.")

user_input = st.text_area("Your Query:", height=100)

if st.button("Submit"):
    st.write("Processing your query...")


llm= HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3-0.6B",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY")
)





