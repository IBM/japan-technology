---
authors: ''
check_date: '2022-08-23'
completed_date: '2021-08-31'
components:
- openshift
- kubernetes
draft: false
excerpt: ネットワークアイソレーションを使用して、OpenShift上にデプロイされたアプリケーションを保護します。
menu_order: 3
meta_description: ネットワークアイソレーションを使用して、OpenShift上にデプロイされたアプリケーションを保護します。
meta_keywords: network isolation, network isolation in OpenShift, mulitenancy
meta_title: ネットワーク分離によるマルチテナンシーの実現
primary_tag: containers
subtitle: OpenShift上に展開されたアプリケーションをネットワーク分離で保護する
tags:
- containers
- security
title: ネットワークの分離
---

マルチテナンシーを実現するには、異なるテナントのネットワークを分離する必要があります。このチュートリアルでは、プロジェクトとネットワーク・ポリシーを使用して、IBM Cloud 上の OpenShift クラスターにデプロイされたアプリケーションとサービスのネットワーク分離を実現する方法を紹介します。

このチュートリアルでは、以下の方法を学びます。

- OpenShift でプロジェクトを作成し、[odo](https://odo.dev/)を使用して Open Liberty 上で動作する Web アプリケーションをデプロイします。
- プロジェクトにネットワークポリシーを使用してマルチテナントの分離を設定する。
- マルチテナントモードの設定をテストする。

### OpenShift のアクセス制御の見直し

おさらいですが、OpenShift のプロジェクトでは、名前空間にアクセスするために、認証と認可が必要です。これにより、認証されたユーザーのみがプロジェクト内のリソースにアクセスできるようになります。ネットワークポリシーは、OpenShift クラスタ内のポッドとネットワークエンドポイント間のトラフィックを制御するリソースです。これらはYAMLファイルで指定されたルールとして設定され、OpenShiftクラスターに適用されます。

ネットワークポリシーでできることの例は以下の通りです。

- OpenShift クラスター内のプロジェクト間のすべてのトラフィックをブロックする
- プロジェクト内のサービスに対する外部からのすべての受信トラフィックをブロックする
- プロジェクト内のサービス間のトラフィックを許可する

### チュートリアルの概要

このチュートリアルでは、2 つのサンプルアプリケーション App1 と App2 を使用して、マルチテナントモードを設定する方法を説明します。App1 と App2 です。

まず、アプリケーションを特定のプロジェクトにデプロイします。

  * App1 はプロジェクト `prj1` にデプロイされます。
  * App2は、プロジェクト `prj2` にデプロイされます。

デプロイされると、App1はエンドポイントを公開し、そのエンドポイントがApp2を呼び出して結果を返します。

次に、プロジェクト `prj2` にネットワークポリシーを適用して、App2 を隔離します。

次に、App1のエンドポイントを再度呼び出すことで、`prj2`のマルチテナントモードの構成をテストします。今回は、App1がApp2を呼び出すことができないので、呼び出しは結果を返さないはずです。以下の図は、ワークフローを示しています。

![os_network_isolation](images/os_network_isolation.png)


## 前提条件

このチュートリアルの手順を完了するには、以下が必要です。

- [IBM Cloud アカウントの作成](https://cloud.ibm.com)
- [Install odo](https://odo.dev/) - odoは、開発者がRed Hat OpenShiftやKubernetes上でコードを反復するのに役立つコマンドライン・インターフェース(CLI)です。
- [Install oc client](https://docs.openshift.com/container-platform/4.6/cli_reference/openshift_cli/getting-started-cli.html) - OpenShift のコマンドラインインターフェイス（CLI）である oc コマンドを使用すると、ターミナルからアプリケーションを作成したり、OpenShift Container Platform プロジェクトを管理したりすることができます。
- [Install Git client](https://git-scm.com/downloads)

## 見積もり時間

このチュートリアルを完了するには、約30分かかります。

## 手順

### OpenShiftクラスターの作成

OpenShift クラスターのインスタンスを作成します。[IBM Cloud Catalog](https://cloud.ibm.com/kubernetes/catalog/create?platformType=openshift)のプロンプトに従って、IBM Cloud にホストされたクラスターを作成します。

### レポをクローンする

以下のコマンドを実行して、レポをクローンします。


これで，`multitenant-network-isolation-tutorial`という名前のフォルダができました．このフォルダには、`App1`と`App2`という2つのアプリケーションのソースコードと、ネットワークポリシーの設定ファイルが入っています。

### IBM Cloud 上の OpenShift クラスターにログインします。

先ほど作成したクラスタの OpenShift Web コンソールを開きます。右上のログインしているユーザーIDをクリックし、**Copy Login Command**を選択します。

ターミナルウィンドウを開きます。先ほどコピーしたログインコマンドを使って、OpenShift にログインします。

### プロジェクトの作成

以下のコマンドを実行して、サンプルアプリケーションごとに2つのプロジェクトを作成します。


### アプリケーションのデプロイ

ここでは、アプリケーション `App1` をプロジェクト `prj1` に、`App2` をプロジェクト `prj2` にデプロイします。

以下のコマンドを実行して、アプリケーション `App1` をプロジェクト `prj1` にデプロイします。


デプロイされたアプリケーション `App1` の URL を取得します。


App1 "にアクセスするためのURLが返されます。そのURLをメモしておいてください。


次に、以下のコマンドを実行して、アプリケーション `app2` をプロジェクト `prj2` にデプロイします。

デプロイされたアプリケーションのURLを取得します。


App2 "にアクセスするためのURLを返します。URLをメモしておいてください。


### App1のエンドポイントを呼び出す

`App1`で公開されているエンドポイント `getdata` を呼び出すには、以下のCURLコマンドを使用します。内部的には、`App2`のエンドポイントを呼び出し、その結果を返します。


上記で呼び出されたURLは、[先ほどのApp1のURL]/app1/getdataです。

`.../multitenant-network-isolation-tutorial/app1/src/main/java/com/example/GetData.java` にあるソースJavaファイル `GetData.java` の `getRequest` メソッドを見てみましょう。

ここでは、getRequestメソッドで、`App2`のエンドポイント`http://app2.prj2.svc.cluster.local:9080/app2/resource`を呼び出しています。


「App1」が「App2」のエンドポイントを呼び出すことができれば、以下のような出力が得られるはずです。


### ネットワークポリシーを使ってprj2にマルチテナントモードを設定する

ここでは、プロジェクト `prj2` に対し、`App2` を `prj2` 内で隔離するためのネットワークポリシーを設定します。

マルチテナントモードの一環として、3つのネットワークポリシーを作成します。

* OpenShift の入口から許可する。
* 同じ名前空間からの許可
* OpenShift モニタリングからの許可

ルールを記載したYAMLファイルを以下に提供します。これらのポリシーは、OpenShift CLI インターフェースを使用してクラスターに適用します。

- **OpenShift Ingressからの許可** - Ingressは、クラスタの外からKubernetesサービスへのアクセスを可能にするオブジェクトです。

このポリシーでは、Ingressを通じてプロジェクト`prj2`に入ってくるリクエストを許可し、`App2`で公開されているエンドポイントを呼び出すことができるようにします。以下で説明するポリシーは、プロジェクト内のすべてのポッドに適用されます。しかし、`podSelector`を使用して、サービスを公開する必要があるポッドにこのポリシーを制限することができます。


- **Allow from same namespace** - このポリシーは、プロジェクト内のポッドからの接続のみを受け入れます。これを設定すると、`prj1` の `App1` は `prj2` の `App2` にリクエストを送ることができなくなります。以下のネットワークポリシーを設定すると、`App1` の URL `http://app2.prj2.svc.cluster.local:9080/app2/resource` への呼び出しは失敗します。


- **Allow from OpenShift monitoring** - このポリシーでは、OpenShift monitoringを使用してサービスのメトリクスを監視することを許可します。


次に、以下のコマンドを実行して、プロジェクト `prj2` にマルチテナントモードを設定します。


以下のコマンドを実行して、ネットワークポリシーが正しく設定されていることを確認します。


以下のような出力が表示されます。


### prj2のマルチテナントモード設定後にApp1のエンドポイントを起動する

「App1」が公開しているエンドポイント「getdata」を再び呼び出すには、以下のコマンドを使用します。


以下の出力からわかるように、`App1`は`App2`のエンドポイントを呼び出すことができません。


OpenShiftのウェブコンソールで`App1`のポッドログにアクセスすると、以下のようなエラーが表示されます。

### IBMクラウドのCalicoネットワークプラグイン

Red Hat® OpenShift® on IBM Cloud™クラスターには、[Calico](https://cloud.ibm.com/docs/openshift?topic=openshift-network_policies)というネットワークプラグインが設定されています。デフォルトのネットワークポリシーが設定されており、クラスター内の各ワーカーノードのパブリックネットワークインターフェースを保護します。CalicoとKubernetesを使って、クラスターのネットワークポリシーを作成することができます。Kubernetesのネットワークポリシーでは、クラスター内のポッドとの間で許可またはブロックしたいネットワークトラフィックを指定できます。ネットワークロードバランサー（NLB）サービスへのインバウンド（入口）トラフィックをブロックするなど、より高度なネットワークポリシーを設定するには、Calicoのネットワークポリシーを使用できます。

### 概要

このチュートリアルでは、Kubernetesのネットワークポリシーを使用して、プロジェクトのマルチテナント分離モードを設定しました。また、OpenShiftのネットワークポリシーと、それを使ってクラスタを隔離するための設定方法についても学びました。

詳しくは以下のリンクをご参照ください。
- [Controlling traffic with network policies for OpenShift on IBM Cloud](https://cloud.ibm.com/docs/openshift?topic=openshift-network_policies)
- [OpenShift でのネットワーキング](https://docs.openshift.com/container-platform/4.6/networking/understanding-networking.html)
- [Using odo for OpenShift](https://docs.openshift.com/container-platform/4.6/cli_reference/developer_cli_odo/understanding-odo.html)