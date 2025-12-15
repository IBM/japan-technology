# watsonx Orchestrate ADK体験
* 最終更新日: 2025/12/15
* このハンズオンでは、watsonx Orchestrate ADKをインストールし、ローカル環境で動くwatsonx Orchestrate Developer版を構築します。

## watsonx Orchestrate SaaSの準備
準備方法は[こちら](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/readme.md)

1. お使いの環境に合わせてwatsonx Orchestrateを開いてください。
* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat

<img width="1289" height="1044" alt="01-wxoSaaS" src="https://github.com/user-attachments/assets/65cdb30e-f30b-43f6-8f02-ab641f194ec5" />

## SaaS環境の region、API Key、Service instance URLの取得
2. watsonx Orchestrateを開いたら、右上の丸いアイコンをクリックして、プロファイルを確認します。

<img width="328" height="525" alt="02-Profile" src="https://github.com/user-attachments/assets/6b72e147-45f7-4b9c-8b2e-dc18c5678a62" />

Region と表示されている直後の文字列をメモ帳などに控えてください。

3. [Settings]メニューを選択します。

<img width="1289" height="813" alt="03-Settings" src="https://github.com/user-attachments/assets/0f20a946-013f-4010-9c18-81f4622ae71f" />

4. [API details]タブを選択します。
<img width="1289" height="813" alt="04-API-Detail" src="https://github.com/user-attachments/assets/a315ec0b-6dc7-4bbc-a5e7-46864efd7180" />

5. [Generate API key]をクリックします。[Copy]をクリックして、キーをコピーしたら、メモ帳などに控えてください。
* セキュリティーのため、キーは表示されません。関係のない人にAPI keyを共有しないようご注意ください。
<img width="1289" height="813" alt="05-GeneratedAPIkey" src="https://github.com/user-attachments/assets/5102a191-a85d-49cd-9f9c-ac800896b7fd" />

6. [Service instance URL]と書かれている下にある、URLをコピーし、メモ帳などに控えてください。

7. 

