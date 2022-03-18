---
also_found_in:
- learningpaths/explore-autoai/
authors: ''
completed_date: '2020-06-04'
components:
- watson-studio
demo:
- button_title: Watch the demo
  type: demo
  url_or_id: https://developer.ibm.com/videos/machine-learning-tutorial-ibm-watson-autoai-data-exploration-and-visualization
draft: false
excerpt: IBM Watson StudioとAutoAIを使って、線形回帰を使って保険料コストを予測するWebアプリケーションを作成します。
github:
- button_title: Get the code
  url: https://github.com/IBM/predict-insurance-charges-with-ai
last_updated: '2020-06-04'
meta_description: IBM Watson StudioとAutoAIを使って、線形回帰で保険料コストを予測するWebアプリケーションを作成します。
meta_keywords: AutoAI, Watson Studio, linear regression, machine learning
meta_title: 保険料コストを予測する機械学習ウェブアプリの作成
primary_tag: artificial-intelligence
related_content:
- slug: automate-model-building-with-autoai
  type: tutorials
- slug: get-started-watson-studio
  type: learningpaths
- slug: whats-new-on-the-ibm-data-asset-exchange
  type: blogs
subtitle: IBM Watson StudioとAutoAIを使って、線形回帰で保険料コストを予測するWebアプリケーションを作成する
tags:
- machine-learning
- python
- object-storage
title: 保険料コストを予測する機械学習ウェブアプリの作成
type: default
---

## まとめ

全世界の保険料総額が5兆ドルを超えて急増し続けている中、これらのコストのほとんどが予防可能であることがわかっています。例えば、喫煙をやめてBMIを数ポイント下げるだけで、保険料を数千ドル削減することができるかもしれません。本アプリケーションでは、年齢、喫煙、BMI、性別、地域による保険料の違いを検証しています。このアプリケーションを利用することで、お客さまは自分のライフスタイルによって保険料が大きく変わることを実感することができます。人工知能（AI）と機械学習を活用し、数秒で保険料を予測することで、お客様に喫煙による保険料の増加を理解していただくことができます。

## 説明

IBM AutoAIを使用して、さまざまな要件の予測モデルの構築に関わるすべてのタスクを自動化しています。AutoAIが優れたモデルを素早く生成することで、時間と労力を節約し、迅速な意思決定プロセスを支援していることがわかります。年齢、性別、BMI、子供の数、喫煙傾向、地域、料金などを含むデータセットからモデルを作成し、個人が支払う健康保険料を予測します。

このコードパターンを完了すると、以下の方法を理解したことになります。

* モデルを構築するために、IBM Cloud 上でサービスを迅速にセットアップする。
* データを取り込み、AutoAIプロセスを開始する
* AutoAI を使用してさまざまなモデルを構築し、パフォーマンスを評価する
* 最適なモデルを選択し、デプロイを完了する
* デプロイされたモデルを使ってRESTコールで予測を生成する
* AutoAIを使用した場合と手動でモデルを構築した場合のプロセスを比較します。
* フロントエンドアプリケーションを使用して、デプロイされたモデルを可視化する

## フロー

![Predict insurance premium flow diagram](images/create-an-application-to-predict-your-insurance-premium-cost-with-autoai.png)

1. ユーザーは、IBM Cloud 上に IBM Watson Studio サービスを作成します。
1. ユーザーは、IBM Cloud Object Storage Service を作成して、Watson Studio に追加します。
1. ユーザーは、保険料データファイルを Watson Studio にアップロードします。
1. ユーザーは、Watson Studio で保険料を予測する AutoAI Experiment を作成します。
1. AutoAI は Watson Machine Learning を使用して複数のモデルを作成し、ユーザーは最もパフォーマンスの高いモデルを展開します。
1. ユーザーは、Flask ウェブアプリケーションを使用して、デプロイされたモデルに接続し、保険料を予測します。

##指示

詳細な手順は[readme](https://github.com/IBM/predict-insurance-charges-with-ai/blob/master/README.md)ファイルに記載されています。これらの手順では、以下の方法を説明しています。

1. データセットをダウンロードする。
1. レポをクローンする。
1. データを調べる（オプション）。
1. IBM Cloud サービスを作成します。
1. AutoAI Experimentを作成して実行します。
1. デプロイメントを作成して、モデルをテストします。
1. モデルからノートブックを作成する（オプション）。
1. アプリケーションを実行します。