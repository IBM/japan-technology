---
abstract: ブロックチェーン革命に参加しよう!このクイックスタートガイドは、ブロックチェーン技術を探求している開発者のためのもので、ブロックチェーンのプリプロダクションネットワークを素早く立ち上げ、サンプルアプリケーションを展開し、クライアントアプリケーションを開発・展開したいと考えています。最新のHyperledger
  Fabricフレームワークをベースにしたブロックチェーンネットワークの起動、Chaincode（ネットワークのビジネスロジック）の記述とインストール、ビジネスプロセスやデジタルインタラクションを合理化するためのクライアントアプリケーションの開発方法をシンプルな手順で紹介しています。
authors: ''
completed_date: '2019-05-30'
components:
- hyperledger-fabric
- hyperledger
display_in_listing: true
draft: false
excerpt: IBMの次世代ブロックチェーン・プラットフォームを使って、キックスターター・ブロックチェーン・ネットワークを構築し、コーディングを始めましょう。
last_updated: '2021-05-13'
meta_description: このクイックスタートガイドは、ブロックチェーン技術を探求しているアプリケーション開発者向けのもので、ブロックチェーンのプリプロダクションネットワークを素早く立ち上げ、サンプルアプリケーションを展開し、クライアントアプリケーションを開発・展開したいと考えている方におすすめです。
meta_keywords: blockchain, blockchain explained, what is blockchain
meta_title: ブロックチェーン101。開発者向けクイックスタート・ガイド - IBM
primary_tag: blockchain
private_portals:
- blockchain
pta:
- emerging technology and industry
pwg:
- blockchain
related_content:
- slug: blockchain-learning-path
  type: series
- slug: cl-blockchain-basics-intro-bluemix-trs
  type: tutorials
- slug: ibm-blockchain-platform-vscode-smart-contract
  type: tutorials
related_links:
- title: Build your blockchain skills with the IBM Developer Blockchain learning path
  url: /series/blockchain-learning-path/
- title: IBM Blockchain Platform Console Video Series
  url: /series/ibm-blockchain-platform-console-video-series/
- title: IBM Blockchain Platform overview
  url: https://www.ibm.com/blockchain/platform
- title: IBM Cloud Kubernetes Service
  url: https://cloud.ibm.com/kubernetes/catalog/cluster?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg
- title: IBM Developer Blockchain code patterns
  url: https://developer.ibm.com/patterns/category/blockchain/
services:
- blockchain
subtitle: IBMの次世代ブロックチェーン・プラットフォームでキックスターター・ブロックチェーン・ネットワークを構築し、コーディングを開始する
tags:
- cloud
time_to_read: 1 hour
title: IBM Blockchain 101:開発者向けクイック・スタート・ガイド
type: tutorial
---

ブロックチェーンの革命は続く!ビジネス利用のための分散型台帳技術を検討しており、デモやパイロット、本番前のステージングのためにビジネス・ブロックチェーンを構築したいと考えている方に、このガイドをお勧めします。次世代のIBM Blockchain Platformを含む、<a href="#start"><strong>今すぐ始める</strong>ためのいくつかの方法をご紹介します。

 <button-link> <text>Kick-start your blockchain journey now</text> <url>https://www.ibm.com/blockchain/getting-started</url></button-link>

このガイドでは、次世代プラットフォームを使って、最新のオープンソースHyperledger Fabricフレームワークをベースにしたブロックチェーンネットワークをスピンアップする方法や、手動でコンポーネントごとに構築する方法を紹介します。しかし、まずはビジネスブロックチェーンネットワークの開発にまつわる主要なコンセプトを確認しましょう。

## ビジネスブロックチェーンの概念

### ビジネス・ブロックチェーン・ネットワークとは？

