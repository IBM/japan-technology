# IBMidの作成方法

> 本ガイドは、2024年7月3日に公開された [Creating an IBMid](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/07/03/creating-an-ibmid)記事に基づいて作成されています。  
> しかし、Planning Analytics on Cloud 環境は継続的にアップデートされていますので、サポートプロセス、UI 表示、チケット作成時の操作フローなどが現状と異なる可能性があります。  
> 操作がガイドと一致しない場合は、**IBM の最新ドキュメントやサポートポータルを必ずご確認**のうえ、最新情報に基づいてご対応ください。

IBM Planning Analytics では、ユーザー認証に IBMid が利用されます。  
IBMid は IBMid 対応のすべてのアプリケーションで使用され、以下の2つの形態があります。

- IBM 管理型：IBM が一元管理するユーザーIDとパスワードのディレクトリ
- エンタープライズフェデレーション型：AzureAD、PingFederate、OKTA、ADFS などの外部Idプロバイダーによってユーザー認証を行う方式（IBMidのフェデレーションについては[こちら](../)を参照してください）

もし貴社がまだエンタープライズフェデレーションを利用していない場合、またはユーザーがIBMidを持っていない場合は、新規にIBMidを作成する必要があります。

---

## IBMidの作成手順

1. ログイン画面から作成  
   Planning Analytics にアクセスするとログインページが表示されます。  
   画面下部の「Create an IBMid（IBMidを作成）」をクリックしてください。  

   ![IBMid ログイン画面](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/8pmBqa2EQR6spBiOogY3_IBMidLogin-M.jpeg)

   あるいは、[IBMid作成ページ](https://www.ibm.com/account/reg/us-en/signup?formid=urx-19776)に直接アクセスして作成することも可能です。

2. フォーム入力  
   必要事項を入力し、任意のパスワードを設定します。  
   パスワードを忘れた場合は、[パスワードリセットページ](https://www.ibm.com/account/reg/us-en/reset-password)から再設定できます。  

   ![IBMid 登録フォーム](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/wpKtQ26nTPaFnmKm0V3x_IBMid%20Form-L.jpeg)

3. メール認証  
   入力完了後「次へ」を押すと、登録したメールアドレスに認証コードが送信されます。  
   メールが届かない場合は、迷惑メールフォルダを確認するか、メール管理者に問い合わせてください。  
   メールは ibmacct@iam.ibm.com から送信されます。  

   ![IBMid メール認証](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/uh68JvRZGPHw6gaCf8mA_IBMid%20Verify-L.jpeg)

4. 利用開始  
   認証が完了すると、登録したメールアドレスとパスワードで Planning Analytics にログインできるようになります（招待を受けている場合に限ります）。  
   サインアップの際には、以下の2種類のメール（認証メールを除く）が届きます。  
   - 新規ユーザー登録コード  
   - 登録完了通知  

   なお、アカウントにはデフォルトで多要素認証（MFA）が有効になります。  

---

## エンタープライズフェデレーションを利用している場合

すでに組織が IBMid エンタープライズフェデレーションを導入している場合は、新規作成は不要です。  
自分のメールアドレスを入力して組織のログインページから認証すれば、自動的にIBMidアカウントがプロビジョニングされます。  

詳細は [IBMid Enterprise Federationの設定方法](../) を参照してください。