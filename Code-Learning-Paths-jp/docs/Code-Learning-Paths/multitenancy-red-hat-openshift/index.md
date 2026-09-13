---
authors: ''
check_date: '2022-08-30'
completed_date: '2021-08-31'
components:
- openshift
- kubernetes
display_in_listing: true
draft: false
excerpt: このラーニングパスは、Red Hat OpenShiftでマルチテナント環境を迅速に構築することに興味がある方を対象としています。
meta_description: このラーニングパスは、Red Hat OpenShiftでマルチテナント環境を迅速に構築することに興味がある方を対象としています。
meta_keywords: multitenancy OpenShift, multitenant environments, RBAC, network isolation,
  resource isolation
primary_tag: containers
related_content:
- slug: build-images-cloud-native-toolkit
  type: learningpaths
- slug: secure-context-constraints-openshift
  type: learningpaths
subtitle: Red Hat OpenShiftでマルチテナント環境を構築する方法を紹介します。
tags:
- security
- devops
title: OpenShiftでマルチテナンシーを始めよう
---

このラーニングパスは、Red Hat OpenShift でマルチテナント環境を素早く設定することに興味のある方を対象としています。このラーニングパスは、マルチテナンシーとは何か、その利点、そしてマルチテナンシー環境について知っておくべき様々な側面を説明する入門記事で構成されています。また、このラーニングパスには、以下に示すマルチテナンシーのさまざまな側面について、ステップバイステップの詳細なチュートリアルが含まれています。

* OpenShiftプロジェクトへのロールベースのアクセスコントロール
* テナントのネットワークの分離
* テナント用のリソースの分離

それぞれの内容をもう少し詳しく見てみましょう。

### 記事Red Hat OpenShiftにおけるマルチテナンシーの紹介

この記事では、以下のようなマルチテナンシーに関連するコアなコンセプトを紹介します。

* マルチテナンシーの定義
* マルチテナンシーの利点
* マルチテナンシーを実現するためのオプション
* IBM Cloudでマルチテナンシーを実現するためのOpenShiftコンテナの構成

<button-link><text>Read the article</text><url>https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/introduction</url>
</button-link> </button-link

### チュートリアルロールベースのアクセスコントロール

このチュートリアルを終了すると、以下の方法を学ぶことができます。

* ユーザーの作成
* ロールバインディングの作成
* ユーザーになりすましてアプリケーションをデプロイする
* ポッドの作成とデプロイ
* 別のユーザーに切り替える

<button-link><text>Complete the tutorial</text><url>https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/rbac</url>
</button-link> </button-link

### チュートリアルです。ネットワーク分離を利用してOpenShiftにデプロイしたアプリケーションを保護する

このチュートリアルを終了すると、以下の方法を学ぶことができます。
* OpenShift でプロジェクトを作成し、Open Liberty 上で動作する Web アプリケーションを odo を使用してデプロイします。
* プロジェクトにネットワークポリシーを使用してマルチテナントアイソレーションを設定する
* マルチテナント・モードの設定をテストする

<button-link><text>Complete the tutorial</text><url>https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/network-isolation</url>
</button-link> </button-link

### チュートリアルリソースアイソレーションを使ってOpenShiftにデプロイしたアプリケーションを保護する

このチュートリアルを終了すると、以下のことがわかるようになります。

*このチュートリアルを終えると、以下のことができるようになります： * 同じプロジェクトにデプロイされた 2 つの異なるアプリケーションのパフォーマンスを観察する。
* 2つの異なるプロジェクトにデプロイされた2つの異なるアプリケーションのパフォーマンスを観察する
* リソースクォータ（CPU、メモリ）をプロジェクトに割り当て、再度アプリケーションのパフォーマンスを観察する。

<button-link><text>Complete the tutorial</text><url>https://developer.ibm.com/learningpaths/multitenancy-red-hat-openshift/resource-isolation</url>
</button-link> </button-link