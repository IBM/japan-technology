---
authors: ''
check_date: '2022-12-09'
completed_date: '2021-06-09'
components:
- openshift
draft: false
excerpt: この記事では、SCCが実際に保護されたLinuxの機能にパーミッションを付与する方法について説明します。
menu_order: 2
meta_description: この記事では、SCCが実際に保護されたLinuxの機能にパーミッションを付与する方法について説明します。
meta_keywords: security context constraint permissions, permissions for Linux functions
meta_title: SCCがパーミッションを指定する方法
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: security-first-certification-for-cloud-native-workloads
  type: videos
- slug: multitenancy-and-role-based-access-control
  type: tutorials
subtitle: 保護されたLinux機能へのアクセス権限の制御
tags:
- security
- linux
time_to_read: 10 minutes
title: SCCがパーミッションを指定する方法
---

Red Hat OpenShift クラスタでは、セキュリティコンテキスト制約 (SCC) を使用して、保護された Linux 機能にアクセスするポッドの権限を制限しています。この記事では、SCC が保護された機能にアクセスする権限をポッドに付与する方法を詳しく見ていきます。

この記事は、アプリケーションを OpenShift クラスターにデプロイする方法と、クラスターがワークロードを管理する方法について一般的な理解をしていることを前提としています。

## セキュリティコンテキスト制約の概要

[Overview of security context constraints](/learningpaths/secure-context-constraints-openshift/intro/)の記事のキーポイントは以下の通りです。

