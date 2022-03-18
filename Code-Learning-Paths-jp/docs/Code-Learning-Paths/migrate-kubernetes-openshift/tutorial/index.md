---
authors: ''
completed_date: '2021-08-23'
components:
- openshift
- kubernetes
- devops
draft: false
excerpt: このチュートリアルでは、イメージの変更とセキュリティポリシーの移行を中心に、KubernetesからOpenShiftへのワークロードの移行を説明します。
menu_order: 4
meta_description: このチュートリアルでは、イメージの変更とセキュリティポリシーの移行を中心に、KubernetesからOpenShiftへのワークロードの移行を説明します。
meta_keywords: migrate Kubernetes to OpenShift, openshift migration, SCCs
meta_title: ワークロードをKubernetesからOpenShiftに移行することができます。イメージとPSPの移行
primary_tag: containers
subtitle: KubernetesからOpenShiftへの移行例を示すチュートリアル
title: チュートリアル例
---

このラーニングパスの前の部分では、ワークロードをKubernetesからOpenShiftに移行する際に注力すべき2つの領域を紹介しました。リマインダーとして、どのようにするかを慎重に検討する必要があります。

- イメージをアップデートしてKubernetesとOpenShiftの両方で動作させる
- KubernetesのPod Security Policies（PSP）をOpenShiftのSecurity Context Constraints（SCC）に移行する。

このチュートリアルでは、イメージの変更とセキュリティポリシーの移行を中心に、KubernetesからOpenShiftへのワークロードの移行について説明します。

## 移行のシナリオ

このチュートリアルで使用するアプリケーションは、特定のAPIを公開し、それらのAPIの統計情報を記録するシンプルなNode.jsアプリケーションです。API の統計情報は、API 名とその API が呼び出された回数を含む .CSV ファイルとして保存されます。このチュートリアルでは、ボリュームの参照先としてコンテナファイルシステムのディレクトリを使用していますが、ファイルシステムを[persistent volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)に置き換えることができます。

以下の機能を持つポッドセキュリティポリシー(PSP)を持つKubernetesクラスタにサンプルアプリケーションを展開します。

* 特定のユーザーがアプリケーションコンテナにアクセス可能
* 「EmptyDir」ボリュームへのアクセスを許可する。
* 特権的なアクセスをユーザーに制限する

このチュートリアルでは、コンテナイメージのベストプラクティスに従い、アプリケーションをデプロイするためのセキュリティポリシーを保持しながら、サンプルアプリケーションをKubernetesからOpenShiftに移行する方法を説明します。

## 事前に必要なもの

このチュートリアルの手順を完了するには、次のものにアクセスする必要があります。

