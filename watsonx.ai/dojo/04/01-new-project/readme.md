# 演習準備
watsonx.ai Dojo #4の演習は、ローカル・コンピューター上でPythonコードを動かし、IBM watsonx.ai APIを利用して、言語モデルへアクセスします。
過去のwatsonx Dojo #2, #3に参加していない人もすぐに取り掛かれるよう、必要なセットアップを記します。

前提条件:
* Windowsの場合、Windows Subsystem Linuxを有効にし、Ubuntu あるいは Ubuntu 22.04.3 LTSが実行できること
* Ubuntu (Windows), Mac 共通: Python 3.10.14がインストールされていること, Python 仮想環境 venv を作ってあること
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

