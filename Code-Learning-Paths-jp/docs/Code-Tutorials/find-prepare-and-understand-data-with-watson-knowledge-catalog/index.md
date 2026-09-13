---
abstract: このチュートリアルでは、IBM Cloud Pak for Data プラットフォーム上の Watson Knowledge Catalog を使用して、エンタープライズ・データ・ガバナンスの問題を解決する方法を示します。機密データの保護と管理、データの系統の追跡、データ・レイクの管理を支援するために、ガバナンス、データ品質、アクティブ・ポリシー管理を使用する方法を説明します。この知識は、データ資産、データセット、分析モデル、およびそれらの関係を組織内の他の人々と迅速に発見し、キュレーションし、分類し、共有するのに役立ちます。
also_found_in:
- /learningpaths/cloud-pak-for-data-learning-path/
authors: ''
completed_date: '2020-02-25'
components:
- cloud-pak-for-data
draft: false
excerpt: このチュートリアルでは、IBM Cloud Pak for Data プラットフォーム上の Watson Knowledge Catalog を使用して、エンタープライズ・データ・ガバナンスの問題を解決する方法を示します。機密データの保護と管理、データの系統の追跡、データ・レイクの管理を支援するために、ガバナンス、データ品質、アクティブ・ポリシー管理を使用する方法を説明します。この知識は、データ資産、データセット、分析モデル、およびそれらの関係を組織内の他の人々と迅速に発見し、キュレーションし、分類し、共有するのに役立ちます。
ignore_prod: false
last_updated: '2021-07-16'
meta_description: このチュートリアルでは、IBM Cloud Pak for Data プラットフォーム上の Watson Knowledge Catalog
  を使用して、エンタープライズ・データ・ガバナンスの問題を解決する方法を示します。機密データの保護と管理、データの系統の追跡、データ・レイクの管理を支援するために、ガバナンス、データ品質、アクティブ・ポリシー管理を使用する方法を説明します。この知識は、データ資産、データセット、分析モデル、およびそれらの関係を組織内の他の人々と迅速に発見し、キュレーションし、分類し、共有するのに役立ちます。
meta_keywords: Data, AI, Analytics, Governance, IBM Cloud Pak for Data, Watson Knowledge
  Catalog
meta_title: Watson Knowledge Catalogでデータを検索、準備、理解する。
primary_tag: analytics
related_content:
- slug: what-data-catalog-and-why-you-need-one
  type: blogs
related_links:
- title: Introducing IBM Watson Knowledge Catalog
  url: https://medium.com/ibm-watson/introducing-ibm-watson-knowledge-catalog-cf42c13032c1
subtitle: IBM Cloud Pak for Dataプラットフォーム上のWatson Knowledge Catalogを使用して、エンタープライズデータガバナンスの問題を解決する。
tags:
- data-management
title: Watson Knowledge Catalogでデータを検索、準備、理解する。
type: tutorial
---

このチュートリアルでは、IBM Cloud Pak for Data プラットフォーム上の IBM Watson Knowledge Catalog を使用して、エンタープライズ・データ・ガバナンスの問題を解決する方法を示します。ガバナンス、データ品質、アクティブ・ポリシー管理を使用して、機密データの保護と管理、データのリネージの追跡、データ・レイクの管理を行う方法を説明します。この知識は、データ資産、データセット、分析モデル、およびそれらの関係をすばやく発見し、キュレーションし、分類し、組織内の他の人と共有するのに役立ちます。

## 学習目標

このチュートリアルでは、以下の方法を学びます。

