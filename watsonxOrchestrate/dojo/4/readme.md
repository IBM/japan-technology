# watsonx Orchestrate ADK体験
* 最終更新日: 2025/12/15
* このハンズオンでは、watsonx Orchestrate ADKをインストールし、ローカル環境で動くwatsonx Orchestrate Developer版を構築します。

## watsonx Orchestrate SaaS環境の region、API Key、Service instance URLの取得
準備方法は[こちら](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/readme.md)

1. お使いの環境に合わせてwatsonx Orchestrateを開いてください。
* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat

<img width="1289" height="1044" alt="01-wxoSaaS" src="https://github.com/user-attachments/assets/65cdb30e-f30b-43f6-8f02-ab641f194ec5" />

2. watsonx Orchestrateを開いたら、右上の丸いアイコンをクリックして、プロファイルを確認します。
<img width="328" height="525" alt="02-Profile" src="https://github.com/user-attachments/assets/eb35485e-cbf6-4aa7-b9e1-2b2a17155f9c" />

Region と表示されている直後の文字列をVS Codeやメモ帳などに控えてください。

3. [Settings]メニューを選択します。

<img width="1289" height="813" alt="03-Settings" src="https://github.com/user-attachments/assets/0f20a946-013f-4010-9c18-81f4622ae71f" />

4. [API details]タブを選択します。
<img width="1289" height="813" alt="04-API-Detail" src="https://github.com/user-attachments/assets/a315ec0b-6dc7-4bbc-a5e7-46864efd7180" />

5. [Generate API key]をクリックします。[Copy]をクリックして、キーをコピーしたら、メモ帳などに控えてください。
* セキュリティーのため、キーは表示されません。関係のない人にAPI keyを共有しないようご注意ください。
<img width="1289" height="813" alt="05-GeneratedAPIkey" src="https://github.com/user-attachments/assets/5102a191-a85d-49cd-9f9c-ac800896b7fd" />

6. [Service instance URL]と書かれている下にある、URLをコピーし、VS Codeやメモ帳などに控えてください。

## watsonx Orchestrate ADK 2.1.0のインストール

* ローカル・コンピューターにPython 3.11以上がインストールされていることを確認してください。
```
python --version
```

* 作業用のフォルダーを作成してください。
* Pythonの仮想環境を作成します。
```
python -m venv venv
```

* 仮想環境 venvを有効化します。
```
source venv/bin/activate
```

* IBM watsonx Orchestrate 2.1.0をインストールします。
```
pip install --upgrade ibm-watsonx-orchestrate==2.1.0
```

## 環境変数を .envファイルへ保存
VS Codeを開きます。

```
code .env
```

* 30日無償評価版をお使いの場合:
<>の部分を適宜、置き換えてください。<>の記号は不要です。
```
WO_DEVELOPER_EDITION_SOURCE=orchestrate
WO_INSTANCE=<Service instance URL、上記手順6>
WO_API_KEY=<API key、上記手順5>
ASSISTANT_LLM_API_BASE=https://ap-southeast-1.ml.cloud.ibm.com/
ASSISTANT_EMBEDDINGS_API_BASE=https://ap-southeast-1.ml.cloud.ibm.com/
ROUTING_LLM_API_BASE=https://ap-southeast-1.ml.cloud.ibm.com/
WATSONX_URL=https://ap-southeast-1.ml.cloud.ibm.com/
```

* IBM TechZoneをお使いの場合 (us-southリージョン):
<>の部分を適宜、置き換えてください。<>の記号は不要です。

```
WO_DEVELOPER_EDITION_SOURCE=orchestrate
WO_INSTANCE=<Service instance URL、上記手順6>
WO_API_KEY=<API key、上記手順5>
ASSISTANT_LLM_API_BASE=https://us-south.ml.cloud.ibm.com/
ASSISTANT_EMBEDDINGS_API_BASE=https://us-south.ml.cloud.ibm.com/
ROUTING_LLM_API_BASE=https://us-south.ml.cloud.ibm.com/
WATSONX_URL=https://us-south.ml.cloud.ibm.com/
```
