---
also_found_in:
- learningpaths/explore-autoai/
authors: ''
check_date: '2021-09-28'
completed_date: '2020-09-30'
components:
- watson-studio
draft: false
excerpt: 機械学習モデルのPythonコードを含むJupyter Notebookを自動的に生成します。
github:
- button_title: Get the code
  url: https://github.ibm.com/ibm-developer-eti-ai-analytics/AutoAI-code-generation
last_updated: '2020-09-30'
meta_description: 機械学習モデルのPythonコードを含むJupyter Notebookを自動生成します。
meta_keywords: watson machine learning, machine learning, python, jupyter notebook,
  models, machine learning models, autoai
meta_title: AutoAIを使ってパイプラインモデルのPythonノートブックを生成する
primary_tag: artificial-intelligence
related_content:
- slug: explore-autoai
  type: learningpaths
- slug: introduction-to-autoai
  type: blogs
- slug: build-a-predictive-model-using-tweets
  type: tutorials
subtitle: 機械学習モデルのPythonコードを含むJupyter Notebookを自動的に作成する
tags:
- machine-learning
- python
- jupyter
title: AutoAIを使ってパイプラインモデルのPythonノートブックを生成する
---

## まとめ

このコードパターンでは、AutoAI を使用して、機械学習モデルの Python コードを含む Jupyter Notebook を自動的に生成する方法を学びます。その後、Watson Machine Learning API を使用して IBM Watson&reg; Machine Learning にモデルをデプロイする前に、Python を使用してモデルパイプラインを探索、修正、再学習します。

## 説明

AutoAI は IBM Watson Studio 内で利用できるグラフィカルなツールで、データセットを分析して複数のモデルパイプラインを生成し、問題に対して選択されたメトリックに基づいてそれらをランク付けします。このコードパターンは、AutoAI の拡張機能を示しています。同じデータセットに対するより基本的な AutoAI の探索については、[Generate machine learning model pipelines to choose the best model for your problem](/tutorials/generate machine-learning-model-pipelines-to-choose-the-best-model-for-your-problem-autoai/) チュートリアルで説明しています。

このコードパターンを完了すると、以下の方法を理解したことになります。

* AutoAIの実験を行う
* Pythonノートブックの生成と保存
* ノートブックを実行して結果を分析する
* Watson Machine Learning SDK を使用してモデルを変更および再学習する
* ノートブック内から Watson Machine Learning を使用してモデルをデプロイする

## フロー

![フロー](images/autoai-code-generation-flow.png)

1. ユーザーは、デフォルトの設定でAutoAI実験を提出する。
1. 複数のパイプラインモデルが生成される。リーダーボードから選択したパイプラインモデルがJupyter Notebookとして保存される。
1. Jupyter Notebookが実行され、修正されたパイプラインモデルがノートブック内に生成される。
1. パイプラインモデルは、Watson Machine Learning API を使用して Watson Machine Learning にデプロイされます。

##指示

詳細な手順は、[readme](https://github.com/IBM/AutoAI-code-generation/blob/master/README.md)ファイルに記載されています。これらの指示は、以下の方法を説明しています。

1. AutoAIの実験を行う。
1. AutoAIが生成したノートブックを保存する。
1. ノートブックを読み込んで実行する。
1. Watson Machine Learning インスタンスを使用して Web サービスとしてデプロイし、スコアリングします。