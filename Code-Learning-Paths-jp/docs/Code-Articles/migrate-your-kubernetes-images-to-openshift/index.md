---
authors: ''
check_date: '2022-07-25'
completed_date: '2021-07-27'
display_in_listing: true
draft: false
excerpt: KubernetesからOpenShiftにイメージを移行する際には、以下の4つの部分が変化することに注意してください。
meta_description: KubernetesからOpenShiftにイメージを移行する際には、以下の4つの部分が変化することに注意してください。
meta_keywords: Kubernetes images, OpenShift images, Kubernetes to OpenShift migration
meta_title: KubernetesのイメージをRed Hat OpenShiftに移行する。
primary_tag: containers
subtitle: KubernetesからOpenShiftにイメージを移行する際に注力すべき4つの領域
tags:
- containers
title: KubernetesのイメージをRed Hat OpenShiftに移行する。
---

Red Hat OpenShiftは、Kubernetesベースのコンテナプラットフォームです。一般的に、Kubernetes クラスタで適切にデプロイおよび実行されるコンテナ化されたアプリケーションは、OpenShift クラスタでも適切にデプロイおよび実行されます。ただし、OpenShift にはいくつかのデフォルトのセキュリティ設定があり、OpenShift にデプロイするためにはコンテナイメージの構築方法を変更する必要があります。

この記事では、OpenShiftで実行するためにKubernetesコンテナイメージを変更する方法と、移行前にコンテナイメージの変更が必要かどうかを確認する方法を紹介します。この記事は、コンテナイメージを設計・構築する人にとって最も有意義なものです。

## 始める前に

ラーニングパス[Design, build, and deploy universal application images](https://developer.ibm.com/learningpaths/universal-application-image)では、KubernetesやOpenShiftでうまく動作するイメージを構築する方法を具体的に説明しています。

この記事では、KubernetesのイメージをOpenShiftで実行できるようにしようとするときに最も問題となる、オリジナルのラーニングパスでカバーされている4つの分野を紹介します。これらには以下が含まれます。

* OCIに準拠したコンテナイメージの構築
* コンテナイメージでのrootユーザーアクセスなしでのプロセス実行
* ベースイメージをRed Hat Enterprise LinuxまたはUniversal Base Imageとしたコンテナイメージの構築
* 統合されたイメージレジストリまたは外部イメージレジストリへのイメージの保存

## OCI に準拠したコンテナイメージの構築

<sidebar>
    <p><b>CRIとOCI-コンプライアンス</b></p><br/> </b><b
    <p>コンテナランタイムは、コンテナイメージを受け取り、そのイメージで定義されたアプリケーションを実行します。もともとKubernetesでは、クラスタの個々のノードがDockerのランタイムを使ってコンテナを実行していました。より多くのコンテナランタイムに対応するために、KubernetesはKubernetesとコンテナランタイムの間に[Container Runtime Interface](https://kubernetes.io/blog/2016/12/container-runtime-interface-cri-in-kubernetes/) という抽象化を行いました。(CRI)と呼ばれるものがあります。CRIは、再コンパイルの必要なく、多種多様なコンテナランタイムを使用するのに役立ちます。
    <p>CRIに準拠したランタイムは、OCIにも準拠しているため、OCIに準拠したイメージを実行することができます。 </p> <p>CRIに準拠したランタイムは、OCIにも準拠しています。
    </sidebar>
    
OCI 準拠のコンテナイメージを構築する方法を理解する前に、まず Open Container Initiative (OCI) が OpenShift とどのように関係しているかを理解する必要があります。

[Open Container Initiative (OCI)](https://opencontainers.org/)は、すべてのコンテナランタイムが、どんなビルドツールで作られたイメージでも実行できるようにするために作られました。OCI はコンテナイメージのフォーマットとランタイムの仕様を公開しています。コンテナイメージは、[OCI Runtime Specification](https://github.com/opencontainers/runtime-spec/blob/master/spec.md)に準拠したあらゆるコンテナランタイムで実行できるように、[OCI Image Format Specification](https://github.com/opencontainers/image-spec/blob/master/spec.md)に準拠する必要があります。OCIはDockerを置き換えるものではなく、Docker EngineはOCIに準拠しています。

OpenShift Container Platform v4では、DockerコンテナエンジンをOCI互換のランタイムとコンテナイメージに特化した軽量コンテナエンジンであるCRI-Oに置き換えました。

### OCI準拠のイメージをOpenShiftに移行する。

OCI準拠のイメージをOpenShiftに移行するには、コンテナイメージがCRI-OのようなOCI準拠のコンテナランタイムで動作するようにOCI準拠であることを確認する必要があります。OCIに準拠したイメージを作成するには、OCIに準拠したイメージを作成するイメージビルドツールを使用します。イメージのビルドにはDockerを使用することもできますが、コンテナランタイムに依存しないOCI準拠のイメージのビルド、実行、管理を支援するツール[Buildah, Podman, Skopeo](https://www.redhat.com/en/blog/say-hello-buildah-podman-and-skopeo)があります。

[OCI準拠のイメージを構築する手順](https://developer.ibm.com/learningpaths/universal-application-image/build-image/#1-use-oci-compliant-tools)については、「Build universal application images」の記事をお読みください。

## root 権限で実行されるプロセスがないイメージの構築

デフォルトでは、イメージのビルドツールは、Dockerfile で別のユーザーが指定されていない限り、root としても実行される（`uid=0` の場合）イメージのビルドに root を使用します。デフォルトでは、OpenShift は任意に割り当てられた非 root ユーザー ID を使用してコンテナを実行します。他のユーザーがアクセスできないファイルへのアクセスなど、ユーザーがrootであるために成功するアクションを実行するイメージは、OpenShiftではこれらのアクションを実行することができません。

### root アクセスによるプロセスへの影響を示す例

rootアクセスが一般的なプロセスにどのような影響を与えるかを示すために、ベースとなるOSのファイルシステムのrootディレクトリ内のファイルを削除する例を見てみましょう。以下の例では、Ubuntu OSを使用しています。

以下のDockerfileには、rootユーザーのアクセスが必要な`/etc/passwd`ファイル（ベースOS `ubuntu`関連）を削除する手順が書かれています。


コンテナイメージは、Dockerfileからビルドされ、IBM Cloud Container Registryのようなレジストリに保存されます。

**Kubernetesでデプロイする**。

このDockerfileをKubernetesにデプロイすると、このような結果になります。

ポッドのステータスは **Completed** で、実行が完了したことを示しています。


ポッドログを見ると、`/etc/passwd`ファイルが正常に削除されています。


**OpenShiftでのデプロイ**。

このイメージをOpenShift上に`oc new-app`コマンドでデプロイすると、以下のような結果になります。

警告メッセージが表示されます。**Image "`us.icr.io/test-namespace/root-app:v1`" は 'root' ユーザーとして実行されますが、これはクラスタ管理者によって許可されていない可能性があります**。


ポッドステータスは***CrashLoopBackOff***で、コンテナがクラッシュしたことを示しています。


ポッドログを見ると、OpenShift Container Platformのデフォルト設定では、イメージ内でroot権限を持つプロセスの実行が許可されていないため、`delete`コマンドの実行に失敗しています。


### 移行時のルートアクセス権限の対処法

移行する前に、コンテナイメージがrootアクセスを必要とするかどうかを評価し、rootで実行しないようにイメージを修正する必要があります。

rootユーザーのアクセスを必要としないイメージであれば、図のようにDockerfileに非rootの`USER`を指定するのがベストです。