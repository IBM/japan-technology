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









