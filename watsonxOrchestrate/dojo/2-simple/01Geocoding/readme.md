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

<img width="1073" height="1068" alt="2-1-7-AddTool" src="https://github.com/user-attachments/assets/45661ffe-7ea7-47ce-b002-ad8cdc2429f5" />

8. [Add a tool]から[Agentic workflow]をクリックします。

<img width="1073" height="1068" alt="2-1-8-AgenticWorkflow" src="https://github.com/user-attachments/assets/6779abc3-0d59-46c0-9e45-61bae88065d9" />

9. [Name your agentic workflow]に名前を付けます。[Name]を入力し、[Start building]をクリックします。
* Name:
   ```
   WeatherFlow
   ```
   
<img width="1073" height="1068" alt="2-1-9-NameTheFlow" src="https://github.com/user-attachments/assets/26b1aef0-5f65-4c81-a8bc-aa7a2e614d94" />

10. ブラウザーの横幅を調整し、フロー画面が見えるように位置を調整します。[WeatherFlow]の下にある [x]印をクリックすると[Flow nodes]の画面が消えるので、適宜利用してください。

<img width="1091" height="1068" alt="2-1-10-AdjustFlowlayout" src="https://github.com/user-attachments/assets/afb93fe8-bc5f-4206-be8b-4f0f270cff0c" />

11. [Flow nodes]タブにある[Generative prompt]を見つけ、マウスでドラッグし、フローの[Add +]につなげます。

<img width="1091" height="1068" alt="2-1-11-GenerativePrompt" src="https://github.com/user-attachments/assets/4c235834-d1d2-43b0-9640-ff60bca4ff9a" />

<img width="1884" height="1162" alt="2-1-11-1-DragDrop" src="https://github.com/user-attachments/assets/fc935bbc-d9e0-4dee-a2f3-78d8776ad307" />

12. [Generative prompt]の画面が表示されます。左側にある[Add +]をクリックします。

<img width="1091" height="1068" alt="2-1-12-GenPrompt-AddInput" src="https://github.com/user-attachments/assets/c7d719e8-ab84-4b77-a2df-39b459efe9b7" />

13. ドロップダウン・リストから[String]を選びます。

<img width="207" height="229" alt="2-1-13-AddString" src="https://github.com/user-attachments/assets/abc08d38-f9e2-4592-b4a4-f9daa1629271" />

14.　[Add string input variable]に[Name]と[Description]を入力し、[Add]をクリックします。

* Name: 
   ```
   city_name
   ```

* Description:
   ```
   都市名
   ```
   
<img width="1047" height="1024" alt="2-1-14-AddStringInput" src="https://github.com/user-attachments/assets/acbd1a8d-9168-4481-a160-3b0c3a0b16e9" />

15. 追加された (city_name) の右側にある Enter a test ... をクリックします。

<img width="1091" height="1068" alt="2-1-15-Input-Cityname" src="https://github.com/user-attachments/assets/04b9e776-3539-4a9b-8356-502bd1a5302e" />

16. テスト文字列を追加します。

16-1. 編集アイコンが見えるので、クリックします。

<img width="262" height="64" alt="2-1-16-1-TestString-Edit" src="https://github.com/user-attachments/assets/f4974555-9574-470a-882b-2943accabc05" />

16-2. 入力欄が現れたら、テスト文字列を入力します。
* テスト文字列:
   ```
   静岡市
   ```
   
   <img width="1091" height="1068" alt="2-1-16-2-TestString" src="https://github.com/user-attachments/assets/cba9e3e8-4ef1-4525-abe9-4227db5198c3" />

16-3. チェックマーク (Accept the test string)をクリックします。

* 操作しづらい場合は、ブラウザーの倍率を80-90%などに変えてください。
<img width="328" height="179" alt="2-1-16-3-Accept" src="https://github.com/user-attachments/assets/15c88603-fb9e-4452-8daa-8548c1864df1" />

16-4. テスト文字列が入力できたことを確認します。

<img width="1091" height="1068" alt="2-1-16-4-Accepted" src="https://github.com/user-attachments/assets/df059318-80b9-494a-8f2e-7671f06ce428" />

