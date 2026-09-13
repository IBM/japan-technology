※ 2021/7/21 移行作業中につき、不完全な状態です。ご注意ください。
--
このチュートリアルは「[ラーニング・パス: IBM Cloud Pak for Data 入門](/jp/series/cloud-pak-for-data-learning-path/)」の一部です。

| レベル | トピック | タイプ |
| --- | --- | --- |
| 100 | [IBM Cloud Pak for Data の紹介](/jp/articles/intro-to-cloud-pak-for-data) | 記事 |
| 101 | [データ仮想化ツールを使用して Db2 Warehouse のデータを仮想化する](/jp/tutorials/virtualizing-db2-warehouse-data-with-data-virtualization/) | チュートリアル |
| 201 | [Data Refinery によるデータの可視化](/jp/tutorials/data-visualization-with-data-refinery) | チュートリアル |
| **202** | **Watson Knowledge Catalog を利用してデータを発見、準備、理解する** | **チュートリアル** |
| 301A | [Watson Machine Learning と Jupyter Notebook を利用してデータ分析、モデルの作成、デプロイを行う](/jp/patterns/data-analysis-model-building-and-deploying-with-wml) | パターン |
| 301B | [Automate model building with AutoAI](/jp/tutorials/automate-model-building-with-autoai) | チュートリアル |
| 301C | [Build a predictive machine learning model quickly and easily with IBM SPSS Modeler](/jp/tutorials/build-an-ai-model-visually-with-spss-modeler-flow) | チュートリアル |
| 401 | [Watson OpenScale でモデルをモニタリングする](/jp/patterns/watson-openscale-with-watson-machine-learning-engine-on-icp4d) | パターン |

このチュートリアルでは、IBM Cloud Pak&reg; for Data プラットフォーム上の IBM Watson&reg; Knowledge Catalog を利用してエンタープライズ・データ・ガバナンスの問題を解決する例を紹介します。この例を通して、機密データの管理、データ・リネージュの追跡、データレイクの管理をサポートするために、ガバナンス、データ品質、アクティブ・ポリシー管理を使用する方法を説明します。この方法を把握していれば、データ資産、データ・セット、分析モデル、およびこれらの関係を迅速に発見、キュレート、分類して、組織の他のメンバーと共有できます。

## 学習の目的

このチュートリアルでは、以下の方法を学びます。

