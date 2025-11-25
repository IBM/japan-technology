# インストラクター用　watsonx.dataの事前準備

当日ハンズオンをスムーズに進行させるために、watsonx.dataの初期設定、Milvusの作成, 各種権限設定, Prestoスキーマ作成を事前に行います。

## 1. Instructor URLにアクセス
Techzoneの「My workshops」メニューから該当のWorkshopを開いてください。そこが Instructor URLです。
<img width="800" alt="" src="images/i01-01-1.jpg"><br>
<img width="800" alt="" src="images/i01-01-2.jpg"><br>
<p>
または該当のWorkshopを開いて表示された「Instructor URL」となります(クリックすると同じ画面になります)
<img width="800" alt="" src="images/i01-01-3.jpg"><br>


## 2. 担当のIDのログインURL, Username, Passwordを使ってIBM Cloudにログイン
Environmentsセクションの　担当番号のセクションを開きます。<br>

### ログインURL
`App ID Instructions`の中に記載されているURLがログインURLです。上の方に表示されている`IBM Cloud Login URL`ではありませんのでご注意ください。<br>

以下のような文章が表示されいるので、この中に記載されている`https://` から始まるURLがログインURLとなります。
<img width="800" alt="" src="../images/01_2-loginurl.jpg"><br>
&nbsp;<br>
`App ID Instructions`の中のURLをクリップボードにコピーして、WebブラウザーのURL入力フィールドにペーストしてログインURLにアクセスしてください。

### Username, Password
`App ID User Credentials`にあります。上の方に表示されている`IBM Cloud Username (your email)`および`IBM Cloud Password (user must provide their own)`ではありませんのでご注意ください。<br>
最初の`@techzone.ibm.com`で終わる文字列がUsername, スペースの後の2番目の文字列がPasswordです。<br>
ログインURLにアクセスして表示されたページのフォームにそれぞれコピーして入力してください。<br>
<img width="500" alt="" src="../images/01_2-username_pw.jpg"><br>



### ログインURLをブラウザーで開き,　Username, Passwordを使ってIBM Cloudにログインします。<br>
尚、自分のIBMIDでのIBM SSOログインと混ざらないように、シークレットウィンドウ(プライベートウィンドウ)を推奨します。
<br>
<img width="800" alt="" src="images/01_2-5.jpg"><br>
&nbsp;<br>

ログイン後、念の為アカウントが該当のWorkshop環境の`Assigned IBM Cloud account`と同じであることを確認してください:<br>
<img width="300" alt="" src="images/Assigned_IBM_Cloud_account.jpg"><br>
&nbsp;<br>
<img width="800" alt="" src="images/Dashboard_IBM_Cloud_account.jpg"><br>
&nbsp;<br>


## 3. リソースリストを表示
左上のナビゲーション・メニューをクリック後、「リソース・リスト」をクリックし、IBM Cloudのリソース・リストを開きます。<br>
<img alt="" src="../images/resource_list_01.jpg"><br>
<img alt="" src="../images/resource_list_02.jpg"><br>



### 4. watsonx.dataのリソースの表示
リソース・リストから[データベース]のグループを見つけて、その中に含まれている watsonx.data のサービスを見つけて、表示されている名前をクリックします。<br>
<img width="800" alt="" src="../images/watsonx.data_01.jpg"><br>


### 5. watsonx.dataのコンソールの表示
watsonx.dataのリソースが表示されるので、「Webコンソールを開く」をクリックします
<img width="800" alt="" src="../images/watsonx.data_02.jpg"><br>
&nbsp;<br>



### 6. watsonx.dataの初期設定実施
以下、デフォルトのまま全て「次へ」をクリックします(5まで):<br>
1.<br>
<img width="800" alt="" src="images/wxd01.jpg"><br>
&nbsp;<br>
2.<br>
<img width="800" alt="" src="images/wxd02.jpg"><br>
&nbsp;<br>
3. <br>
<img width="800" alt="" src="images/wxd03.jpg"><br>
&nbsp;<br>
4. <br>
<img width="800" alt="" src="images/wxd04.jpg"><br>
&nbsp;<br>
5. <br>
<img width="800" alt="" src="images/wxd05.jpg"><br>
&nbsp;<br>


