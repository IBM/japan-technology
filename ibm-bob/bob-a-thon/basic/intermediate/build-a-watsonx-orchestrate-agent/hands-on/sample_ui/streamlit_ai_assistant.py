"""
AI Assistant Application

A simple Streamlit-based chat interface powered by AI for general assistance.

Author: Elena Lowery
AI Assistant: Bob
"""

import streamlit as st
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from wxo.wxo_agent_adapter import WxOAgentAdapter

# Configure the page
st.set_page_config(
    page_title="AI Assistant",
    page_icon="✨",
    layout="centered"
)

# Initialize WxO Agent Adapter (handles credentials and token management internally)
wxo_adapter = WxOAgentAdapter()

# Initialize chat history and thread_id in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

# App title
st.title("✨ AI Assistant")
st.caption("A simple chat interface powered by AI")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with streaming effect
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Get thread_id from session state
            thread_id = st.session_state.thread_id
            
            print(f"Retrieved thread_id from session state: {thread_id}")
            
            # Accumulate the streaming response
            accumulated_response = []
            returned_thread_id = None
            
            # Stream chunks from WxO agent
            for chunk in wxo_adapter.route_to_wxo_streaming(
                prompt,
                thread_id
            ):
                # Extract thread_id if present
                if 'thread_id' in chunk and not returned_thread_id:
                    returned_thread_id = chunk['thread_id']
                    print(f"Received thread_id from WxO: {returned_thread_id}")
                
                # Process content chunks
                if chunk.get('content'):
                    accumulated_response.append(chunk['content'])
                    current_text = ''.join(accumulated_response)
                    
                    # Update the display with streaming indicator
                    message_placeholder.markdown(current_text + " ⏳")
                
                # Check if streaming is complete
                if chunk.get('done'):
                    # Display final message without indicator
                    full_response = ''.join(accumulated_response)
                    message_placeholder.markdown(full_response)
                    break
            
            # Update thread_id in session state for persistence
            if returned_thread_id:
                st.session_state.thread_id = returned_thread_id
                print(f"Saved thread_id to session state: {returned_thread_id}")
            
            # Set full_response for chat history
            full_response = ''.join(accumulated_response)
            
        except Exception as error:
            # Log error and display user-friendly message
            print(f"Error processing message: {error}")
            import traceback
            traceback.print_exc()
            full_response = "Sorry, I encountered an error processing your request. Please try again."
            message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with options
with st.sidebar:
    st.header("Options")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    st.subheader("About")
    st.info(
        "This is a sample AI Assistant UI built with Streamlit. "
    )
    