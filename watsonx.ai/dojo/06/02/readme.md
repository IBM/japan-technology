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

3. st_echo.py コードを確認します。Visual Stdio Codeは開いたままにしてください。

```st_echo.py
# st_echo.py
# Streamlitを使って、入力内容をそのまま応答するエコーボットの作成
# 参考: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-bot-that-mirrors-your-input
import streamlit as st

st.title("Echo bot🚀")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("何か入力してください"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):

```

4. 次のコマンドを入力して、Echoボットを起動します。

```
streamlit run st_echo.py
```

5. ブラウザーが起動し、Echoボットが動きます。アプリに入力して、内容がそのまま出力されるのを確認します。

<img width="1241" alt="wxai06-02-echobot" src="https://github.com/user-attachments/assets/0258d524-539c-49af-a532-0ddd7d33b8bb" />

6. 右上の３点メニューをクリックし、[Settings]をクリックします。
<img width="1241" alt="wxai06-02-settings" src="https://github.com/user-attachments/assets/41a15d29-7622-4e4a-9809-08daa5a5038b" />

7. [Run on save]のチェックボックスをオン ☑️ にし、[x]をクリックして、Settings画面を閉じます。
<img width="1241" alt="wxai06-02-runonsave" src="https://github.com/user-attachments/assets/313f1a4e-63c7-40dc-ae1e-ac3ba3abeae7" />

8. Visual Studio Codeに戻り、st_echo.pyの6行目を変更して、保存します。

変更前:

```
st.title("Echo bot🚀")
```

変更後:
```
st.title("エコーボット😃")
```

9. ブラウザーに戻り、エコーボット😃 が表示されていることを確認します。Streamlitの環境がst_echo.pyの変更をトリガーにアプリを動的に更新することがわかります。
<img width="1241" alt="wxai06-02-title-changed" src="https://github.com/user-attachments/assets/e51cc7fc-a579-440e-97ce-027ad88d166d" />




