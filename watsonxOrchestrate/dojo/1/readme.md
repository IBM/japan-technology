# watsonx Orchestrate 環境の準備

watsonx Orchestrateの環境をお持ちでない場合、次の方法の何れかを用いて、準備します。
* 30日無償評価版の登録
* IBM Technology Zoneを使った環境の作成 (IBM社員並びにIBM Partner Plus登録済みのパートナー様限定）
* IBM Cloudアカウントを使い、環境の作成（すでにIBM Cloudをお使いのお客様、パートナー様）

## 30日無償評価版の登録

手順1: 次のURLへアクセスして、30日無償評価版に登録
https://www.ibm.com/account/reg/jp-ja/signup?formid=urx-52753

手順2: 必須項目を入力します。
<img width="1221" height="1011" alt="wxoTrial-registration" src="https://github.com/user-attachments/assets/fa13b4b7-5b20-460e-9526-9c8e410d0eb3" />

手順3: お使いのメール環境を確認し、IBM Security (ibmacct@iam.ibm.com) から届いた「新規ユーザー登録」という件名のメールを開きます。メールの中に、7桁の確認コードがあるので、コピーしてください。

手順4: ブラウザーに戻り、[検証トークン]と書かれているところに、先ほどの7桁の確認コードを貼り付けて、[送信]をクリックします。
<img width="1326" height="1043" alt="wxo-ConfirmationCode" src="https://github.com/user-attachments/assets/f40074bf-e8a3-4e2b-8e02-cf6f81d6b6a0" />

手順5: 送信後、しばらくすると、[Deply your trial]と書かれたページが表示されます。[Deployment Region]と[インスタンス名]を次のように指定し、最後に[Create Trial Instance]をクリックします。
* Deployment region: Singapore (ap-southeast-1)
* インスタンス名: 任意の名前をつけます。他の人と名前が重複しないよう、年月日や色など命名を工夫してください。（重複しているかどうかの確認が取れません）

<img width="1326" height="1043" alt="DeployYourTrial" src="https://github.com/user-attachments/assets/9344cbba-5af3-4fe4-becb-1537bcd2b898" />

手順6: しばらく待つと、試用版環境が整います。[今すぐ試用版にアクセスする]をクリックして、ログイン画面に進みます。
<img width="1326" height="1043" alt="InstanceIsReady" src="https://github.com/user-attachments/assets/c8b2d396-8d61-4edd-bcb2-af108f60066c" />

ご注意：手順6で、ログイン画面がループする問題が発生した場合の対処方法について
IBM IDの認証強化に伴い、IBM IDに多要素認証を割り当てる必要があります。

お使いのメール環境を確認し、IBM SaaS (service@saas.ibm.com) から届いた「Welcome to your IBM watsonx Orchestrate trial!」という件名のメールを開きます。メールの中にある[Access trial]のリンクのアドレスをコピーします。

<img width="544" height="777" alt="emailfromIBMSaaS" src="https://github.com/user-attachments/assets/8970ab69-04ba-4b0c-b935-371f0c98067e" />

ブラウザーのプライベート・ウィンドウ、シークレット・ウィンドウ、またはInPrivateウィンドウを開き、コピーしたリンクを貼り付けます。リンクがhttp:で始まっているので、Google ChromeやMicrosoft Edgeの場合、「HTTPS とのセキュリティで保護された接続はサポートされていません」という警告が表示されますが、[サイトに進む]をクリックします。

<img width="1014" height="759" alt="SiteWarning" src="https://github.com/user-attachments/assets/2b11369f-07ac-498e-a35c-c30afd3578e3" />

watsonx Orchestrateのログイン画面が表示されますので、登録したIBM ID (Eメール・アドレス）とパスワードを使ってログインします。
<img width="1014" height="759" alt="wxoLogin" src="https://github.com/user-attachments/assets/a04fab94-97fe-4eea-ba60-c6d57874681e" />

もし、多要素認証の登録が表示された場合は、[Eメール]を選択して、次に進みます。

<img width="1115" height="951" alt="MultifactorAuth" src="https://github.com/user-attachments/assets/b552f1c7-7090-4185-b98f-a9e717d93f80" />

ログインが完了すると、https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat が開きます。

<img width="1060" height="976" alt="wxoChat" src="https://github.com/user-attachments/assets/d5581229-4e7a-479b-a0a5-7e79407cc0c7" />

## IBM Technology Zoneを使った環境の作成
IBM社員並びにIBM Partner Plus登録済みのパートナー様は、IBM Technology Zoneを利用できます。

Watsonx Orchestrate Trial/Standard
https://techzone.ibm.com/my/reservations/create/6810e845d4c668424c04f121

