# テキストファイルに知識を書いておき、granite-8b-japanese、Chroma、LangChainを利用して、RAGを実行する

前提条件: [演習準備](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/04/01-new-project/readme.md)を完了していること
* watsonxのプロジェクトが作成されている
* watsonxのプロジェクトIDを取得できている
* IBM CloudのAPI Keyが取得できている

免責事項: 生成AIは事前学習したデータを活用しながらテキストを生成します。言語モデルに含まれている言葉が確率で選択されるため、生成AIは事実と異なる結果を生成する場合があります。生成AIのハルシネーションから間違った内容が伝わらないよう、生成された内容をそのまま利用するのではなく、必ず、事実確認を行なってください。

利用モデル: [IBM granite-8b-japanese](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-granite-8b-japanese.html?context=wx&locale=ja)  

##
1. （すでにvenv環境を開いている場合はスキップしてください)Windowsの場合はUbuntu、Macの場合はターミナルを開きます。Python仮想環境 venvに入ります。以降の手順でコマンドはこのvenv環境下、~/wxaiディレクトリーで実行します。

```
cd ~/wxai
source venv/bin/activate
```
2. このハンズオンで利用するテキストファイルをダウンロードします。

```
wget https://raw.githubusercontent.com/IBM/japan-technology/refs/heads/main/watsonx.ai/dojo/04/02-rag/knowledge.txt
```

MacOSでwgetコマンドが見つからない場合は、wgetをインストールしてから、上のコマンドを実行します。
```
brew install wget
```

3. catコマンドでテキストファイルの内容を確認します。途中で表示が止まったら、Enterキーを続けて押して進みます。
```
cat knowledge.txt | more
```

4. 開いたknowledge.txtに、次の内容が表示されていることを確認します。最初の３つの質疑応答は、watsonx.ai Dojo #3で利用したものと同じです。
```
静岡県の有名なレストランを３つ教えてください。
・炭焼きレストランさわやか (げんこつハンバーグ料理が大人気)
・中華ファミリーレストラン五味八珍（中華料理、浜松餃子が大人気）
・元祖丁子屋（とろろ汁が大人気）


静岡県出身の有名人、芸能人を4人教えてください。
・広瀬すず （静岡県静岡市清水区出身）
・長澤まさみ （静岡県磐田市出身）
・百田夏菜子  （静岡県浜松市出身）
・久保田利伸 (静岡県静岡市清水区、旧清水市出身)


静岡県がモデルとなっているアニメ作品を３つ教えてください。
・「ラブライブ！サンシャイン！！」聖地は、静岡県沼津市が中心です。伊豆・三津シーパラダイスも有名で、多くのファンが訪れています。
・「ちびまる子ちゃん」静岡県静岡市清水区（旧清水市）がモデルになっています。エスパルス・ドリームプラザ内に「ちびまる子ちゃんランド」があり、多くのファンが訪れています。
・「シュート！」静岡県掛川市がモデルとなったサッカー漫画です。作品内の掛川高校は、掛川西高校がモデルと言われています。


IBM TechXchangeについて教えてください。
IBM製品とテクノロジーに関する最新情報をお届けし、体感いただけます。
最新技術のセッション、デモ、ハンズオンの場を提供します。 
また、コミュニティー・イベント、技術者の皆様との交流の場を通じて、技術者同士が学び、繋がるネットワーキングの機会もご提供します。
全てのセッションは日本語で実施されます。


LangChainとは
LangChainの中核をなすのは、抽象化によってLLMアプリケーションのプログラミングを効率化する開発環境です。
抽象化とは、1つ以上の複雑なプロセスの構成ステップをすべてカプセル化した名前付きコンポーネントとみなすことでコードを簡素化することです。


```

5. このハンズオンで使うPythonスクリプトをダウンロードします。

```
wget https://raw.githubusercontent.com/IBM/japan-technology/refs/heads/main/watsonx.ai/dojo/04/02-rag/lcqa.py
```

6. Visual Studio Codeからダウンロードした lcqa.py を開きます。
```
code lcqa.py
```
7. lcqa.py の9行目が step = 1 になっていることを確認します。
```
step = 1
```

8. lcqa.py の14行目にプロジェクトID、20行目にAPI Keyを入力します。入力したら、Visual Studio Codeの[File]-[Save]メニューで保存します。Visual Studio Codeはそのままにしてください。
Windowsの場合 [ctrl]+[s] キー, MacOSの場合 [command]+[s] キーで保存ができます。

```
MY_PROJECT_ID = "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
```

```
MY_API_KEY ="XXXXXXXXXXXXXXXXXXXXXXXXXXXXX_XXXXXXXXXXXXXX"
```

9. Ubuntuまたはターミナルに戻り、次のコマンドを実行します。
```
python lcqa.py
```