**ビジネス・ブロックチェーン・ネットワーク**は、分散型台帳技術（DLT）を利用して、ネットワークに参加しているメンバー組織間でビジネス資産を効率的かつ安全に移転するための分散型ネットワークです。資産には、自動車、ダイヤモンド、生鮮食品、保険記録など、物理的なものとデジタルなものがあります。共有される**_分散型台帳**には、ネットワークの参加者間で行われたすべての資産取引の不変的な履歴が記録され、それらの資産の現在の状態（ワールドステート）がカタログ化される。取引を管理するビジネスルールは、メンバーによって合意され、**スマートコントラクト**にカプセル化される。

ブロックチェーンネットワークのメンバーは、銀行や証券会社などの中央機関や信頼できる仲介者に依存して取引を検証するのではなく、**_consensus_**メカニズムを使用して、ネットワーク全体の取引処理速度、透明性、説明責任を向上させています。さらに機密性を高めるために、メンバーはデータの分離を可能にする1つまたは複数の**_チャネル**に参加し、チャネル固有の台帳はそのチャネル内の認証されたピアによって共有されます。

ビジネス向けのブロックチェーンネットワークは、企業、大学、病院など、識別可能で検証可能な機関のグループが共同で所有し、運営しています。このような**_許可されたネットワーク**では、参加者は互いに知られており、取引はビットコインネットワークのような許可されていない公共のネットワークよりもはるかに速く処理されます。ビットコインでは、参加者が匿名であるため、「プルーフ・オブ・ワーク」などのコンセンサス・メカニズムに頼らざるを得ず、身元確認や取引の検証に時間のかかる計算が必要となる。

さらに詳しい説明が必要ですか？

* [Introduction to distributed ledgers](/tutorials/cl-blockchain-basics-intro-blueemix-trs/)をご覧ください。
* IBM Blockchain Platform上でビジネス・ネットワークをセットアップする方法を紹介した4部作の[IBM Blockchain Platform Console Video Series](/series/ibm-blockchain-platform-console-video-series/)をご覧ください。

### ビジネス・ブロックチェーンのオープンソース・エンジンであるハイパーレッジャー・ファブリック

