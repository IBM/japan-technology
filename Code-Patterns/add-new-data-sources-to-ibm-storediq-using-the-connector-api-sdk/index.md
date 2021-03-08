---
#Front matter (metadata).
authors:                # REQUIRED - Note: can be one or more
  - name: Shikha Maheshwari
    email: shika.mah@in.ibm.com
  - name: Balaji Kadambi
    email: bkadambi@in.ibm.com
  - name: Manjula Hosurmath
    email: mhosurma@in.ibm.com

completed_date: "2018-08-07"

components:
  - "storediq"

draft: false

excerpt: IBM StoredIQ で Connector API SDK を使用して、新しいデータ・ソースのカスタム・コネクターを作成する。
meta_description: IBM StoredIQ で Connector API SDK を使用して、新しいデータ・ソースのカスタム・コネクターを作成する。
github:
  - url: https://github.com/IBM/connector-for-storediq/
    button_title: "コードを入手する"

meta_keywords: "storedIQ, artificial intelligence"
meta_title: "データ・ソースを IBM StoredIQ に追加する"

last_updated: "2018-08-07"

subtitle: "IBM StoredIQ で Connector API SDK を使用して、新しいデータ・ソースのカスタム・コネクターを作成する"

title: "Connector API SDK を使用して新しいデータ・ソースを IBM StoredIQ に追加する"

type: default

primary_tag: "artificial-intelligence"

pta:
  - "system integrators"

pwg:
  - "none"

related_links:           # OPTIONAL - Note: zero or more related links
  - title: IBM StoredIQ Platform の概要
    url: https://www.ibm.com/support/knowledgecenter/en/SSEHPS_7.6.0/overview/overview.html
    description: IBM StoredIQ Platform の概要をご覧ください。

  - title: IBM StoredIQ データ・ソースおよびボリュームに関する Redbook
    url: https://www.redbooks.ibm.com/redpapers/pdfs/redp5316.pdf
    description: IBM StoredIQ データ・ソースおよびボリュームの詳細を調べてください。

  - title: IBM StoredIQ Connector API SDK
    url: https://github.com/IBM/connector-for-storediq/blob/master/doc/IBM_StoredIQ_Connector_API_SDK.pdf
    description: IBM StoredIQ Connector API SDK のリファレンス・ガイドをご覧ください。

tags:
- "python"
---

## 概要

IBM StoredIQ では、組織が非構造化データを理解および制御して、ビジネスに不可欠な情報に、その情報を必要とする担当者を迅速につなげられるようになっています。IBM StoredIQ を使用すると、組織は動的なデータを識別、分析、処理して、e-ディスカバリー、情報ガバナンス、データ管理、記録管理の要件を満たすことができます。IBM StoredIQ は、e-メール・サーバー、ファイル共有、Box をはじめ、多種多様なデータ・ソースに接続します。そのためのコネクターは、データ・ソースと StoredIQ との間の接続を確立するソフトウェア・コンポーネントです。IBM StoredIQ 開発環境の外部にあるデータ・ソースであっても、IBM StoredIQ Connector API SDK を使用すれば、新しいデータ・ソースのコネクターを作成することができます。その方法を説明しているのが、このパターンです。

## 説明

IBM StoredIQ プラットフォームは強力かつ極めてスケーラブルな非構造化データ管理プラットフォームとして、組織がインプレースでデータを理解して分析し、関連するデータ・セットを識別してアクションを取るために役立ちます。IBM StoredIQ では、Box、Microsoft Office 365、FileNet をはじめ、85 を超えるデータ・ソースをサポートしています。

データ・ソースは IBM StoredIQ ソリューションの重要な部分です。その重要なデータ・ソースへの接続には、IBM StoredIQ のソフトウェア・コンポーネントがコネクターとして使用されます。IBM StoredIQ に用意されている Connector API SDK を使用してカスタム・コネクターを作成すれば、StoredIQ でサポートしていない新しいデータ・ソースにも接続できます。IBM StoredIQ Connector API SDK では、コネクターのロジックを StoredIQ アプリケーションのロジックから切り離すことによって、コネクターを簡単に開発できるようになっていいます。また、この SDK は既存のコネクターをカスタマイズしたり拡張したりするためにも使用できます。新しいコネクターを作成した後は、そのコネクターを使用して、サポートされているデータ・ソースと同じように IBM StoredIQ 内で新しいデータ・ソースのデータを管理できます。

このコード・パターンを参考に、コネクターの手法および新しいデータ・ソースのコネクターを作成する方法を理解してください。このコード・パターンをひととおり完了すると、以下の方法がわかるようになります。

* IBM StoredIQ のコネクターを開発する
* 稼働中の IBM StoredIQ にコネクターを統合する
* 稼働中の IBM StoredIQ にコネクターを登録する
* コネクターをテストする

## フロー

![フロー](../../images/flow-storediq-1.png)

1. Connector SDK を使用して、データ・ソースのコネクターを開発します。
1. コネクターを、StoredIQ データ・サーバーおよびゲートウェイ・サーバーに統合して登録します。
1. StoredIQ の管理者ダッシュボードを使用して、新しいコネクター用のボリュームを追加し、そのボリュームからデータを収集して情報セットを作成します。
1. Data Workbench ダッシュボードで、データ・ソースの内容を表示します。

## 手順

詳細な手順については、[README](https://github.com/IBM/connector-for-storediq/blob/master/README.md) を参照してください。
