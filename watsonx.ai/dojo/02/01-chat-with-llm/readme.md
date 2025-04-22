## 言語モデルを使ったチャット機能を試す

最終更新日: 2025/4/22

IBM watsonx.aiのプロンプト・ラボを使い、言語モデルとチャットしてみましょう。プロンプトは、AIに質問や指示を与えるためにユーザーが入力するものです。
参考URL: [プロンプト・ラボ](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-prompt-lab.html?context=wx&locale=ja "Prompt Lab")

前提条件:
* IBM watsonx 上に新規プロジェクトを作ってあること ([作成方法](https://github.com/IBM/japan-technology/tree/main/watsonx.ai/dojo/create-new-project "Create New Project"))
* プロジェクトを作成した直後であれば、特に何もしないで、表示されているプロジェクトの画面から作業を継続してください。

参考: 
* 作成済みのプロジェクトの参照方法: ブラウザーから https://jp-tok.dataplatform.cloud.ibm.com/projects/?context=wx を開きます。
##

1. 作成したプロジェクトの[概要]タブを開きます。

<img width="1144" alt="wxai02-01-01-project-overview" src="https://github.com/user-attachments/assets/3c1d12fa-0ca4-4aed-bced-24d8c0da5b7c" />

* [リソース使用量]のタイルにある、[トークン]の数が、現在、watsonx.aiで使ったトークン数の合計となります。watsonx無料評価版、IBM CloudからWatson Machine Learningをライト・プラン（無料枠）で利用している場合、50,000トークンまで利用できます。言語モデルによる推論を実行する度に、トークンが消費されますので、気になる方は、この先の演習を進めながら、プロジェクトの概要ページで確認してください。 


2. 作業の開始欄にある[ファウンデーション・モデルを使用したチャットとプロンプトの作成]をクリックします。

<img width="1144" alt="wxai02-01-02-prompt-lab" src="https://github.com/user-attachments/assets/c6430d37-fdf5-4a1e-93aa-73cc9e805e17" />

3. Prompt Labの利用条件にすべて☑️を入れて、[ツアーの開始]をクリックします。

<img width="1144" alt="wxai02-01-03-user-consent" src="https://github.com/user-attachments/assets/25d04fbd-96df-451f-834a-cce870590946" />


4. Prompt Labのツアーが表示されますので、[次へ]で進んでいき、最後に[完了]をクリックします。

<img width="1144" alt="wxai02-01-04-tour1" src="https://github.com/user-attachments/assets/399bdea2-4f5e-4d29-93ce-cc31b3b82b9b" />

<img width="1144" alt="wxai02-01-04-tour2" src="https://github.com/user-attachments/assets/d77c4a44-1913-4445-95cc-a5f950d171e3" />

<img width="1144" alt="wxai02-01-04-tour3" src="https://github.com/user-attachments/assets/5c25bfee-4092-439b-89f1-1c11075edcfb" />

<img width="1144" alt="wxai02-01-04-tour4" src="https://github.com/user-attachments/assets/49004d58-0c66-40ec-a68c-b0e48ec6cab8" />


5. IBM watsonx.aiのプロンプト・ラボが開き、チャットの準備ができたことを確認します。質問の例に表示されている[What are more efficient alternative to a 'for loop' in Python?]をクリックします。

<img width="1144" alt="wxai02-01-05-python-prompt" src="https://github.com/user-attachments/assets/cff49537-297f-421a-b14f-41a90714b257" />


6. チャット機能が llama-3-3-70b-instruct 言語モデルを呼び出し、回答を生成するのを確認します。英語とコード・スニペット（Python言語の短いコード)を交えた回答が表示されます。

<img width="1144" alt="wxai02-01-06-response-python" src="https://github.com/user-attachments/assets/6b8a9956-8d0d-4d3b-84f9-6b9a52a5bf54" />


7. [何かを入力してください]と表示されているテキスト・ボックスに

```今の内容を日本語で説明してください。```

と入力し、[Enter]キーを押します。

<img width="1144" alt="wxai02-01-07-response-japanese" src="https://github.com/user-attachments/assets/58b78619-427f-4854-bf7d-cba1b60a5ee7" />


直前に英語で回答された内容が日本語で説明されます。チャット機能は直前のプロンプトや生成内容を覚えているので、気になることがあれば、どんどん質問しましょう。

8. [何かを入力してください]と表示されているテキスト・ボックスに

```今の内容を韓国語で説明してください。```

と入力し、[Enter]キーを押します。

<img width="1144" alt="wxai02-01-08-response-korean" src="https://github.com/user-attachments/assets/64a8dff8-bee1-4d47-842f-8a5e257b0d29" />


ここで言語モデルの便利な点が体験できました。多言語の生成ができる言語モデルを利用していると、ある自然言語から別の自然言語への翻訳を言語モデル自身に任せることができます。

9. チャットのクリア機能を呼び出します。
<img width="823" alt="wxai-chat-07-ClearChat" src="https://github.com/user-attachments/assets/eb601335-e501-4101-9fbd-e92cc9392de9">

10. チャットをクリアして良いか、確認ダイアログ・ウィンドウが表示されます。迷わずに[クリア]をクリックします。

<img width="1144" alt="wxai02-01-10-clear-chat-confirm" src="https://github.com/user-attachments/assets/aa151e8b-72ed-4099-a960-f28783ecb684" />

11. チャットの初期画面に戻ったことを確認します。

<img width="1144" alt="wxai02-01-11-chat-initial" src="https://github.com/user-attachments/assets/07aeebd6-c45e-4065-95b2-1ea63540b8d5" />


   ここで私たちは「プロンプト・ラボにおいて、今までのチャット履歴にアクセスできないのでしょうか」という疑問が生じます。チャット履歴が残っていることを確認しましょう。

12. プロンプト・ラボの画面左上側にある[履歴]のアイコンを見つけて、クリックします。
<img width="391" alt="wxai-chat-10-historyIcon" src="https://github.com/user-attachments/assets/a120b3a2-7986-4521-b628-edde57938d41">

13. これまでのチャットの[履歴]が表示されているのを確認します。[llama-3-3-70b-instruct What are more efficient al...]で始まる履歴をクリックします。

<img width="343" alt="wxai02-01-13-history" src="https://github.com/user-attachments/assets/67b3284c-f46e-4627-8266-aef994c2fda0" />


14. チャット履歴が呼び出され、プロンプト・ラボ上に表示されたことを確認します。画面右下の方にある[復元]をクリックします。

<img width="1144" alt="wxai02-01-14-restore-chat" src="https://github.com/user-attachments/assets/02babfea-7c7b-4140-bb78-b08671b5079e" />


15. チャットが復元され、[履歴]が更新されたことを確認します。

<img width="1144" alt="wxai02-01-15-continue-chat" src="https://github.com/user-attachments/assets/a5e3333b-0b07-4a95-b01b-5d92353d9571" />

* プロンプト・ラボを使って、言語モデルとのチャットを試すことができることと、履歴を呼び出すことができることを体験しました。

16. [新規プロンプト +]という文字の左側にある💾アイコンをクリックし、[名前を付けて保存]を選びます。

<img width="841" alt="wxai02-01-16-saveas" src="https://github.com/user-attachments/assets/0e20a708-1059-4d16-addd-afd0e86fde27" />


17. 作業の保存ウィンドウが表示されます。[資産タイプ]から[プロンプト・セッション]を選択し、[詳細の定義]欄にある[名前]に
```chat01```と入力し、最後に[保存]をクリックします。

<img width="1144" alt="wxai02-01-17-saveas-promptsession" src="https://github.com/user-attachments/assets/a6c1a27c-6e12-4cfa-827b-04d9680cbacf" />


18. 画面左上にある [プロジェクト]のところに、[chat01]の文字が見えることを確認します。

<img width="301" alt="wxai02-01-18-prompt-session" src="https://github.com/user-attachments/assets/c85b23a1-1b69-4d92-a7bb-bd11b91863bc" />

このハンズオンでは、IBM watsonx.aiのプロンプト・ラボに含まれているチャット機能を簡単に試して、プロンプト・セッションを保存するところまでを体験しました。

参考: 2025/4/22 に作業した結果では、この演習で5,016トークンを消費しました。
<img width="1145" alt="wxai02-01-used-numoftoken" src="https://github.com/user-attachments/assets/5d708478-030f-4a3e-8054-ab6b0216fcfe" />

* SkillsBuildのセミナーに参加されている方は、[granite-8b-japanese 言語モデルを使い、フリー・フォームのプロンプトを改良しながら、地方の魅力を伝えるための文章を生成する](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/01-simple-prompt/readme.md)、へ進んでください。


