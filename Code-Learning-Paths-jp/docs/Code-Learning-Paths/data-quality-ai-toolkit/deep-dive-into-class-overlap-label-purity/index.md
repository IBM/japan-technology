---
authors: ''
check_date: '2022-07-08'
completed_date: '2021-07-08'
draft: false
excerpt: 分類データセットのクラスオーバーラップとラベル純度に基づくデータ品質を評価する。
menu_order: 3
meta_description: 分類データセットのクラスオーバーラップとラベル純度に基づくデータ品質を評価する。
meta_keywords: API, data science, data quality, IBM Research
meta_title: クラスのオーバーラップとラベルの純度に関する深堀り
primary_tag: artificial-intelligence
related_content:
- slug: data-analysis-using-python/
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
subtitle: 分類データセットのクラスオーバーラップとラベル純度に基づくデータ品質の評価
tags:
- deep-learning
- machine-learning
- data-science
- data
- ibm-research-content
title: クラスのオーバーラップとラベルの純度に関する深堀り
---

このチュートリアルでは、IBM API Hub プラットフォームで利用可能な Data Quality for AI API を使用して、分類された表形式 (構造化) データのクラス・オーバーラップおよびラベル純度ベースのデータ品質を評価する方法を学びます。このチュートリアルでは、クラス・オーバーラップとラベル・ピュリティのメトリクスの意味と、これらの API を呼び出して探索する方法について説明します。

## 前提条件

このチュートリアルを完了するには、以下が必要です。

* CSV形式の表形式（構造化）データセット
* Python 3

## 見積もり時間

このチュートリアルを完了するには、約15分かかります。

## データセット

このチュートリアルでは、DataHubから公開されている<a href="https://datahub.io/machine-learning/adult" target="_blank" rel="noopener noreferrer">Adult</a>のデータセットを使用します。このデータセットは、年収5万円以上であるかどうかを評価する分類タスクに基づいています。このデータセットを使って、クラスオーバーラップとラベル純度のAPIの機能を説明します。

## 初期設定

始めるには

1. 以下のAPIキーの値を記述したconfig.jsonファイルを作成します。このラーニングパスの前のチュートリアルでは、[Client IDとClient secretを取得する]方法を説明しました(https://developer.ibm.com/learningpaths/data-quality-ai-toolkit/assessing-quality-of-tabular-data-sets-using-apis/)。

インポートjson
インポート リクエスト

# config.jsonから資格情報ヘッダーを読み込む
credentials_headers = json.load(open("config.json", "r"))

with open('adult.csv', 'r') as fp:
  response = requests.post(
    'https://api.ibm.com/dataquality4ai/run/data_quality/structured/label_purity',
    headers=credentials_headers,
    files={'data_file': fp}.
  )
print("Response JSON -", response.json())

### Step 2.ジョブIDを使ってラベル純度の結果を得る

前のステップで返した `job_id` を使って、`get_result` APIコールを呼び出し、ジョブの結果やステータスを得ることができます。

#### リクエスト