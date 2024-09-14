# watsonx.aiの起動 (IBM Cloudコンソール)
このパートでは、次の操作を学びます。
* watsonx.aiの起動

参考URL: IBM watsonx as a Service の資料

https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/welcome-main.html?context=wx&audience=wdp

このページの手順を正しく実行した後は、IBM watsonxのサービスに直接ログインできます。手順は[こちら]([https://github.com/IBM/japan-technology/watsonx.ai/dojo/start/readme2.md ](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/start/readme2.md "login to watsonx")です。

免責事項: 表示されているIBM CloudコンソールやIBM watsonx as a Serviceのコンソールの画像は、講師が 2024/9/14時点で利用している環境をキャプチャーしたものです。アカウントの名前やリソースの名前は、皆さんがお使いの環境とは異なっていますので、ご注意ください。

## watsonx.aiの起動
### 前提条件:
* IBM Cloudのアカウントが使えること
* IBM Cloudのリソースリスト上に、Cloud Object Storage, Watson Studio, Watson Machine Learningが登録されていること

* 上記２つの前提条件を満たせていない場合は、[こちらの資料](https://speakerdeck.com/oniak3ibm/watsonx-ai-dojo-prereq "watsonx.ai Prerequisite")を参考にしながら、準備してください。

IBM Cloudは、IBM watsonx as a Serviceという、watsonx.aiを利用して言語モデルや機械学習モデルを操作、デプロイするサービスを提供しています。

![watsonx as a Service](https://dataplatform.cloud.ibm.com/docs/api/content/wsj/getting-started/images/arch-1.svg?context=wx&locale=ja "watsonx as a service")

注意: watsonx.ai Dojoの勉強会では、watsonx.governanceは利用しません。

### 起動までの手順

1. Webブラウザーから https://cloud.ibm.com を開き、IBM IDあるいはGoogle アカウントを利用して、IBM Cloudへログインします
<img width="1430" alt="ibmcloud-login" src="https://github.com/user-attachments/assets/71a89ab1-64ea-4f63-a501-c0e2682725fb">

2. IBM Cloudのリソース・リストを開きます。https://cloud.ibm.com/resources へアクセスすると簡単です。
   リソース・リストはIBM Cloudのアカウントで使われているIBM Cloudのサービスの一覧です。
   もし複数のIBM Cloudアカウントをご利用されている場合は、適切なアカウントが選択されているかどうかをご確認ください。特にIBM Technology Zoneをご利用の場合、複数のアカウントに参加する場合があります。予約情報をご確認の上、正しいアカウントを選択してください。

3. IBM Cloudのリソース・リストから[AI/機械学習]のグループを見つけて、その中に含まれている Watson Studio のサービスを見つけて、表示されている名前をクリックします。
<img width="1377" alt="wxai-start-02-resourcelist" src="https://github.com/user-attachments/assets/2839bd02-4ccf-4064-bfda-928a3cc78a23">

4. Watson Studioのリソースが表示されます。
 <img width="1377" alt="wxai-start-03-watsonstudio" src="https://github.com/user-attachments/assets/db81d5a8-16b9-427c-acce-801eb3c2303b">

5. Watson Studioのページから、[Launch-in][v]の[v]をクリックして、表示されたメニューから[watsonx]を選びます。
<img width="1377" alt="wxai-start-04-launch" src="https://github.com/user-attachments/assets/04b67121-07bb-4f1a-b8e7-e0dbaaa34c5c">

5. IBM CloudからIBM watsonx が展開されているクラウドサービスへ移動します。この時、再度IBMへのログイン画面が表示された場合は、ログインしてください。
<img width="1548" alt="wxai-start-01-login" src="https://github.com/user-attachments/assets/48d1b763-cb8a-42fd-8d37-1cac0393a125">

6. もし、「情報を入力して続行してください」という画面が表示された場合は、正しいユーザー・アカウント名を選んでください。
<img width="1548" alt="wxai-start-05-confirm" src="https://github.com/user-attachments/assets/8dac97d3-9ae9-47fb-ab2a-7bcb75020007">
   アカウントの選択例:
<img width="1548" alt="wxai-start-06-rightaccount" src="https://github.com/user-attachments/assets/ab518282-d9db-46d0-9552-1bae8349330b">

7. IBM watsonx as a Serviceのトップページが表示されます。
<img width="1548" alt="wxai-start-07-ready" src="https://github.com/user-attachments/assets/f0d126b9-560e-44f9-9a48-e32c189656a7">


8. [ツアーの実行→]をクリックし、ガイドに従って、画面を進めます。
   
   8-1:タスクを開始する方法
<img width="1548" alt="wxai-tour01" src="https://github.com/user-attachments/assets/ca078f0d-179c-4901-b3fb-f0595386aa83">

   8-2:その他のタスクを参照する方法
<img width="1548" alt="wxai-tour02" src="https://github.com/user-attachments/assets/bc596461-2821-4482-a9e0-c1691a0f9d7c">

   8-3:作業またはサンプルの選択
<img width="1548" alt="wxai-tour03" src="https://github.com/user-attachments/assets/385a0ed0-5024-4c75-9807-20576dadff40">

9. これで IBM watsonx.ai を利用する準備が整いました。

watsonx.ai Dojoにオンラインで参加していて、ここまでの流れがうまく進まない場合は、チャットからお知らせください。

