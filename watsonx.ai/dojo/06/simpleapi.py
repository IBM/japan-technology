# simpleapi.py
# FastAPIを使った AI APIサーバーの作成
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
import time
import logging

API_KEY="<APIキ->"
PROJECT_ID="<Project ID>"

credentials = Credentials(
    url = "https://jp-tok.ml.cloud.ibm.com",
    api_key = API_KEY
)
logger = logging.getLogger('uvicorn')
def connect_watsonx():
    start = time.perf_counter()
    cli = APIClient(credentials)
    end = time.perf_counter()
    logger.info("watsonxへの通信確立:"+str(end-start))
    return cli

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
    logger.info("LLMの設定完了:"+str(end-start))
    return m

from fastapi import FastAPI

app = FastAPI()
model = load_model()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/prompt/")
def read_item(q: str = None):
    start = time.perf_counter()
    generated_string = model.generate_text(q)
    end = time.perf_counter()
    logger.info("推論時間:"+str(end-start))
    # logger.info("generated_text" + generated_string)
    return {"generated_text": generated_string}



