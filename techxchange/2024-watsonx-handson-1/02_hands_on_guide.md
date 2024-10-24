# ハンズオン実施
前提：
[ワークショップ環境へのアクセス](01_techzone_use_environments.md)が完了し、IBM CloudのダッシュボードがWebブラウザーに表示されていることが前提です。
<img width="800" alt="" src="images/01_2-5-ibmcloud.jpg"><br>

## ハンズオン
以下の順序で各リンクにアクセスし、実施してください

### 1. [wastonx.data: Milvus 情報の取得](watsonx_data_get_milvus_info.md)<br>
wastonx.dataのMilvusの接続情報を取得します

### 2. [wastonx.ai: Watson Studioの立ち上げ](watsonx_ai_get_watson_studio.md)<br>
wastonx.aiのWatson Studioを立ち上げ、サンドボックスプロジェクトを開きます

### 3. [notebook実行](watsonx_ai_run_notebook.md)
#### 1. [Excelをベクトル化してベクトルDB Milvusに入れよう！]()<br>
TevchXchange Japanの情報が入ったExcelファイルをベクトル化してベクトルDB Milvusに入れます

#### 2. [ベクトルDB Milvusに入ったデータで類似検索してみよう!]()<br>
1で準備したベクトルDBのデータでLangChainを使用して類似検索してみます

#### 3. [ベクトルDB Milvusとwatsonx.ai LLMでRAGを構成して、質問をしてみよう!]()<br>
 1で準備したベクトルDBのデータとwatsonx.ai LLMでLangChainを使用してRAGを構成し、質問をしてみます

#### 4. [ベクトルDB Milvusとwatsonx.ai LLMでRAGを構成して、チャットアプリを作成してみよう!]()<br>
3の仕組みを利用してチャットアプリを作成します



