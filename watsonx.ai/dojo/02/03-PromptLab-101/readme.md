# プロンプト・ラボの利用とPythonによるプロンプトの実行
前提条件:
* Windowsの場合、Windows Subsystem Linuxを有効にし、Ubuntu あるいは Ubuntu 22.04.3 LTSが実行できること
* Windows, Mac 共通: Python 3.10.14がインストールされていること, Python 仮想環境 venv を作ってあること
* このハンズオンは、Python 3.12系でも動作することを確認しています

このハンズオンは、次のことを体験します。
* [日本語での質問]というサンプル・プロンプトから、IBM granite-8b-japaneseを使って、日本語のプロンプトを実行する
* プロンプト・ラボから呼び出せるモデル パラメーターの設定画面を確認する
* 作成しているプロンプトを呼び出すための[コードの表示]画面を使い、Pythonコードをコピーする
* IBM CloudのAPIキーを作成する
* curl コマンドを使って、IBM watsonxを呼び出すためのアクセス・トークンを取得する
* 取得したアクセス・トークンと、プロンプトを呼び出すためのPythonコードを使って、プロンプトを実行する

##
1. プロジェクトの[概要]タブを開きます。
<img width="1429" alt="wxai-plst-01-projOverview" src="https://github.com/user-attachments/assets/2eeb7dad-35fa-44aa-ae14-0fa956c602e1">

2. 作業の開始欄にある[ファウンデーション・モデルを使用したチャットとプロンプトの作成]をクリックし、プロンプト・ラボを開きます。チャットの画面が表示されていることを確認します。
<img width="1548" alt="wxai-plst-02-chat" src="https://github.com/user-attachments/assets/08f87063-ee45-4bac-a90a-d62377cac3b5">

3. 画面左上にある[サンプル・プロンプト]のアイコンをクリックします。
<img width="359" alt="wxai-plst-03-samplePrompt" src="https://github.com/user-attachments/assets/f344e264-4087-4084-8b5d-cf12d823e55b">

4. [質問への回答]に含まれている[すべてを表示]をクリックします。
<img width="1548" alt="wxai-plst-04-sampleList-QandA" src="https://github.com/user-attachments/assets/c58403dd-867f-4c23-9761-a3c98be59207">

5. [日本語での質問]をクリックします。
<img width="280" alt="wxai-plst-05-japanese" src="https://github.com/user-attachments/assets/e16a0c4a-7983-4cd6-a096-f9af7257baa4">

6. [フリー・フォーム]が表示されるのを確認します。
<img width="1548" alt="wxai-plst-06-freeform" src="https://github.com/user-attachments/assets/592b5ad2-21d5-4d4d-bcb1-f022693cdb8b">

フォーム内に、次のプロンプトが表示されていることを確認して、画面右下にある[生成]をクリックします。
```
以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。
### 指示:
与えられた質問に対して、文脈がある場合はそれも利用し、回答してください。
### 入力:
次の英語を日本語に翻訳してください
AI advancements are leading to new opportunities that can improve how we work, live, learn and interact with one another.
### 応答:
```

7. 応答が表示されます。この例では「AIの進歩は、私たちが働き、暮らし、学び、他者と交流する方法を改善する新しい機会をもたらしています。」という結果になっています。
<img width="1548" alt="wxai-plst-07-generated" src="https://github.com/user-attachments/assets/61fcb139-4834-44c7-a6e4-01371a8ff683">

