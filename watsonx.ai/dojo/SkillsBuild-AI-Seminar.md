# watsonx.ai Dojo ハンズオン用資料 (IBM SkillsBuild AIセミナー用) 
最終更新日: 2025/4/21
このフォルダには、watsonx.ai Dojoで公開している資料から、IBM SkillsBuild AIセミナーで利用するものをまとめています。

ハンズオンの目的:
* オープンな技術を活用して開発されているAIプラットフォーム、watsonxを短時間で試す
* チャット形式で言語モデルと対話し、様々な自然言語に対応できることを確認する
* 言語モデルが学習していない内容に対して、プロンプト内にヒントを与えて回答させる、RAG(Retrieval Augmented Generation、検索拡張生成)の基本となる事を体験する
* 時間に余裕があれば、Googleから検索した内容を使って回答するAIエージェントを体験する

ハンズオン中のサポート:
* 気になることがありましたら、ハンズオン会場内の講師やスタッフにお声がけください。
* ハンズオン、AIセミナーと全く関係ない質問については、回答できない場合がありますので、ご注意ください。

免責事項: 
* IBM watsonx as a Serviceはクラウド・サービスです。定期的な更新が発生するため、資料内の画像と、製品のユーザー・インターフェイスが一致していない場合があります。またクラウド・サービスのため、インターネット接続が確保できない場合は接続できません。会場のWiFiがうまく繋がらない場合、お持ちのスマホからテザリングを用いて、お使いのPC/macをインターネットに繋げてください。
* 表記がおかしい、誤字脱字がある、など資料へのフィードバックは遠慮なく、お近くのスタッフにお寄せください。
* 演習3のAIエージェントは、リリース前のベータ版です。公式文書も少なく、期待通りに動作しない場合もありますのでご注意ください。

## 事前準備
* インターネットに接続できる PCまたはmac
* watsonx体験環境の準備: watsonxを体験するためには、無料評価版への登録が簡単です。もし、セミナー会場で登録する場合は、お手持ちのスマホから、あるいはスマホにテザリングで接続したPC/macから次のURLにアクセスしてください。
* [watsonx 30日無料評価版への登録](https://jp-tok.dataplatform.cloud.ibm.com/registration/stepone?context=wx&preselect_region=true)

## はじめに
初めてIBM watsonx as a Serviceをご利用の際は、watsonxの起動方法を学び、操作を覚えましょう。
* [watsonx.aiの起動 (IBM watsonx セットアップ済みの場合)](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/start/readme2.md "Launch watsonx directly")

## 演習1: プロンプト・ラボのチャット機能を体験する
この演習は、IBM watsonx.aiのプロンプト・ラボに含まれるチャット機能を体験します。
* [新規プロジェクトの作成](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/create-new-project/readme.md "Create New Project")
* [言語モデルを使ったチャットを試す](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/02/01-chat-with-llm/readme.md "Chat with LLM")

## 演習2: プロンプト・ラボのフリー・フォームを使ってプロンプトを作る
この演習は、プロンプト・ラボのフリー・フォームから出発して、指定された内容を含む文章を生成するプロンプトを試します。
ハンズオンの文書上は、プロジェクトが別の名前で表現されていますが、上記演習1で作成したプロジェクトをそのまま利用しても構いません。
* [granite-8b-japanese 言語モデルを使い、フリー・フォームのプロンプトを改良しながら、地方の魅力を伝えるための文章を生成する](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/01-simple-prompt/readme.md "Prompt Lab - freeform")

## 演習3: AIエージェントを試してみる
演習1、演習2が終わり、時間に余裕がある方は、AIエージェントを試してみましょう。
https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/07/readme.md


