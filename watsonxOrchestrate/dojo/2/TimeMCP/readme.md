# 2. AIエージェントにツールとして、MCPサーバーを追加する

* MCP (Model Context Protocol) は、エージェントがMCPサーバーを通じて外部ツールやデータソースと安全かつ柔軟にやり取りできるようにするための標準規格です。
* このハンズオンでは、Node.js (TypeScript)で作成され公開されている[time-mcp](https://github.com/yokingma/time-mcp/tree/main)をAIエージェントに繋げます。
* [WeatherInfoエージェント](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2/WeatherAgent/readme.md)が出来上がっている状態から出発しています。
* このコンテンツは、[Business Automation Handsonコンテンツ](https://ibm.github.io/ba-handson-jp/wxoagent/tool/#optionmcp)の内容を、最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。

1. Toolset項目を選択し、[Add tool+]をクリックします。

<img width="1178" height="1042" alt="21AddTool" src="https://github.com/user-attachments/assets/5bcaf810-2767-4480-837a-399f775b8240" />

2. [Add a new tool]から[Add from file or MCP server]をクリックします。
   
<img width="1178" height="1042" alt="22AddFromFileOrMCPserver" src="https://github.com/user-attachments/assets/45c94aee-4d0a-409b-bcce-5c432af2387f" />

3. [Add a new tool]から[Import from MCP server]をクリックします。

<img width="1178" height="1042" alt="23ImportFromMCPserver" src="https://github.com/user-attachments/assets/8a34dc8b-cb9d-42a2-936a-d7d0e5cc03b5" />

4. [Import or remove tools from MCP server]から[Add MCP server +]をクリックします。
   
<img width="1178" height="1042" alt="24AddMCPserver" src="https://github.com/user-attachments/assets/3d0534b3-8a50-4e5c-a134-67223f95f950" />

5. [Add MCP server]でパラメータを設定してから、[Connect]をクリックします。
   * Server name: ```time_mcp```
   * Install command: ```npx -y time-mcp```

<img width="1178" height="1042" alt="25AddMCP-Parameters" src="https://github.com/user-attachments/assets/75810d4f-f8ff-4e63-8920-fb4a2ae0d525" />

6. MCP serverへの接続が始まりますので、しばらく待ちます。
   
<img width="1178" height="1042" alt="26Connecting" src="https://github.com/user-attachments/assets/11f84e51-eac6-449d-bea5-e1335405a5db" />

7. ”Connection successful" の文字を確認し、MCP serverへ接続できたら、[Done]をクリックします。
<img width="1134" height="998" alt="27Connected" src="https://github.com/user-attachments/assets/438e2072-6bf4-464c-af30-1c4ff075bb13" />

8. Import or remove tools from MCP serverの画面から、[time_mcp:current_time]の行を探し、トグル・スイッチを[On]にします。

<img width="1178" height="1042" alt="28CurrentTime" src="https://github.com/user-attachments/assets/5b2ec7e8-abd9-41f4-9fcb-116edc1ee160" />

9. Import or remove tools from MCP serverの画面の右上にある[x]をクリックして、画面を閉じます。
    
<img width="1178" height="1042" alt="29Close" src="https://github.com/user-attachments/assets/cfab5cc3-359a-4f70-aeaf-de6b0ac7f1bc" />

10. Toolset項目のToolsに、追加した[time_mcp:current_time]ツールが表示されていることを確認します。
    
<img width="1178" height="1042" alt="30Tools" src="https://github.com/user-attachments/assets/0fcddfc5-af68-4e05-a36e-bd70e0f74ec2" />

11. BehaviorのInstructionsを変更します。
* Instructions: ```回答は日本語で行なってください。
  定型の挨拶は省略し、最初の質問から回答してください。
  current_time toolを使用する際は、formatとして　"YYYY/MM/DD HH:mm"　を指定してください。```

<img width="1178" height="1042" alt="31ToolBehavior" src="https://github.com/user-attachments/assets/f131b2e9-bc1a-4e62-b2b8-3bd61cd9530d" />

12. チャット欄をリセットし、AIエージェントに「```現在のニューヨークの日時は？```」と入力します。他にも地名を指定して質問してみましょう。

<img width="1178" height="1042" alt="32TimeQueries" src="https://github.com/user-attachments/assets/9892cc75-37dd-4f16-af3b-e80567ce6272" />

この演習では、時刻に対する問い合わせに対応するMCP serverに接続し、AIエージェントが時刻に対する質問に回答できるようになりました。

MCPサーバーについては、例えば、[このページ](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file)で定期的に情報が更新されています。
使えそうなMCPサーバーを見つけたら、この演習を参考に、試していきましょう。
