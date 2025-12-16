# watsonx Orchestrate ADK体験
* 最終更新日: 2025/12/15
* このハンズオンでは、watsonx Orchestrate ADKをインストールし、ローカル環境で動くwatsonx Orchestrate Developer版を構築します。

## watsonx Orchestrate SaaS環境の region、API Key、Service instance URLの取得
準備方法は[こちら](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/readme.md)

1. お使いの環境に合わせてwatsonx Orchestrateを開いてください。
* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat

<img width="1289" height="1044" alt="01-wxoSaaS" src="https://github.com/user-attachments/assets/65cdb30e-f30b-43f6-8f02-ab641f194ec5" />

2. watsonx Orchestrateを開いたら、右上の丸いアイコンをクリックして、プロファイルを確認します。
<img width="328" height="525" alt="02-Profile" src="https://github.com/user-attachments/assets/eb35485e-cbf6-4aa7-b9e1-2b2a17155f9c" />

Region と表示されている直後の文字列をVS Codeやメモ帳などに控えてください。

3. [Settings]メニューを選択します。

<img width="1289" height="813" alt="03-Settings" src="https://github.com/user-attachments/assets/0f20a946-013f-4010-9c18-81f4622ae71f" />

4. [API details]タブを選択します。
<img width="1289" height="813" alt="04-API-Detail" src="https://github.com/user-attachments/assets/a315ec0b-6dc7-4bbc-a5e7-46864efd7180" />

5. [Generate API key]をクリックします。[Copy]をクリックして、キーをコピーしたら、メモ帳などに控えてください。
* セキュリティーのため、キーは表示されません。関係のない人にAPI keyを共有しないようご注意ください。
<img width="1289" height="813" alt="05-GeneratedAPIkey" src="https://github.com/user-attachments/assets/5102a191-a85d-49cd-9f9c-ac800896b7fd" />

6. [Service instance URL]と書かれている下にある、URLをコピーし、VS Codeやメモ帳などに控えてください。

## watsonx Orchestrate ADK 2.1.0のインストール

* Windows環境における注意点: WSLのLinux環境へのインストールはできません。
* Pythonパッケージマネージャーは pipを使います。watsonx Orchestrate ADK 2.1.0はuvに対応していないので、uv経由で作成した仮想環境、uvでインストールしたPythonパッケージを識別できません。
7. ローカル・コンピューターにPython 3.11以上がインストールされていることを確認してください。

macOSの場合は、ターミナルを開きます。以降のコマンド入力は同じターミナルで実行します。
＊ [macOS] Pythonのバージョンを確認します。
```
python --version
```

Windows OSの場合は、PowerShellを開きます。以降のコマンド入力は同じPowerShellで実行します。

* [Windows] Code PageをUTF-8にします。
```
chcp 65001
```
＊ [Windows] PowerShell内でのスクリプト実行を許可します。
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
＊ [Windows] Pythonのバージョンを確認します。
```
python --version
```

8. 作業用のフォルダーを作成してください。ここでは、ホーム・ディレクトリ（ユーザー用のフォルダ）の下にwxoフォルダーを作っています。

```
mkdir ~/wxo
cd ~/wxo
```

9. venvという名前で、Pythonの仮想環境を作成します。
* ADKのインストールを通じて、多くのPythonパッケージがインストールされます。既存のPython環境と独立したものにするために、仮想環境を使います。

```
python -m venv venv
```

10. 仮想環境 venvを有効化します。

macOSの場合:
```
source venv/bin/activate
```

Windowsの場合:
```
venv\Scripts\activate
```

11. pipコマンドのインストールまたは更新を行います。

```
python -m pip install --upgrade pip
```

12. IBM watsonx Orchestrate 2.1.0をインストールします。

```
pip install --upgrade ibm-watsonx-orchestrate==2.1.0
```
## watsonx Orchestrate Developer Editionのインストール
### 環境変数を .envファイルへ保存
13. Visual Studio Codeを開きます。codeコマンドのPATHを設定していない場合は、Visual Studio Codeを開き、コマンドパレットから```Command: Install 'code' command in PATH command```を実行してください。

```
code .env
```

