# watsonx.aiの起動 (IBM Cloudコンソール)

最終更新日: 2025/4/21
このパートでは、次の操作を学びます。
* watsonx.aiの起動

参考URL: [IBM watsonx as a Service の資料](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/welcome-main.html?context=wx&audience=wdp "IBM watsonx SaaS document")

このページの手順を正しく実行した後は、IBM watsonxのサービスに直接ログインできます。手順は[こちら](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/start/readme2.md "login to watsonx")です。

免責事項: 表示されているIBM CloudコンソールやIBM watsonx as a Serviceのコンソールの画像は、講師が 2025/4/21時点で利用している環境をキャプチャーしたものです。アカウントの名前やリソースの名前は、皆さんがお使いの環境とは異なっていますので、ご注意ください。

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

<img width="1076" alt="IBMCloud-login" src="https://github.com/user-attachments/assets/f8d0f6fb-0ffb-4bde-a1db-4358cdfe02dc" />


2. IBM Cloudのリソース・リストを開きます。https://cloud.ibm.com/resources へアクセスすると簡単です。
   リソース・リストはIBM Cloudのアカウントで使われているIBM Cloudのサービスの一覧です。
   もし複数のIBM Cloudアカウントをご利用されている場合は、適切なアカウントが選択されているかどうかをご確認ください。特にIBM Technology Zoneをご利用の場合、複数のアカウントに参加する場合があります。予約情報をご確認の上、正しいアカウントを選択してください。

3. IBM Cloudのリソース・リストから[AI/機械学習]のグループを見つけて、その中に含まれている watsonx.ai Studio のサービスを見つけて、表示されている名前をクリックします。

<img width="1135" alt="IBMCloud-resources" src="https://github.com/user-attachments/assets/4c44ba71-c064-44da-93c6-7299ccee74e7" />

4. watsonx.ai Studioのリソースが表示されます。

<img width="1135" alt="watsonxai-studio" src="https://github.com/user-attachments/assets/e9d70e47-ac3c-4ae0-995c-a5f855275757" />


5. Watson Studioのページから、[Launch-in][v]の[v]をクリックして、表示されたメニューから[watsonx]を選びます。

<img width="1135" alt="launch-watsonx" src="https://github.com/user-attachments/assets/e8ff203c-21c6-4f07-b74c-62c204fec0f5" />


6. IBM CloudからIBM watsonx が展開されているクラウドサービスへ移動します。移動する際に、もし再度IBMへのログイン画面が表示された場合は、ログインしてください。ログイン画面が表示されなかった場合は、手順8へ進んでください。

* Firefoxでの例
<img width="1548" alt="wxai-start-01-login" src="https://github.com/user-attachments/assets/48d1b763-cb8a-42fd-8d37-1cac0393a125">

7. もし、「情報を入力して続行してください」という画面が表示された場合は、正しいユーザー・アカウント名を選んでください。

* Firefoxでの例
<img width="1548" alt="wxai-start-05-confirm" src="https://github.com/user-attachments/assets/8dac97d3-9ae9-47fb-ab2a-7bcb75020007">
   アカウントの選択例:
<img width="1548" alt="wxai-start-06-rightaccount" src="https://github.com/user-attachments/assets/ab518282-d9db-46d0-9552-1bae8349330b">

8. IBM watsonx as a Serviceのトップページが表示されます。

<img width="1135" alt="welcome-to-watsonx" src="https://github.com/user-attachments/assets/8276a141-6098-4647-b932-b65182996510" />


9. [ツアーの実行→]をクリックし、ガイドに従って、画面を進めます。
   
   9-1:タスクを開始する方法

<img width="1135" alt="wxtour01" src="https://github.com/user-attachments/assets/9ae3e87d-0d8a-447b-9744-8f1e2db336ad" />


   9-2:その他のタスクを参照する方法

<img width="1135" alt="wxtour02" src="https://github.com/user-attachments/assets/97c3e5f1-1fb3-4d3c-b4a6-344eda8aa6cf" />


   9-3:作業またはサンプルの選択

<img width="1135" alt="wxtour03" src="https://github.com/user-attachments/assets/2f480f5d-5fc5-4a55-b779-c6e98279e446" />


10. これで IBM watsonx.ai を利用する準備が整いました。

watsonx.ai Dojoにオンラインで参加していて、ここまでの流れがうまく進まない場合は、チャットからお知らせください。