17. [User prompt]を入力します。
* User prompt:
   ```
   与えられた {city_name}を使って、緯度、経度、国コード(ISO 3166-1 alpha-2)を調べて
   ```

<img width="1091" height="1068" alt="2-1-17-UserPrompt" src="https://github.com/user-attachments/assets/df942414-3d48-4a83-9ee5-15b069d496d3" />

18.　入力パラメーターの確認を行います。
18-1. {city_name} は (city_name)と水色背景の枠内に表示されます。User prompt欄にある [{x}}をクリックしましょう。

<img width="585" height="185" alt="2-1-18-Variables" src="https://github.com/user-attachments/assets/7259e353-6e8c-462c-a61e-280ce6cedaef" />

18-2 フロー変数 (Flow vairables)が表示され、[Generative prompt]の[city_name]入力変数が指定されていることがわかります。

<img width="1091" height="1068" alt="2-1-18-2" src="https://github.com/user-attachments/assets/9fbc5903-74f6-41f5-90f4-8602d7614dc3" />

19. このプロンプトの出力結果をObject型でアクセスできるようにしましょう。[Output as Object]のスイッチをオンにします。

<img width="1091" height="1068" alt="2-1-19-OutputAsObject-on" src="https://github.com/user-attachments/assets/3f4594b6-d8c6-4f4c-bf0f-9b88c6cd0bfe" />

20. [Create an object output]の画面で、出力内容を定義していきましょう。

20-1. 出力の名前 [Name]を入力します。
* Name:
   ```
   output
   ```

<img width="1091" height="1068" alt="2-1-20-1-Name" src="https://github.com/user-attachments/assets/540109f7-4b50-4281-a79b-8e667ff8b0ad" />

20-2. 画面左側にある [{} output] の右側にある[+]をクリックします。ドロップダウン・リストから[Decimal]を選びます。

<img width="1091" height="1068" alt="2-1-20-2-Decimal" src="https://github.com/user-attachments/assets/2d06df11-006c-41df-a3e6-27ce0015a949" />

20-3. プロパティの[Name]と[Description]を入力します。
* Name:
   ```
   latitude
   ```

* Description:
   ```
   緯度
   ```

<img width="1047" height="1024" alt="2-1-20-3-latitude" src="https://github.com/user-attachments/assets/edf425fc-6b46-4ca1-8ff5-7cfd94401ff0" />

20-4. 同様の方法で、緯度を表すDecimal型の変数を追加します。
* Name:
   ```
   longitude
   ```

* Description:
   ```
   経度
   ```

<img width="1091" height="1068" alt="2-1-20-4-longitude" src="https://github.com/user-attachments/assets/ff012df4-1a8d-4eda-9cc1-45572c0ab8f1" />


20-5. 同様の方法で、国コードを表すString型の変数を追加します。

* Name:
   ```
   country_code
   ```

* Description:
   ```
   国コード
   ```
<img width="1047" height="1024" alt="2-1-20-5-country_code" src="https://github.com/user-attachments/assets/e780f98b-4dd4-40af-8d2d-f8ec502589c2" />

20-6. [JSON view]をクリックして、正しくオブジェクトが定義されているかどうかを確認しましょう。問題なければ[Save]をクリックします。

<img width="1091" height="1068" alt="2-1-20-6-JSON-view" src="https://github.com/user-attachments/assets/aec04fc5-5893-42d8-ac39-1e8a8ce81e90" />

21. このプロンプトをテストします。右下にある[Generate Preview]をクリックします。

<img width="1091" height="1068" alt="2-1-21-Gen-Preview" src="https://github.com/user-attachments/assets/19d24a8e-ce30-4edc-a88f-425856df2527" />

22.　生成結果を確認します。静岡市の緯度、経度、国コードが表示されます。

* 生成例:
```
{
  "latitude": 34.9756,
  "longitude": 138.3828,
  "country_code": "JP"
}
```

<img width="1091" height="1068" alt="2-1-22-Geocoded" src="https://github.com/user-attachments/assets/32110872-e2e3-4d12-8ccb-5007c22e0aff" />

* 表示されない場合、これまでの手順12から20-6までを確認してください。もし[Input]が見えない場合、[Define prompts]タブをクリックしてください。

23. [Generative prompt]画面の右上にある[x]をクリックして、フロー全体の画面に戻ります。

