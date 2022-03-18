---
abstract: 最近、ブロックチェーンが話題になっています。この技術を利用して、どのような業界が利益を得ることができるのかを見てみましょう。
authors: ''
completed_date: '2016-05-09'
draft: false
excerpt: 最近、ブロックチェーンが話題になっています。この技術を利用して、どのような業界が利益を得ることができるのかを見てみましょう。
last_updated: '2017-08-21'
meta_description: 最近、ブロックチェーンが話題になっています。この技術を利用して、どのような業界が利益を得ることができるのかを見てみましょう。
meta_keywords: blockchain, what is blockchain, blockchain technology
meta_title: ブロックチェーンの基礎知識。用語解説とユースケース
primary_tag: blockchain
pta:
- None
pwg:
- None
related_content:
- slug: cl-ibm-blockchain-101-quick-start-guide-for-developers-bluemix-trs
  type: tutorials
- slug: build-a-blockchain-network
  type: patterns
- slug: ibm-blockchain-platform-vscode-smart-contract
  type: tutorials
related_links:
- title: More blockchain resources on IBM Developer
  url: /technologies/blockchain/
- title: 'Blockchain basics: Introduction to distributed ledgers'
  url: /tutorials/cl-blockchain-basics-intro-bluemix-trs/
- title: 'IBM Blockchain 101: Quick-start guide for developers'
  url: /tutorials/cl-ibm-blockchain-101-quick-start-guide-for-developers-bluemix-trs/
- title: IBM Blockchain Pulse blog
  url: https://www.ibm.com/blogs/blockchain/
- title: Hyperledger Fabric application samples
  url: https://github.com/hyperledger/fabric-samples
subtitle: ブロックチェーンの主要用語と無限の可能性を秘めたアプリケーション
tags:
- blockchain
title: ブロックチェーンの基礎知識。用語解説とユースケース
type: tutorial
---

控えめに言っても、ブロックチェーンは最近の人気トピックです。この新しいテクノロジーを利用して、企業がどのように利益を得ることができるのかを見てみましょう。

## 1 ブロックとブロックチェーンネットワーク

ブロックチェーンとは、ビジネスネットワーク上で共有される分散型台帳の一種です。ビジネス上の取引は、連続した、追記のみの、改ざん不可能な_**ブロック**_として、台帳に永久に記録されます。確認されたすべての取引ブロックは、生成ブロックから最新のブロックまでハッシュリンクされているため、_**blockchain**_と呼ばれています。

 <sidebar> <heading>すべてのブロックチェーンは同じように作られているわけではない</heading> <p><a href="https://www.ibm.com/blogs/blockchain/2017/05/the-difference-between-public-and-private-blockchain/">パブリックブロックチェーンとプライベートブロックチェーン</a>の違いがわかりますか？<a href="https://www.ibm.com/blogs/blockchain/2017/05/the-difference-between-bitcoin-and-blockchain-for-business/">ビットコイン vs. ビジネス向けブロックチェーン</a>の間? </p></sidebar>

ブロックチェーンとは、このように、ネットワーク内のブロックチェーンの開始以降に行われたすべての取引の歴史的記録です。ブロックチェーンは、ネットワークの単一の真実の情報源として機能します。

ブロックチェーンネットワークには、パーミッションドレスとパーミッションドレスがあります。_**Permissionless**_ネットワークは、あらゆる参加者に開かれており、取引はネットワークの既存のルールに照らして検証されます。参加者が匿名であっても、台帳上の取引を見ることができます。パーミッションレスでパブリックなブロックチェーンネットワークの例としては、ビットコインがよく知られています。

