# パブリック・クラウド内のデジタル・ウォレットをセキュリティーで保護する

### Web フロントエンドを備えたデジタル・ウォレット・アプリケーションと Electrum ビットコイン・クライアントを IBM Cloud Hyper Protect Virtual Server 内にデプロイする

English version: https://developer.ibm.com/patterns/secure-bitcoin-wallet-with-ibm-cloud-hyper-protect-virtual-servers
  ソースコード: https://github.com/IBM/secure-bitcoin-wallet/

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2020-01-28

 
## 概要

このコード・パターンでは [Electrum 3.3.6](https://github.com/spesmilo/electrum/tree/3.3.6) を使用して、Web フロントエンドを備えたデジタル・ウォレット・アプリケーションと Electrum ビットコイン・クライアントを IBM Cloud Hyper Protect Virtual Server 内にデプロイする方法を説明します。このアプリケーションを IBM Cloud Hyper Protect Virtual Server 内にデプロイするとともに、ビットコイン・ウォレットを暗号化するために IBM Cloud Hyper Protect Crypto Services を統合します。この統合は省略可能ですが、この統合によってセキュリティーがさらに強化されます。

## 説明

ビットコインのような暗号通貨は、デジタル・アセットを盗もうとするハッカーに狙われるため、トップレベルの保護が必要になります。通貨の安全を守るためには、デジタル・ウォレットをセキュリティーで保護しなければなりません。このコード・パターンのサンプルでは、アクセスしやすいようにデジタル・ウォレットをパブリック・クラウド内にデプロイしますが、IBM Cloud Hyper Protect Services を使用して高度なセキュリティーを確保します。

まず始めに、IBM Cloud Hyper Protect Virtual Server インスタンスを作成します。このインスタンスに正しいユーザーしかアクセスできないようにするために、SSH 鍵を生成します。続いて、Python バックエンド・アプリケーションを作成してデプロイし、最後に Electrum ビットコイン・アプリケーションを作成してデプロイします。このビットコイン・アプリケーションでは Node.js を使用して静的 Web サイトに対応し、jQuery を使用して Python バックエンド・アプリにリクエストを送信します。完成したデジタル・ウォレット・アプリケーションは、ユーザー情報を受け入れてクラウド上のビットコイン・ファンドにアクセスできます。このアプリを IBM Cloud Hyper Protect Virtual Server 内で実行することで、アプリで使用するストレージも確実に暗号化できます。さらに、IBM Cloud Hyper Protect Crypto Services を利用すれば、改ざん防止策が講じられた HSM 内に保管された鍵によってアプリケーション自体も暗号化されるようにすることができます。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* Etherum ビットコイン・デジタル・ウォレット・アプリケーションを作成して実行する
* IBM Cloud Hyper Protect Virtual Server を立ち上げる
* (省略可) IBM Cloud Hyper Protect Crypto Services を統合してウォレットを暗号化する

## フロー

![フロー図](../../images/flow.png)

1. ユーザーがブラウザーから、Electrum フロントエンドに接続されたビットコイン・ウォレット・アプリケーションにアクセスします。
1. リクエスト (送信/受信) は、Electrum ビットコイン・クライアント・サーバーにルーティングされます。これは JSON RPC サーバーとして稼働し、ビットコイン・ネットワークとやりとりしてウォレットを管理します。
1. ウォレット・ファイルを暗号化/復号には、アプリケーションが HSM 内に保管された鍵を使用する必要があります。HSM 内に保管された鍵には IBM Cloud Hyper Protect Crypto Services を介してアクセスできます。

## 手順

このパターンの詳しい手順については、[README](https://github.com/IBM/secure-bitcoin-wallet/blob/master/README.md) ファイルを参照してください。
