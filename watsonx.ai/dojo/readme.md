# watsonx.ai Dojo ハンズオン用資料
このフォルダには、watsonx.ai Dojoで利用するハンズオン資料を公開しています。

免責事項: IBM watsonx as a Serviceはクラウド・サービスです。定期的な更新が発生するため、資料内の画像と、製品のユーザー・インターフェイスが一致していない場合があります。

## はじめに
初めてIBM watsonx as a Serviceをご利用の際は、watsonxの起動方法を学び、操作を覚えましょう。
* [watsonx.aiの起動 (IBM Cloudコンソール)](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/start/readme.md "Launch watsonx from IBM Cloud")
* [watsonx.aiの起動 (IBM watsonx セットアップ済みの場合)](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/start/readme2.md "Launch watsonx directly")

# 生成AIを使ったアプリ開発入門編 (watsonx.ai Dojo #2)

## 演習1: チャット・モード
この演習は、IBM watsonx.aiのプロンプト・ラボに含まれるチャット機能を体験します。またチャット機能に調べたい文書をアップロードすることで、生成AIが文書の内容を参照しながら、質問に答えることができます。IBM Redbooksから英語のPDFファイルをダウンロードして、チャット機能から質問してみましょう。
* [新規プロジェクトの作成](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/create-new-project/readme.md "Create New Project")
* [基盤モデルを使ったチャットを試す](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/02/01-chat-with-llm/readme.md "Chat with LLM")
* [文書と言語モデルを使ったチャット](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/02/02-chat-with-document/readme.md "Chat with Doc")
## 演習2: プロンプト・ラボ 
この演習は、プロンプト・ラボのサンプル・プロンプトを利用して、日本語の質問に回答するプロンプトを試します。IBM watsonx APIを利用して、Pythonのスクリプトからプロンプトを実行し、JSON文字列として結果を受け取る体験を行います。生成AIアプリ開発の入り口に立ちましょう。
* [プロンプト・ラボの利用とPythonによるプロンプトの実行](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/02/03-PromptLab-101/readme.md "Prompt Lab and Python") 

# プロンプト・エンジニアリング (watsonx.ai Dojo #3)
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
* [granite-8b-japanese 基盤モデルを使い、フリー・フォームのプロンプトを改良しながら、地方の魅力を伝えるための文章を生成する](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/01-simple-prompt/readme.md "Prompt Lab - freeform")

## 演習2: プロンプト・ラボの構造化フォームを使ってプロンプトを作り、Web APIとしてデプロイする
この演習は、プロンプト・ラボの[構造化]から出発して、プロンプト内の例示により言語モデルが持っていない知識を補いながら、指定された内容を含む文章を生成するプロンプトを試します。出来上がったプロンプトを、プロンプト・テンプレートとして保存し、そのテンプレートをWeb APIとしてデプロイします。Web APIをデプロイする前に、デプロイメント・スペースの作成、スペースのプロモートなど、慣れない手順が入ってきますが、順を追って進めていきましょう。デプロイが完了すると、インターネットあるいはIBM Cloud内のプライベート接続から、Web APIの呼び出しでプロンプトを実行できます。

* [granite-8b-japanese 言語モデルを使い、構造化されたプロンプトを改良しながら、地方の魅力を伝えるための文章を生成する](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/02-structured-prompt/readme.md "Prompt Lab - Structured")

## 演習3: デプロイ済みのWeb APIへアクセスする
この演習は、デプロイ済みのWeb APIを呼び出す方法について、テスト環境を含めて体験します。上述の演習2の結果を利用しますので、ご注意ください。
* [watsonx.ai にデプロイ済みのWeb APIを呼び出す](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/03-invoke-webapi/readme.md "Invoke WebAPI")


# watsonx.ai Dojo #4 生成AIを使ったアプリ開発、応用編 (LangChainとChromaによるRAGの基本実装) 

watsonx.ai Dojo #4の演習は、Dojo #2やDojo #3の演習結果との依存関係はありません。
Dojo #3で利用したプロンプトを再利用しますが、新しいプロジェクト内に展開するので、Dojo #4の演習のみで進めることができます。

IBM watsonxがセットアップ済みであれば、順番に進めることができます。このセットアップ済みとは、次の何れかを示します。
* IBM watsonxの30日無料評価版を使っている
* IBM Cloudのアカウントを使いWatson Studio, Watson Machine Learning, Cloud Object Storageがセットアップ済みである
* IBM Technology Zoneからwatsonxの環境を予約している

もし、これらの条件を満たしていない場合は、[事前準備](https://speakerdeck.com/oniak3ibm/watsonx-ai-dojo-prereq "prereq") をご覧の上、必要な環境をご準備ください。
watsonx.ai Dojoのセッション中は、環境セットアップについてサポートすることができませんのでご注意ください。

## 演習1: [LangChainによるRAG、演習準備](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/04/01-new-project/readme.md)
この演習では、ローカル・コンピューター上のPython仮想環境の確認、Pythonパッケージのインストールあるいはアップデート、watsonx.aiのプロジェクト作成、プロジェクトIDの取得を行います。

## 演習2: [テキストファイルに知識を書いておき、granite-8b-japanese、Chroma、LangChainを利用して、RAGを実行する](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/04/02-rag/readme.md)
この演習では、ローカル・コンピューター上のPython仮想環境を使って、LangChainを使ったRAGを実行するために必要なことを、１つずつ実行しながら確認していきます。