現代のビジネス需要に対応するため、IBMは他社と共同で、The Linux Foundation&reg;が主催するHyperledger&reg;プロジェクトの1つである**_Hyperledger Fabric_**&trade;と呼ばれる、オープンソースで本番に対応したビジネスブロックチェーンフレームワークを開発しました。Hyperledger Fabricは、幅広い産業分野において、許可されたネットワーク上での分散型台帳ソリューションをサポートします。そのモジュラー・アーキテクチャは、ブロックチェーン・ソリューションの機密性、耐障害性、柔軟性を最大限に高めます。Hyperledger Fabric v1.0には、27の組織から159人のエンジニアが参加しました。これは、最初の生産可能なビジネスブロックチェーンフレームワークを意味しました。2019年1月、Hyperledger Fabricはv1.4で最初のLong Term Supported（LTS）プロジェクトのリリースを発表しました。その後のLTSリリースでは、[公式サイト](https://github.com/hyperledger/fabric#releases)から最新情報を確認することができます。Hyperledger Fabricの4回目の誕生日である2020年1月には、V2が一般利用可能となり、いくつかの驚異的な新機能が導入されました。

もっと深く潜ってください。

* [Hyperledger Fabricプロジェクト概要](https://www.hyperledger.org/projects/fabric)
* [ブロックチェーンネットワークにおけるHyperledger Fabricの技術的利点トップ6](https://developer.ibm.com/articles/top-technical-advantages-of-hyperledger-fabric-for-blockchain-networks/)

### IBMのエンタープライズ対応プラットフォーム。IBMブロックチェーン・プラットフォーム

[IBM Blockchain Platform](https://www.ibm.com/blockchain/platform/)は、IBM Cloud上でのSoftware-as-a-Service提供と、Kuberenetes cluster v1.17以上に展開するソフトウェア経由の2つの方法で提供されるブロックチェーンです。  IBM Blockchain Platformは、分散型、複数機関、マルチクラウドのビジネスネットワークの開発、ガバナンス、運用を簡素化するために設計された、唯一の完全に統合されたエンタープライズ対応のブロックチェーン・プラットフォームです。IBMブロックチェーン・プラットフォームは、Hyperledger Fabricフレームワークのオープンソース・テクノロジーを活用することで、この分散化された世界におけるコラボレーションを加速します。

IBM Blockchain Platformは、ネットワークのメンバーが開発を開始することを迅速かつ容易にし、最も要求の厳しいユースケースや規制された業界にも対応できるパフォーマンス、プライバシー、セキュリティーを備えたコラボレーション環境に素早く移行することができます。

#### 小さく始めて大きくする

IBM Blockchain Platformでは、必要なものだけをデプロイし、環境を動的に追加することができます。個々のノードのリソース（CPU/メモリ/ストレージ）を変更したり、ノード自体を追加したりすることができます。概念実証から試験運用、本番運用まで、安全かつ高性能で拡張性に優れたネットワーク上で移行することができます。最新のオプションでは、独自のインフラを持ち込み、どこにでも展開できる柔軟性を備えています。つまり、オンプレミスでも他のホスティングプロバイダーでも、ブロックチェーンのノードやメンバーを接続して取引を行うことができます。これらすべてを、IBM Blockchain Platformが提供するのと同じルック＆フィールと使いやすいツールで実現します。このプラットフォームは、プリプロダクション・アプリケーションの開発とテストから、成長するプロダクション・エコシステムまで、簡単で経済的なオンランプとなるように設計されています。

IBM ブロックチェーン・プラットフォームをご覧ください。

* [IBM Blockchain Platform overview](https://www.ibm.com/blockchain/platform)
* [Develop, govern, and operate your business network with the IBM Blockchain Platform](/tutorials/cl-ibm-blockchain-platform-develop-govern-operate-your-business-network/)

## IBMブロックチェーン・プラットフォームの中身 {:#sp}になります。

開発者がブロックチェーン開発を始めるための最も簡単で経済的な方法は、[IBM Blockchain Platform on Red Hat Marketplace](https://marketplace.redhat.com/en-us/products/ibm-blockchain)です。この開発・テスト環境は、ブロックチェーン技術を模索しているネットワーク事業者や開発者、あるいはデモやパイロット、概念実証のためにブロックチェーンネットワークを構築したいと考えている人に最適です。

企業、スタートアップ、学術、初心者、経験者を問わず、どんな開発者でも、IBM Blockchain Platformを使って、フル機能の複数組織のブロックチェーンネットワークにコードを展開することができます。

IBM ブロックチェーン・プラットフォームを使用すると、次のことが可能になります。

**構築**を行うことができます。

* [任意のクラウドまたは独自のプライベート・クラウドにデプロイする機能](https://www.ibm.com/blogs/blockchain/2019/02/taking-the-next-step-towards-deploying-blockchain-anywhere/)
* [VS Code IDEプラグインとコードサンプル](/tutorials/ibm-blockchain-platform-vscode-smart-contract/)により、スマートコントラクトの開発が容易になります。
* シングルノードでの展開により、より詳細なコントロールが可能
* インフラストラクチャの管理と秘密鍵への単独アクセス
* 開発からテストまでを1つのインスタンスで行うことで、市場投入までの時間を短縮できます。

**運用と管理**。

* 単一のインスタンスで無制限のユースケース、チャネル、構成が可能なため、柔軟なネットワーク構成が可能です。
* 識別子、台帳、スマートコントラクトにより、コントロールとオーナーシップが向上します。
* 現在のHyperledger Fabricの機能は、より最新の技術の利点を提供します。

**成長**している

* 1つのピアを複数のオーダーサービスに接続することで、柔軟なネットワーク構成を実現
* IBM Kubernetes Serviceを利用したインフラにより、コントロールとオーナーシップが向上します。
* 柔軟な価格設定により、初期投資なしで、小規模から始めて、使用した分だけ支払うことができます。

## Start now!Red Hat MarketplaceのIBM Blockchain Platformを使って、ブロックチェーンネットワークをキックスタートさせましょう {:#start}となります。

実際のビジネス・ブロックチェーンの使い方を学び、ブロックチェーンのスキルとアプリケーションの開発を今すぐ始めるための最も簡単で経済的な方法は、IBM Blockchain Platform on Red Hat Marketplaceにサインアップすることです。

### サンプルビジネスネットワークを展開する

ステップ・バイ・ステップで、サンプル・ネットワークを IKS Free Tier にデプロイする方法を学びます。そうすれば、シミュレーションされた複数組織のネットワーク上で、ブロックチェーン・アプリケーションの開発、デモ、ステージングを開始することができます。

1. Red Hatアカウントを使用して、[無料トライアル](https://marketplace.redhat.com/en-us/products/ibm-blockchain)にサインアップします。
1. 起動ボタンが表示されたら、ブロックチェーンコンソールに入り、クイックスタートチュートリアルと、デプロイ可能なさまざまなノードが表示されます。
1. クイックスタートを選択すると、"Build a network"、"Join a network"、"Deploy a smart contract on the network "といった一連の簡単なステップが案内されます。

完全な詳細については、IBM Blockchain Platformのドキュメントを参照してください。ここでは、案内される内容のプレビューを紹介します。

* **Deploy** 認証局、注文サービスノード、またはピアを展開します。
* **アイデンティティとチャネルを作成する**。
* アセットクラス、参加者クラス、トランザクションクラス、イベントクラス、アクセスコントロールルールを定義して、ビジネスネットワークをモデル化する。
* ****スマートコントラクトを書く**、スマートコントラクトをインストールする**、スマートコントラクトをインスタンス化する**、クライアントアプリケーションを使用してトランザクションを送信する**。

## What's *not* in the free tier?

Free Tierは、運用ツールの概要を確認したり、迅速な開発やテストを行うために最適化されています。スタンダードプランとはいくつかの点で異なります。

* 1ヶ月後に自動的に削除され、スタンダードプランに移行することはできません。したがって、1ヶ月を超えてデータが残っていると、インスタンス全体が消滅してしまいますのでご注意ください。
* ストレステストには使用しないでください。これは無料のリソースであり、IBMがすべてのコストを負担しているため、無料で利用できるようにするためには、IBMはこれらのインスタンスに割り当てられるリソースを制限する必要があります。
* これらのデプロイメントにはメンテナンスは適用されません。Hyperledger Fabricの新しいバージョンが利用可能になった場合、IBMはFree Tierインスタンスをこの新しいレベルにアップグレードしませんので、IBM Blockchain Platformインスタンスを削除して新たに再起動する必要があります。

## フリーティアの先にあるものは？

本格的に活動を開始し、ネットワークを成長させ、ネットワーク定義、スマート・コントラクト、アプリケーションを、強化されたセキュリティとプレミアム・サポートのレイヤーを追加した本番環境にデプロイする準備ができたら、[IBM Cloud](https://cloud.ibm.com/catalog/services/blockchain-platform?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)を利用することになります。

スタンダードプランでは、IBM Blockchain Platformのノードを増やしたり、リソース（コンピュートとストレージ）を増やしたりすることができるほか、安全なクラウドであるKubernetesベースのポータブル環境で動作する、クラッシュ耐性のある本番レベルのインフラストラクチャを利用することができます。これには、ランタイム/データの分離、発注サービスと認証局の高可用性、ディザスタリカバリのための複数ゾーンの使用機能が含まれます。

## オープンソースの技術を自分のコンピュータで直接使えばいいんじゃない？

Hyperledger Fabricフレームワークに基づいてローカルに展開されたブロックチェーンは、素晴らしいシミュレーションになります。しかし、他のメンバー組織にアクセスできなければ、複数組織のネットワークのスケーラビリティやパワーを体験したり、テストしたりすることはできません。また、オープンソース技術をローカルで使用するには、コマンドラインでのコーディングにもう少し忍耐力と器用さが必要です。

逆に、IBM Blockchain Platformでは、スケーラブルで信頼性が高く、完全に統合された運用・ガバナンスツールのセットを手に入れることができ、ネットワークの作成、デプロイメント、モニタリング、ガバナンスを簡単なクリックと簡単な指示で行うことができます。開発したコードやスキルは本番環境に簡単に移行できるため、本番で本格的なネットワークに移行する際にも、まったく同じ経験をすることができます。

さらに、私たちが提供するIBM Blockchain Platformのツールとともに、献身的にオープンソース・コード・ベースに貢献し続けているエキスパートに直接アクセスすることができます。

## スマートコントラクトの迅速な開発および/またはテストをお探しですか？

Hyperledger Fabric用のスマートコントラクトの開発について詳しく知るための最も簡単で経済的な方法は、無料の[IBM Blockchain Platform VS Code extension](https://marketplace.visualstudio.com/items?itemName=IBMBlockchain.ibm-blockchain-platform)を入手することです。コマーシャル・ペーパーやFabCarなど、開始するのに役立つサンプルがいくつか組み込まれています。エクステンションをインストールしたら、[このチュートリアル](/tutorials/ibm-blockchain-platform-vscode-smart-contract/)を見ながら、最初のスマートコントラクトを作成することができます。

VS Codeエクステンションでは、複数のワークスペースを簡単に管理しながら、スマートコントラクトの開発、パッケージ化、デプロイを素早く行うことができます。さらに、このエクステンションには、ローカルのHyperledger Fabricのインストールが組み込まれており、スマートコントラクトを素早くテストすることができます。さらに、リモートネットワークに簡単に接続できるため、パッケージ化したスマートコントラクトを、参加しているあらゆるネットワークに展開することができます。

## ヘルプとサポートを受ける

サポートや質問への回答を得る方法はたくさんあります。

1. 一般的なブロックチェーンに関する質問の場合。<br/> [IBM Community](https://community.ibm.com/community/user/ibmz-and-linuxone/groups/topic-home/discussions?communitykey=d92f829f-9174-4aa9-9ee3-54da65afaf87&tab=discussions)を検索します。すでに質問されたものを閲覧するか、新しい質問を投稿してください（キーワード **blockchain** を含む）。<br/> <br/>
2.IBM Blockchain Platformのヘルプについて。<br/> UIの**Support**セクションでは、リリースノートだけでなく、セルフヘルプのための多くのリソースを提供しています。ソフトウェアの不具合や、与えられたリソースでは解決できない問題については、IBM Cloud Service Portalでサポートケースを提出する手順が記載されています。サポートケースを提出すると、数分以内にメールで回答が得られます。<br/> <br/>
3.Hyperledger Fabric の実装に関する具体的な質問について。<br/> [Hyperledger Rocket.Chat channels](https://chat.hyperledger.org/home) と [Stack Overflow](https://stackoverflow.com/questions/tagged/hyperledger-fabric) があなたのベストベッツです。<br/> <br/>

## 次のステップ

最後に、ブロックチェーンのスキルを身につけるための素晴らしい方法をご紹介します。

* ブロックチェーン学習の旅で次のステップを踏む -- [IBM Developer Blockchain learning path](/series/blockchain-learning-path/)に沿って進んでください。
<br/>
* IBM Developerの[Blockchain content hub](/technologies/blockchain/)に立ち寄ってください。これは、ビジネスのためのブロックチェーン・ソリューションを開発して展開するためのツールやチュートリアル、コードやコミュニティのサポートを提供します。<br/> <br/>
* IBM Blockchain Platformでビジネス・ネットワークをセットアップする方法を詳しく紹介している、4部構成の[IBM Blockchain Platform Console Video Series](/series/ibm-blockchain-platform-console-video-series/)をご覧ください。<br/> <br/>
* 複雑な問題を解決するためのロードマップを提供し、概要、アーキテクチャー図、プロセス・フロー、レポ・ポインター、追加の読み物を含む、IBM Developerの多くの[blockchain code patterns](/patterns/category/blockchain/)をチェックしてください。