## granite-8b-japanese 言語モデルを使い、構造化されたプロンプトを改良しながら、地方の魅力を伝えるための文章を生成する
IBM watsonx.aiのプロンプト・ラボを使い、静岡県の魅力を伝えるための文章を作ってみましょう。

参考URL: [プロンプト・ラボ](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-prompt-lab.html?context=wx&locale=ja "Prompt Lab")

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
6. 
