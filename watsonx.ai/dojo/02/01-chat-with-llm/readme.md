## 言語モデルを使ったチャット機能を試す
IBM watsonx.aiのプロンプト・ラボを使い、言語モデルとチャットしてみましょう。プロンプトは、AIに質問や指示を与えるためにユーザーが入力するものです。
参考URL: [プロンプト・ラボ](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-prompt-lab.html?context=wx&locale=ja "Prompt Lab")

1. 作成したプロジェクトの[概要]タブを開きます。
<img width="1548" alt="wxai-chat-01-proj-overview" src="https://github.com/user-attachments/assets/0d1e2ea8-a580-480a-94a4-0a9a6a10edd6">

2. 作業の開始欄にある[ファウンデーション・モデルを使用したチャットとプロンプトの作成]をクリックします。チャット機能のツアーが表示されますので、[完了]をクリックします。
<img width="1548" alt="wxai-chat-02-tour" src="https://github.com/user-attachments/assets/3c4356d7-f486-4fdd-815f-d3ca69b9e59c">

3. IBM watsonx.aiのプロンプト・ラボが開き、チャットの準備ができたことを確認します。質問の例に表示されている[What are more efficient alternative to a 'for loop' in Python?]をクリックします。
<img width="1548" alt="wxai-chat-03-Chat-Toppage" src="https://github.com/user-attachments/assets/4638014c-b940-4e4d-aa0b-b708f1b86ae3">

4. チャット機能が llama-3-8b-instruct 言語モデルを呼び出し、回答を生成するのを確認します。英語とコード・スニペット（Python言語の短いコード)を交えた回答が表示されます。
<img width="1548" alt="wxai-chat-04-ResponseAboutPython" src="https://github.com/user-attachments/assets/144c42d9-9e6b-418b-946c-857e9d8b7b88">

5. [何かを入力してください]と表示されているテキスト・ボックスに「今の内容を日本語で説明してください。」と入力し、[Enter]キーを押します。
<img width="1548" alt="wxai-chat-05-ResponseInJapanese" src="https://github.com/user-attachments/assets/934b1f84-0504-41f9-8268-682ecc27bbbc">
直前に英語で回答された内容が日本語で説明されます。チャット機能は直前のプロンプトや生成内容を覚えているので、気になることがあれば、どんどん質問しましょう。

6. [何かを入力してください]と表示されているテキスト・ボックスに「今の内容を韓国語で説明してください。」と入力し、[Enter]キーを押します。
<img width="1548" alt="wxai-chat-06-ResponseInKorean" src="https://github.com/user-attachments/assets/fc92f348-5633-4ef9-b5a8-c7b1cbe39bc4">
ここで言語モデルの便利な点が体験できました。多言語の生成ができる言語モデルを利用していると、ある自然言語から別の自然言語への翻訳を言語モデル自身に任せることができます。

7. チャットのクリア機能を呼び出します。
<img width="823" alt="wxai-chat-07-ClearChat" src="https://github.com/user-attachments/assets/eb601335-e501-4101-9fbd-e92cc9392de9">

8. チャットをクリアして良いか、確認ダイアログ・ウィンドウが表示されます。迷わずに[Clear]をクリックします。
<img width="1548" alt="wxai-chat-08-ConfirmToClear" src="https://github.com/user-attachments/assets/d8461688-937c-40d5-8df8-afa0334b96db">

9. チャットの初期画面に戻ったことを確認します。
<img width="1548" alt="wxai-chat-09-cleared" src="https://github.com/user-attachments/assets/0e2a21bf-0a07-4a99-935d-9885e35409f4"> 
   ここで私たちは「プロンプト・ラボにおいて、今までのチャット履歴にアクセスできないのでしょうか」という疑問が生じます。チャット履歴が残っていることを確認しましょう。

10. プロンプト・ラボの画面左上側にある[履歴]のアイコンを見つけて、クリックします。
<img width="391" alt="wxai-chat-10-historyIcon" src="https://github.com/user-attachments/assets/a120b3a2-7986-4521-b628-edde57938d41">

11. これまでのチャットの[履歴]が表示されているのを確認します。[llama-3-8b-instruct What are more efficient...]で始まる履歴をクリックします。
<img width="490" alt="wxai-chat-11-historyList" src="https://github.com/user-attachments/assets/c83b9c25-f354-4061-99e3-e8eac547e22d">

12. チャット履歴が呼び出され、プロンプト・ラボ上に表示されたことを確認します。画面右下の方にある[復元]をクリックします。
<img width="1548" alt="wxai-chat-12-RestoredChat" src="https://github.com/user-attachments/assets/d6c6f9da-8622-4bbd-9ae7-fa51c311db25">

13. チャットが復元され、[履歴]が更新されたことを確認します。
 <img width="1548" alt="wxai-chat-13-continueChat" src="https://github.com/user-attachments/assets/95e7ac17-d338-4c09-8f90-c47d06fbaf95">
    プロンプト・ラボを使って、言語モデルとのチャットを試すことができることと、履歴を呼び出すことができることを体験しました。

14. [新規プロンプト +]という文字の左側にある💾アイコンをクリックし、[名前を付けて保存]を選びます。
<img width="1426" alt="wxai-chat-14-SaveAs" src="https://github.com/user-attachments/assets/21cfba2a-0a35-4f79-90fb-d52cca057160">

15. 作業の保存ウィンドウが表示されます。[資産タイプ]から[プロンプト・セッション]を選択し、[詳細の定義]欄にある[名前]に「chat01」と入力し、最後に[保存]をクリックします。
<img width="1548" alt="wxai-chat-15-SavePromptSession" src="https://github.com/user-attachments/assets/cd9c4809-c49a-40f3-a26e-5062c20d9b8c">

16. 画面左上にある [プロジェクト]のところに、[chat01]の文字が見えることを確認します。
<img width="335" alt="wxai-chat-15-promptSession" src="https://github.com/user-attachments/assets/c4f25bd6-525a-4f39-9c28-78c505a0e7a4">

このハンズオンでは、IBM watsonx.aiのプロンプト・ラボに含まれているチャット機能を簡単に試して、プロンプト・セッションを保存するところまでを体験しました。
