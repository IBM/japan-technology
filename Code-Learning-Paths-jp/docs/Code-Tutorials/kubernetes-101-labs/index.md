---
also_found_in:
- learningpaths/get-started-containers/
authors: ''
check_date: '2021-06-30'
completed_date: '2018-12-09'
components:
- docker
- kubernetes
draft: false
excerpt: Dockerイメージを構築してKubernetesクラスタにデプロイする方法、アプリケーションのデプロイを制御する方法、AIサービスを追加する方法、クラスタを安全に監視する方法などをご紹介します。
last_updated: '2021-01-16'
meta_description: Dockerイメージを構築してKubernetesクラスタにデプロイする方法、アプリケーションのデプロイを制御する方法、AIサービスを追加する方法、クラスタを安全に監視する方法などをご紹介します。
meta_keywords: kubernetes 101, kubernetes labs, kubernetes training, kubernetes exercises
meta_title: Kubernetes 101：Kubernetesを理解するためのラボです。
primary_tag: containers
related_content:
- slug: kubernetes-learning-path
  type: series
- slug: get-started-containers
  type: learningpaths
subtitle: Dockerコンテナイメージを構築し、アプリをKubernetesクラスタにデプロイする方法
time_to_read: 3 hours
title: Kubernetes 101：Kubernetesを理解するためのラボです。
---

あなたはKubernetesについて学びたいと思っていますが、このトピックに関する記事やブログ記事の量に完全に圧倒されていますか？聞いたことはあるし、他の人のコードで見たこともあるけど、実際に何ができるの？それはあなたのコンテナにどのように役立つのでしょうか？Kubernetesはコンテナの一種ですか？この一連のラボは、混乱を解消し、Kubernetesを快適に使えるようにするためのものです。これらは、開発者であるあなたを念頭に置いて設計されています。

このラボを完了すると、以下のことが得られます。

* Kubernetesのコアコンセプトを完全に理解する。
* IBM Cloud Kubernetes ServiceのKubernetes上でDockerイメージを構築し、アプリケーションをデプロイする方法に関する知識
* インフラストラクチャ管理にかかる時間を最小限に抑えながら、制御されたアプリケーションのデプロイメント
* アプリを拡張するためにAIサービスを追加するスキル
* より安全なクラスタとアプリ、およびそれらを監視する方法の理解

これらのラボのすべての演習を完了するには、約3時間かかります。まずはいくつかの演習を試してみてください。

## 前提条件

これらのラボでは、IBM Cloud の有料アカウントまたはサブスクリプション・アカウントを持つ無料の Kubernetes クラスターを使用します。はじめに、<a href="https://cloud.ibm.com/registration/?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg" target="_blank" rel="noopener noreferrer">IBM Cloud アカウント</a>に登録します。その後、<a href="https://ibm.github.io/workshop-setup/PAYASYOUGO/" target="_blank" rel="noopener noreferrer">このガイド</a>に従って、Pay-As-You-Goアカウントにアップグレードします。

##ラボ

* <a href="https://ibm.github.io/kube101/Lab0/" target="_blank" rel="noopener noreferrer">__Lab 0. Access a Kubernetes cluster__</a>
ハンズオンラボのためには、Kubernetesクラスタが必要です。このラボでは、IBM Cloud Kubernetes Service、ホストされたトライアル環境、ローカル・ワークステーションで実行するためのKubernetesの構成など、クラスターを作成するためのオプションについて説明します。また、IBM Cloud のコマンドライン・ツールと Kubernetes CLI をインストールし、実習用のサンプル Guestbook アプリケーションをダウンロードするためのウォークスルーを提供します。

* <a href="https://ibm.github.io/kube101/Lab1/" target="_blank" rel="noopener noreferrer">__Lab 1.最初のアプリケーションをデプロイする__</a
Go で書かれたシンプルな Guestbook アプリケーションを、IBM Cloud Kubernetes Service 内でホストされている Kubernetes クラスターにデプロイします。

* <a href="https://ibm.github.io/kube101/Lab2/" target="_blank" rel="noopener noreferrer">__Lab 2.デプロイメントの拡張と更新__</a
デプロイメント内のインスタンス数を更新する方法と、Kubernetes 上でアプリケーションのアップデートを安全にロールアウトする方法を学びます。

* <a href="https://ibm.github.io/kube101/Lab3/" target="_blank" rel="noopener noreferrer">__Lab 3.マルチティアアプリケーションの構築__</a
同じGuestbookアプリケーションを、`kubectl`コマンドラインヘルパー関数ではなく、設定ファイルを使ってデプロイする方法を学びます。設定ファイルの仕組みを利用することで、Kubernetesクラスタ内に作成されるすべてのリソースをより細かく制御することができます。