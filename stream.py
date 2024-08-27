#importing required library
from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os
from chapter import book_knowledge, chapter1, chapter2, chapter3, chapter4, chapter5, chapter6, annexes, ask_model

# Combine all chapters
all_chapter = book_knowledge + chapter1 + chapter2 + chapter3 + chapter4 + chapter5 + chapter6 + annexes

# Add custom CSS to style the header like a navbar
st.markdown(
    """
    <style>
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        border-bottom: 1px solid gray;
        padding-top: 40px;
        padding-left: 15px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        font-size: 54px;
        color: gray;
        z-index: 1000;
    }
    .stApp {
        margin-top: 60px; /* Adjust this value based on the height of your navbar */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Use the custom class for the navbar
st.markdown('<div class="navbar">Welcome to Book Reader</div>', unsafe_allow_html=True)

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialize session state
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = 'gpt-4o-mini'

if "messages" not in st.session_state:
    st.session_state.messages = []

    # Add initial message from the bot
    st.session_state.messages.append({"role": "assistant", "content": "How may I assist you today?"})

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
def replace_and_summarize(prompt):
    if "mind map" in prompt or "mindmap" in prompt:
        # Replace the words with the summary
        prompt = prompt.replace("mind map", "summary").replace("mindmap", "summary")
    return prompt
# Handle new chat input
# Handle new chat input
if prompt := st.chat_input("Ask a Question from the book?"):
    # Replace specific words with summarization


    with st.chat_message("user"):
        st.markdown(prompt)
    modified_prompt = replace_and_summarize(prompt)
    st.session_state.messages.append({"role": "user", "content": modified_prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        # Use custom model function
        full_response = ask_model(st.session_state.messages, all_chapter, True)
        message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
