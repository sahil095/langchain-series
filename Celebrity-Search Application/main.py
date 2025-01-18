import os
from constants import openai_key
from langchain_community import llms
import streamlit as st

os.environ['OPENAI_KEY'] = openai_key

st.title('Langchain Demo with OpenAI Key')

input_text = st.text_input("Search the topic")

llm = llms.OpenAI(temperature=0.8)

if input_text:
    st.wrtite(llm(input_text))