最後に「終了して移動」をクリックします。<br>
初期設定が終わるまで約20分ほど待ちます。<br>
この間ブラウザーの画面は表示したままにしておきます。初期設定が終わるまでログアウトもしないでください。<br>
<img width="800" alt="" src="images/wxd06.jpg"><br>
&nbsp;<br>

初期設定が終わると、watsonx.dataのダッシュボードが表示されます。<br>
<img width="800" alt="" src="images/wxd07.jpg"><br>
&nbsp;<br>

### 7. Milvusサービスの作成
左上のグローバル・ナビゲーションをクリック後、「インフラストラクチャー・マネージャー」をクリックし、インフラストラクチャー・マネージャーを開きます。<br>
<img  src="../images/watsonx.data_navimenu.jpg"><br>
&nbsp;<br>
<img  src="../images/watsonx.data_navi_infra.jpg"><br>
&nbsp;<br>
&nbsp;<br>
インフラストラクチャー・マネージャーが表示されます。<br>
右上の「コンポーネントの追加」をクリックします。<br>
<img  width="800" src="images/wxd09.jpg"><br>
&nbsp;<br>
&nbsp;<br>
「コンポーネントの追加」画面が開きます。<br>
**サービス**の下の「Milvus」をクリックします。<br>
<img  width="800" src="images/wxd10.jpg"><br>
&nbsp;<br>
「次へ」をクリックします。<br>
<img  width="800" src="images/wxd11.jpg"><br>
&nbsp;<br>

一般情報の画面が表示されます。<br>
- 表示名に`Milvus`を入力
- ストレージのドロップダウンリストから`cos-bucket`を選択
- パスに`milvus`入力

その後、「作成」をクリックします。<br>
<img  width="800" src="images/wxd12.jpg"><br>
&nbsp;<br>

Milvusサービスのプロビジョンが開始されます。サービスが稼働するまで待ちます(8〜10分くらい)。<br>
<img  width="800" src="images/wxd13.jpg"><br>
&nbsp;<br>

以下のようにMilvusが表示されていtれば、Milvus稼働完了です<br>
<img  width="800" src="images/wxd14.jpg"><br>
&nbsp;<br>

Milvusの上にマウスを重ねると、「Milvus実行中」と表示されます。
<img  width="800" src="images/milvus01.jpg"><br>
&nbsp;<br>

### 8. Milvusサービスに権限追加 (プロビジョン中でも設定可能)
「Milvus」アイコンをクリックします。サービスの詳細が表示されます。<br>
「アクセス制御タブ」をクリックし、「アクセス権限の追加」をクリックします。
<img  width="800" src="images/milvus02.jpg"><br>
&nbsp;<br>

最初にIBM Cloud LoginのURL,　Username, Passwordを取得したのと同じ担当番号のEnvironment Infoのある、`Access group name`の値を取得します。<br>
<img  width="800" src="images/i_IBMCloud_groupname.jpg"><br>
&nbsp;<br>


検索窓にその`Access group name`の値を入力し、検索します。(最初の数文字(例:`eid`)のみでも出てきます)<br>
その後表示されたGroupにチェックを入れ、役割を「管理者」にセットし、「追加」をクリックします。<br>
<img  width="800" src="images/milvus03.jpg"><br>
&nbsp;<br>

「アクセス制御」に追加したグループの権限が正しく表示されているのを確認します。
<img  width="800" src="images/milvus04.jpg"><br>
&nbsp;<br>


Milvusの設定はこれで完了です。右上の「X」をクリックしてMilvusの画面を閉じてください。

### 9. starterエンジンにアクセス権の追加
「starter」アイコンをクリックします。エンジンの詳細が表示されます。<br>
「アクセス制御タブ」をクリックし、「アクセス権限の追加」をクリックします。
<img  width="800" src="images/starter01.jpg"><br>
&nbsp;<br>

