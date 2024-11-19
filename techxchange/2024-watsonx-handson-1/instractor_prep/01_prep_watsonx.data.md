# インストラクター用　watsonx.dataの事前準備

当日ハンズオンをスムーズに進行させるために、watsonx.dataの初期設定、Milvusの作成を事前に行います。

## 1. Instructor URLにアクセス
Instructor URLはメールか、　TechzoneのMy workshopsメニューから取得してください。

## 2. 担当のIDのIBM Cloud LoginのURL, Username, Passwordを使ってIBM Cloudにログイン
Environmentsセクションの　担当番号のセクションを開き、そこに書いてあるIBM Cloud LoginのURL,　Username, Passwordを使ってIBM Cloudにログインします。<br>
尚、自分のIBMIDでのIBM SSOログインと混ざらないように、シークレットウィンドウ(プライベートウィンドウ)を推奨します。
<br>

<img width="800" alt="" src="images/i01-02.jpg">
<img width="800" alt="" src="images/01_2-5.jpg"><br>


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
以下、デフォルトのまま全て「次へ」をクリックします(6まで):<br>
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
6. <br>
<img width="800" alt="" src="images/wxd06.jpg"><br>
&nbsp;<br>

最後に「終了して移動」をクリックします。<br>
初期設定が終わるまで約12分ほど待ちます。<br>
この間ブラウザーの画面は表示したままにしておきます。初期設定が終わるまでログアウトもしないでください。<br>
<img width="800" alt="" src="images/wxd06-1.jpg"><br>
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
**Services**の下の「Milvus」をクリックします。<br>
<img  width="800" src="images/wxd10.jpg"><br>
&nbsp;<br>
「次へ」をクリックします。<br>
<img  width="800" src="images/wxd11.jpg"><br>
&nbsp;<br>

一般情報の画面が表示されます。<br>
表示名に`Milvus`を入力し、その他はデフォルトのままで、「作成」をクリックします。<br>
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

### 8. Milvusサービスに権限追加
「Milvus」アイコンをクリックします。サービスの詳細が表示されます。<br>
「アクセス制御タブ」をクリックし、「アクセス権限の追加」をクリックします。
<img  width="800" src="images/milvus02.jpg"><br>
&nbsp;<br>

最初にIBM Cloud LoginのURL,　Username, Passwordを取得したのと同じ担当番号のセクション中の下の方にある、`IBM Cloud Service ID`の値を取得します。<br>
<img  width="800" src="images/i_IBMCloud_serviceid.jpg"><br>
&nbsp;<br>


検索窓にその`IBM Cloud Service ID`の値を入力し、検索します。<br>
その後表示されたGroupにチェックを入れ、役割を「管理者」にセットし、「追加」をクリックします。<br>
<img  width="800" src="images/milvus03.jpg"><br>
&nbsp;<br>

「アクセス制御」に追加したグループの権限が正しく表示されているのを確認します。
<img  width="800" src="images/milvus04.jpg"><br>
&nbsp;<br>


Milvsの設定はこれで完了です。


