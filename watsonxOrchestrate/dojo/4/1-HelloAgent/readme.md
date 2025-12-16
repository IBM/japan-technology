# ADKでエージェントを作る
参考資料: [エージェントを作ってみよう！](https://github.ibm.com/ba-techsales-jp/ba-handson-jp/blob/main/docs/wxo_adk/agents.md)

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





