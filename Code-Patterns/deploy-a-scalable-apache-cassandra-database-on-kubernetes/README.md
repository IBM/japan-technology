# スケーラブルな Apache Cassandra データベースを Kubernetes 上にデプロイする

### 既存のアプリケーションをシームレスにクラウドに移行する

English version: https://developer.ibm.com/patterns/deploy-a-scalable-apache-cassandra-database-on-kubernetes
  ソースコード: https://github.com/IBM/scalable-cassandra-deployment-on-kubernetes

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2017-10-28

 
## 概要

最近の企業では、膨大な量のデータを収集し、保管し、分析するようになっています。複数のデータ・センター、コモディティー・サーバー、クラウドの全体にわたって大量の構造化データ、半構造化データ、非構造化データを管理するには、極めてスケーラブルなオープンソースの NoSQL データベースである Apache Cassandra が理想的な選択肢となります。Kubernetes は、世界で最もよく使われているコンテナー・オーケストレーション・システムであり、GitHub 上の最もアクティブなプロジェクトの 1 つとしてランキングされています。このコード・パターンで、クラウド・ネイティブの Cassandra 実装を Kubernetes 上にデプロイして、この 2 つの強力なシステムを統合する方法を説明します。

## 説明

このコード・パターンでは、Kubernetes クラスターが発揮する最大限の力を明らかにするために、NoSQL データベースとして世界で最もよく使われている Apache Cassandra を、コンテナー・オーケストレーション・プラットフォームとして世界で最もよく使われている Kubernetes 上にデプロイする例を説明します。この例から、IBM Cloud Container Service 内の Kubernetes クラスターからマルチノードのスケーラブルな Cassandra クラスターをデプロイするための完全なロードマップを把握できるはずです。Cassandra の各コンポーネントは、単独のコンテナー内またはコンテナーのグループ内で稼働します。

Apache Cassandra の分散型システムでは、複数のデータ・センターにわたって多数のノードをデプロイすることができます。しかも Cassandra の分散型アーキテクチャーは、複数のデータ・センターでのデプロイメント、冗長性、フェールオーバー、そして障害回復を明確な目的として調整されています。これらの特長から、Cassandra はコンテナー・オーケストレーション・プラットフォームと抜群に相性が良く、自動化、運用、スケーリング、モニタリングのすべてのメリットを最大限に利用できます。

## フロー

![フロー](../../images/architecture-cassandra-on-kube.png)

1. 開発者がヘッドレス・サービスを作成します。Kubernetes サービスとは、論理的なポッドのセットと、それにアクセスするポリシーを定義する抽象的なものです。Cassandra クラスターの生成と「シード」のディスカバリーには、ヘッドレス Cassandra サービスを利用します。
1. 開発者が Kubernetes ReplicationController を作成します。このコントローラーが、Cassandra クラスターの非永続型ポッド・ノードを作成し、スケーリングに対応します。最初の Cassandra ノードが作成されたことを確認した後、開発者は ReplicationControlle 内にさらにノードを追加して Cassandra クラスターをスケーリングできます。
1. 永続型 Cassandra ノードを作成するために、開発者は提供されたファイルを使用してボリュームを作成し、静的プロビジョニングを使用して永続ボリュームとしてプロビジョニングします。これらの PersistentVolume を、Cassandra ノードと同じ数だけ作成します。
1. 開発者が Kubernetes StatefulSets を使用して、Cassandra クラスターの永続型ノード・ポッドを作成し、クラスターをスケーリングします。StatefulSet の役目は、順序付けられたデプロイメント、順序付けられたターミネーションを行い、ネットワークに一意の名前を付けることです。
1. 開発者が Cassandra Query Language (CQL) を使用して、Cassandra キー・スペース上に Employee テーブルを作成し、更新します。

## 手順

このコード・パターンに取り組む準備はできましたか？詳しい手順については、[README](https://github.com/IBM/scalable-cassandra-deployment-on-kubernetes) を参照してください。
