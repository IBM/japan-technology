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

手順1: ブラウザーから、次のURLを開きます。IBM IDは、IBM社員の場合はw3 ID、パートナー様の場合は、IBM Technology Zoneアクセスに登録済みのIBM IDを使ってください。

https://techzone.ibm.com/my/reservations/create/6810e845d4c668424c04f121

手順2: IBM Technology Zone Terms and Condtionsが表示された場合、内容を確認し、

☑️ I have read and accept the terms and conditions.

にチェックを入れます。

<img width="1060" height="976" alt="AcceptTermsAndCondition" src="https://github.com/user-attachments/assets/8b783c37-accf-4290-b703-c67334d62e34" />

手順3: Welcome to IBM Technology Zone! Tell us about yourself. と表示された場合、[Skip for now]をクリックします。
<img width="1060" height="976" alt="TellusAboutYourself" src="https://github.com/user-attachments/assets/17c6da1c-55fc-4219-add3-81175b902a05" />

手順4: Create a reservation のページから、[Request an environment]を選択します。
<img width="1060" height="976" alt="CreateAreservation" src="https://github.com/user-attachments/assets/43e79a1b-e9e7-47bd-9665-c1ab477f2167" />

手順5: 次のスクリーンショットを参考に必要事項を記入します。
* Purpose: [Education]
* Purpose description: To do AI Agent workshop
* Prefered Geography: [any - AP - jp-tok region -any datacenter]

<img width="1060" height="976" alt="FilloutReservation" src="https://github.com/user-attachments/assets/220afad1-b7a5-4a44-9afb-3c99b3956291" />

手順6: ☑️ I agree to IBM Technology Zone's Terms & Conditions and End User Security Policies. にチェックを入れて、[Submit]をクリックします。

手順7: IBM CloudとIBM Technology Zoneからのメールを確認します。
* Account: Action required: You are invited to join an account in IBM Cloud
IBM Technology Zoneで使っているIBM Cloud Enterprise アカウントへの招待メールとなります。
英文メール内の [Join Now]をクリックして、お使いのIBM IDでユーザーを登録します。

* Reservation Ready on IBM Technology Zone
IBM Technology Zoneの環境が準備できたことを通知するメールとなります。

手順8: IBM Cloudのリソースリストへアクセスし、[製品]列に[watsonx Orchestrate]が表示されている行を見つけます。その行をクリックします。
* URL: https://cloud.ibm.com/resources
* 画面の一番上の行にある、[管理]の右側に表示されているアカウント番号が、手順7で案内されたアカウントと一致していることを確認してください。
* 異なるアカウントが表示されている場合は、(？)マークの左にある[v]をクリックし、ドロップ・ダウン・メニューから適切なアカウントに切り替えてください。
<img width="1218" height="925" alt="CloudResources" src="https://github.com/user-attachments/assets/e8ab3788-c548-46a4-83e7-7fae07c416f3" />

手順9: [watsonx Orchestrateを起動]をクリックします。

<img width="1218" height="925" alt="Launchwxo" src="https://github.com/user-attachments/assets/5af1a1e1-9737-4e16-b7fc-e23847a60b76" />

手順10: watsonx Orchestrateの起動を確認します。https://us-south.watson-orchestrate.cloud.ibm.com/chat が開きます。
<img width="1218" height="925" alt="wxoIBMCloud" src="https://github.com/user-attachments/assets/d2b0ace3-8d68-4212-8ea8-789ac274707b" />






