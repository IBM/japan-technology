# オフライン・ファーストのショッピング・リスト・プログレッシブ Web アプリを作成する

### Web アプリの利便性とネイティブ・アプリのパフォーマンスを兼ね備えたプログレッシブ Web アプリを構築する

English version: https://developer.ibm.com/patterns/create-an-offline-first-shopping-list-progressive-web-app
ソースコード: https://github.com/ibm-watson-data-lab/shopping-list-vanillajs-pouchdb

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2019-03-28

 
## 概要

Vanilla JS (プレーン JavaScript)、React、Preact、Polymer、Ember.js、Vue.js のそれぞれを使用して作成された、オンライン・ファーストの一連のショッピング・リスト・プログレッシブ Web アプリのデモを紹介します。各実装では PouchDB を使用して、アプリがオフラインでもオンラインでも機能するようになっています。オンライン時のアプリは、Cloudant&reg; NoSQLDB と同期します。

## 説明

私たちは、それぞれに異なるスタックを使用した一連のオフライン・ファースト・デモ・アプリを作成しました。具体的には、Vanilla JS (プレーン JavaScript)、React、Preact、Polymer、Ember.js、Vue.js のそれぞれを使用した実装です。アプリがオフラインでも機能するように、Service Worker と PouchDB を使用して、ショッピング・リスト・データをローカルにキャッシュします。オンライン時は、PouchDB が Cloudant NoSQL DB または Apache CouchDB と同期するため、デバイス間でショッピング・リストを共有できます。

いずれか任意のテクノロジー・スタックを使用してこの開発者向けパターンを完了すると、以下の方法がわかるようになります。

* オフラインのときはローカル・データを使用してブラウザー内で稼働し、オンラインのときはリモート・データベースと同期するアプリを実装する
* オフライン・ファースト・プログレッシブ Web アプリを作成する

## フロー

![フロー](../../images/shopping-list-arch2.png)

1. ユーザーがオフライン・ファースト・プログレッシブ Web アプリを使用してショッピング・リストを管理します。
1. Vanilla JS (プレーン JavaScript)、React、Preact、Polymer、Ember.js、または Vue.js を使用してプログレッシブ Web アプリを作成し、Service Worker を利用してオフラインでもアプリが機能するようにします。
1. オフライン時は、ショッピング・リストがローカルで PouchDB 内に保管されます。
1. オンライン時は、PouchDB データベースが IBM Cloudant データベースと同期します。