1. [カタログとデータをセットアップする](#1-set-up-catalog-and-data)
1. [コラボレーターを追加してアクセスを制御する](#2-add-collaborators-and-control-access)
1. [カテゴリーを追加する](#3-add-categories)
1. [データ・クラスを追加する](#4-add-data-classes)
1. [ビジネス用語を追加する](#5-add-business-terms)
1. [ポリシーのルールを追加する](#6-add-rules-for-policies)

## 前提条件

* [IBM Cloud Pak for Data](https://www.ibm.com/products/cloud-pak-for-data)
* [Watson Knowledge Catalog](https://www.ibm.com/support/producthub/icpdata/docs/content/SSQNUZ_current/wsj/catalog/overview-wkc.html)
* カタログを作成して管理するための管理者アクセス権限

## 所要時間

このチュートリアルの所要時間は約 30 ～ 45 分です。

## 手順

**注:** デフォルトのカタログは、自社のエンタープライズ・カタログです。このカタログは、Watson Knowledge Catalog サービスをインストールすると自動的に作成されます。高度なデータ・キュレーション・ツールが適用されるのは、このカタログのみです。デフォルトのカタログは、データ保護ルールが適用されるように管理されます。情報資産ビューには、キュレーションに役立つよう、デフォルトのカタログに含まれる資産の追加プロパティーが示されます。以降に作成するカタログは、管理対象または非管理対象にすることができます。これらのカタログには情報資産ビューはありませんが、基本的なデータ・キュレーション・ツールが用意されます。

## ステップ 1. カタログとデータをセットアップする {: #1-set-up-catalog-and-data}

### カタログを作成する

これから IBM Watson Knowledge Catalog を利用し始める場合は、最初にプロビジョニングする必要があります。ホーム・ページの右上にある「**Services (サービス)** 」アイコンをクリックして IBM Watson Knowledge Catalog を開いてください。

![サービス・アイコンのスクリーンショット](../../images/wkc-click-services-icon.jpg)

「**Data Governance (データ・ガバナンス)** 」セクションで、「**Watson Knowledge Catalog** 」タイルをクリックします。

![IBM Watson Knowledge Catalog タイルを示す画面のスクリーンショット](../../images/wkc-open-service.png)

手順に従って IBM Watson Knowledge Catalog をデプロイします。

#### IBM Watson Knowledge Catalog を開く

1. 右上にある「**Open (開く)** 」をクリックして起動します。
![IBM Watson Knowledge Catalog を開くためのボタンのスクリーンショット](../../images/wkc-open-service-2.jpg)

1. 左上のハンバーガー (☰) メニューから、**「Organize (編成)」 > 「All catalogs (すべてのカタログ)」** を選択します。
![カタログ・メニュー項目のスクリーンショット](../../images/wkc-admin-open-catalog-menu.png)

1. 「Your catalogs (あなたのカタログ)」ページで、「**Create catalog (カタログを作成)** 」または「**New Catalog (新しいカタログ)** 」をクリックします。
![IBM Watson Knowledge Catalog でカタログの作成を開始するための操作を示す画面のスクリーンショット](../../images/wkc-create-catalog.png)

1. カタログの名前 (例: `TelcoDataCatalog`) と説明 (省略可) を入力し、「**Enforce data protection rules (データ保護ルールを適用する)** 」チェック・ボックスをオンにしてから、「**Create (作成)** 」をクリックします。
![IBM Watson Knowledge Catalog のカタログに名前を付けて作成する画面のスクリーンショット](../../images/wkc-name-describe-create.png)

1. 前の画面でチェック・ボックスをオンにしたときに表示されるポップアップでは、「**OK** 」をクリックしてください。
![データ保護ルールの適用を確認するポップアップのスクリーンショット](../../images/wkc-enforce-data-protection.png)

#### 方法 1: データ資産を追加する

1. [Telco-Customer-Churn.csv](../../static/Telco-Customer-Churn.csv) ファイルをダウンロードします。「**Browse Assets (資産の参照)** 」タブで、「Now you can add assets (資産を追加できます)」の下に示されている「**here (ここ)** 」リンクをクリックしてデータの追加を開始します。
![資産の追加を開始する操作を示す画面のスクリーンショット](../../images/wkc-add-data-asset.png)

1. または、右上にある「**Add to catalog + (カタログに追加 +)** 」をクリックして、例えば「**Local files (ローカル・ファイル)** 」を選択してデータを追加することもできます。
![ローカル・ファイルをカタログに追加するためのメニュー項目のスクリーンショット](../../images/wkc-add-to-catalog-local-files.png)

1. [Telco-Customer-Churn.csv](../../static/Telco-Customer-Churn.csv) ファイルをダウンロードした場所を参照してダブルクリックするか、「**Open (開く)** 」をクリックします。必要に応じて説明を入力してから、「**Add (追加)** 」をクリックします。
![ローカル・ファイルをカタログに追加する画面のスクリーンショット](../../images/wkc-file-selected-now-add.png)

**注:** 読み込みが完了するまで、カタログを離れないでください。カタログを離れると読み込みが中止され、読み込み途中の不完全な資産が削除されます。

新しく追加した Telco-Customer-Churn.csv ファイルがカタログの「Browse Assets (資産の参照)」タブに表示されます。

![カタログに新しく追加されたデータを示す画面のスクリーンショット](../../images/wkc-browse-assets.png)

#### 方法 2: 接続を追加する

1. リモート DB (IBM Cloud 内の DB2 Warehouse など) への接続を追加することもできます。それには、**「Add to catalog + (カタログに追加 +)」 > 「Connection (接続)」** を選択します。
![接続をカタログに追加するためのメニュー項目を示す画面のスクリーンショット](../../images/wkc-add-connection.png)

1. リモート DB を選択してクリックします。
![Db2 Warehouse を選択する画面のスクリーンショット ](../../images/wkc-choose-db2-warehouse-conn.png)

1. 接続の詳細を入力して、「**Test (テスト)** 」をクリックします。接続成功のメッセージが返されたら、「**Create (作成)** 」をクリックします。
![Db2 Warehouse に接続するための詳細を入力する画面のスクリーンショット](../../images/wkc-enter-connection-details.png)

追加した接続がカタログ内に表示されます。

![Db2 Warehouse との接続が表示された画面のスクリーンショット](../../images/wkc-new-connection-shows-up.png)

#### 方法 3: 仮想化データを追加する

**注**: デフォルトのカタログに仮想化データを追加するユーザーには、そのカタログに対する管理者アクセス権限または編集者アクセス権限が付与されている必要があります。

1. 左上のハンバーガー (☰) メニューから**「Organize (編成)」 >「All catalogs (すべてのカタログ)」** を選択し、**「Add to Catalog + (カタログに追加 +)」 > 「Connected asset (接続済み資産)」** をクリックします。
![接続済み資産を追加するためのメニュー項目を示す画面のスクリーンショット](../../images/wkc-add-connected-asset.png)

1. **「Source (ソース)」 > 「Select source (ソースを選択)」** をクリックします。DV 内のスキーマを参照し、追加するテーブルを選択してから「**Select (選択)** 」をクリックします。
![ソースを選択する画面のスクリーンショット](../../images/wkc-select-source.png)

これで、ユーザーが他の資産と同じように仮想化データをカタログからプロジェクトに追加できるようになります。

### ステップ 2. コラボレーターを追加してアクセスを制御する {: #2-add-collaborators-and-control-access}

1. 他のユーザーにカタログに対するアクセス権限を付与するには、「Access Control (アクセス制御)」タブで「**Add Collaborator (コラボレーターの追加)** 」をクリックします。
![カタログに対するアクセス権限をユーザーに付与するウィンドウのスクリーンショット](../../images/wkc-access-control-add-collaborator.png)

1. ユーザーを検索し、ユーザー名をクリックして選択します。そのユーザーのロール (管理者、編集者、または閲覧者) を選択してから「**Add (追加)** 」をクリックします。
![ユーザーを検索してコラボレーターとして追加するウィンドウのスクリーンショット](../../images/wkc-choose-user-and-add.png)

1. カタログ内のデータにアクセスするには、データの名前をクリックします。
![データの名前をクリックしてデータを開く操作を示す画面のスクリーンショット](../../images/wkc-click-data-name-to-open.png)

1. データのプレビューが開き、メタデータと最初の数行が表示されます。
![データのプレビュー画面のスクリーンショット](../../images/wkc-data-preview.png)

1. 「**Review (レビュー)** 」タブをクリックします。このタブで、データを評価できます。また、データにコメントを追加して、チームメイトにフィードバックを提供することもできます。
![データをレビューするタブのスクリーンショット](../../images/wkc-review-data.png)

### ステップ 3. カテゴリーを追加する

IBM Watson Knowledge Catalog 内での基本的な抽象化は、カテゴリーです。カテゴリーはフォルダーに似ています。 

資産のカテゴリーを追加するには、左上のハンバーガー (☰) メニューから**「Organize (編成)」 > 「Data and AI Governance (データと AI のガバナンス)」 > 「Categories (カテゴリー)」** を選択します。

![カテゴリーを追加するためのメニュー項目を示す画面のスクリーンショット](../../images/wkc-add-categories.png)

カテゴリーを .csv 形式でインポートすることも (方法 1)、手作業で追加することもできます (方法 2)。

#### 方法 1: カテゴリーをインポートする

[glossary-organize-categories.csv](../../static/glossary-organize-categories.csv) ファイルをダウンロードします。このファイルに含まれているカテゴリー・データをインポートすることになります。

1. 「**Import (インポート)** 」をクリックします。
![カテゴリーをインポートするためのボタンのスクリーンショット](../../images/wkc-import-categories.png)

1. 「**Add file (ファイルを追加)** 」をクリックし、ダウンロードした [glossary-organize-categories.csv](../../static/glossary-organize-categories.csv) ファイルを参照して選択してから、「**Next (次へ)** 」をクリックします。
![csv のインポート・ウィンドウのスクリーンショット](../../images/wkc-import-csv.png)

1. 「Select merge option (マージ方法を選択)」の下に示されている「**Replace all values (すべての値を置換する)** 」をオンにしてから「**Import (インポート)** 」をクリックします。
![マージ方法を選択するインポート・ウィンドウのスクリーンショット](../../images/wkc-import-select-merge-option.png)

インポートが完了すると、「The import completed successfully (インポートが正常に完了しました)」というメッセージが表示されます。「**Close (閉じる)** 」をクリックしてメッセージを閉じます。

![インポートの完了メッセージを示す画面のスクリーンショット](../../images/wkc-import-complete.png)

このようにしてカテゴリー、ビジネス用語、区分、ポリシーなどをインポートし、ガバナンス・カタログに取り込むことができます。

#### 方法 2: 手作業でカテゴリーを追加する

1. 「**Create category (カテゴリーを作成)** 」をクリックします。
![データを整理するカテゴリーを作成するためのボタンのスクリーンショット](../../images/wkc-menu-organize-categories.png)

1. カテゴリーの名前 (例: `Billing`) と説明 (省略可) を入力し、「**Save (保存)** 」をクリックします。
![新しいカテゴリー Billing を追加する操作を示す画面のスクリーンショット](../../images/wkc-new-category-billing.png)

1. 新しく追加した Billing カテゴリーの画面で「**Create category (カテゴリーを作成)** 」を再び選択すると、サブカテゴリー (例: `Total Charges`) を作成できます。
![サブカテゴリー Total Charges を追加する操作を示す画面のスクリーンショット](../../images/wkc-new-sub-category-totalcharges.png)

1. Billing カテゴリーにはタイプ (`Business term` など) を選択できます。
![Business Term タイプを選択する操作を示す画面のスクリーンショット](../../images/wkc-category-select-type.png)

1. 資産の区分 (機密、個人情報、機密個人情報など) を作成することもできます。その場合も同じようにして、左上のハンバーガー (☰) メニューから**「Organize (編成)」 > 「Data and AI Governance (データと AI のガバナンス)」 > 「Classifications (区分)」** を選択します。
![区分を追加するためのメニュー項目を示す画面のスクリーンショット](../../images/wkc-add-classifications.png)

1. 「**New classification (新しい区分)** 」ドロップダウンから「**Create new classification (新しい区分を作成)** 」を選択します。新しく作成した区分をタイプとしてカテゴリーに追加できます。
![区分タイプを選択する画面のスクリーンショット](../../images/wkc-add-classifications-2.png)

### ステップ 4. データ・クラスを追加する

資産のプロファイルを作成するときは、可能な場合はコンテンツからデータ・クラスが推論されますが、独自のデータ・クラスを追加することもできます。

1. 資産のデータ・クラスを追加するには、左上のハンバーガー (☰) メニューから**「Organize (編成)」 > 「Data and AI Governance (データと AI のガバナンス)」 > 「Data class (データ・クラス)」** を選択し、**「New data class (新しいデータ・クラス)」 > 「Create new data class (新しいデータ・クラスを作成)」**をクリックします。
![データ・クラスを作成するためのボタンのスクリーンショット](../../images/wkc-menu-organize-data-classes.png)

1. 新しいデータ・クラスの名前 (例: `alphanumeric`) を入力し、必要に応じて 1 次カテゴリーや説明を入力してから、「**Save as draft (ドラフトとして保存)** 」をクリックします。
![新しいデータ・クラスを作成するウィンドウのスクリーンショット](../../images/wkc-create-data-class.png)

1. データ・クラスを作成した後、このクラスのスチュワードを追加したり、区分やビジネス用語を関連付けたりできます。必要な設定が完了したら、「**Publish (公開)** 」をクリックします。
![データ・クラスのツールを示す画面のスクリーンショット](../../images/wkc-data-class-add-term-publish.png)
![データ・クラスを公開する際にコメントを入力するウィンドウのスクリーンショット](../../images/wkc-data-publish-comment.png)

作成したこのデータ・クラスを、Telco-Customer-Churn.csv 資産の列に追加しましょう。

1. 作成したカタログ (この手順では例として `TelcoDataCatalog` と名付けています) に戻って、カタログの列ビューを開きます。それにはまず、ハンバーガー (☰) メニューをクリックし、**「Organize (編成)」 > 「All catalogs (すべてのカタログ)」 > 「TelcoDataCatalog」** を選択してください。

1. 「Browse assets (資産の参照)」タブで、データ・セット **Telco-Customer-Churn.csv** をクリックして列/行のプレビューを表示します。

1. 右のほうにスクロールして「CustomerID」列を表示します。「Customer Number (顧客番号)」の横にある下矢印をクリックし、「**View all (すべて表示)** 」をクリックします。
![データ・クラスの変更を開始する操作を示す画面のスクリーンショット](../../images/wkc-admin-existing-data-class.png)

1. 表示されるウィンドウ内で、新しく作成したデータ・クラス (alphanumeric) を検索します。このクラスが検索結果として返されたら、それをクリックしてから「**Select (選択)** 」をクリックします。
![列を数値データ・クラスに変更する操作を示す画面のスクリーンショット](../../images/wkc-admin-alphanumeric-data-class.png)

### ステップ 5. ビジネス用語を追加する

[ビジネス用語](https://dataplatform.cloud.ibm.com/docs/content/wsj/governance/dmg16.html)を使用すると、ビジネス・コンセプトの定義を標準化して、企業全体で統一された理解しやすい方法でデータを記述できるようにすることができます。カテゴリーを作成して、それをビジネス用語にする方法はすでに説明しましたが、ビジネス用語を独自のエンティティーとして作成することもできます。

1. 左上のハンバーガー (☰) メニューから**「Organize (編成)」> 「Data and AI Governance (データと AI のガバナンス)」 > 「Business terms (ビジネス用語)」** を選択します。
![データのビジネス用語を作成するためのボタンのスクリーンショット](../../images/wkc-organize-data-business-terms.png)

1. 右上の「**New business term (新しいビジネス用語)** 」ドロップダウンをクリックし、「**Create new business term (新しいビジネス用語を作成)** 」ボタンをクリックします。
![ビジネス用語を作成するためのボタンのスクリーンショット](../../images/wkc-create-business-term.png)

1. 新しいビジネス用語の名前 (例: `Billing`) を入力し、必要に応じて説明を追加してから「**Save as draft (ドラフトとして保存)** 」をクリックします。
![新しいビジネス用語の名前を入力するウィンドウのスクリーンショット](../../images/wkc-name-new-business-term.png)

1. ビジネス用語が作成されると、ウィンドウが表示されます。関連する用語を作成したり、他のメタデータを追加したりするための一連の選択肢が表示されます。「**Publish (公開)** 」をクリックすると、この用語がプラットフォームのユーザーに公開されます。
![ビジネス用語を公開するためのボタンのスクリーンショット](../../images/wkc-publish-business-term.png)

1. 新しく表示されるウィンドウで、必要に応じてコメントを追加してから「**Publish (公開)** 」をクリックします。
![ビジネス用語の公開を確認するウィンドウのスクリーンショット](../../images/wkc-click-publish.png)

1. 作成したカタログ (この手順では例として `TelcoDataCatalog` と名付けています) に戻って、カタログの列ビューを開きます。それにはまず、ハンバーガー (☰) メニューをクリックし、**「Organize (編成)」 > 「All catalogs (すべてのカタログ)」 > 「TelcoDataCatalog」** を選択します。「Browse assets (資産の参照)」タブで、データ・セット **Telco-Customer-Churn.csv** をクリックして列/行のプレビューを表示します。右のほうにスクロールして「TotalCharges」列を表示し、「**Column information (列情報)** 」アイコン (目のように見えるアイコン) をクリックします。
![「TotalCharges」列情報を選択する操作を示す画面のスクリーンショット](../../images/wkc-totalcharges-column-information.png)

1. 表示されるウィンドウで、「Business Terms (ビジネス用語)」の横にある編集アイコン (鉛筆のようなアイコン) をクリックします。
![ビジネス用語を編集するためのアイコンのスクリーンショット](../../images/wkc-assign-terms-to-column.png)

1. 「Business Terms (ビジネス用語)」の下に「`Billing`」(ビジネス用語に指定した名前) と入力して、この用語を検索します。検索結果として返された用語「**Billing** 」をクリックしてから、「**Apply (適用)** 」をクリックします。
![ビジネス用語を適用するウィンドウのスクリーンショット](../../images/wkc-search-billing-to-assign-term.png)

1. 用語が適用されたら、ウィンドウを閉じます。

1. 同じ手順を繰り返して、ビジネス用語「`Billing`」を「MonthlyCharges」列にも追加します。これで、プラットフォーム内からこれらの用語を検索できるようになります。例えば、最上位の TelcoDataCatalog に戻り、「What assets are you searching for? (検索対象の資産を入力してください) 」というコメントが表示された検索バーに、この独自に作成したビジネス用語「Billing」を入力します。
![ビジネス用語を使用して検索する操作を示す画面のスクリーンショット](../../images/wkc-search-business-terms.png)

Telco-Customer-Churn.csv データ・セットが表示されます。このデータ・セットには、ビジネス用語「Billing」でタグが付けられた列が含まれているためです。

### ステップ 6. ポリシーのルールを追加する

次は、データに対するユーザーのアクセスを制御するルールを作成します。上記の手順に従って「`CustomerID`」というビジネス用語を作成して、データ・セット内の「CustomerID」列にこの用語を割り当ててください。以下に詳しい手順を説明していますが、まずは自分で試してください。復習する必要がなければ、「[ルールを追加する](#adding-a-rule)」手順にスキップしてかまいません。

#### ビジネス用語を作成する方法の復習

1. 左上のハンバーガー (☰) メニューから**「Organize (編成)」 > 「Data and AI Governance (データと AI のガバナンス)」 > 「Business terms (ビジネス用語)」** を選択します。
1. 右上の「**New business term (新しいビジネス用語)** 」ドロップダウンをクリックし、「**Create new business term (新しいビジネス用語を作成)** 」ボタンをクリックします。
1. 新しいビジネス用語の名前として「`CustomerID`」と入力し、必要に応じて説明を追加してから「**Save as draft (ドラフトとして保存)** 」をクリックします。表示されるウィンドウで、「**Publish (公開)** 」をクリックします。ポップアップ内で必要に応じてコメントを入力し、「**Publish (公開)** 」をクリックします。
1. TelcoDataCatalog に戻って、このカタログの列ビューを開きます。それにはまず、ハンバーガー (☰) メニューから**「Organize (編成)」 > 「All catalogs (すべてのカタログ)」** を選択し、「**TelcoDataCatalog** 」を選択します。「Browse assets (資産の参照)」タブで、データ・セット **Telco-Customer-Churn.csv** をクリックして列/行のプレビューを表示します。右のほうにスクロールして「CustomerID」列を表示し、「**Column information (列情報)** 」アイコン (目のように見えるアイコン) をクリックします。
1. 表示されるウィンドウで、「Business Terms (ビジネス用語)」の横にある**編集** アイコン (鉛筆のようなアイコン) をクリックします。
1. 「Business Terms (ビジネス用語)」の下に「`CustomerID`」と入力して、この用語を検索します。検索結果として返された用語「**CustomerID** 」をクリックしてから、「**Apply (適用)** 」をクリックします。

#### ルールを追加する {: #adding-a-rule}

1. 左上のハンバーガー (☰) メニューから**「Organize (編成)」 > 「Data and AI Governance (データと AI のガバナンス)」 > 「Rules (ルール)」** を選択します。
![「Rules (ルール)」メニュー項目を示す画面のスクリーンショット](../../images/wkc-rules-menu.png)

1. 「**New rule (新しいルール)** 」ドロップダウンから「**Create new rule (新しいルールを作成)** 」を選択します。
![新しいルールを作成するためのメニュー項目を示す画面のスクリーンショット](../../images/wkc-create-rule.png)

1. 作成するルールのタイプとして「**Data protection rule (データ保護ルール)** 」を選択します。
![データ保護ルールを示す画面のスクリーンショット](../../images/wkc-data-protection.png)

1. ルールの詳細として、ルールの名前、タイプ、アクセス、ビジネス定義を入力します。

1. ルール・ビルダーの「Condition 1 (条件 1)」として「if business term contains any CustomerID (ビジネス用語に CustomerID が含まれている場合)」と、「Action (アクション)」として「then mask data in columns containing `alphanumeric` (alphanumeric を含む列内のデータをマスキングする)」を指定します。「Substitute (置換)」のタイルを選択して、識別不可能なハッシュに置換されるようにします。これにより、実際の CustomerID は難読化されますが、データベース結合などのアクションは引き続き機能します。最後に「**Create (作成)** 」をクリックします。
![CustomerID をマスキングするルールを定義する画面のスクリーンショット](../../images/wkc-rule-substitute-customer-id.png)

カタログ内の Telco-Customer-Churn.csv 資産を再表示すると、「CustomerID」列は前と同じように見えますが、管理者以外のユーザーにはこの列内にロック・アイコンが示されます。また、CustomerID はハッシュ値で置換されています。
![マスキングされた CustomerID を示す画面のスクリーンショット](../../images/wkc-masked-column-customer-id.png)

データを難読化するルールを追加するには、「Profile (プロファイル)」タブを表示して、「TotalCharges」列までスクロールします。この列のデータは「Quantity (数量)」区分として推論されていることがわかります。
![「Quantity (数量)」に区分されている TotalCharges を示す画面のスクリーンショット](../../images/wkc-inferred-classifier-totalcharges.png)

推論されている区分が意図したものでない場合は、ここで区分を変更できます。

1. この「TotalCharges」列を難読化するルールを作成できます。
![「TotalCharges」列を難読化するルールを示す画面のスクリーンショット](../../images/wkc-build-obfuscate-rule.png)

1. この列のデータは同様にフォーマット設定されたデータで置き換えられます。
![難読化された「TotalCharges」列を示す画面のスクリーンショット](../../images/wkc-obfuscated-totalchurn-column.jpg)

## まとめ

このチュートリアルでは、IBM Cloud Pak for Data プラットフォーム上に用意されている、強力なデータ操作ツールのいくつかを紹介しました。IBM Watson Knowledge Catalog を利用すると、チーム・メンバーがそれぞれのロールで共同作業して、データと AI の力を企業で活用できるようになります。

このチュートリアルは「[ラーニング・パス: IBM Cloud Pak for Data 入門](/jp/series/cloud-pak-for-data-learning-path)」の一部です。このシリーズで引き続き IBM Cloud Pak for Data の詳細を学ぶには、次のパターン「[Watson Machine Learning と Jupyter Notebook を利用してデータ分析、モデルの作成、デプロイを行う](/jp/patterns/data-analysis-model-building-and-deploying-with-wml)」、またはチュートリアル「[Automate model building with AutoAI](/components/cloud-pak-for-data/tutorials/automate-model-building-with-autoai)」あるいは「[Build a predictive machine learning model quickly and easily with IBM SPSS Modeler](/components/cloud-pak-for-data/tutorials/build-an-ai-model-visually-with-spss-modeler-flow)」に進んでください。
