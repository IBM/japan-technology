# 演習3: FastAPIでAPIサーバーを作ってみる
最低限のコードでAI推論を実行できることが確認できたら、このコードを発展させて、APIサーバーに変えてみます。
この演習ではFastAPIをインストールし、AI推論を実行するAPIサーバーをPythonコードを使って動作させます。

前提条件:
* IBM watsonx as a Serviceの環境にアクセスできること

### Task 1: [FastAPI](https://fastapi.tiangolo.com/ja/)のインストール
1. Windowsの場合はUbuntu、Macの場合はターミナルを開きます。Python仮想環境 venvに入ります。以降の手順でコマンドはこのvenv環境下、~/wxaiディレクトリーで実行します。

```
cd ~/wxai
source venv/bin/activate
```

2. FastAPIをインストールします。

```
pip install fastapi
```

### Task 2: APIサーバーの実行と改造

1. APIサーバーのソースコード simpleapi.py をダウンロードします。

```
wget https://raw.githubusercontent.com/IBM/japan-technology/refs/heads/main/watsonx.ai/dojo/06/simpleapi.py
```

もし、MacOSでwgetコマンドが見つからない場合は、wgetをインストールしてから、上のコマンドを実行します。

```
brew install wget
```

2. Visual Studio Codeでsimpleapi.pyを開きます。

```
code simpleapi.py
```

3. simpleapi.py コードを確認します。APIキーとProject IDは書き換えてください。この後の作業で使うので、Visual Stdio Codeは開いたままにしてください。

```simpleapi.py
# simpleapi.py
# FastAPIを使った AI APIサーバーの作成
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
import time
import logging

API_KEY="<APIキ->"
PROJECT_ID="<Project ID>"

credentials = Credentials(
    url = "https://jp-tok.ml.cloud.ibm.com",
    api_key = API_KEY
)
logger = logging.getLogger('uvicorn')
def connect_watsonx():
    start = time.perf_counter()
    cli = APIClient(credentials)
    end = time.perf_counter()
    logger.info("watsonxへの通信確立:"+str(end-start))
    return cli

def load_model():
    start = time.perf_counter()
    m = ModelInference(
            model_id="ibm/granite-3-8b-instruct",
            api_client=connect_watsonx(),
            project_id=PROJECT_ID,
            params = {
                "max_new_tokens": 600
            }
        )
    end = time.perf_counter()
    logger.info("LLMの設定完了:"+str(end-start))
    return m

from fastapi import FastAPI

app = FastAPI()
model = load_model()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/prompt/")
def read_item(q: str = None):
    start = time.perf_counter()
    generated_string = model.generate_text(q)
    end = time.perf_counter()
    logger.info("推論時間:"+str(end-start))
    # logger.info("generated_text" + generated_string)
    return {"generated_text": generated_string}
```

4. 次のコマンドを入力して、APIサーバーを起動します。

```
uvicorn simpleapi:app --reload
```

出力例
```
INFO:     Will watch for changes in these directories: ['/Users/oniak3.ai/wxai']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7152] using WatchFiles
INFO:     watsonxへの通信確立:1.9019767910067458
INFO:     LLMの設定完了:2.4667096659977688
INFO:     Started server process [7154]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

5. ブラウザーを起動し、次のURLにアクセスして、Swagger UIを表示します。
URL:
```
http://127.0.0.1:8000/docs
```
<img width="1107" alt="wxai06-02-fastapi-swagger" src="https://github.com/user-attachments/assets/79e8885d-74a2-4e7a-8ecc-5f9c8c4ffa6d" />

6. ブラウザーに表示されている画面から、/prompt/ APIを展開します。
<img width="1011" alt="wxai06-03-fastapi-prompt" src="https://github.com/user-attachments/assets/c7231d1c-2bd5-404b-94e3-86e5aeaf9199" />

7. [Try it out]をクリックし、qパラメータにプロンプトを入力します。
qパラメータ:
```
C#を使ってONNXモデルを呼び出すコードを作成してください。
```
<img width="1011" alt="wxai06-03-fastapi-ready2execute" src="https://github.com/user-attachments/assets/243e8090-469a-41be-ad09-b239d1d48aae" />

8. [Execute]をクリックします。
<img width="1011" alt="wxai06-03-fastapi-response" src="https://github.com/user-attachments/assets/1775bc54-35ce-4c58-a864-690f2e982ab7" />

9. 新しいUbuntuまたはターミナルを開いて、次のコマンドを実行し、同じ結果が得られることを確認します。
```
curl -X 'GET' \
  'http://127.0.0.1:8000/prompt/?q=C%23%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6ONNX%E3%83%A2%E3%83%87%E3%83%AB%E3%82%92%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%99%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E4%BD%9C%E6%88%90%E3%81%97%E3%81%A6%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82' \
  -H 'accept: application/json'