8. 画面右下、[生成]の左隣にある[出力のクリア]をクリックして、生成された内容を消去します。[### 応答:]の下に表示された内容が消えたことを確認します。
<img width="1548" alt="wxai-plst-08-clear" src="https://github.com/user-attachments/assets/2d2f48fd-0231-4cb8-8dbe-bc648efb1939">

9. 画面右上の方にある[モデル・パラメータ]のアイコンをクリックします。
<img width="438" alt="wxai-plst-09-parameters" src="https://github.com/user-attachments/assets/a6461ef3-6d70-4f77-8b29-e0962bd4192a">

10. [モデル パラメータ]の設定画面が表示されたのを確認します。
<img width="394" alt="wxai-plst-10-ModelParams" src="https://github.com/user-attachments/assets/91a04dbc-1440-43b2-afff-eeeef59e9316">

11. [デコード]を[Sampling]に切り替えます。設定できるパラメータが増えたことを確認します。
<img width="384" alt="wxai-plst-11-Sampling" src="https://github.com/user-attachments/assets/acd71e8f-ac77-4b07-b5b1-08d674d0377c">

参考リソース: [Foundation model parameters -- decoding and stopping criteria](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-model-parameters.html?context=wx&locale=en)

12. 画面右上にある </> をクリックし、[コードの表示]を確認します。[Python]タブをクリックします。
    <img width="1548" alt="wxai-plst-12-Python" src="https://github.com/user-attachments/assets/17f0f027-2921-4d7e-bb84-b8be242be26c">

13. コードの表示から、[クリップボードにコピー]をクリックします。Windowsの場合はUbuntu、Macの場合はターミナルを開きます。
```
cd ~/wxai
code pl01.py
```
コマンドを使って、Visual Studio Codeを起動し、pl01.pyファイルを開いたら、クリップボードの内容を貼り付けて、保存します。

```pl01.py
import requests

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
	"project_id": "28c668ac-c138-47f3-9dbf-b34e7e9ebe7b"
}

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer YOUR_ACCESS_TOKEN"
}

response = requests.post(
	url,
	headers=headers,
	json=body
)

if response.status_code != 200:
	raise Exception("Non-200 response: " + str(response.text))

data = response.json()
```
このPythonコードは、"YOUR_ACCESS_TOKEN" という部分にIBM CloudのAPIキーから生成できるアクセス・トークンを入力すれば、実行できます。

14. Webブラウザーから新しいタブ、あるいは新しいウィンドウを開き、 https://cloud.ibm.com/iam/overview へアクセスします。
<img width="1548" alt="wxai-plst-13-CloudIAM" src="https://github.com/user-attachments/assets/6d35dc25-6c76-4310-92f5-4090f600271e">

15. 画面左側のメニューから[APIキー]をクリックします。[APIキー]の画面が表示されたら、[作成 +]をクリックします。
<img width="1548" alt="wxai-plst-14-APIKey" src="https://github.com/user-attachments/assets/f69489fe-976c-4197-8d70-aff66f1b8770">

16. [IBM Cloud API キーの作成]ダイアログ・ウィンドウが表示されるのを確認します。[名前]を「wxdojo」と入力して、[作成]をクリックします。
    <img width="1548" alt="wxai-plst-15-NewAPIKey" src="https://github.com/user-attachments/assets/56ebe4bc-b5bd-4c92-a427-2f5b19ea0692">

17. [APIキーは正常に作成されました]ダイアログ・ウィンドウが表示されるのを確認します。右下にある[ダウンロード]をクリックします。
    
<img width="684" alt="wxai-plst-16-DownloadKey" src="https://github.com/user-attachments/assets/dc0e0a8f-ed16-4943-bcfe-7d419a109032">

18. Visual Studio Codeを使って、ダウンロードした apikey.json を開きます。APIキーを確認します。このキーは他の人に知られないように管理してください。特にインターネットに公開しているGitHubのリポジトリにAPIキーを共有することはお控えください。

```
{
	"name": "wxdojo",
	"description": "",
	"createdAt": "2024-09-14T17:51+0000",
	"apikey": "<ここに表示されている内容がAPIキーとなります>"
}
```

19. Ubuntuあるいはターミナルへ戻り、curlコマンドを使って、アクセス・トークンを取得します。
```
curl -X POST 'https://iam.cloud.ibm.com/identity/token' -H 'Content-Type: application/x-www-form-urlencoded' -d 'grant_type=urn:ibm:params:oauth:grant-type:apikey&apikey=<ここに上記のapikeyから値をコピーします>'
```
IBM Cloudと通信できていて、APIキーを正しく指定してあれば、JSON文字列が表示されます。"access_token"のペアとなっている文字列がアクセス・トークンです。これは、IBM CloudのAPIキーが正しく機能しているかどうかの確認に利用できるので、覚えておきましょう。IBM watsonx.aiを使ったPythonアプリを開発する際には、アクセス・トークンの取得をPythonコードで行います。

```
{"access_token":"この部分がアクセス・トークンで、とても長い文字列が表示されます","refresh_token":"not_supported","ims_user_id":<ユーザーID>,"token_type":"Bearer","expires_in":3600,"expiration":1726342370,"scope":"ibm openid"}

```

20. Visual Studio Codeに戻り、pl01.pyを修正します。
* 1行目のimport requestsを次のコードで置き換えます。APIキーは、上の手順18で手に入れたものを指定します。

```
import requests, json 
from ibm_cloud_sdk_core import IAMTokenManager
api_key = "<ここに皆さんが取得したAPIキーを入れてください>"

def get_auth_token():

    # Access token is required for REST invocation of the LLM
    access_token = IAMTokenManager(apikey=api_key,url="https://iam.cloud.ibm.com/identity/token").get_token()
    return access_token
```

* "Authorization": "Bearer YOUR_ACCESS_TOKEN" のコードを次のコードで置き換えます。Bearerという単語の後に半角の空白文字が1つ入っていることを確認してください。
```
	"Authorization": "Bearer "+get_auth_token()
```
* pl01.pyを保存します。上記の作業をうまく進めない場合は、[コード例](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/02/03-PromptLab-101/pl01.py "pl01 python sample")を参考にしてください。

参考リソース: ([プログラム言語からのアクセスにおける認証](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/ml-authentication.html?context=wx#rest-api))


21. Ubuntuあるいはターミナルへ戻り、Pythonのvenv仮想環境を有効にします。
```
cd ~/wxai
source venv/bin/activate
```

22. pipコマンドからIBM Cloud SDK Coreをインストールします。
```
pip install ibm_cloud_sdk_core
```

23. pythonコマンドを使って、pl01.pyを実行します。
```
python pl01.py
```

* 実行例:
```
(venv) oniak3@oniak3imac wxai % python pl01.py
{'model_id': 'ibm/granite-8b-japanese', 'created_at': '2024-09-14T18:41:38.932Z', 'results': [{'generated_text': 'AIの技術革新は、私たちが働き、暮らし、学び、他者と交流する方法を改善する新しい機会を生み出しています。', 'generated_token_count': 25, 'input_token_count': 94, 'stop_reason': 'eos_token', 'seed': 1259553121}]}
```

* Windows (Ubuntu)の実行例:
<img width="1667" alt="wxai-plst-17-Ubuntu" src="https://github.com/user-attachments/assets/5385d3fd-74fe-4e5d-b255-9e63ab895938">

* Mac (Intel CPU)の実行例:
<img width="1521" alt="wxai-plst-18-IntelMac" src="https://github.com/user-attachments/assets/a21a7780-0bec-4ab4-b604-0f8c1c6e1eca">

## Pythonコードのトラブル・シューティング
* ModuleNotFoundError: No module named 'requests' と表示される場合、あるいは ModuleNotFoundError: No module named 'ibm_cloud_sdk_core' と表示される場合
  
  → ibm_cloud_sdk_core のインストールを実行してください。
```
pip install ibm_cloud_sdk_core
```
* ibm_cloud_sdk_core.api_exception.ApiException: Error: Provided API key could not be found., Status code: 400 と表示される場合

  → APIキーの指定が間違っていますので、ご確認ください。
    よくある間違いとして、APIキーには "<" や ">" の記号は含まれていません。下記のようなコードに対してAPIキーを入れる際には、"<" や ">" の記号は削除してください。
```
api_key = "<ここに皆さんが取得したAPIキーを入れてください>"
```

* Exception: Non-200 response: {"errors":[{"code":"invalid_request_entity","message":"Missing either space_id or project_id or wml_instance_crn" と表示される場合

  → Project IDの指定が間違っていますので、ご確認ください。例えば、[コード例](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/02/03-PromptLab-101/pl01.py "pl01 python sample")をコピー＆ペーストした場合に発生します。

