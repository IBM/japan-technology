# プロビジョニング

プロビジョニングフェーズでは、以下の流れとなります。

1. [IBM Cloudログイン](../../watsonx-ai/01_instance/01_ibmcloud_login/)
2. [サブスクリプションコードの適用](../../watsonx-ai/01_instance/02_subscription_code/)
3. [リソース・グループの作成](../../watsonx-ai/01_instance/03_resource_group/)
4. 各種インスタンスの作成
    - IBM Cloud Object Storage の作成
    - watsonx.ai Runtime（Watson Machine Learning）の作成
    - watsonx.ai Studio の作成
    - watsonx.governance の作成
    - watsonx.governance Openscale のセットアップ
5. [アクセス・グループの作成と権限設定](../../watsonx-ai/01_instance/05_access_group/)
    - リソース・グループ
    - 使用額参照
6. [アクセス・グループへのユーザー追加](../../watsonx-ai/01_instance/06_access_group_user/)


## watsonx.ai Studio

1. 画面上の検索ボタンをクリックする
![](./images/ws1.png)

2. 表示された入力欄に **watsonx.ai Studio** と入力し、数秒後に表示される **カタログ結果** 欄の **watsonx.ai Studio** をクリックする
![](./images/ws2.png)


3. 作成するインスタンスの条件を指定する
   
   1. **ロケーションの選択** セクションで、使用するリージョンを選択する
      
      1. ダラスの場合  
      **ダラス (us-south)** を選択する
      ![](./images/ws3.png)
 
      1. 東京の場合  
      **東京 (jp-tok)** を選択する
      ![](./images/ws4.png)
    
    1. **料金プランの選択** セクションで、 **Professional** を選択する
    ![](./images/ws5.png)
    
    1. **リソースの構成** セクションで、サービス名に **watsonx.ai Studio-XXXXX** を入力(XXXXXは任意の文字列)、リソース・グループの選択で前で作成した **RG_XXXXX** を選択する。タグは空欄でOK
    ![](./images/ws6.png)

4. 画面右の要約欄で **以下のご使用条件を読み、同意します｡** にチェックを入れ、**作成** ボタンをクリックする
![](./images/ws7.png)

5. 作成した **watsonx.ai Studio** の詳細画面に自動的に遷移したら完了
![](./images/ws8.png)


## watsonx.ai Runtime (Watson Machine Learning)

1. 画面上の検索ボタンをクリックする
![](./images/wr1.png)

2. 表示された入力欄に **watsonx.ai Runtime** と入力し、数秒後に表示される **カタログ結果** 欄の **watsonx.ai Runtime** をクリックする
![](./images/wr2.png)

3. 作成するインスタンスの条件を指定する

    1. **ロケーションの選択** セクションで、使用するリージョンを選択する

        - ダラスの場合   
        **ダラス (us-south)** を選択する
        ![](./images/wr3.png)

        - 東京の場合   
        **東京 (jp-tok)** を選択する
        ![](./images/wr4.png)

    2. **料金プランの選択** セクションで、使用するプランを選択する

        - Essentials の場合   
        **Essentials** を選択する
        ![](./images/wr5.png)

        - Standard の場合   
        **Standard** を選択する
        ![](./images/wr6.png)

    3. **リソースの構成** セクションで、サービス名に **Watson Machine Learning-XXXXX** を入力(XXXXXは任意の文字列)、リソース・グループの選択で前で作成した **RG_XXXXX** を選択する。タグは空欄でOK
    ![](./images/wr7.png)

4. 画面右の要約欄で **以下のご使用条件を読み、同意します｡** にチェックを入れ、**作成** ボタンをクリックする
![](./images/wr8.png)

5. 作成した **watsonx.ai Runtime** の詳細画面に自動的に遷移したら完了
![](./images/wr9.png)


## Cloud Object Storage

1. **起動** セクションで **IBM watsonx** をクリックする
![](./images/cos1.png) 

2. 新たに表示されたwatsonxタブを選択し、右上の「×」ボタンをクリックする
![](./images/cos2.png) 

3. **さらに詳しくみる** のポップアップが出てくるので、右上の「×」ボタンをクリックする
![](./images/cos3.png) 

4. 作業用のプロジェクトを作成するために、左上のハンバーガーメニューをクリックする
![](./images/cos4.png) 

5. **プロジェクト** セクションで **すべてのプロジェクトの表示** を選択する
![](./images/cos5.png) 

6. **新規プロジェクト +** をクリックする
![](./images/cos6.png) 


## watsonx.governance
1. 画面上の検索ボタンをクリックする

2. 表示された入力欄に **watsonx.gov** と入力し、数秒後に表示される **カタログ結果** 欄の **watsonx.governance** をクリックする
![](./images/wxgov.png)


3. 作成するインスタンスの条件を指定する
   
   1. **ロケーションの選択** セクションで、使用するリージョンを選択する
      
      1. ダラスの場合  
      **ダラス (us-south)** を選択する
 
    2. **料金プランの選択** セクションで、 **基本情報** を選択する
    
    3. **サービス名** セクションで、サービス名に **watsonx.governance-XXXXX** を入力(XXXXXは任意の文字列)、リソース・グループの選択で前で作成した **RG_XXXXX** を選択する。タグは空欄でOK
![](./images/wxgov2.png)

4. 画面右の要約欄で **以下のご使用条件を読み、同意します｡** にチェックを入れ、**作成** ボタンをクリックする
![](./images/wxgov3.png)

5. 作成した **watsonx.governance** の詳細画面に自動的に遷移したら完了

## watsonx.governance　OpenScale
1. リソースリストから作成したwatsonx.governance を選択
![](./images/openscale.png)

2. ドロップダウンリストから「Watson OpenScaleで起動」を選択
![](./images/openscale2.png)

3. 「自動セットアップ」をクリック (＊数十分かかります)
![](./images/openscale3.png)