<img width="1091" height="1068" alt="2-1-23-Close" src="https://github.com/user-attachments/assets/8acae3c2-c660-4364-8764-85394d3967d4" />

24. 左上 [WeatherFlow] の右側にある [Edit details]をクリックします。

<img width="1091" height="1068" alt="2-1-24-EditDetails" src="https://github.com/user-attachments/assets/c43efcc2-72ea-45a0-bf5a-ac0d4e7bf453" />

25. WeatherFlowの概要ページが開きます。Descriptionを入力します。

* Description:
   ```
   与えられた都市名から緯度、経度、国コードを調べます
   ```
<img width="1047" height="1024" alt="2-1-25-Overview" src="https://github.com/user-attachments/assets/2e078ea3-0942-404d-b75e-5bab0626032b" />

26. [Parameters]タブに切り替えます。[Add input +]をクリックし、[String]を選択します。

<img width="1091" height="1068" alt="2-1-26-AddInput" src="https://github.com/user-attachments/assets/4e207675-37ae-4ec5-8043-399d612c421a" />

27. [Add string input]に[Name]と[Description]を入力します。最後に[Add]をクリックします。

* Name: 
   ```
   city_name
   ```

* Description:
   ```
   都市名
   ```
   
   <img width="1091" height="1068" alt="2-1-27-cityname" src="https://github.com/user-attachments/assets/b1287f2f-859c-4c59-9590-32ae167c6aac" />

28. 入力パラメータが1つ定義できたことを確認し、[Done]をクリックします。

<img width="1047" height="1024" alt="2-1-28-Done" src="https://github.com/user-attachments/assets/bb3f6689-c89e-4942-9ed1-9647b5ec132f" />

29. [Generative prompt]の名前を[Geocode]に変更します。[Generative prompt]をクリックし、表示されたウィンドウの上側にある編集アイコンをクリックします。

<img width="1091" height="1068" alt="2-1-29-Edit" src="https://github.com/user-attachments/assets/bb3d4b78-7fbf-4755-bc70-96b010e19c78" />

30.　名前を Geocode と入力します。
* 名前: 
   ```
   Geocode
   ```

   <img width="443" height="380" alt="2-1-30-Geocode" src="https://github.com/user-attachments/assets/023f77e6-21e9-48e5-b8e2-d8f0a48d0cf5" />

31. フロー内のGenerative promptの名前が[Geocode]に変わったことを確認して、右上の[Done]をクリックします。

<img width="1091" height="1068" alt="2-1-31-Flow-Done" src="https://github.com/user-attachments/assets/e0a15df0-e8ba-4096-9f4c-38291bcfc591" />

32. 作成したフローをテストしましょう。チャット欄に次のプロンプトを入力します。
* プロンプト:
   ```
   静岡市の位置情報を教えて
   ```
* 応答例:
```
静岡市の位置情報は以下の通りです。

- 緯度 (latitude): 34.9756  
- 経度 (longitude): 138.3828  
- 国コード (country code): JP  

ご参考になれば幸いです。
```
<img width="1091" height="1068" alt="2-1-32-test1" src="https://github.com/user-attachments/assets/8449a044-3572-43f4-b238-bb8a6ff936a3" />

33. 別のプロンプトでテストしましょう。
* プロンプト:
   ```
   浜松市、静岡市、沼津市の位置情報を教えて
   ```
* 応答例:

以下にご指定いただいた3つの市の位置情報をまとめました。

| 市名 | 緯度 (latitude) | 経度 (longitude) | 国コード (country code) |
|------|-----------------|------------------|--------------------------|
| 浜松市 | 34.7108 | 137.7260 | JP |
| 静岡市 | 34.9756 | 138.3828 | JP |
| 沼津市 | 35.1069 | 138.8648 | JP |

##
演習は以上です。
続いて、[気象情報を取得するワークフローを作成する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2-simple/02WeatherFlow/readme.md)に進んでください。

## まとめ
* この演習では、基盤モデルの知識を使って、位置情報を提供するフローを作成しました。
* watsonx Orchestrateの基盤モデルがGPT-OSS 120Bになったことで、基盤モデルの知識も活かしながらAIエージェントを開発できます。
