## granite-8b-japanese 言語モデルを使い、構造化されたプロンプトを改良しながら、地方の魅力を伝えるための文章を生成する
IBM watsonx.aiのプロンプト・ラボを使い、静岡県の魅力を伝えるための文章を作ってみましょう。
出来上がったプロンプトは、プロンプト・テンプレートとして保存し、その後、Watson Machine Learningを使って、Webサービスとしてデプロイします。

参考URL: 
* [プロンプト・ラボ](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-prompt-lab.html?context=wx&locale=ja "Prompt Lab")
* [プロンプト・テンプレートのデプロイ](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/prompt-template-deploy.html?context=wx&locale=ja "Deploy prompt template")


免責事項: 生成AIは事前学習したデータを活用しながらテキストを生成します。言語モデルに含まれている言葉が確率で選択されるため、生成AIは事実と異なる結果を生成する場合があります。このハンズオンでは、段階的にプロンプトを改善するため、途中、意図しない結果を敢えて得ることも行います。生成AIのハルシネーションから間違った内容が伝わらないよう、生成された内容をそのまま利用するのではなく、必ず、事実確認を行なってください。

前提条件:
* IBM watsonx 上に新規プロジェクト「Dojo #3」を作ってあること ([作成方法](https://github.com/IBM/japan-technology/tree/main/watsonx.ai/dojo/create-new-project "Create New Project"))

<img width="1524" alt="wxai03-00-newProject" src="https://github.com/user-attachments/assets/3a3a0179-c655-4c57-bc22-b90e15a7da5c">

プロジェクト作成後は、Watson Machine Learningの関連付けを確認してください。
<img width="1524" alt="wxai03-00-associatedML" src="https://github.com/user-attachments/assets/5b3248b6-9683-454b-9ed6-99e439928eff">

##

1. Webブラウザーから https://jp-tok.dataplatform.cloud.ibm.com/projects/?context=wx へアクセスして、プロジェクト一覧を開きます。
  <img width="1521" alt="wxai03-02-01-projectList" src="https://github.com/user-attachments/assets/b70b3dc3-61e4-40c1-8636-17e28803b911">

2. 「Dojo #3」を見つけて、リンクをクリックします。
  <img width="1521" alt="wxai03-02-02-dojo03" src="https://github.com/user-attachments/assets/1f413bc5-d7e9-41e1-a2b9-84f2192a4b6d">

3. 「Dojo #3」の概要ページから、作業の開始欄にある[ファウンデーション・モデルを使用したチャットとプロンプトの作成]をクリックします。
  <img width="1521" alt="wxai03-02-03-toPromptLab" src="https://github.com/user-attachments/assets/f818db7a-40f1-4c38-9bcb-f091b883f6e3">

