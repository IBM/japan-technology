# 宇宙から都市を見分ける

### Watson Visual Recognition を利用して、ISS から撮影された世界の都市の画像を識別するカスタム分類子を作成する

English version: https://developer.ibm.com/patterns/identify-cities-from-space-using-watson-visual-recognition
  ソースコード: https://github.com/IBM/cities-from-space

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-07-23

 ## 概要

[Windows on Earth](https://www.windowsonearth.org/) プロジェクトでは、国際宇宙ステーション上の宇宙飛行士が撮った数々の画像を揃えています。この画像ギャラリーには、雲、夕焼け、農場、そして夜間に撮られた世界の各都市の画像があります。このコード・パターンでは都市の画像と Watson Visual Recognition を結び付けて、夜の画像に基づいてさまざまな都市を識別するカスタム分類子の作成方法を説明します。

## 説明

1998 年に打ち上げられた国際宇宙ステーション (ISS) は、微小重力の宇宙環境にある研究所の役割を果たしています。ここでは乗組員たちが、生物学、人類生物学、物理学、天文学、気象学などの分野の実験を行っています。こうした実験によって大量のデータと実験結果が生まれており、その多くは一般公開されています。Windows on Earth プロジェクトでは、科学研究、教育、社会支援を目的に、宇宙飛行士が撮った画像を揃えています。このコード・パターンでは、さまざまな都市の夜の画像を材料に、IBM Watson Visual Recognition を使用して視覚認識カスタム分類子を作成することで、ISS から撮影された何千点もの画像を、AI を使用して分類し、組織化できることを実証します。

このコード・パターンをひととおり完了すると、以下の方法がわかるようになります。

* 国際宇宙ステーションから撮影された画像を使用して、視覚認識カスタム分類子をトレーニングする
* Watson Visual Recognition サービスを利用して画像を分類する Node.js サーバーを作成する
* サーバーの起動時に、視覚認識カスタム分類子を初期化させる
* Watson Visual Recognition を利用して、宇宙から撮った都市の画像を分類する

## フロー

![フロー](../../images/arch-identify-cities-space.png)

1. ユーザーが Web UI を操作して、宇宙から見た夜の都市の画像を選択します。
1. 選択した画像が、クラウド内で稼働中のサーバー・アプリケーションに渡されます。
1. サーバーが画像を分析対象として Watson Visual Recognition サービスに送信します。
1. Watson Visual Recognition サービスが画像を分類し、その画像から識別された都市とその識別結果の信頼レベルを示す情報をサーバーに返します。

## 手順

このパターンの詳細な手順については、[README](https://github.com/IBM/cities-from-space/blob/master/README.md) を参照してください。手順の概要は以下のとおりです。

1. GitHub リポジトリーを複製します。
1. Watson Visual Recognition サービス・インスタンスを作成します。
1. env ファイルに Watson Visual Recoginition API キーを追加します。
1. 依存関係をインストールしてサーバーを実行します。
