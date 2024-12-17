# Tuning Studio 体験
watsonx.ai Dojo #5の最初の演習は、Tuning Studioの体験です。
この演習は、公式文書に含まれている [Quick start: Tune a foundation model](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/get-started-tuning-studio.html?context=wx&locale=en)を参考にしています。

前提条件:
* IBM watsonx as a Serviceの環境にアクセスできること

### Task 1: 新規プロジェクトの作成

1. Webブラウザーを開き、https://jp-tok.dataplatform.cloud.ibm.com/login?context=wx へアクセスします。
<img width="1548" alt="スクリーンショット 2024-09-14 16 28 14" src="https://github.com/user-attachments/assets/a0420116-4506-4917-bf70-1a08c8e67bc4">
2. お使いのIBM IDを入力して[続行] をクリックします。

3. IBM watsonx が起動します。

4. Webブラウザーから https://jp-tok.dataplatform.cloud.ibm.com/projects/new-project?context=wx へアクセスします。
名前を ```Dojo #5``` と入力して、[作成]をクリックします。
<img width="1533" alt="wxai05-01-01-newproject" src="https://github.com/user-attachments/assets/6217bc45-5255-4c9a-ad49-1970945227bf" />

5. プロジェクトの概要ページが開くので[管理]をクリックします。
<img width="1533" alt="wxai05-01-05-overview" src="https://github.com/user-attachments/assets/e602e5bd-157d-4133-89aa-6d2cef6cb23b" />

6. プロジェクトの管理ページの左側にある[サービスおよび統合]をクリックします。[サービスの関連付け +]をクリックします。
<img width="1533" alt="wxai05-01-06-associates" src="https://github.com/user-attachments/assets/02978ebd-4c4c-4e54-b139-72ac9f78d726" />

7. Watson Machine Learning または watsonx.ai Runtime のサービスが表示されるので、リストの左側にあるチェックボックスをクリックします。続いて、[アソシエイト]をクリックします。
<img width="1533" alt="wxai05-01-07-associatesWML" src="https://github.com/user-attachments/assets/ef02c015-b266-445a-93c5-0e0b92bcc49c" />

8. watsonx.ai Runtime (Watson Machine Learning)のサービスが関連づけられたことを確認します。
* Watson Machine Learningはwatsonx.ai Runtimeに名前が変わりました。
<img width="1533" alt="wxai05-01-08-aiRuntime" src="https://github.com/user-attachments/assets/1b8854bc-6292-493f-a4fc-135e90d62787" />

### Task 2: 基盤モデルのテスト
1. [概要]タブをクリックして、Dojo #05プロジェクトの概要ページに戻り、[基盤モデルを使用したチャットとプロンプトの作成]をクリックします。
 <img width="1533" alt="wxai05-01-t2-01-OpenPromptLab" src="https://github.com/user-attachments/assets/7326b04a-7fda-47f6-9613-46b16e79136a" />
2. [構造化]タブをクリックして、モデル・メニューから[すべての基盤モデルを表示する]をクリックします。
<img width="1533" alt="wxai05-01-t2-02-OpenLLM" src="https://github.com/user-attachments/assets/8d2bae38-5175-4af7-a6d1-4cb792df831f" />
3. [granite-13b-instruct-v2]モデルをクリックします。
<img width="1533" alt="wxai05-01-t2-03-granite13b" src="https://github.com/user-attachments/assets/bbf9b98d-6e00-44ec-8f9e-ef77d868467d" />
4. Model Datasheetが表示されるので、[モデルの選択]をクリックします。
<img width="1533" alt="wxai05-01-t2-04-Model-granite13b" src="https://github.com/user-attachments/assets/e55bf4c1-1431-43a3-b5de-0d957614795a" />
5.命令（オプション)に次の文字列を入力します。

```
Summarize customer complaints
```

<img width="1533" alt="wxai05-01-t2-05-instruction" src="https://github.com/user-attachments/assets/fd935bc1-bb7a-470c-9578-6d8b543d4200" />
6. 例(オプション)に入力と出力、２つの例を加えます。

1つ目:

入力:

```
I forgot in my initial date I was using Capital One and this debt was in their hands and never was done.
```

出力:

```
Debt collection, sub-product: credit card debt, issue: took or threatened to take negative or legal action sub-issue
```

2つ目: [例の追加+]をクリックして、入力欄を増やしてください。

入力:

```
I am a victim of identity theft and this debt does not belong to me. Please see the identity theft report and legal affidavit.
```

出力:

```
Debt collection, sub-product, I do not know, issue. attempts to collect debt not owed. sub-issue debt was a result of identity theft
```

<img width="1533" alt="wxai05-01-t2-06-examples" src="https://github.com/user-attachments/assets/496e4e4b-d6d4-44f8-b4a1-c4b5e30b0d73" />

7. 試行の[入力:]欄にプロンプトを入力します。
   
```
After I reviewed my credit report, I am still seeing information that is reporting on my credit file that is not mine. please help me in getting these items removed from my credit file.
```

<img width="1533" alt="wxai05-01-t2-07-PromptTest" src="https://github.com/user-attachments/assets/1c4a7e3e-d30a-4c79-9fe5-ee5543b7bd92" />

8. [生成]をクリックします。生成結果を確認します。
<img width="1533" alt="wxai05-01-t2-08-generated" src="https://github.com/user-attachments/assets/d852dede-dbc6-4c95-a08c-dd949d555294" />


9. [名前を付けて保存]をクリックします
<img width="1413" alt="wxai05-01-t2-09-SaveAs" src="https://github.com/user-attachments/assets/0dd289c8-355d-4fd3-8dcc-00d14da27608" />