1. [カタログを設定する](#1-set-up-catalog)
1. [データアセットの追加](#2-add-data-assets)
1. [コラボレーターの追加とアクセス制御](#3-add-collaborators and control-access)
1. [カテゴリの追加](#4-add-categories)
1. [データクラスの追加](#5-add-data-classes)
1. [ビジネス用語の追加](#6-ビジネス用語の追加)
1. [ポリシーのルールを追加](#7-add-rules-for-policies)

## 前提条件

* [IBM Cloud Pak for Data](https://www.ibm.com/jp-ja/products/cloud-pak-for-data)
* [Watson Knowledge Catalog](https://www.ibm.com/jp-ja/cloud/watson-knowledge-catalog)
* カタログを作成・管理するための管理者アクセス

## 見積もり時間

このチュートリアルを完了するには、約 30～45 分かかります。

## 手順

## 1.カタログを作成する

> 注：デフォルトのカタログは、エンタープライズカタログです。これは、Watson Knowledge Catalog サービスをインストールすると自動的に作成され、高度なデータキュレーションツールが適用される唯一のカタログです。デフォルトのカタログは、データ保護ルールが適用されるように管理されています。情報資産ビューには、キュレーションに役立つデフォルトカタログ内の資産の追加プロパティが表示されます。その後に作成するカタログは、ガバナイズされたものでもガバナイズされていないものでもよく、情報資産ビューはなく、基本的なデータ キュレーション ツールが提供されます。

まず、カタログを作成し、いくつかのデータを読み込みます。

### カタログの作成

* 左上(☰)のハンバーガーメニューで、`カタログ`→`全カタログ`を選択します。

  ![カタログを開くメニュー](images/wkc-admin-open-catalog-menu.png)

* *Your catalogs*ページから、`Create catalog`ボタンをクリックします。

  ![create WKC catalog](images/wkc-create-catalog.png)

* カタログに名前をつけ、`Enforce data protection rules`チェックボックスをチェックし、オプションで説明を記入します。そして、`Create`ボタンをクリックします。

  ![name and create wkc catalog](images/wkc-admin-name-creat-catalog.png)

*> *注意：データ保護のチェックボックスを選択する際には、ポップアップウィンドウで`Ok`をクリックしてください。

## 2.データ資産の追加

カタログにアセットを追加するにはいくつかの方法があります。ここでは、ローカルデータのアセットを追加します。また、以下に接続アセットを追加するオプションセクションがあります。

## ローカルデータアセット

1. [application_personal_data.csv](static/applicant_personal_data.csv)ファイルをダウンロードします。**Browse Assets**タブの下、Now you can add assetsの下、**here**をクリックしてデータを追加します。

* 右上の `Add to Catalog +` をクリックし、`Local files` を選択します。

  ![ローカルファイルのカタログへの追加](images/wkc-add-to-catalog-local-files.png)

* 「Select file(s)」パネルの「browse」リンクをクリックします。`/data/split/applicant_personal_data.csv` ファイルをブラウズして選択します。任意の説明を追加して、「Add」ボタンをクリックする。

  ![click add for local files to catalog](images/wkc-admin-file-selected-now-add.png)

*  > *NOTE: 読み込みが完了するまで、カタログの中にいてください!カタログから離れると、不完全なアセットは削除されます。

* 新しく追加されたファイルは、カタログの*Browse Assets*タブの下に表示されます。

  ![カタログに新しく追加されたデータ](images/wkc-admin-browse-assets.png)

### (Optional) Add Connection

* `Add to Catalog +` -> `Connection` を選択することで、例えば *DB2 Warehouse in IBM Cloud* など、様々なデータソースへの接続を追加することができます。

  ![カタログに接続を追加](images/wkc-add-connection.png)

* 追加したいデータソースの種類をクリックします（例：`Db2 Warehouse`）。

  ![chosen db2 warehouse connection ](images/wkc-choose-db2-warehouse-conn.png)

* 接続の詳細を入力し、`Create`をクリックします。

  ![enter db2 warehouse connection details](images/wkc-enter-connection-details.png)

* カタログに接続が表示されます。

****注意: 仮想化されたデータは、そのカタログの管理者または編集者のアクセス権を持つ人が、*Default*カタログに追加することができます。「データの仮想化」を接続として追加するオプションがあります。

### (オプション) 接続からのデータの追加

データソースへの接続が確立すると、その接続からアセットを追加できるようになります。

* `+Add to Catalog` -> `Connected asset` をクリックします。

  ![add connected asset](images/wkc-add-connected-asset.png)

* `*Source*をクリック -> `Select source`.DV`から自分のスキーマ(例:UserXYZW)を参照し、結合したテーブルを選択する。Select "をクリックします。

これでユーザーは、カタログの他のアセットと同様に、このテーブルをプロジェクトに追加することができます。

## 3.コラボレーターの追加とアクセスコントロール

* *アクセスコントロール*タブで、「コラボレーターの追加」をクリックすると、他のユーザーにカタログへのアクセス権を与えることができます。

  ![give users access to the catalog](images/wkc-admin-access-control-add-collaborator.png)

* `Collaborators` の欄にユーザーの名前を入力すると、そのユーザーを検索することができます。名前をクリックしてユーザーを選択し、`Add`をクリックする。

* ユーザーの役割を `Admin`, `Editor`, `Viewer` のいずれかから選択することができます。その後，「Add」ボタンをクリックする。

  ![協力者の役割を選択](images/wkc-admin-user-roll-choice.png)

* カタログのデータにアクセスするには、データ名をクリックしてください。

  ![click data name to open](images/wkc-admin-click-data-name-to-open.png)

* メタデータとGovernance artifactsを含むデータの概要が開きます。

  ![データの概要](images/wkc-admin-data-overview.png)

* `Asset` タブをクリックすると、最初の1000行のプレビューが表示されます。

  ![データのプレビュー](images/wkc-admin-data-preview.png)

* `Review` タブをクリックすると、データを評価したり、コメントをつけたりすることができ、データの消費者にフィードバックを与えることができます。

  ![データのレビュー](images/wkc-admin-review-data.png)

## 4.カテゴリーの追加

Watson Knowledge Catalog の基本的な抽象化は、Category です。カテゴリーは、フォルダに類似しています。必要に応じてカテゴリーを追加したり、CSV形式でインポートしたりすることができます。

### カテゴリーのインポート(オプション)

ユニークな名前のカテゴリーをインポートするには、ターミナルウィンドウでコマンドを実行することに慣れている必要があります。この作業に慣れていない方は読み飛ばしてください。

* カテゴリの名前はすべてグローバルスコープなので、固有の名前を持つファイルをインポートする必要があります。このリポジトリをクローンまたはダウンロードした場所に行き、`data/wkc/glossary-organize-categories.csv`というファイルにナビゲートしてください。スクリプト`data/wkc/prepend-user-tag.py`を、あなたのインティアルやその他のタグを使って実行し、ユニークなファイルを作成します。例えば、`./prepend-user-tag -T scottda`とします。`T`パラメータでタグを追加しなければ、Pythonのtime.time()文字列を使って、ユニークなCategory名を持つユニークなファイルが生成されます。

  ![prepend-user-tagスクリプトの実行](images/wkc-admin-prepend-user-tag.png)

* 左上のハンバーガーメニューから `Governance` -> `Categories` を選択し、`Add category` ボタンをクリックして `Import from file` を選択することで、アセットのカテゴリーをインポートします。

  ![Import categories](images/wkc-admin-import-categories.png)

* 例えば、`data/wkc/scottda-glossary-organize-categories.csv`は、`./prepend-user-tag.py -T scottda`を実行して作成したファイルになります。「Next」ボタンをクリックします。

  ![Import select file](images/wkc-import-select-file.png)

* `Select merge option` で `Replace all values` を選択し、`Import` をクリックします。

  ![選択マージオプションのインポート](images/wkc-import-select-merge-option.png)

* インポートが完了すると、「The import completed succesfully」と表示されます。

* このようにして、カテゴリー、ビジネス用語、分類、ポリシーなどをインポートして、ガバナンスカタログを作成することができます。

### 手動でカテゴリーを追加する

> 注: カテゴリー、ビジネス用語、データクラス、およびその他のガバナンスの成果物は、グローバルな範囲です。注意: カテゴリー、ビジネス用語、データクラス、およびその他のガバナンスアーティファクトはグローバルな範囲です。例えば、以下の例では、`XXX-Personal Data`の代わりに`scottda-Personal Data`を使用しています。

インポートだけでなく、手動でカテゴリーを作成することもできます。左上（☰）のハンバーガーメニューから`Governance`→`Categories`を選択し、`Add category`ボタンをクリックしてから`New category`をクリックして、アセットのカテゴリーを追加します。

  ![データカテゴリの整理](images/wkc-admin-menu-organize-categories.png)

* イニシャルやユニークなタグ(*XXX-Personal Data*など)を付けた名前と、オプションで説明文を付けて、`Save`ボタンをクリックします。

  ![新規カテゴリーの請求書](images/wkc-admin-new-category-personal-data.png)

* ここで、*Personal Data*カテゴリー画面の*Subcategories*の下にある`Create category`リンクを押すと、*Residence Information*のようなサブカテゴリーを作成することができます。

  ![サブカテゴリ・レジデンス情報](images/wkc-admin-new-subcategory-residence-information.png)

* *Personal Data* カテゴリでは、`Business term` のような *Type* を選択することができます。

  ![select business term type](images/wkc-admin-category-add-artifact.png)

* 左上のハンバーガーメニューから`Governance`→`Classifications`を選択することで、同様に*Confidential*、*Personally Identifiable Information*、*Sensitive Personal Information*のような資産の分類を作成することもできます。

  ![分類を選択](images/wkc-admin-navigate-classifications.png)

* 右上の「Add classification」ボタンをクリックして、ドロップダウンメニューから「New classification」を選択します。これらの分類は、あなたのカテゴリーに*タイプ*として追加することができます。

  ![select classification type](images/wkc-admin-add-classifications.png)

## 5.データクラスの追加

> 注：カテゴリー、ビジネス用語、データクラス、およびその他のGovernanceアーティファクトは、グローバルな範囲です。作成するように言われたら、自分のイニシャルや何かユニークなタグを前もって付けておかないと失敗します。例えば、以下の例では、「XXX-alphanumeric」の代わりに「scottda-alphanumeric」を使用します。

アセットをプロファイリングする際には、可能な限りコンテンツからデータクラスが推測されます。これについては後で詳しく説明します。また、独自のデータクラスを追加することもできます。

* 左上のハンバーガーメニューから「ガバナンス」→「データクラス」を選択し、「データクラスの追加」ボタンをクリックし、ドロップダウンメニューから「新規データクラス」を選択することで、アセットにデータクラスを追加することができます。

  ![データクラスの整理](images/wkc-admin-menu-organize-data-classes.png)

* *XXX-alphanumeric*のように、イニシャルやタグを前もって付けた名前を新しいデータクラスに付けて、Primaryカテゴリの`Change`をクリックします。

  ![新しいデータクラス](images/wkc-admin-create-data-class.png)

*Personal Data*のプライマリーカテゴリーを選び、`Add`をクリックします。

  ![プライマリーカテゴリーの変更](images/wkc-admin-change-primary-category.png)

* ここで、`Save as draft`をクリックします。

* データクラスが作成されたら、オプションとして、このクラスに*Stewards*を追加したり、*classification*や*business terms*を関連付けたりすることができます。準備ができたら、`Publish`ボタンをクリックして、ポップアップウィンドウでもう一度`Publish`をクリックします。

  ![データクラス用ツール](images/wkc-data-class-add-term-publish.png)

* それでは、そのデータクラスを *applicant_personal_data.csv* アセットのカラムに追加してみましょう。

**** 先ほど作成したカタログ（例：*CreditDataCatalog*）に戻って、それを開きます（(☰)ハンバーガーメニューの `Catalogs` -> `All catalogs` で `CreditDataCatalog` を選択）。*Browse assets*タブで、データセット*applicant_personal_data.csv*をクリックして、`Asset`タブをクリックすると、列/行のプレビューが表示されます。*CustomerID*列を見つけて、「顧客番号」の横にある下矢印をクリックし、次に*View all*をクリックします。

  ![データクラスの変更](images/wkc-admin-existing-data-class.png)

* 開いたウィンドウで、新しく作成したデータクラスである*alphanumeric*を検索し、検索で戻ってきたらそれをクリックします。そして、`Select`ボタンをクリックします。

  ![Set colunn to numerical data class](images/wkc-admin-numeric-data-class.png)

## 6.ビジネス用語の追加

> 注：カテゴリー、ビジネス用語、データクラス、およびその他のGovernanceアーティファクトは、グローバルな範囲です。作成するように言われたら、自分のイニシャルや何かユニークなタグを前もって付けておかないと失敗します。例えば、以下では、`XXX-連絡先情報`の代わりに`scottda-連絡先情報`を使用しています。

[ビジネス用語](https://dataplatform.cloud.ibm.com/docs/content/wsj/governance/dmg16.html)を使用して、ビジネスコンセプトの定義を標準化することで、企業全体で統一された理解しやすい方法でデータを記述することができます。

カテゴリーを作成して、それを*ビジネス用語*にする方法はすでに見ました。ビジネス・タームを独自のエンティティとして作成することもできます。

* 左上（☰）のハンバーガー・メニューから、「ガバナンス」→「ビジネス用語」を選択します。

  ![データビジネス用語の整理](images/wkc-admin-organize-data-business-terms.png)

* 右上の「Add business term」ボタンをクリックし、ドロップダウンメニューの「New business term」オプションをクリックします。

  ![ビジネス用語の作成](images/wkc-admin-create-business-term.png)

* 新しいビジネス用語に、イニシャルや*XXX-Contact Information*のようなタグを前もって付けた名前と、オプションで説明を付けます。*Primary category* の下の `Change` をクリックして *Personal data* を選択し、`Save as draft` ボタンをクリックします。

  ![名前の新しいビジネス用語](images/wkc-admin-name-business-term.png)

* 用語が作成されると、ウィンドウが表示されます。関連用語の作成やその他のメタデータを追加するための豊富なオプションが表示されます。とりあえず、`Publish`をクリックして、この用語をプラットフォームのユーザーが利用できるようにします。ポップアップした確認ウィンドウで「Publish」をクリックします。

  ![ビジネス用語の公開](images/wkc-admin-publish-business-term.png)

****先ほど作成したカタログ（例：*CreditDataCatalog*）に戻って、それを開きます（(☰)ハンバーガーメニュー `Catalog` -> `All catalogs` で `CreditDataCatalog` を選択）。*Browse assets*タブで、データセット*applicant_personal_data.csv*をクリックし、次に`Asset`タブをクリックすると、列/行のプレビューが表示されます。*Email*列を見つけて、*列情報*アイコンをクリックします（「目」のように見えます）。

  ![メール欄の情報を選択](images/wkc-admin-email-column-information.png)

* 開いたウィンドウで、*Business terms*の横にある*edit*アイコン（「鉛筆」のように見える）をクリックします。

  ![ビジネス用語の編集](images/wkc-admin-assign-terms-to-column.png)をクリックします。

* *XXX-Contact Information*（*scottda-ContactInfo*のようなあなたのユニークな名前の用語）先ほど*Business terms*で作成した用語を入力すると、その用語が検索されます。見つかった`Contact Information`の用語をクリックして、`Apply`をクリックします。

  ![ビジネス用語の検索](images/wkc-admin-search-contact-to-assign-term.png)

* 用語が適用されたら、そのウィンドウの`Close`をクリックしてください。次に、同じようにして、*Telephone*列に*Contact Information* Business termを追加します。

* これで、プラットフォーム内でこれらの用語を検索できるようになります。例えば、トップレベルの*CreditDataCatalog*に戻って、"What assets are you searching for? "というコメントのある検索バーに、固有の*<unique_string>Contact Information*という用語を入力します。

  ![ビジネス用語で検索](images/wkc-admin-search-business-terms.png)

* *applicant_personal_data.csv*データセットは、*Contact Infomation*ビジネス用語でタグ付けされたカラムを含んでいるので、表示されます。

## 7.ポリシーのルールを追加する

ユーザーがデータにアクセスする方法を制御するルールを作成できるようになりました。

> 注意：ワークショップのチームメイトは、ルールに関連付ける用語を単純に1つ再利用することができます（例：*CustomerID*）。

* *XXX-CustomerID*というビジネス用語を作成するか、またはワークショップのチームメイトのビジネス用語の1つをこのエクササイズのために再利用してください。それを上記の手順でデータセットの*CustomerID*列に割り当てます。詳細が必要な場合は以下を参照してくださいが、まず自分で試してみてください。また、注意喚起が不要な場合は以下の*Adding a rule*にスキップしてください。

### ビジネス用語のレビューを作成する方法

* 左上（☰）のハンバーガーメニューから、「Governance」→「Business terms」を選択します。

* 右上の「ビジネス用語の追加」ボタンをクリックし、ドロップダウンメニューの「新規ビジネス用語」を選択します。

**** 新しいビジネス用語に *XXX-CustomerID* という名前と、オプションで説明を付けます。*プライマリー・カテゴリ*の下にある「変更」をクリックして、*Personal data*を選択し、「ドラフトとして保存」ボタンをクリックします。次のウィンドウで`Publish`をクリックします。

* 先ほど作成したカタログ（例：*CreditDataCatalog*）に戻り、それを開きます（(☰)ハンバーガーメニューの`Catalog`->`All catalogs`で`CreditDataCatalog`を選択）。*Browse assets*タブで、データセット*applicant_personal_data.csv*をクリックして、`Asset`タブをクリックすると、列/行のプレビューが表示されます。*CustomerID*列を見つけて、*Column information*アイコンをクリックします（「目」のように見えます）。

* 開いたウィンドウで、*Business terms* の隣にある *edit* アイコンをクリックします（「鉛筆」のように見えます）。

* *Business terms* の下に *CustomerID* を入力すると、その用語が検索されます。検索された `CustumerID` の用語をクリックして、`Apply` をクリックします。その後、ポップアップウィンドウを閉じます。

### ルールの追加

* 左上のハンバーガーメニューから、`Governance` -> `Rules` を選択します。

* 右上の「Add rule」ボタンをクリックして、ドロップダウンメニューから「New rule」を選択してください。

* 「Create a new rule」ページで、「Data protection rule」オプションを選択します。

  ![データ保護ルール](images/wkc-new-dataprotection-rule.png)

* ルールにユニークな *XXX-Name* を与え、*Type* を `Access` に設定したまま、*Business definition* を追加してください。

* *Rule builder* > *Condition1* の下にあります。`If`の条件では、*Business term* *Contains any* *CustomerID*を選択します。*Action* の下の `then` パネルでは、*mask data* *in columns containing* *alphanumeric* を選択します。「Substitute」のタイルを選択すると、個人を特定できないハッシュが作成されます。これにより、実際のCustomerIDは見えなくなりますが、データベースの結合などの動作は可能になります。「ルールの作成」ボタンをクリックします。

  ![define rule for masking customerID](images/wkc-admin-rule-substitute-customer-id.png)

* ここで、カタログ内の*applicant_personal_data.csv*アセットの*CustomerID*カラムに戻ると、前と同じように見えます。しかし、管理者ではないユーザーには「ロック」アイコンが表示され、customerIDがハッシュ値で置き換えられていることがわかります。

* データを*難読化*するルールを追加するには、*Age*という新しいデータクラスを作成します。必要に応じて上記の説明を参照し、クラスを公開することを忘れないでください。

*CreditDataCatalog*に戻り、*applicant_personal_data.csv*資産の下で、`Overview`タブに行き、*Age*列までスクロールします。「下矢印」をクリックすると、データが*Code*に分類されていることが推測されます。`View all`をクリックして分類器を変更します。

  ![Age classified as Code](images/wkc-admin-inferred-classifier-code.png)

* 今度は、*Age*と入力し始めてclassifierを変更します。これが検索で出てきたら、それを選択して、`Select`ボタンをクリックします。

  ![classifierを変更して使用](images/wkc-admin-change-classifier-select.png)

* 前述の指示に従って、この *Age* カラムを *難読化* するための新しいデータ保護ルールを構築することができます。

  ![Age obfuscate rule](images/wkc-admin-create-obfuscate-rule.png)

* これで、管理者以外のユーザーがその列を見たときに、同様のフォーマットのデータに置き換えられたデータが表示されます。

## まとめ

このラボでは、以下の方法を学びました。

* カタログとデータの設定
* コラボレーターの追加とアクセス制御
* カテゴリーの追加
* データクラスの追加
* ビジネス用語の追加
* ポリシーのルールの追加

このチュートリアルは、[Getting started with IBM Cloud Pak for Data Learning Path](/learningpaths/cloud-pak-for-data-learning-path/)の一部です。このシリーズを続けて IBM Cloud Pak for Data について詳しく学ぶには、次のパターンである [Data analysis, model building, and deploying with Watson Machine Learning with notebook](/patterns/data-analysis-model-building-and-deploying-with-wml/) を参照してください。次のチュートリアルである[Automate model building with AutoAI](/tutorials/automate-model-building-with-autoai/)または[Build a predictive machine learning model quickly and easily with IBM SPSS Modeler](/tutorials/build-an-ai-model-visually-with-spss-modeler-flow/)を見てみましょう。

このチュートリアルでは、IBM Cloud Pak for Data プラットフォームでデータを扱う際に利用できる強力なツールの一部を学びました。IBM Watson Knowledge Catalog を使えば、チーム・メンバーがそれぞれの役割で協力して、データと AI を企業にもたらすことができます。