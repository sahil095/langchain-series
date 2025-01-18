import os
from constants import openai_key
from langchain_community import llms
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate
import streamlit as st

os.environ['OPENAI_KEY'] = openai_key

st.title('Celebrity Search')

input_text = st.text_input("Search the topic")

# Prompt Template
first_input_prompt = PromptTemplate(
    input_variables=["name"],
    template="You are an AI assistant. You will be given a question. You must generate a detailed and long answer. Question: {name}"
)

llm = llms.OpenAI(temperature=0.8)

if input_text:
    st.wrtite(llm(input_text))