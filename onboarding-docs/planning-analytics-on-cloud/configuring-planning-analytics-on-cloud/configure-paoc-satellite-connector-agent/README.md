# Satellite Connector Agent の構成

> 本ガイドは、2024年5月2日に公開された [Configure PAoC Satellite Connector Agent](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/07/02/configure-paoc-satellite-connector-agent) を基にしています。  
> その後の Planning Analytics on Cloud の更新により、ファイアウォールの設定、FTP/FTPeS 接続方式、メニューや操作手順などが変更されている場合があります。  
> ページの内容と操作が異なる場合は、**IBM の最新ドキュメントや公式ガイドラインを必ず確認**し、最新版に沿った対応を行ってください。

---

## データベースアクセス

- **ファイアウォールルール**：IBM Cloud への送信ポート 443 を許可する必要があります。  
- **特定のエンドポイント情報**： [SCA ネットワーク要件](https://cloud.ibm.com/docs/satellite?topic=satellite-understand-connectors#network-requirements) を参照してください。

---

## 背景

多くの場合、計画アプリケーションに必要なデータはデータベースから取得されます。たとえば、販売計画のための組織階層や、前年の実績データを今年の計画のベースとして使用するケースなどです。

これらのデータはフラットファイルとして Planning Analytics にアップロードすることも可能ですが、**データベースに直接接続することで以下の利点があります：**

- ファイルを抽出・転送・読み込む手間を省き、**常に最新のデータをオンデマンドで取得可能**
- SQLの`SELECT`文を修正するだけで済むため、**開発がより迅速**
- **「ドリルダウン（drill to detail）」が可能**  
  例：SKU（最下層）のレベルで計画を立てる必要がない場合でも、上位レベル（例：商品カテゴリ）で計画を行い、必要に応じて構成要素（SKUの詳細）を確認できる

---

## セキュアな接続手段

企業がインターネット経由でデータベースを完全に公開することは稀です。そのため、**セキュアかつ暗号化された方法**でデータベースにアクセスする必要があります。

Planning Analytics がODBC接続でデータベースにアクセスするための方法は次の2通りです：

1. クラウドデータベースが**暗号化ODBC接続を提供する場合**（例：DB2 on Cloud、AzureAD、Amazon Redshift など）  
2. データベースが**ファイアウォールの内側（オンプレミスまたはクラウド内）に存在する場合**、追加技術により安全なネットワークパスを確立する必要がある

### ポイント別対応

- **1の場合**：IBM サポートチームにチケットを発行。サポート対象DBであれば、必要な設定について顧客と連携し、**Satellite Connector は使用せず、直接接続**が作成される。
- **2の場合**：**Satellite Connector を使用**

---

## Satellite Connector の概要

**Satellite Connector Agent (SCA)** はオンプレミスにインストールされ、Planning Analytics on Cloud へ向けて送信接続を確立します。この接続は暗号化され、Planning Analytics はODBCコマンドを SCA 経由で対象データベースに送信します。

![Satellite Connector 全体構成図](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/bnUjPbtjQFamUvnWlhIG_SCA%20Diagram-L.jpeg)

**注意**：Satellite Connector は IBM の完全な独立技術であり、IBM Cloud アカウント内で利用可能です。Planning Analytics on Cloud では、その技術の一部（Agent）のみがサブスクリプションに組み込まれており、**サーバー側の構成に関するドキュメントは無視してください**。

---

## ライセンスと構成制限

- 各顧客には **1つのSatellite Connector** が提供されます（追加購入も可能）
- 1つのConnectorで **複数のPlanning Analytics on Cloud 環境（例：開発・本番）に対応可能**
- 最大 **6つのエージェント（高可用性用）をサポート**
- 最大 **35のエンドポイント（データベース接続）をサポート**

---

## インストール要件と準備

### Agent の設置方式

- **Windowsサービスとしてネイティブ実行** または **Dockerエージェントとして実行**
- 多くのクライアントがWindows環境を使用しているため、ここでは**Windowsネイティブ方式に焦点を当てます**

Dockerを使用する場合は、以下を参照してください：  
[Docker Desktop WSL 2 backend on Windows](https://docs.docker.com/desktop/wsl/)

### Windows Agent のハードウェア要件

- 1台以上のマシン（通常は仮想）にインストール
- OS: Windows 10以降 または Windows Server 2016以降
- CPU: 最低4コア、メモリ: 最低4GB
- マシンは対象データベースへのネットワーク経路が必要、ポート443でインターネット接続可能であること

---

### その他の構成制限

- デフォルトで1つのSatellite Connectorが開発・本番を含むすべての環境をカバー
- 例：開発環境では開発用DB、本番環境では本番DBを使用するなど、同一Connector内でエンドポイントを分けられる
- **2つのWindows Agentは同一マシン上で共存できない**（サービスとして動作するため）

※ バージョン1.2.0以降、この制限は緩和され、同一マシンに複数エージェントの設置が可能になっていますが、これは高可用性構成（HA）には寄与しません。

---

### 高可用性（HA）構成について

- 通常、**1つのConnectorに対し3台のマシンにエージェントを分散配置**することが推奨されます
- 代替手段として、**Dockerコンテナを使用し、1台のマシンで複数エージェントを実行する構成**も可能です

---

## ネットワーク構成とファイアウォール

- 各エージェントマシンは対象の内部DB/クラウドDBへのネットワークルートを持つ必要があります
- **インターネットへの送信（ポート443）**が必要です

### ファイアウォール構成に関する注意

- 送信先を制限している場合、**FQDN（完全修飾ドメイン名）での許可を推奨**（IPアドレスは変更される可能性があるため）

ネットワーク要件およびエンドポイント一覧は以下参照：  
[ネットワーク要件](https://cloud.ibm.com/docs/satellite?topic=satellite-understand-connectors#network-requirements)

---

## データセンター対応マッピング

| Planning Analytics on Cloud データセンター | 対応 Satellite Connector データセンター |
|-------------------------------------------|----------------------------------------|
| Amsterdam, Netherlands                    | Frankfurt, Germany                     |
| Frankfurt, Germany                        | Frankfurt, Germany                     |
| Sydney, Australia                         | Singapore                              |
| Montreal, Canada                          | Toronto, Canada                        |
| Washington DC, USA                        | Washington DC, USA                     |
| San Jose, California, USA                 | Dallas, Texas, USA                     |

## ステップ1：Planning Analytics Workspace に Satellite Connector を定義する

Satellite Connector を使用するための最初のステップは、**Planning Analytics Workspace（PAW）内にコネクターを定義すること**です。

### 1. 「Administration」タイルを選択する

まず、Planning Analytics Workspace にログインし、**「Administration（管理）」タイル**をクリックします。

![Administration タイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/Owl8QrMQbqVXp5n0EP0R_Admin%20tile.jpeg)

---

### 2. 「Satellite Connector」タイルを選択する

次に、左側メニューまたはタイルの中から、**「Satellite Connector」タイル**をクリックします。

![Satellite Connector タイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/krGMzToRQaWtOggF1v2C_SatelliteConnectorTile.jpeg)

---

### 3. 「Create connector」を選択する

Satellite Connector の管理画面が開いたら、画面上の **「Create connector（コネクター作成）」ボタン**をクリックします。

![Create connector ボタン](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/uhAheabLQxGs3RhYJ6qI_CreateConnector.jpeg)

---

### 4. コネクター名を入力して作成

コネクターにわかりやすい名前を付けます（例：「London」「Head Office」など、エージェントをインストールする場所に基づいた名称）。  
名前を入力したら、**「Create」ボタンをクリック**します。

![コネクター名の入力](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/4ioYzseOTwi4i3srVJpu_Name%20Connector.jpeg)

---

### 5. コネクターの詳細を確認

作成した Satellite Connector はリストに表示され、**コネクターの場所や現在のステータスなどの詳細情報**が確認できます。

![コネクターの詳細画面](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/R2mfmGAjTgyjCldBAr0S_Connector%20details.jpeg)

## ステップ2：クライアント、構成ファイル、アクセストークンのダウンロード

Satellite Connector を作成した後は、**エージェントのインストーラー、構成ファイル、および API アクセスキー**をダウンロードします。

---

### 1. 「Connector Agents」タブを開く

Planning Analytics Workspace の左側で、先ほど作成した Satellite Connector を選択します。  
次に、画面右側の **「Connector Agents」タブ** をクリックします。

![Connector Agents タブ](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/j1deofapQHCBNzQPL18U_Connector%20Agents.jpeg)

---

### 2. Windows エージェント、構成ファイル、API キーを順にダウンロード

この画面から、以下3つのファイルをそれぞれダウンロードします：

1. Windows エージェント インストーラー  
2. 構成ファイル（Config）  
3. API アクセスキー（JSON）

**「Download connector agent」** ボタンをクリックして、Windows エージェントを取得します。

![ファイルのダウンロード画面](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/7QteYJSSRaqFaPaO0C0T_Download%20files.jpeg)

---

### 3. Docker イメージを選ぶことも可能

このドキュメントでは Windows のインストールにフォーカスしていますが、**Docker イメージを取得することも可能です**。

詳しくは以下を参照してください：  
[Installing the Docker agent](https://cloud.ibm.com/docs/satellite?topic=satellite-run-agent-locally)

![Docker または Windows 選択肢](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/008Ex9mMTmeloQ6pqBVN_Docker%20or%20Windows.jpeg)

---

### 4. インストーラーのダウンロード確認

Windows インストーラーを選択すると、ファイルのダウンロードが開始されます。

![インストーラーのダウンロード中](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/sDx4CM2aTQqjQ9J4lQe7_downloading.jpeg)

---

### 5. 構成ファイルと API キーの取得

Windows を選択し、必要に応じてタグを付けて構成ファイル（agent configuration file）をダウンロードします。

![構成ファイルのダウンロード](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/plUJjlqETI6aUzuohzNE_Configuration%20file.jpeg)

---

最後に、API キー（access key）もダウンロードしてください。  
このキーはエージェントが Planning Analytics 環境に接続するために必要です。

## ステップ3：エージェントのインストールと構成（構成ファイル・アクセストークンを使用）

### 1. ZIPファイルのブロック解除

Satellite Connector Agent のインストールを開始する前に、インストーラーZIPファイルを適切な場所に**展開**する必要があります。

Windows では、ダウンロードされたファイルがブロックされていることがあるため、**ZIPファイルを右クリック →「プロパティ」→「ブロック解除」** を確認してください。

![ブロック解除](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/JQAYkImcTBSokJIysk3w_Unblock%20before%20extract.jpeg)

---

### 2. ファイルの展開

すべてのファイルをインストール先のディレクトリ（例：`C:\sat-win-client`）に展開します。  
展開先のフォルダは任意に指定可能です。

![インストーラーの展開](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/ieXf8Q86SeWeNhUzz5FY_ExtractInstaller.jpeg)

---

### 3. 構成ファイルの編集

Planning Analytics 管理画面からダウンロードした `config.json` を開き、以下の項目を正しく設定します：

- `SATELLITE_CONNECTOR_IAM_APIKEY` のパスを、展開したインストーラーの場所に設定する

> 注意：Windows パスの `\` はエスケープ文字として `\\` にする必要があります（例：`C:\\sat-win-client`）

![構成ファイルの編集](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/1VjCVIulTKGhzT4glb6V_Edit%20Config%20file.jpeg)

![APIキーのパス指定](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/Wy9oNtmT1WHl3hDSOY0Q_update%20path%20to%20the%20api%20key.jpeg)

---

### 4. 構成ファイルとAPIキーをインストーラーフォルダに配置

編集した `config.json` とダウンロード済みの `apikey.json` を、インストーラーを展開したフォルダ（例：`C:\sat-win-client`）のルートにコピーします。  
上書き確認が表示された場合は「はい」を選択してください。

![構成ファイルの上書き](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/oAqKHaSsSOWytv3fm46S_replace%20config%20file.jpeg)

---

### 5. PowerShell でインストーラーを実行

管理者権限で **PowerShell** を起動し、展開フォルダに移動して `.\install` を実行します。

![PowerShell を開く](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/dMUhXvc1TpqXcSUKHxdn_open%20powershell.jpeg)

![インストーラーの実行](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/j0ER8IsYT1qya8XwozrQ_change%20dir%20and%20install.jpeg)

インストール中に「このデバイスに変更を加えますか？」というポップアップが表示された場合は、「はい」を選択します。

![デバイスの変更確認](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/Xs9DA8nnQ3S4s1y3qXKc_Allow%20changes%20to%20device.jpeg)

---

### 6. インストールの確認

インストールが完了すると、Windowsサービスに「Satellite Connector」が追加されており、実行中であることを確認できます。

![サービスの確認](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/lv1cwL7SPWKi2iSFBJrg_You%20can%20check%20service%20is%20running.jpeg)

Planning Analytics の管理画面に戻り、Satellite Connector のステータスが「Online」と表示されていれば成功です。

![オンライン確認](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/HvGmcwt9TjGbGwoEbZNl_Online%20view-L.jpeg)

---

## ステップ4：ODBC エンドポイントの作成と接続テスト

### 1. エンドポイントの作成

Satellite Connector の画面で「**Endpoints**」タブを開き、「**Create**」をクリックします。

![エンドポイントの作成](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/J0tNcmkRTjaPDT4BpJaH_create%20endpoint.jpeg)

必要なデータベース接続情報を入力します。

- Name：Planning Analytics で使用する ODBC 名（既存 TI プロセスと一致させると便利）
- Server host：データベースサーバのホスト名または IP アドレス
- Server port：ODBCポート（例：DB2は50000）
- ODBC driver：対象DBのドライバーを選択（追加が必要な場合はサポートに問い合わせ）
- Database name：対象のデータベース名

![エンドポイント入力フォーム](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/nz5yaxCrQMC9ViQFtpKS_Create%20Endpoint%20form.jpeg)

---

### 2. 接続テストの実行

作成したエンドポイントを選択し、メニューから「**Details**」を選択します。

![エンドポイントの詳細を開く](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/h4VXvUwhSSCNrj5bOCXQ_To%20test%20select%20details.jpeg)

ユーザー名とパスワードを入力して「Submit」をクリックすると、接続テストが実行されます。

![接続テストの送信](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/StzpIvNQeSZ1AdBgIJ0w_Test%20Connection.jpeg)

接続が成功すると、以下のようなメッセージが表示されます。

![接続成功メッセージ](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/jz12CeKDT4ylu2eOFFWL_Connection%20success%20message.jpeg)

---

## オプション：SQL 接続のテスト（Workbench使用）

より詳細なSQL接続テストを行いたい場合は、Planning Analytics Workbench を使用します。

### 1. Workbench を開く

画面左上のメニューから「New」→「Workbench」を選択します。

![Workbench を開く](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/HweIWq0eTpqBMOfWJtuS_open%20workbench.jpeg)

### 2. 新しいプロセスを作成

対象のデータベースを展開し、「Create Process」を選択します。

![プロセス作成](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/vTMjPgdwQlueq5NxXldH_Create%20process.jpeg)

任意のプロセス名を入力します。

![プロセス命名](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/Hxq6LfqWQEWekvyFiU5S_create%20test%20process.jpeg)

---

### 3. 接続テストを実行

1. データベース接続を選択  
2. 作成済みのODBC名を選択  
3. DBのユーザー名とパスワードを入力  
4. テーブルに対するSQLクエリを記述  
5. 「Preview」をクリック

![データプレビューの確認](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/XcqoUzX6RZ6ErcI7GRd0_preview%20data.jpeg)

---

以上で Satellite Connector Agent のインストールと ODBC 経由での接続テストの手順は完了です。  
さらなる詳細は IBM の公式ドキュメントをご参照ください：  
[Administer Satellite Connector - IBM Docs](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=workspace-administer-satellite-connector-cloud-only)
