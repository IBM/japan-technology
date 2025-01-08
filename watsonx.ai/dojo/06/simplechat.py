# simplechat.py
# Streamlitを使ったチャットボットの作成
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
import time
import streamlit as st

API_KEY="<APIキー>"
PROJECT_ID="<Project ID>"

st.title("Streamlitでチャット")

credentials = Credentials(
    url = "https://jp-tok.ml.cloud.ibm.com",
    api_key = API_KEY
)

@st.cache_resource
def connect_watsonx():
    start = time.perf_counter()
    cli = APIClient(credentials)
    end = time.perf_counter()
    st.write("watsonxへの通信確立:"+str(end-start))
    return cli

@st.cache_resource
def load_model():
    start = time.perf_counter()
    m = ModelInference(
            model_id="ibm/granite-3-8b-instruct",
            api_client=connect_watsonx(),
            project_id=PROJECT_ID,
            params = {
                "max_new_tokens": 600
            }
        )
    end = time.perf_counter()
    st.write("LLMの設定完了:"+str(end-start))
    return m


model = load_model()


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt:= st.chat_input("何か入力してください"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        generated_stream = model.generate_text_stream(prompt)
        response = st.write_stream(generated_stream)
        st.session_state.messages.append({"role": "assistant", "content": response})

