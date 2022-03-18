---
abstract: このチュートリアルでは、クレジット・リスクのユースケースでAutoAIサービスの利点を説明し、回帰や分類の問題がコードなしでどのように処理されるか、またこのサービスでどのようにタスク（フィーチャー・エンジニアリング、モデル選択、ハイパーパラメーター・チューニングなど）が行われるかについて理解を深めていただきます。このチュートリアルでは、パイプラインの中から最適なモデルを選択する方法や、IBM
  Cloud Pak for Dataプラットフォームを介してこれらのモデルをデプロイして使用する方法についても詳しく説明しています。
also_found_in:
- /learningpaths/cloud-pak-for-data-learning-path/
authors: ''
completed_date: '2020-01-15'
components:
- cloud-pak-for-data
- watson-studio
content_tags:
- hcbt
draft: false
excerpt: このチュートリアルでは、クレジット・リスクのユースケースでAutoAIサービスの利点を説明し、回帰や分類の問題がコードなしでどのように処理されるか、またこのサービスでどのようにタスク（フィーチャー・エンジニアリング、モデル選択、ハイパーパラメーター・チューニングなど）が行われるかについて理解を深めていただきます。このチュートリアルでは、パイプラインの中から最適なモデルを選択する方法や、IBM
  Cloud Pak for Dataプラットフォームを介してこれらのモデルをデプロイして使用する方法についても詳しく説明しています。
ignore_prod: false
last_updated: '2021-07-16'
meta_description: このチュートリアルでは、クレジット・リスクのユースケースでAutoAIサービスの利点を説明し、回帰や分類の問題がコードなしでどのように処理されるのか、またこのサービスでどのようにタスク（フィーチャー・エンジニアリング、モデル選択、ハイパーパラメーター・チューニングなど）が行われるのかについて理解を深めていただきます。このチュートリアルでは、パイプラインの中から最適なモデルを選択する方法や、IBM
  Cloud Pak for Dataプラットフォームを介してこれらのモデルをデプロイして使用する方法についても詳しく説明しています。
meta_title: AutoAIによるモデル構築の自動化
primary_tag: analytics
services:
- watson-studio
subtitle: 回帰問題や分類問題をコードレスで処理できる方法を紹介
tags:
- artificial-intelligence
- machine-learning
- hcbt
title: AutoAIによるモデル構築の自動化
type: tutorial
---

AIのためのAIを作ることを目的に、IBMはWatson&trade;Studio上に[AutoAI](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.0?topic=models-autoai)というサービスを導入しました。

AutoAIは、データサイエンティストの作業を楽にするために、機械学習のタスクを自動化する機能です。モデリングのためのデータの準備、問題に最適なアルゴリズムの選択、学習したモデルのパイプラインの作成などを自動的に行い、パブリック・クラウドでも、IBM Cloud Pak for Dataをはじめとするプライベート・クラウドでも実行することができます。

## 学習目標

このチュートリアルでは、AutoAI サービスの利点をユースケースで説明します。これにより、回帰や分類の問題がどのようにコードなしで処理されるのか -- そして、このサービスでどのようにタスク（フィーチャー・エンジニアリング、モデル選択、ハイパーパラメータ・チューニングなど）が行われるのかについて理解を深めることができます。このチュートリアルには、パイプラインの中から最適なモデルを選択するための詳細や、IBM Cloud Pak for Dataプラットフォームを介してこれらのモデルをデプロイして使用する方法も含まれています。

## 前提条件