14. 次の何れかの方法で、.envファイルの中身を作成し、保存します。 
参考: https://developer.watson-orchestrate.ibm.com/developer_edition/wxOde_setup
* 30日無償評価版をお使いの場合:
全ての行をコピーして、.envファイルに貼り付けた後、<>の部分を適宜、置き換えてください。<>の記号は不要です。
```
WO_DEVELOPER_EDITION_SOURCE=orchestrate
WO_INSTANCE=<Service instance URL、上記手順6>
WO_API_KEY=<API key、上記手順5>
ASSISTANT_LLM_API_BASE=https://ap-southeast-1.ml.cloud.ibm.com/
ASSISTANT_EMBEDDINGS_API_BASE=https://ap-southeast-1.ml.cloud.ibm.com/
ROUTING_LLM_API_BASE=https://ap-southeast-1.ml.cloud.ibm.com/
WATSONX_URL=https://ap-southeast-1.ml.cloud.ibm.com/
```

* IBM TechZoneをお使いの場合 (us-southリージョン):
全ての行をコピーして、.envファイルに貼り付けた後、<>の部分を適宜、置き換えてください。<>の記号は不要です。

```
WO_DEVELOPER_EDITION_SOURCE=orchestrate
WO_INSTANCE=<Service instance URL、上記手順6>
WO_API_KEY=<API key、上記手順5>
ASSISTANT_LLM_API_BASE=https://us-south.ml.cloud.ibm.com/
ASSISTANT_EMBEDDINGS_API_BASE=https://us-south.ml.cloud.ibm.com/
ROUTING_LLM_API_BASE=https://us-south.ml.cloud.ibm.com/
WATSONX_URL=https://us-south.ml.cloud.ibm.com/
```

