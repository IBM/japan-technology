---
authors: ''
check_date: 2022-08-04
completed_date: '2021-08-04'
display_in_listing: true
draft: false
excerpt: Kubernetesのポッドセキュリティポリシー(PSP)をRed Hat OpenShiftのセキュアコンテキスト制約に変換するために変更する必要がある内容をご紹介します。
meta_description: Kubernetesのポッドセキュリティポリシー(PSP)をRed Hat OpenShiftのセキュアコンテキスト制約に変換するために変更する必要がある内容をご紹介します。
meta_keywords: kubernetes pod security policies, Kubernetes PSPs, OpenShift SCCs,
  OpenShift secure context constraints
meta_title: KubernetesポッドのセキュリティポリシーをOpenShiftのセキュリティコンテキスト制約に移行します。
primary_tag: containers
related_content:
- slug: secure-context-constraints-openshift
  type: learningpaths
- slug: universal-application-image
  type: learningpaths
subtitle: ワークロードをKubernetesからRed Hat OpenShiftに移行する際に行うべきセキュリティアップデート
tags:
- security
title: KubernetesポッドのセキュリティポリシーをOpenShiftのセキュリティコンテキスト制約に移行します。
---

Red Hat OpenShiftは、Kubernetesベースのコンテナプラットフォームです。一般的に、Kubernetes クラスタで正しくデプロイされて実行されるコンテナ化されたアプリケーションは、OpenShift クラスタでも正しくデプロイされて実行されます。ただし、KubernetesとOpenShiftの違いの1つは、クラスターがポッドにコンテナのセキュリティコンテキストの変更を許可する方法です。

* Kubernetesには、セキュリティコンテキストを変更する権限を付与するためのPod Security Policies (PSP)という機能があります。
* OpenShiftには、Security Context Constraints (SCC)と呼ばれる似て非なる機能があります。

アプリケーションはどちらのタイプのクラスターでも同じようにデプロイされるので、デプロイメントマニフェストを変更する必要はありません。しかし、OpenShift クラスタの構成は異なり、PSP の代わりに SCC が使用されており、RBAC アーティファクトは、アクセスを許可するためにこれらの新しい SCC アーティファクトに接続する必要があります。

この記事では、クラスタ管理者がクラスタのセキュリティポリシーをKubernetesからOpenShiftに移行する方法を紹介します。クラスタ管理者は、PSPとSCCの構成と展開を担当します。具体的には、PSPをSCCに変換する方法と、PSPの代わりにSCCを使用するようにRBACアーティファクトを更新する方法を説明しています。

## 始める前に

ラーニングパス [Get started with security context constraints on Red Hat OpenShift](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift) では、OpenShift で SCC を構築して使用する方法を正確に説明しています。SCC に慣れていない方は、まずラーニングパスをお読みください。

## Podセキュリティポリシー、セキュリティコンテキスト制約、RBACの定義

KubernetesのPod Security PoliciesをOpenShiftのSecurity Context Constraintsに移行する_方法を説明する前に、それぞれのセキュリティメカニズムが何をするのかを見てみましょう。

### Kubernetesのポッドセキュリティポリシー(PSP)

Kubernetesクラスタ内のコンテナは、そのアプリケーションがホストネットワークやボリュームなどの資産にアクセスすることを制限します。これは、アプリケーションがLinux環境や他のコンテナに影響を与えるような変更を行うことを防ぐためです。アプリケーションが保護されたLinux機能へのアクセスを必要とする場合、ポッドはこのアクセスを設定することができます。ポッドが実行されるためには（つまり、クラスターがポッドを認めるためには）、ポッドが構成したアクセスをクラスターが許可する必要があります。

Kubernetesクラスタでは、PSPを使用して、ポッドがコンテナ上で有効にできるパーミッションを指定します。[Kubernetes docs](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)によると。"`PodSecurityPolicy` オブジェクトは、ポッドがシステムに受け入れられるために実行しなければならない一連の条件と、関連フィールドのデフォルトを定義します。"PSPはオプションのアドミッションコントローラとして、Kubernetesクラスタ上で実行できるものを制限する役割を果たします。

### OpenShiftにおけるSCC(Security Context Constraints)について

OpenShiftはKubernetesよりも厳しいセキュリティポリシーを採用しています。OpenShiftでは、コンテナ化されたアプリケーションが保護されたLinux機能にアクセスできるようにするために、SCC（Security Context Constraints）を使用します。SCCはクラスタ内で定義され、管理者がポッドのパーミッションを制御できるようにします。

