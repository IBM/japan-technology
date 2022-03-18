---
authors: ''
check_date: '2022-08-30'
completed_date: '2021-08-10'
components:
- openshift
- kubernetes
- devops
display_in_listing: true
draft: false
excerpt: このガイドでは、既存のKubernetesサービスをOpenShiftでうまく動作するように移行する方法を説明しています。
meta_description: このガイドでは、既存のKubernetesサービスをOpenShiftでうまく動作するように移行する方法を説明しています。
meta_keywords: migrate Kubernetes to OpenShift, openshift migration, SCCs
primary_tag: containers
related_content:
- slug: build-images-cloud-native-toolkit
  type: learningpaths
- slug: secure-context-constraints-openshift
  type: learningpaths
subtitle: KubernetesのサービスをRed Hat OpenShift上で動作するように変更する方法をご紹介します。
title: サービスをKubernetesからOpenShiftに移行する
---

Kubernetesクラスターにデプロイできるアプリケーションサービスを構築すると、サービスをホストするユーザーに大きな柔軟性を提供できます。クラスタがホストされている場所であれば、サービスもホストすることができます。Red Hat OpenShiftクラスターは、Kubernetesのすべての機能に加えて、より高いセキュリティとベンダーサポートを提供します。KubernetesとOpenShiftはほとんどの点で高い互換性を持っていますが、Kubernetesで適切に動作するサービスがOpenShiftでも全く同じように動作するとは限りません。

このガイドは、KubernetesとOpenShiftの両方のクラスターで適切にデプロイおよび実行されるようにサービスをパッケージ化する必要がある方のためのものです。具体的には、既存のKubernetesサービスをOpenShiftでうまく動作するように移行する方法を案内します。このような柔軟性を加えることで、Kubernetesのみを利用する顧客から、OpenShiftを利用する顧客まで、潜在的な顧客の市場を拡大することができます。

### スキルレベル

このガイドに従うには、Kubernetes と Red Hat OpenShift の経験者である必要があります。

### 読む時間

このラーニングパスは、約2時間で完了します。

## Openshiftの利用を検討する理由

OpenShiftはKubernetesをベースに構築されており、Red Hat Enterprise Linux（RHEL）テクノロジー上で動作し、エンタープライズアプリケーションのホスティングに価値のある追加機能を備えています。OpenShiftとRed Hat Enterprise Linuxには、LinuxやKubernetesのようなオープンソースプロジェクトに付随するコミュニティサポートよりも、より明確に定義されたSLAやセキュリティ機能を備えたRed Hatによるベンダーサポートが含まれています。OpenShift用に設計されたコンテナにはRHELライブラリが含まれており、Kubernetesよりも完全に統合されたスタックをRHELカーネルで実行します。

## KubernetesからOpenShiftへの移行

アプリケーションやサービスをKubernetesからOpenShiftに移行する際には、主に2つの問題点に注意する必要があります。  

1. コンテナのイメージ。Kubernetes用のイメージを構築するためのプロセスは、しばしばOpenShift用に改良する必要があります。

1. 保護されたLinux機能。保護されたLinux機能へのアクセスをコンテナに許可するためにクラスタが使用する機能は、KubernetesのものとOpenShiftでは異なります。

これらの問題について、もう少し詳しく調べてみましょう。

### コンテナイメージの移行

OpenShiftはKubernetesよりも安全にコンテナを実行しますが、このセキュリティ上の制約により、コンテナとそのアプリケーションを実行しようとするとエラーが発生することがあります。Red HatはOpenShiftのサポートだけでなく、OpenShiftで動作するコンテナのサポートも行っていますが、コンテナのイメージがRed Hatの認証仕様を満たすように構築されている場合に限ります。

コンテナがOpenShiftで安全に実行され、レッドハットのサポートの対象となるためには、イメージの構築プロセスをOpenShiftの要件に合わせて変更する必要があります。アプリケーションをコンテナとしてパッケージ化し、それをクラスターにデプロイするためのデプロイメントマニフェストを実装する際には、主に4つの領域に気を配る必要があります。

<button-link><text>Read the article</text><url>/learningpaths/migrate-kubernetes-openshift/migrate-images</url>。
</button-link> </button-link

### 保護されたLinux機能の移行

多くのアプリケーションは保護されたLinux機能へのアクセスを必要としません。そのような場合、Kubernetes と OpenShift では、ポッドでセキュリティコンテキストを指定して、デフォルトではブロックされている Linux 機能へのアクセスをコンテナに設定することができます。しかし、不正なコンテナが持つべきでないアクセスを自らに付与することを防ぐために、セキュリティコンテキストが付与しようとするアクセスをクラスタが承認する必要があります。

Kubernetesでは、ポッドセキュリティポリシー（PSP）という1つの機能を使ってアクセスを認可します。OpenShiftでは、セキュリティコンテキスト制約（SCC）という別の機能を使ってアクセスを認可します。したがって、Kubernetesで動作するPSPは、OpenShiftでは動作しません。PSPを、対応するパーミッションを持つSCCに変換する必要があります。

クラスタ管理者は、PSPとSCCを使ってクラスタを構成し、ポッドデプロイメントが使用できるようにするため、この違いが気になります。

<button-link><text>Read the article</text><url>migrate-kubernetes-psp-openshift-scc</url>。
</button-link>をクリックします。