検索窓に8で使用した`Access group name`の値を入力し、検索します。(最初の数文字(例:`eid`)のみでも出てきます)<br>
その後表示されたGroupにチェックを入れ、役割を「管理者」にセットし、「追加」をクリックします。<br>
<img  width="800" src="images/starter02.jpg"><br>
&nbsp;<br>

「アクセス制御」に追加したグループの権限が正しく表示されているのを確認します。
<img  width="800" src="images/starter03.jpg"><br>
&nbsp;<br>


starterエンジンの設定はこれで完了です。右上の「X」をクリックしてstarterの画面を閉じてください。

### 10. iceberg_dataカタログにアクセス権の追加 (プロビジョン中でも設定可能)
「iceberg_data」(表示は「iceberg_d...」)アイコンをクリックします。エンジンの詳細が表示されます。<br>
「アクセス制御タブ」をクリックし、「アクセス権限の追加」をクリックします。
<img  width="800" src="images/iceberg_data01.jpg"><br>
&nbsp;<br>

検索窓に8で使用した`Access group name`の値を入力し、検索します。(最初の数文字(例:`eid`)のみでも出てきます)<br>
その後表示されたGroupにチェックを入れ、役割を「管理者」にセットし、「追加」をクリックします。<br>
<img  width="800" src="images/iceberg_data02.jpg"><br>
&nbsp;<br>

「アクセス制御」に追加したグループの権限が正しく表示されているのを確認します。
<img  width="800" src="images/iceberg_data03.jpg"><br>
&nbsp;<br>


iceberg_dataカタログの設定はこれで完了です。右上の「X」をクリックしてiceberg_dataの画面を閉じてください。



### 11. cos-bucketストレージにアクセス権の追加
「cos-bucket」アイコンをクリックします。ストレージの詳細が表示されます。<br>
「アクセス制御タブ」をクリックし、「アクセス権限の追加」をクリックします。
<img  width="800" src="images/cos-bucket01.jpg"><br>
&nbsp;<br>

検索窓に8で使用した`Access group name`の値を入力し、検索します。(最初の数文字(例:`eid`)のみでも出てきます)<br>
その後表示されたGroupにチェックを入れ、役割を「管理者」にセットし、「追加」をクリックします。<br>
<img  width="800" src="images/cos-bucket02.jpg"><br>
&nbsp;<br>

「アクセス制御」に追加したグループの権限が正しく表示されているのを確認します。
<img  width="800" src="images/cos-bucket03.jpg"><br>
&nbsp;<br>


cos-bucketストレージの設定はこれで完了です。右上の「X」をクリックしてcos-bucketの画面を閉じてください。


### 12. iceberg_dataカタログにスキーマ作成
左上のグローバル・ナビゲーションをクリック後、「データ・マネージャー」をクリックし、データ・マネージャーを開きます。<br>
<img  src="../images/watsonx.data_navimenu.jpg"><br>
&nbsp;<br>
<img  src="../images/watsonx.data_navi_datamgr.jpg"><br>
&nbsp;<br>
&nbsp;<br>
データ・マネージャーが表示されます。<br>
左側の「関連付けられたカタログ」の下の「iceberg_data」にマウスを乗せると、右側にアクションメニュー「︙」が表示されるので、クリックします。<br>
「スキーマの作成」メニューが表示されるので、クリックします。<br>
<img  src="images/datamgr01.jpg"><br>
&nbsp;<br>

「スキーマの作成」が表示されます。<br>
名前に`invoice_schema`と入力し、「作成」をクリックします。<br>
<img  src="images/datamgr02.jpg"><br>
&nbsp;<br>
左側の「関連付けられたカタログ」の下の「iceberg_data」の下に「invoice_schema」スキーマが表示されていることを確認します。
<img  src="images/datamgr03.jpg"><br>
&nbsp;<br>

 watsonx.dataでの初期設定は以上です。<br>
 後で使うので、 watsonx.dataの画面は閉じないでおいてください。

  02: [インストラクター用　watsonx.data Premiumの事前準備](02_prep_watsonx.data_premium.md) に進んでください。