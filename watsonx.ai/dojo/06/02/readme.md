# Streamlitでチャットボットを作ってみる
最低限のコードでAI推論を実行できることが確認できたら、このコードを発展させて、チャットボットに変えてみます。
この演習ではStreamlitをインストールし、入力をそのまま出力するEchoボットを作ります。その後、AI推論を組み込んだコードを実行します。

前提条件:
* IBM watsonx as a Serviceの環境にアクセスできること

### Task 1: Hello Streamlit
1. Windowsの場合はUbuntu、Macの場合はターミナルを開きます。Python仮想環境 venvに入ります。以降の手順でコマンドはこのvenv環境下、~/wxaiディレクトリーで実行します。

```
cd ~/wxai
source venv/bin/activate
```

2. Streamlitをインストールします。

```
pip install streamlit
```

3. Streamlitをテスト実行します。ローカルURL: http://localhost:8501 にWebサービスが起動し、自動的にブラウザーが開きます。

```
streamlit hello
```
<img width="1241" alt="wxai06-02-streamlit-hello" src="https://github.com/user-attachments/assets/7bb713dc-2df5-46f3-bcb5-413bcf4a42fd" />

4. Ubuntuまたはターミナルに戻り、[ctrl]+[c]でプロセスを終了します。

### Task 2: Echoボットの実行と改造

1. Echoボットのソースコード st_echo.py をダウンロードします。

```
wget https://raw.githubusercontent.com/IBM/japan-technology/refs/heads/main/watsonx.ai/dojo/06/st_echo.py
```

もし、MacOSでwgetコマンドが見つからない場合は、wgetをインストールしてから、上のコマンドを実行します。

```
brew install wget
```

2. Visual Studio Codeでst_echo.pyを開きます。

```
code st_echo.py
```


