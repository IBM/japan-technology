Wifi Assistant

# ネットワーク（Wi-Fiパスワード案内）

* 最終更新日: 2025/11/10

## 全体像の確認

* ハンズオンのゴール: この会話フローを、プログラミングコードを書かずにWeb GUIの操作だけで構築することがゴールです。
* 使用するツール: このハンズオンではwatsonx Orchestrateの環境にログインし、その中でAI Assistant Builderという機能を使います。これは、AIとの対話（チャットボット）の流れを専門に作るためのツールです。
* Action（アクション)とは、AIアシスタントが実行できる『一つの仕事』の単位です。今回は『Wi-Fiパスワードを案内する』というActionを1つ作ります。

<img width="2633" height="2711" alt="Wi-Fiが繋がらない" src="https://github.com/user-attachments/assets/493092ec-fbc0-4cfb-bf46-f4e0204da6ec" />

##
1. watsonx Orchestrateを開き、左上のメニューから、[Build]-[Assistant Builder]を選択します。

※ お使いの環境に合わせてwatsonx Orchestrateを開いてください。
* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat

<img width="1098" height="1000" alt="01AssistantBuilder" src="https://github.com/user-attachments/assets/3807edcd-2fc7-4d97-ac31-afe6266a696e" />

2. 初回のアシスタント作成であるので、「Welcome to AI assistant builder」の画面を使って進めます。「Create your first assistant」の入力欄に次の内容を設定します。それぞれ設定したら、右上にある[Next]をクリックします。

* Assistant name:
  ```
  社内ヘルプデスク
  ```

* Description:
  ```
  社内の問い合わせに回答するアシスタントです。
  ```

* Assistant language:
  ```
  Japanese
  ```

  <img width="1098" height="1000" alt="02Create1stAssistant" src="https://github.com/user-attachments/assets/1f4f5d3a-813a-42ba-ae21-11939300d751" />

3. 続いて「Personalize your assistant」の画面が表示されます。Webサイトで動作するチャットボットを作成するので、デプロイ先は「Web」とします。Tell us about yourselfのところは、皆さんに適したものを選択してください。それぞれ設定したら、右上の[Next]をクリックします。

* Where do you plan on deploying your assistant?
  ```
  Web
  ```

* Which industry do you work in?
  ```
  Software
  ```

* What is your role on the team building the assistant?
  ```
  Developer
  ```

* Which statement describes your needs best?
  ```
  I want to provide confident answers to common questions.
  ```


<img width="1098" height="1000" alt="03PersonalizeYourAssistant" src="https://github.com/user-attachments/assets/0392094f-5eeb-47ef-9cb7-ac8834781d5e" />

4. 続いて「Customize your chat UI」の画面が表示されます。アシスタントの名前を設定します。他の項目は特に設定しなくて良いですが、好きなテーマや色を選んで、お好みの外観に仕上げましょう。設定が終わったら、右上の[Next]をクリックします。

* Assistant's name as known by customers:
  ```
  Webアシスタント
  ```
<img width="1098" height="1000" alt="04CustomizeYourChatUI" src="https://github.com/user-attachments/assets/3be74434-25cc-4981-8653-b789c8a6ee88" />

5. 続いて「Preview your assistant」の画面が表示されます。右上の[Create]をクリックします。
<img width="1098" height="1000" alt="05PreviewYourAssistant" src="https://github.com/user-attachments/assets/f21630b5-c232-4631-8a4f-17a3568bc677" />

6. ここからAIアシスタントの[Actions]を設定していきましょう。左上側にある[Home]メニューから[Actions]を選択します。
<img width="190" height="261" alt="06MenuAction" src="https://github.com/user-attachments/assets/a84a8046-eebd-4325-a363-0d736d186cdf" />

7. 「Actions」の画面が開きました。まだ何もアクションを設定していないので、画面中央にある[Create action +]をクリックします。
<img width="1148" height="1000" alt="07CreateYour1stAction" src="https://github.com/user-attachments/assets/6a88990c-080a-4edf-bde5-b7e70b5d0834" />