* デフォルトでは、OpenShift は、Linux の保護された機能へのアクセスを制限することで、コンテナを隔離します。SCC では、一部のポッドが保護された機能の一部またはすべてにアクセスすることができます。
* 開発者が保護された機能へのアクセス許可を必要とするアプリケーションを作成する場合、デプロイ担当者はそのセキュリティコンテキスト（SC）でそれらの許可を要求するデプロイメントマニフェストを作成し、管理者はそれらの許可を与えるSCCを割り当てる必要があります。
  * ポッドは、SC から要求され、SCC から付与されたパーミッションで、コンテナの Linux 環境を構成します。アプリケーションが、SC で要求されていない保護された機能を実行しようとすると、コンテナはアプリケーションがその機能を実行するのをブロックします。アプリケーションはこれをエラーとして認識します。
  * カスタムSCCは、[Principle of Least Privilege](https://redhat-connect.gitbook.io/best-practices-guide/principle-of-least-privilege)を使用して開発し、可能な限り少ないアクセスを許可する必要があります。
* 管理者は、サービスアカウントに SCC を割り当てることで SCC を利用可能にします。
* マニフェストでは、サービスアカウントを指定することで、ポッドがSCCを利用できるようにします。
* SCCがマニフェストで要求されたすべての権限を付与した場合にのみ、クラスタはマニフェストで指定された各ポッドをディプロイすることができます。

以上の点を踏まえて、この仕組みを詳しく見ていきましょう。

## SCCによるパーミッションの指定方法

ここまでは「パーミッション」という総称で、ポッドが（デプロイメントマニフェストを介して）要求できることと、SCCが許可することを説明してきました。OpenShiftでは、パーミッションを「特権」「アクセスコントロール」「能力」の3つの側面から指定します。

各アスペクトには、独自のルールと構文があります。以下のセクションでは、ディプロイメントマニフェスト側（許可を求める側）とSCC側（許可を与える側）の両方で使用できる、利用可能なフィールドと値のいくつかについて詳しく説明します。

### 特権

特権とは、ポッドが配備されたときに持つ一般的な権限を表します。SCCやディプロイメントマニフェストでは、設定値が「true」の場合、その特権が許可されていることを意味します。

SCCでの特権の例を示します。

* `allowPrivilegedContainer` -- ポッドが特権プロセスでコンテナを実行できるかどうかを指定します。
* `allowPrivilegeEscalation` -- 子プロセスが親プロセスよりも多くの特権を得られるかどうかを指定します。

ディプロイメントマニフェストでは、これらの特権をコンテナに対して要求することができます。例えば、以下のようになります。


_**important**:SCCでは[特権コンテナ](https://docs.docker.com/engine/reference/run/#runtime-privilege-and-linux-capabilities)の実行やエスカレーションを許可することができますが、そうするとホストの安全性が大幅に低下します。特権コンテナは、コンテナ内で実行されているプロセスに、"コンテナの外でホスト上で実行されているプロセスとほぼ同じアクセス "を許可します。議論の余地はありますが、コンテナがプロセスを含むことでホストを保護できないのであれば、コンテナを使用することの重要な利点が無効になります。また、「[Should You Run Privileged Docker Containers?](https://phoenixnap.com/kb/docker-privileged#htoc-why-running-privileged-containers-is-not-secure)」_もご覧ください。

### アクセス制御

アクセスコントロールでは、ポッドが実行する特定のユーザーIDやグループIDの値を管理します。

SCCでは、アクセスを指定するためのフィールドのリストは以下の通りです。

* `runAsUser` は、ポッド内のすべてのコンテナを実行する際に使用するユーザーIDの許容範囲を指定します。
* `supplementalGroups` は、ポッド内のすべてのコンテナを実行するために使用するグループIDの許容範囲を指定します。
* `fsGroup` では、ポッドのストレージボリュームを制御するために使用するグループ ID の許容範囲を指定します。
* `seLinuxContext` は、SELinux コンテキストの設定に使用する許容値を指定します。

SCCのアクセスコントロール設定では、以下の値を指定できます。

* `MustRunAs` および `MustRunAsRange` は、コンテナが要求できるユーザ ID 値の範囲を強制するとともに、必要に応じてデフォルト値を割り当てます。
* `RunAsAny` は、ユーザ ID が SCC やプロジェクトで指定された範囲内である必要がないことを示し、あらゆる ID を要求できるようにします。これにより、ルートユーザー(UID=0)を指定することができますが、これは非ルートユーザーIDに比べて著しく安全性が低いことに注意してください。
* `MustRunAsNonRoot` は、任意の非 root ID 値 (0 以外の任意のユーザ ID) を要求できることを示します。これは `RunAsAny` と似ていますが、より安全です。

ディプロイメントマニフェストでは、これらのフィールドを使用してコンテナまたはポッドのアクセスを要求できます。

* `securityContext.runAsUser` -- 特定のユーザー ID で実行することを要求する。
* `securityContext.runAsGroup` -- 特定のグループ ID での実行を要求する。
* `securityContext.fsGroup` -- ストレージボリュームにアクセスするために、特定のグループIDの下で実行することを要求する。
* `securityContext.seLinuxOptions` -- 特定の SELinux コンテキストのラベルセットを使用して実行するように要求する。

****SELinuxとは？

[Security-Enhanced Linux (SELinux)](https://www.redhat.com/en/topics/linux/what-is-selinux)は、追加のアクセス制御セキュリティを提供するLinuxカーネルモジュールで、以下のようなメリットがあります。

* **すべてのプロセスとファイルにラベルを付ける：** SELinuxのポリシールールは、プロセスとファイルの相互作用や、プロセス同士の相互作用を定義します。SELinuxポリシールールは、プロセスとファイル、およびプロセス同士の相互作用を定義します。
* SELinuxのアクセス決定は、SELinuxのユーザ、ロール、タイプ、そしてオプションとしてセキュリティレベルなど、利用可能なすべての情報に基づいて行われます。
* **SELinuxポリシー**は、管理者によって定義され、システム全体に適用されます。
**SELinuxポリシー**は、管理者によって定義され、システム全体に適用されます。* * **特権昇格攻撃に対する改善された緩和策** プロセスはネームスペースで実行されるため、互いに分離されています。SELinuxのポリシールールは、プロセスがファイルや他のプロセスにアクセスする方法を定義します。

### 機能概要

[Linux capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html)へのアクセスを制御します。これは、システム時刻へのアクセスやネットワーク設定など、スーパーユーザの個別権限です。これらの機能はポッド内で動作する個々のコンテナに割り当てられ、ポッドの設定よりも優先されます。

ケイパビリティの例を以下に示します。

* `CHOWN` -- ファイルの所有権やグループの所有権を変更できます。
* `KILL` -- 一致するユーザー ID を持たないプロセスにシグナルを送ることができます。
* `NET_BROADCAST` -- ブロードキャストとマルチキャストのリッスンができます。
* `NET_ADMIN` -- インターフェースの設定、ルーティングテーブルの設定、マルチキャストの設定、IPファイアウォールの管理などを行うことができます。
* `SYS_CHROOT` -- `chroot` コマンドを使用できます。
* `SYS_ADMIN` -- ドメイン名やホスト名の設定、マウント/アンマウントの実行、共有メモリのロック/アンロックなどができます。
* `SYS_TIME` -- システムクロックを操作することができます。
* `MKNOD` -- `mknod()` の特権的な側面を提供します。
* `SETCAP` -- ファイルに機能を設定したり、削除したりできます。

ケイパビリティの完全なリストは [include/linux/capability.h](https://github.com/torvalds/linux/blob/master/include/uapi/linux/capability.h) で指定されています。

SCCはこれらのフィールドを使って機能を付与します。

* `defaultAddCapabilities` -- 各コンテナに自動的に追加されるデフォルトのケイパビリティのリスト。
* `requiredDropCapabilities` -- 各コンテナ上で実行が禁止されているケイパビリティのリスト。
* `allowedCapabilities` -- ディプロイメントマニフェストで要求することが許可されているコンテナの機能のリスト

ディプロイメント マニフェストは、これらのフィールドを使用してコンテナのケイパビリティを要求できます。

* `securityContext.capabilities.add` -- コンテナの機能を要求する。
* `securityContext.capabilities.drop` -- コンテナに要求できるケイパビリティのリスト。

任意の SCC は、特権、アクセス制御、およびケイパビリティという 3 つの側面を使用してパーミッションを指定します。OpenShift にはいくつかの定義済み SCC があります。管理者は、カスタム SCC を実装することでこれらを追加することができます。

## まとめ

セキュリティコンテキスト制約が、ポッドが保護された Linux 機能にアクセスすることを可能にする権限をどのように付与するかを詳しく見たので、[定義済みおよびカスタム SCC](/learningpaths/secure-context-constraints-openshift/openshift-predefined-scc/)を探求するこのラーニングパスの次の記事に進む準備ができました。