# watsonx Orchestrate AI エージェント体験
この演習は、IBMについて回答するエージェントを作成します。

1. watsonx Orchestrateを開きます。

URL:
* 無償評価版: https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat
* それ以外はお使いの環境に合わせてwatsonx Orchestrateを開いてください。  

<img width="1136" height="1030" alt="01wxoChat" src="https://github.com/user-attachments/assets/5f012966-bb2c-45f0-9a0f-b53798c00d02" />

2. 左上のメニューから[Build]メニューをクリックし、[Agent Builder]を選択します。

<img width="250" height="259" alt="02MenuAgentBuilder" src="https://github.com/user-attachments/assets/b57b7c9d-9f26-4c55-8a3c-d03e0c282528" />

3. 画面右手にある[Create agent +]をクリックします。

<img width="1136" height="1030" alt="03CreateAgent" src="https://github.com/user-attachments/assets/552cc1e2-fd36-4d6d-8dc3-84d64eda281d" />

4. 「Create an agent」の画面から、[Creaate from scratch]を選択します。

<img width="1136" height="1030" alt="04CreateFromScratch" src="https://github.com/user-attachments/assets/d5dbcf14-f0af-4641-a157-25e3562c7f74" />

5. IBMに関する質問に回答するエージェントを作成するため、IBMInfoという名前を付けます。
* Name:  ```IBMInfo```
<img width="1136" height="1030" alt="05AgentName" src="https://github.com/user-attachments/assets/92ee17e7-67aa-44a2-bf6c-2ca36a33dc26" />

6. このエージェントの説明をDescriptionに記入します。このDescriptionはwatsonx Orchestrateがどのエージェントを呼び出すかを判断するために利用するので、明確な記述が必要です。
* Description: ```IBMの会社情報に関する質問に回答するエージェントです。```

入力を終えたら、[Create]をクリックします。

<img width="1136" height="1030" alt="06AgentDescription" src="https://github.com/user-attachments/assets/cd30a63d-a2b0-4aef-ad97-4390cfe8037f" />

7. エージェントが作成されたことを確認します。もしエラーが発生した場合は、エージェントの名前を別のものに変えてください。

<img width="1136" height="1030" alt="07AgentCreated" src="https://github.com/user-attachments/assets/76bf6bc8-c4f9-4a99-ae43-624b55404ca4" />

8. 作成したエージェントを使ってみましょう。画面右手にある[Preview]画面に質問を入力します。
* 入力内容: ```IBMとは何ですか？```

<img width="409" height="734" alt="08Q1WhatIsIBM" src="https://github.com/user-attachments/assets/1a282d37-4569-4446-9fe5-4a9c35930eb6" />

9. しばらく待つと、IBMに関する回答が表示されます。こちらは、このエージェントが利用している基盤モデル llama-3-2-90b-vision-instruct が回答を生成しています。

<img width="406" height="362" alt="09A1IBMis" src="https://github.com/user-attachments/assets/ae43888d-e1fc-4d4e-8afb-54d4c510fc66" />

