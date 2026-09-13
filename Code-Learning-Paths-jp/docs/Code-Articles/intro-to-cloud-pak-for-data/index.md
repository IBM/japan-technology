---
also_found_in:
- /learningpaths/cloud-pak-for-data-learning-path/
authors: ''
completed_date: '2019-10-06'
components:
- cloud-pak-for-data
draft: false
excerpt: IBM Cloud Pak for Dataの紹介
ignore_prod: false
last_updated: '2020-02-25'
meta_description: IBM Cloud Pak for Dataの紹介
meta_keywords: cloud pak for data, introduction, overview
meta_title: IBM Cloud Pak for Dataの紹介
primary_tag: analytics
subtitle: IBM Cloud Pak for Dataの基本を学ぶ
tags:
- analytics
- data-management
- data-science
- databases
- machine-learning
title: IBM Cloud Pak for Dataの紹介
---

[IBM Cloud Pak for Data](https://www.ibm.com/jp-ja/products/cloud-pak-for-data)は、[Red Hat OpenShift Container platform](https://www.openshift.com/products/container-platform)上でネイティブに動作し、IBM Cloud、Amazon Web Services(AWS)、Microsoft Azureなど多くのクラウドプラットフォーム上で動作する、統合済みのデータおよびAIプラットフォームです。サービスは、データを収集、整理、分析するためのオープンで拡張可能なクラウドネイティブプラットフォームで提供されます。ガバナンスが組み込まれたエンドツーエンドのアナリティクスを行うための単一のインターフェースです。また、エンドツーエンドのAIワークフローをサポートし、ガバナンスをかけます。

### データを収集する

* すべてのデータにアクセスできるようにし、移行の必要がなく、ソースから安全にアクセスできるようにします。
* すべてのデータに接続し、データサイロを解消します。

### データの整理

* データの準備、ポリシー、セキュリティ、コンプライアンスを簡素化できる、信頼できるビジネス対応の分析基盤を構築します。
* データとAIのライフサイクルを管理・自動化する。

### あなたのデータを分析する

* 組織全体で一貫して拡張するAIおよび機械学習機能を構築、展開、管理します。

### AIの導入

* 信頼性と透明性をもって、ビジネス全体でAIを運用することができます。
* ベンダーロックインを回避し、どこでも俊敏に実行できます。

IBM Cloud Pak for Dataは、AIへの旅を加速するための規定のアプローチを提供します。これは、お客様が旅のどの段階にいても、ビジネスのデジタル変革を推進できるように開発されたAI Ladderです。IBM Cloud Pakは、重要なクラウド、データ、AIのすべての機能をコンテナ化されたマイクロサービスとしてまとめ、マルチクラウド・プラットフォームでAI Ladderを提供します。

## 製品のウォークスルーをする

IBM Cloud Pak for Dataは、データの価値を引き出し、AIのための情報アーキテクチャを構築するのに役立ちます。この製品ウォークスルーでは、スケーラブルなKubernetesプラットフォームを使って、データを収集、整理、分析し、AIを注入する方法をステップ・バイ・ステップでデモンストレーションしています。

<iframe width="560" height="315" src="https://www.youtube.com/embed/oPN_FhGZSCg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 建築

IBM Cloud Pak for Dataは、マルチノードのIBM Cloudプライベート・クラスター上で実行される構成済みのマイクロサービスで構成されています。マイクロサービスは、データ・ソースへの接続を可能にし、単一の Web アプリケーションからデータのカタログ化と管理、探索とプロファイリング、変換、および分析を行うことができます。

IBM Cloud Pak for Dataは、Red Hat OpenShiftを使用して、マルチノードのKubernetesクラスターにデプロイされます。IBM Cloud Pak for Dataは3ノードのクラスターにデプロイすることもできますが、パフォーマンスの向上、クラスターの安定性、ワークロードの増加をサポートするためのクラスターのスケーリングのしやすさを考慮して、本番環境は最低でも6ノードのクラスターにデプロイすることを強く推奨します。

## まとめ

この記事では、IBM Cloud Pak for Dataを紹介し、関連する用語や概念を説明し、製品のウォークスルーを提供し、アーキテクチャの概要を紹介しました。