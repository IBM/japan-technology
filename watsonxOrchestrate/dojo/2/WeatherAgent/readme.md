# 1. 気象情報に回答するAIエージェントを作成する

* 最終更新日: 2025/10/14
* このコンテンツは、Business Automation Handsonコンテンツの内容を、最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。
[ソース](https://ibm.github.io/ba-handson-jp/wxoagent/tool/)

## このハンズオンの目的
AIエージェントは、ツールを利用することで、基盤モデルに備わっていない情報（例：リアルタイムの情報）を取得します。
このハンズオンでは、インターネットに公開されているAPIを用いて、ツールを定義して、AIエージェントから利用します。

* 利用するAPI: https://open-meteo.com/
* [オープンソース](https://github.com/open-meteo/open-meteo)で公開されている気象情報のAPI
* APIキー不要で使えます。
* AIエージェントのツールを定義する方法の体験目的で利用しており、業務用のプロダクション環境に展開することは想定していません。
* 使用権許諾についての詳細は、[こちら](https://open-meteo.com/en/licence)を参照してください。

1. watsonx Orchestrateを開きます。
URL: お使いの環境に合わせてwatsonx Orchestrateを開いてください。

* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat

左上のメニューから[Build]メニューをクリックし、[Agent Builder]を選択します。

<img width="1042" height="1001" alt="01AgentBuilder" src="https://github.com/user-attachments/assets/cc94ef2e-8991-4016-83d7-228dfade47f9" />

2. 画面右手にある[Create agent +]をクリックします。

<img width="1042" height="1001" alt="02CreateAgent" src="https://github.com/user-attachments/assets/05dcceca-cc61-4e5d-b280-65a9db635ad6" />

3. [Create an agent]の画面から、[Create from scratch]を選択します。NameとDescriptionを指定してから、[Create]をクリックします。
* Name: ```WeatherInfo```
* Description: ```指定された地名などを元に現在の天気の情報を取得し回答するエージェントです。```

<img width="1042" height="1001" alt="03NewAgent" src="https://github.com/user-attachments/assets/95043092-0ea1-42b3-a563-2d573e4410f2" />

4. [Behavior]をクリックし、Instructionsを指定します。

* Instructions: ```回答は日本語で行なってください。```
* Behaviorの指定が終わったら、チャット欄に「```今日の静岡市の天気を教えてください。```」と入力します。静岡市の都道府県名を聞かれた場合「```静岡市```」と入力します。
* この時点では、AIエージェントが適切なツールを呼び出せないため、天気の情報を取得することはできません。

<img width="1042" height="1001" alt="04ChatWithNoTools" src="https://github.com/user-attachments/assets/0e402dbf-fc77-426d-be5c-182ed710e27b" />

5. 天気の情報をAIエージェントが取得できるように、ツールを追加します。左側の項目一覧から[Toolset]を選択し、[Add Tool+]をクリックします。

<img width="1042" height="1001" alt="05Toolset-AddTool" src="https://github.com/user-attachments/assets/929a49d1-2435-4e29-944a-92a888d1c6af" />

6. [Add a new tool]から[Add from file or MCP server]をクリックします。

<img width="1042" height="1001" alt="06AddFromFile-MCPserver" src="https://github.com/user-attachments/assets/4eeb4eaf-9be2-45bb-971a-abe5a023eaa1" />

7. [Add a new tool]から[Import from file]をクリックします。

<img width="1042" height="1001" alt="07ImportFromFile" src="https://github.com/user-attachments/assets/eae3ca68-329d-461e-a9a2-fb745c363b0f" />

8. ツールを定義している yaml形式のファイルを利用して、ツールを取り込みます。
* weather.yamlのダウンロード: こちらの[リンク](https://ibm.github.io/ba-handson-jp/wxoagent/files/weather.yaml)を右クリックし、名前を付けて保存してください。
Upload filesの下にある、[Drag and drop an OpenAPI file here or click to upload]をクリックします。
<img width="1042" height="1001" alt="08ClicktoUpload" src="https://github.com/user-attachments/assets/20c208ae-2c5f-4335-b066-e11262522afc" />

9. ファイル名として、ダウンロード済みの weather.yaml を指定します。

<img width="1042" height="1001" alt="09ChooseWeatherYaml" src="https://github.com/user-attachments/assets/3258ef5c-439d-4457-91f4-7d9871fe9fd3" />

10. weather.yamlがアップロードされ、"Validation successful"と表示されたのを確認します。[Next]をクリックします。

<img width="998" height="957" alt="10WeatherYaml-Validated" src="https://github.com/user-attachments/assets/db2a2151-7fff-4764-a0fc-f23ac570986d" />

11. Operationsと書かれている表にある、[current weather for corrdinates]という文字がある行に☑️を入れ、最後に[Done]をクリックします。

<img width="1042" height="1001" alt="11SelectOperations" src="https://github.com/user-attachments/assets/8ba0a062-0154-45fc-8e4f-a01522bb02fd" />

12. 画面の右上に「Tool Added」と表示されることを確認します。併せて、Toolset項目のTools内に、追加された[current weather for corrdinates]ツールが表示されていることを確認しましょう。これで、AIエージェントからツールが呼び出せます。

<img width="1042" height="1001" alt="12AddedTheTool" src="https://github.com/user-attachments/assets/579c0930-4c91-45a0-a023-c3d083d69e7f" />

13. Preview欄をリセットして、AIエージェントに「```あなたのできることを教えてください```」と質問します。
* もし「Hello!」と表示された場合は、もう一度「```あなたのできることを教えてください```」と質問します。

<img width="1042" height="1001" alt="13WhatCapability" src="https://github.com/user-attachments/assets/accb17d7-d6cc-44d0-8a9c-af6d14a595fd" />

14. Behaviorに指示を追加します。AIエージェントは、「Hello」で始まる定型の挨拶を省略します。
    * Instructions: ```回答は日本語で行なってください。 定型の挨拶は省略し、最初の質問から回答してください。```

<img width="1042" height="1001" alt="14SetBehaviors" src="https://github.com/user-attachments/assets/882ee0fc-e631-4823-af74-dbc4d9ed6935" />

15. チャット欄をリセットし、AIエージェントに「```東京都新宿区の天気は？```」と質問します。
    * もし緯度と経度を聞かれた場合は、「```緯度: 35.689、経度:139.692```」と追加で入力します。
    * ご注意: この挙動は、製品が使用しているシステム・プロンプトが、変数の値を勝手に想定、生成しないように (Never - Assume/make up values)、という指示を与えていることによるものです。
    * 緯度、経度の確認をスキップする方法として、BehaviorのInstructionsに書いておく方法があります。
    * 「ユーザーから都市の天気を問われた場合は、都市名から緯度と経度を想定して構いません。current_weather_for_coordinatesツールを呼び出して天気情報を取得してください。」

<img width="1178" height="1001" alt="15ShinjukuWeather" src="https://github.com/user-attachments/assets/c6d29cfb-1d8d-4365-a1b1-2dd465754358" />

16. 回答が得られたら、[Show Reasoning]をクリックし、ツールにどのようなパラメータが渡されたかを確認します。併せて、Outputの内容も確認しましょう。

<img width="1178" height="1001" alt="16WeatherReasoning" src="https://github.com/user-attachments/assets/6aeee7f8-8da7-4773-8abc-e63a5db87d13" />

17. 複数の地域の天気を比較する質問を使って、AIエージェントに自律的に考え、行動してもらいましょう。
* チャット欄をリセットし、AIエージェントに「```横浜と宇都宮ではどちらの方が涼しい？```」と質問します。
* ツールを使って気温を調べてくれない場合、AIエージェントに「```実行してください```」と入力します。

<img width="1178" height="1001" alt="17AgenticQA" src="https://github.com/user-attachments/assets/2ac1de88-91b3-4706-b8cf-d58a5a06331f" />

18. 3つの地域の気温を比較しましょう。
* チャット欄をリセットし、AIエージェントに「```静岡県沼津市、静岡県静岡市、静岡県浜松市の気温を表形式で比較してください。```」と入力します。
* AIエージェントがツールを使って* 気温を調べてくれない場合、AIエージェントに「```気温を表形式で比較してください。```」と入力します

<img width="1134" height="998" alt="18ComparedWithTable" src="https://github.com/user-attachments/assets/6cf4c8a2-a243-487e-897e-a1dc7c3cde8f" />

19. AIエージェントに応用問題を解いてもらいましょう。 
* チャット欄をリセットし、AIエージェントに「```明日の千葉の気温は、今日より2度高くなるらしいのですが、何度になりますか？```」と入力します。
* Agent styleがDefaultなので、うまく回答してくれません。

<img width="1178" height="1042" alt="19WeatherTomorrow01" src="https://github.com/user-attachments/assets/9dccb240-2a27-4841-b1b5-2ceeb00d13b5" />

20. Knowledge項目を選択し、[Agent style]を[ReAct]に変更します。
* チャット欄をリセットし、AIエージェントに「```明日の千葉の気温は、今日より2度高くなるらしいのですが、何度になりますか？```」と入力します。
* Think (考える） - Act　（行動する） - Observe　（観察する）という段階で、推論が実行されます。

<img width="1178" height="1042" alt="20WeatherTomorrow02" src="https://github.com/user-attachments/assets/25109ff0-84c0-448c-a5c9-e81ff8e8e2e4" />


続けて、[AIエージェントにツールとして、MCPサーバーを追加する](https://github.com/IBM/japan-technology/tree/main/watsonxOrchestrate/dojo/2/TimeMCP)に進みましょう。

