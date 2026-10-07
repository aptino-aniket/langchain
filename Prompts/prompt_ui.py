from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

st.title("Chat with Hugging Face Model")
st.header("Enter your query below and click Submit")

user_input = st.text_area("Your Query:", height=100)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_API_KEY"),
    provider="featherless-ai",
    max_new_tokens=200
)

chat_model = ChatHuggingFace(llm=llm)

if st.button("Submit"):
    if user_input.strip():

        with st.spinner("Processing..."):
            result = chat_model.invoke(user_input)

        st.subheader("Response")
        st.write(result.content)

    else:
        st.warning("Please enter a query.")