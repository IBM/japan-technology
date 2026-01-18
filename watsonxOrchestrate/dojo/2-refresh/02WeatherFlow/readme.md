# 2. 気象情報を取得するワークフローを作成する
* 最終更新日: 2026/01/18
* こちらは、Business Automation Hands-onのwatsonx Orchestrate [Lab 3](https://ibm.github.io/ba-handson-jp/wxoagent/flow/)を最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。
* 問い合わせした地名が米国であるかどうかを判断し、米国以外の国であれば気温を摂氏で、そうでなければ、気温を華氏で回答します。


## 参考資料 
* [Agentic Workflows](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=tools-agentic-workflows)
* [Code blocks](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=workflows-code-blocks)
* [Agentic workflow expressions](https://developer.watson-orchestrate.ibm.com/tools/flows/flow_expression)

##

0. 作成するワークフローの全体像
* [演習1](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2-refresh/01WeatherAgent/readme.md)が完了している状態で、名前の異なる新しいAIエージェントを作ります。
* watsonx OrchestrateのAgentic Workflow作成ツールを利用します。
* 作成するフローは１つの分岐(Branch)を伴うものです。ワークフロー作成ツールの操作に慣れるため、ハンズオンで体験しましょう。

フローの説明:
* step 1: [Geocode:geocode] ツール： 指定された地名から、緯度・経度、国コードを取得します。結果はJSON文字列となります。

Geocode:geocodeの出力例 (addressdetail=1, q=静岡市):

```
[
  {
    "place_id": 243339469,
    "osm_type": "relation",
    "osm_id": 4674742,
    "lat": "34.9751974",
    "lon": "138.3831697",
    "category": "boundary",
    "type": "administrative",
    "place_rank": 16,
    "importance": 0.6257569776868801,
    "addresstype": "city",
    "name": "静岡市",
    "display_name": "静岡市, 静岡県, 420-8602, 日本",
    "address": {
      "city": "静岡市",
      "province": "静岡県",
      "ISO3166-2-lvl4": "JP-22",
      "postcode": "420-8602",
      "country": "日本",
      "country_code": "jp"
    },
    "boundingbox": [
      "34.8019562",
      "35.6459570",
      "138.0829590",
      "138.6539534"
    ]
  }
]
```

* step 2: [Json-loader] Python Code block、[Geocode:geocode]の戻り値から、出力として、緯度(latitude)、経度(longitude)、国コード(country_code)を取得します。デバッグ用にtrace_logという文字列を用意します。

* step 3: [current weather for coordinates]ツール、step 2で得られた緯度・経度を利用して、現在の気象情報を取得します。

* step 4: step 2で得られた国コードを利用して、分岐を作ります。米国の場合 (country_code == 'us' / 'US') はUSA Codeblock (Step 5)、それ以外はNot USA Codeblock (Step 6)へ進みます。

* step 5: 米国の場合 (USA Code block)、step 3で得られた気象情報を使い、気温を摂氏から華氏に変換（摂氏に華氏を変換するには 9/5をかけてから32を加える）します。気温の単位を"°F 華氏"に設定します。

USA Code blockの出力(String型): temp_celsius (摂氏の気温）, temp_fahrenheit(華氏の気温), temp_unit(気温の単位), trace_log(トレースログ)

* step 6: 米国ではない場合 (Not USA Code block)、step 3で得られた気象情報を使い、気温の単位を"℃ 摂氏"に設定します。
Not USA Code blockの出力(String型): temp_unit(気温の単位), trace_log(トレースログ)

* step 7: 結果を出力します。

<img width="1000" height="1142" alt="2-2-1-flowOverview" src="https://github.com/user-attachments/assets/658d8d6f-aa08-4cdd-9be6-0b2bd49fe191" />

* ご注意: Geocodeツールが利用している[Nominatim APIの呼び出し制約](https://operations.osmfoundation.org/policies/nominatim/)のため、複数拠点の緯度・経度情報を連続で検索すると、予期せぬエラーが発生し、緯度・経度がそれぞれ0になる場合があります。表示された結果の緯度・経度・国コードの情報を確認し、緯度・経度がそれぞれ0になっている場合は、おそらくNominatim APIの呼び出しに失敗しています。

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

15. [WeatherFlow]の全体像が表示されるので、初期状態を確認します。
<img width="1162" height="995" alt="2-2-15-InitialFlow" src="https://github.com/user-attachments/assets/3ae60aad-7bb9-4274-af2c-5f1c3ef9f2e0" />

16. 左上にある[+]アイコンをクリックして、[Tools]タブを選択します。演習1で登録した[Geocode:geocode]、[current weather for coordinate]ツールが表示されていることを確認します。ご注意: 次の画面に見えている[Geocode:reverse_geocode]は使いません。
<img width="1206" height="1039" alt="2-2-16-Tools" src="https://github.com/user-attachments/assets/2fee8749-9115-40d1-87cb-9e39cb4d35df" />

17. [Geocode:geocode]ツールをドラッグして、フローの矢印の中心あたりにドロップします。

<img width="1061" height="849" alt="2-2-17-Tool-DragDrop" src="https://github.com/user-attachments/assets/5771e6f0-6693-4dbb-84e0-dd5286b3f265" />

18. [Current weather for coordinate]ツールをドラッグして、[Geocode:geocode]の下側にドロップします。
<img width="1206" height="1039" alt="2-2-18-2-Tools" src="https://github.com/user-attachments/assets/58386827-88b6-482a-a8cc-e1674c1f5c39" />

19. [Geocode:geocode]をクリックし、表示されたウィンドウ内で、[Edit data ma
pping]をクリックします。
<img width="1206" height="1039" alt="2-2-19-GeoCode-mapping" src="https://github.com/user-attachments/assets/2e64815f-237d-4023-bb3b-026245b1780a" />

20. [Map data for 'Geocode:geocode']の画面を確認し、[Inputs]の下に表示されている[Ask user for input if auto-mapping is unsuccessful]のスイッチをオフにします。
* このスイッチがオンになっていると、パラメーターのマッピングができない場合に、AIエージェントからユーザーに問い合わせが行われます。
<img width="1280" height="1139" alt="2-2-20-NotAsk" src="https://github.com/user-attachments/assets/6f245bc6-58ee-4a4e-9a00-d5c0cbbe0895" />

21.[Remove all automapping]をクリックして、すべてのパラメーターに対する自動マッピングを削除します。
<img width="1363" height="1139" alt="2-2-21-RemoveAutoMap" src="https://github.com/user-attachments/assets/d0aeb182-c24c-4aaf-b0e0-f8fa6653e455" />

22.すべての自動マッピングが削除されたことを確認します。
<img width="1363" height="1139" alt="2-2-22-AutomapRemoved" src="https://github.com/user-attachments/assets/5261f9bb-a624-42e2-8dba-5aa3914a2584" />

23. AIエージェントに入力された地名と[q]パラメーターを対応させます。[q]パラメーターに表示されている[{x}]をクリックします。
<img width="608" height="108" alt="2-2-23-q-variable" src="https://github.com/user-attachments/assets/dfb1b8cb-a151-4635-827f-d03ca66469e5" />

24. [q]パラメーターの下側に、変数名を参照するためのメニューが表示されます。[Input]をクリックして、表示されている[city_name]を選択します。
<img width="606" height="224" alt="2-2-24-Input-city" src="https://github.com/user-attachments/assets/dac96914-e2f7-4e42-9f0d-046825af179f" />

25. [q]パラメーターに[city_name]がマッピングされたことを確認します。
<img width="1363" height="1139" alt="2-2-25-GeoCode-Mapping" src="https://github.com/user-attachments/assets/ed1b66aa-9187-4a1c-96e7-37a805343743" />

* [addressdetails]と[format]の値を入力します。[Enter a value]をクリックすると値を入力できます。

addressdetails:
   ```
   1
   ```
   
format:
   ```
   jsonv2
   ```
* 3つのパラメーター(addressdetails, format, q)のマッピングが正しくできたら、[Map data for 'Geocode:geocode']の右側にある[x]をクリックして、設定画面を閉じましょう。
<img width="605" height="808" alt="2-2-25-1-params" src="https://github.com/user-attachments/assets/0698affc-03a6-40bc-94c2-d9536df0bbcf" />

26. 左上の[+]をクリックし、[Flow nodes]タブから[Code block]を見つけ、[Geocode:geocode]ツールと[current weather for coordinates]ツールとの間にドロップします。

<img width="1840" height="1030" alt="2-2-26-Codeblock-DD" src="https://github.com/user-attachments/assets/e17f5d98-6206-4d89-892b-cab3e789a505" />

27. 追加されたCode blockをクリックして、ブロック名を変更します。
<img width="354" height="341" alt="2-2-27-Codeblock-Edit" src="https://github.com/user-attachments/assets/43f99138-b804-4b69-9311-78514a7efddc" />

* Code block名:
   ```
   Json-loader
   ```

28. [Json-loader]のCode blockの下側にある[Define outputs]をクリックします。

<img width="356" height="335" alt="2-2-27-1-Editing" src="https://github.com/user-attachments/assets/4f46fa96-14a3-4b89-a552-143221dd6d74" />

29. 4つのOutputsを作成します。

<img width="622" height="477" alt="2-2-28-4outputs" src="https://github.com/user-attachments/assets/df4e3c02-36b0-4113-994f-2c7104090daf" />

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
  trace_log
  ```
  
* Description:
  ```
  トレースログ
  ```
---
* Type: String
* Name:
  ```
  country_code
  ```
  
* Description:
  ```
  国コード
  ```

30. [Json-loader] Code blockから[Open Code Editor]をクリックします。

<img width="368" height="353" alt="2-2-30-JsonLoader-cb" src="https://github.com/user-attachments/assets/ac6174dc-8ba8-4eef-9bd5-849035da7c6f" />

31. [Code block for 'Json-loader']が開くのを確認します。

<img width="611" height="840" alt="2-2-31-CodeEditor" src="https://github.com/user-attachments/assets/3bb16b0f-ee40-414d-9527-815999298b26" />

32. 次のコードをコピーして、エディターに貼り付けます。

* watsonx OrchestrateのSaaS環境では、Pythonコードからのログ出力を確認するのが容易ではないため、デバッグ文字列にAgentic Workflowの出力として書き出します。
* 数値から文字、文字から数値など、型の不一致などで実行時例外が発生するのを避けるため、変換において、既定値を設定しています。エラーで異常終了させないことを重視しているため、コード量が多くなっています。
```
# ===== ログ蓄積用のヘルパー関数 =====
trace_log = []

def log(message):
    """ログメッセージを蓄積"""
    trace_log.append(message)

# ===== 安全な属性取得関数 =====
def safe_get_attr(obj, attr, default=None):
    """属性を安全に取得"""
    try:
        return getattr(obj, attr, default)
    except:
        return default

# ===== JSON文字列からの値抽出（正規表現不使用） =====
def extract_from_string(text, key):
    """文字列から特定のキーの値を抽出（簡易版）"""
    try:
        # "key":"value" または "key":value のパターンを探す
        search_pattern = f'"{key}":'
        idx = text.find(search_pattern)
        if idx == -1:
            return None
        
        # コロンの後から値を抽出
        start = idx + len(search_pattern)
        # 引用符をスキップ
        while start < len(text) and text[start] in ' "':
            start += 1
        
        # 値の終わりを探す（カンマ、閉じ括弧、引用符まで）
        end = start
        while end < len(text) and text[end] not in '",}]':
            end += 1
        
        value = text[start:end].strip()
        return value if value else None
    except:
        return None

log("=== Json-loader processing started ===")

# ===== 1. 出力を取得 =====
try:
    step_output = flow["Geocode:geocode"].output
    log("Geocode output retrieved successfully")
except Exception as e:
    log(f"ERROR: Failed to get Geocode output: {str(e)}")
    self.output.country_code = "NODE_ERROR"
    self.output.latitude = 0.0
    self.output.longitude = 0.0
    self.output.trace_log = "\n".join(trace_log)
    # 早期終了
    step_output = None

# ===== 2. データの抽出とパース =====
data = None
if step_output is not None:
    try:
        log("Attempting to parse output...")
        
        # A: すでにオブジェクト（辞書/リスト）として渡されている場合
        if isinstance(step_output, (list, dict)):
            data = step_output
            log("Output is already a dict/list")
        
        # B: content[0].text 形式の場合
        else:
            content_attr = safe_get_attr(step_output, 'content')
            if content_attr is not None:
                try:
                #    import json
                    text_content = content_attr[0].text
                    data = json.loads(text_content)
                    log("Parsed from content[0].text")
                except:
                    log("Failed to parse content[0].text")
            
            # C: 単純な文字列の場合
            if data is None:
                try:
                    # import json
                    data = json.loads(str(step_output))
                    log("Parsed from string representation")
                except:
                    log("Failed to parse as JSON string")
    
    except Exception as e:
        log(f"ERROR in parsing: {str(e)}")

# ===== 3. パースに失敗した場合の文字列抽出 =====
if data is None and step_output is not None:
    log("Attempting string extraction as fallback...")
    try:
        raw = str(step_output)
        log(f"Raw output length: {len(raw)}")
        
        # 簡易的な抽出
        lat_str = extract_from_string(raw, "lat")
        lon_str = extract_from_string(raw, "lon")
        
        if lat_str and lon_str:
            self.output.latitude = float(lat_str)
            self.output.longitude = float(lon_str)
            log(f"Extracted lat={lat_str}, lon={lon_str}")
            
            # 国コードの推定
            if "United States" in raw or "USA" in raw:
                self.output.country_code = "US"
            elif "Japan" in raw or "日本" in raw:
                self.output.country_code = "JP"
            else:
                # country_codeを直接抽出
                cc_str = extract_from_string(raw, "country_code")
                if cc_str:
                    self.output.country_code = cc_str.upper()
                else:
                    self.output.country_code = "UNKNOWN"
            
            log(f"Country code: {self.output.country_code}")
        else:
            log("ERROR: Could not extract lat/lon from string")
            self.output.country_code = "PARSE_FAIL"
            self.output.latitude = 0.0
            self.output.longitude = 0.0
    
    except Exception as e:
        log(f"ERROR in string extraction: {str(e)}")
        self.output.country_code = "EXTRACT_ERROR"
        self.output.latitude = 0.0
        self.output.longitude = 0.0

# ===== 4. 正常にパースできた場合の処理 =====
if data is not None:
    log("Processing parsed data...")
    try:
        # リストの場合は最初の要素を取得
        if isinstance(data, list):
            if len(data) > 0:
                target = data[0]
                log(f"Using first element of list (length: {len(data)})")
            else:
                log("ERROR: Empty list")
                target = {}
        else:
            target = data
            log("Using data as-is (dict)")
        
        # 緯度・経度の取得
        if isinstance(target, dict):
            lat_value = target.get("lat", 0)
            lon_value = target.get("lon", 0)
            
            self.output.latitude = float(lat_value)
            self.output.longitude = float(lon_value)
            log(f"Latitude: {self.output.latitude}")
            log(f"Longitude: {self.output.longitude}")
            
            # 住所情報から国コードを取得
            addr = target.get("address", {})
            if isinstance(addr, dict):
                cc = addr.get("country_code", "US")
                self.output.country_code = str(cc).upper()
                log(f"Country code from address: {self.output.country_code}")
            else:
                # addressがない場合は直接country_codeを探す
                cc = target.get("country_code", "US")
                self.output.country_code = str(cc).upper()
                log(f"Country code (direct): {self.output.country_code}")
        else:
            log("ERROR: Target is not a dict")
            self.output.country_code = "TYPE_ERROR"
            self.output.latitude = 0.0
            self.output.longitude = 0.0
    
    except Exception as e:
        log(f"ERROR in data extraction: {str(e)}")
        self.output.country_code = "EXTRACT_FAIL"
        self.output.latitude = 0.0
        self.output.longitude = 0.0

log("=== Json-loader processing finished ===")
log(f"Final: country={self.output.country_code}, lat={self.output.latitude}, lon={self.output.longitude}")

# ===== 5. ログを出力変数に設定 =====
self.output.trace_log = "\n".join(trace_log)
```

33. コードを貼り付けたら、右上の[x]クリックして、Code Editorを終了します。

<img width="615" height="838" alt="2-2-32-JsonLoaderCode" src="https://github.com/user-attachments/assets/370812d5-43e3-4d3c-8c5c-7d719cbe7b0c" />

34. [current weather for coordinate]ツールをクリックし、[Edit data mapping]をクリックします。

<img width="629" height="301" alt="2-2-33-WeatherTool" src="https://github.com/user-attachments/assets/e5dcc7ed-5f52-4e54-8792-24da540d7a1a" />

35. ツールのデータ・マッピングを確認します。

<img width="610" height="317" alt="2-2-35-WT-mapping" src="https://github.com/user-attachments/assets/a2f62e47-c4ec-433c-85c1-54b2add39878" />

36. 自動マッピングの設置を削除します。
* [Ask user for input if auto-mapping is unsuccessful]をオフにします。
* [Remove all auto-mapping]をクリックします。
<img width="613" height="322" alt="2-2-36-WT-removed" src="https://github.com/user-attachments/assets/5012b8ea-d956-451a-98df-9a0bf26db602" />

37. [current_weather]の値を[True]に設定します。

<img width="612" height="319" alt="2-2-37-CurrentWeather" src="https://github.com/user-attachments/assets/5b5b02ed-fa80-456f-81da-972e6790414e" />

38. [latitude]の値を、[{x}]クリックし、[Json-loader]の[latitude]出力にマップします。

<img width="618" height="472" alt="2-2-38-latitude" src="https://github.com/user-attachments/assets/7a91fc74-6da3-4c59-aab2-d2d4ad186aea" />

39. 同様に[longitude]の値を、[{x}]クリックし、[Json-loader]の[longitude]出力にマップします。

<img width="618" height="519" alt="2-2-39-longitude" src="https://github.com/user-attachments/assets/fe23b27e-b5e0-44ce-9c3f-66bd36928b97" />

40. 'Map data for 'current weather for coordinates'の右側にある[x]をクリックして、マッピング画面を閉じます。
<img width="615" height="314" alt="2-2-40-datamapping" src="https://github.com/user-attachments/assets/d462e88d-3926-4dad-a0c6-f0e31f9ebd58" />

41. [current weather for coordinates]の下側に[Branch]を作ります。左上の[+]をクリックし、[Flow Nodes]タブにある[Flow controls]から[Branch]を選んで、ドラッグ＆ドロップします。[Path 1]と[Path 2]が作られるので、それぞれに[Code block]を追加します。

* Path 1: [USA] Code block
* Path 2: [Not USA] Code block

42. [Branch 1]の条件式を設定します。[Json-loader]の[country_code]出力を使って、式を評価します。

* 完成した状態:
<img width="517" height="243" alt="2-2-42-branch" src="https://github.com/user-attachments/assets/a4dab000-8bc4-4ba2-8c4f-f8a4f9c2bcfa" />

* 初期状態: [Edit condition]をクリックして、条件式を作成します。
<img width="377" height="268" alt="2-2-42-branch-init" src="https://github.com/user-attachments/assets/469aefea-e38c-4875-bbd2-f2c58569d36c" />

* １行目: flow["Json-loader].output.country_code == "US"

* 左辺は ifの右側にある[+]をクリックして、Json-loaderからの[country_code]出力を選びます。
<img width="375" height="171" alt="2-2-42-condition" src="https://github.com/user-attachments/assets/0217cd62-39b5-4051-ba20-9e6b3913ca40" />

* 比較式は[==]を選択します。
* 右辺は、
 ```
 US
 ```
 を入力します。

<img width="656" height="452" alt="2-2-42-1-US" src="https://github.com/user-attachments/assets/2ed49217-55c4-45cd-9002-6ae8247278ab" />

* 2行目: flow["Json-loader].output.country_code == "us" 
* [Add condition+]をクリックして、[or]を選びます。
* 左辺は [{x}]をクリックして、Json-loaderからの[country_code]出力を選びます。
* 比較式は[==]を選択します。
* 右辺は、
 ```
 us
 ```
 を入力します。

<img width="648" height="494" alt="2-2-42-2-us" src="https://github.com/user-attachments/assets/b8d83551-4a1f-4ba7-acae-41e080b4c606" />

43. [USA] Code blockをクリックし、[Define outputs]から4つの出力を作成します。

<img width="612" height="483" alt="2-2-43-USA-outputs" src="https://github.com/user-attachments/assets/35ef7e20-fe22-44e1-9700-c49888004162" />

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
---
* Type: String
* Name:
  ```
  temp_celsius
  ```
  
* Description:
  ```
  摂氏表示の気温
  ```
---
* Type: String
* Name:
  ```
  temp_fahrenheit
  ```
  
* Description:
  ```
  華氏表示の気温
  ```

44. [USA] Code blockのCode editorを開き、次のコードを貼り付けます。

```
# ===== ログ蓄積用のヘルパー関数 =====
trace_log = []

def log(message):
    """ログメッセージを蓄積"""
    trace_log.append(message)

# ===== 安全な取得関数 =====
def safe_get_nested(obj, *keys, default=None):
    """ネストされた属性を安全に取得"""
    result = obj
    try:
        for key in keys:
            if result is None:
                return default
            if isinstance(result, dict):
                result = result.get(key, None)
            else:
                result = getattr(result, key, None)
            if result is None:
                return default
        return result
    except Exception as e:
        log(f"safe_get_nested error: {str(e)}")
        return default

# ===== 1. 天気情報の取得と華氏変換 =====
log("=== Weather processing started ===")

try:
    weather_node = flow["current weather for coordinates"]
    log("Weather node retrieved successfully")
    
    # 温度を取得
    temp_c = safe_get_nested(weather_node, "output", "current_weather", "temperature")
    log(f"Temperature (raw): {temp_c}")
    
    if temp_c is not None:
        temp_c = float(temp_c)
        log(f"Temperature (float): {temp_c} C")
        
        # 華氏に変換
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        log(f"Converted to Fahrenheit: {temp_f} F")
        
        # 出力に設定
        self.output.temp = str(round(temp_f, 1))
        self.output.temp_unit = "°F"
        self.output.temp_celsius = str(round(temp_c, 1))
        self.output.temp_fahrenheit = str(round(temp_f, 1))
        
        log(f"Output set: temp={self.output.temp}, unit={self.output.temp_unit}")
        
        # 天気コード
        weathercode = safe_get_nested(weather_node, "output", "current_weather", "weathercode", default=0)
        self.output.current_weather_code = weathercode
        log(f"Weather code: {weathercode}")
        
    else:
        log("ERROR: Temperature is None")
        self.output.temp = "N/A"
        self.output.temp_unit = "°F"
        self.output.current_weather_code = "UNKNOWN"
        
except Exception as e:
    log(f"ERROR in weather processing: {str(e)}")
    self.output.temp = "ERROR"
    self.output.temp_unit = "ERROR"
    self.output.error_weather = str(e)

log("=== Weather processing finished ===")

# ===== 2. Json-loaderからの取得 =====
log("=== Loader processing started ===")

try:
    loader_node = flow["Json-loader"]
    log("Loader node retrieved successfully")
    
    c_code = safe_get_nested(loader_node, "output", "country_code", default="UNKNOWN")
    latitude = safe_get_nested(loader_node, "output", "latitude", default=0.0)
    longitude = safe_get_nested(loader_node, "output", "longitude", default=0.0)
    
    log(f"Loader data: country={c_code}, lat={latitude}, lon={longitude}")
    
    self.output.country_code = str(c_code)
    self.output.latitude = float(latitude)
    self.output.longitude = float(longitude)
    
except Exception as e:
    log(f"ERROR in loader processing: {str(e)}")
    self.output.country_code = "UNKNOWN"
    self.output.latitude = 0.0
    self.output.longitude = 0.0
    self.output.error_loader = str(e)

log("=== Loader processing finished ===")

# ===== 3. パス名の設定 =====
self.output.latest_path_name = f"USA:{self.output.country_code}"
log(f"Path name set: {self.output.latest_path_name}")

# ===== 4. 最終ログ =====
log("=== Code block execution completed ===")
log(f"Total log entries: {len(trace_log)}")

# ===== 5. ログを出力変数に設定 =====
self.output.trace_log = "\n".join(trace_log)
```

45. [Not USA] Code blockをクリックし、[Define outputs]から2つの出力を作成します。
<img width="608" height="401" alt="2-2-45-NotUSA-outputs" src="https://github.com/user-attachments/assets/5d8633c6-7fea-41ac-9914-871455b2d874" />

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

46. [Not USA] Code blockのCode Editorを開き、次のコードを貼り付けます。

```
# ===== ログ蓄積用のヘルパー関数 =====
trace_log = []

def log(message):
    """ログメッセージを蓄積"""
    trace_log.append(message)

# ===== 安全な取得関数 =====
def safe_get_nested(obj, *keys, default=None):
    """ネストされた属性を安全に取得"""
    result = obj
    try:
        for key in keys:
            if result is None:
                return default
            if isinstance(result, dict):
                result = result.get(key, None)
            else:
                result = getattr(result, key, None)
            if result is None:
                return default
        return result
    except Exception as e:
        log(f"safe_get_nested error: {str(e)}")
        return default

# ===== 1. 天気情報の取得（摂氏のまま） =====
log("=== Weather processing started ===")

try:
    weather_node = flow["current weather for coordinates"]
    log("Weather node retrieved successfully")
    
    # 温度を取得（摂氏）
    temp_c = safe_get_nested(weather_node, "output", "current_weather", "temperature")
    log(f"Temperature (raw): {temp_c}")
    
    if temp_c is not None:
        temp_c = float(temp_c)
        log(f"Temperature (float): {temp_c} C")
        
        # 摂氏のまま出力に設定
        self.output.temp = str(round(temp_c, 1))
        self.output.temp_unit = "°C"
        self.output.temp_celsius = str(round(temp_c, 1))
        
        log(f"Output set: temp={self.output.temp}, unit={self.output.temp_unit}")
        
        # 天気コード
        weathercode = safe_get_nested(weather_node, "output", "current_weather", "weathercode", default=0)
        self.output.current_weather_code = weathercode
        log(f"Weather code: {weathercode}")
        
    else:
        log("ERROR: Temperature is None")
        self.output.temp = "N/A"
        self.output.temp_unit = "°C"
        self.output.current_weather_code = "UNKNOWN"
        
except Exception as e:
    log(f"ERROR in weather processing: {str(e)}")
    self.output.temp = "ERROR"
    self.output.temp_unit = "ERROR"
    self.output.error_weather = str(e)

log("=== Weather processing finished ===")

# ===== 2. Json-loaderからの取得 =====
log("=== Loader processing started ===")

try:
    loader_node = flow["Json-loader"]
    log("Loader node retrieved successfully")
    
    c_code = safe_get_nested(loader_node, "output", "country_code", default="UNKNOWN")
    latitude = safe_get_nested(loader_node, "output", "latitude", default=0.0)
    longitude = safe_get_nested(loader_node, "output", "longitude", default=0.0)
    
    log(f"Loader data: country={c_code}, lat={latitude}, lon={longitude}")
    
    self.output.country_code = str(c_code)
    self.output.latitude = float(latitude)
    self.output.longitude = float(longitude)
    
except Exception as e:
    log(f"ERROR in loader processing: {str(e)}")
    self.output.country_code = "UNKNOWN"
    self.output.latitude = 0.0
    self.output.longitude = 0.0
    self.output.error_loader = str(e)

log("=== Loader processing finished ===")

# ===== 3. パス名の設定 =====
self.output.latest_path_name = f"Not USA:{self.output.country_code}"
log(f"Path name set: {self.output.latest_path_name}")

# ===== 4. 最終ログ =====
log("=== Code block execution completed ===")
log(f"Total log entries: {len(trace_log)}")

# ===== 5. ログを出力変数に設定 =====
self.output.trace_log = "\n".join(trace_log)
```

47. フロー全体を確認し、[USA]と[Not USA]、２つのCode blockの後、8 outputsにつながっていることを確認します。問題なければ、右上の[Done]をクリックします。
<img width="1126" height="1142" alt="2-2-47-Done" src="https://github.com/user-attachments/assets/347d1cb5-052b-49fb-9661-080e5e9690a0" />

48. [WeatherAgent02]の左側メニューから[Knowledge]を選択し、[Add source +]をクリックします。

<img width="1126" height="1142" alt="2-2-48-AddSource" src="https://github.com/user-attachments/assets/ecbf572d-9210-4761-8672-13a29db913c5" />

49. [Add Knowledge]から[Exisiting Knowledge]を選択します。
<img width="600" height="254" alt="2-2-49-ExistingKnowledge" src="https://github.com/user-attachments/assets/a8047be7-ec35-4591-99cf-7885b6886634" />

50. [Add knowledge to WeatherAgent02]から、[WMO Weather Code]を選択し、[Add knowledge]をクリックします。
<img width="1126" height="1142" alt="2-2-50-WMO-Code" src="https://github.com/user-attachments/assets/9b02f4f1-dd51-48d4-b410-1086f7dc1991" />

51. [Weather Agent02]に[WMO Weather Code]が追加されたことを確認します。

<img width="1126" height="1142" alt="2-2-51-KnowledgeAdded" src="https://github.com/user-attachments/assets/1dfd3cc4-4b66-4dc5-98f0-2bbe28b3eb62" />

52. [WeatherAgent02]の左側メニューから[Behavior]を選択し、[Instructions]を入力します。

Instructions:
```
日本語で回答してください。
ユーザーから与えられた都市名を使い、WeatherFlowツールを使って、気象情報を取得してください。気温の単位は、出力されたtemp_unitを使って表示ください。
根拠を示すために気象情報の出力（current_weather_code, temp, temp_unit, country_code, latitude, longitude, latest_path_name）を全て表示してください。trace_logがあれば、それも出力してください。WeatherFlowツール内では、文字列データを翻訳したり、大文字・小文字の変換をしないでください。
```

53. チャット欄に質問を入力します。

チャット欄:
```
東京都新宿区の天気は？
```

<img width="1126" height="1142" alt="2-2-53-Shinjuku" src="https://github.com/user-attachments/assets/2a20062a-c0a6-473f-bfbb-2330a65201ae" />

54. 違う質問を入力します。

チャット欄:
```
静岡市とシアトルの天気を表で比較して
```
<img width="669" height="820" alt="2-2-54-Shizuoka-Seattle" src="https://github.com/user-attachments/assets/99a23c82-c475-4f4e-af5d-ef5d04b55ec6" />

* 再度ご注意: Geocodeツールが利用している[Nominatim APIの呼び出し制約](https://operations.osmfoundation.org/policies/nominatim/)のため、複数拠点の緯度・経度情報を連続で検索すると、予期せぬエラーが発生し、緯度・経度がそれぞれ0になる場合があります。このAIエージェントで2拠点の比較はおそらく問題になりませんが、3拠点以上を比較すると、Nominatim API呼び出しの失敗により、緯度・経度がそれぞれ0になります。その場合、AIエージェントが回答している気象情報はヌル島（Null Island）のデータとなりますので、ご注意ください。AIエージェントの回答内容に含まれている緯度・経度が0以外になっているかどうかを必ずご確認ください。

55. 最後に右上の[Deploy]ボタンをクリックして、このAIエージェントをデプロイしてください。

演習2は以上です。

## まとめ

* Agentic Workflowを利用し、MCP server、OpenAPI、それぞれを組み合わせたワークフローを作成しました。
* MCP serverからの戻り値を加工するJson-loader Code blockを実装することで、指定した都市名に対応する国コードを取得できるようにしました。
* Branchを使い、国コードが "US" または "us" であることを条件にして、気温の単位を「華氏表示」に対応させるCode blockを作成しました。米国以外の国においては、「摂氏表示」に対応するCode blockを作成しました。 


