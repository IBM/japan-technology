---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
draft: false
excerpt: この記事では、Red Hat OpenShift の定義済みのセキュリティコンテキスト制約に含まれるものを説明し、さらに SCC をカスタマイズする方法を紹介します。
menu_order: 3
meta_description: この記事では、Red Hat OpenShift の定義済みのセキュリティコンテキスト制約に含まれるものを説明し、さらに SCC
  をカスタマイズする方法を紹介します。
meta_keywords: custom security context constraint, predefined SCCs
meta_title: 定義済みのセキュリティコンテキスト制約とカスタムSCCの比較
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
subtitle: 定義済みSCCに含まれるものとそのカスタマイズ方法
tags:
- security
- linux
time_to_read: 10 minutes
title: 定義済みSCCとカスタムSCC
---

この記事では、Red Hat OpenShift の定義済みのセキュリティコンテキスト制約 (SCC) に含まれる内容を説明し、SCC をカスタマイズする方法も紹介します。

SCC は事前定義またはカスタムのいずれかです。定義済みの SCC は、クラスターが作成されたときにクラスターに組み込まれます。管理者がカスタムSCCを作成すると、そのクラスタに固有のSCCになります。管理者は定義済みのSCCを変更せず、カスタムSCCを作成または変更する必要があります。どのSCCもそのクラスタに対してグローバルなものであるため、サービスアカウントがどのプロジェクトに属しているかに関わらず、どのSCCもどのサービスアカウントにも割り当てることができます。

## OpenShiftの定義済みSCC

各 OpenShift クラスタには 8 つの定義済み SCC があり、それぞれが一連の権限を指定しています。この表は、「[Managing SCCs in OpenShift](https://www.openshift.com/blog/managing-sccs-in-openshift)」に掲載されているもので、定義済みSCCの一覧と説明が記載されています。(なお、「UID」はユーザーID、「GID」はグループIDです)。

| **SCC名** | **説明** | **コメント** |
|--------------|-----------------|--------------|
| **restricted**｜すべてのホスト機能へのアクセスを拒否し、クラスターがプロジェクトに割り当てたセットからUIDとSELinuxコンテキストでポッドを実行することを要求します。| これは最も安全なSCCで、常にデフォルトで使用されます。ほとんどの典型的なステートレスワークロードに対応します。|
| **nonroot** SCCと同じ機能を提供しますが、ユーザーは非rootのUIDで実行することができます。| 予測可能な非 root UID を必要とするアプリケーションに適していますが、 **restricted** SCC で設定された他のすべての制限で機能します。|
| **anyuid** | **restricted**と同じですが、ユーザーが任意のUIDおよびGIDで実行できます。| **anyuid** **restricted**と同じですが、ユーザーが任意のUIDとGIDで実行できるようになります。SELinuxコントロールを使用すれば、保護レイヤを追加する上で重要な役割を果たすことができます。また、望ましくないシステムコールをフィルタリングするために**seccomp**を使用するのも良いアイデアです。|
| **hostmount-anyuid** | **restricted** SCCのすべての機能を提供しますが、ホストマウントとポッドによる任意のUIDを許可します。  これは主に、クラスタに不可欠なインフラストラクチャ部分である信頼されたワークロードであるpersistent volume recyclerによって使用されます。| このSCCは、永続的ボリュームリサイクラーのみが使用する必要があります。警告：**anyuid**と同じ警告ですが、hostmount-anyuidはさらにホストボリュームのマウントを許可します。*Warning:* このSCCは、UID 0を含む任意のUIDとしてホストファイルシステムのアクセスを許可します。注意して許可してください。|
| **hostnetwork**｜ホストネットワークとホストポートの使用を許可しますが、プロジェクトに割り当てられたUIDとSELinuxコンテキストでポッドを実行することが必要です。| **hostnetwork**｜このSCCでは、ポッドがホストネットワークスタックを直接「見て、使う」ことができます。ポッドがゼロでないUIDと事前に割り当てられたSELinuxコンテキストで実行されることを要求することで、いくつかのセキュリティを追加することができます。|
| **node-exporter** | [Prometheus Node Exporter](https://prometheus.io/docs/guides/node-exporter/)にのみ使用されます。(Prometheusは人気のあるKubernetesモニタリングツールです。) | このSCCはPrometheusでのみ使用してください。Prometheusがクラスタからメトリクスを取得するために特別に設計されています。ホストネットワーク、ホストPIDS、ホストボリュームへのアクセスは可能ですが、ホストIPCへのアクセスはできません。また、**anyuid**を許可します。アプリケーションはこのSCCを使用すべきではありません。|
| しかし、プロジェクトに割り当てられたUIDとSELinuxコンテキストでポッドを実行する必要があります。| すべてのホストの名前空間へのアクセスは、UIDとSELinuxを制限するとはいえ、危険です。これは、必要な信頼できるワークロードにのみ使用する必要があります。|
| **privileged** | すべての特権およびホスト機能へのアクセスを許可し、任意のユーザ、グループ、fsGroup として、また任意の SELinux コンテキストで実行することができます。これは、最も緩和されたSCCポリシーです。| このSCCでは、ポッドがホストノードとワーカーノード、および他のコンテナのすべてを制御できます。信頼できるワークロードのみがこれを使用する必要があります。ポッドがホストを完全に制御できるようになるため、本番環境では絶対に使用すべきではないというケースもあります。|
<br>

_**IMPORTANT:** 定義済みの SCC を変更しないでください。定義済みのSCCをカスタマイズすると、OpenShiftがアップグレードされたときに問題が発生する可能性があります。代わりに、新しいカスタムSCCを作成してください。

定義済みSCCの概要を理解したところで、定義済みSCCを詳しく調べてみましょう。

### 制限付きSCCの検討

`Restricted` SCCは、各プロジェクトの`default`サービスアカウントに割り当てられるため、デフォルトのSCCとなります。そのため、サービスアカウントを指定しないすべてのデプロイメントでは、`restricted` SCCが使用されており、最も一般的なSCCとなっています。詳しく見ていきましょう。

SCCは、以下のOpenShift CLIコマンドのいずれかを実行することで見ることができます。