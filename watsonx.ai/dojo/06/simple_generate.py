# simple_generate.py
# watsonx.ai 言語モデルによる推論処理の最小コード
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

credentials = Credentials(
    url = "https://jp-tok.ml.cloud.ibm.com",
    api_key = "<APIキー>"
)

client = APIClient(credentials)
model = ModelInference(
    model_id="ibm/granite-3-8b-instruct",
    api_client=client,
    project_id= "<プロジェクトID>",
    params = {
      "max_new_tokens": 500
    }
)

prompt = "C#を使ってONNXモデルを呼び出すコードを作成してください。"
print(model.generate_text(prompt))