8. 「What kind of action do you want to build?」の画面が表示されます。大きなタイルで表現されている[Custom-built action]をクリックします。
<img width="1148" height="1000" alt="08CustomBuiltAction" src="https://github.com/user-attachments/assets/5118c695-1fc8-4789-ba5f-f3e92a382e06" />

9. 「New action」の画面が開きます。ここでは、AIアシスタントの起動フレーズ「Wi-Fiが繋がらない」を登録し、[Save]をクリックします。

* What does your customer say to start this interaction?
  ```
  Wi-Fiが繋がらない
  ```
<img width="1148" height="1000" alt="09NewAction" src="https://github.com/user-attachments/assets/a4ad734b-3d82-4523-aab0-9f3c97ed72c8" />

10. Editorが開くので、「Wi-Fiが繋がらない」という問い合わせから出発するアクションを定義します。
<img width="1148" height="1000" alt="10Editor" src="https://github.com/user-attachments/assets/5a2027e1-28c3-4430-a4e6-864b1d27ab57" />

11. 「Customer start with:」と書かれたタイルの下側にある [v]をクリックし、内容を展開します。
<img width="282" height="155" alt="11Expand-StartWith" src="https://github.com/user-attachments/assets/7a02b5d3-c80a-41b6-87da-d8ecef98de80" />

12. 「Customer start with:」と書かれたタイルが大きく表示され、右側には、[Display name]、[Add example phrases:]が表示されています。
<img width="1148" height="1000" alt="12DisplayName-Examples" src="https://github.com/user-attachments/assets/537a4109-a551-44b8-aa1a-3bd58278e63b" />

13. 必要な項目を入力します。
* Display name:
  ```
  ネットワーク（Wi-Fiパスワード案内）
  ```

* Add example phrases: １行ずつ入力してください
  ```
  Wi-Fiパスワード
  ```
  
  ```
  無線LANのパスワード
  ```

  ```
  wifi password
  ```

  ```
  社内ネットワーク つながらない
  ```

* Add example phrasesを入力する理由は、問い合わせするユーザーがどのような言い回し（例：Wi-Fiパスワード、wifi password）で質問してきても、watsonx Orchestrateが『これはWi-Fiパスワードの質問だ』と賢く理解できるように、AIの『辞書』に言葉を登録しています。これを自然言語理解（NLU）のトレーニングと呼びます。
  
<img width="1151" height="983" alt="13Filled-DisplayName-Examples" src="https://github.com/user-attachments/assets/0b76414b-fc30-40f1-a200-b707ef6a37a9" />

14. 必要な入力を終えたら、左側に表示されている[Conversation steps]の下にある[1]のタイルをクリックします。
<img width="289" height="312" alt="14ToStep1" src="https://github.com/user-attachments/assets/2c5d29e6-5725-45db-8953-e953b6cc7b2a" />

15. 右側の画面に[Step 1]と表示されたことを確認します。このステップの画面では、AIアシスタントが発する言葉(Assitant says)、ユーザーからの応答の定義(Define customer response)、次に何をするか(And then)の設定ができます。
<img width="1151" height="983" alt="15Step1-init" src="https://github.com/user-attachments/assets/82231d69-971e-46cd-b658-4f7b6b164b32" />

16. [Assistant says]を入力し、[Define customer response]をクリックします。

* Assistant says: 
  ```
  今どのオフィスにいますか？
  ```
<img width="539" height="224" alt="16DefineCustomerResponse" src="https://github.com/user-attachments/assets/baddf44b-ed9f-4f2b-895c-c33182c41634" />

17. [Define customer response]の画面に表示される[Options]を使って、回答用の選択肢を作成します。[Options]の下に表示されている[As buttons]のところをクリックします。
<img width="1151" height="983" alt="17Options" src="https://github.com/user-attachments/assets/cff4d856-4036-4dfe-8ce7-21b1c8eea48e" />

