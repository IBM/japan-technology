---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
content_tags:
- hcbt
draft: false
excerpt: Red Hat OpenShift のワークロードでセキュリティコンテキスト制約を使用する方法を学びます。
meta_description: Red Hat OpenShift のワークロードでセキュリティコンテキスト制約を使用する方法を学びます。
meta_keywords: security context constraints, security in OpenShift
meta_title: ラーニングパスRed Hat OpenShift でのセキュリティコンテキスト制約の利用開始
primary_tag: containers
related_content:
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
- slug: l-lpic1-104-5/
  type: tutorials
subtitle: Red Hat OpenShift のワークロードでセキュリティコンテキスト制約を使用する方法を紹介します。
tags:
- security
- linux
- hcbt
time_to_read: 2 hours
title: Red Hat OpenShift でのセキュリティコンテキスト制約の使用を開始します。
---

このラーニングパスは、Red Hat OpenShift でのセキュリティコンテキスト制約の使用方法を理解することに興味のある方を対象としています。セキュリティコンテキスト制約 (SCC) は、コンテナ化されたアプリケーションが保護された Linux 機能にアクセスすることを可能にします。

このラーニングパスは、OpenShift デプロイメントで SCC を作成して使用する方法を示す、入門記事と詳細記事、およびハンズオンデモによるステップバイステップのチュートリアルで構成されています。

## アウトカム

このラーニングパスを完了すると、以下のようになります。

* SCCの概念を以下のようにしっかりと理解する。
    * SCCとは何か？
    * セキュアポッドの展開
    * ポッドが追加のアクセスを要求する方法
    * SCC がパーミッションを指定する方法
    * OpenShift の定義済み SCC
    * カスタム SCC の作成
    * デプロイメントがパーミッションを指定する方法
* SCC を使用して、以下のような実践的な経験を得ることができます。
    * ワークロードに割り当てられている SCC とセキュリティコンテキストを認識する。
    * デフォルトのサービスアカウントとデフォルトのセキュリティコンテキストの使用
    * SCC の検証エラーの確認
    * SCCの作成とサービスアカウントへの割り当て
    * 特別な権限を要求するセキュリティコンテキストと、それを許可するSCCの使用