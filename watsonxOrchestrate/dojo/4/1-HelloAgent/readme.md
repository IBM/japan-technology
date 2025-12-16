# ADKでエージェントを作る
* 最終更新日: 2025/12/16
* 参考資料: [エージェントを作ってみよう！](https://github.ibm.com/ba-techsales-jp/ba-handson-jp/blob/main/docs/wxo_adk/agents.md)

## 前提条件
* watsonx Orchestrate ADK 2.1.0 がインストール済みである。
* watsonx Orchestrate Developer版が動作している
* Visual Studio Codeにwatsonx Orchestrate ADK拡張機能がインストールされている
* Windowsの場合、PowerShellを通じてコマンドを実行
* macOSの場合、ターミナルを通じてコマンドを実行

これらの条件が整っていない場合、[watsonx Orchestrate ADK環境構築](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/4/readme.md) を実行して、環境を整えてください。

### ADKがインストール済みで、ローカル版のwatsonx Orchestrateが起動していない場合の対処方法
* macOSの場合:

```
cd ~/wxo
source venv/bin/activate
orchestrate server start -e .\.env
```

* Windowsの場合 (PowerShell):

```
chcp 65001
```

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

```
cd ~/wxo
venv\Scripts\activate
orchestrate server start -e .\.env
```

* (mac/Windows共通) localのwatsonx Orchestrateを有効にする
```
orchestrate env activate local
```

* (mac/Windows共通) localのwatsonx OrchestrateのUI機能を起動する
```
orchestrate chat start
```

## 既存のエージェントの確認
1. コマンドを入力し、Visual Studio Codeを開きます。

```
cd ~/wxo
code .
```
2. Visual Studio Code内の<img width="40" height="41" alt="wxo" src="https://github.com/user-attachments/assets/7ff0b277-720b-47f1-8c3c-0c9309a0178b" />アイコンをクリックして、watsonx OrchestrateのExplorerを開きます。[EXPLORER}>[Agents]のフォルダーを見ると、AskOrchestrateエージェントが確認できます。

<img width="1046" height="806" alt="vscode-wxo-ADK" src="https://github.com/user-attachments/assets/2385db81-b13b-47d5-b01c-187c656c928a" />

3. コマンドを入力し、エージェントの一覧を確認します。

```
orchestrate agents list
```

## 新しいエージェントの作成
4. Visual Studio Codeに戻り、コマンド・パレットを開きます。
＊　macOS: [Shift]+[command]+[p] キー
* Windows: [ctrl]+[Shift]+[p]キー

5. 作成するエージェントの名前をクリップボードにコピーします。
```
finance_agent
```
6. コマンド・パレット内で、[watsonx Orchestrate: create new agent]を選び、[Enter]キーを入力します。

<img width="1056" height="1012" alt="vscode-adk-createNewAgent" src="https://github.com/user-attachments/assets/e507e6b2-9a04-4b0a-8abf-ade9034d32a9" />

7. 作成するエージェントの名前を入力欄が表示されるので、コピー済みの名前を貼り付けます。
* ご注意: 名前の入力欄が表示されている最中に、入力フォーカスを別のウィンドウに変更すると、名前の入力がキャンセルされます。

* コマンド・パレットを選択した直後
<img width="597" height="77" alt="cna-Name" src="https://github.com/user-attachments/assets/1dd494e2-6135-497a-bb69-81d65fbcfbee" />

* finance_agentと入力（クリップボードから貼り付け)した直後
<img width="591" height="72" alt="cna-Finance" src="https://github.com/user-attachments/assets/122bab24-5020-43cf-9d23-c5a7e2e7e7f8" />

8. Visual Studio Code上に finance_agent.yamlのテンプレートが展開されます。
<img width="1046" height="806" alt="finance-yaml-template" src="https://github.com/user-attachments/assets/77d370b2-1e72-4b95-af6f-2ac7401b7c5b" />

```
spec_version: v1
kind: native
style: default
name: 
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
description: >
  You are an agent who specializes in 
instructions: >
  
collaborators:
  - 
tools:
  - 
```

9. finance_agent.yamlを次の内容で上書きします。コピー機能を使って、クリップボードにコピーして、その内容をそのままVisual Studio Codeに貼り付けてください。その後、finance_agent.yamlを保存してください。

```
spec_version: v1
kind: native
style: default
name: finance_agent
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
description: >
  企業情報の専門家のエージェントです。
instructions: >
  企業情報について日本語で回答してください。
```

10. Visual Studio Codeのコマンド・パレットを開き、[watsonx Orchestrate: Import Current File]を選択します。
<img width="600" height="106" alt="adk-import-current" src="https://github.com/user-attachments/assets/555440a7-31aa-46a2-a2a7-633beca4f1c4" />

