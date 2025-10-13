# ツールとフローを使って気象情報を取得する

* こちらは、Business Automation Hands-onのwatsonx Orchestrate [Lab 3](https://ibm.github.io/ba-handson-jp/wxoagent/flow/)を最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。
* 問い合わせの内容が東京であるかどうかを判断し、東京であれば気温を摂氏で、そうでなければ、気温を華氏で回答します。
* 前提条件: [WeatherAgentの演習](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/2/WeatherAgent/readme.md)が終わっていること

## 参考資料 
* [Agentic Workflows](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=tools-agentic-workflows)
* [Code blocks](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=workflows-code-blocks)
* [Agentic workflow expressions](https://developer.watson-orchestrate.ibm.com/tools/flows/flow_expression)

0. 作成するワークフローの全体像
* watsonx Orchestrateのワークフロー作成ツールを利用します。
* 作成するフローは単純です。ワークフロー作成ツールの操作に慣れるため、ハンズオンで体験しましょう。
* 気象情報の取得は、WeatherAgentのパートで追加した[current weather for coordinates]ツールを使います
* 条件分岐としてのBranchを1つ作成し、指定された city_name が "東京" であるかどうかを判定し、摂氏を単位として回答するか、あるいは華氏を単位として回答するかを選択します。
* 華氏を単位とした場合、摂氏で表現されている気温を華氏に変換します。（摂氏に華氏を変換するには 9/ 5をかけてから32を加える）

<img width="1024" height="1042" alt="00Overview" src="https://github.com/user-attachments/assets/22b508b1-9bad-4dec-a452-e3601ad128c3" />

1. watsonx Orchestrateを開きます。 
URL: お使いの環境に合わせてwatsonx Orchestrateを開いてください。
* 無償評価版 (シンガポール): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat
* TechZone (ダラス): https://us-south.watson-orchestrate.cloud.ibm.com/chat
左上のメニューから[Build]メニューをクリックし、[Agent Builder]を選択します。
<img width="1134" height="998" alt="01CreateAgent" src="https://github.com/user-attachments/assets/dddfa54a-49c1-4872-87c5-fb87fe408087" />

2. 左上のメニューを閉じて、[Build agents and tools]画面から、[All tools]を選択し、[Create tool+]をクリックします。

<img width="1178" height="1042" alt="02CreateTool" src="https://github.com/user-attachments/assets/0770aac8-2514-4cf2-b69a-0dd8daf2cae4" />

3. [Add a new tool]から「Create an agentic workflow]をクリックします。

<img width="1178" height="1042" alt="03CreateAnAgenticWorkflow" src="https://github.com/user-attachments/assets/84a24ff2-1562-483d-b71a-9829920aede6" />

4.　ワークフロー・エディターが起動します。この状態は何も入力や出力が定義されていません。

<img width="1178" height="1042" alt="04FlowEditor" src="https://github.com/user-attachments/assets/c1989a00-1c2e-4c27-b546-dfb2bf066453" />

5. Untitledの右にある編集ボタン<img width="22" height="21" alt="Editmenu" src="https://github.com/user-attachments/assets/a079c254-5ab6-4c51-a1df-4aa1c57cfd5d" />
をクリックします。ワークフローのNameとDescriptionを入力したら、[Save]をクリックして保存します。

* Name: ```WeatherFlow```
* Description: ```特定の都市の天気情報を取得する```
<img width="1178" height="1042" alt="05NameAndDescription" src="https://github.com/user-attachments/assets/9aa5fef7-af4a-44fa-b049-927aaef5795b" />

6. 入力(input)項目に何もないことを確認します。
<img width="874" height="384" alt="06AddInput" src="https://github.com/user-attachments/assets/721b5f97-d5f5-4a52-ab16-753371614a46" />

7. WeatherFlowに入力(input)項目を追加します。[Add input+]をクリックし、[String]を選択します。
<img width="1256" height="1042" alt="07AddInput-String" src="https://github.com/user-attachments/assets/6073e129-4ca3-4f77-8c14-604dd690b125" />

8. [Add string input]にName,　Description, Required を設定し、[Add]をクリックします。
* Name: ```city_name```
* Description: ```都市名```
* Required: ```On```
<img width="646" height="509" alt="08String-Parameters" src="https://github.com/user-attachments/assets/1a20bb93-2686-4c61-ba0e-c987494cf1ee" />


9. Inputs(1) と表示が変わり、手順8で設定したパラメーターが一覧表示されていることを確認します。
<img width="886" height="242" alt="09List-Input" src="https://github.com/user-attachments/assets/ea94f47d-ccfd-417c-b862-7cff19b79994" />


10. 次に出力(Output)項目を追加します。[Add output+]をクリックし、[String]を選択します。
<img width="187" height="266" alt="10AddOutput-String" src="https://github.com/user-attachments/assets/5be7ae65-b246-4936-bed9-6c9fec239573" />

11. [Add string output]にName, Descriptionを設定し、[Add]をクリックします。
* Name: ```temp```
* Description: ```都市の気温```

<img width="646" height="394" alt="11String-Parameters" src="https://github.com/user-attachments/assets/771bb249-80c4-43bb-ba37-b96937986861" />

12. 入力項目と出力項目を確認したら、[Save]をクリックします。
<img width="1256" height="1042" alt="12Inputs-Outputs" src="https://github.com/user-attachments/assets/0136a20d-61bd-45ff-b338-5e72d77b021e" />


13. WeatherFlowの全体像を確認します。この時点では入力と出力の間に何も処理がありません。
<img width="1178" height="1042" alt="13Flow-overview" src="https://github.com/user-attachments/assets/7e84a8d9-9a75-4c99-ab28-10478b8b6ae0" />

14. Add Tools <img width="38" height="35" alt="14Add-Tools" src="https://github.com/user-attachments/assets/f29069e2-fdcc-472c-9e7a-b00cd8fe33c4" /> のアイコンをクリックします。


15. [Tools]タブを選択し、検索用テキストボックスに「```weather```」と入力します。[current weather for coordinate...]が見つかります。
<img width="526" height="213" alt="15Find-WeatherTool" src="https://github.com/user-attachments/assets/864b80e8-9067-4c14-8d2a-a611a3216038" />

16. [Tools]タブに表示されている[current weather for coordinate...]ツールをドラッグして、InputsとOutputsの間の青い矢印にドロップします。
<img width="959" height="700" alt="16DragTool" src="https://github.com/user-attachments/assets/0b621999-6b4f-4953-935b-e1ec989360d7" />

17. InputsとOutputsの間に[current weather for coordinate]ツールが追加されました。
<img width="1178" height="1042" alt="17FlowWithTool" src="https://github.com/user-attachments/assets/44de9c1e-b3cb-4e7a-910e-62cbc03d130c" />

18. 追加されたツールを選択し、表示されたウィンドウ内にある[Edit data mapping]をクリックします。
<img width="707" height="435" alt="18StartEditDatamapping" src="https://github.com/user-attachments/assets/78e09adf-92ea-46f9-b5f2-2a0ee558f806" />

19. 表示内容を確認します。
<img width="527" height="452" alt="19Edit1stStage" src="https://github.com/user-attachments/assets/b930e417-7b2f-4570-b628-1c6688db6305" />

20.　[Auto-map x]と削除用の[x]が見えるように、ブラウザーの横幅を大きくします。
<img width="1222" height="1042" alt="20Edit-ChangePageWidth" src="https://github.com/user-attachments/assets/5f0761a9-21a9-4005-904d-b3b4f1573155" />

21.　[current_weather]の行にある<img width="120" height="33" alt="21Automap-delete" src="https://github.com/user-attachments/assets/b33d2ffc-8905-4103-8daf-30d783708a7a" />の[x]をクリックします。

22. [current_weather]の行にあるAuto-mapが削除されました。
<img width="546" height="454" alt="22Automap-deleted" src="https://github.com/user-attachments/assets/bfae1d0f-e8b2-44c3-98f4-d57b16d0b7b1" />


23. [Enter a value]をクリックします。[current_weather]の行にあるトグル・スイッチがOffになります。
<img width="540" height="442" alt="23Off" src="https://github.com/user-attachments/assets/3791567a-de9e-435a-99e7-9e32bd1e648b" />

24. Offになっているトグル・スイッチをクリックして、Onにします。

<img width="544" height="441" alt="24On" src="https://github.com/user-attachments/assets/99ba7608-e819-4fd6-8f03-7363ae05c569" />

25. Map data for 'current weather for coordinates' のウィンドウの右上にある[x]をクリックして閉じます。

<img width="537" height="88" alt="25Close" src="https://github.com/user-attachments/assets/5943e13f-434c-411b-be3b-9dc2e053f0cf" />

26. WeatherFlowの右上にある[Done]をクリックして、ワークフローの編集を完了します。
<img width="1222" height="1042" alt="26Done" src="https://github.com/user-attachments/assets/2458b022-1150-412d-8248-a6edb284f955" />

27. [Build agents and tools]の画面から、[WeatherInfo]エージェントを開きます。
<img width="1222" height="1042" alt="27WeatherInfo" src="https://github.com/user-attachments/assets/0b14fe54-cef6-4e6f-a3ff-466fce1b8eb2" />

28. Toolset項目を選択し、[Add tool+]をクリックします。
<img width="1222" height="1042" alt="28AddTool" src="https://github.com/user-attachments/assets/2166378f-d207-47ed-996c-58b213215e9f" />

29. [Add a new tool]から[Add from local instance]をクリックします。
<img width="1222" height="1042" alt="29AddFromLocalInstance" src="https://github.com/user-attachments/assets/46e8e281-7a07-4120-86fb-b4deb7d59e12" />

30. [Add tools to WeatherInfo]の検索テキスト・ボックスに「```weather```]と入力します。先ほど作成したWeatherFlowが表示されます。

