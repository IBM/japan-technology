# プライベート・クラスターとパブリック・クラスターの両方にわたって Istio を使用する

### プライベート・クラスターとパブリック Kubernetes クラスター間でサービスを接続してハイブリッド・クラウドを構成する

English version: https://developer.ibm.com/patterns/istio-for-multi-clusters-across-iks-and-icp
  ソースコード: https://github.com/IBM/istio-hybrid/

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2018-09-05

 
## 概要

ハイブリッド・クラウドを最後まで進めることに決めたとしたら、さまざまなワークロードのすべてを管理するのは簡単ではないと覚悟していることでしょう。このパターンで取り上げるアプリは、Web フロントエンド、ストレージ用の Redis leader とそのレプリカとして作成された一連の Redis followers、そして Kubernetes のレプリケーション・コントローラー、ポッド、サービスで構成されています。  この[サンプル・アプリケーション](https://github.com/IBM/guestbook/tree/master/v2)では、ユーザーがコメントを送信すると Watson Tone Analyzer によってコメントの内容に応じた絵文字が追加されます。この目的を達成するため、私たちは各種のマイクロサービスが Kubernetes クラスター上でもプライベート・クラウド・クラスター上でも稼動するよう、マルチクラスターを構成しました。サンプル・アプリがリモートの Tone Analyzer サービスを呼び出すときは、クラスター間の通信を確立します。Tone Analyzer サービス自体は、クラウドから Watson Tone Analyzer サービスを呼び出します。

## 説明

このパターンでは、[IBM Cloud Private](https://www.ibm.com/jp-ja/cloud/private) と [IBM Cloud Kubernetes Service](https://www.ibm.com/jp-ja/cloud/container-service) (IKS) クラスターとの間で Istio を使ってサービスを接続することで、ハイブリッド・クラウドを作成します。IBM Cloud Private に組織ネットワークの外部からアクセスすることはできませんが、IBM Cloud Private は IKS クラスターにアクセスできるということを前提としてあります。したがって、IBM Cloud Private クラスターから VPN トンネルを起動すれば、IBM Cloud Private 上で稼動するサービスと IKS 上で稼動するサービスとの間に VPN トンネル経由の双方向通信をセットアップできます。

このパターンで使用するサンプル・アプリケーションには Watson Tone Analyzer を利用するために IBM Cloud が必要ですが、ここで紹介する次のようなパターンは、プライベート・クラスターとパブリック・クラスターを統合するシナリオのほとんどで使用できます。

* VPN トンネルを使用してプライベート・クラウドとパブリック・クラウドを接続する
* プライベート・クラスターとパブリック・クラスターの間でマイクロサービスを分散させながらも、マイクロサービス間の双方向接続を維持する
* Istio を使用して、マルチクラスターのトラフィックをルーティングする

## フロー

![フロー](../../images/istio-hybrid-arch-diagram.png)

1.  `guestbook` アプリのユーザーがブラウザーを使用して、`guestbook` サービスが提供する Guestbook Web ページにパブリック・クラウドからアクセスします。
1.  ゲストがコメントを送信した場合、`guestbook` サービスは送信されたテキストのトーンに基づく感情アイコンで、そのコメントをエンリッチする必要があります。したがって、`guestbook` サービスはトーンを分析するために  `analyzer` サービスを呼び出し、送信されたテキストを渡します。`guestbook` サービスは、それがローカル・サービスであるかのように `analyzer` サービスを呼び出します (サービス/アプリはリモート・サービスをサポートするように変更されていません)。
1.  `analyzer` サービスはリモートのプライベート・クラウド上で稼動しているため、呼び出しが Istio によって VPN トンネル経由でプライベート・クラウドの Ingress ゲートウェイにルーティングされます。
1.  `analyzer` サービスが *Watson Tone Analyzer* サービスを呼び出し、受信したテキスト・ペイロードを渡します。これにより、パブリック・サービスからトーンの分析結果が返されます。
1.  `analyzer` サービスからのレスポンスが到着すると、`guestbook` アプリは送信されたテキストと一致する感情アイコンを Web ページ内のコメントに追加します。

## 手順

 このパターンに取り組む準備はできましたか？このアプリケーションを起動して使用する方法について詳しくは、[README](https://github.com/IBM/istio-hybrid/blob/master/README.md) ファイルを参照してください。