* [IBM Cloud アカウント](https://cloud.ibm.com) (このチュートリアルを IBM Cloud で試す場合)
* [Kubernetes クラスター](https://cloud.ibm.com/kubernetes/catalog/create)。このチュートリアルでは、IBM クラウド・カタログでアクセスできる IBM Kubernetes Service を使用します。
* [An OpenShift cluster](https://cloud.ibm.com/kubernetes/catalog/create?platformType=openshift)を使用します。このチュートリアルでは、IBM Cloud 上の OpenShift クラスターを使用します。他の OpenShift 環境でも、手順を再現できるはずです。
* [Gitクライアント](https://git-scm.com/downloads)
* [kubectl クライアント](https://kubernetes.io/docs/tasks/tools/)
* [oc のクライアント](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html)
* [DockerHub アカウント](https://hub.docker.com/)

## 見積もり時間

このチュートリアルを完了するには、約60分かかります。

## 手順

1. コードを入手する
2.作成したアプリケーションをKubernetesにデプロイする
3.移行用のコードを準備する
4.移行したアプリケーションをOpenShiftにデプロイする
5.移行結果の分析

### 1.コードの取得

以下のリポジトリをクローンします。


### 2.アプリケーションのKubernetesへのデプロイ

****1.コンテナイメージの作成

まず、アプリケーションのコンテナイメージを構築する必要があります。このチュートリアルでは、DockerHubをイメージレジストリとして使用します。このチュートリアルではDockerHubをイメージレジストリとして使用していますが、お好みのイメージレジストリを選択してください。

以下のコマンドを実行して、コンテナ・イメージを構築します。

イメージのURL`<your-docker-account>/k8image`をメモしておきます。以下のコマンドで`deploy.yaml`を修正します。


****2.アプリケーションのデプロイ

ターミナルウィンドウを使ってKubernetesクラスタにログインします。

IBM Cloud Kubernetesサービスの場合、IBM Cloudダッシュボードの「Resource Summary」セクションの「Clusters」に移動し、クラスタの名前をクリックします。「Actions > Connect via CLI」を選択し、指定された手順を実行してクラスターにアクセスします。

このチュートリアルでは、名前空間 `mlp-ns` とサービス・アカウント `mlp-sa` を使用します。ネームスペースとサービスアカウントを作成してください。


ターミナルウィンドウで、クローンリポジトリの `deploy-to-k8s` フォルダに移動し、以下のコマンドを実行してください。


以下のコマンドで、ポッドに正しいPSPが適用されているかどうかを確認します。


のように出力されるはずです。


ポッドのデプロイには、`custom-mlp-psp`というPSPが適用されていることに注目してください。


**3.アプリケーションにアクセスする**。

`kubectl get nodes -o wide`というコマンドでIBM KubernetesクラスタのパブリックIPを取得し、`http://<cluster-public-ip>:32600/`でアプリケーションにアクセスできます。

このアプリケーションは3つのAPIを公開しています。APIは、`/api1`, `/api2`, `/api3`の3つを公開しています。

これらのAPIを呼び出すにはCURLコマンドを使用します。


APIの呼び出しにより、コンテナのボリュームマウントパス `/mydata` にあるファイル `apistats.csv` が更新される。このファイルには、それぞれのAPIが呼び出された回数が記録されている。これらのAPIを何度も呼び出してみてください。

APIが呼び出されるたびに、ファイル`apistats.csv`が更新されているかどうかを確認してください。

次のコマンドでコンテナシェルに入ります。


ここで、ディレクトリを`/mydata`に変更します。すると、`apistats.csv`という名前のファイルが見つかるはずです。このファイルの内容を印刷すると、ログに記録されたデータを見ることができます。


このような出力が得られるはずです。


おめでとうございます。これで既存の設定をシミュレートできました。

### 3.マイグレーション用のコードの準備

このセクションでは、移行のために必要な変更点について説明します。なお、このチュートリアルでは、`migrate-apps-from-k8s-to-ocp/deploy-to-openshift`にある修正コードを提供しているので、変更する必要はありません。参考までに以下の内容を記載します。

#### 3.1 画像の移行

Dockerfileを修正する際は、以下を参考にしてください。

* [Migrate your Kubernetes images to OpenShift](https://developer.ibm.com/learningpaths/migrate-kubernetes-openshift/migrate-images/)
* [Best practices for designing a Universal Application Image](https://developer.ibm.com/learningpaths/universal-application-image/design-universal-image/)

修正したDockerfileは、クローンしたリポジトリの`~/migrate-apps-from-k8s-to-ocp/deploy-to-openshift`で提供されています。そのファイルの内容を紹介します。


この例では、次のようなベスト・プラクティスに基づいて画像を作成しています。イメージは

* ベースイメージとしてRed Hat UBIを使用。
* 最新のセキュリティアップデートを含む
* 2段階のイメージビルドを使用
* ユーザーIDを定義して、ルートユーザープロセスを回避する

> 注意：Red Hat認証に合格できるイメージを構築したい場合は、Dockerfileにラベルやライセンスフィルなどの情報を追加する必要があるかもしれません。詳しくはこちらの記事でご紹介しています。[Best practices for designing a universal application image](https://developer.ibm.com/learningpaths/universal-application-image/design-universal-image/)をご覧ください。

また、[Cloud-native toolkit](https://cloudnativetoolkit.dev)を使用して、OpenShiftの認証可能なイメージを構築することもできます。詳しくはラーニングパスの[Build Images with the Cloud-Native Toolkit](https://developer.ibm.com/learningpaths/build-images-cloud-native-toolkit/)をお読みください。

#### 3.2 Kubernetes PSPからOpenShift SCCへの移行

記事[Migrate your Kubernetes pod security policies to OpenShift security context constraints](https://developer.ibm.com/learningpaths/migrate-kubernetes-openshift/migrate-kubernetes-psp-openshift-scc/)では、PSPをSCCに移行するために必要なことを正確に説明しています。

「psp.yaml」を「scc.yaml」に移行すると、以下のようになります。


いくつかのフィールドは `scc.yaml` と `psp.yaml` で異なることに注意してください。

* 種類が `PodSecurityPolicy` から `SecurityContextConstraints` に変更されました。
* `privileged` は `allowPrivilegedContainer` に変更されました。
* ユーザーとグループの範囲指定の方法が変わりました。
* ボリュームの制御方法に変更はありません

同様に、`rbac.yaml`も移行され、Gitレポの`deploy-to-openshift`フォルダに置かれています。

### 4.移行したアプリケーションを OpenShift にデプロイします。

**4.1 コンテナイメージの構築**。

ステップ2で述べたように、アプリケーションのコンテナイメージを構築する必要があります。

> 注意：このチュートリアルでは、DockerHubをイメージレジストリとして使用しています。注意：このチュートリアルでは、イメージレジストリとしてDockerHubを使用していますが、統合されたイメージレジストリやその他のイメージレジストリを選択することができます。

イメージのURL`<your-docker-account>/ocp-image`をメモしておきます。以下のコマンドで`deploy.yaml`を修正します。


****4.2 アプリケーションのデプロイ

ターミナルウィンドウを使って、OpenShiftクラスタにログインします。

IBM Cloud コンソールから、`Clusters > Your OpenShift Cluster > OpenShift web console`に移動します。OpenShift ウェブ・コンソールで、右上隅のメニュー（メールアドレスを含むラベル）をクリックし、「Copy Login Command」を選択します。Display token "をクリックして、コマンドをターミナルセッションにペーストし、OpenShiftクラスターにログインします。


このチュートリアルでは、名前空間 `mlp-ns` とサービスアカウント `mlp-sa` にKubernetesと同じ名前を使用しています。

以下のコマンドを実行します。


ターミナルウィンドウから、クローンしたリポジトリの `deploy-to-openshift` フォルダに移動します。

以下のコマンドを実行します。


以下のコマンドを実行して、ポッドにどのようなSCCが適用されているかを確認します。


このような出力が得られるはずです。


ポッドのデプロイに対して、`mlp-scc` SCCが適用されていることに注目してください。

サービスを公開して、アプリケーションにアクセスするためのルートを取得します。


このルートを使って、デプロイされたアプリケーションにアクセスすることができます。

### 5.結果の分析

`http://<ルート>`を使ってアプリケーションにアクセスできます。CURLコマンドを使ってAPIを呼び出すことができます。


これらのAPIを複数回呼び出してみましょう。

「apistats.csv」ファイルを確認するには、コマンドでコンテナにアクセスします。


ここで、ディレクトリを `/mydata` に変更します。ファイル `apistats.csv` の内容を印刷して、ログデータを確認します。


おめでとうございます。イメージとポッドのパーミッションを変更することで、KubernetesからOpenShiftへのアプリケーションの移行に成功しました。

> なお、このチュートリアルでは、パーシステントボリュームではなく、コンテナ内のマウントパスを使用しています。このため、`apistats.csv`ファイルの内容は、アプリケーションと一緒に移行されません。このファイルは、デプロイされたコンテナごとに新たに作成されます。

### トラブルシューティング

以下に、発生する可能性のある問題とその解決策を示します。これは完全なリストではなく、一般的な問題とその解決策を示しています。

#### アプリケーションが OpenShift にデプロイされない。

コマンド `oc get events` でイベントを確認してください。

[`**ケース1**:イベントでは、`unable to validate against any security context constraint:Invalid value: xxxx: must be in the ranges:[yyyy, zzzzz]]と表示されます。

このエラーが発生する原因として、以下のことが考えられます。
- 正しい SCC が配備に適用されていない。正しい SCC を適用できるように、ロールとロールバインディングが設定されていることを確認してください。
- SCC は配置ファイルで指定されたユーザを許可していません。SCC が、配置で指定されたユーザーにポッドの配置を許可していることを確認してください。

`**ケース2**:イベントでは、`unable to validate against any security context constraint: [spec.volume[0]:無効な値です。`"emptyDir": emptyDirボリュームは、プロバイダの制限を使用することはできません`。

このエラーは、SCCが`emptyDir`ボリュームの使用を許可していない場合に発生します。`scc.yaml` ファイルの `volumes` で `emptyDir` が許可されていることを確認してください。

同様に、他のパラメータのエラーも確認し、問題を解決してください。

#### アプリケーションに、SCCで定義されているものよりも追加のコンテナパーミッションが設定されています。

Kubernetesでは、特権コンテナを許可するポリシーを指定するコントロールキーは `privileged` です。OpenShiftでの同じコントロールキーは、`allowProvilegedContainer`です。また、`allowProvilegedContainer`はデフォルトでは`true`となっています。そのため、このフラグが正しい値で設定されていることを確認することが重要です。

このフラグの値を確認するには、`oc get scc mlp-scc -o yaml`というコマンドを実行します。出力では、`allowPrivilegeEscalation`に正しい値が設定されていることを確認します。同様に、PSPから対応するすべてのフラグが利用可能で、正しい値が設定されていることを確認します。

### まとめ

このチュートリアルでは、サンプルアプリケーションを使用して、KubernetesからOpenShiftへのアプリケーションの移行プロセスを示しました。このチュートリアルでは、2つの分野での移行について紹介します。
- イメージの移行: コンテナイメージのベストプラクティスに従う
- ポッドセキュリティの検討：ポッドのセキュリティパーミッションをセキュリティコンテキスト制約に移行する