<img width="1222" height="1042" alt="30FindWeather" src="https://github.com/user-attachments/assets/e7f1b8c9-f8f9-4943-97fe-8e171496f257" />

31. [WeatherFlow]の左にある☑️を有効にして、[Add to agent]をクリックします。
<img width="1222" height="1042" alt="31AddtoAgent" src="https://github.com/user-attachments/assets/6b25db7f-7212-4a02-b825-506d028c98dc" />

32. Toolset項目に戻り、[Tools]に表示されている[current weather for coordinates]ツールを削除します。このツールは、WeatherFlowの中で呼び出されるので、WeatherInfoエージェントとの関連付けは不要です。
<img width="1222" height="1042" alt="32RemoveCurrentWeatherTool" src="https://github.com/user-attachments/assets/87721cbd-611d-4694-9add-6f19a1ffb585" />

33. Preview欄をリセットして、AIエージェントに「```東京の気温は？```」と質問します。処理は非同期に実施され、応答を待っている間は追加の入力ができませんので、ご注意ください。

<img width="1222" height="1042" alt="33RunWeatherFlow" src="https://github.com/user-attachments/assets/16a8f3b1-cdf0-4f8b-b323-05dde9274555" />

34. しばらく待っていると、AIエージェントから回答があります。
<img width="1222" height="1042" alt="34ResponseFromTheFlow" src="https://github.com/user-attachments/assets/5a64bb6b-5a61-4a09-b28c-2e4d966bdaf7" />

