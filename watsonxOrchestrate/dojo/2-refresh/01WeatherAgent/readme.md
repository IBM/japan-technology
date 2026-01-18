# 1. 気象情報に回答するAIエージェントを作成する

* 最終更新日: 2026/01/18
* このコンテンツは、Business Automation Handsonコンテンツの内容を、若干発展させて最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。
[ソース](https://ibm.github.io/ba-handson-jp/wxoagent/tool/)

## このハンズオンの目的
AIエージェントは、ツールを利用することで、基盤モデルに備わっていない情報（例：リアルタイムの情報）を取得します。
このハンズオンでは、インターネットに公開されているAPIを用いて、ツールを定義して、AIエージェントから利用します。

* 利用するAPI: https://open-meteo.com/
* [オープンソース](https://github.com/open-meteo/open-meteo)で公開されている気象情報のAPI
* APIキー不要で使えます。
* AIエージェントのツールを定義する方法の体験目的で利用しており、業務用のプロダクション環境に展開することは想定していません。
* 使用権許諾についての詳細は、[こちら](https://open-meteo.com/en/licence)を参照してください。

0. watsonx Orchestrateを開きます。
URL: お使いの環境に合わせてwatsonx Orchestrateを開いてください。

* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat

* Welcome画面が表示されたら、"I'm here to build an AI Agent" をクリックします。
<img width="1223" height="1089" alt="2-1-0-Welcome" src="https://github.com/user-attachments/assets/cdcca54a-302d-4776-a81b-8411e17d3a49" />

* 左下のメニューから[Build]メニューをクリックし、[Agent Builder]を選択します。

1. 画面右手にある[Create new agent]をクリックします。
<img width="1223" height="1089" alt="2-1-1-CreateAgent" src="https://github.com/user-attachments/assets/7e4a56d5-59c8-4b6a-8f30-9444c1d21321" />

2. [Create from scratch]タブを選択し、NameとDescriptionを入力します。

* Name:
  ```
  WeatherInfo
  ```
* Description:
  ```
  指定された地名などを元に現在の天気の情報を取得し回答するエージェントです。
  ```

<img width="1223" height="1089" alt="2-1-2-WeatherAgent" src="https://github.com/user-attachments/assets/c7c9ba93-6f1d-4372-9c6c-fdb9f2ec9439" />

3. [Model deprecation notice]の画面が表示された場合は、[close]をクリックします。
* 今後は、GPT OSS-120Bを利用してください。
<img width="1223" height="1089" alt="2-1-3-ModelDeprecation" src="https://github.com/user-attachments/assets/38d513d2-4cfb-4e3d-8e0b-7f11feead07c" />

4. [Model]選択のドロップダウン・メニューから[GPT OSS-120B - OpenAI (via Groq)]を選択します。
<img width="1223" height="1089" alt="2-1-4-ChooseModel" src="https://github.com/user-attachments/assets/d67d3ebc-a8be-4e69-9672-b4a89b150c8d" />

5. 左側のメニューから[Behavior]をクリックし、[Instructions]を設定します。

* Instructions:
  ```
  回答は日本語で行なってください。
  ```
<img width="1223" height="1089" alt="2-1-5-Behavior" src="https://github.com/user-attachments/assets/b9c79005-161c-45dd-a7fe-bd3d28fcb6e6" />

6. Behaviorの指定が終わったら、チャット欄に「
  ```
  今日の静岡市の天気を教えてください。
  ```
  」と入力します。

<img width="1223" height="1089" alt="2-1-6-Sorry" src="https://github.com/user-attachments/assets/5e4c45c6-0149-4a85-a1bd-84ef8c0825b9" />

* この時点では、AIエージェントが適切なツールを呼び出せないため、天気の情報を取得することはできません。これは期待通りの動作なので、問題ありません。

7. 天気の情報をAIエージェントが取得できるように、ツールを追加します。左側のメニューから[Toolset]を選択し、[Add Tool+]をクリックします。

<img width="1223" height="1089" alt="2-1-7-AddTool" src="https://github.com/user-attachments/assets/5aef81c5-f762-4736-8943-0bf79626b247" />

8. [Add a tool]ウィンドウから、下側にある[MCP server+]をクリックします。

<img width="1223" height="1089" alt="2-1-8-MCPserver" src="https://github.com/user-attachments/assets/98f56739-351c-4cdf-8603-982df94661ee" />

9. [Add tool and manage MCP servers]から[Add MCP server]をクリックします。

<img width="1223" height="1089" alt="2-1-9-AddMCPserver" src="https://github.com/user-attachments/assets/d645c42d-0c4b-46b4-8e5a-a7fef685509a" />

10. [Add an MCP server]から[local MCP server]をクリックします。
* ここで言うローカル、とは、皆さんのローカル・コンピューターではなく、watsonx OrchestrateのSaaS環境内のコンピューターのことです。
* watsonx Orchestrateの実行環境内にMCP serverをインストールして実行することを意味します。

<img width="1223" height="1089" alt="2-1-10-LocalMCPserver" src="https://github.com/user-attachments/assets/34d4b8df-c9fe-4222-b61c-7c6ff4714840" />

11. [Add an MCP server]ウィンドウにインストールするMCP serverの詳細情報を入力します。入力を終えたら、[Import]をクリックします。

* Server name:
  ```
  Geocode
  ```

* Description: (後でMCP serverのメタ情報で上書きされるので、特に指定しなくても大丈夫です)
  ```
  都市名から緯度・経度を取得
  ```

* Install command: 
  ```
  npx -y @goecoding-ai/mcp
  ```

12. [Add tool and manage MCP servers]ウィンドウ内に「"Geocode" is ready.」の文字が表示され、ツールを選択できるようになります。

* [Geocode:geocode]という名前のツールを選択し、チェックボックスが有効になるのを確認します。
* [Add to agent]をクリックします。

<img width="1223" height="1089" alt="2-1-12-AddTools" src="https://github.com/user-attachments/assets/0d79a588-a234-494f-acee-040662b9e1f2" />

13. [Toolset]の[Tools]に[Geocode:geocode]ツールが表示されていることを確認します。

<img width="1223" height="1089" alt="2-1-13-Tools" src="https://github.com/user-attachments/assets/c723c14f-3d01-4a68-a428-60fcafd5bf8f" />

* このAIエージェントから、Geocodeツールを呼び出せるようになりました。

14. チャット欄で<img width="23" height="27" alt="2-1-14-reset" src="https://github.com/user-attachments/assets/4a9f8a7b-e614-4300-b7bf-bacca4c2dc91" />をクリックし、リセットします。

15. Geocodeツールのテストを実行します。

  チャット欄: 
  ```
  geocodeを使って、静岡市の緯度・経度を教えて
  ```
  <img width="1223" height="1089" alt="2-1-15-PromptGeocode" src="https://github.com/user-attachments/assets/32866fd0-f22f-4049-b64b-4588cd4a80bd" />


16. テスト結果を確認します。

  応答例:
  ```
  静岡市の緯度・経度は次の通りです。
  緯度 (latitude): 34.9751974
  経度 (longitude): 138.3831697
  ```
  <img width="1179" height="1045" alt="2-1-16-Geocoded" src="https://github.com/user-attachments/assets/523523b4-18fe-481b-9ed6-dfc086b279af" />
  
17. 左メニューから[Toolset]を選択し、[Tools]から[Add tool+]をクリックします。
    
<img width="1223" height="1089" alt="2-1-17-Addtool" src="https://github.com/user-attachments/assets/47700161-8d04-44e5-a5c6-556082530311" />

18. [Add a tool]から[OpenAPI]をクリックします。

<img width="1223" height="1089" alt="2-1-18-AddTool-OpenAPI" src="https://github.com/user-attachments/assets/3efa8b39-5072-415f-ae12-fbe1299aee8e" />

19. [Import tool]の画面が開きます。

* ツールを定義している OpenAPI 3.0.0準拠の仕様書
が入っているyaml形式のファイルを利用して、ツールを取り込みます。
* weather.yamlのダウンロード: こちらの[リンク](https://ibm.github.io/ba-handson-jp/wxoagent/files/weather.yaml)を右クリック (Macの場合、[control]を押しながらクリック)し、名前を付けて保存してください。
Upload filesの下にある、[Drag and drop an OpenAPI file here or click to upload]をクリックします。

 <img width="1223" height="1089" alt="2-1-19-ImportTool" src="https://github.com/user-attachments/assets/c3ec2644-6007-42ee-9834-c7c6b3dc4567" />

* 参考: YAML形式でOpenAPI 3 の完全な仕様書を作る場合は、インターネットから情報を取得する機能を備えた生成AIサービスに頼ると簡単です。
* プロンプトの例「watsonx Orchestrateのツールとして利用できるよう、open-meteoのforecast APIからOpenAPI 3.0の完全な仕様書を作ってください。」

* ツールを追加する際の注意点: 同じ名前のツールを複数登録しようとすると、名前の後ろに番号が付与されていきますのでご注意ください。
  Code Blockからツールの値を参照する際に、その番号も合わせて指定する必要が出てくるので、名前の後ろに番号が付与されないよう、ツールの名前を変更するなど、実装で工夫してください。

20. weather.yamlをアップロードすると、watsonx Orchestrateは、内容を検証します。
* 検証が完了すると"Validation successful"と表示されますので、[Next]をクリックします。
<img width="1223" height="1089" alt="2-1-20-Validated-yaml" src="https://github.com/user-attachments/assets/a013d12c-0f38-4b19-b38f-f25c48713d55" />

21. [Operations] というリストが表示されるので、[current weather for coordinates]にチェックを入れて、[Done]をクリックします。
<img width="1223" height="1089" alt="2-1-21-Operations" src="https://github.com/user-attachments/assets/256c6330-6657-48aa-b23c-f741ba114d22" />

22. しばらくすると、watsonx Orchestrateが気象ツールを取り込み、画面右上に[Tool Added]と表示します。
<img width="1223" height="1089" alt="2-1-22-ToolAdded" src="https://github.com/user-attachments/assets/b4c3266e-b9a0-4b5f-aa4c-09aa6ff868be" />

23. Open Meteoの気象APIで利用されているWMO （世界気象機関）の気象コードを解釈できるよう、簡単なテキストファイルを[Knowledge]として取り込みます。左側のメニューから[Knowledge]を選択し、[Add source +]をクリックします。
<img width="1223" height="1089" alt="2-1-23-AddSource" src="https://github.com/user-attachments/assets/a096b1f6-fc83-4db5-9452-7ea578e086f7" />

* テキストファイルのダウンロードは[こちら](https://raw.githubusercontent.com/IBM/japan-technology/refs/heads/main/watsonxOrchestrate/dojo/2-refresh/Weather.txt) を右クリック (Macの場合、[control]を押しながらクリック)し、名前を付けて保存してください。: 

24. [Add knowledge]から[New knowledge]をクリックします。
* ご注意: Existing knowledgeは、watsonx Orchestrateの環境に登録済みのデータを選択する場合に使います。
<img width="1223" height="1089" alt="2-1-24-NewKnowledge" src="https://github.com/user-attachments/assets/50fc79ae-65b7-49c4-86d8-8ececec354de" />

25. [Choose knowledge source]から[Upload files]を選択し、最後に[Next]をクリックします。
<img width="1223" height="1089" alt="2-1-25-Uploadfiles" src="https://github.com/user-attachments/assets/cf476389-b708-45da-9d3c-b95337acd4f8" />

26. [Drag and drop files here or click to upload]をクリックし、手順23でダウンロードしたWeather.txt(気象コードの説明が入ったテキストファイル)をアップロードします。ファイル名が表示されたことを確認して、[Next]をクリックします。

<img width="1223" height="1089" alt="2-1-26-AddKnowledge" src="https://github.com/user-attachments/assets/f4612f6a-1abf-40d5-9cc0-bbaa34161197" />

27. [Choose knowledge source]の画面から、詳細を入力し、[Save]をクリックします。

  Name: 
  ```
  WMO Weather Code
  ```

  Description: 
  ```
  WMO Weather Code マッピングテーブル
  ```

28. 左側のメニューから[Behavior]を選択し、[Instructions]を更新します。

  Instructions: 
  ```
  回答は日本語で行なってください。
  1.　[Geocode:geocode] ツールを使って、都市名から緯度・経度を取得してください。
  2.　[current weather for coordinates] ツールを使って、天気・気象情報を取得してください。この時current_weather = trueとしてください。
  3.　[current weather for coordinates] ツールから得られた、current_weatherオブジェクトの内容を気象情報として返してください。
  ```
  
  <img width="1432" height="1142" alt="2-1-28-Behavior" src="https://github.com/user-attachments/assets/9883e21b-38b0-447e-a55f-d289fae74892" />

29. チャット欄で<img width="23" height="27" alt="2-1-14-reset" src="https://github.com/user-attachments/assets/4a9f8a7b-e614-4300-b7bf-bacca4c2dc91" />をクリックし、リセットします。

30. AIエージェントに東京都新宿区の天気を質問します。回答を確認します。

回答例:
<img width="1432" height="1142" alt="2-1-30-WeatherResult" src="https://github.com/user-attachments/assets/14732d41-b20e-4d2a-b2cb-21958c977dfb" />

31. 回答が得られたら、[Show Reasoning]をクリックし、ツールにどのようなパラメータが渡されたかを確認します。併せて、Outputの内容も確認しましょう。

* Reasoningの例:
<img width="1432" height="1142" alt="2-1-31-Reasoning" src="https://github.com/user-attachments/assets/57223733-7b18-4885-85f4-d53e134e4f38" />

* Outputの例:

``` 
{
  "current_weather": {
    "interval": 900,
    "is_day": 1,
    "temperature": 9.9,
    "time": "2026-01-18T03:45",
    "weathercode": 0,
    "winddirection": 29,
    "windspeed": 3.7
  },
  "current_weather_units": {
    "interval": "seconds",
    "is_day": "",
    "temperature": "°C",
    "time": "iso8601",
    "weathercode": "wmo code",
    "winddirection": "°",
    "windspeed": "km/h"
  },
  "elevation": 45,
  "generationtime_ms": 0.06198883056640625,
  "latitude": 35.7,
  "longitude": 139.6875,
  "timezone": "GMT",
  "timezone_abbreviation": "GMT",
  "utc_offset_seconds": 0
}
```
 
32. 複数の地域の天気を比較する質問を試してみましょう。
* チャット欄をリセットし、AIエージェントに「
    ```
    横浜市と宇都宮市では、どちらの方が涼しい？
    ```
    」と質問します。

<img width="1432" height="1142" alt="2-1-32-Yokohama-Utsunomiya" src="https://github.com/user-attachments/assets/8a550ca8-f098-4b06-9b8a-0546cb91bd2f" />


33. 3つの地域の気温を比較しましょう。
* チャット欄をリセットし、AIエージェントに「
    ```
    静岡県沼津市、静岡県静岡市、静岡県浜松市の気温を表形式で比較してください。
    ```
    」と入力します。
    

<img width="1605" height="1142" alt="2-1-33-3CitiesInShizuoka" src="https://github.com/user-attachments/assets/317f823f-2ff9-43cb-a6f8-9f6be946c786" />

34. AIエージェントに応用問題を解いてもらいましょう。 
* チャット欄をリセットし、AIエージェントに「
   ```
   明日の千葉の気温は、今日より2度高くなるらしいのですが、何度になりますか？
   ```
   」と入力します。

<img width="1605" height="1142" alt="2-1-34-RelativeTemparature" src="https://github.com/user-attachments/assets/bde57ea7-eae9-4728-8936-281d4dea44d0" />


演習1は以上です。

## まとめ
この演習で体験したことを整理しておきましょう。

* MCP serverを利用して、都市名から緯度・経度情報を取得する
* Open-Meteoの気象APIをOpenAPIツールとして取り込み、緯度・経度から気象情報を取得する
* WMO気象コードの説明ファイルを知識として取り込み、気象コードの説明に利用する
* BehaviorのInstructionsを通じて、AIエージェントに期待する動作を指定する 

続けて、[気象情報を取得するワークフローを作成する](https://github.com/IBM/japan-technology/tree/main/watsonxOrchestrate/dojo/2/TimeMCP)に進みましょう。

