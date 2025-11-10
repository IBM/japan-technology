# ネットワーク（Wi-Fiパスワード案内）

* 最終更新日: 2025/11/10

## 全体像の確認

<img width="2633" height="2711" alt="Wi-Fiが繋がらない" src="https://github.com/user-attachments/assets/493092ec-fbc0-4cfb-bf46-f4e0204da6ec" />

##
1. watsonx Orchestrateを開き、左上のメニューから、[Build]-[Assistant Builder]を選択します。

<img width="1098" height="1000" alt="01AssistantBuilder" src="https://github.com/user-attachments/assets/3807edcd-2fc7-4d97-ac31-afe6266a696e" />

2. 初回のアシスタント作成であるので、「Welcome to AI assistant builder」の画面を使って進めます。「Create your first assistant」の入力欄に次の内容を設定します。それぞれ設定したら、右上にある[Next]をクリックします。

* Assistant name:
  ```
  社内ヘルプデスク
  ```

* Description:
  ```
  社内の問い合わせに回答するアシスタントです。
  ```

* Assistant language:
  ```
  Japanese
  ```

3. 続いて「Personalize your assistant」の画面が表示されます。Webサイトで動作するチャットボットを作成するので、デプロイ先は「Web」とします。

* Where do you plan on deploying your assistant?
  ```
  Web
  ```

* Which industry do you work in?
  ```
  Software
  ```

* What is your role on the team building the assistant?
  ```
  Developer
  ```

* Which statement describes your needs best?
  ```
  I want to provide confident answers to common questions.
  ```
<img width="1098" height="1000" alt="02Create1stAssistant" src="https://github.com/user-attachments/assets/1f4f5d3a-813a-42ba-ae21-11939300d751" />

<img width="1098" height="1000" alt="03PersonalizeYourAssistant" src="https://github.com/user-attachments/assets/0392094f-5eeb-47ef-9cb7-ac8834781d5e" />

<img width="1098" height="1000" alt="04CustomizeYourChatUI" src="https://github.com/user-attachments/assets/3be74434-25cc-4981-8653-b789c8a6ee88" />

<img width="1098" height="1000" alt="05PreviewYourAssistant" src="https://github.com/user-attachments/assets/f21630b5-c232-4631-8a4f-17a3568bc677" />

<img width="190" height="261" alt="06MenuAction" src="https://github.com/user-attachments/assets/a84a8046-eebd-4325-a363-0d736d186cdf" />

<img width="1148" height="1000" alt="07CreateYour1stAction" src="https://github.com/user-attachments/assets/6a88990c-080a-4edf-bde5-b7e70b5d0834" />

<img width="1148" height="1000" alt="08CustomBuiltAction" src="https://github.com/user-attachments/assets/5118c695-1fc8-4789-ba5f-f3e92a382e06" />

<img width="1148" height="1000" alt="09NewAction" src="https://github.com/user-attachments/assets/a4ad734b-3d82-4523-aab0-9f3c97ed72c8" />

<img width="1148" height="1000" alt="10Editor" src="https://github.com/user-attachments/assets/5a2027e1-28c3-4430-a4e6-864b1d27ab57" />

<img width="282" height="155" alt="11Expand-StartWith" src="https://github.com/user-attachments/assets/7a02b5d3-c80a-41b6-87da-d8ecef98de80" />

<img width="1148" height="1000" alt="12DisplayName-Examples" src="https://github.com/user-attachments/assets/537a4109-a551-44b8-aa1a-3bd58278e63b" />

<img width="1151" height="983" alt="13Filled-DisplayName-Examples" src="https://github.com/user-attachments/assets/0b76414b-fc30-40f1-a200-b707ef6a37a9" />

<img width="289" height="312" alt="14ToStep1" src="https://github.com/user-attachments/assets/2c5d29e6-5725-45db-8953-e953b6cc7b2a" />

<img width="1151" height="983" alt="15Step1-init" src="https://github.com/user-attachments/assets/82231d69-971e-46cd-b658-4f7b6b164b32" />

<img width="539" height="224" alt="16DefineCustomerResponse" src="https://github.com/user-attachments/assets/baddf44b-ed9f-4f2b-895c-c33182c41634" />

<img width="1151" height="983" alt="17Options" src="https://github.com/user-attachments/assets/cff4d856-4036-4dfe-8ce7-21b1c8eea48e" />

<img width="1151" height="983" alt="18EditResponse" src="https://github.com/user-attachments/assets/afb7b31e-3cfa-46a1-81e4-70a71b3d9fa9" />

<img width="535" height="277" alt="19SaveResponseToReuse" src="https://github.com/user-attachments/assets/1c1e216e-a9c6-418b-98d6-17eb73d8d79c" />

<img width="1151" height="983" alt="20NewSavedResponse" src="https://github.com/user-attachments/assets/35650faa-a8ce-484a-9064-87cb52dd8680" />

<img width="1151" height="983" alt="21Preview" src="https://github.com/user-attachments/assets/d6637b78-bc33-43ed-b8b0-3a5eba3a356f" />

<img width="320" height="40" alt="22CloseChatWindow" src="https://github.com/user-attachments/assets/928fc059-68c7-425e-a417-a177c311b189" />

<img width="1151" height="983" alt="23PreviewClosed-NewStep" src="https://github.com/user-attachments/assets/6d47988f-40a4-4d7c-8d20-f94a22de36e1" />

<img width="1151" height="983" alt="24-Step2-WithCondition" src="https://github.com/user-attachments/assets/df447ed6-5fd0-4805-a96c-1b298166606b" />

<img width="988" height="580" alt="25-Step2-Condition-AssistantSays" src="https://github.com/user-attachments/assets/50767e63-2626-4787-9150-2cc31fa48e84" />

<img width="984" height="780" alt="26-Step2-EndTheAction" src="https://github.com/user-attachments/assets/16a6c396-dfb5-4eee-8b6c-793579301515" />

<img width="374" height="538" alt="27-Step2-Preview" src="https://github.com/user-attachments/assets/10328286-3ac0-4f5f-b4a4-5509cf7ed3dd" />

<img width="660" height="329" alt="28-Step3-ChooseOffice" src="https://github.com/user-attachments/assets/585093db-0ef1-4c80-973e-b5fc36a6b201" />

<img width="981" height="773" alt="29-Step3-AssistantSays-AndThen" src="https://github.com/user-attachments/assets/b3398cce-cd90-400a-a49f-af526cb59c7b" />

<img width="368" height="530" alt="30-Step3-Preview" src="https://github.com/user-attachments/assets/91aa2555-a14d-4e2b-aafc-0d7e64da47d3" />

<img width="989" height="785" alt="31-Step4-SetAll" src="https://github.com/user-attachments/assets/6f2de719-db1a-4cfd-adc1-2529503bdca6" />

<img width="367" height="533" alt="32-Step4-Preview" src="https://github.com/user-attachments/assets/65130a13-b606-45cd-9a9d-4175d6062ccc" />




