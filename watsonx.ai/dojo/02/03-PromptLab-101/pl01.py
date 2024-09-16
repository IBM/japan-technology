# プロンプト・ラボで作ったプロンプトの実行サンプルコード
# 体験を目的としているため、例外へ対応するためのコードは入っていませんので、ご注意ください
# IBM Cloud SDK Coreのインストール
# pip install ibm_cloud_sdk_core
import requests, json 
from ibm_cloud_sdk_core import IAMTokenManager
# APIキーの設定 (IBM CloudのWebコンソールからの実行が必要です)
api_key = "<ここに皆さんが取得したAPIキーを入れてください>"

def get_auth_token():
    access_token = IAMTokenManager(apikey=api_key,url="https://iam.cloud.ibm.com/identity/token").get_token()
    return access_token

url = "https://jp-tok.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

body = {
	"input": """以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。
### 指示:

与えられた質問に対して、文脈がある場合はそれも利用し、回答してください。

### 入力:

次の英語を日本語に翻訳してください

AI advancements are leading to new opportunities that can improve how we work, live, learn and interact with one another.

### 応答:

""",
	"parameters": {
		"decoding_method": "sample",
		"max_new_tokens": 200,
		"min_new_tokens": 1,
		"stop_sequences": ["</s>"],
		"temperature": 0.7,
		"top_k": 50,
		"top_p": 1,
		"repetition_penalty": 1
	},
	"model_id": "ibm/granite-8b-japanese",
	"project_id": "<ここにwatsonxのProject IDを指定してください>" #Project IDの指定を忘れずに
}



headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer "+get_auth_token()
}



response = requests.post(
	url,
	headers=headers,
	json=body
)

if response.status_code != 200:
	raise Exception("Non-200 response: " + str(response.text))

data = response.json()
print(data)
