# watsonx.ai Dojo # プロンプト・エンジニアリング
watsonx.ai Dojo #3の演習は、Dojo #2の演習結果との依存関係はありません。

IBM watsonxがセットアップ済みであれば、順番に進めることができます。このセットアップ済みとは、次の何れかを示します。
* IBM watsonxの30日無料評価版を使っている
* IBM Cloudのアカウントを使いWatson Studio, Watson Machine Learning, Cloud Object Storageがセットアップ済みである
* IBM Technology Zoneからwatsonxの環境を予約している

もし、これらの条件を満たしていない場合は、[事前準備](https://speakerdeck.com/oniak3ibm/watsonx-ai-dojo-prereq "prereq") をご覧の上、必要な環境をご準備ください。
watsonx.ai Dojoのセッション中は、環境セットアップについてサポートすることができませんのでご注意ください。

[watsonx.aiの起動方法](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/start/readme2.md "Launch watsonx directly")や[新規プロジェクトの作成方法](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/create-new-project/readme.md "Create New Project")がわからない場合は、それぞれリンクを辿って確認してください。

## 演習1: プロンプト・ラボのフリー・フォームを使ってプロンプトを作る
この演習は、プロンプト・ラボのフリー・フォームから出発して、指定された内容を含む文章を生成するプロンプトを試します。
こちらは後続の演習との依存関係がありません。
* [granite-8b-japanese 言語モデルを使い、フリー・フォームのプロンプトを改良しながら、地方の魅力を伝えるための文章を生成する](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/01-simple-prompt/readme.md "Prompt Lab - freeform")

## 演習2: プロンプト・ラボの構造化フォームを使ってプロンプトを作り、Web APIとしてデプロイする
この演習は、プロンプト・ラボの[構造化]から出発して、プロンプト内の例示により言語モデルが持っていない知識を補いながら、指定された内容を含む文章を生成するプロンプトを試します。出来上がったプロンプトを、プロンプト・テンプレートとして保存し、そのテンプレートをWeb APIとしてデプロイします。Web APIをデプロイする前に、デプロイメント・スペースの作成、スペースのプロモートなど、慣れない手順が入ってきますが、順を追って進めていきましょう。デプロイが完了すると、インターネットあるいはIBM Cloud内のプライベート接続から、Web APIの呼び出しでプロンプトを実行できます。

* [granite-8b-japanese 言語モデルを使い、構造化されたプロンプトを改良しながら、地方の魅力を伝えるための文章を生成する](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/02-structured-prompt/readme.md "Prompt Lab - Structured")

## 演習3: デプロイ済みのWeb APIへアクセスする
この演習は、デプロイ済みのWeb APIを呼び出す方法について、テスト環境を含めて体験します。上述の演習2の結果を利用しますので、ご注意ください。
* [watsonx.ai にデプロイ済みのWeb APIを呼び出す](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/03-invoke-webapi/readme.md "Invoke WebAPI")