11. しばらく待つと、[Successfully imported finance_agent.yaml]と表示されます。
<img width="465" height="57" alt="Import-successful" src="https://github.com/user-attachments/assets/8cded511-d832-440d-bb0b-4b37b359ca01" />

12. watsonx Orchestrate Explorerに戻り、[Agents]の行にある<img width="26" height="25" alt="refresh" src="https://github.com/user-attachments/assets/d52b3eac-2758-4f5e-bd11-91eb9b52b9de" /> (refreshアイコン)をクリックします。
<img width="331" height="100" alt="Explorer-beforeRefresh" src="https://github.com/user-attachments/assets/9dea05ac-a039-4664-b837-5a20ce1b44ce" />

13. Explorer画面にエージェントの情報が読み込まれます。

<img width="336" height="118" alt="Explorer-Refreshed" src="https://github.com/user-attachments/assets/5c275cc4-c5ed-48bf-980b-5551834df75b" />

14. [finance_agent]の行にある <img width="20" height="22" alt="chat-icon" src="https://github.com/user-attachments/assets/7416105e-f735-4493-9a24-97f53f5ff4c3" /> (chatアイコン)をクリックします。

15. [finance_agent]のチャット機能が表示されます。

<img width="1046" height="806" alt="finance_agent_chat1" src="https://github.com/user-attachments/assets/6e4fa174-c086-41fe-a4e1-b3fb3bfd6bec" />

16. このエージェントには、まだ呼び出せるツールが組み込まれていませんが、基盤モデルを使った回答ができます。
チャット欄への入力:
```
企業の業績を表す代表的な指標を教えて。
```
* Windows上の実行例
<img width="1020" height="846" alt="chat1-Windows" src="https://github.com/user-attachments/assets/6a45d927-847b-4203-baf6-ffa24c098b4b" />

* mac上の実行例
<img width="1062" height="776" alt="chat1-Mac" src="https://github.com/user-attachments/assets/29c3f977-7a89-4786-89b1-c73f9ce6f4cd" />

## スターター・プロンプトの変更とエージェントの更新
* よくある問い合わせ等、代表的なプロンプトをスターター・プロンプトとしてあらかじめ3つまで定義しておくことが可能です。スターター・プロンプトを定義し、エージェントを更新してみましょう。

17. Visual Studio Codeに戻り、finance_agent.yamlを以下の内容で置き換えます。yamlファイルを閉じてしまった場合は、watsonx Orchestrate Explorerから[finance_agent]をクリックします。表示されるダイアログ・ウィンドウには[Replace]で回答してください。
<img width="277" height="252" alt="replace-yn" src="https://github.com/user-attachments/assets/bae8cfb6-28e0-4d85-b1d6-09fe3bbe3a49" />

```
spec_version: v1
kind: native
style: default
name: finance_agent
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
description: >
  企業情報の専門家のエージェントです。
instructions: >
  企業情報について日本語で回答してください。
welcome_content:
    welcome_message: "企業情報エージェント"
    description: "企業情報についてはお任せください"
starter_prompts:
    is_default_prompts: false
    prompts:
        - id: "prompt_id_1"
          title: "用語のリスト"
          subtitle: "企業の業績に関する指標をリストします。"
          prompt: "企業の業績を表す代表的な指標を5個リストして"
          state: "active"
        - id: "prompt_id_2"
          title: "用語の比較"
          subtitle: "ROAとROEの違いを説明します。"
          prompt: "ROAとROEの意味とその違いを表形式で整理して"
          state: "active"
```
18. 手順10と同様にfinance_agent.yamlの内容をインポートします。Visual Studio Codeのコマンド・パレットを開き、[watsonx Orchestrate: Import Current File]を選択します。[Successfully imported finance_agent.yaml]と表示されるのを待ちます。
<img width="600" height="106" alt="adk-import-current" src="https://github.com/user-attachments/assets/555440a7-31aa-46a2-a2a7-633beca4f1c4" />

19. watsonx Orchestrate Explorerに戻り、[finance_agent]から<img width="20" height="22" alt="chat-icon" src="https://github.com/user-attachments/assets/7416105e-f735-4493-9a24-97f53f5ff4c3" /> (chatアイコン)をクリックします。

20. [企業情報エージェント]が表示されます。うまく表示されない場合は、チャット画面で<img width="28" height="26" alt="reset-icon" src="https://github.com/user-attachments/assets/073d9f09-6a4a-460b-b9c0-90edc4c0eb95" /> (resetアイコン)をクリックします。

<img width="1494" height="846" alt="company-info-agent" src="https://github.com/user-attachments/assets/ad1a86d2-f7f3-4f8f-94bf-fe426f177a0d" />

21. [用語のリスト]や[用語の比較]をクリックして、動作を確認してください。

##
以上、watsonx Orchestrate ADKを使った、AIエージェントの作成体験でした。この次のハンズオンでは、Pythonで作成したツールをこのAIエージェントに連携させます。