35. 基本的な動作が確認できたので、ワークフローを変更し、東京以外の都市が指定された場合には、気温を華氏表記に変えましょう。
[Tools]に表示されている[WeatherFlow]の右側にある３点リーダーを選択し、[Edit details]をクリックします。
<img width="406" height="401" alt="35EditDetails" src="https://github.com/user-attachments/assets/8203df22-bd0f-45b4-bd7d-3825aca6c70e" />

36. 出力(output)項目を追加するために、[Add output+]をクリックし、[String]を選びます。
<img width="196" height="267" alt="36AddOutput-String" src="https://github.com/user-attachments/assets/89723091-9768-463d-bbc1-2e0e7e3fbf32" />

37. [Add string output]にName, Descriptionを設定し、[Add]をクリックします。
* Name: ```temp_unit```
* Description: ```tempが摂氏か華氏かを示す```

<img width="646" height="394" alt="37String-Parameters" src="https://github.com/user-attachments/assets/182e0997-eeaa-4aeb-8d1e-c9c947e0fb5e" />

38. WeatherFlowのInputs(1)、Outputs(2)を確認したら、[Save]をクリックします。
<img width="1222" height="1042" alt="38SaveState" src="https://github.com/user-attachments/assets/63a2aae9-7e43-4320-b1cc-44908c8f4103" />

39.
<img width="415" height="402" alt="39OpeninFlowBuilder" src="https://github.com/user-attachments/assets/164e049f-23ec-4bef-8ccf-3a7e96ac03c1" />

40.
<img width="1222" height="1042" alt="40AddFlowItem" src="https://github.com/user-attachments/assets/cf86559d-90a0-4709-92ba-3c0eacf6e4b2" />

41.
<img width="579" height="539" alt="41FlowControls-Branch" src="https://github.com/user-attachments/assets/3226f852-36e1-4751-ae27-040f3311d4be" />

42.
<img width="1222" height="1042" alt="42Path1" src="https://github.com/user-attachments/assets/a852a6c4-9a58-4e53-afa1-3ebd57bdbdf7" />