* [IBM Cloud Pak for Data](https://www.ibm.com/analytics/cloud-pak-for-data)

## 想定される時間

このチュートリアルの所要時間は約20分(AutoAIのトレーニングを含む)で、以下のステップに分かれています。

このセクションは、以下のステップに分かれています。

1. [プロジェクトとAutoAIインスタンスの作成](#1-create-a-project-and-autoai-instance)
1. [AutoAI実験の実行](#2-run-autoai-experiment)
1. [AutoAIモデルの保存](#3-save-autoai-model)
1. [AutoAIノートの保存](#4-save-autoai-notebook)
1. [モデルを宣伝する](#5-モデルを宣伝する)

## 1.プロジェクトとAutoAIインスタンスの作成

このラーニングパスのためのプロジェクトをまだ作成していない場合は、以下の指示に従ってプロジェクトを作成してください。そうでない場合は、[AutoAI実験の実行](#1-run-autoai-experiment)にスキップできます。

### IBM Cloud Pak for Data プロジェクトの作成

Cloud Pak for Dataでは、特定の目標を達成するために使用するリソース(問題に対する解決策を構築するためのリソース)を収集/整理するために、プロジェクトという概念を使用しています。プロジェクトのリソースには、データ、共同研究者、ノートブックやモデルなどの分析資産などがあります。

* (☰)ナビゲーションメニューの「プロジェクト」セクションで、「すべてのプロジェクト」をクリックします。

  ![(☰)メニュー -> プロジェクト](images/menu-projects.png)

* `右上にある **New project`** ボタンをクリックします。

  ![新しいプロジェクトを開始](images/new-project.png)

* `Analytics project` のラジオボタンを選択して、 **`Next`** ボタンをクリックします。

  ![新規アナリティクスプロジェクト](images/new-project-type.png)

* ****``Create an empty project``を選択します。

  ![空のプロジェクトの作成](images/cpd-create-empty-project.png)

* `プロジェクトの名前とオプションの説明を入力し、 **Create`** をクリックします。

  ![Pick a name](images/project-name.png)

### この実験のデータセットをダウンロードして、プロジェクトに読み込みます。

* [german_credit_data.csv](static/german_credit_data.csv) データセットをダウンロードします。

* **Browse** をクリックし、ダウンロードしたファイルを選択して、データセットを分析プロジェクトにアップロードします。

## 2.AutoAI実験の実行

* AutoAI 実験を開始するには、ページ上部の *`Add to Project`* ボタンをクリックし、`AutoAI experiment` を選択します。

  ![プロジェクトの追加](images/autoai-add-project.png)

* AutoAI experiment assetに名前を付け、ドロップダウンメニューにデフォルトのcompute configurationオプションを残します。そして、`Create`ボタンをクリックします。

  ![Naming your services](images/autoai-name-experiment.png)

* 実験を設定するには、まず機械学習モデルの学習に使用するデータセットを与える必要があります。ここでは、プロジェクトにあらかじめ読み込まれているCSVファイルのデータセットの1つを使用します。「プロジェクトから選択」オプションをクリックします。

  ![Select data](images/autoai-select-dataset-project.png)

* ダイアログで、`german_credit_data.csv` ファイルを選択して、`Select asset` ボタンをクリックします。

  ![データの選択](images/autoai-select-dataset.png)

**** データセットが読み込まれたら、モデルに予測させたい内容を指定する必要があります。*Select prediction column*パネルで、`Risk`の行を探してクリックしてください。

* AutoAIは、データセットと予測のために選択された列に基づいて、実験のためのデフォルト値を設定します。これには、構築するモデルの種類、最適化するメトリクス、テスト/トレーニングの分割などが含まれます。これらの値を表示/変更するには、*`Experiment settings`*ボタンをクリックします。

  ![Choose Churn column and run](images/autoai-choose-prediction-and-configure.png)

* `Data source settings` パネルの `Select columns to include` セクションで、`CustomerID` カラム名のチェックボックスの選択を外します。これにより、モデルの機能として顧客IDカラムが使用されなくなります。実験の他の部分を変更することもできますが、ここでは残りのデフォルト値を受け入れて、`Save settings`ボタンをクリックします。

  ![Choose features and save](images/autoai-exp-settings-columns.png)

* 実験を開始するには、`Run experiment`ボタンをクリックします。

  ![Run experiment](images/autoai-exp-run.png)

* AutoAIの実験が実行されます。AutoAIは、データセットを準備し、データセットを学習/評価グループに分割し、モデルの種類に応じて最もパフォーマンスの高いアルゴリズム/推定量を見つけるステップを実行します。そして、上位N個のアルゴリズムのそれぞれについて、以下の一連の候補パイプラインを構築します（ここで、Nは設定で選択した数で、デフォルトは2です）。

    * ベースラインモデル（パイプライン1）
    * ハイパーパラメータの最適化（パイプライン2）
    * 自動フィーチャーエンジニアリング（パイプライン3）
*    ハイパーパラメータの最適化（パイプライン4） * エンジニアリングされたフィーチャーの上でのハイパーパラメータの最適化

* 異なるアルゴリズム／評価者が選択され、異なるパイプラインが作成・評価されると、UIに進捗が表示されます。完了したパイプラインのパフォーマンスは、リーダーボードで各パイプラインのセクションを展開することで確認できます。

  ![autoai progress](images/autoai-pipeline-progress.png)

* 実験の実行には数分かかることがあります。完了すると、パイプラインが作成されたというメッセージが表示されます。実験が完了するまで次のセクションには進まないでください。

## 3.AutoAIモデルの保存

* 実験が完了すると、UIで様々なパイプラインやオプションを検討することができます。利用可能なオプションには、パイプラインの比較、別のパフォーマンス指標に基づくランキングの変更、実験のログの表示、パイプラインのランク付けされたリストの表示などがあります（実験の最適化指標（ここでは精度）に基づくランキング）。

  ![autoai pipelines created](images/autoai-pipelines-complete.png)

* 下にスクロールすると、*Pipeline leaderboard*が表示されます。トップパフォーマンスのパイプラインが1位になっています。

* 次のステップでは、最も良い結果を出したモデルを選択し、そのパフォーマンスを確認します。今回の実験では、Pipeline 4が最も良い結果を出しました。リーダーボードから該当するパイプライン名をクリックすると、詳細な結果を見ることができます。

  ![pipeline leaderboard](images/autoai-pipeline-leaderboard-topranked.png)

* モデルの評価ページでは、実験のメトリクス、混同行列、実行された特徴変換（もしあれば）、どの特徴がモデルに寄与しているか、パイプラインの詳細などが表示されます。オプションとして、パイプラインの詳細をクリックして見ることができます。

  ![モデル評価](images/autoai-toppipeline-details.png)

* このモデルをデプロイするには、*`Save as`* ボタンをクリックします。次の画面で、`モデル`を選択してください。デフォルトの名前のままか、変更して、オプションで説明やタグを追加して、`Create`をクリックして保存します。

  ![モデルの保存](images/autoai-pipelin-save-model.png)

* モデルがプロジェクトに保存されたことを示す通知が届きます。モデルがプロジェクトに保存されたことを示す通知が届きます。通知を見てプロジェクトに戻るには、`View in project`をクリックするか、左上のナビゲーターでプロジェクト名をクリックしてプロジェクトのメインページに戻ります。

  ![プロジェクトの選択](images/autoai-project-navigator.png)

* *Assets*ページの*Models*セクションに新しいモデルが表示されます。

## 4.4. AutoAIノートブックの保存

* AutoAIの実験をノートブックとして保存するには、選択したパイプラインのウィンドウに戻り、「Save as」をクリックします。

> *注：パイプラインのウィンドウに戻るには、プロジェクトの概要ページを開き、AutoAI実験をクリックして、リーダーボードからパイプラインをクリックします*。

  ![ノートブックの保存](images/autoai-toppipeline-details.png)

* `Notebook` タイルを選択し、デフォルトの名前を受け入れるか、必要に応じて変更します。オプションで説明やタグを追加して、「Create」をクリックします。

  ![Name and create notebook](images/autoai-save-as-notebook.png)

* ノートブックがプロジェクトに保存されたことを示す通知が表示されます。パイプラインの詳細ウィンドウを閉じて、画面の上部にプロジェクトに戻るパスを露出させます。あなたのプロジェクト名をクリックして、プロジェクトの概要ページに移動します。

  ![プロジェクトへのナビゲート](images/autoai-navigate-to-project.png)

* ノートブックはプロジェクトに保存され、詳細な検討や変更、修正、新しいモデルの作成に利用することができます。詳細は、[Modifying and running an AutoAI generated notebook](static/running-autoai-notebook.md)のドキュメントを参照してください。

## 5.モデルをプロモートする

* モデルを保存したら、次はデプロイスペースでモデルを利用できるようにして、デプロイできるようにする必要があります。「アセット」ページの「モデル」セクションで、保存したモデルの名前をクリックします。

  ![AIモデルの選択](images/autoai-choose-asset-ai-model.png)

* モデルをデプロイできるようにするには、先に設定したデプロイメントスペースで利用できるようにする必要があります。`Promote to deployment space`をクリックしてください。

  ![Deploying the model](images/autoai-promote-to-space.png)

***> ***注：ここでは、ワークショップの *pre-work* セクションでデプロイメントスペースを既に作成していることを前提としています。

* 必要に応じて、任意の説明やタグを追加してください。*`Promote`*ボタンをクリックしてください。

  ![Promote model](images/autoai-promote-to-space-confirm.png)をクリックします。

* モデルが正常にデプロイメントスペースに昇格したことを示す通知が表示されます。

  ![デプロイメントスペースの作成](images/autoai-promotion-success.png)

## Conclusion

本節では、Cloud Pak for Data上で機械学習モデルを構築するための1つのアプローチを取り上げました。AutoAIは、以下のようなタスクを自動化することで、最適なモデルを見つけるのに役立つことを見てきました。

* データ整理
* モデルアルゴリズムの評価と選択
* フィーチャーエンジニアリング
* ハイパーパラメータの最適化

AutoAIについてもっと知りたいですか？では、[Use AutoML to find and deploy the best models in minutes](https://developer.ibm.com/technologies/artificial-intelligence/learningpaths/explore-autoai/)をご覧ください。