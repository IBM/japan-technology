# 演習1: watsonx AI推論を実行するための最低限のコードを確認し、実行する
watsonx.ai Dojo #6の最初の演習は、最低限のコードでAI推論を実行します。
新しいプロジェクトを作成し、watsonx.ai Runtimeを関連付けし、プロジェクトIDを取得します。その後、Cloud APIキーを取得します。
AI推論を実行するための最低限のコードを確認し、Pythonから実行して試します。

前提条件:
* IBM watsonx as a Serviceの環境にアクセスできること

### Task 1: 新規プロジェクトの作成

1. Webブラウザーを開き、https://jp-tok.dataplatform.cloud.ibm.com/login?context=wx へアクセスします。
<img width="1533" alt="wxai05-01-login" src="https://github.com/user-attachments/assets/33e9ed75-312d-4f06-bf0a-fe2b20c05412" />


2. お使いのIBM IDを入力して[続行] をクリックします。

3. IBM watsonx が起動します。

4. Webブラウザーから https://jp-tok.dataplatform.cloud.ibm.com/projects/new-project?context=wx へアクセスします。
名前を ```Dojo #6``` と入力して、[作成]をクリックします。
<img width="1337" alt="wxai06-01-newproject" src="https://github.com/user-attachments/assets/9af0d6e6-6fb1-4bce-9ab5-9bbf234f4f6e" />


5. プロジェクトの概要ページが開くので[管理]をクリックします。
<img width="1337" alt="wxai06-01-manage-project" src="https://github.com/user-attachments/assets/128000cd-62aa-4f20-b13c-a90076ee41e7" />

6. プロジェクトの管理ページの左側にある[サービスおよび統合]をクリックします。[サービスの関連付け +]をクリックします。
<img width="1337" alt="wxai06-01-service-integration" src="https://github.com/user-attachments/assets/27bb682a-38d9-419c-b8b4-0c637a300da8" />

7. Watson Machine Learning または watsonx.ai Runtime のサービスが表示されるので、リストの左側にあるチェックボックスをクリックします。続いて、[アソシエイト]をクリックします。
<img width="1337" alt="wxai06-01-associates-airuntime" src="https://github.com/user-attachments/assets/d6e731c2-de8a-4d6a-9e3b-15a23a96fb03" />

8. watsonx.ai Runtime (Watson Machine Learning)のサービスが関連づけられたことを確認します。
* Watson Machine Learningはwatsonx.ai Runtimeに名前が変わりました。
<img width="1337" alt="wxai06-01-associated" src="https://github.com/user-attachments/assets/68899c35-0407-4884-97dd-97d85e3c68ba" />

9. [管理] タブの左メニューから[一般]をクリックし、画面中央付近にある[プロジェクトID]の下に表示されているIDをコピーします。[クリップボードにコピー]をクリックします。このIDは、Visual Studio Codeやメモ帳などに貼り付けて、後から使えるようにしてください。
<img width="1337" alt="wxai06-01-copy-projectid" src="https://github.com/user-attachments/assets/d1c67ede-96d5-4eb4-8c76-04c5ebf6d881" />


### Task 2: APIキーの取得
1. ブラウザーから別のタブを開いて、https://cloud.ibm.com/iam/apikeys へアクセスします。ページが開いたら、[作成 +]をクリックします。
<img width="1698" alt="wxai06-01-cloud-apikey" src="https://github.com/user-attachments/assets/661a7fc2-eab7-496e-8414-2a1b1ed4c885" />

2. IBM Cloud APIキーの作成画面が開きます。[名前]を[wxdojo06]と入力して、[作成]をクリックします>
<img width="1698" alt="wxai06-01-create-apikey" src="https://github.com/user-attachments/assets/876fbfa0-cdd4-44fa-b4cc-25b997c9d1e8" />

3. APIキーは正常に作成されました、と表示されます。[ダウンロード]をクリックして、APIキーを含んだファイルをダウンロードします。
<img width="1698" alt="wxai06-01-download-apikey" src="https://github.com/user-attachments/assets/ee4aa31c-c5d4-4f55-ba50-bf6ab9411552" />

4. Visual Studio Codeを使って、ダウンロードした apikey.json を開きます。APIキーを確認します。このキーは他の人に知られないように管理してください。特にインターネットに公開しているGitHubのリポジトリにAPIキーを共有することはお控えください。

```
{
	"name": "wxdojo06",
	"description": "",
	"createdAt": "2025-01-06T03:14+0000",
	"apikey": "<ここに表示されている内容がAPIキーとなります>"
}
```

### Task 3: 推論のための最低限のコードを確認、実行

1. Windowsの場合はUbuntu、Macの場合はターミナルを開きます。Python仮想環境 venvに入ります。以降の手順でコマンドはこのvenv環境下、~/wxaiディレクトリーで実行します。

```
cd ~/wxai
source venv/bin/activate
```

2. このハンズオンで利用するテキストファイルをダウンロードします。

```
wget https://raw.githubusercontent.com/IBM/japan-technology/refs/heads/main/watsonx.ai/dojo/06/simple_generate.py
```

もし、MacOSでwgetコマンドが見つからない場合は、wgetをインストールしてから、上のコマンドを実行します。

```
brew install wget
```

3. Visual Studio CodeでダウンロードしたPythonファイルを開きます。

```
code simple_generate.py
```

4. コードを確認します。

```
# simple_generate.py
# watsonx.ai 言語モデルによる推論処理の最小コード
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference

credentials = Credentials(
    url = "https://jp-tok.ml.cloud.ibm.com",
    api_key = "<APIキー>"
)

client = APIClient(credentials)
model = ModelInference(
    model_id="ibm/granite-3-8b-instruct",
    api_client=client,
    project_id= "<プロジェクトID>",
    params = {
      "max_new_tokens": 500
    }
)

prompt = "C#を使ってONNXモデルを呼び出すコードを作成してください。"
print(model.generate_text(prompt))
```

5. Visual Studio Codeを使い、Task 1で取得したプロジェクトIDとTask 2で取得したAPIキーを、それぞれ<プロジェクトID>、<APIキー>と置き換えます。それぞれ、コピーしたものを貼り付けてください。simple_generate.pyを保存します。

6. ターミナルまたはUbuntuに戻り、Pythonコードを実行します。

```
python simple_generate.py > onnx.md
```

7. 出力を確認します。出力トークン数を500に制限しているので、内容が途中までとなりますが、この演習では気にしないでください。
出力内容はmarkdown形式になっています。Visual Studio Codeのmarkdownプレビュー機能が使えます。

キーボードショートカット
* Windowsの場合: [Ctrl]+[k]を押してから[v]
* MacOSの場合] [Command]+[k]を押してから[v]

```
code onnx.md
```

--- ここから ---
以下は、C#でONNXモデルを呼び出すコードの例です。

```csharp
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

このコードは、
---- ここまで ---