一方、_**Permissioned**_ネットワークは、通常はプライベートで、特定のビジネスネットワーク内の参加者に限定されます。パーミッションド・ブロックチェーンでは、参加者は自分に関連する取引のみを閲覧することができます。[Hyperledger](https://www.hyperledger.org/)は、ビジネス向けのパーミッションド・ブロックチェーンの開発を支援するために、Linux Foundationが主催する共同作業です。

## 2 分散型台帳

分散型台帳とは、ネットワークのメンバー間で共有、複製、同期されるデータベース、または記録システムの一種である。分散型台帳は、ネットワークの参加者の間で行われた資産やデータの交換などの取引を記録する。この共有された台帳により、異なる台帳を調整するための時間と費用が不要になる。

 <sidebar> <heading>分散型台帳のメリット</heading> <p>この<a href="/tutorials/cl-blockchain-basics-intro-blueemix-trs/">分散型台帳入門</a>で、レガシー台帳の問題点と解決策を探ります。</p></sidebar>

ネットワークの参加者は、台帳のレコードの更新を管理し、合意によって同意します。銀行や政府のような中央、第三者の仲介者は関与しません。分散型台帳のすべての記録には、タイムスタンプと固有の暗号署名があるため、台帳はネットワーク内のすべての取引の監査可能な履歴となります。

分散型台帳技術の実装としては、The Linux Foundationが主催するオープンソースの[Hyperledger Fabric](https://www.hyperledger.org/projects/fabric)ブロックチェーンがあります。

## 3 参加者

ビジネスのためのブロックチェーンネットワークは、識別可能で検証可能な**_参加者**のグループによって運営される、共同で所有されるピアツーピアネットワークです。参加者は個人でも、企業、大学、病院などの機関でもよい。

## 4 資産、取引、およびチャネル

価値を生み出すために所有または管理できるものはすべて、_**asset**_です。資産には、有形のもの（車や農場の新鮮な桃など）と無形のもの（抵当権や特許など）があります。**トランザクション**_とは、台帳への資産の移転、または台帳からの資産の移転のことです。Hyperledger Fabricのブロックチェーンでは、資産はキーと値のペアの集まり（例えば、vehicleOwner=Daisy）として、バイナリ形式またはJSON形式、あるいはその両方で表現されます。

Hyperledger Fabricブロックチェーンにおいて、**_channel_**とは、2人以上の特定のネットワークメンバーの間で、プライベートで機密性の高い取引を行うことを目的とした、プライベートな「サブネット」のコミュニケーションです。2人の参加者がチャンネルを形成した場合、その参加者は、そのチャンネルで取引を行い、そのチャンネルの元帳のコピーを共有するために、認証され、承認されなければなりません（他の参加者は不可）。チャネルのおかげで、プライベートで機密性の高い取引を必要とするネットワークメンバーは、ビジネス上の競争相手や他の制限されたメンバーと同じブロックチェーンネットワーク上で共存することができます。

## 5 コンセンサス

 <sidebar> <heading>Pluggable consensus</heading> <p> <a href="https://www.hyperledger.org/projects/fabric">Hyperledger Fabric</a>は、ブロックチェーンフレームワークの実装で、The Linux Foundationが主催するHyperledgerプロジェクトの1つです。<a href="https://www.hyperledger.org/projects/fabric">Hyperledger Fabric</a>では、コンセンサスやメンバーシップサービスなどのコンポーネントをプラグアンドプレイで利用することができます。 </p></sidebar>

_**コンセンサス**_とは、ブロックチェーン・ビジネス・ネットワークのメンバーが、トランザクションが有効であることに同意し、元帳を一貫して同期させるために使用する協調プロセスのことです。コンセンサス・メカニズムは、台帳に追加された取引を改ざんするには、多くの場所で同時に発生しなければならないため、不正取引のリスクを低減します。

コンセンサスを得るためには、参加者が取引に同意し、それを検証してから台帳に永久に記録される。参加者は、取引を検証するためのルールを確立することもできます。システム管理者でさえも、台帳に追加された取引を削除することはできません。参加者の信頼できるネットワークは、パーミッションレス・ブロックチェーンの高いコストに比べて、コンセンサスを確立するためのコストを削減します。

ビジネスブロックチェーンでは、多様な合意形成メカニズムを選択することができます。信頼度が高い場合、単純な多数決で十分な場合もあれば、ネットワークがより洗練された方法を選択する場合もあります。

## 6 スマートコントラクトとチェーンコード

****スマートコントラクトは、台帳とのやりとりを管理し、ネットワーク参加者が取引のある部分を自動的に実行することを可能にします。例えば、スマートコントラクトでは、到着時期によって変化する商品の発送費用を規定することができます。両者が合意した条件を元帳に書き込むと、商品を受け取ったときに適切な資金が自動的にやり取りされます。

Hyperledger Fabricでは、スマートコントラクトはチェーンコードに書き込まれており、両者は実質的に同義語と考えられています。

 <sidebar> <heading>A simple chaincode sample</heading> <p>元帳にアセットを作成する方法を示す<a href="https://hyperledger-fabric.readthedocs.io/en/latest/chaincode4ade.html">chaincode sample</a>を見てみましょう。</p></sidebar>

Hyperledger Fabricにおいて、**_chaincode_**とは、ネットワーク資産と、その資産を変更するためのトランザクション命令（ビジネスロジック）を定義する、Goで書かれたコードのことです。チェーンコードは、適切な権限を持つメンバーによってチャンネルにインストールされ、インスタンス化されます。そのチャンネルでトランザクションが実行されると、Chaincodeの関数が元帳に値を読み書きします。

## 7 ブロックチェーンアプリケーション

ブロックチェーンアプリケーションには、ユーザー向けアプリケーション、スマートコントラクト、台帳という相互に依存する3つのコンポーネントが必要です。

一番上の層は、ネットワーク参加者のニーズを満たす_**ユーザー向けアプリケーション**_です。このアプリケーションでは、ユーザーがスマートコントラクトを起動し、ビジネスネットワーク内の取引を引き起こすことができます。**スマートコントラクト**_は、ネットワークのビジネスロジック（資産、所有権、譲渡）をカプセル化します。スマートコントラクトを起動するたびに、ネットワーク上でトランザクションが発生し、元帳が更新されます。**台帳**_は、スマートコントラクトのデータ（例えば、vehicleOwner=Daisy）の現在の値を保持し、ネットワーク全体に分散されています。

## ブロックチェーンのユースケース

ブロックチェーン技術は、摩擦が少なく効率的な活動を組織化するため、多くの産業にとって強力なゲームチェンジャーとなります。ブロックチェーン技術は、多くの産業に強力な変革をもたらします。ブロックチェーンは、金融、医療、政府などのさまざまな分野で、すでに産業の再構築に貢献しています。ここでは、その無限の可能性の一部をご紹介します。

* [**モノのインターネット**](https://www.ibm.com/internet-of-things/trending/blockchain)
  貨物輸送。貨物輸送： 複数の輸送会社を利用して貨物を輸送し、透明性とタイムリーな配送を確保する。
  部品の追跡とコンプライアンス。フリートメンテナンスのための純正部品および交換部品の実績記録の保存
  運用保守データの記録。ビジネスパートナーとの共有や法規制に対応するために、運転記録やメンテナンス記録を保存する。
* [**アイデンティティ管理**](https://www.ibm.com/blockchain/solutions/identity)
  信頼できるデジタルアイデンティティの構築
* [**サプライチェーン**](https://www.ibm.com/blockchain/industries/supply-chain)
  食品安全ネットワークにおけるトレーサビリティー、透明性、効率性の向上
* [**金融サービス**](https://www.ibm.com/blockchain/industries/financial-services)
  お客様を知る。信頼できる顧客の最新情報へのアクセスにより、金融機関の顧客サービスの精度が向上する
  Clearing and settlement:金融機関間のリアルタイムなポイント・ツー・ポイントの資金移動により、決済が迅速化される
  その他の例信用状、社債、トレーディングプラットフォーム、送金、レポ取引、外国為替など。
* ヘルスケア
  電子カルテ
  ウイルスバンク
  医師とベンダーのRFPサービスと保証契約
  ブロックチェーンヘルスリサーチコモンズ
  ブロックチェーン・ヘルス公証人
* 保険
  クレーム処理
  P2P保険
  オーナーズタイトル
  販売・引受
* 政府
  政府の入札プロセス
  議決権行使
  税制
* ゲーム
* 音楽

などなど、枚挙にいとまがありません。この他にも、ブロックチェーン技術の恩恵を受けている多くの[**産業**](https://www.ibm.com/blockchain/industries/)や[**使用例**](https://www.ibm.com/blockchain/use-cases/)をご覧ください。

## 結論

ブロックチェーンの主要な用語を理解することで、この劇的に破壊的な技術がどのように機能するのか、また多くの産業でどのように生産的な利用が可能なのかを理解することができるでしょう。

## 次のステップ

[**IBM Developer**の**Blockchain Hub**](/technologies/blockchain/)に立ち寄ってください。ここでは、ビジネス向けのブロックチェーン・ソリューションを開発・展開するための、コードやコミュニティ・サポートとともに、無料のツールやチュートリアルを提供しています。

Happy blockchaining!