10. 作業の保存ウィンドウから、以下を入力し、[保存]をクリックします。
* 資産タイプ: [プロンプト・テンプレート]
* 名前: ```Base model prompt```
<img width="1533" alt="wxai05-01-t2-PromptTemplate" src="https://github.com/user-attachments/assets/acec4cdd-50eb-4fd1-a584-1f91a0c35c6d" />

### Task 3: 学習データの追加

1. 画面左上、IBM watsonxのハンバーガー・メニューから[リソース・ハブ]を選択します。
<img width="1533" alt="wxai05-01-t3-MenuResourceHub" src="https://github.com/user-attachments/assets/d7d86eed-9194-462a-9118-f88fa24cd9fb" />

2. リソース・ハブの[サンプル]タブをクリックし、検索文字列に[customer]と入力します。検索結果から[Customer complaints training data]をクリックします。
<img width="1533" alt="wxai05-01-t3-CustomerComplaintsData" src="https://github.com/user-attachments/assets/d8f47fa3-efa2-4f0a-a9f4-359321800949" />

3. [Customer complaints training data]の説明画面が表示されたら、[プロジェクトに追加]をクリックします。プロジェクト名は[Dojo #5]を選択します。
   
<img width="1533" alt="wxai05-01-t3-addData" src="https://github.com/user-attachments/assets/1734cf12-6727-47c1-b26e-a6621408d3ae" />

4.[プロジェクトの表示]をクリックします。
<img width="437" alt="wxai05-01-t3-showProject" src="https://github.com/user-attachments/assets/96f2dc10-85a2-434e-8fb2-6e22357bad86" />

5. Dojo #5のプロジェクト概要が表示されるので、[資産]タブをクリックします。手順3で追加したデータが資産として登録されていることを確認します。
<img width="1533" alt="wxai05-01-t3-Assets" src="https://github.com/user-attachments/assets/3a005580-8a3d-4f8e-b264-653ff09fdb4f" />

### Task 4: Tuning Studioの準備

1. Dojo #5のプロジェクト概要タブに戻り、[ラベル付きデータを使用した基盤モデルの調整]をクリックします。
<img width="1533" alt="wxai05-01-t4-overview" src="https://github.com/user-attachments/assets/2445b995-7387-44e0-87b5-4e12d893b2ad" />

2. [ラベル付きデータを使用した基盤モデルのチューニング]のウィンドウが開くので、名前を[Summarize customer complaints tuned model]と入力して、[作成]をクリックします。
<img width="1533" alt="wxai05-01-t4-labeledData" src="https://github.com/user-attachments/assets/d2e3950b-2370-4742-9f44-5d36b3472575" />

### Task 5: Tuning Studioの構成

1. [チューニング済みモデルの構成]のウィンドウが表示されます。[基盤モデルの選択]をクリックします。
   
<img width="1533" alt="wxai05-01-t4-TuningDetail-selectLLM" src="https://github.com/user-attachments/assets/2df72211-6e1a-4f2f-963c-9a079b4e5e68" />

2.[基盤モデルの選択]から[granite-13b-instruct-v2]をクリックします。
<img width="1533" alt="wxai05-01-t4-Granite13b" src="https://github.com/user-attachments/assets/ddb3f79c-08ff-4ac5-be57-9d1a254ca6cf" />

3. [granite-13b-instruct-v2]のModel Sheetが表示されるので、[選択]をクリックします。
<img width="1533" alt="wxai05-01-t4-Granite-ModelSheet" src="https://github.com/user-attachments/assets/d62bde56-847b-4d4d-a33f-327f59959f77" />

4. [プロンプトをどのように初期化しますか]の設定で、[テキスト]をクリックし、[タスクの説明および指示]に次の内容を入力します。

```
Summarize the complaint provided into one sentence.
```

<img width="1533" alt="wxai05-01-t5-task" src="https://github.com/user-attachments/assets/c299d545-3269-4bb1-9bec-6560b0d55af7" />

5. [どのタスクが目標に適合していますか?]の設定で、[要約]をクリックします。
   
<img width="1533" alt="wxai05-01-5-Summarization" src="https://github.com/user-attachments/assets/481dceee-7467-40d0-9547-f44287233207" />

6. [トレーニング・データの追加]から[プロジェクトから選択]をクリックします。
<img width="1533" alt="wxai05-01-6-projectData" src="https://github.com/user-attachments/assets/7bddb6d8-d284-4fde-b7ed-59aa43be14ac" />

7. [プロジェクトからデータを選択します]の画面から、[データアセット]をクリックし、[データ資産]から[Customer complaints training data]を選びます。最後に[アセットの選択]をクリックします。
<img width="1533" alt="wxai05-01-t5-chooseData" src="https://github.com/user-attachments/assets/dfffd26a-c567-414b-b9ce-cfb5007a7770" />

8. Tuning Studioを起動するための構成が完了しました。
<img width="1533" alt="wxai05-01-t5-ready" src="https://github.com/user-attachments/assets/e87d2f45-780a-4246-b2b0-d52c6c5b6805" />

9. ここから先の手順について、注意事項を確認します。問題がなければ、10に進んでください。何か気になる場合は、ここで中断してください。中断した場合、チューニングした結果は確認できませんので、ご理解ください。
* チューニングを開始するとwatsonx.ai Runtimeが動作し、利用できるコンピュート・リソースが減っていきます。
* 無料枠で利用している場合、利用可能なコンピュート・リソースが足りなくなる場合があります。
* チューニングには時間がかかり、30分以上、要する場合があります。

10. [チューニングの開始]をクリックします。










