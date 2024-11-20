# LangChainによるRAG、演習準備
watsonx.ai Dojo #4の演習は、ローカル・コンピューター上でPythonコードを動かし、IBM watsonx.ai APIを利用して、言語モデルへアクセスします。
過去のwatsonx Dojo #2, #3に参加していない人もすぐに取り掛かれるよう、必要なセットアップを記します。

前提条件:
* Windowsの場合、Windows Subsystem Linuxを有効にし、Ubuntu あるいは Ubuntu 22.04.3 LTSが実行できること
* Ubuntu (Windows), Mac 共通: Python 3.10.14がインストールされていること, Python 仮想環境 venv を作ってあること (念の為、Python 3.12.6でも動作を確認しています)
* Python環境構築の参考資料: [watsonx.ai Dojo #1準備編](https://speakerdeck.com/oniak3ibm/wxaidojo01-20240821 "watsonx.ai Dojo #1") スライド28からスライド31を参照

##

1. Windowsの場合はUbuntu、Macの場合はターミナルを開きます。コマンドを実行して、Python仮想環境 venvに入ります。
```
cd ~/wxai
source venv/bin/activate
```

上記コマンドがエラーとなる場合、次の2点を確認しましょう。
* 確認1: ホーム・ディレクトリーに wxai フォルダがない場合は、Ubuntu(Windows)またはターミナル(Mac)から、次のコマンドを実行して作成します。

```
cd ~
mkdir wxai
cd wxai
```

* 確認2: venvというPython仮想環境がない場合は、Ubuntuまたはターミナルから、次のコマンドを実行して作成します。
```
cd ~/wxai
python -m venv venv
source venv/bin/activate
```

2. Python仮想環境 venv内で必要なPythonパッケージをインストール、すでにインストールされていればアップデートします。Ubuntu(Windows)またはターミナル(Mac)から、次のコマンドを実行します。
* 以降、watsonx.ai Dojo #4では、コマンドの実行は ~/wxai フォルダー内だけで実行します。

pipの更新
```
python -m pip install --upgrade pip
```

IBM Cloud SDK Core
```
pip install -U ibm_cloud_sdk_core
```

IBM watsonx
```
pip install -U ibm_watsonx_ai
```

Hugging Face Transformers
```
pip install -U transformers 
```

sentencepiece
```
pip install -U sentencepiece
```

langchain
```
pip install -U langchain
```

langchain_ibm
```
pip install -U langchain_ibm
```

langchain_chroma
```
pip install -U langchain_chroma
```

langchain_huggingface
```
pip install -U langchain_huggingface
```

langchain_community
```
pip install -U langchain_community
```
3. Webブラウザーを開き、https://jp-tok.dataplatform.cloud.ibm.com/login?context=wx へアクセスします。
<img width="1548" alt="スクリーンショット 2024-09-14 16 28 14" src="https://github.com/user-attachments/assets/a0420116-4506-4917-bf70-1a08c8e67bc4">
4. お使いのIBM IDを入力して[続行] をクリックします。

5. IBM watsonx が起動します。

6. Webブラウザーから https://jp-tok.dataplatform.cloud.ibm.com/projects/new-project?context=wx へアクセスします。

<img width="1193" alt="wxai04-01-01-newproject" src="https://github.com/user-attachments/assets/2fce5cee-f301-4c9f-8554-6b08e8744ae5">
7. プロジェクトの概要ページが開くので[管理]をクリックします。
<img width="1193" alt="wxai04-01-02-projoverview" src="https://github.com/user-attachments/assets/1cf750c5-013e-4dcd-9fd9-1bead114a9cf">

8. プロジェクトの管理ページが開くので[詳細]欄にある[プロジェクトID]を見つけ、[クリップボードにコピー]をクリックします。このIDは、Visual Studio Codeやメモ帳などに貼り付けてください。
<img width="1193" alt="wxai04-01-03-projectId" src="https://github.com/user-attachments/assets/a32621e2-b3ea-4f3b-a5b0-a31071176306">

9. プロジェクトの管理ページの左側にある[サービスおよび統合]をクリックします。[サービスの関連付け +]をクリックします。

<img width="1193" alt="wxai04-01-04-serviceintegration" src="https://github.com/user-attachments/assets/d0e6dd0a-da05-413e-b46c-a8a0cbd0eb1b">

10. Watson Machine Learningのサービスが表示されるので、リストの左側にあるチェックボックスをクリックします。続いて、[アソシエイト]をクリックします。
<img width="1193" alt="wxai04-01-05-AssociatesWML" src="https://github.com/user-attachments/assets/6510fb65-571a-487a-9996-9693c7e1f715">

11. Watson Machine Learningのサービスが関連づけられたことを確認します。

<img width="1193" alt="wxai04-01-06-associatedWML" src="https://github.com/user-attachments/assets/44d20a10-1872-42aa-9a0e-429b0917cb61">

12. ブラウザーから別のタブを開いて、https://cloud.ibm.com/iam/apikeys へアクセスします。ページが開いたら、[作成 +]をクリックします。

<img width="1193" alt="wxai04-01-08-APIKey" src="https://github.com/user-attachments/assets/81dcde8d-1c74-49b2-b3fd-d40061974db3">

13. IBM Cloud APIキーの作成画面が開きます。[名前]を[dojo04]と入力して、[作成]をクリックします>
<img width="1193" alt="wxai04-01-09-createAPIkey" src="https://github.com/user-attachments/assets/c00af974-fe49-4a7c-ad58-802b9a26c1a8">

14. APIキーは正常に作成されました、と表示されます。[ダウンロード]をクリックして、APIキーを含んだファイルをダウンロードします。

<img width="1193" alt="wxai04-01-10-APIKey-Download" src="https://github.com/user-attachments/assets/f3609cf9-a742-4936-b686-f6d5d92ac9aa">

15. ダウンロードした apikey.json ファイルをVisual Studio Codeで開きます。次のような形式になっています。"apikey": の右側にあるキーがAPI Keyとなります。これは他の人に見られないようしてください。watsonx.ai Dojoのセッション中に、Microsoft Teamsのチャットに書き込まないようご注意ください。
```
{
	"name": "dojo04",
	"description": "",
	"createdAt": "2024-11-10T06:51+0000",
	"apikey": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX_XXXXXXXXXXXXXX"
}
```