```

10. Visual Studio Codeに戻り、simpleapi.pyの51行目のコメントの　# を削除し、ファイルを保存します。
変更前:
```
# logger.info("generated_text" + generated_string)
```

変更後:
```
logger.info("generated_text" + generated_string)
```

11. FastAPIのプロセスに戻ると、simpleapi.pyが更新されたことをトリガーにして、APIサーバーが再読み込みされていることがわかります。
出力例:
```
WARNING:  WatchFiles detected changes in 'simpleapi.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [7154]
INFO:     watsonxへの通信確立:0.7731447499973001
INFO:     LLMの設定完了:1.3217707089934265
INFO:     Started server process [8305]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
``` 

12. 上記9の手順をもう一度実行します。FastAPIのプロセスに戻ると、推論結果がログ表示されていることがわかります。
出力例:
``` 
INFO:     推論時間:7.642010666997521
INFO:     generated_text

以下は、C#でONNXモデルを呼び出すコードの例です。

using System;
using System.IO;
using System.Runtime.InteropServices;
using ONNXRuntime;

class Program
{
    static void Main(string[] args)
    {
        // ONNXモデルのパスを指定
        string modelPath = "path/to/your/model.onnx";

        // ONNXRuntimeのセッションを作成
        SessionOptions sessionOptions = new SessionOptions();
        sessionOptions.GraphOptimizationLevel = GraphOptimizationLevel.ORT_ENABLE_ALL;
        Session session = new Session(sessionOptions, modelPath);

        // 入力データを準備
        float[] inputData = { 1.0f, 2.0f, 3.0f, 4.0f };
        int[] inputShape = { 1, 4 };

        // 入力データをONNXRuntimeのセッションに提供
        IRuntimeSession sessionRuntime = session.CreateRuntimeSession();
        IOutputInfo outputInfo = sessionRuntime.GetOutputInfoByName("output_name");
        IValue inputValue = IValue.CreateTensor<float>(inputShape, inputData);
        sessionRuntime.Run(new[] { inputValue });

        // 出力データを取得
        IValue outputValue = sessionRuntime.GetOutputByName("output_name");
        float[] outputData = outputValue.GetTensor<float>().ToArray();

        // 出力データを表示
        Console.WriteLine("Output data: " + string.Join(", ", outputData));
    }
}


このコードは、ONNXモデルを読み込み、入力データを提供し、出力データを取得し、表示します。ONNXモデルのパスを変更して、自分のモデルを使用してください。また、入力データと出力データの名前を、ONNXモデルに基づいて変更してください。

ONNXRuntimeは、C#でONNXモデルを呼び出すためのライブラリです。ONNXRuntimeのインストール方法については、以下のリンクを参照してください。

- [ONNXRuntime for C#](https://github.com/microsoft/onnxruntime/blob/master/docs/Csharp.md)

このコードは、ONNXモデルを呼び出す基本的な例です。実際のアプリケーションでは、エラー処理や入力データの準備など、さらに複雑な処理が必要になる場合があります。
INFO:     127.0.0.1:59264 - "GET /prompt/?q=C%23%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6ONNX%E3%83%A2%E3%83%87%E3%83%AB%E3%82%92%E5%91%BC%E3%81%B3%E5%87%BA%E3%81%99%E3%82%B3%E3%83%BC%E3%83%89%E3%82%92%E4%BD%9C%E6%88%90%E3%81%97%E3%81%A6%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82 HTTP/1.1" 200 OK
``` 