43.

<img width="1222" height="1042" alt="43Path1-Item" src="https://github.com/user-attachments/assets/58417d9d-0d25-4eb3-ac64-c09a6c8d2cf4" />

44.
<img width="493" height="331" alt="44Codeblock" src="https://github.com/user-attachments/assets/ea661a27-32b0-41ff-8cde-a3356b050e55" />

45.
<img width="1222" height="1042" alt="45Path2-Codeblock" src="https://github.com/user-attachments/assets/24e6f7cc-0043-46ea-b7c1-018602d4f017" />

46.
<img width="1178" height="998" alt="46Codeblock1-2" src="https://github.com/user-attachments/assets/21e8c5db-c05d-4c53-8d9c-1d62b214e3dc" />

47.
<img width="1222" height="1042" alt="47Codeblock1-define" src="https://github.com/user-attachments/assets/88f40ec6-6e7c-4133-a33b-7eb0aed5613f" />

48.
<img width="1222" height="1042" alt="48Codeblock1-output" src="https://github.com/user-attachments/assets/4d66f408-9783-4cb0-b87e-fc401d8d0628" />

49.
<img width="1178" height="998" alt="49StringParameters" src="https://github.com/user-attachments/assets/0b9cc0a9-7143-46bd-aacd-37cfbef12c68" />

50.
<img width="1178" height="998" alt="50Codeblock1-output-defined" src="https://github.com/user-attachments/assets/23c9dabd-705b-4bb7-a00e-5c5aca5acfcc" />

51.
<img width="540" height="728" alt="51CodeEditor" src="https://github.com/user-attachments/assets/84b946b2-ff85-4ba1-a699-d6928df8b288" />

52.
<img width="540" height="211" alt="52Codeblock1-code" src="https://github.com/user-attachments/assets/1e150022-7cab-4279-81d7-24d832bd5db9" />

53.
<img width="544" height="87" alt="53CloseCode-Editor" src="https://github.com/user-attachments/assets/0e878df6-bde8-41af-b473-3d4e3c289623" />

54.
<img width="1222" height="1042" alt="54Codeblock2-define" src="https://github.com/user-attachments/assets/f8abccd5-3bf0-4eaa-9ca6-ed5ac0f1f292" />

55.
<img width="1222" height="1042" alt="55Codeblock2-output" src="https://github.com/user-attachments/assets/2188222e-48fc-4f02-b81f-1d7512e99b8c" />

56.
<img width="647" height="396" alt="56StringParameters" src="https://github.com/user-attachments/assets/728c1c62-93d0-43a3-b5a6-d112a24c31aa" />

57.
<img width="1222" height="1042" alt="57Codeblock2-output-defined" src="https://github.com/user-attachments/assets/26b91057-4cbb-4b45-93f7-db8d690d67a7" />

58.
<img width="940" height="194" alt="58Codeblock2-code" src="https://github.com/user-attachments/assets/1a14b0c5-701c-4009-8249-7fd7cd33dc7c" />

59.
<img width="1024" height="1042" alt="59EditBranch" src="https://github.com/user-attachments/assets/40aefd54-05ef-47fd-be9c-d99d894bb675" />

60.
<img width="582" height="251" alt="60IfCondition" src="https://github.com/user-attachments/assets/32d2e64c-a276-4fa4-9b4d-eaa95c7d7906" />

61.
<img width="675" height="432" alt="61CityName" src="https://github.com/user-attachments/assets/ec3619e8-7ccb-4e80-8761-2540ff3371f4" />

62.
<img width="651" height="426" alt="62Operators" src="https://github.com/user-attachments/assets/b689910d-a42b-4eac-a738-ec08d122e5ae" />

63.
<img width="739" height="301" alt="63CityNameEqualsTokyo" src="https://github.com/user-attachments/assets/be64031e-f4cc-49f8-824a-29a80d208537" />

64.

<img width="1024" height="1042" alt="64Done" src="https://github.com/user-attachments/assets/e74ca900-4773-4d96-a068-b66e9ec936da" />

65.
<img width="350" height="362" alt="65TemparatureTokyo" src="https://github.com/user-attachments/assets/73476be5-d656-4a82-b1c0-0cfe1ac8fa81" />

66.

<img width="341" height="357" alt="66TemparatureNewYork" src="https://github.com/user-attachments/assets/ca9fd1e4-57c3-4baa-a350-6f5edae9807e" />

