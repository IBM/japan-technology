# 気象情報に回答するAIエージェントを作成する

* 最終更新日: 2025/10/13
* このコンテンツは、Business Automation Handsonコンテンツの内容を、最新のwatsonx Orchestrate (英語UI版)を使って実行できるようにしたものです。
[ソース](https://ibm.github.io/ba-handson-jp/wxoagent/tool/)

## このハンズオンの目的
AIエージェントは、ツールを利用することで、基盤モデルに備わっていない情報（例：リアルタイムの情報）を取得します。
このハンズオンでは、インターネットに公開されているAPIを用いて、ツールを定義して、AIエージェントから利用します。

* 利用するAPI: https://open-meteo.com/
* [オープンソース](https://github.com/open-meteo/open-meteo)で公開されている気象情報のAPI
* APIキー不要で使えます。
* AIエージェントのツールを定義する方法の体験目的で利用しており、業務用のプロダクション環境に展開することは想定していません。
* 使用権許諾についての詳細は、[こちら](https://open-meteo.com/en/licence)を参照してください。

1.

<img width="1042" height="1001" alt="01AgentBuilder" src="https://github.com/user-attachments/assets/cc94ef2e-8991-4016-83d7-228dfade47f9" />

2. 

<img width="1042" height="1001" alt="02CreateAgent" src="https://github.com/user-attachments/assets/05dcceca-cc61-4e5d-b280-65a9db635ad6" />

3.

<img width="1042" height="1001" alt="03NewAgent" src="https://github.com/user-attachments/assets/95043092-0ea1-42b3-a563-2d573e4410f2" />

4.

<img width="1042" height="1001" alt="04ChatWithNoTools" src="https://github.com/user-attachments/assets/0e402dbf-fc77-426d-be5c-182ed710e27b" />

5.

<img width="1042" height="1001" alt="05Toolset-AddTool" src="https://github.com/user-attachments/assets/929a49d1-2435-4e29-944a-92a888d1c6af" />

6.

<img width="1042" height="1001" alt="06AddFromFile-MCPserver" src="https://github.com/user-attachments/assets/4eeb4eaf-9be2-45bb-971a-abe5a023eaa1" />

7.

<img width="1042" height="1001" alt="07ImportFromFile" src="https://github.com/user-attachments/assets/eae3ca68-329d-461e-a9a2-fb745c363b0f" />

8.

<img width="1042" height="1001" alt="08ClicktoUpload" src="https://github.com/user-attachments/assets/20c208ae-2c5f-4335-b066-e11262522afc" />

9.

<img width="1042" height="1001" alt="09ChooseWeatherYaml" src="https://github.com/user-attachments/assets/3258ef5c-439d-4457-91f4-7d9871fe9fd3" />

10.

<img width="998" height="957" alt="10WeatherYaml-Validated" src="https://github.com/user-attachments/assets/db2a2151-7fff-4764-a0fc-f23ac570986d" />

11.

<img width="1042" height="1001" alt="11SelectOperations" src="https://github.com/user-attachments/assets/8ba0a062-0154-45fc-8e4f-a01522bb02fd" />

12.

<img width="1042" height="1001" alt="12AddedTheTool" src="https://github.com/user-attachments/assets/579c0930-4c91-45a0-a023-c3d083d69e7f" />

13.

<img width="1042" height="1001" alt="13WhatCapability" src="https://github.com/user-attachments/assets/accb17d7-d6cc-44d0-8a9c-af6d14a595fd" />

14.

<img width="1042" height="1001" alt="14SetBehaviors" src="https://github.com/user-attachments/assets/882ee0fc-e631-4823-af74-dbc4d9ed6935" />

15.

<img width="1178" height="1001" alt="15ShinjukuWeather" src="https://github.com/user-attachments/assets/c6d29cfb-1d8d-4365-a1b1-2dd465754358" />

16.

<img width="1178" height="1001" alt="16WeatherReasoning" src="https://github.com/user-attachments/assets/6aeee7f8-8da7-4773-8abc-e63a5db87d13" />

17.

<img width="1178" height="1001" alt="17AgenticQA" src="https://github.com/user-attachments/assets/2ac1de88-91b3-4706-b8cf-d58a5a06331f" />

18.

<img width="1134" height="998" alt="18ComparedWithTable" src="https://github.com/user-attachments/assets/6cf4c8a2-a243-487e-897e-a1dc7c3cde8f" />

19.

<img width="1178" height="1042" alt="19WeatherTomorrow01" src="https://github.com/user-attachments/assets/9dccb240-2a27-4841-b1b5-2ceeb00d13b5" />

20.

<img width="1178" height="1042" alt="20WeatherTomorrow02" src="https://github.com/user-attachments/assets/25109ff0-84c0-448c-a5c9-e81ff8e8e2e4" />
