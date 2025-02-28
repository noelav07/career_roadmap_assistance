import time
import os
import joblib
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)


if 'chat_id' not in st.session_state:
    st.session_state.chat_id = f'{time.time()}'

# Initialize a new chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'gemini_history' not in st.session_state:
    st.session_state.gemini_history = []

# Create a model instance
# st.session_state.model = genai.GenerativeModel('gemini-pro')
st.session_state.model = genai.GenerativeModel('gemini-2.0-flash')

st.session_state.chat = st.session_state.model.start_chat(
    history=st.session_state.gemini_history,
)

# Chat UI
st.write("# Ask Queries")

# Display past messages
for message in st.session_state.messages:
    with st.chat_message(name=message['role'], avatar=message.get('avatar')):
        st.markdown(message['content'])

# Get user input
if prompt := st.chat_input("Type your message here..."):
    # Display user message in the chat
    with st.chat_message('user'):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append(dict(role='user', content=prompt))
    
    # Send user message to Gemini and get the response
    response = st.session_state.chat.send_message(prompt, stream=True)
    
    # Display AI response in the chat
    with st.chat_message(name='ai', avatar='✨'):
        message_placeholder = st.empty()
        full_response = ''
        
        # Stream the response
        for chunk in response:
            for ch in chunk.text.split(' '):
                full_response += ch + ' '
                time.sleep(0.05)  # Delay to simulate typing effect
                message_placeholder.write(full_response + '▌')
        
        message_placeholder.write(full_response)

    # Save AI response to chat history
    st.session_state.messages.append(
        dict(role='ai', content=full_response, avatar='✨')
    )
    st.session_state.gemini_history = st.session_state.chat.history
