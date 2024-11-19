# LangChainを使った、RAG実装
# Special Thanks to kyokonishito
import ibm_watsonx_ai
import os
import time
import langchain
import pprint
#langchain.debug = True

step = 1
# 処理時間の計測用、参考としてなので、通常の実装では必要ありません
start = time.perf_counter()

# watsonx.ai のプロジェクトから、プロジェクトIDをコピーして入力します。
MY_PROJECT_ID = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"

# API Keyの取得: https://cloud.ibm.com/iam/apikeys
# 取得したAPIは共有しないようにご注意ください。
# 通常は API Keyは .env ファイルに格納することが推奨されますが、
# あくまでもハンズオンを進めやすくするために、直接コード内に書いています。
MY_API_KEY ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXX_XXXXXXXXXXXXXX"

# watsonx.aiへの接続情報の作成
# ibm_watsonx_ai でエラーとなる場合は、パッケージをインストールします。
# pip install ibm_watsonx_ai
from ibm_watsonx_ai import Credentials
credentials = Credentials(
    # watsonx.aiのAuthentication用のエンドポイントのURL(東京リージョン)
    url = "https://jp-tok.ml.cloud.ibm.com", 
    api_key = MY_API_KEY
)

# 使用するLLMのパラメータを作成します。

from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from ibm_watsonx_ai.foundation_models import Model

generate_params = {
    GenParams.MAX_NEW_TOKENS: 500,
    GenParams.MIN_NEW_TOKENS: 0,
    GenParams.DECODING_METHOD: "greedy",
    GenParams.REPETITION_PENALTY: 1
}

# 使用するLLMへのアクセスを設定します
from langchain_ibm import WatsonxLLM

custom_llm = WatsonxLLM(
    model_id= "ibm/granite-8b-japanese",
    url=credentials.url,
    apikey=credentials.api_key,
    params=generate_params,
    project_id=MY_PROJECT_ID
)

end = time.perf_counter()
print(">>>watsonx startup:"+str(end-start))


# プロンプトに指定する「入力」の内容を文章で記述します
query_shizuoka ="""
静岡県を知らない人に向けて、静岡県への旅行をお勧めする文章を作ってください。例があればその例を参考にして、次の「見出し一覧」にある項目を含めて書いてください。文章の最後は「魅力あふれる静岡県にお越しください！」としてください。同じ内容を繰り返さないでください。

「見出し一覧」:
- 静岡県にある観光名所3ヶ所
- 静岡県出身の有名人、芸能人4人
- 静岡県で有名なレストラン3つ
- 静岡県がモデルとなっているアニメ作品3つ
"""
if step == 1:
    start = time.perf_counter()
    print("step1: 知識を与えないで、LLMに対する質問を実行します。")
    # 知識を与えないで、LLMに対する質問を実行します。
    result = custom_llm.invoke(query_shizuoka)
    end = time.perf_counter()
    print(">>>Invoked LLM:"+str(end-start))
    # 期待と異なる結果が表示されることを確認します。
    print(">>>生成結果:")
    pprint.pprint(result)
    exit(0)


from langchain_chroma import Chroma

from langchain_huggingface import HuggingFaceEmbeddings
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import CharacterTextSplitter

# Embeddingsを作成します。
embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")

from langchain.indexes import vectorstore
# Chromaデータベースの永続化用ディレクトリー名 (この演習では使いません)
my_database = "./mychroma.db"

from langchain_community.document_loaders import TextLoader
start = time.perf_counter()
# TextLoaderを使って、テキストファイルを読み込む
loader = TextLoader('./knowledge.txt')
document=loader.load()

# テキストファイル内の文字列データを、改行が3回連続するところを基準に小さく分割する
# ここでは chunk_sizeが 110文字。
# 「静岡県出身の有名人、芸能人を4人教えてください」ところの文字数に近い、
# 対象となる部分の文字数がそれを下回っていても、超えていても、異なる文書として分割される
# 2組の文章がひとまとまりにならないような文字数を指定しておくと良い
# 例えば、chunk_size = 250にすると、レストランと有名人の２つの文書が１つの文書にまとまる
# https://github.com/langchain-ai/langchain/issues/7452
text_splitter = CharacterTextSplitter(
    separator = "\n\n\n",
    chunk_size = 110,
    chunk_overlap = 0,
    length_function = len,
)
# テキストファイルから読み込んだ内容を分割する
docs = text_splitter.split_documents(document)
if step == 2:
    print("知識をテキストファイルから読み込み、小さく分割します")
    print("len(docs) = "+str(len(docs)))
    for doc in docs:
        pprint.pprint (doc)
    end = time.perf_counter()
    print("\n>>>text splitted:"+str(end-start))
    exit(0)

# Chromaデータベースを使って、文書を追加します
from langchain_chroma import Chroma
start = time.perf_counter()
vector_store = Chroma(
    collection_name="langchain_collection",
    collection_metadata={"hnsw:space": "cosine"} ,
    embedding_function=embeddings #,
    # persist_directory=my_database,  # もしローカルにデータを保存したい場合は指定します
)

vector_store.add_documents(documents=docs)
end = time.perf_counter()
print("\n>>>Added documents:"+str(end-start))

if step==3:
    # Chromaデータベースに対して、問い合わせを実行します
    start = time.perf_counter()
    result = vector_store.similarity_search_with_score(query_shizuoka)
    print("vector_store.similarity_search_with_scoreを実行")
    pprint.pprint(result)
    end = time.perf_counter()
    print("\n>>>search completed:"+str(end-start))
    start = time.perf_counter()
    result = vector_store.similarity_search_with_score("IBM TechXchangeとは何ですか")
    print("vector_store.similarity_search_with_scoreを実行")
    pprint.pprint(result)
    end = time.perf_counter()
    print("\n>>>search completed:"+str(end-start))

    exit(0)

# Retrieverの作成
start = time.perf_counter()
retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold", 
    #search_kwargs={'score_threshold': 0.5, "k":3}
    search_kwargs={'score_threshold': 0.8}
)
if step==4:
    # LangChainのRetriever (この場合Chromaデータベース)に問い合わせを実行します
    print("retriver.invokeから問い合わせを実行")
    result = retriever.invoke(query_shizuoka)
    pprint.pprint(result)
    end = time.perf_counter()
    print("\n>>>retriver invoked:"+str(end-start))
    exit(0)


# PromptTemplateの作成 {context}, {question}はパラメータの値に置き換わる
from langchain.prompts import PromptTemplate
prompt_template = """以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。

### 指示:
与えられた質問に対して、文脈がある場合はそれも利用し、回答してください。

文脈: 
{context}

### 入力: 
{question}
### 応答:"""

myPromptTemplate = PromptTemplate.from_template(prompt_template)

from langchain.schema.runnable import RunnablePassthrough

# RAG用の処理の連鎖をオーバーロードされた | 演算子で表現する
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | myPromptTemplate
    | custom_llm
)

start = time.perf_counter()
result = rag_chain.invoke(query_shizuoka)
end = time.perf_counter()
print("\n>>>RAG completed:"+str(end-start))
print(result)

start = time.perf_counter()
query = "IBM TechXchange Japanとは?"
result = rag_chain.invoke(query)
end = time.perf_counter()
print("\n>>>RAG completed:"+str(end-start))
print(result)

start = time.perf_counter()
query = "LangChainについて教えてください"
result = rag_chain.invoke(query)
end = time.perf_counter()
print("\n>>>RAG completed:"+str(end-start))
print(result)

exit(0)

