---
authors: ''
completed_date: '2020-03-17'
components:
- watson-ml-accelerator
- cloud-pak-for-data
draft: false
excerpt: Watson Machine Learning Acceleratorの概要とその機能をご紹介します。
last_updated: '2021-06-22'
menu_order: 1
meta_description: Watson Machine Learning Acceleratorの概要とその機能をご紹介します。
meta_keywords: Watson Machine Learning Accelerator, Introduction, overview, get started
meta_title: Watson Machine Learning Acceleratorの紹介
primary_tag: artificial-intelligence
related_content:
- slug: use-computer-vision-with-dli-watson-machine-learning-accelerator
  type: tutorials
- slug: dynamic-resilient-and-elastic-deep-learning-with-watson-machine-learning-accelerator
  type: tutorials
- slug: accelerate-deep-learning-training-with-watson-studio-and-wml-accelerator
  type: tutorials
subtitle: Watson Machine Learning Acceleratorの概要とその機能をご紹介します。
tags:
- machine-learning
- deep-learning
- data-science
title: Watson Machine Learning Acceleratorの紹介
---

データと機械学習モデルがビジネスにもたらす価値を理解する業界のリーダーが増えるにつれ、あらゆるビジネス分野で人工知能（AI）の導入が進んでいます。市場投入までの時間を短縮して価値を高めるには、正確なモデルを作成する時間を短縮することが不可欠です。

IBM Cloud Pak for Dataは、データとAIサービスを統合した統一プラットフォームを提供し、AIの構築、実行、管理を支援します。IBM Watson Machine Learning Acceleratorは、エンド・ツー・エンドの透明性と可視性を備えたディープ・ラーニングを加速するために設計された機能で、企業や組織がディープ・ラーニングや機械学習をより利用しやすくしながら、AIアプリケーションを本番環境に導入することができます。

## Watson Machine Learning Acceleratorとは？

Watson Machine Learning Acceleratorは、ディープラーニングや機械学習をより身近なものにし、AIの恩恵をビジネスにもたらすためのエンタープライズAIインフラストラクチャです。人気の高いオープンソースの深層学習フレームワークと効率的なAI開発ツールを組み合わせています。

データサイエンティストは、ハイパーパラメータのチューニングなど、ワークロードをスケールアウトしながら、ジョブを中断することなく、フェアシェアの割り当てや優先度の高いスケジューリングに基づいて、増え続けるデータサイエンティストとGPUリソースを弾力的に共有することで、AIの旅を加速することができます。詳細については、以下のビデオをご覧ください。

<video-container><video-id>ylRRXgp1HfY </video-id><video-title display="yes"></video-title>Watson Machine Learning Accelerator 2.2 introduction</video-container>の動画です。

Watson Machine Learning Acceleratorは、Red Hat OpenShift Container PlatformとIntel&reg;サーバー上で動作するIBM Cloud Pak for Dataで利用できるようになりました。Watson Machine Learning Accelerator は、アクセラレーションされた IBM Power Systems&trade; サーバーと Intel サーバーの両方でオンプレミスで引き続き利用できます。


## Watson Machine Learning Accelerator のデプロイメント

Watson Machine Learning Accelerator は、IBM Cloud Pak for Data のサービスとしてデプロイすることも、スタンドアローンでオンプレミスにインストールすることもできます。Watson Machine Learning Accelerator をサービスとしてデプロイする方法については、<a href="https://www.ibm.com/docs/en/cloud-paks/cp-data/3.5.0?topic=overview" target="_blank" rel="noopener noreferrer">IBM Cloud Pak for Data</a> と <a href="https://www.ibm.com/docs/en/cloud-paks/cp-data/3.5.0?topic=catalog-watson-machine-learning-accelerator" target="_blank" rel="noopener noreferrer">Watson Machine Learning サービス</a> をご覧ください。また、Watson Machine Learning Accelerator をオンプレミスでインストールして設定している場合は、<a href="https://www.ibm.com/docs/en/wmla/1.2.3?topic=planning-wml-accelerator" target="_blank" rel="noopener noreferrer">Planning on installing Watson Machine Learning Accelerator 1.2.3</a>をご覧ください。

## Watson Machine Learning Accelerator の機能

Watson Machine Learning Accelerator の主な機能の概要は以下のとおりです。

### GPUを活用した深層学習の加速

Watson Machine Learning Acceleratorは、深層学習のジョブをGPUハードウェアで実行します。GPUは、企業にとって眠っていては困る特殊なハードウェアです。これらの特殊なハードウェアにより、ディープラーニングの結果を高速化し、高いスループットを実現します。トレーニングワークロードをGPUとCPUで実行した場合のスピードの違いを示すノートブックの例として、この[ビデオ](/components/watson-ml-accelerator/videos/deliver-faster-deep-learning-results-on-gpus/)をご覧ください。深層学習のトレーニングが、GPUでは最大10倍も速くなることがわかります。

### 弾性分散トレーニング

Watson Machine Learning AcceleratorのElastic Distributed Training機能は、定義されたリソースポリシーを使用して、複数の実行中のジョブでGPUの共有と再割り当てを可能にします。リソースポリシーは、ビジネスライン、プロジェクト、またはユーザー間で定義することができ、GPUリソースの公平な割り当てと優先的なアクセスを保証します。データサイエンティストが深層学習のトレーニングジョブを提出すると、ジョブは自動的に共有リソースに割り当てられ、トレーニングワークロードの配分が簡素化されます。

[ビデオ](/videos/balance-deep-learning-jobs-with-elastic-distributed-training/)では、Elastic Distributed Trainingがどのように深層学習ジョブをバランスよく配置するかをご覧いただけます。

### ハイパーパラメータ最適化の自動化

ハイパーパラメータ最適化の自動化は、データサイエンティストがハイパーパラメータの検索を並行して自動化することで、トレーニングの速度を最適化するのに役立ちます。Watson Machine Learning Accelerator API を使用して、ハイパーパラメータ最適化トレーニングを自動化する方法をご覧ください(/videos/Automatehyperparameter-optimization-training-with-the-wml-accelerator-api/)。

### 弾性分散推論

推論モデルをサービスとして公開します。Watson Machine Learning Accelerator for Cloud Pak for Data での推論のダウンロードと設定については、<a href="https://www.ibm.com/docs/en/wmla/2.2.0?topic=inference-download-configure-dlim-cli-tool" target="_blank" rel="noopener noreferrer">コマンドラインツールのダウンロード</a>を参照してください。Watson Machine Learning Accelerator をオンプレミスで使用する場合は、<a href="https://www.ibm.com/docs/en/wmla/1.2.3?topic=inference-using-services-via-cli" target="_blank" rel="noopener noreferrer">コマンドラインツール</a>を設定します。

## 結論

本記事では、Watson Machine Learning Accelerator の概要とその機能について説明しました。Watson Machine Learning Accelerator のインストールや設定、使用方法については、[How to use Watson Machine Learning Accelerator](/articles/accelerate-dl-with-wmla-and-cp4d/)をご覧ください。