* なぜ自由入力（Free text）ではなく選択肢（Options）を使うのか？：この後のステップで、『もし箱崎が選ばれたら、箱崎オフィスのパスワードを教える』という条件分岐を行いたいからです。選択肢にすることで、ユーザーの回答をAIアシスタントが100%正確に認識できます。

18. [Edit response]の画面が表示されるので、[Option 1]から[Option 3]をそれぞれ入力し、最後に[Apply]をクリックします。

* Option 1: 
  ```
  箱崎
  ```

* Option 2: 
  ```
  虎ノ門
  ```

* Option 3: 
  ```
  その他
  ```

<img width="1151" height="983" alt="18EditResponse" src="https://github.com/user-attachments/assets/afb7b31e-3cfa-46a1-81e4-70a71b3d9fa9" />

19. 設定した[Options]が表示されていることを確認し、[Edit response]と同じ行にある[Save response for reuse]アイコンをクリックします。
<img width="535" height="277" alt="19SaveResponseToReuse" src="https://github.com/user-attachments/assets/1c1e216e-a9c6-418b-98d6-17eb73d8d79c" />


20. 「New saved response」の画面が表示されます。[Name]項目を入力して、[Apply]をクリックします。
* Name (required): 
  ```
  その他
  ```

<img width="1151" height="983" alt="20NewSavedResponse" src="https://github.com/user-attachments/assets/35650faa-a8ce-484a-9064-87cb52dd8680" />

21. 画面右下の[Preview]をクリックし、AIアシスタントの動作を確認しましょう。
* ご用件をお伺いいたします。: 
  ```
  繋がらない
  ```

* 今どのオフィスにいますか？:
  ```
  虎ノ門
  ```

<img width="1151" height="983" alt="21Preview" src="https://github.com/user-attachments/assets/d6637b78-bc33-43ed-b8b0-3a5eba3a356f" />

* このアクションはまだ完成していないので、Preview画面内に「There are no additional steps for this actions.  Add a new step or end the action.」と表示されます。

22. [Preview]画面にある[-]をクリックして、チャット・ウィンドウを閉じます。
<img width="320" height="40" alt="22CloseChatWindow" src="https://github.com/user-attachments/assets/928fc059-68c7-425e-a417-a177c311b189" />

23. 左側にある[Conversation steps]欄の下側にある[New step +]をクリックします。
<img width="1151" height="983" alt="23PreviewClosed-NewStep" src="https://github.com/user-attachments/assets/6d47988f-40a4-4d7c-8d20-f94a22de36e1" />

24. [Step 2]のEditorが開いたら、[Is taken]と表示されている右側にあるドロップ・ダウン・リストボックスを開き、下側にある[with conditions]を選択します。
<img width="1151" height="983" alt="24-Step2-WithCondition" src="https://github.com/user-attachments/assets/df447ed6-5fd0-4805-a96c-1b298166606b" />

25. [Conditions]のところが展開されます。if [All] of this is true: と書かれている下の行を確認します。条件が次のようになっていることを確認してください。

* [1. 今どのオフィスにいますか？] [is] [箱崎]

[Step 1]の回答が[箱崎]の場合に限って、このアクションが実行されます。

確認ができたら、Assistant says:を入力します。（ご注意:このパスワードは架空のものです）

* Assistant says:
  ```
  箱崎オフィスのWi-Fiパスワードは「HZ1234#56!」です。
  ```

<img width="988" height="580" alt="25-Step2-Condition-AssistantSays" src="https://github.com/user-attachments/assets/50767e63-2626-4787-9150-2cc31fa48e84" />

26. [And then]の下にある[Continue to next step]をクリックし、[End the action]を選択します。これにより、AIアシスタントはユーザーからの問い合わせに対するアクションを終了します。
<img width="984" height="780" alt="26-Step2-EndTheAction" src="https://github.com/user-attachments/assets/16a6c396-dfb5-4eee-8b6c-793579301515" />

