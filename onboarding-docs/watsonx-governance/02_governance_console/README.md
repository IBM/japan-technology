# ガバナンス・コンソール

watsonx.governance をプロビジョニングする際、ガバナンスコンソールは自動的にプロビジョニングされることはできません。 

ガバナンスコンソールを使用するには、OpenPagesのインスタンスをプロビジョニングし、管理者が watsonx.governance のインスタンスと統合する必要があります。

ガバナンスコンソールのセットアップは以下の流れとなります。

1. ガバナンス・コンソール用サービスの作成

2. ガバナンス・コンソール統合設定準備

3. APIキーの取得

4. watsonx.governanceからOpenPagesへの接続

5. ガバナンス・コンソールサービス設定

6. ガバナンス・コンソール統合設定


## ガバナンス・コンソール用サービスの作成

1. IBM Cloudに管理者アカウントでログインします。アカウントの設定が今回利用するアカウントになっていることを確認します。アカウントが確認できたら [リソースの作成] をクリックします。
![](./images/instance.png)


2. 検索ダイアログに “OpenPages”と入力し、表示されたサービスをクリックします。2025年5月時点ではガバナンス・コンソールはIBM Cloudの“OpenPages”というサービスを用いて実現します。今後ガバナンス・コンソールもwatsonx.governanceに統合され、当手順は不要になる予定です。
![](./images/instance2.png)


3. サービス作成画面が表示されます。下記を参考に情報を入力します。

     - プラン：標準
     - サービス名：（任意の値）
     - AWS region：（任意の値）
     - Base currency：JPY
     - Sample data：Include(*)
     - Solutions (Select one)：Model Risk Governance
       ※ 上記以外はデフォルト値のまま

※サービスが立ち上がるまでに2〜3時間かかる可能性があります。

4. ご利用条件をご確認のうえ、[以下のご使用条件を読み、同意します。]にチェックを入れ、[作成] ボタンをクリックします。
![](./images/instance3.png)


## ガバナンス・コンソール統合設定準備
次に先程作成したOpenPagesサービスをガバナンス・コンソールとして使用するための設定を行います。
ガバナンス・コンソール統合設定を行うには、以下の権限が必要となります。

1. IBM Cloud API Key作成権限が必要

     - 【参考】[IBM Docs] 
     - https://cloud.ibm.com/docs/account?topic=account-manapikey
          
2. watsonx.governanceインスタンス管理者レベルのアクセス権限
     
     - IAMプラットフォーム管理権限（インベントリ作成に必要）
          - 【参考】[IBM Docs] ガバナンスのためのコラボレーション・ロール
          - https://www.ibm.com/docs/ja/watsonx/saas?topic=cases-collaboration-roles-governance
          
3. OpenPagesインスタンス管理者レベル、およびユーザー・レベルのアクセス権限

## APIキーの取得

1. watsonx.governanceに接続するためのAPIキーを取得します。
IBM Cloud にアクセスし [管理 ＞ アクセス（IAM）] をクリックします。
![](./images/api.png)

2. 左側メニューより [API キー] をクリックし、表示された画面で [作成] をクリックします。
![](./images/api2.png)

3. 任意の [名前] を入力し、[作成] をクリックします。
![](./images/api3.png)

5. 作成されると下記右側の画面が表示されますので、[コピー]してテキストファイル等で保存しておくか、[ダウンロード] しておきます。
ダウンロードしたファイルはJSON形式になっており、テキストエディタで中身を確認できます。
![](./images/api4.png)

## watsonx.governanceからOpenPagesへの接続
1. OpenPagesインスタンスへアクセスします。
インスタンス名は [ガバナンス・コンソール用サービスの作成] 手順で指定した名前となります。
OpenPagesインスタンスは [AI機械学習] の中に分類されています。
![](./images/service.png)

2. 左側メニューより [Environment] をクリックし、[固定URL] をコピーしテキストファイルなどで保存しておきます。※URLは後続の手順で使用します。
![](./images/service3.png)

3. 左側メニューより [Setting] をクリックし、[watsonx.governance 統合] 部分に先ほど作成したAPI キーを入力し、[接続のテスト] をクリックします。
接続に成功したら [保存] をクリックします。
![](./images/service2.png)

※ 以下の画面のように、IBM Cloud上のOpenPagesインスタンスページで左側メニュー [Setting]の [watsonx.governance 統合] 部分が表示されない場合、以下の手順を行います。
![](./images/option.png)

