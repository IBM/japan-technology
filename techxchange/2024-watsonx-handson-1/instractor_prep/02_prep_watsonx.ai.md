# インストラクター用　watsonx.aiの事前準備

当日ハンズオンをスムーズに進行させるために、watsonx.dataの初期設定、Milvusの作成を事前に行います。

## 1. Instructor URLにアクセス
Instructor URLはメールか、　TechzoneのMy workshopsメニューから取得してください。

## 2. 担当のIDのIBM Cloud LoginのURL, Username, Passwordを使ってIBM Cloudにログイン
Environmentsセクションの　担当番号のセクションを開き、そこに書いてあるIBM Cloud LoginのURL,　Username, Passwordを使ってIBM Cloudにログインします。<br>
<img width="800" alt="" src="images/i01-02.jpg">
<img width="800" alt="" src="images/01_2-5.jpg"><br>


## 3. リソースリストを表示
左上のナビゲーション・メニューをクリック後、「リソース・リスト」をクリックし、IBM Cloudのリソース・リストを開きます。<br>
<img alt="" src="../images/resource_list_01.jpg"><br>
<img alt="" src="../images/resource_list_02.jpg"><br>


### 4. watsonx.aiのリソースの表示
リソース・リストから[AI/機械学習]のグループを見つけて、その中に含まれている Watson Studio のサービスを見つけて、表示されている名前をクリックします。<br>
<img width="800" alt="" src="images/wxa02.jpg"><br>
&nbsp;<br>

### 5. watsonx.aiのトップページの表示
watsonx.Studioのリソースが表示されるので、[Launch in][v]の[v]をクリックして、表示されたメニューから[watsonx]を選びます。<br>
<img width="800" alt="" src="images/wxa03.jpg"><br>
&nbsp;<br>

以下の画面が表示されますが、何もしないでしばらく待ちます。<br>
<img width="800" alt="" src="images/wxa04.jpg"><br>
&nbsp;<br>

しばらくすると以下の画面に変わるので、「続行」をクリックします。<br>
<img width="800" alt="" src="images/wxa05.jpg"><br>
&nbsp;<br>

watsonx.aiのトップページが開きます。「watsonxへようこそ」というウィンドウが表示された場合は右上の[X]をクリックして閉じてください。<br>
<img width="800" alt="" src="images/wxa06.jpg"><br>
&nbsp;<br>

「さらに詳しくみる」というウィンドウが表示された場合は右上の[X]をクリックして閉じてください。<br>
<img width="800" alt="" src="images/wxa06-1.jpg"><br>
&nbsp;<br>

### 6. サンドボックス・プロジェクトを開く
今回使用するサンドボックス・プロジェクトは最初のwatson.ai利用時に自動的に作成されるプロジェクトです。<br>
トップページ表示直後はしばらく作成中となりますが、1〜2分で作成されます。<br>
プロジェクトが、下記のような表示になったら`notsetのサンドボックス`(`notset`は違う文字列になる可能性があります)をクリックします。<br>
<img width="800" alt="" src="images/wxa07.jpg"><br>
&nbsp;<br>



### 7. サンドボックス・プロジェクトに権限付与
「管理」タブをクリックします<br>
<img width="800" alt="" src="images/wxa08.jpg"><br>
&nbsp;<br>
左のメニューから「アクセス制御」をクリックします<br>
<img width="800" alt="" src="images/wxa09.jpg"><br>
&nbsp;<br>
左のメニューから「コラボレーターの追加」をクリックします<br>
<img width="800" alt="" src="images/wxa10.jpg"><br>
&nbsp;<br>
「アクセスグループの.....」を選択します<br>
<img width="800" alt="" src="images/wxa11.jpg"><br>
&nbsp;<br>
最初にIBM Cloud LoginのURL,　Username, Passwordを取得したのと同じ担当番号のセクション中の下の方にある、`IBM Cloud Service ID`の値を取得します。<br>
<img  width="800" src="images/i_IBMCloud_serviceid.jpg"><br>
&nbsp;<br>


検索窓にその`IBM Cloud Service ID`の値を入力し、検索します。<br>
その後表示されたGroupにチェックを入れ、役割を「管理者」にセットします。<br>
<img width="800" alt="" src="images/wxa12.jpg"><br>
&nbsp;<br>
「追加」をクリックします。<br>
<img width="800" alt="" src="images/wxa13.jpg"><br>
&nbsp;<br>
「アクセス制御」のコラボレーターに追加したグループの権限が正しく表示されているのを確認します。
<img width="800" alt="" src="images/wxa14.jpg"><br>
&nbsp;<br>


watsonx.aiの設定はこれで完了です。<br>
別にUsernameの設定をする場合はwatsonx.ai、watson.data, IBM Cloudコンソール、全てログアウトしてから実行してください。


