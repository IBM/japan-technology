# Watson Natural Language Classifier を利用して e-メール・フィッシングを検出する

### e-メール・フィッシングの試みを検出するように Watson Natural Language Classifier をトレーニングする

English version: https://developer.ibm.com/patterns/predict-phishing-attempts-in-email-with-nlc
  ソースコード: https://github.com/IBM/nlc-email-phishing

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-09-19

 
## 概要

現代社会において、e-メールは人々と企業の間で使用されている主な通信手段です。けれどもそれと同時に、e-メールは不正を働こうとする者にとって、不正や「フィッシング詐欺」を行う大きな可能性を開きます。不正な e-メールの検出は分類問題の一種と見なされるため、このコード・パターンでは、e-メールを分類して「フィッシング」、「スパム」、「ハム」(疑わしくない e-メールの場合) のいずれかのラベルを付けるアプリの作成方法を説明します。

## 説明

現代社会では、e-メールが主要な通信形式と見なされています。けれども、この通信形式にはフィッシングという問題が伴います。個人や企業を餌食にするフィッシング詐欺は、世界全体で 10 億米ドルもの損失を記録する一因となっています。この問題を阻止できるよう、フィッシングを検出する手法を考え出して適用する必要があります。

このコード・パターンでは、e-メールを分類して「フィッシング」、「スパム」、「ハム」(疑わしくない e-メールの場合) のいずれかのラベルを付けるアプリケーションの作成方法を説明します。このパターンでは IBM Watson Natural Language Classifier を利用し、EDRM Enron e-メール・データ・セットに含まれる e-メールを使ってモデルをトレーニングします。Watson Natural Language Classifier サービスを利用すれば、Web UI 内で迅速、簡単にカスタム NLC モデルを作成できます。作成したモデルは Watson Developer Cloud Node.js SDK を使用して Node.js アプリにデプロイし、ブラウザーから実行できます。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* Web UI を使用して Watson Natural Language Classifier モデルを作成する
* NLC モデルを使用して e-メールをフィッシングとして分類する Node.js アプリケーションを作成する
* Watson Developer Cloud SDK for Node.js を使用する

## フロー

![フロー](../../images/flow-predict-phishing-attempts.png)

1. ユーザーが Natural Language Classifier GUI を操作してモデルをトレーニングします。
1. Natural Language Classifier に EDRM データをロードして、トレーニング用のサンプル e-メールを提供します。
1. ユーザーが e-メール・テキストを分類対象としてアプリケーションに送信します。
1. アプリが Watson Natural Language Classifier を利用して、送信されたテキストがフィッシング、スパム、ハムのどれに分類されるか判別します。

## 手順

詳細な手順については、[README](https://github.com/IBM/nlc-email-phishing/blob/master/README.md) を参照してください。手順の概要は以下のとおりです。

1. GitHub リポジトリーを複製します。
1. IBM Cloud を使用して、Watson Natural Language Classifier サービス・インスタンスを作成します。
1. Natural Language Classifier モデルをトレーニングします。
1. 資格情報を構成します。
1. アプリケーションを実行します。
