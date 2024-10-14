## watsonx.ai にデプロイ済みのWebサービスを呼び出す


前提条件: [watsonx.ai Dojo #3 パート2](https://github.com/IBM/japan-technology/tree/main/watsonx.ai/dojo/03/02-structured-prompt) を完了し、depWSがデプロイできていること。

免責事項: 生成AIは事前学習したデータを活用しながらテキストを生成します。言語モデルに含まれている言葉が確率で選択されるため、生成AIは事実と異なる結果を生成する場合があります。このハンズオンでは、段階的にプロンプトを改善するため、途中、意図しない結果を敢えて得ることも行います。生成AIのハルシネーションから間違った内容が伝わらないよう、生成された内容をそのまま利用するのではなく、必ず、事実確認を行なってください。

#

1. Webブラウザーから https://jp-tok.dataplatform.cloud.ibm.com/ml-runtime/dashboard?context=wx へアクセスし、[デプロイメント]のページを開きます。
[スペース]タグをクリックします。
<img width="1521" alt="wxai03-03-01-deployments" src="https://github.com/user-attachments/assets/ff3d0cf1-a801-4cdc-b0bc-5dcc83f84423">

2. [wxaiSpace]というデプロイメント・スペースが一覧に表示されていることを確認し、[wxaiSpace]をクリックします。
<img width="1521" alt="wxai03-03-02-wxaiSpace" src="https://github.com/user-attachments/assets/e17e2892-7b97-4165-a4da-1ce66fd02fea">

3. [wxaiSpace]の画面が表示されます。資産の中に[Welcome-Shizuoka-template]が表示されていることを確認します。
<img width="1521" alt="wxai03-03-03-promptTemplate" src="https://github.com/user-attachments/assets/84b16606-1631-41bf-a119-43554c3439cd">

4. [デプロイメント]タブをクリックし、[depWS]がデプロイ済みであることを確認します。[depWS]をクリックします。
<img width="1521" alt="wxai03-03-04-depWS" src="https://github.com/user-attachments/assets/b719ed01-58d0-4235-be4d-583e26591e13">

5. [depWS]の画面が表示されます。これまでの手順を確認して、デプロイ済みのサービスを見つける方法を覚えておきましょう。
<img width="1521" alt="wxai03-03-05-depWS-detail" src="https://github.com/user-attachments/assets/8d51b673-526f-42f5-83b6-2889ee0478bf">
* パブリック・エンドポイントURLの例: https://jp-tok.ml.cloud.ibm.com/ml/v1/deployments/wst01/text/generation?version=2021-05-01
* wst01のところは、皆さんが指定したwst01で始まる文字列が表示されるはずです。

6. 続けて、[テスト]タブをクリックします。テスト画面が表示されるので、右下の[生成]をクリックします。
<img width="1521" alt="wxai03-03-06-depWS-test" src="https://github.com/user-attachments/assets/1b16f92b-8d9f-4b2c-9f55-fcc4b61efdff">

7. しばらく待つと、[プロンプト結果]が表示されます。
<img width="1521" alt="wxai03-03-07-promptResults" src="https://github.com/user-attachments/assets/bb78ac00-a7d9-42f8-ba50-d5c6ae9ad06d">

8. [JSONビュー]をクリックして、結果をJSON形式で確認しましょう。[JSONファイルのダウンロード]をクリックして、ローカル・コンピュータに保存します。
<img width="1521" alt="wxai03-03-08-jsonView" src="https://github.com/user-attachments/assets/f0a007b9-7b6a-4315-a4e5-22e23f41bb3d">

9. 右上の[x]をクリックして、結果を閉じます。
10. [ストリーム]タブをクリックし、手順6と同様に、右下の[生成]をクリックします。
<img width="1521" alt="wxai03-03-09-stream-test" src="https://github.com/user-attachments/assets/fb1dc074-845e-4a21-b082-ae353943dadf">

11. しばらく待つと、[プロンプト結果]が表示されます。手順7や手順8とは異なり、文章が細かく分割されて送られてきているのを確認できます。
<img width="1521" alt="wxai03-03-11-streamedResult" src="https://github.com/user-attachments/assets/69a5096f-5602-44ff-8697-5e66502516f7">

12. [テキスト・ビュー]をクリックして、右下にある[テキスト・ファイルのダウンロード]を選びましょう。

<img width="1521" alt="wxai03-03-12-streamedTextResults" src="https://github.com/user-attachments/assets/0b65696b-8377-474e-8daf-e0e3244f570c">

13. 右上の[x]をクリックして、結果を閉じます。
14. [JSON]タブをクリックして、手順6や手順10と同様に、右下の[生成]をクリックします。
<img width="1521" alt="wxai03-03-14-json" src="https://github.com/user-attachments/assets/042ca88d-8062-4637-8999-848bc7a8f89d">

15. しばらく待つと、[プロンプト結果]が表示されます。手順7と同じ結果が得られていることを確認します。
<img width="1521" alt="wxai03-03-15-jsonResult" src="https://github.com/user-attachments/assets/f900230b-bcb0-44d4-88bf-e8d56e4525e6">


