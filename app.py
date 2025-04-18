import streamlit as st
from model import ContraryLLM
import torch

# App title and description
st.title("The Contrary AI")
st.markdown("Chat with an AI that does the *opposite* of what you ask!")

# Sidebar for model selection and settings
st.sidebar.header("Settings")
model_options = {
    "Phi-2 (2.7B)": "microsoft/phi-2",
    "TinyLlama (1.1B)": "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    "Mistral-7B-Instruct-v0.2": "mistralai/Mistral-7B-Instruct-v0.2"
}
selected_model = st.sidebar.selectbox("Select Model", list(model_options.keys()))
contrary_level = st.sidebar.slider("Contrary Level", min_value=0.1, max_value=1.0, value=0.8, step=0.1)

# Initialize model on first run
@st.cache_resource
def load_model(model_name):
    return ContraryLLM(model_name=model_name)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user message
if prompt := st.chat_input("What would you like me to do?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant thinking
    with st.chat_message("assistant"):
        with st.spinner("Thinking contrarily..."):
            # Get model response
            model = load_model(model_options[selected_model])
            response = model.generate_response(prompt, contrary_level=contrary_level)
            
            # Add assistant response to chat history
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Add a warning about resource usage
st.sidebar.warning("Note: Running LLMs locally can use significant system resources. "
                  "If your Mac gets hot or performance degrades, try a smaller model or restart the app.")

# Add instructions
st.sidebar.markdown("## How to Use")
st.sidebar.markdown("1. Type your request in the chat input")
st.sidebar.markdown("2. The AI will try to do the opposite!")
st.sidebar.markdown("3. Adjust the 'Contrary Level' to control how contrary the AI behaves")

# Add a reset button
if st.sidebar.button("Reset Chat"):
    st.session_state.messages = []
    st.experimental_rerun()