1. watsonx.governanceインスタンスへアクセスし、watsonx.governanceを起動します。
![](./images/connect.png)
![](./images/connect2.png)
2. Navigation Menu ナビゲーション・メニュー・アイコン and AI Governance > AI use casesをクリック。
![](./images/option2.png)
3. 「設定の管理」(歯車のアイコン) > 一般 > ガバナンスコンソールをクリックし、 セットアップをクリックします
![](./images/option3-0.png)
![](./images/option3.png)
    1. APIキーの取得と固定 URL のステップ2でコピーした URL と、 APIキーの取得と固定 URL のステップ1でコピーした API キーを入力してください。
    2. インベントリーを選択します。
        ※ ユーザーがユースケースを作成すると、このインベントリに作成されます。
        ※ 作業者の名前は自動的にデフォルトのオーナーとして表示されますが、別のユーザーを選択することもできます。 新しいユースケースは、デフォルトの所有者が所有します。
    4. 「適用」をクリックします。
        Governance Console (IBM OpenPages) 統合 が有効になります。
![](./images/option3-1.png)
4. 管理ページで、統合を有効にします。
![](./images/option4.png)

## ガバナンス・コンソールサービス設定

1. ガバナンス・コンソール側のユーザーのプロファイルを設定してきます。プロファイルはユーザーごとの表示設定で、今回はモデルリスク管理用のものを設定します。OpenPagesのURLをクリックします。
![](./images/service4.png)

2. 右上歯車メニューから [ユーザーとセキュリティ ＞ ユーザー] をクリックします。
![](./images/service5.png)

3. 表示されたユーザー一覧より、ガバナンス・コンソールへアクセス対象となるユーザーをクリックします。
検索欄にユーザー名を入力することで絞り込みもできます。
![](./images/service6.png)

4. [ロケールおよびプロファイル] セクションにて、[許可されたユーザー・プロファイル] に“watsonx-governance MRG Master” を選択します。続いて、[現在のプロファイル] に“watsonx-governance MRG Master”を選択し、[保存] をクリックします。他のユーザーも同様に設定します。
![](./images/service7.png)

5. Governance console で統合をセットアップします。まず、OpenPagesのURLをクリックし、Governance consoleを起動します。
    watsonx.governance MRG マスタープロファイルを使用していることを確認します。
![](./images/option5-1.png)
    管理メニュー > Integrations > watsonx.governance をクリックする。
![](./images/option5-2.png)
    「API キーと固定 URL 取得」 で作成した API キーを入力します。
![](./images/option5-3.png)
    接続をテストし、 Saveをクリックする。

## ガバナンス・コンソール統合設定

1. watsonx.governanceインスタンスへアクセスします。インスタンス名は作成時に指定した名前となります。
watsonx.governanceインスタンスは [AI機械学習] の中に分類されています。
![](./images/connect.png)

2. [watsonx.governanceで起動] をクリックします。
![](./images/connect2.png)

3. 左上メニューより、[AIガバナンス ＞ インベントリー] をクリックします。
![](./images/connect3.png)

4. [新規インベントリー] をクリックし、インベントリーを作成します。
![](./images/connect4.png)

任意の[名称] を設定し、[作成] をクリックします。
![](./images/connect4-1.png)

5. 左上メニューより、[AIガバナンス ＞ AIユース・ケース] をクリックします。
![](./images/connect5.png)

6. AIユースケース右横にある歯車マークをクリックすると、[管理画面] が表示されます。
![](./images/connect6.png)

7. [外部モデル・ガバナンス] のチェックを入れます。
![](./images/connect7.png)

[外部モデル・ガバナンスのセットアップ] 画面が表示されるのでさきほど作成したインベントリーとデフォルトの所有者を設定し、[適用] をクリックします。
![](./images/connect7-1.png)

9. [ガバナンス・コンソール（IBM OpenPages）の統合] のチェックを入れます。
[ガバナンス・コンソール統合のセットアップ] 画面が表示されるので、これまでの手順で取得・作成した情報を入力します。
![](./images/connect8.png)

10. 以下の情報を入力します。

    - デプロイメント・モード：スタンドアロン
    - URL：OpenPagesのURL
    - API キー：IBM CloudのAPI キー
    - 在庫：作成したインベントリーを選択
    - デフォルトの所有者：管理者を設定

入力したら [適用] をクリックします。
![](./images/connect9.png)

11. 管理画面で [IBM OpenPagesに移動] をクリックすると、ガバナンス・コンソール画面が開きます。
![](./images/connect10.png)
![](./images/connect10-1.png)

※ 上記すべての設定を行っても画面のバナーが「ガバナンス・コンソール」ではなく「OpenPages」に表示されている場合、以下の手順を行います。
1. IBM Cloud上のOpenPagesインスタンスへアクセスします。
インスタンス名は [ガバナンス・コンソール用サービスの作成] 手順で指定した名前となります。
OpenPagesインスタンスは [AI機械学習] の中に分類されています。
![](./images/service.png)

2. 左側メニューより [Settings] をクリックし、[Service Instance Branding] のセクションでwatsonx.governance欄にOnへ切り替えます。
![](./images/brand.png)

以上で、ガバナンス・コンソール統合設定を完了しました。
