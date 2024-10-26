# ハンズオン実施
前提：
[ワークショップ環境へのアクセス](01_techzone_use_environments.md)が完了し、IBM CloudのダッシュボードがWebブラウザーに表示されていることが前提です。
<img width="800" alt="" src="images/01_2-5-ibmcloud.jpg"><br>

## ハンズオン
以下の順序で各リンクにアクセスし、実施してください

### 1. wastonx.data: Milvus 情報の取得
wastonx.dataのMilvusの接続情報を取得します
- [wastonx.data: Milvus 情報の取得](watsonx_data_get_milvus_info.md)

### 2. wastonx.ai: Watson Studioの立ち上げ
wastonx.aiのWatson Studioを立ち上げ、サンドボックスプロジェクトを開きます
- [wastonx.ai: Watson Studioの立ち上げ](watsonx_ai_open_watson_studio.md)<br>

### 3. NotebookをJupyter Notebookエディター・ツールで開いて実行
以下T.B.D.
#### 1. Excelをベクトル化してベクトルDB Milvusに入れよう<br>
TechXchange Japanの情報が入ったExcelファイルをベクトル化してベクトルDB Milvusに入れます
- [Notebookを新規作成して開く](open_notebook_01.md)

もし既に作成済みの場合は、「アセット」タブから、「`techxchange_handson_01_vectordb.ipynb`」を選択し、右側の︙をクリックし、「編集」を選択してください。<br>
![alt text](images/open_notebook_from_asset01.jpg)

2に進む際、Notebookを開いたままにするには、上部のプロジェクト名を右クリックし、「新しいタブで開く」でプロジェクトを新しいタブで開いてください。<br>
![alt text](images/open_project_from_notebook.jpg)

#### 2. ベクトルDB Milvusに入ったデータで類似検索してみよう!<br>
- 1で準備したベクトルDBのデータでLangChainを使用して類似検索してみます

#### 3. ベクトルDB Milvusとwatsonx.ai LLMでRAGを構成して、質問をしてみよう!<br>
-  1で準備したベクトルDBのデータとwatsonx.ai LLMでLangChainを使用してRAGを構成し、質問をしてみます

#### 4. ベクトルDB Milvusとwatsonx.ai LLMでRAGを構成して、チャットアプリを作成してみよう!<br>
- 3の仕組みを利用してチャットアプリを作成します

---
[watsonxハンズオン1 さわってみようベクトル・データベース watsonx.dataでRAG体験 - トップページに戻る](README.md)




