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

4. プロンプト・ラボが開いたら、[構造化」をクリックします。（ご注意：最後にプロンプト・ラボを操作した時にチャット、構造化、フリー・フォームのどの画面で利用していたかによって状況が変わります。）

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

* 最小トークン数: ```300```
* 最大トークン数: ```800```
<img width="1521" alt="wxai03-02-07-parametersV2" src="https://github.com/user-attachments/assets/ce688946-9a8c-4e69-abc7-f59e60690365">


8. 画面右下の[生成]をクリックします。
   <img width="1521" alt="wxai03-02-09-generated1V2" src="https://github.com/user-attachments/assets/5aa420ca-dda0-4762-9480-5f9336794aad">

生成例を貼っておきます。この内容には事実と異なる情報が含まれていますので、ご注意ください。
```
静岡県は、富士山や伊豆半島などの美しい自然景観、徳川家康公が築いた歴史的な建造物、伊豆や熱海などの温泉など、魅力的な観光資源に恵まれています。また、お茶やみかんなどの特産品も豊富です。静岡県出身の有名人では、歌手の大石恵理子さん、俳優の哀川翔さん、お笑い芸人のなすびさんなどがいます。静岡県で有名なレストランでは、さわやか御殿場インター店、炭焼きレストランさわやか富士鷹岡店、さわやか静岡インター店などが人気です。静岡県をモデルとしたアニメ作品としては、「ゆるキャン△」や「ちびまる子ちゃん」などが有名です。魅力あふれる静岡県にお越しください！

静岡県にある観光名所3ヶ所

静岡県には、富士山や伊豆半島などの美しい自然景観、徳川家康公が築いた歴史的な建造物、伊豆や熱海などの温泉など、魅力的な観光資源に恵まれています。

静岡県出身の有名人、芸能人4人

静岡県出身の有名人では、歌手の大石恵理子さん、俳優の哀川翔さん、お笑い芸人のなすびさんなどがいます。

静岡県で有名なレストラン3つ

静岡県で有名なレストランでは、さわやか御殿場インター店、炭焼きレストランさわやか富士鷹岡店、さわやか静岡インター店などが人気です。

静岡県がモデルとなっているアニメ作品3つ

静岡県をモデルとしたアニメ作品としては、「ゆるキャン△」や「ちびまる子ちゃん」などが有名です。

魅力あふれる静岡県にお越しください！

静岡県は、富士山や伊豆半島などの美しい自然景観、徳川家康公が築いた歴史的な建造物、伊豆や熱海などの温泉など、魅力的な観光資源に恵まれています。また、お茶やみかんなどの特産品も豊富です。静岡県出身の有名人では、歌手の大石恵理子さん、俳優の哀川翔さん、お笑い芸人のなすびさんなどがいます。静岡県で有名なレストランでは、さわやか御殿場インター店、炭焼きレストランさわやか富士鷹岡店、さわやか静岡インター店などが人気です。静岡県をモデルとしたアニメ作品としては、「ゆるキャン△」や「ちびまる子ちゃん」などが有名です。魅力あふれる静岡県にお越しください！
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

<img width="1521" alt="wxai03-02-09-examplesV2" src="https://github.com/user-attachments/assets/64589066-06f1-434f-ad2a-9db3f45139e2">


10. [出力のクリア]をクリックしてから、画面右下の[生成]をクリックします。上記手順8の結果と異なることを確認します。

<img width="1521" alt="wxai03-02-10-generated2V2" src="https://github.com/user-attachments/assets/e5c3ed14-afcf-4635-846a-5ca1316d994a">

生成例:
```
 静岡県は、富士山や伊豆半島などの豊かな自然と、徳川家康公が築いた歴史ある都市が調和した魅力的な県です。

静岡県にある観光名所3ヶ所

1. 富士山：静岡県と山梨県に跨る日本最高峰の独立峰で、日本の象徴ともいえる名峰です。
2. 三保の松原：静岡県静岡市清水区の三保半島にある景勝地です。富士山と羽衣伝説で知られる松林が見られます。
3. 修善寺：静岡県伊豆市にある温泉街です。伊豆最古の温泉と言われ、多くの観光客が訪れます。

静岡県出身の有名人、芸能人4人

1. 広瀬 すず：静岡県静岡市清水区出身。女優、ファッションモデルとして活躍中。
2. 長澤 まさみ：静岡県磐田市出身。女優として数々の話題作に出演している。
3. 百田 夏菜子：静岡県浜松市出身。ももいろクローバーZのリーダーで、女優としても活躍中。
4. 久保田 利伸：静岡県静岡市清水区出身。歌手、音楽プロデューサーとして活躍中。

静岡県で有名なレストラン3つ

1. 炭焼きレストランさわやか：げんこつハンバーグが名物の静岡県内に展開するファミリーレストラン。県内に多くの店舗がある。
2. 中華ファミリーレストラン五味八珍：静岡県内に展開する中華ファミリーレストラン。浜松餃子が名物で、多くの観光客が訪れます。
3. 元祖丁子屋：静岡県静岡市駿河区丸子にあるとろろ汁の専門店。東海道五十三次にも指定されている。

静岡県がモデルとなっているアニメ作品3つ

1. ラブライブ！サンシャイン!!：静岡県沼津市が舞台。伊豆・三津シーパラダイスも有名で、多くのファンが訪れています。
2. ちびまる子ちゃん：静岡県静岡市清水区が舞台。エスパルス・ドリームプラザ内に「ちびまる子ちゃんランド」があり、多くのファンが訪れています。
3. シュート！：静岡県掛川市が舞台。作品内の掛川高校は、掛川西高校がモデルと言われています。
```
11. モデル・パラメータを変えて、出力内容が変わることを体験しましょう。デコードを[Sampling]に設定すると、テキストを生成するごとに異なる結果が得られます。

<img width="295" alt="wxai03-02-11-parameters-Sampling" src="https://github.com/user-attachments/assets/588539a6-3a96-4159-9b33-33ac8379bde4">

Samplingの場合、ランダム・シードを固定にすると、[生成]を実行した時に同じような結果が得られます。
* デコード: Sampling
* 温度: ```0.9```
* 上位P(中核サンプリング): ```1```
* 上位K: ```75```
* ランダム・シード: ```65534```
* 反復ペナルティ: ```1```
  
生成例:
```
 はじめまして。静岡県は伊豆や富士山、浜名湖などの美しい自然に囲まれ、美味しい海の幸や山の幸にも恵まれています。また、歴史探訪には最適な場所でもあります。徳川家康公ゆかりの地としても有名です。

静岡県の代表的な観光名所と言えば、やっぱり富士山です。世界遺産にも登録され、日本一の高さを誇る富士山は、見る者を圧倒するほどの雄大さです。近くには、日本一深いとされる駿河湾もあり、海産物も豊富です。また、伊豆半島には、温泉やダイビングスポットが数多くあり、人気のリゾート地となっています。

静岡県出身の有名人、芸能人と言えば、まず真っ先に浮かぶのが、ご存知、世界遺産に登録された富士山の麓にある富士宮市出身の徳川家康公でしょう。続いて、同じく富士宮市出身の笑福亭鶴瓶師匠や、清水エスパルスの大滝選手や奥井選手、ジュビロ磐田の伊藤選手と小川選手など、スポーツ選手が多く活躍しています。最近では、女優の長澤まさみさん、人気グループ「ももいろクローバーZ」の百田夏菜子さんも静岡県出身です。

静岡県で有名なレストランと言えば、まずは、やはり「さわやか」のげんこつハンバーグでしょう。げんこつサイズにギュッと詰まった肉汁とデミグラスソースが絡んだこのハンバーグは、静岡県民だけでなく、多くの観光客にも大人気のメニューです。また、中華ファミリーレストランの「五味八珍」は、浜松餃子が看板メニューで、こちらも静岡県民にはお馴染みのレストランです。

最後に、静岡県をモデルとしたアニメ作品と言えば、「ちびまる子ちゃん」でしょう。静岡県静岡市清水区（旧清水市）を舞台に、主人公のまる子とその家族、友人たちが繰り広げるほのぼのとした日常を描いた作品です。また、サッカー漫画の「シュート！」も、静岡県掛川市をモデルとした作品で、多くのサッカー選手に夢を与えました。

魅力あふれる静岡県にお越しください！
```
12. 「プロンプトのテスト」で入力項目にしていた内容を次のもので置き換えます
入力: ```{your_input}```
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

16. モデル・パラメータを開き、デコードをGreedyに戻します。画面右下の[生成]をクリックして、手順10と同じ結果が得られるを確認します。
<img width="1521" alt="wxai03-02-16-runByVariable" src="https://github.com/user-attachments/assets/2133d6c4-821f-4d81-a878-4d0e69743ad3">

17. [出力のクリア]をクリックして、生成内容を消去します。
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

22. [すべての資産]から[Welcome-Shizuoka-template]を見つけ、右端にある[⋮] (オーバーフロー・メニューを開く/閉じる)をクリックし、開いたメニューから[スペースへのプロモート]をクリックします。

<img width="1521" alt="wxai03-02-22-promote2Space-Menu" src="https://github.com/user-attachments/assets/e7b3a14a-b3a4-4e68-b6ce-6d32934d6fec">

23. [スペースへのプロモート]ウィンドウが表示されます。[ターゲット・スペース]にある[スペースの選択または作成]をクリックします。
<img width="1521" alt="wxai03-02-23-createNewSpace" src="https://github.com/user-attachments/assets/5cef1478-3104-4c2c-8ab4-91d04ef29b57">

24. [デプロイメント・スペースの作成]ウィンドウが表示されます。次の内容を設定し、最後に[作成]をクリックします。
* 名前: ```wxaiSpace```
* デプロイメント・ステージ: 開発
* 機械学習サービスの選択(オプション): [機械学習サービスの新規作成]の下に表示されている、既存のWatson Machine Learningのサービス名を選択
  
<img width="1148" alt="wxai03-02-24-deploymentSpaceSettings" src="https://github.com/user-attachments/assets/e490c8c9-b239-4cef-8720-6afef826c774">

25. [スペースを準備しています]という表示になるので、しばらく待ちます。
<img width="1521" alt="wxai03-02-25-provisioningSpace" src="https://github.com/user-attachments/assets/86cf7f15-105e-4235-9b77-c0240e639c42">

26. [スペースの準備が完了しました]を確認します。右上の[x]ボタンをクリックします。
<img width="1521" alt="wxai03-02-25-spaceReady" src="https://github.com/user-attachments/assets/3f662170-3d35-4af1-b0a1-8d2a99425367">

27. [スペースへのプロモート]ウィンドウに戻ります。[☑️][プロモート後、スペース内のプロンプト・テンプレートに移動]にチェックを入れて、[プロモート]をクリックします。
<img width="1521" alt="wxai03-02-27-promote2Space" src="https://github.com/user-attachments/assets/56535f92-c053-4238-9b80-0236a1c950ad">

28. [プロモーションが進行中です]の表示が出るので、しばらく待ちます。
<img width="1521" alt="wxai03-02-28-promoting" src="https://github.com/user-attachments/assets/edbc0868-1741-4119-af9b-6aa9874a0cd3">

29. [デプロイメント / wxaiSpace / Welcome-Shizuoka-template] の画面になったことを確認し、[新規デプロイメント]をクリックします。
<img width="1521" alt="wxai03-02-29-deployment" src="https://github.com/user-attachments/assets/919077cf-c8e8-412a-8f87-72d174208ad3">

30. [スペースに関連付けられた機械学習サービス・インスタンスはありません]と表示されるので、[スペース設定に移動]をクリックします。
<img width="1521" alt="wxai03-02-30-noMLInstances" src="https://github.com/user-attachments/assets/848967cd-3f20-43d5-a71d-433fb90a64fe">


31. wxaiSpaceという名前のデプロイメント・スペースが表示されます。画面右下にある[インスタンスの関連付け +]をクリックします。
<img width="1521" alt="wxai03-02-31-wxaiSpace" src="https://github.com/user-attachments/assets/dab31df5-8bd5-46c6-9d8d-96901d27f865">

32. 表示されたWatson Machine Learningを選択して、最後に[保存]をクリックします。
<img width="1521" alt="wxai03-02-32-setML" src="https://github.com/user-attachments/assets/646fb9f3-c5c7-40ce-9398-e061db9f761a">

33. wxaiSpaceの画面から[資産]タブをクリックし、資産の一覧を表示します。
<img width="1521" alt="wxai03-02-33-assets" src="https://github.com/user-attachments/assets/c9905090-e305-4b80-9095-d98b414b8a84">

34. [Welcome-Shizuoka-template]というプロンプト・テンプレートを見つけ、[⋮]をクリックして、[デプロイ]をクリックします。
<img width="1521" alt="wxai03-02-34-deployMenu" src="https://github.com/user-attachments/assets/bdf6480a-7b34-46f4-8aef-3a0aba31a61f">

35. [デプロイメントの作成]ウインドウが開くので、次の項目を設定してから、最後に[作成]をクリックします。
* 名前: ```depWS```
* サービス提供名: ```wst01``` この文字の後に、皆さんの英数字を組み合わせて、ユニークな名前にしてください。

<img width="1521" alt="wxai03-02-35-createDeployment" src="https://github.com/user-attachments/assets/c24bb236-14b6-41a4-ab29-55172eb2d187">

36. depWsが[デプロイ済み]であることを確認します。

  <img width="1521" alt="wxai03-02-36-deployed" src="https://github.com/user-attachments/assets/ce59ff46-2898-42dd-982c-c858ac003e48">

この演習2はここまでです。続けて、[演習3](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/03-invoke-webapi/readme.md)に進んでください。

 