[Role Based Access Controls](https://docs.openshift.com/container-platform/4.6/authentication/managing-security-context-constraints.html#role-based-access-to-ssc_configuring-internal-oauth)と同様です。(RBAC)がユーザーのクラスタのリソースへのアクセスを管理するのと同様に、SCCはポッドのLinux機能へのアクセスを管理します。

学習パス[Get started with security context constraints on Red Hat OpenShift](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift/)では、SCCとは何か、どのように使用するのかを徹底的に紹介しています。

### 役割ベースのアクセス制御(RBAC)

SCC は、直接または理想的には RBAC ロールを介して、セキュリティアカウントと関連付けられます。RBAC は、ポリシーやセキュリティ制約の使用を許可するために使用します。RBACインフラストラクチャは、Role、ClusterRole、RoleBinding、およびClusterRoleBindingによって実装されます。まず、RoleまたはClusterRoleは、目的のポリシーを使用するためのアクセスを許可する必要があります。次に、(Cluster)Roleを認可されたユーザーにバインドします。

KubernetesとOpenShiftのRBACについて、PSPとSCCをどのように組み込んでいるのかを詳しく知りたい方は、こちらをご覧ください。

  - [KubernetesにおけるRBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
  - [Using RBAC for PSP](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#via-rbac)
  - [OpenShiftでのRBAC](https://docs.openshift.com/container-platform/4.6/authentication/using-rbac.html)
  - [SCCでのRBACの使用](https://docs.openshift.com/container-platform/4.6/authentication/managing-security-context-constraints.html#role-based-access-to-ssc_configuring-internal-oauth)

これらの背景情報を参考に、KubernetesからOpenShiftにポリシーを移行するために必要なことをご覧ください。

## KubernetesからOpenShiftへのセキュリティポリシーの移行

KubernetesからOpenShiftにセキュリティポリシーを移行するには、Pod Security PolicyのすべてのコントロールアスペクトがSecurity Context Constraintsに移行されていることを確認する必要があります。クラスタ管理者は、PSPとSCCの両方を定義します。

まず、Kubernetesクラスタで利用可能なPSPを特定する必要があります。PSPの一覧を取得するには、このコマンドを使用します。


Kubernetesクラスタには、デフォルトではビルトインのPSPは含まれていません。この例では、`my-custom-psp`というPSPを追加しています。すると、コマンドはそれをリストに表示します（リストの中で唯一のアイテムです）。


`my-custom-psp`の設定を見るには、次のコマンドを実行します。


このコマンドは、PSPを表示します。


このポリシーでは、コントロールの一部を

- `privileged` が "false" に設定されています。このポリシーでは、特権的なアクセス権を持つポッドのデプロイを許可しません。
- `fsGroup`と`supplementalGroups`には、グループIDの特定の範囲に対する制限が与えられています。
- このポリシーでは、特定のボリュームへのアクセスを許可します。`persistentVolumeClaim`、`secret`、`emptyDir`の3つです。

### PSP を SCC に変換する

コントロールを OpenShift の SCC に移行する必要があります。以下の表は、KubernetesとOpenShiftの間のセキュリティコントロールフィールドのマッピングです。基本的には、OpenShiftのSCCファイルを構築する際に、左のPSPコントロールフィールド名を、該当する右のSCCコントロールフィールド名に置き換えて、PSPファイルを更新します。

| コントロール・アスペクト｜PSP フィールド名｜SCC フィールド名｜?
| --- | --- | --- |
| 特権コンテナの実行 | privileged | allowPrivilegedContainer
| ホストの名前空間の使用｜hostPID，hostIPC｜allowHostPID，allowHostIPC
| ホストのネットワークおよびポートの使用法 | hostNetwork, hostPorts | allowHostNetwork, allowHostPorts |
| ボリュームタイプの使用状況｜volume｜volume｜。
| ホストファイルシステムの使用法｜allowedHostPaths｜（注）｜｜。
| 特定のFlexVolumeドライバーを許可する｜allowedFlexVolumes｜allowedFlexVolumes｜（注記参照
| ポッドのボリュームを所有するFSグループを割り当てる｜fsGroup｜fsGroup
| 読み取り専用のルートファイルシステムの使用を要求する｜readOnlyRootFilesystem｜readOnlyRootFilesystem｜readOnlyRootFilesystem
| readOnlyRootFilesystem｜readOnlyRootFilesystem｜コンテナのユーザ及びグループID｜runAsUser， runAsGroup，supplementalGroups｜runAsUser，fsGroup，supplementalGroups｜。
| root 権限へのエスカレーションの制限 | allowPrivilegeEscalation, defaultAllowPrivilegeEscalation | allowPrivilegeEscalation, defaultAllowPrivilegeEscalation |
| Linux capabilities｜defaultAddCapabilities, requiredDropCapabilities, allowedCapabilities｜defaultAddCapabilities, requiredDropCapabilities, allowedCapabilities｜...
| コンテナの SELinux コンテキスト｜seLinux｜seLinuxContext｜。
| コンテナのSELinuxコンテキスト｜seLinux｜seLinuxContext｜コンテナのAllowed Proc Mount Type｜allowedProcMountTypes｜（注記参照
| コンテナが使用するAppArmorプロファイル｜annotations｜アノテーション
| コンテナで使用される seccomp プロファイル｜アノテーション｜アノテーション｜｜（注
| コンテナが使用する sysctl プロファイル｜forbiddenSysctls, allowedUnsafeSysctls｜forbiddenSysctls, allowedUnsafeSysctls｜（注釈参照


> NOTE: `allowedHostPaths`:SCCには`allowedHostPaths`に相当するものはありません。SCC では、[Red Hat Customer Portal](https://access.redhat.com/solutions/5314051)で説明されているように、別の方法で処理されます。

> 注意: `allowedProcMountTypes`:SCC には、`allowedProcMountTypes` に相当するものはありません。

コントロールアスペクトとそのフィールド名の詳細については、Kubernetesのドキュメントの[What is a Pod Security Policy?](https://kubernetes.io/docs/concepts/policy/pod-security-policy/#what-is-a-pod-security-policy)と、OpenShiftのドキュメントの[SecurityContextConstraints](https://docs.openshift.com/container-platform/4.7/rest_api/security_apis/securitycontextconstraints-security-openshift-io-v1.html#specification)を参照してください。

名前やコントロールの表現方法には多少の違いがあるかもしれません。上の表が示すように、PSPの`privileged`はSCCでは`allowPrivilegedContainer`、PSPの`hostNetwork`はSCCでは`allowHostNetwork`といった具合にです。

### コントロールアスペクト値の指定

コントロールアスペクトの詳細にもバリエーションがあります。例えば、`RunAsUser` コントロールの表現方法が異なります。

PSPでは


SCCでは


SCCではすべてのコントロールがどのように表現されているのか、PSPとはどう違うのかを理解するために、[SCC Learning Path](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift)を徹底的に読み込んでください。

### 変換されたPSPはどのようなものか

先ほどのPSPのマニフェストの例をSCCのマニフェストファイルに適応すると、以下のようになります。


このSCCをファイルに保存し、コマンドを使ってクラスタにデプロイすることができます。


これで、既存のPSPからSCC設定ファイルを作成するために必要なことがわかりました。次のステップは、RBACアーティファクトであるRole(またはClusterRole)とRoleBinding(またはClusterRoleBinding)を移行することです。

### RBACの移行

ロールとロールバインディングは、どのユーザーがどのポリシーにアクセスできるかをマッピングするのに役立ちます。

1. セキュリティポリシーを OpenShift に移行する前に、特定のポッドのセキュリティポリシーを使用するロールを特定する必要があります。ロールのリストを取得するには、`kubectl get roles -n <namespace>` を使用し、特定のロールの YAML 出力を取得するには、`kubectl get role <role_name> -o yaml -n <namespace>` を使用します。

    ロールのYAML出力の例を以下に示します。


    このロールは、リソース `podsecuritypolicies` をアクション `use` にマッピングしていることに注意してください。

`    podsecuritypolicies`を使用するすべてのロールについて、対応するロールをOpenShiftで作成する必要があります。

1. 次のステップは、ロールをユーザーやサービスアカウントにマッピングするRoleBindingsを特定することです。セキュリティポリシーをKubernetesからOpenShiftに移行する際には、ロールを移行するのと同じ方法でRoleBindingsを移行します。

1. セキュリティポリシーを使用するClusterRolesがある場合は、ClusterRolesとClusterRoleBindingsも移行する必要があります。

    > 注：SCCおよび(Cluster)RoleBindingで指定されたユーザー、グループ、およびサービスアカウントが存在することを確認する必要があります。ユーザーやグループが存在しない場合は、以下のいずれかを行う必要があります。
    > 適切なユーザー、グループ、またはサービス・アカウントを含むようにロールを編集します。
    > - SCCおよびClusterRoleBindingで使用できるように、OpenShiftで必要なユーザー、グループ、またはサービスアカウントを作成する。

これらのマニフェストファイル（SCC、(Cluster)Role、(Cluster)RoleBinding）をすべて作成したら、これらをクラスタに適用することで、SCCが実装され、アプリケーションのデプロイメントが安全に行われるようになります。

## Kubernetesの定義済みPSPとOpenShiftの定義済みSCCのマッピング

一般的に、クラスタ内のアプリケーションポッドに権限を付与するために、管理者はベンダーが提供する定義済み（つまりデフォルト）のPSPを使用するのではなく、カスタムPSPを定義する必要があります。アプリケーションを移行するために、管理者は上述のように、カスタムPSPの定義を対応するカスタムSCCの定義に変換する必要があります。しかし、アプリケーションがベンダーの定義済みPSPを使用している場合、管理者はそれらを対応する定義済みSCCにどのように変換すればよいのでしょうか？

まず、Kubernetesクラスターにはデフォルトで内蔵のPSPが含まれていないため、SCCに変換するための定義済みPSPはありません。OpenShiftでは9つの[default SCCs](https://docs.openshift.com/container-platform/4.7/authentication/managing-security-context-constraints.html#security-context-constraints-about_configuring-internal-oauth)が定義されていますが、それは以下の通りです。

- ANYUID
- ホストアクセス
- ホストマウント-ANYUID
- ホストネットワーク
- ノード・エクスポーター
- ノンルート
- 特権
- 制限付き
- パイプライン-SCC

詳細は[OpenShift's predefined SCCs](https://developer.ibm.com/learningpaths/secure-context-constraints-openshift/openshift-predefined-scc/#openshift-s-predefined-sccs)を参照してください。

OpenShift の事前定義された SCC は、主に Red Hat がクラスターに構築するツールが使用するためのものです。ユーザーアプリケーションも定義済みSCCを使用することができますが、[最小特権の原則](https://en.wikipedia.org/wiki/Principle_of_least_privilege)により、アプリケーションが必要とする特権に完全に一致するものがない限り、アプリケーションが必要とする特権のみを持つカスタムSCCを定義することがより安全なアプローチとなります。

### IBM Cloud Kubernetes Serviceにおける定義済みのPSPとSCC

[IBM Cloud Kubernetes Service](https://cloud.ibm.com/docs/containers) (IKS)クラスターから[Red Hat OpenShift on IBM Cloud](https://cloud.ibm.com/docs/openshift)クラスターにアプリケーションを移行する場合、IBMはいくつかの独自の定義済みPSPとSCCを組み込んでいます。IBMがホストするKubernetesクラスターには、これらの[追加のPSP](https://cloud.ibm.com/docs/containers?topic=containers-psp#ibm_psp)が含まれます。

- ibm-anyuid-hostaccess-psp
- ibm-anyuid-hostpath-psp（アイビーエム-アニュイッド-ホストパス-psp
- ibm-anyuid-psp
- ibm-privileged-psp
- ibm-restricted-psp

IBM ホスト型 OpenShift クラスタには、これらの [追加 SCC](https://cloud.ibm.com/docs/openshift?topic=openshift-openshift_scc#ibm_sccs) が含まれます。

- ibm-anyuid-hostaccess-scc
- ibm-anyuid-hostpath-scc（アイビーエム-アニュイッド-ホストパス-scc
- IBM-ANYUID-SCC
- ibm-privileged-SCC
- ibm-restricted-scc

ご覧のとおり、IBMがあらかじめ定義したPSPとSCCは1対1で対応しています。唯一の違いは、名前の最後に「psp」または「scc」というサフィックスが付いていることです。IBM の定義済み PSP を使用しているアプリケーションを OpenShift に移行する場合は、RBAC リソースを変更して、「psp」名のリソースではなく「scc」名のリソースを指定します。

### Amazon Elastic Kubernetes Serviceの定義済みPSPについて

Amazon Elastic Kubernetes Service(EKS)では、Kubernetesクラスタに[1つの定義済みPSP](https://docs.aws.amazon.com/eks/latest/userguide/pod-security-policy.html)を追加し、`eks.privileged`としています。このポリシーには制限がないため、コンテナ内で有効にできる特権に制限はありません。Red Hat OpenShift Service on AWS (ROSA) は、OpenShift クラスタに定義済みの SCC を追加しません。`eks.privileged` PSP を必要とするアプリケーションを移行するには、その RBAC を更新して Red Hat によって事前に定義された `privileged` SCC を使用します。

### Azure Kubernetes Serviceの事前定義されたPSP

同様に、Azure Kubernetes Service(AKS)では、`privileged`という名前の単一の[default AKS policy](https://docs.microsoft.com/en-us/azure/aks/use-pod-security-policies#default-aks-policies)を追加し、AKSはクラスタ内の認証済みユーザに適用します。このポリシーには制限がないため、クラスター内のどのユーザーも、有効にできる特権に制限がなく、コンテナをデプロイすることができます。Azure Red Hat OpenShiftでは、Red Hatがすでに搭載しているSCCに、事前に定義されたSCCを追加していませんが、Red Hatが事前に定義しているSCCの1つに、`privileged`というものがあります。したがって、アプリケーションがAzureの`privileged` PSPを使用する場合は、そのRBACを更新して、Red Hatが事前に定義した`privileged` SCCを使用するようにしてください。

## まとめ

ステートフルなワークロードでは、パーシステントボリューム、ネットワーク機能、ユーザーやグループを使用することがよくあります。これらのリソースはKubernetesでもOpenShiftでもPSPやSCCを使って保護されています。上記のプロセスに従うことで、これらのリソースのセキュリティコントロールアスペクトをKubernetesからOpenShiftに移行することができるはずです。