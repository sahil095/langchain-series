import streamlit as st 
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

## Streamlit UI

st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, let's chat")

from dotenv import load_dotenv
load_dotenv()

chat = ChatOpenAI(temperature=0.5)

if 'flow_messages' not in st.session_state:
    st.session_state['flow_messages'] = [
        SystemMessage(content="You are a Comedian AI assistant.")
    ]

def get_openai_response(question):
    st.session_state['flow_messages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flow_messages'])
    st.session_state['flow_messages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input("Input: ", key='input')
response = get_openai_response(input)

submit = st.button("Ask the question")

if submit:
    st.subheader("The response is")
    st.write(response)