エラーが発生する場合の対処方法
* ibm_watsonx_ai.wml_client_error.WMLClientError: Error getting IAM Token. 
　おそらくAPI Keyが指定されていないか、間違っています。
* Reason: {"id":"WSCPA0000E","code":400,"error":"Bad Request","reason":"Invalid project GUID encountered in request path: XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX.","message":"The server cannot or will not process the request due to an apparent client error (e.g. malformed request syntax)."}
　おそらくプロジェクトIDが指定されていないか、間違っています。

プロジェクトIDとAPIキーが正しく指定されている場合の出力例:
* granite-8b-japaneseに何も知識を与えていない状態でプロンプトを実行しているので、生成された結果を見て、がっかりしないでください。
```
(venv) oniak3.ai@AkiranoMacBook-Pro wxai % python lcqa.py
>>>watsonx startup:1.9746542500215583
step1: 知識を与えないで、LLMに対する質問を実行します。
>>>Invoked LLM:7.000577916012844
>>>生成結果:
('- 静岡県のお祭り3つ\n'
 '- 静岡県のお土産5つ\n'
 '- 静岡県へのアクセス方法3つ\n'
(途中省略)
 '- 静岡県での警察3つ\n'
 '- 静岡県での交通3つ\n')
```

10. Visual Studio Codeに戻り、lcqa.py の9行目を書き換えます。lcqa.pyを保存します。Visual Studio Codeはそのままにしてください。
```
step = 2
```

11. Ubuntuまたはターミナルに戻り、次のコマンドを実行します。
```
python lcqa.py
```

12. 出力結果を確認します。step 2では、knowledge.txtの内容を読み込み、質問と回答が１つの文書になるよう分割しています。5つの文書に分かれていることを確認します。
分割の基準を110文字に設定していますが、110文字をこえる文書も取り扱えることがわかります。
CharacterTextSplitterを初期化する際に、2組の質疑応答がひとまとまりにならないような文字数を指定しておくと、期待通りに分割されます。


```
(venv) oniak3.ai@AkiranoMacBook-Pro wxai % python lcqa.py
>>>watsonx startup:2.72061379099614
Created a chunk of size 239, which is longer than the specified 110
Created a chunk of size 179, which is longer than the specified 110
知識をテキストファイルから読み込み、小さく分割します
len(docs) = 5
Document(metadata={'source': './knowledge.txt'}, page_content='静岡県の有名なレストランを３つ教えてください。\n・炭焼きレストランさわやか (げんこつハンバーグ料理が大人気)\n・中華ファミリーレストラン五味八珍（中華料理、浜松餃子が大人気）\n・元祖丁子屋（とろろ汁が大人気）')
Document(metadata={'source': './knowledge.txt'}, page_content='静岡県出身の有名人、芸能人を4人教えてください。\n・広瀬すず （静岡県静岡市清水区出身）\n・長澤まさみ （静岡県磐田市出身）\n・百田夏菜子  （静岡県浜松市出身）\n・久保田利伸 (静岡県静岡市清水区、旧清水市出身)')
Document(metadata={'source': './knowledge.txt'}, page_content='静岡県がモデルとなっているアニメ作品を３つ教えてください。\n・「ラブライブ！サンシャイン！！」聖地は、静岡県沼津市が中心です。伊豆・三津シーパラダイスも有名で、多くのファンが訪れています。\n・「ちびまる子ちゃん」静岡県静岡市清水区（旧清水市）がモデルになっています。エスパルス・ドリームプラザ内に「ちびまる子ちゃんランド」があり、多くのファンが訪れています。\n・「シュート！」静岡県掛川市がモデルとなったサッカー漫画です。作品内の掛川高校は、掛川西高校がモデルと言われています。')
Document(metadata={'source': './knowledge.txt'}, page_content='IBM TechXchangeについて教えてください。\nIBM製品とテクノロジーに関する最新情報をお届けし、体感いただけます。\n最新技術のセッション、デモ、ハンズオンの場を提供します。 \nまた、コミュニティー・イベント、技術者の皆様との交流の場を通じて、技術者同士が学び、繋がるネットワーキングの機会もご提供します。\n全てのセッションは日本語で実施されます。')
Document(metadata={'source': './knowledge.txt'}, page_content='LangChainとは\nLangChainの中核をなすのは、抽象化によってLLMアプリケーションのプログラミングを効率化する開発環境です。\n抽象化とは、1つ以上の複雑なプロセスの構成ステップをすべてカプセル化した名前付きコンポーネントとみなすことでコードを簡素化することです。')

>>>text splitted:0.000358375022187829
```

エラーが発生する場合の対処方法
* Pythonパッケージのインストールを確認してください


