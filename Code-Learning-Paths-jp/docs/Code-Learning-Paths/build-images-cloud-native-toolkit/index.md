---
authors: ''
check_date: '2022-06-30'
completed_date: '2021-06-30'
components:
- openshift
- kubernetes
- devops
display_in_listing: true
draft: false
excerpt: オープンソースのCloud-Native Toolkitのビルドパイプラインを使用して、Red Hat Certificationに合格するイメージを作成します。
meta_description: オープンソースのCloud-Native Toolkitのビルドパイプラインを使用して、Red Hat Certificationに合格するイメージを作成します。
meta_keywords: universal application images, cloud-native toolkit
primary_tag: containers
related_content:
- slug: introduction-to-kubernetes-operators
  type: articles
- slug: how-operators-extend-kubernetes-functionality
  type: articles
subtitle: Cloud-Native Toolkitのビルドパイプラインを使用して、Red Hat Certification用のイメージを作成する。
title: Cloud-Native Toolkitによるイメージの構築
---

KubernetesやRed Hat OpenShiftでうまく動作するために必要なすべての要件を満たす[ユニバーサルアプリケーションイメージ](/learningpaths/universal-application-image)を構築することは、圧倒されるように感じることがあります。オープンソースのCloud-Native Toolkitを使用すると、うまく構築されたイメージを簡単に作成することができます。

[Cloud-Native Toolkit](https://cloudnativetoolkit.dev/)には、イメージ構築のベストプラクティス、ツール、学習教材が多数含まれており、反復可能で保守可能なプロセスも用意されています。このツールキットは、ソフトウェア開発ライフサイクル (SDLC) 全体を通じて使用でき、Red Hat Container Certification 用のユニバーサルアプリケーションイメージを構築する機能を含め、完全なアプリケーションを開発することができます。このツールキットは、KubernetesやOpenShiftのクラスター、IBM Cloud、その他の場所で実行できます。

## 前提条件

このラーニングパスのチュートリアルを完了するには、クラスター管理者がCloud-Native ToolkitをRed Hat OpenShiftクラスターにインストールする必要があります。この作業はクラスター上で一度だけ行う必要があり、その後は複数のプロジェクトで使用することができます。

- [クラウドネイティブツールキットのインストール](/learningpaths/build-images-cloud-native-toolkit/install-toolkit)

## 手順と成果

### 1.スターターキットから始める

Cloud-Native Toolkitの使い方を知るために、最初のチュートリアルから始めます。[Use the Cloud-Native Toolkit starter kits](/learningpaths/build-images-cloud-native-toolkit/starter-kits)

このチュートリアルはあなたを助けます。

   * Cloud-Native Toolkitの使い方を学ぶ。
   * CI パイプラインの作成と実行
   * コンテナとしてデプロイされるクラウド・ネイティブ・アプリケーションの構築

### 2.既存のアプリケーションとCloud-Native Toolkitを使って、イメージを構築する。

Cloud-Native Toolkitを使ってコンテナ化したい既存のアプリケーションが単一のレポにある場合は、チュートリアルの指示に従ってください。
[Use Cloud-Native Toolkit on an existing application](/learningpaths/build-images-cloud-native-toolkit/existing-application)で案内しています。

   * Cloud-Native Toolkitを既存のアプリケーションで使用する。
   * CIパイプラインで実行するためにGitHubリポジトリを準備する方法を学ぶ
   * アプリケーションに合わせてパイプラインのタスクを変更する方法を学ぶ
   * OpenShift認証用のコンテナイメージの準備

### 3.複数のレポからアプリケーションを使用する

複数のリポジトリにまたがる、より複雑なアプリケーションがある場合は、上級チュートリアルの[Build an OpenShift certifiable image from a complex application](/learningpaths/build-images-cloud-native-toolkit/poly-repo/)を読んで、その方法を学びましょう。

   * クラウドネイティブツールキットを実際のオープンソースアプリケーションで使用する。
   * 複数のGitHubリポジトリで動作するようにパイプラインタスクを変更する
   * パイプラインのアクションを変更するためのパラメータの追加と使用
   * イメージリリースにセマンティックバージョニングを使用
   * OpenShift認証のためのコンテナイメージの準備