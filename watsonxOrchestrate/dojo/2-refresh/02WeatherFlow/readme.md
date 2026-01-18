# 2. ツールとワークフローを使って気象情報を取得する
* 最終更新日: 2026/01/18
* こちらは、Business Automation Hands-onのwatsonx Orchestrate [Lab 3](https://ibm.github.io/ba-handson-jp/wxoagent/flow/)を最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。
* 問い合わせした地名が米国であるかどうかを判断し、米国以外の国であれば気温を摂氏で、そうでなければ、気温を華氏で回答します。
* 同じ名前のツールを複数回登録すると起きてしまう間違いについて、追記してあります。ご注意ください。

## 参考資料 
* [Agentic Workflows](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=tools-agentic-workflows)
* [Code blocks](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=workflows-code-blocks)
* [Agentic workflow expressions](https://developer.watson-orchestrate.ibm.com/tools/flows/flow_expression)

##

0. 作成するワークフローの全体像
* watsonx Orchestrateのワークフロー作成ツールを利用します。
* 作成するフローは１つの分岐(Branch)を伴うものです。ワークフロー作成ツールの操作に慣れるため、ハンズオンで体験しましょう。
* 気象情報の取得は、WeatherAgentのパートで追加した[current weather for coordinates]ツールを使います
* 条件分岐としてのBranchを1つ作成し、地名をGeocode MCP Serverで緯度・経度に変換する際に得られる国コード country_code が "US" / "us" であるかどうかを判定し、気温の単位を華氏あるいは摂氏として回答するかを分岐します。
* 華氏を単位とした場合、摂氏で表現されている気温を華氏に変換します。（摂氏に華氏を変換するには 9/5をかけてから32を加える）

<img width="1000" height="1142" alt="2-2-1-flowOverview" src="https://github.com/user-attachments/assets/658d8d6f-aa08-4cdd-9be6-0b2bd49fe191" />

1. watsonx Orchestrateを開きます。
URL: お使いの環境に合わせてwatsonx Orchestrateを開いてください。

* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat
* 画面右手にある[Create new agent]をクリックします。
<img width="1223" height="1089" alt="2-2-1-CreateAgent" src="https://github.com/user-attachments/assets/7e4a56d5-59c8-4b6a-8f30-9444c1d21321" />

2. [Create from scratch]タブを選択し、NameとDescriptionを入力します。

* Name:
  ```
  WeatherAgent02
  ```
* Description:
  ```
  気象情報を取得し、回答するエージェントです。
  ```
<img width="1162" height="995" alt="2-2-2-createFromScratch" src="https://github.com/user-attachments/assets/6070abfe-6888-4ad9-a422-12ce5ba24a4d" />

3. [Model]選択のドロップダウン・メニューから[GPT OSS-120B - OpenAI (via Groq)]を選択します。
<img width="1206" height="1039" alt="2-2-3-GPT-model" src="https://github.com/user-attachments/assets/58c9df7f-f38f-45ac-bec4-862de0913630" />

4. 左側の[Toolset]メニューを選択し、[Add tool +]をクリックします。

<img width="1206" height="1039" alt="2-2-4-Addtool" src="https://github.com/user-attachments/assets/dc0676be-609b-481b-8dc3-831ad224c107" />

5. [Add a tool]から[Agentic workflow]をクリックします。

<img width="1206" height="1039" alt="2-2-5-AgenticWorkflow" src="https://github.com/user-attachments/assets/a7756765-86f1-418d-8b71-f0cd60c584e0" />

6. [Name your agentic workflow]から[Name]を入力し、[Start building]をクリックします。

* Name:
  ```
  WeatherFlow
  ```
  
  <img width="1206" height="1039" alt="2-2-6-NameAflow" src="https://github.com/user-attachments/assets/35ce7b92-dc66-4dba-baf6-e58366c94a79" />

7. [WeatherFlow]の設定画面に変わるので、[Description]を入力し、[Done]をクリックします。

* Description:
  ```
  与えられた地名の天気情報を取得する
  ```
<img width="954" height="888" alt="2-2-7-FlowDescription" src="https://github.com/user-attachments/assets/82f0c30a-e8b7-48ea-81be-6b3d912360f9" />


8. [WeatherFlow]のInput/Outputパラメーターを作成します。先に完成状態を確認しましょう。Inputが1、Outputsが8あります。
* Outputsのリストは既定値が1ページ5アイテムになっているので、[Items per page]を[10]に設定してください。
<img width="1250" height="1194" alt="2-2-8-FlowParams" src="https://github.com/user-attachments/assets/ca601aa8-739d-4470-bf9c-eb47755509a3" />

9. Inputパラメーターを作成します。[Add input +]をクリックし、ドロップダウン・リストから[String]を選択します。

<img width="1206" height="1039" alt="2-2-9-AddInput" src="https://github.com/user-attachments/assets/267ab00b-b025-482f-977c-b83c01805fb5" />

10. [Add String input]ダイアログに、[Name]と[Description]を入力し、最後に[Add]をクリックします。
* Name:
  ```
  city_name
  ```
* Description:
  ```
  都市名
  ```
<img width="1206" height="1039" alt="2-2-10-AddStringInput" src="https://github.com/user-attachments/assets/bf3d9f3c-9e6d-4b4e-9096-6b12fb0a4e24" />

11. Outputパラメーターを作成します。[Add output +]をクリックし、ドロップダウン・リストから[String]を選択します。
<img width="1206" height="1039" alt="2-2-11-AddOutput" src="https://github.com/user-attachments/assets/4155e03f-71d2-4aae-b8a6-ba5d5c22cd77" />

12. [Add String output]ダイアログに、[Name]と[Description]を入力し、最後に[Add]をクリックします。
<img width="627" height="385" alt="2-2-12-AddString-Temp" src="https://github.com/user-attachments/assets/5f4d7aa3-cdae-4fc7-8164-bae19bd53393" />

* Name:
  ```
  temp
  ```
  
* Description:
  ```
  気温
  ```

13. 同様の方法で、残りのパラメーターも作成してください。緯度・経度についてはDecimal型、それ以外はString型です。

* Type: String
* Name:
  ```
  country_code
  ```
  
* Description:
  ```
  国コード
  ```
---

* Type: String
* Name:
  ```
  current_weather_code
  ```
  
* Description:
  ```
  現在の気象コード
  ```

---

* Type: String
* Name:
  ```
  last_path_name
  ```
  
* Description:
  ```
  分岐後の処理ノード
  ```
---

* Type: Decimal
* Name:
  ```
  latitude
  ```
  
* Description:
  ```
  緯度
  ```
---

* Type: Decimal
* Name:
  ```
  longitude
  ```
  
* Description:
  ```
  経度
  ```

---

* Type: String
* Name:
  ```
  temp_unit
  ```
  
* Description:
  ```
  気温の単位
  ```

---

* Type: String
* Name:
  ```
  trace_log
  ```
  
* Description:
  ```
  トレースログ
  ```

14. パラメーターが正しく作成されているかどうか、特にTypeとNameが正しく入力されているかを確認します。最後に[Done]をクリックします。
<img width="1250" height="1194" alt="2-2-8-FlowParams" src="https://github.com/user-attachments/assets/f3f94b78-d42a-41ca-ab68-7db855c14394" />


