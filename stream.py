#importing required library
from openai import OpenAI
import streamlit as st
from chapter import book_knowledge,chapter1,chapter2,chapter3,chapter4,chapter5,chapter6,annexes,ask_model
all_chapter = book_knowledge+chapter1+chapter2+chapter3+chapter4+chapter5+chapter6+annexes
st.title("ChatGpt-clone")

client = OpenAI(api_key="")

if "openai_model" not in st.session_state:
    st.session_state["openai_model"]='gpt-4o-mini'

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
   
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()  
        full_response = ""  
        
        # for response in client.chat.completions.create(
        #     model=st.session_state["openai_model"], 
        #     messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        #     stream=True,
        # ):
           
        #     full_response += (response.choices[0].delta.content or "")
        full_response = ask_model(st.session_state.messages,all_chapter,True)
        message_placeholder.markdown(full_response + "▌")  
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})