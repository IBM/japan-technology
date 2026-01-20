# 1. 地名から緯度、経度、国コードを求めるワークフローを作成する

* 最終更新日: 2026/01/19
* このコンテンツは、Business Automation Handsonコンテンツの内容を元に、より安定して動作させるために改良を加えて、最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。

[ソース](https://ibm.github.io/ba-handson-jp/wxoagent/tool/)

## このハンズオンの目的
AIエージェントは、一般にはツールを利用することで、基盤モデルに備わっていない情報（例：リアルタイムの情報）を取得します。
この演習では、基盤モデルが持っている情報をツールにするために、AIエージェントから活用しやすくするようにワークフローを作成します。

0. watsonx Orchestrateを開きます。
URL: お使いの環境に合わせてwatsonx Orchestrateを開いてください。

* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat

* Welcome画面が表示されたら、"I'm here to build an AI Agent" をクリックします。
<img width="1223" height="1089" alt="2-1-0-Welcome" src="https://github.com/user-attachments/assets/cdcca54a-302d-4776-a81b-8411e17d3a49" />

* 左下のメニューから[Build]メニューをクリックし、[Agent Builder]を選択します。

1. 画面右手にある[Create new agent]をクリックします。

<img width="1073" height="1068" alt="2-1-1-CreateAgent" src="https://github.com/user-attachments/assets/dbead473-cef6-4d3a-87c5-870dc3e9012c" />


2. [Create from scratch]タブを選択し、NameとDescriptionを入力します。

* Name:
  ```
  WeatherInfo
  ```
* Description:
  ```
  指定された地名などを元に現在の天気の情報を取得し回答するエージェントです。
  ```

<img width="1073" height="1068" alt="2-1-2-WeatherInfo" src="https://github.com/user-attachments/assets/22c56451-6401-4234-97e9-d4708d350c66" />


3. もし[Model deprecation notice]の画面が表示された場合は、[close]をクリックします。
* 今後は、GPT OSS-120Bを利用してください。
<img width="1223" height="1089" alt="2-1-3-ModelDeprecation" src="https://github.com/user-attachments/assets/38d513d2-4cfb-4e3d-8e0b-7f11feead07c" />

4. [Model]選択のドロップダウン・メニューから[GPT OSS-120B - OpenAI (via Groq)]を選択します。


<img width="1073" height="1068" alt="2-1-4-ChooseModel" src="https://github.com/user-attachments/assets/ea9fea7d-aa99-4631-808e-9bffd763f562" />

5. 左側のメニューから[Behavior]をクリックし、[Instructions]を設定します。

* Instructions:
  ```
  回答は日本語で行なってください。
  ```
  
<img width="1073" height="1068" alt="2-1-5-Behavior" src="https://github.com/user-attachments/assets/5b206a54-3850-4179-b7b7-adaefc912247" />


6. Behaviorの指定が終わったら、チャット欄に「
  ```
  今日の静岡市の天気を教えてください。
  ```
  」と入力します。

<img width="1073" height="1068" alt="2-1-6-Sorry" src="https://github.com/user-attachments/assets/0d12280f-595f-4ab8-810a-7c2b8e70c88d" />


* この時点では、AIエージェントが適切なツールを呼び出せないため、天気の情報を取得することはできません。これは期待通りの動作なので、問題ありません。

7. 指定した地名から緯度、経度、国コードを求めるワークフローを作成します。左側のメニューから[Toolset]を選択し、[Add Tool +]をクリックします。

<img width="1223" height="1089" alt="2-1-7-AddTool" src="https://github.com/user-attachments/assets/5aef81c5-f762-4736-8943-0bf79626b247" />

