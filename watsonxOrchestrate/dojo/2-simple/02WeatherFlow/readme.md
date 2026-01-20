# 気象情報を取得するワークフローを作成する
* 最終更新日: 2026/01/21
* このコンテンツは、Business Automation Handsonコンテンツの内容を、若干発展させて最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。
[ソース](https://ibm.github.io/ba-handson-jp/wxoagent/tool/)

## このハンズオンの目的
AIエージェントは、ツールを利用することで、基盤モデルに備わっていない情報（例：リアルタイムの情報）を取得します。
このハンズオンでは、インターネットに公開されているAPIを用いて、ツールを定義して、AIエージェントから利用します。

* 利用するAPI: https://open-meteo.com/
* [オープンソース](https://github.com/open-meteo/open-meteo)で公開されている気象情報のAPI
* APIキー不要で使えます。
* AIエージェントのツールを定義する方法の体験目的で利用しており、業務用のプロダクション環境に展開することは想定していません。
* 使用権許諾についての詳細は、[こちら](https://open-meteo.com/en/licence)を参照してください。

* 前提条件: 演習1[地名から緯度、経度、国コードを求めるワークフローを作成する](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2-simple/01Geocoding/readme.md)が終わっていること

0. watsonx Orchestrateが起動済みで、演習1で作成した[WeatherInfo]が開いている状態にしてください。

<img width="1091" height="1068" alt="2-2-0-Start" src="https://github.com/user-attachments/assets/42ab5c93-4c50-4942-8c2f-cf39cc728d48" />

1. 左メニューから[Toolset]を選択し、[Tools]から[Add tool+]をクリックします。

<img width="1091" height="1068" alt="2-2-1-AddTool" src="https://github.com/user-attachments/assets/77a6cb67-96de-46d5-8061-95317c6fb72a" />

2. [Add a tool]から[OpenAPI]をクリックします。

<img width="1091" height="1068" alt="2-2-2-OpenAPI" src="https://github.com/user-attachments/assets/8f9264dd-5b41-458e-9bbd-7ed2d43806ad" />

3.　[Import tool]の画面が開きます。
* ツールを定義している OpenAPI 3.0.0準拠の仕様書が入っているyaml形式のファイルを利用して、ツールを取り込みます。
* weather.yamlのダウンロード: こちらの[リンク](https://ibm.github.io/ba-handson-jp/wxoagent/files/weather.yaml)を右クリック (Macの場合、[control]を押しながらクリック)し、名前を付けて保存してください。
Upload filesの下にある、[Drag and drop an OpenAPI file here or click to upload]をクリックします。

<img width="1091" height="1068" alt="2-2-3-ImportTool" src="https://github.com/user-attachments/assets/62f45378-3e3d-4149-a5d5-4d41f489342c" />

* 参考: YAML形式でOpenAPI 3 の完全な仕様書を作る場合は、インターネットから情報を取得する機能を備えた生成AIサービスに頼ると簡単です。
* プロンプトの例「watsonx Orchestrateのツールとして利用できるよう、open-meteoのforecast APIからOpenAPI 3.0の完全な仕様書を作ってください。」

* ツールを追加する際の注意点: 同じ名前のツールを複数登録しようとすると、名前の後ろに番号が付与されていきますのでご注意ください。
  Code Blockからツールの値を参照する際に、その番号も合わせて指定する必要が出てくるので、名前の後ろに番号が付与されないよう、ツールの名前を変更するなど、実装で工夫してください。

4. weather.yamlをアップロードすると、watsonx Orchestrateは、内容を検証します。
* 検証が完了すると"Validation successful"と表示されますので、[Next]をクリックします。
  
<img width="1091" height="1068" alt="2-2-4-Validated" src="https://github.com/user-attachments/assets/c6d25391-d6a8-4ba0-9c24-8b69e9b1b19f" />

5. [Operations] というリストが表示されるので、[current weather for coordinates]にチェックを入れて、[Done]をクリックします。

<img width="1091" height="1068" alt="2-2-5-Operation" src="https://github.com/user-attachments/assets/3a1522d6-a868-4635-a342-8085f0910cfe" />

6. しばらくすると、watsonx Orchestrateが気象ツールを取り込み、画面右上に[Tool Added]と表示します。

<img width="1091" height="1068" alt="2-2-6-Tool-Added" src="https://github.com/user-attachments/assets/82d50a7c-1d6c-48ce-9c38-4b6b6aafcc3f" />

7. Open Meteoの気象APIで利用されているWMO （世界気象機関）の気象コードを解釈できるよう、簡単なテキストファイルを[Knowledge]として取り込みます。
* 左側のメニューから[Knowledge]を選択し、[Add source +]をクリックします。
<img width="1091" height="1068" alt="2-2-7-Knowledge" src="https://github.com/user-attachments/assets/68db75a6-7346-4c98-a19f-5f30a79547e0" />

* テキストファイルのダウンロードは[こちら](https://raw.githubusercontent.com/IBM/japan-technology/refs/heads/main/watsonxOrchestrate/dojo/2-simple/wmo_weather_codes_with_emoji.csv)を右クリック (Macの場合、[control]を押しながらクリック)し、名前を付けて保存してください。
8. [Add knowledge]から[New knowledge]をクリックします。
<img width="1091" height="1068" alt="2-2-8-NewKnowledge" src="https://github.com/user-attachments/assets/069dc849-70e5-457a-8cc1-2b4c10ad303d" />

9. [Choose knowledge source]から[Upload files]を選択し、最後に[Next]をクリックします。

<img width="1091" height="1068" alt="2-2-9-Uploadfiles" src="https://github.com/user-attachments/assets/66fa1e66-fad8-4d97-8798-0144258bbef6" />

10. [Drag and drop files here or click to upload]をクリックし、手順7でダウンロードしたwmo_weather_codes_with_emoji.csv(気象コードの説明が入ったテキストファイル)をアップロードします。
* ファイル名が表示されたことを確認して、[Next]をクリックします。

<img width="1091" height="1068" alt="2-2-10-Uploaded" src="https://github.com/user-attachments/assets/16af7df7-6fd8-4ce4-813a-8fdcd9faad4b" />

11. [Knowledge details]に[Name]と[Description]を入力します。最後に[Save]をクリックします。

* Name:
```
WMO気象コード
```

* Description:
```
* wmo_code: WMO天気コード（0-99）
* emoji: 天気絵文字
* short_en: 短い表現（英語）
* short_ja: 短い表現（日本語）
* description_en: 詳細説明（英語）
* description_ja: 詳細説明（日本語） 
```
<img width="1091" height="1068" alt="2-2-11-KnowledgeDetail" src="https://github.com/user-attachments/assets/3631a3c1-f258-4991-b2d6-1744fea05dab" />

12. 追加したKnowledgeが利用可能になるのを待ちます。
<img width="1091" height="1068" alt="2-2-12-KnowledgeReady" src="https://github.com/user-attachments/assets/4d0d5081-6560-4035-a4bb-51c6c9fc3b1f" />

13. 左側の[Toolset]をクリックし、[WeatherFlow]を[Open in flow builder]を使って開きます。
<img width="1091" height="1068" alt="2-2-13-OpenWF" src="https://github.com/user-attachments/assets/637c5906-be9c-4763-9f94-2d60803dbca1" />

14. [Flow nodes]のウィンドウが見えていなければ、左上の[+]をクリックし、開きます。
<img width="1091" height="1068" alt="2-2-14-FlowNodes" src="https://github.com/user-attachments/assets/a06aa42a-b75e-43a5-b1be-d2e06c033560" />

15. [Tools]タブを開きます。[current weather for coordinate]ツールを見つけます。
* 検索テキストボックスに[for co]と入力すると見つかります。
<img width="1047" height="1024" alt="2-2-15-Tool" src="https://github.com/user-attachments/assets/73a9877c-7aad-4a78-b9de-f7a07327340c" />

16. [current weather for coordinate]ツールをドラッグし、[Geocode]と[0 outputs]の間の線にドロップします。
<img width="1884" height="1162" alt="2-2-16-dd-tool" src="https://github.com/user-attachments/assets/c6c73b02-1dd3-4803-850b-5339cfdf7001" />

17. フロー上の[current weather for coordinates]をクリックし、[Edit data mapping]をクリックします。
<img width="1091" height="1068" alt="2-2-17-EditDatamapping" src="https://github.com/user-attachments/assets/d4af8ddd-e1d6-4798-95b0-f8a675aa53bd" />

18. [Ask user for input if auto-mapping is unsuccessful]をオフにします。
<img width="599" height="335" alt="2-2-18-map-off" src="https://github.com/user-attachments/assets/508eedcf-2dc5-42cc-a9e1-b12a5d85e997" />

19. [Remove all auto-mapping]をクリックし、[Auto-map]を全て削除します。

<img width="598" height="322" alt="2-2-19-Automap-remove" src="https://github.com/user-attachments/assets/64e7378c-4044-443c-8877-17bc1af55102" />

20. [current_weather]の値を [True] に設定します。
<img width="590" height="314" alt="2-2-20-current-weather" src="https://github.com/user-attachments/assets/55c689c5-3a5c-48c3-bf15-033adb7a59b9" />

21. [latitude]の右側にある[{x}]をクリックし、Geocodeにあるoutput.latitudeを選択します。
<img width="593" height="463" alt="2-2-21-latitude" src="https://github.com/user-attachments/assets/128e0823-44eb-425a-bdf8-de2afd30eb7d" />

22. [longitude]の右側にある[{x}]をクリックし、Geocodeにあるoutput.longitudeを選択します。選択が終わったら、右上の[x]をクリックして、マッピング画面を閉じます。
<img width="593" height="323" alt="2-2-22-mapped" src="https://github.com/user-attachments/assets/eb97dc8c-db7f-49ce-949c-2da734428642" />

23. WeatherFlowの右側にある[Edit Details]をクリックし、Overviewの[Description]を入力します。入力を終えたら[Done]をクリックします。

* Description:
```
与えられた都市名から緯度、経度、国コード、気象情報を調べます
```

<img width="1082" height="1067" alt="2-2-23-WFDetails" src="https://github.com/user-attachments/assets/fd65af4d-9490-49a0-a29e-dce39befca7b" />

24. WeatherFlowの画面の右上の[Done]をクリックして、フロー・ビルダーを閉じます。

<img width="1082" height="1067" alt="2-2-24-Done" src="https://github.com/user-attachments/assets/84e90c09-7a2b-4bf2-a3cd-d2df278f1217" />

25. WeatherInfoの左側メニューから[Behavior]をクリックし、[Instructions]を次の内容で上書きします。
* Instructions:
```
回答は日本語で行なってください。
1. WeatherFlowで指定された都市の気象情報を調べます
2. WeatherFlowで得られた内容を使って、WMO気象コードで「天気絵文字」と「短い表現」を見つけます
3. 米国の都市の場合は、気温を華氏で表示します。
4. 現在時刻はJapan Standard Time (UTC+09:00)で表示します。
```

<img width="1082" height="1067" alt="2-2-25-Behavior" src="https://github.com/user-attachments/assets/997a11ee-11a6-4064-a446-44d8139db96f" />

26. AIエージェントをテストしましょう。
* プロンプト:
```
静岡市の天気は？
```

* 応答例:
```
申し訳ありませんが、現在の静岡市の天気に関する情報は持っていません。
```

* このエラーは気象情報の取得に失敗しているわけではなく、気象コードから説明文を取り出すツールで失敗しています。この問題を手順27-29で修正します。

27. 手順7から手順12で追加したKnowledgeの調整を行います。左側メニューから[Knowledge]を選択し、[WMO気象コード]内の[Edit details]をクリックします。
<img width="1082" height="1067" alt="2-2-27-EditDetails" src="https://github.com/user-attachments/assets/5d40c37e-24de-4f7e-b8da-cf69cd126d9a" />

28. 画面左側にある[Edit knowledge settings]をクリックします。
<img width="1082" height="1067" alt="2-2-28-EditKnowledgeSettings" src="https://github.com/user-attachments/assets/c5cb8203-a138-41ba-aa0e-f33633ae8d47" />

29. [Edit knowledge settings]の画面で次の２つを設定し、[Save]をクリックします。

* Response : [Dynamic (Preview)]
* Maximum Search Results:
```
1
```

<img width="1082" height="1067" alt="2-2-29-Settings" src="https://github.com/user-attachments/assets/10b2d0fa-42db-4a63-97d4-cbde7e108970" />

30.　画面上から2行目にある、Agent chat / Manage agents / WeatherInfo と並んでいる[WeatherInfo]をクリックします。
<img width="1082" height="1067" alt="2-2-30-WF" src="https://github.com/user-attachments/assets/23ad64a4-39b0-4a52-9068-6172badd3521" />

31.　WeatherInfoの画面に戻るので、もう一度、AIエージェントをテストしましょう。
* プロンプト:
```
静岡市の天気は？
```

* 応答例:

```
**静岡市の現在の天気（JST）**  
- **日時**：2026‑01‑21 03:45 JST  
- **気温**：3.3 °C  
- **天気コード**：1（主に晴れ）  
- **天気絵文字**：☀️  
- **短い表現**：主に晴れ  

※米国の都市でないため、気温は摂氏のまま表示しています。  
```