4. プロンプト・ラボが開いたら、[構造化」をクリックします。（ご注意：最後にプロンプト・ラボを操作した時にチャット、構造化、フリー・フォームのどの画面で利用していたかによって状況が変わります。）モデル: [granite-8b-japanese] を選択してください。

  <img width="1521" alt="wxai03-02-04-Structured" src="https://github.com/user-attachments/assets/fc8924bd-56c0-44d4-8c22-61adf8e04d8c">

5. セットアップ欄の[命令 (オプション)]のところに、次のテキストを入力します。
```
あなたは素晴らしいマーケティング・スペシャリストです。日本全国各地の魅力を発信するための文章を作ります。その土地や文化を知らないけれど、有名な芸能人やメーカー名、誰もが知っている名所、美味しい食事などの話を紹介しながら、その地方への旅行を大歓迎する文章を考えてください。
```

<img width="1521" alt="wxai03-02-05-instruction" src="https://github.com/user-attachments/assets/4094e158-88a7-4073-b2ae-7d435ccf7b99">

6. 試行欄にある[プロンプトのテスト]の下にある[入力]に、次のテキストを入力します。
```
静岡県を知らない人に向けて、静岡県への旅行をお勧めする文章を作ってください。例があればその例を参考にして、次の「見出し一覧」にある項目を含めて書いてください。文章の最後は「魅力あふれる静岡県にお越しください！」としてください。同じ内容を繰り返さないでください。

「見出し一覧」:
- 静岡県にある観光名所3ヶ所
- 静岡県出身の有名人、芸能人4人
- 静岡県で有名なレストラン3つ
- 静岡県がモデルとなっているアニメ作品3つ
```
<img width="1521" alt="wxai03-02-06-testPromptV2" src="https://github.com/user-attachments/assets/cc5dc718-7823-42da-80c2-6b9e6e5afe0a">


7. 画面の右上側にあるモデル・パラメータ <img width="54" alt="wxai03-01-09-modelParameters" src="https://github.com/user-attachments/assets/ac1843cb-9473-4f17-9b4d-fae32a3e0ae7">をクリックして、モデル・パラメータの小さなウィンドウ内に３つのパラメータを設定します。
* シーケンスの停止: ```↵↵``` (Enterキーを2回押す。その後 [+]をクリックしてシーケンスの追加を実行する)
<img width="277" alt="wxai03-02-06-addSequence" src="https://github.com/user-attachments/assets/fbeae205-5d13-4ea3-92ba-1802c0507fb1">

* 最小トークン数: ```450```
* 最大トークン数: ```500```

<img width="288" alt="wxai03-02-modelParamOptimized" src="https://github.com/user-attachments/assets/57a3653d-d35d-4c24-a922-6b1ff8174339">


8. 画面右下の[生成]をクリックします。

<img width="1397" alt="wxai03-02-08-v3-generated" src="https://github.com/user-attachments/assets/34c2bdd2-86e6-4720-b9f6-c5f8771b3aa1">


生成例を貼っておきます。この内容には事実と異なる情報が含まれていますので、ご注意ください。
```
静岡県は、富士山や伊豆半島などの美しい自然景観、徳川家康公が築いた歴史的な遺産、伊豆や熱海などの温泉など、魅力的な観光資源に恵まれています。また、お茶やみかんなどの特産品も豊富です。静岡県出身の有名人では、歌手の大石恵理子さん、俳優の哀川翔さん、お笑い芸人のなすびさんなどがいらっしゃいます。静岡県で有名なレストランでは、さわやか御殿場インター店、さわやか静岡インター店、さわやか浜北店などが人気です。また、静岡県をモデルとしたアニメ作品としては、「ゆるキャン△」や「ちびまる子ちゃん」などが有名です。魅力あふれる静岡県にお越しください！


静岡県にある観光名所3ヶ所

1. 富士山：静岡県と山梨県に跨る日本最高峰の独立峰で、標高3776m。日本を象徴する山として、多くの観光客が訪れます。

2. 伊豆半島：静岡県東部にある半島で、温泉や海、自然景観など、多くの観光資源に恵まれています。

3. 修善寺：伊豆半島中部に位置する温泉街で、伊豆最古の温泉と言われています。

静岡県出身の有名人、芸能人4人

1. 大石恵理子さん：歌手、女優

2. 哀川翔さん：俳優

3. なすびさん：お笑いタレント

4. 駿河太郎さん：俳優、ミュージシャン

静岡県で有名なレストラン3つ

1. さわやか御殿場インター店：静岡県内に展開するファミリーレストランで、げんこつハンバーグが有名。

2. さわやか静岡インター店：同じくさわやかレストランで、げんこつハンバーグランチが人気。

3. さわやか浜北店：同じくさわやかレストランで、げんこつハンバーグランチが人気。

静岡県がモデルとなっているアニメ作品3つ

1. ゆるキャン△：女子高生がキャンプをしたり、アウトドアを楽しんだりする様子をゆるやかに描いたアニメ。静岡県がモデルの場所がいくつか登場します。

2. ちびまる子ちゃん：静岡県清水市を舞台にしたアニメで、まる子や友蔵、家族の日常が描かれています。

3. 徳川家康：江戸幕府を開いた徳川家康の生涯を描いたアニメ。静岡県浜松市がモデルの場所が登場します。
```
9. ここからFew Shotプロンプティングを試していきましょう。言語モデルに含まれていない知識を３つ、例として、追加していきます。
※ ここで追加している内容は、プロンプト・エンジニアリングの作業例として取り上げているだけに過ぎず、出力に含まれている内容と、著者や著者の所属企業とは一切関係がありません。

入力:
```
静岡県の有名なレストランを３つ教えてください。
```

出力:
```
・炭焼きレストランさわやか (げんこつハンバーグ料理が大人気)
・中華ファミリーレストラン五味八珍（中華料理、浜松餃子が大人気）
・元祖丁子屋（とろろ汁が大人気）
```

例を増やすために、[例の追加 +]をクリックします。

入力:
```
静岡県出身の有名人、芸能人を4人教えてください。
```

出力:
```
・広瀬すず  (静岡県静岡市清水区出身）
・長澤まさみ （静岡県磐田市出身）
・百田夏菜子  （静岡県浜松市出身）
・久保田利伸 (静岡県静岡市清水区、旧清水市出身)
```

さらに例を増やすために、[例の追加 +]をクリックします。
入力:
```
静岡県がモデルとなっているアニメ作品を３つ教えてください。
```

出力:
```
・「ラブライブ！サンシャイン！！」　聖地は、静岡県沼津市が中心です。伊豆・三津シーパラダイスも有名で、多くのファンが訪れています。
・「ちびまる子ちゃん」静岡県静岡市清水区（旧清水市）がモデルになっています。エスパルス・ドリームプラザ内に「ちびまる子ちゃんランド」があり、多くのファンが訪れています。
・「シュート！」静岡県掛川市がモデルとなったサッカー漫画です。作品内の掛川高校は、掛川西高校がモデルと言われています。
```


<img width="1398" alt="wxai03-02-09-v3-Examples" src="https://github.com/user-attachments/assets/b5bd1203-33bc-48e0-8692-ca1783665bf7">



10. [出力のクリア]をクリックしてから、画面右下の[生成]をクリックします。上記手順8の結果と異なることを確認します。
    

<img width="1400" alt="wxai03-02-10-v3Result" src="https://github.com/user-attachments/assets/514a8e41-642f-400c-aeec-8462b157d847">



生成例:
```
静岡県は、富士山や伊豆半島などの豊かな自然と、徳川家康公が築いた歴史ある都市が調和した魅力的な県です。

静岡県にある観光名所3ヶ所

1. 富士山：静岡県と山梨県に跨る日本最高峰の独立峰で、日本の象徴ともいえる名峰です。
2. 三保の松原：静岡県静岡市清水区の三保半島にある景勝地です。富士山と羽衣伝説で知られる松林が見られます。
3. 修善寺：静岡県伊豆市にある温泉街です。伊豆の小京都とも呼ばれ、桂川に架かる朱色の橋や竹林が風情があります。

静岡県出身の有名人、芸能人4人

1. 広瀬すず：静岡県静岡市清水区出身。女優として、数多くの映画やドラマに出演しています。
2. 長澤まさみ：静岡県磐田市出身。女優として、数多くの映画やドラマに出演しています。
3. 百田夏菜子：静岡県浜松市出身。ももいろクローバーZのリーダーで、女優としても活躍しています。
4. 久保田利伸：静岡県静岡市清水区、旧清水市出身。歌手として、数多くのヒット曲を世に送り出しています。

静岡県で有名なレストラン3つ

1. 炭焼きレストランさわやか：げんこつハンバーグが名物のレストランチェーンです。静岡県内に多くの店舗を展開しています。
2. 中華ファミリーレストラン五味八珍：静岡県内に多くの店舗を展開する中華ファミリーレストランです。浜松餃子が人気です。
3. 元祖丁子屋：とろろ汁が名物の食事処です。東海道五十三次にも指定されている由緒ある店です。

静岡県がモデルとなっているアニメ作品3つ

1. ラブライブ！サンシャイン!!：静岡県沼津市が舞台のアニメです。多くのファンが訪れている聖地巡礼スポットがあります。
2.ちびまる子ちゃん：静岡県静岡市清水区が舞台のアニメです。清水エスパルスのある三保の松原や、ちびまる子ちゃんランドなど、多くのファンが訪れている聖地巡礼スポットがあります。
3.シュート！：静岡県掛川市が舞台のサッカー漫画です。掛川西高校など、多くのファンが訪れている聖地巡礼スポットがあります。

魅力あふれる静岡県にお越しください！
```
11. モデル・パラメータを変えて、出力内容が変わることを体験しましょう。デコードを[Sampling]に設定すると、テキストを生成するごとに異なる結果が得られます。

<img width="288" alt="wxai03-02-11-v3-Sampling-parameters" src="https://github.com/user-attachments/assets/8b2c939f-41ea-4ea0-a006-8914955dfa04">

これを複数回試してください。

Samplingの場合、ランダム・シードを固定の値にすると、[生成]を実行した時に同じような結果が得られます。
* デコード: Sampling
* 温度: ```0.9```
* 上位P(中核サンプリング): ```1```
* 上位K: ```75```
* ランダム・シード: ```65534```
* 反復ペナルティ: ```1```
* 最小トークン数: ```530```
* 最大トークン数: ```600```
  
生成例: 
```
はじめまして。静岡県は伊豆や富士山、浜名湖などの美しい自然に囲まれ、美味しい海の幸や山の幸にも恵まれています。温暖な気候で、一年を通して過ごしやすく、春には桜、夏には海水浴や花火、秋には紅葉、冬にはスキーなど、多彩なアクティビティが楽しめます。

静岡県にある観光名所3ヶ所

1. 伊豆シャボテン動物公園（伊東市） - 日本一多くのサボテンや多肉植物と動物が飼育されているテーマパーク。カピバラやレッサーパンダが人気。
2. 三保の松原（静岡市清水区） - 国の名勝・天然記念物。富士山と羽衣伝説で知られる名勝地。
3. 富士サファリパーク（裾野市） - ライオンやトラ、ゾウなど、野生の動物たちをマイカーやバスに乗って間近に観察できる。

静岡県出身の有名人、芸能人4人

1. 広瀬すず（静岡市清水区出身） - モデル、女優。連続テレビ小説「なつぞら」でヒロインを務めた。
2. 長澤まさみ（磐田市出身） - 女優。映画「世界の中心で、愛をさけぶ」や「岳」など話題作に多数出演。
3. 百田夏菜子（浜松市天竜区出身） - 歌手、アイドル。ももいろクローバーZのリーダー。
4. 久保田利伸（清水市、旧清水市出身） - シンガーソングライター。代表曲に「LA・LA・LA LOVE SONG」など。

静岡県で有名なレストラン3つ

1. 炭焼きレストランさわやか（げんこつハンバーグ） - 静岡県内に約60店舗を展開するファミリーレストラン。看板メニューは「げんこつハンバーグ」。
2. 中華ファミリーレストラン五味八珍（浜松餃子） - 静岡県内に約40店舗を展開する中華ファミリーレストラン。浜松餃子が人気。
3. 元祖丁子屋（とろろ汁） - 江戸時代に創業された老舗とろろ汁専門店。ふわふわの食感と自然薯の豊かな風味が特徴。

静岡県がモデルとなったアニメ作品3つ

1. ラブライブ！サンシャイン!! - 聖地は沼津市が中心。伊豆・三津シーパラダイスも有名。
2.ちびまる子ちゃん - 静岡県静岡市清水区（旧清水市）が舞台。静岡茶やサッカー、大道芸などが描かれ、多くのファンが訪れる。
3.シュート！ - 静岡県掛川市がモデル。作品内の掛川高校は、掛川西高校がモデルと言われる。

終わりに

魅力あふれる静岡県にお越しください！...
もっと詳しく知る
観光
歴史
自然
グルメ
```
12. [出力のクリア]をクリックして生成結果を消去し、[プロンプトのテスト]で入力項目にしていた内容を次のもので置き換えます。
* 入力: ```{your_input}```

<img width="1521" alt="wxai03-02-12-promptTemplate" src="https://github.com/user-attachments/assets/a95b3125-72ab-454b-b8cc-c155679d80a5">

13. 画面の右上にある「プロンプト変数」と表示される[{#}]をクリックします。
<img width="474" alt="wxai03-02-13-promptVariables" src="https://github.com/user-attachments/assets/06a08e90-3a32-465f-a6b7-d6a7906c0459">

14. 「プロンプト変数」という小さなウィンドウが開いたら、[新規変数 +]をクリックします。
<img width="284" alt="wxai03-02-14-promptVariablesWindow" src="https://github.com/user-attachments/assets/a88c155c-5d17-4440-86fd-666526635147">

15. [変数]と[デフォルト値]を入力します。
* 変数: ```your_input```
* デフォルト値: 
```
静岡県を知らない人に向けて、静岡県への旅行をお勧めする文章を作ってください。例があればその例を参考にして、次の「見出し一覧」にある項目を含めて書いてください。文章の最後は「魅力あふれる静岡県にお越しください！」としてください。同じ内容を繰り返さないでください。

「見出し一覧」:
- 静岡県にある観光名所3ヶ所
- 静岡県出身の有名人、芸能人4人
- 静岡県で有名なレストラン3つ
- 静岡県がモデルとなっているアニメ作品3つ
```
<img width="1521" alt="wxai03-02-15-defaultVariables" src="https://github.com/user-attachments/assets/1b851b97-bac0-4b88-9930-8e31992820a1">

16. モデル・パラメータを開き、デコードをGreedyに戻します。停止基準のトークン数も変更します。
* 最小トークン数: ```450```
* 最大トークン数: ```500```

<img width="1402" alt="wxai03-02-15-greedy" src="https://github.com/user-attachments/assets/1ad3c27d-2014-4dd7-9f33-841d9fe976ee">


17. 画面右下の[生成]をクリックして、手順10と同じ結果が得られることを確認します。
<img width="1401" alt="wxai03-02-17-generated" src="https://github.com/user-attachments/assets/ab213d36-e0da-41f0-a157-230acbf91501">

18. 画面上側の[名前をつけて保存]をクリックします。
<img width="590" alt="wxai03-03-18-SaveAsMenu" src="https://github.com/user-attachments/assets/dfe65844-3181-4895-af3d-be374019a66c">

19. 資産タイプと名前を指定して、[保存]をクリックします。
* 資産タイプ: [プロンプト・テンプレート]
* 名前: ```Welcome-Shizuoka-template```
<img width="1521" alt="wxai03-02-19-AssetType" src="https://github.com/user-attachments/assets/f0ac9207-7115-4b58-906c-ab3affa2b5f2">
  
20. 画面左上の [プロジェクト / Dojo #3] と表示されている [Dojo #3]をクリックします。

<img width="539" alt="wxai03-02-20-toDojo03Oveview" src="https://github.com/user-attachments/assets/a8c15fc7-4b31-43f5-aaac-d45af309a034">

21. Dojo #03のプロジェクトページから[アセット]をクリックします。
<img width="851" alt="wxai03-02-21-overview2Asset" src="https://github.com/user-attachments/assets/8845d5a3-d452-4124-8349-047a9b9644df">

ここからの手順は、Watson Machine Learningを使って、プロジェクト内の資産をスペースへプロモートして、スペース内に移した資産をWeb APIとしてデプロイします。それぞれの繋がりがわかりづらいので、図で整理しておきます。理解すべき点は、２つあります。
* スペースとプロジェクトは独立した関係であり、１つのスペースには、複数のプロジェクトから資産をプロモートすることができます
* スペースにプロモートされた資産のみがデプロイメントできます（プロジェクトから直接デプロイメントはできません）
<img width="2107" alt="wxai03-02-project-space-deployment" src="https://github.com/user-attachments/assets/d980f3f8-6ebe-455c-8fe9-f5e8e71177fd">


22. [すべての資産]から[Welcome-Shizuoka-template]を見つけ、右端にある[⋮] (オーバーフロー・メニューを開く/閉じる)をクリックし、開いたメニューから[スペースへのプロモート]をクリックします。

<img width="1521" alt="wxai03-02-22-promote2Space-Menu" src="https://github.com/user-attachments/assets/e7b3a14a-b3a4-4e68-b6ce-6d32934d6fec">

23. [スペースへのプロモート]ウィンドウが表示されます。[ターゲット・スペース]にある[スペースの選択または作成]をクリックします。
<img width="1521" alt="wxai03-02-23-createNewSpace" src="https://github.com/user-attachments/assets/5cef1478-3104-4c2c-8ab4-91d04ef29b57">

24. [デプロイメント・スペースの作成]ウィンドウが表示されます。次の内容を設定し、最後に[作成]をクリックします。
* 名前: ```wxaiSpace-``` この後ろに皆さんのイニシャルや好きな英数字を入れてください。
* デプロイメント・ステージ: 実動
* 機械学習サービスの選択(オプション): [機械学習サービスの新規作成]の下に表示されている、既存のWatson Machine Learningのサービス名を選択
  
<img width="1145" alt="wxai03-02-24-wxaiSpace" src="https://github.com/user-attachments/assets/cb66c81c-45a6-412c-b23f-b942a59a928a">


25. [スペースを準備しています]という表示になるので、しばらく待ちます。
<img width="706" alt="wxai03-02-25-prepareSpace" src="https://github.com/user-attachments/assets/c071c793-f994-4229-9fb6-7f6699e793db">


26. [スペースの準備が完了しました]を確認します。右上の[x]ボタンをクリックします。

<img width="695" alt="wxai03-02-26-spaceReady" src="https://github.com/user-attachments/assets/c0e009b6-f0a8-41b3-afbc-ab3ee50292d7">

27. [スペースへのプロモート]ウィンドウに戻ります。[☑️][プロモート後、スペース内のプロンプト・テンプレートに移動]にチェックを入れて、[プロモート]をクリックします。

<img width="1275" alt="wxai03-02-27-v3Promote2Space" src="https://github.com/user-attachments/assets/7f8d183a-153b-4cf2-8d32-0b31c1dafc7e">

28. [プロモーションが進行中です]の表示が出るので、しばらく待ちます。
    
<img width="1521" alt="wxai03-02-28-promoting" src="https://github.com/user-attachments/assets/edbc0868-1741-4119-af9b-6aa9874a0cd3">

29. [デプロイメント / wxaiSpace / Welcome-Shizuoka-template] の画面になったことを確認し、[新規デプロイメント]をクリックします。

<img width="1402" alt="wxai03-02-29-noDeploymentsYet" src="https://github.com/user-attachments/assets/68e746fb-7520-42c3-80b9-258537590bcb">

30. [スペースに関連付けられた機械学習サービス・インスタンスはありません]と表示されるので、[スペース設定に移動]をクリックします。
<img width="1521" alt="wxai03-02-30-noMLInstances" src="https://github.com/user-attachments/assets/848967cd-3f20-43d5-a71d-433fb90a64fe">


31. wxaiSpace-で始まる名前のデプロイメント・スペースが表示されます。画面右下にある[インスタンスの関連付け +]をクリックします。

<img width="1402" alt="wxai03-02-31-wxaiSpaceAO" src="https://github.com/user-attachments/assets/e2c2ca15-446e-4b2f-aad1-73b6d9ec5737">

32. 表示されたWatson Machine Learningを選択して、最後に[保存]をクリックします。
* 機械学習サービスの選択
<img width="417" alt="wxai03-02-31-ChooseML" src="https://github.com/user-attachments/assets/54c64b10-6ddc-45b4-8ca9-aa142ddc4878">

* 保存できた状態

<img width="1402" alt="wxai03-02-32-MLSaved" src="https://github.com/user-attachments/assets/87c7842e-22f3-46ab-91e8-d4a9bde182dc">


33. wxaiSpace- で始まる名前の画面から[資産]タブをクリックし、資産の一覧を表示します。

<img width="1399" alt="wxai03-02-33-v3Assets" src="https://github.com/user-attachments/assets/427ca3c4-da1d-43b0-95d8-cf09f4524ad6">


34. [Welcome-Shizuoka-template]というプロンプト・テンプレートを見つけ、[⋮]をクリックして、[デプロイ]をクリックします。

<img width="1395" alt="wxai03-02-24-DeployMenu" src="https://github.com/user-attachments/assets/99da8c7a-9d8b-42ff-920c-00a69d279c84">

35. [デプロイメントの作成]ウインドウが開くので、次の項目を設定してから、最後に[作成]をクリックします。
* 名前: ```depWS```
* サービス提供名: ```wst01_``` この文字の後に、皆さんの好きな英数字(英語は小文字で書いてください。英語の大文字は使えません。)を組み合わせて、ユニークな名前にしてください。

<img width="1274" alt="wxai03-02-35-createDeploymentV3" src="https://github.com/user-attachments/assets/b1e2058e-955f-42cb-b4f6-d8b60da46767">

36. depWSが[デプロイ済み]であることを確認します。

<img width="1398" alt="wxai03-02-36-v3Deployed" src="https://github.com/user-attachments/assets/bd56ff0c-0374-4f21-9e84-08f726443304">


この演習2はここまでです。続けて、[演習3](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/03-invoke-webapi/readme.md)に進んでください。

 



