---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
draft: false
excerpt: 配置がどのようにパーミッションを指定するのか、また、セキュリティコンテキスト制約の許可プロセスについて説明します。
menu_order: 5
meta_description: 配置がどのようにパーミッションを指定するのか、また、セキュリティコンテキスト制約の許可プロセスについて説明します。
meta_keywords: security context constraint deployments, predefined SCCs
meta_title: デプロイメントによるパーミッションの指定方法
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
subtitle: SCCが実際にどのように使われているか
tags:
- security
- linux
time_to_read: 10 minutes
title: デプロイメントによるパーミッションの指定方法
---

このラーニングパスでは、多数のセキュリティコンテキスト制約（SCC）の概念（定義済みおよびカスタム）、パーミッションの指定方法、サービスアカウントへの割り当て方法などを説明してきました。では、SCCが実際に使用されるのはどのような場合でしょうか。この記事では、配備がどのようにパーミッションを指定するのか、またSCCの承認プロセスを説明することで、この疑問に答えます。

SCCは、正しく実行するために追加の権限を必要とするアプリケーションを含む配置で使用されます。ディプロイメント担当者は、ディプロイメント マニフェストの 2 つのフィールドを構成することで、これらの権限を指定します。デプロイヤーは、デプロイメントマニフェストを使用して、ポッドをデプロイおよび管理するオブジェクトであるデプロイメントを作成します。以下は、YAML ディプロイメントマニフェストの例です。