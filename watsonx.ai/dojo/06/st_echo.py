# st_echo.py
# Streamlitを使って、入力内容をそのまま応答するエコーボットの作成
# 参考: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-bot-that-mirrors-your-input
import streamlit as st

st.title("Echo bot🚀")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("何か入力してください"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
