---
authors: ''
check_date: '2022-12-30'
completed_date: '2021-06-30'
components:
- openshift
draft: false
excerpt: 既存のNode.jsアプリケーションにCloud-Native Toolkitを使用して、OpenShiftの認証可能なイメージを構築するには、以下の手順に従ってください。
menu_order: 3
meta_description: 既存のNode.jsアプリケーションにCloud-Native Toolkitを使用して、OpenShiftの認証可能なイメージを構築するには、以下の手順に従ってください。
meta_keywords: fast install, cloud native toolkit installation, install cloud native
  toolkit
meta_title: 既存のアプリケーションにCloud-Native Toolkitを使用して、OpenShiftの認証可能なイメージを構築する。
primary_tag: containers
subtitle: 既存のNode.jsアプリケーションをCloud-Native Toolkitに導入します。
tags:
- containers
time_to_read: 30 minutes
title: Cloud-Native Toolkitを既存のアプリケーションに使用する
---

このチュートリアルでは、[Cloud-Native Toolkit](https://cloudnativetoolkit.dev/)をアプリケーションに組み込んで、Red Hat OpenShiftクラスター上でアプリケーションを構築、テスト、デプロイする方法を紹介します。ツールキットを使用して、アプリケーションをユニバーサル・アプリケーション・イメージ（UAI）にするタスクのパイプラインを作成する方法を実際に体験してください。これは、[Red Hat Container Certification](https://connect.redhat.com/en/partner-with-us/red-hat-container-certification)の要件を満たすための大きな第一歩となります。

このチュートリアルは、記事[Use the Cloud-Native Toolkit starter kits](/learningpaths/build-images-cloud-native-toolkit/starter-kits/)で説明されている概念に基づいています。

このチュートリアルの手順に従って、ツールキットを使用して必要なファイルを既存のGitHubリポジトリに追加し、アプリケーションのデプロイを管理するためのOpenShift CI/CDパイプラインを構築できるようにします。

GitHub リポジトリに加えた変更は、パイプラインのトリガーとなります。

* コードベースのコンパイルとビルド
*コードベースのコンパイルとビルド * レポで定義されたユニットテストや統合テスト、SonarQube を使用したコード品質とセキュリティを含むテストの実行
* UAI の構築とスキャン
* UAI を OpenShift クラスタにデプロイする
* UAI と GitHub リポジトリにリリースバージョンのタグを付ける
* UAIをコンテナレジストリに格納

このチュートリアルでは、パイプラインが失敗する可能性のある例と、それらの問題を解決するための手順についても説明します。

## 前提条件

このチュートリアルを完了するには、以下へのアクセスが必要です。

* [GitHub](https://github.com/)のパブリック・アカウントをお持ちの方。
* [IBM Cloud](https://cloud.ibm.com/?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg) のアカウント
* Red Hat OpenShift クラスタ

また、以下のセットアップ作業を行う必要があります。

* チュートリアル[Install the Cloud-Native Toolkit](/learningpaths/build-images-cloud-native-toolkit/install-toolkit/)で説明されているように、OpenShiftクラスターにCloud-Native Toolkitをインストールします。OpenShiftクラスターの管理者のみがツールキットをインストールすることで、お客様がアクセスできるようになります。
* [ドキュメント](https://cloudnativetoolkit.dev/getting-started/prereqs/)に記載されている手順に従って、Cloud-Native Toolkit 用のアカウントを準備します。これには、GitHub と IBM のアクセストークンの生成が含まれます。
* Cloud-Native Toolkit [developer tools](https://cloudnativetoolkit.dev/getting-started/dev-env-setup/)を自分のマシンにインストールします。
* Cloud-Native Toolkit [Command Line Interface (CLI)](https://cloudnativetoolkit.dev/getting-started/cli)をインストールします。

>**NOTE**:IBM Cloud アカウントが必要なのは、このサンプルアプリが Watson Assistant サービスを使用するためだけです。Cloud-Native Toolkit の要件ではなく、Red Hat OpenShift など、サポートされている Kubernetes ベースのクラスターと一緒に使用することができます。

## 見積もり時間

このチュートリアルを完了するには、約 60 分かかります。

## デプロイされるアプリケーション

このチュートリアルで使用するアプリケーションは、オープンソースの Node.js アプリケーションです -- IBM Cloud 上に作成された IBM Watson Assistant サービス上に構築された、ピザを注文するチャットボットです。

このアプリケーションは、以下のような特性を持っているため、良い例となります。

* オープンソースのGitHubリポジトリで管理されているソース
* アプリのインストール、テスト、および実行方法を指定する従来のビルドファイル
* 定義されたユニットテストとインテグレーションテスト
* Dockerイメージを構築するためのDockerfile

リポジトリは[https://github.com/IBM/watson-assistant-slots-intro](https://github.com/IBM/watson-assistant-slots-intro)で、アプリのビルドと実行の手順を示すREADMEが含まれています。

このアプリが完全に機能するには、IBM Watson Assistant サービスの使用が必要です。そのためには、Watson サービスの設定と構成が必要です。

また、アプリをローカルで実行してテストしたい場合は、Node.jsランタイムや`npm`をインストールする必要があります。

このチュートリアルのパイプラインの部分だけに集中して、Watson サービスには一切触れたくないという方のために、このチュートリアルでは Watson サービスの内容をバイパスしても、最終的にデプロイを成功させるための手順を紹介します。

## 手順

1. [レポをフォークしてクローンする](#1-fork-and-clone-the-repo)
1. [Cloud-Native Toolkitを使うためにプロジェクトを準備する](#2-prepare-your-project-touse-the-cloud-native-toolkit)
1. [GitHubレポの準備】(#3-prepare-the-github-repo)
1. [ツールキットを使ってパイプラインを作成する](#4-use-the-toolkit-to-create-a-pipeline)
1. [パイプラインを OpenShift の Web コンソールで見る](#5-watch-the-pipeline-in-the-openshift-web-console)
1. **[デプロイ**タスクの問題を解決する](#6-resolve theissue-with-the-deploy-task)
1. [パイプラインを再実行する](#7-re-run-the-pipeline)
1. **[健康**タスクの問題を解決する](#8-resolve-the-issue-with-the-health-task)1.
1. [結果を調べる](#9-結果を調べる)

### 1.レポをフォークしてクローンを作成する

まず、自分のGitHubアカウントにレポをフォークします。次に、フォークしたレポをローカルマシンにクローンします。

// ヘルスエンドポイントの追加
app.get('/health', (req, res) => { ...
  console.log('Health Check called');
  res.send('UP');
});