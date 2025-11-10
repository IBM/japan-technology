# PC故障の問い合わせ
* 最終更新日: 2025/11/10

## 全体像の確認

<img width="2035" height="2676" alt="PC故障の問い合わせ" src="https://github.com/user-attachments/assets/ebcc9fb2-4ce4-4c00-bf7a-0ba43638f36b" />

* 故障しているデバイスのOSを確認します。
* Macの場合: サポートA部門を案内します。
* Windowsの場合: メーカー名の先頭文字を確認します。
* メーカー名の先頭文字が'L'の場合: サポートL部門を案内します。
* それ以外の場合: サポートM部門を案内します。
  
##

1. [ネットワーク（Wi-Fiパスワード案内)](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/3/WiFiAssistant/readme.md)の演習が終わっている状態から出発します。[New action +]をクリックします。
<img width="1208" height="317" alt="33-Actions-List" src="https://github.com/user-attachments/assets/9cf6a530-48ca-4eff-b2ab-52322a52d82a" />

2. 「What kind of action do you want to build?」の画面が表示されます。大きなタイルで表現されている[Custom-built action]をクリックします。
<img width="1325" height="983" alt="34-NewCustomAction" src="https://github.com/user-attachments/assets/d2d22a15-d294-4174-a467-686a3851325e" />

3. 「New action」の画面が開きます。ここでは、AIアシスタントの起動フレーズ「PC故障の問い合わせ」を登録し、[Save]をクリックします。

<img width="440" height="184" alt="35-PCOutofOrder" src="https://github.com/user-attachments/assets/17786856-4ae7-4aa1-9d9f-3b31bf833fe7" />

4. 「PC故障の問い合わせ」タイルを展開し、必要事項を入力します。

必要な項目を入力します。
* Display name:
  ```
  PC故障の問い合わせ
  ```

* Add example phrases: １行ずつ入力してください
  ```
  パソコンが起動しない
  ```
  
  ```
  Macが動かない
  ```

  ```
  PCが壊れた
  ```

  ```
  ブルースクリーン
  ```

<img width="832" height="776" alt="36-DisplayName-Examples" src="https://github.com/user-attachments/assets/26092564-f936-4b88-97a6-cbc35d989f99" />

5. 以降、似たような作業の繰り返しであるため、作業のポイントを書いておきます。全体のフローを参考にして、完成させてください。連絡先は架空のものです。ご注意ください。

## Step 1:

* Assistant says:

  ```
  故障しているのは Windows と Mac のどちらですか？
  ```

* Options:

  ```
  Windows
  ```

  ```
  Mac
  ```
* Name: (New Saved response)

  ```
  os
  ```

## Step 2:

* Assistant says:

  ```
  メーカー名の先頭文字を教えてください。L ですか？ それ以外ですか？
  ```

* Options:

  ```
  L
  ```

  ```
  それ以外
  ```


  <img width="1325" height="983" alt="39-Step2-detail" src="https://github.com/user-attachments/assets/a4c65c73-aecc-46fb-bd00-ac9370e5e887" />

  <img width="578" height="559" alt="40-Step2-Options" src="https://github.com/user-attachments/assets/a817dc94-1425-4bb8-959b-1fe1b54578ee" />

## Step 3:

* Conditions:
  ```
  if [Step 1] is [Windows]
  ```

  ```
  and if [Step 2] is [L]
  ```

* Assistant says:

  ```
  サポートL部門、123-4567にご連絡ください。
  ```

* And Then:

  ```
  End of action
  ```

## Step 4:

* Conditions:
  ```
  if [Step 1] is [Windows]
  ```

  ```
  and if [Step 2] is [それ以外]
  ```

* Assistant says:

  ```
  サポートM部門、123-9988にご連絡ください。
  ```

* And Then:

  ```
  End of action
  ```

## Step 5:

* Conditions:

  if [Step 1] is [Mac]

* Assistant says:

  ```
  サポートA部門、123-0202にご連絡ください。
  ```

* And Then:

  ```
  End of action
  ```
