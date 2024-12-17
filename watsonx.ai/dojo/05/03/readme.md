# InstructLab CLI体験その１ (初期化とモデルのダウンロード)

このハンズオンでは、InstructLabの主な機能を体験していきます。公式文書はこちら。
* コマンドは、InstructLab CLIをインストール済みのUbuntuまたはターミナル上で操作してください。

## 全体像
![ilab](https://github.com/user-attachments/assets/3edcea99-7b89-4225-a1a0-fcfceb456d07)

### 環境の初期化
* 公式文書は[こちら](https://github.com/instructlab/instructlab/tree/main?tab=readme-ov-file#%EF%B8%8F-initialize-ilab)
1. Python仮想環境 ilabが有効になっていることを確認します。
2. 次のコマンドを入力して、InstructLabの環境を初期化します。
```
ilab config init
```

3. ガイドに従って操作を進めます。。Enterキーを押すと、既定の値が設定されます。
* こちらは、Apple M3 Maxを搭載したmacの例です
```
----------------------------------------------------
         Welcome to the InstructLab CLI
  This guide will help you to setup your environment
----------------------------------------------------

Please provide the following values to initiate the environment [press 'Enter' for default options when prompted]

Path to taxonomy repo [/Users/<ユーザー名>/.local/share/instructlab/taxonomy]: Enter

Should I clone https://github.com/instructlab/taxonomy.git for you? [Y/n]: Y

Cloning https://github.com/instructlab/taxonomy.git...
Path to your model [/Users/<ユーザー名>/.cache/instructlab/models/granite-7b-lab-Q4_K_M.gguf]: Enter

Generating config file:
    /Users/<ユーザー名>/.config/instructlab/config.yaml

We have detected the APPLE M3 MAX profile as an exact match for your system.

--------------------------------------------
    Initialization completed successfully!
  You're ready to start using `ilab`. Enjoy!
--------------------------------------------
```
### モデルのダウンロード
* 公式文書は[こちら](https://github.com/instructlab/instructlab/tree/main?tab=readme-ov-file#-download-the-model)
1. 次のコマンドを入力して、モデルをダウンロードします。
```
ilab model download
```
Ubuntu上の出力例:
```
Downloading model from Hugging Face:
    Model: instructlab/granite-7b-lab-GGUF@main
    Destination: /home/ilab/.cache/instructlab/models
Downloading 'granite-7b-lab-Q4_K_M.gguf' to '/home/ilab/.cache/instructlab/models/.cache/huggingface/download/granite-7b-lab-Q4_K_M.gguf.6adeaad8c048b35ea54562c55e454cc32c63118a32c7b8152cf706b290611487.incomplete'
INFO 2024-12-17 02:07:46,015 huggingface_hub.file_download:1536: Downloading 'granite-7b-lab-Q4_K_M.gguf' to '/home/ilab/.cache/instructlab/models/.cache/huggingface/download/granite-7b-lab-Q4_K_M.gguf.6adeaad8c048b35ea54562c55e454cc32c63118a32c7b8152cf706b290611487.incomplete'
granite-7b-lab-Q4_K_M.gguf: 100%|▉| 4.08G/4.08G [00:47<00:00, 85.2MB/
Download complete. Moving file to /home/ilab/.cache/instructlab/models/granite-7b-lab-Q4_K_M.gguf
INFO 2024-12-17 02:08:34,174 huggingface_hub.file_download:1552: Download complete. Moving file to /home/ilab/.cache/instructlab/models/granite-7b-lab-Q4_K_M.gguf
Downloading model from Hugging Face:
    Model: instructlab/merlinite-7b-lab-GGUF@main
    Destination: /home/ilab/.cache/instructlab/models
Downloading 'merlinite-7b-lab-Q4_K_M.gguf' to '/home/ilab/.cache/instructlab/models/.cache/huggingface/download/merlinite-7b-lab-Q4_K_M.gguf.9ca044d727db34750e1aeb04e3b18c3cf4a8c064a9ac96cf00448c506631d16c.incomplete'
INFO 2024-12-17 02:08:34,539 huggingface_hub.file_download:1536: Downloading 'merlinite-7b-lab-Q4_K_M.gguf' to '/home/ilab/.cache/instructlab/models/.cache/huggingface/download/merlinite-7b-lab-Q4_K_M.gguf.9ca044d727db34750e1aeb04e3b18c3cf4a8c064a9ac96cf00448c506631d16c.incomplete'
merlinite-7b-lab-Q4_K_M.gguf: 100%|▉| 4.37G/4.37G [01:08<00:00, 63.5M
Download complete. Moving file to /home/ilab/.cache/instructlab/models/merlinite-7b-lab-Q4_K_M.gguf
INFO 2024-12-17 02:09:43,522 huggingface_hub.file_download:1552: Download complete. Moving file to /home/ilab/.cache/instructlab/models/merlinite-7b-lab-Q4_K_M.gguf
Downloading model from Hugging Face:
    Model: TheBloke/Mistral-7B-Instruct-v0.2-GGUF@main
    Destination: /home/ilab/.cache/instructlab/models

TheBloke/Mistral-7B-Instruct-v0.2-GGUF requires a HF Token to be set.
Please use '--hf-token' or 'export HF_TOKEN' to download all necessary models.
```

2. 次のコマンドを入力して、ダウンロードしたモデルを確認します。
```
ilab model list
```

出力例:
```
+------------------------------+---------------------+--------+
| Model Name                   | Last Modified       | Size   |
+------------------------------+---------------------+--------+
| granite-7b-lab-Q4_K_M.gguf   | 2024-12-17 02:08:34 | 3.8 GB |
| merlinite-7b-lab-Q4_K_M.gguf | 2024-12-17 02:09:43 | 4.1 GB |
+------------------------------+---------------------+--------+
```
3. (オプション）その他、Hugging Face上のモデルをダウンロードする場合は、Hugging Faceのアカウントを作成し、プロファイルページから、Access Tokenを作成してください。
<img width="1942" alt="HFAccessToken" src="https://github.com/user-attachments/assets/36270c91-295b-4e91-859f-76ab52f5cee5" />
* [Create New Token]をクリックすると、必要なアクセス権が表示されます。

Token Name: ```iLab download```

* [Read access to contents of all public gated repos you can access]のみにチェックをつけます。

<img width="1263" alt="hfCreateToken" src="https://github.com/user-attachments/assets/ea73ef57-cb00-4fc0-a4e3-a22420fb94a9" />

* 最後に[Create Token]をクリックしてください。
* 表示された[Save your Access Token]のウィンドウ内にある [Copy]ボタンをクリックして、アクセストークンをコピーします。メモ帳などに保存してください。
* コマンドのオプション --hf-token に指定する、あるいは 環境変数 export HF_TOKEN=hf_xxxx と設定して、アクセストークンを利用してください






