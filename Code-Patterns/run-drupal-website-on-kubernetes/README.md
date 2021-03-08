# Drupal 駆動の Web サイトを Kubernetes 上で実行する

### Kubernetes の力を利用して Drupal デプロイメントを管理する

English version: https://developer.ibm.com/patterns/run-drupal-website-on-kubernetes
  ソースコード: https://github.com/IBM/drupal-on-kubernetes-sample

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-08-01

 ## 概要

Drupal は人気の高い無料のオープンソース CMS (コンテンツ管理システム) です。Drupal をバックエンドとして使用している Web サイトの数は、世界中で数百万にも上ります。このパターンでは、Drupal サイトの速度と回復力を向上させるために、サイトを複数のマイクロサービスに分割するという方法を説明します。このパターンは、Drupal 駆動のサイトを Kubernetes 上で実行するという明確な目的を持った開発者向けです。Kubernetes を活用してマイクロサービスをオーケストレーションすれば、簡単に Drupal のスケーラビリティーと力を利用できるようになります。そのため、Drupal の新しいリリースを使用して、サイトに悪影響を与えることなく、最新の状態にサイトを維持しておくことが容易です。

## 説明

このパターンでは、Kubernetes と Postgres を使用して Drupal サイトをセットアップします。Drupal は人気の高いオープンソース CMS (コンテンツ管理システム) です。Drupal をバックエンドとして使用している Web サイトの数は、世界中で数百万にも上ります。サービスをコンテナーに分割することで、Kubernetes の力を利用できるようになります。

このコード・パターンをひととおり完了すると、以下の方法がわかるようになります。

* Kubernetes 内で複数のコンテナーを実行するアプリを構成する
* Kubernetes を介してホストされた Web サイトを実行する
* Kubernetes の永続ボリュームを使用して、コンテナーが再起動されても常に Drupal の構成が維持されるようにする

## フロー

![フロー](../../images/arch-diagram-deploying-drupal-iks.png)

1. ユーザーが Drupal Web インターフェースを操作します。
1. Drupal コンテナーは独自の永続ボリュームを使用して Web サイト・データを保管します (コンテンツは保管しません)。
1. Drupal コンテナーが PostgreSQL コンテナーに接続して Web サイトのコンテンツにアクセスします。
1. PostgreSQL コンテナーは独自の永続ボリュームを使用してデータベースのコンテンツを保管します。

## 手順

1. リポジトリーを複製します。
1. Kubernetes クラスターを作成します。
1. サービスとデプロイメントを作成します。
1. Drupal にアクセスします。

このパターンに取り組む準備はできましたか？アプリケーションを起動して使用する方法について詳しくは、[README](https://github.com/IBM/drupal-on-kubernetes-sample/blob/master/README.md) を参照してください。