27. [Preview]をクリックして、AIアシスタントの動作を確認しましょう。

* ご用件をお伺いいたします。: 
  ```
  WiFi
  ```

* 今どのオフィスにいますか？:
  ```
  箱崎
  ```
<img width="355" height="529" alt="27-Step2-PreviewV2" src="https://github.com/user-attachments/assets/fed5f52d-5c4f-43bf-af71-4aa56fd8c0b7" />

28. 手順23と同様に左側にある[Conversation steps]欄の下側にある[New step +]をクリックします。[Step 3]のEditorが開いたら、[Is taken]と表示されている右側にあるドロップ・ダウン・リストボックスを開き、下側にある[with conditions]を選択します。

* Conditions内に表示されているオフィスの[Options]項目から、[虎ノ門]を選択します。

<img width="660" height="329" alt="28-Step3-ChooseOffice" src="https://github.com/user-attachments/assets/585093db-0ef1-4c80-973e-b5fc36a6b201" />

29. [Step 3]の[Assistant says]を入力します。[And then]の下にある[Continue to next step]をクリックし、[End the action]を選択します。

* Assistant says:（ご注意:このパスワードは架空のものです）
  ```
  虎ノ門オフィスのWi-Fiパスワードは「TR7171#48!」です。
  ```

<img width="894" height="772" alt="29-Step3-New" src="https://github.com/user-attachments/assets/3bd38af1-7365-462b-8ee3-0a70823feaf6" />

30. [Preview]をクリックして、AIアシスタントの動作を確認します。

* ご用件をお伺いいたします。: 
  ```
  ネットワーク
  ```

* 今どのオフィスにいますか？:
  ```
  虎ノ門
  ```
<img width="368" height="530" alt="30-Step3-Preview" src="https://github.com/user-attachments/assets/91aa2555-a14d-4e2b-aafc-0d7e64da47d3" />

* もしPreviewで虎ノ門と入力しても虎ノ門オフィスのパスワードが表示されない場合、ステップ28のConditionsの設定（1. 今どのオフィスにいますか? is 虎ノ門）が正しいか確認しましょう。

31. 手順23、28と同様に左側にある[Conversation steps]欄の下側にある[New step +]をクリックします。[Step 4]のEditorが開いたら、[Is taken]と表示されている右側にあるドロップ・ダウン・リストボックスを開き、下側にある[with conditions]を選択します。[Assitant Says]、[And Then]を設定します。

* Conditions内に表示されているオフィスの[Options]項目から、[その他]を選択します。

* Assistant says:（ご注意:このパスワードは架空のものです）
  ```
  そのほかのオフィスのWi-Fiパスワードは「GN5963#41!」です。
  ```
* And Then:
  ```
  End the action
  ```
<img width="989" height="785" alt="31-Step4-SetAll" src="https://github.com/user-attachments/assets/6f2de719-db1a-4cfd-adc1-2529503bdca6" />

32. [Preview]をクリックし、AIアシスタントの動作を確認します。
<img width="367" height="533" alt="32-Step4-Preview" src="https://github.com/user-attachments/assets/65130a13-b606-45cd-9a9d-4175d6062ccc" />


* ご用件をお伺いいたします。: 
  ```
  パスワード
  ```

* 今どのオフィスにいますか？:
  ```
  その他
  ```

33. 最後にEditorの右上にある[x]をクリックして、アクション一覧画面に戻ります。
<img width="1208" height="317" alt="33-Actions-List" src="https://github.com/user-attachments/assets/54a60964-31ce-487b-bf5d-07951cfa1b6f" />

おめでとうございます！これで、『お客様の質問の意図を理解し』『選択肢で回答を誘導し』『条件に応じて異なる回答を返す』という、チャットボットの最も重要な基本ロジックを完成できました。

[次の演習](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/3/PCFailureAssistant/readme.md)に進んでください。

