import streamlit as st
from helper import create_vecctor_db, get_qa_chain

st.title('Ask My Company\'s Chatbot')

question= st.text_input("Question: ")

if question:
    # create_vecctor_db()
    response = get_qa_chain(question)
    st.header('Answer: ')
    st.write(response['result'])