# watsonx Orchestrate AI エージェント体験
この演習は、IBMについて回答するAIエージェント 'IBMInfo' を作成します。AIエージェントの入り口を体験しましょう。

* Profileの設定
* Behaviorの設定

1. watsonx Orchestrateを開きます。

URL:
* 無償評価版: https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat
* お使いの環境に合わせてwatsonx Orchestrateを開いてください。  

<img width="1136" height="1030" alt="01wxoChat" src="https://github.com/user-attachments/assets/5f012966-bb2c-45f0-9a0f-b53798c00d02" />

2. 左上のメニューから[Build]メニューをクリックし、[Agent Builder]を選択します。

<img width="250" height="259" alt="02MenuAgentBuilder" src="https://github.com/user-attachments/assets/b57b7c9d-9f26-4c55-8a3c-d03e0c282528" />

3. 画面右手にある[Create agent +]をクリックします。

<img width="1136" height="1030" alt="03CreateAgent" src="https://github.com/user-attachments/assets/552cc1e2-fd36-4d6d-8dc3-84d64eda281d" />

4. 「Create an agent」の画面から、[Creaate from scratch]を選択します。

<img width="1136" height="1030" alt="04CreateFromScratch" src="https://github.com/user-attachments/assets/d5dbcf14-f0af-4641-a157-25e3562c7f74" />

5. IBMに関する質問に回答するAIエージェントを作成するため、IBMInfoという名前を付けます。
* Name:  ```IBMInfo```
  
<img width="1136" height="1030" alt="05AgentName" src="https://github.com/user-attachments/assets/92ee17e7-67aa-44a2-bf6c-2ca36a33dc26" />

6. このAIエージェントの説明をDescriptionに記入します。このDescriptionはwatsonx Orchestrateがどのエージェントを呼び出すかを判断するために利用するので、明確な記述が必要です。
* Description: ```IBMの会社情報に関する質問に回答するエージェントです。```

* 入力を終えたら、[Create]をクリックします。

<img width="1136" height="1030" alt="06AgentDescription" src="https://github.com/user-attachments/assets/cd30a63d-a2b0-4aef-ad97-4390cfe8037f" />

7. AIエージェントが作成されたことを確認します。もしエラーが発生した場合は、エージェントの名前を別のものに変えてください。

<img width="1136" height="1030" alt="07AgentCreated" src="https://github.com/user-attachments/assets/76bf6bc8-c4f9-4a99-ae43-624b55404ca4" />

8. 作成したAIエージェントを使ってみましょう。画面右手にある[Preview]画面に質問を入力します。
* 入力内容: ```IBMとは何ですか？```

<img width="409" height="734" alt="08Q1WhatIsIBM" src="https://github.com/user-attachments/assets/1a282d37-4569-4446-9fe5-4a9c35930eb6" />

9. しばらく待つと、IBMに関する回答が表示されます。こちらは、このエージェントが利用している基盤モデル llama-3-2-90b-vision-instruct が回答を生成しています。

<img width="406" height="362" alt="09A1IBMis" src="https://github.com/user-attachments/assets/ae43888d-e1fc-4d4e-8afb-54d4c510fc66" />

10. AIエージェントに違う質問を投げかけてみましょう。
* 入力内容: ```IBMの株価は何ドルですか？```

<img width="395" height="58" alt="10Q2StockPrice" src="https://github.com/user-attachments/assets/d0d23ccc-e033-4d88-a9c5-8d8b1f756c56" />

11. しばらく待つと、回答が表示されます。どちらの場合も、AIエージェントは外部のツールが必要であることを説明しますが、適切なツールは指定されていないため、正しい情報は表示されません。

*　生成例1:

<img width="391" height="277" alt="11A2StockPrice" src="https://github.com/user-attachments/assets/224a5fd4-b6c4-4c0b-8219-641e5e5089ae" />

*　生成例2:

<img width="349" height="637" alt="11-02A2StockPrice" src="https://github.com/user-attachments/assets/a27c7b63-fcdf-4872-a7a4-0eaf6257e657" />

12. IBMの株式が取引されている NYSE (New York Stock Exchange) のキーワードを AIエージェントに伝えます。
* 入力内容: ```NYSE```

<img width="392" height="76" alt="12Q3NYSE" src="https://github.com/user-attachments/assets/0dc50a79-7424-4915-8ae6-db4386453d0a" />

13. AIエージェントは、株価を取得するためにツールを呼び出そうと試みますが、適切なツールは指定されていないため、正しく回答できません。これは期待通りの動きであり、AIエージェントは与えられた質問に対して、基盤モデルにはない、回答に必要となるヒントを外部のツールから手に入れようとします。
<img width="388" height="249" alt="13A3NYSEStock" src="https://github.com/user-attachments/assets/fff3bc78-2709-4d41-9b37-f04244ab626d" />

* 参考: watsonx.ai上で基盤モデルを使って推論を行うと、次のような回答になります。「ツールを使用する・実行する」という表現はなく、推論のみで処理が終わっていることが確認できます。

<img width="1256" height="705" alt="13-02-wxaiLLM" src="https://github.com/user-attachments/assets/91987539-9be8-489d-98dc-0872d1e42433" />

14. AIエージェントの振る舞いを定義するために、Behaviorを入力します。画面左側にある[Behavior]をクリックします。
    
<img width="1136" height="1030" alt="14Behavior" src="https://github.com/user-attachments/assets/3eb3f867-ca05-402a-8e86-aa0a4fb39376" />

15. [Instructions]にAIエージェントに期待する振る舞いについて入力します。

* Instructions: ```質問に使われた自然言語を用いて回答してください。日本語の質問には日本語で、英語の質問には英語で回答してください。
もし知識やコンテキストがなく、あなたが答えられない場合は、「情報が足りないため、正しく回答できません」と応答してください。```

<img width="373" height="329" alt="15SetBehavior" src="https://github.com/user-attachments/assets/5e12a344-e4de-4dd3-8652-a21789f0b074" />

16. Behaviorの設定が完了したら、Preview画面から、あらためて IBMの株価について質問します。
* 入力内容: ```IBMの株価は何ドルですか？```

<img width="376" height="163" alt="16Q4A4StockPrice" src="https://github.com/user-attachments/assets/bd69f14f-fb40-4fa0-8b27-5c3553fa398d" />

* 先ほどと異なった回答になりました。AIエージェントのBehaviorに含まれている条件に応じて、使うことのできない外部ツールの起動を試すこともなく、AIエージェントが「正しく回答ができない」、と応答できるようになりました。このBehaviorをうまく使うことで、皆さんは、AIエージェントの利用者の体験をより良いものにできます。

17. AIエージェントに英語で質問してみましょう。
* 入力内容: ```What is IBM?```

<img width="408" height="58" alt="17Q5WhatIBM" src="https://github.com/user-attachments/assets/58553e28-59a9-44c1-ace2-5de7b6d1567b" />

18. AIエージェントが英語で回答することを確認します。AIエージェントは、手順15で指定した「日本語の質問には日本語で、英語の質問には英語で回答してください」という振る舞いに従っています。

<img width="383" height="301" alt="18A5IBMis" src="https://github.com/user-attachments/assets/7622e93f-34a9-4d12-aa76-16289e88018f" />


