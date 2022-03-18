---
authors: ''
check_date: '2022-07-08'
completed_date: '2021-07-08'
draft: false
excerpt: いくつかのAPIコールを呼び出すことで、データセットのデータ品質評価を取得する方法をステップバイステップで説明します。
menu_order: 2
meta_description: いくつかのAPIコールを呼び出すことで、データセットのデータ品質評価を取得する方法をステップバイステップで説明します。
meta_keywords: API, data science, data quality, IBM Research
meta_title: APIを使って表形式のデータセットのデータ品質を評価する
primary_tag: artificial-intelligence
related_content:
- slug: data-analysis-using-python
  type: learningpaths
- slug: analyzing-geospatial-environment-data
  type: tutorials
related_links:
- title: Data Quality for AI APIs
  url: https://www.ibm.com/products/dqaiapi
- title: API Documentation
  url: https://developer.ibm.com/apis/catalog/dataquality4ai--data-quality-for-ai/Introduction
- title: Slack workspace [Request an invite]
  url: https://join.slack.com/t/dqai/shared_invite/zt-ra98jfbm-KgZwRlokg~5_3_A7FyFm3g
subtitle: いくつかのAPIコールを呼び出すことで、データセットのデータ品質評価を得る方法をステップバイステップで説明しています。
tags:
- deep-learning
- machine-learning
- data-science
- data
- ibm-research-content
title: APIを使って表形式のデータセットのデータ品質を評価する
---

IBM Researchが提供する<a href="https://developer.ibm.com/apis/catalog/dataquality4ai--data-quality-for-ai/Introduction" target="_blank" rel="noopener noreferrer">Data Quality for AI</a>は、さまざまなデータ・プロファイリングや品質評価メトリクスを提供し、取り込まれたデータの品質を体系的かつ客観的に評価するためのAPIスイートです。このチュートリアルでは、いくつかのAPIコールを呼び出すことで、データ・セットのデータ品質評価を得る方法をステップ・バイ・ステップで説明します。また、APIを使い始めるのに役立つ詳細なコード例もご紹介します。このチュートリアルでは、IBM API Hub プラットフォームで Data Quality for AI のトライアル・サブスクリプションにアクセスするなど、いくつかの基本的な手順を説明します。  

このチュートリアルでは、Pythonコード・スニペットを使用して完全なユースケースを紹介しています。ただし、API を呼び出すために独自のプログラミング言語を選択することができます。リファレンス・コード・スニペットは、<a href="https://developer.ibm.com/apis/catalog/dataquality4ai--data-quality-for-ai/Introduction" target="_blank" rel="noopener noreferrer">API documentation</a>ページで、一部の言語(例えば、cURL、Java、Node、PHP、Go、Swift、Ruby)に対応しています。利用可能なデータ品質APIについては、このチュートリアルを利用することができます。

* クラスオーバーラップ
* クラス・パリティ
* ラベルの純度
* 外れ値検出
* データの重複
* データの同質性
* データプロファイラ
* データの完全性
* 相関関係の検出

## 前提条件

このチュートリアルを完了するには、以下のものが必要です。

* IBM ID
* CSV形式の表形式（構造化）データセット
* Python 3

## 見積もり時間

このチュートリアルを完了するには、約15分かかります。

## 手順

### ステップ 1.環境設定

環境を整えるために

1. <a href="https://developer.ibm.com/apis/catalog/dataquality4ai--data-quality-for-ai/Introduction/" target="_blank" rel="noopener noreferrer">Data Quality for AI</a> APIsのドキュメントページに移動し、「**Get trial subscription**」をクリックします。

    ![Data Quality for AIの概要ページ](images/DQA-dashboard.png)

1. 新しいタブで登録ページが起動します。すでにIBM IDをお持ちの方は、**Log in**を選択してください。IBM IDをお持ちでない方は、新規にIBM IDを作成してください。

1. ログインすると、システムはお客様にトライアル・サブスクリプションの権利を与え、My IBM ページに移動します。Data Quality for AI API 試用版のタイルを見つけて、**Launch**をクリックします。

1. My APIs］ページで［Data Quality for AI］タイルをクリックし、ページが開いたら［Key management］セクションを見つけます。行を展開して、クライアントIDとクライアントシークレットの両方を確認します。可視性（目）のアイコンをクリックすると、実際の値が表示されます。これらの値は、このチュートリアルで使用するAPIキーなので、注意してください。

    ![鍵管理ページ](images/key-management.png)

1. 受け取ったAPIキーの値でconfig.jsonファイルを作成します。