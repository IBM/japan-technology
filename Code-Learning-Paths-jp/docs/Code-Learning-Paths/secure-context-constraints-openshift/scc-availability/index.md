---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
draft: false
excerpt: このドキュメントでは、管理者がセキュリティ コンテキスト制約を配置で使用できるようにする方法について説明します。
menu_order: 4
meta_description: このドキュメントでは、管理者がセキュリティ コンテキスト制約を配置で使用できるようにする方法について説明します。
meta_keywords: custom security context constraint, predefined SCCs
meta_title: セキュリティ コンテキスト制約を配備で利用可能にする
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
subtitle: セキュリティ コンテキスト制約を配置で使用できるようにする手順
tags:
- security
- linux
time_to_read: 10 minutes
title: SCCを利用可能にする
---

これまで、このラーニング パスでは、主要なセキュリティ コンテキスト制約 (SCC) とその権限、および定義済み SCC とカスタム SCC の違いについて説明してきました。この記事では、管理者がSCCを配備で使用できるようにする方法について説明します。重要なリソースは *サービスアカウント* で、これには SCC を (直接またはロールやグループを介して間接的に) 割り当てることができます。SCC が割り当てられると、配置はそのサービス アカウントを簡単に指定して SCC にアクセスできるようになります。

## ロールベースアクセスコントロール(RBAC)

サービスアカウントは、Red Hat OpenShift クラスタのロールベースのアクセス制御 (RBAC) を使用して構成されるリソースタイプの 1 つです。このセクションでは、ユーザーアカウントやサービスアカウント、ロールやバインディングなどのRBACリソースとその仕組み、および管理者がそれらを使用してパーミッションやアクセスを管理する方法について、すでに理解していることを前提としています。参考までに、OpenShift のドキュメントのこれらのページを参照してください。

* [Using RBAC to define and apply permissions](https://docs.openshift.com/container-platform/4.6/authentication/using-rbac.html)
* [Understanding and creating service accounts](https://docs.openshift.com/container-platform/4.6/authentication/understanding-and-creating-service-accounts.html)

RBACオブジェクトのスコープについて、いくつかの留意点があります。

* ユーザーアカウントは、クラスタ全体に適用されます。
* 例えば、各プロジェクトにはそれぞれデフォルトのサービスアカウントがあります。
* ロールには、プロジェクトに限定されたローカルロール（`Role`）と、クラスタに限定されたクラスタロール（`ClusterRole`）があります。
* SCCはクラスタに対してグローバルな役割を果たします。

SCCはクラスタ全体に適用されます。クラスタ全体のRBACオブジェクトを作成するには、ユーザがクラスタ管理者である必要があります。各プロジェクトの管理者（クラスタ管理者を含む）は、プロジェクトレベルのRBACオブジェクトを作成します。

## サービスアカウント

サービスアカウント_は、クラスタで動作するコンポーネントがクラスタのAPIに直接アクセスできるようにするものです。これはユーザーアカウントに似ていますが、単一のプロジェクトにスコープされ、通常のユーザーの認証情報を共有する必要はありません。配置はサービスアカウントを介してSCCにアクセスするため、どのユーザが配置したかに関わらずSCCへのアクセスが可能になります。

各サービスアカウントのユーザ名は、そのプロジェクトと名前に由来します。