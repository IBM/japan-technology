# Hyperledger Fabric ネットワークを IBM Cloud 上にデプロイする

### IBM Cloud Container 上の Kubernetes API サービスを利用してビジネス・ネットワークをセットアップする

English version: https://developer.ibm.com/patterns/deploy-hyperledger-fabric-network-on-ibm-cloud
  ソースコード: https://github.com/IBM/blockchain-network-on-kubernetes/

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-05-03

 
## 概要

ブロックチェーン・テクノロジーはビジネスに大革命をもたらし、ビジネス取引の方法を一新させます。ブロックチェーンでは、ビジネス・ネットワークに参加するメンバー間での取引の記録を、メンバー間で共有する不変のレジャーに残せるようにすることで、複数の関係者が関わる取引モデルを変えます。このようなブロックチェーン・ソリューションを開発するために必要になるのは、ブロックチェーン・アプリケーションを作成してデプロイする開発環境をセットアップすることです。このコード・パターンではブロックチェーンの開発を開始できるよう、IBM Cloud™ Container Service 上の Kubernetes API を使用して、迅速にブロックチェーン・ネットワークを Hyperledger Fabric 上にデプロイする方法を説明します。

## 説明

ブロックチェーンとは、取引の履歴を記録する不変の共有レジャーを指します。この不変の共有レジャーにより、信用を築き、説明責任、透明性を確保する新世代のトランザクション・アプリケーションが促されています。

ブロックチェーンの使用ケースを開発する際に必ず最初のステップとなるのは、ブロックチェーン・アプリケーションを作成してデプロイするための Hyperledger Fabric 対応の開発環境をセットアップすることです。セットアップした開発環境内で、Hyperledger Fabric 1.0 を稼働する小規模なブロックチェーン・ネットワークを作成することになります。Hyperledger Fabric ネットワークは、以下の形でセットアップすることができます。

* [Local Hyperledger Fabric network using Docker Compose](https://hyperledger-fabric.readthedocs.io/en/latest/build_network.html)
* [IBM Blockchain Platform](https://cloud.ibm.com/catalog/services/blockchain?cm_sp=ibmdev-_-developer-patterns-_-cloudreg)。IBM Cloud 上でホストされた柔軟な SaaS (Software-as-a-Service) オファリングです。
* [IBM Cloud](https://cloud.ibm.com/?cm_sp=ibmdev-_-developer-patterns-_-cloudreg) 上の Kubernetes API</li>

このコード・パターンでは、IBM Cloud 上の Kubernetes API を使用して、Hyperledger Fabric を基盤にビジネス・ネットワークをセットアップする際に必要となる手順を説明します。さらにこのコード・パターンには、迅速にネットワークをデプロイできる、自動化された完全なスクリプトも用意されています。[IBM Cloud Container Service](https://console.bluemix.net/containers-kubernetes/catalog/cluster?cm_sp=ibmdev-_-developer-patterns-_-cloudreg) では [Docker](https://docs.docker.com/get-started/) と [Kubernetes](https://kubernetes.io/) を結合した強力なツール一式を使用できるようになっていて、Docker でコンテナー化したアプリケーションを、Kubernetes API を使用して個別のコンピューティング・ホストからなるクラスターに自動的にデプロイし、運用、スケーリング、モニタリングすることができます。また、クラウドでホストされた Hyperledger Fabric ネットワークであれば、チーム・メンバー間でのコラボレーションも容易になります。

このパターンでは、それぞれに 1 つのピア・ノードを保持する 4 つの組織からなる Hyperledger Fabric ネットワークと、単一の発注サービスをプロビジョニングします。皆さん独自のブロックチェーン・ネットワークをデプロイする際は、以下の作業が必要となります。

1. 必要なネットワーク・トポロジー (つまり、組織の数、組織ごとのピアの数、発注サービス) を決定する
1. このパターンを使用してブロックチェーン・ネットワークをデプロイする
1. デプロイしたネットワークのブロックチェーン・アプリケーションの開発を開始する

## フロー

![フロー](../../images/arch-deploy-blockchain-kubernetes-1.png)

1. IBM Cloud Developer Tools の CLI にログインし、IBM Cloud Container Service プラグインを初期化します。
1. CLI を使用して Kubernetes クラスターのコンテキストを設定します。その後、Kubernetes 構成ファイルをダウンロードして、そのファイル内で KUBECONFIG 環境変数を設定します。
1. スクリプトを実行して Kubernetes クラスター上に Hyperledger Fabric ネットワークをデプロイします。
1. Kubernetes ダッシュボードにアクセスします。

## 手順

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the [README](https://github.com/IBM/blockchain-network-on-kubernetes/blob/master/README.md).