15. watsonx Orchestrate Developer版のコンテナ展開先をローカルにあるDocker環境を指定します。
* 環境がない方は [Rancher Desktop by SUSE](https://rancherdesktop.io/) などをDocker環境をインストールしてください。
```
orchestrate settings docker host --user-managed
```
* orchestrateコマンドが動作しない場合は、手順12をご確認ください。

16. watsonx Orchestrate Developer版のコンテナをダウンロードして、ローカル版のサーバー機能を起動します。
* コンテナ・イメージをダウンロードする際に、通信がタイムアウトになるなど、エラーが生じる場合があります。エラーが発生したら、少し待ってから、同じコマンドを再実行してください。
* 多くのコンテナ・イメージを利用するため、気長にお待ちください。
```
orchestrate server start -e .\.env
```

* 起動時の出力例:
```
(venv) PS C:\Users\oniak3\wxo> orchestrate server start -e .\.env
[INFO] - Auto-detecting local IP address for async tool callbacks...
[INFO] - Using Docker internal URL: http://host.docker.internal:4321
[INFO] - For external tools, consider using ngrok or similar tunneling service.
[WARNING] - Using user managed docker installation, this configuration is not officially supported
[INFO] - Running docker compose-up...
[INFO] - Logging into Docker registry inside NativeDockerManager: registry.ap-southeast-1.dl.watson-orchestrate.ibm.com ...
[INFO] - Successfully logged into Docker.
[INFO] - Detected architecture: AMD64, using DBTAG: 11-12-2025-64d224e
[INFO] - Starting docker-compose WxO Server DB service inside NativeDockerManager...
[INFO] - Database container started successfully. Now starting other services...
[INFO] - Starting docker-compose services...
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"HOME\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WATSONX_APIKEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"HOME\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WATSONX_APIKEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ASSISTANT_EMBEDDINGS_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"BAM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WATSONX_APIKEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ROUTING_LLM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ASSISTANT_LLM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WATSONX_APIKEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ASSISTANT_EMBEDDINGS_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"SKILLS_CATALOG_ENDPOINT\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WATSONX_APIKEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WXO_AWS_IAM_URL\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ASSISTANT_LLM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"BAM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"TEAM_SERVER_ENDPOINT\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WXO_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ROUTING_LLM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WATSONX_APIKEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ROUTING_LLM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"BAM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ASSISTANT_LLM_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"ASSISTANT_EMBEDDINGS_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:35:50+09:00" level=warning msg="The \"WATSONX_APIKEY\" variable is not set. Defaulting to a blank string."
[+] Running 15/16
[+] Running 15/16edition-wxo-server-db-1                  Running   0.0s
[+] Running 15/16edition-wxo-server-db-1                  Running   0.0s
[+] Running 14/16edition-wxo-server-db-1                  Running   0.0s
[+] Running 14/16edition-wxo-server-db-1                  Waiting   0.3s
[+] Running 14/16edition-wxo-server-db-1                  Waiting   0.4s
[+] Running 14/16edition-wxo-server-db-1                  Waiting   0.5s
[+] Running 14/16edition-wxo-server-db-1                  Waiting   0.6s
[+] Running 14/16edition-wxo-server-db-1                  Waiting   0.7s
[+] Running 16/17edition-wxo-server-db-1                  Waiting   0.8s
 ✔ Container dev-edition-wxo-server-db-1                  Healthy   0.8s
[+] Running 17/17edition-wxo-builder-1                    Running   0.0s
 ✔ Container dev-edition-wxo-server-db-1                  Healthy   0.8s
 ✔ Container dev-edition-wxo-builder-1                    Running   0.0s
 ✔ Container dev-edition-wxo-server-minio-1               Healthy   0.8s
 ✔ Container dev-edition-ai-gateway-1                     Running   0.0s
 ✔ Container dev-edition-wxo-agent-gateway-1              Running   0.0s
 ✔ Container dev-edition-wxo-server-redis-1               Running   0.0s
 ✔ Container dev-edition-ui-1                             Removed   0.3s
 ✔ Container dev-edition-wxo-server-connection-manager-1  Running   0.0s
 ✔ Container dev-edition-tools-runtime-1                  Running   0.0s
 ✔ Container dev-edition-wxo-tempus-runtime-1             Running   0.0s
 ✔ Container dev-edition-tools-runtime-manager-1          Running   0.0s
 ✔ Container dev-edition-wxo-milvus-etcd-1                Running   0.0s
 ✔ Container dev-edition-socket-handler-1                 Running   0.0s
 ✔ Container dev-edition-wxo-milvus-standalone-1          Running   0.0s
 ✔ Container dev-edition-wxo-server-worker-1              Running   0.0s
 ✔ Container dev-edition-wxo-server-1                     Running   0.0s
 ✔ Container dev-edition-wxo-server-minio-setup-1         Started   0.2s
[INFO] - Services started successfully.
[INFO] - Running DB migrations inside NativeDockerManager...
time="2025-12-16T11:36:51+09:00" level=warning msg="The \"HOME\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:36:51+09:00" level=warning msg="The \"WXO_AWS_IAM_URL\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:36:51+09:00" level=warning msg="The \"SKILLS_CATALOG_ENDPOINT\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:36:51+09:00" level=warning msg="The \"TEAM_SERVER_ENDPOINT\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:36:51+09:00" level=warning msg="The \"WXO_API_KEY\" variable is not set. Defaulting to a blank string."
time="2025-12-16T11:36:51+09:00" level=warning msg="The \"HOME\" variable is not set. Defaulting to a blank string."
Skipping already applied migration: 00_init_db.sql
Skipping already applied migration: 01_create_tables.sql
Skipping already applied migration: 02_triggers_and_functions.sql
Skipping already applied migration: 03_security.sql
Skipping already applied migration: 04_rls_policies.sql
Skipping already applied migration: 20240508.sql
Skipping already applied migration: 20240606.sql
Skipping already applied migration: 20240628.sql
Skipping already applied migration: 20240701.sql
Skipping already applied migration: 20240704.sql
Skipping already applied migration: 20240714.sql
Skipping already applied migration: 20240724.sql
Skipping already applied migration: 20240807.sql
Skipping already applied migration: 20240830.sql
Skipping already applied migration: 20241029.sql
Skipping already applied migration: 20241113.sql
Skipping already applied migration: 20241125.sql
Skipping already applied migration: 20241210.sql
Skipping already applied migration: 20250108.sql
Skipping already applied migration: 20250114.sql
Skipping already applied migration: 20250211.sql
Skipping already applied migration: 20250310.sql
Skipping already applied migration: 20250403.sql
Skipping already applied migration: 20250404.sql
Skipping already applied migration: 20250408.sql
Skipping already applied migration: 20250414.sql
Skipping already applied migration: 20250422.sql
Skipping already applied migration: 20250501.sql
Skipping already applied migration: 20250502.sql
Skipping already applied migration: 20250512.sql
Skipping already applied migration: 20250513.sql
Skipping already applied migration: 20250514.sql
Skipping already applied migration: 20250518.sql
Skipping already applied migration: 20250519.sql
Skipping already applied migration: 20250523.sql
Skipping already applied migration: 20250528.sql
Skipping already applied migration: 20250530.sql
Skipping already applied migration: 20250602.sql
Skipping already applied migration: 20250605.sql
Skipping already applied migration: 20250609.sql
Skipping already applied migration: 202506117.sql
Skipping already applied migration: 20250611.sql
Skipping already applied migration: 20250612.sql
Skipping already applied migration: 20250613.sql
Skipping already applied migration: 20250614.sql
Skipping already applied migration: 20250616.sql
Skipping already applied migration: 20250619.sql
Skipping already applied migration: 20250620.sql
Skipping already applied migration: 20250622.sql
Skipping already applied migration: 20250626.sql
Skipping already applied migration: 20250627.sql
Skipping already applied migration: 20250704.sql
Skipping already applied migration: 20250707.sql
Skipping already applied migration: 20250708.sql
Skipping already applied migration: 20250711.sql
Skipping already applied migration: 20250718.sql
Skipping already applied migration: 20250729_NOT_FOR_ON_PREM.sql
Skipping already applied migration: 20250808.sql
Skipping already applied migration: 20250820.sql
Skipping already applied migration: 20250821.sql
Skipping already applied migration: 20250822.sql
Skipping already applied migration: 20250825.sql
Skipping already applied migration: 20250828.sql
Skipping already applied migration: 20250829.sql
Skipping already applied migration: 20250901.sql
Skipping already applied migration: 20250903.sql
Skipping already applied migration: 20250909.sql
Skipping already applied migration: 20250910.sql
Skipping already applied migration: 20250912.sql
Skipping already applied migration: 20250918.sql
Skipping already applied migration: 20250919.sql
Skipping already applied migration: 20250924.sql
Skipping already applied migration: 20250925.sql
Skipping already applied migration: 20250926.sql
Skipping already applied migration: 20251001.sql
Skipping already applied migration: 20251006.sql
Skipping already applied migration: 20251007.sql
Skipping already applied migration: 20251008.sql
Skipping already applied migration: 20251009.sql
Skipping already applied migration: 20251022.sql
Skipping already applied migration: 20251023.sql
Skipping already applied migration: 20251029.sql
Skipping already applied migration: 20251101.sql
Skipping already applied migration: 20251103.sql
Skipping already applied migration: 20251104.sql
Skipping already applied migration: 20251107.sql
Skipping already applied migration: 20251110.sql
Skipping already applied migration: 20251111.sql
Skipping already applied migration: 20251112.sql
Skipping already applied migration: 20251120.sql
Skipping already applied migration: 20251121.sql
Skipping already applied migration: 20251124.sql
Skipping already applied migration: 20251125.sql
Skipping already applied migration: 20251128.sql
Skipping already applied migration: 20251201.sql
Existing wxo_observability DB found
Skipping already applied observability migration: 00_init_db.sql
Skipping already applied observability migration: 01_create_tables.sql
Skipping already applied observability migration: 02_triggers_and_functions.sql
Skipping already applied observability migration: 03_security.sql
Skipping already applied observability migration: 04_rls_policies.sql
Skipping already applied observability migration: 20250116.sql
Skipping already applied observability migration: 20251201.sql
[INFO] - Migration ran successfully.
[INFO] - Waiting for orchestrate server to be fully initialized and ready...
[INFO] - Orchestrate services initialized successfully
[INFO] - local tenant found
[INFO] - You can run `orchestrate env activate local` to set your environment or `orchestrate chat start` to start the UI service and begin chatting.
```

17. ローカル版のwatsonx Orchestrate を有効化します。
```
orchestrate env activate local
```
出力例:
```
[INFO] - local tenant found
[INFO] - Environment 'local' is now active
```

18. ローカル版のwatsonx Orchestrateのチャット機能を起動します。
```
orchestrate chat start
```

出力例:
```
[WARNING] - Using user managed docker installation, this configuration is not officially supported
[INFO] - local tenant found
[INFO] - Auto-detecting local IP address for async tool callbacks...
[INFO] - Using Docker internal URL: http://host.docker.internal:4321
[INFO] - For external tools, consider using ngrok or similar tunneling service.
[INFO] - Waiting for orchestrate server to be fully started and ready...
[INFO] - Starting docker-compose UI service inside NativeDockerManager...
[INFO] - Chat UI Service started successfully.
[INFO] - Waiting for UI component to be initialized...
[INFO] - Opening chat interface at http://localhost:3000/chat-lite
[WARNING] - When using local chat, requests that the user 'Connect Apps' must be resolved by running `orchestrate connections set-credentials`
```

19. 自動的にブラウザーが開き、watsonx Orchestrateの画面が表示されます。
<img width="1920" height="1080" alt="wxoLaunched" src="https://github.com/user-attachments/assets/033d4616-c8a3-439d-9506-0c99a4cc738c" />

* すでに3000番ポートが利用されているとエラーになります。3000番ポートを使っているプロセスを終了する方法を示します。
macOSの場合:
```
lsof -ti:3000 | xargs kill -9
```

Windowsの場合: netstatを使って、プロセスIDを探し、taskkillでそのIDを指定する
```
netstat -nao | find "3000"
taskkill /pid <Process ID>
```


