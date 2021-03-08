# 災害時の状況確認をドローンで自動化してオフライン通信を促進する

### 視覚認識によって航空画像から S.O.S. メッセージを検出する

English version: https://developer.ibm.com/patterns/automate-post-disaster-checks-and-foster-offline-communication
ソースコード: https://github.com/code-and-response/droneaid

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2019-10-17

 _このコード・パターンは [2020 Call for Code Global Challenge](https://developer.ibm.com/jp/callforcode/) の一部です。_

## 概要

緊急援助隊員の捜索および救助活動において、今やドローンは不可欠のツールとなっています。このコード・パターンでは、視覚認識を使用して航空画像から S.O.S. メッセージを検出し、タグ付けする方法を説明します。

## 説明

2017 年はハリケーン・マリア、イルマ、ハーベイからカリフォルニア州の破壊的な山火事に至るまで、記録的な自然災害に見舞われた年でした。人為的災害は言うまでもなく、世界中の人々は津波、竜巻、洪水、土砂崩れ、地震、火山の噴火などの自然災害に苦しめられています。

捜索および救助活動においても災害救助活動においても、今や航空画像は不可欠です。けれども、誰もがヘリコプターや衛星を利用できるわけではありません。そこで、航空写真をすばやく安価に撮るにはドローンが必須のツールとなっています。

このコード・パターンでは、以下のタスクを行う方法を説明します。

* [Cloud Annotations](https://cloud.annotations.ai/) を利用して、オブジェクト検出によって普遍的な救助シンボル (「S.O.S」など) を識別できるように視覚認識モデルをトレーニングする
* Tello ドローンから動画をストリーミングして動画フィードをキャプチャーする
* 動画フィードに対して予測を実行し、その結果をダッシュボードに表示する Web アプリを構成する

## フロー

![災害後視覚認識アーキテクチャーのフロー図](../../images/post-disaster-visual-recognition-3.png)

1. ユーザーが Lens Studio を使用してサンプル画像を生成します。
2. ユーザーが画像を Cloud Annotations にアップロードします。Cloud Annotations はそれらの画像を使用してモデルをトレーニングし、TensorFlow.js モデルをエクスポートします。
3. ユーザーが TensorFlow.js モデルを Web アプリケーションに追加します。
4. ユーザーが Tello ドローンをコンピューターに接続し、Web アプリケーションを起動します。
5. ドローンの動画フィードが Web アプリケーションによってキャプチャーされます。
6. キャプチャーされた動画フレームが TensorFlow.js モデルによって分析されます。
7. Web アプリの UI に視覚認識分析の結果が表示されます。

## 手順

このコード・パターンに取り組む準備はできましたか？詳細な手順については、[README.md](https://github.com/Code-and-Response/DroneAid/blob/master/README.md) と [SETUP.md](https://github.com/Code-and-Response/DroneAid/blob/master/SETUP.md) を参照してください。手順の概要は次のとおりです。

1. 拡張現実を使用して画像セットを生成します。
2. モデルをトレーニングします。
3. ダッシュボードをデプロイします。
