# watsonx Orchestrate AI エージェント体験 Part 2
この演習は、IBMについて回答するAIエージェント 'IBMInfo' にRAGの手法で知識を追加します。Part 1が終わっている状態からスタートしますので、ご注意ください。

* Knowledgeの追加

1. IBMInfoエージェント管理ページ左側にある[Knowledge]をクリックし、[Knowledge source]セクションにある[Choose knowledge +]をクリックします。
<img width="1110" height="1024" alt="19Knowledge" src="https://github.com/user-attachments/assets/07181d1c-f1d7-41ab-accf-e337f4f81ef9" />

2. [Choose knowledge source]の画面で、[Upload files]を選択し、[Next]をクリックします。
<img width="1110" height="1024" alt="20UploadFile" src="https://github.com/user-attachments/assets/80757589-5310-4236-a1e2-2fe2266fd41f" />

3. こちらの[リンク](https://ibm.github.io/ba-handson-jp/wxoagent/files/2024-annual-report.pdf)を利用し、ローカル・コンピューターに2024-annual-report.pdfファイルをダウンロードします。

4. 青色で表示されている[Drag and drop files here or click to upload]のところへ、ダウンロードしたファイルをドラッグ＆ドロップする、あるいは、リンクをクリックして2024-annual-report.pdfファイルをアップロードします。
<img width="1110" height="1024" alt="21FilePicker" src="https://github.com/user-attachments/assets/cfddbd4d-64e4-4cc5-8fd1-7e8b7f4330d6" />

5. 2024-annual-report.pdfファイルを指定できたので、[Next]をクリックします。

<img width="1110" height="1024" alt="22FileSelected" src="https://github.com/user-attachments/assets/6208fb40-eb08-4114-8c66-56097f75e6cf" />

6. [Description]の入力を行います。このDescription(説明)はエージェントに知識の内容を知らせるものです。下記のDescriptionを入力し、[Save]をクリックします。

* Description:  ```これは2024年のIBMの年次報告書です。財務情報とIBMのコア事業戦略を含んでいます。```
<img width="1110" height="1024" alt="23KnowledgeDescription" src="https://github.com/user-attachments/assets/f33c858b-4865-4b22-9d5e-c314237191cc" />

7. [Knowledge source]セクションを見ると、[Processing...]の文字が表示されています。アップロードしたPDFと入力したDescriptionを用いて、AIエージェントが利用できるKnowledgeが準備されます。処理が終わるまで、しばらく待ちます。（参考:この資料を作成した際には、1分15秒程度で完了しました）

<img width="358" height="392" alt="24FileProcessing" src="https://github.com/user-attachments/assets/93561435-a1f9-40dc-b65f-0b40671d7702" />

8. 処理が終わると、[Knowledge source]の[Files]セクションに、Connectedの文字、File nameに2024-annual-report.pdf、Knowledge source descriptionに指定した'これは2024年のIBMの年次報告書です。財務情報とIBMのコア事業戦略を含んでいます。'の文字が見えます。
<img width="1448" height="997" alt="25FileLoaded" src="https://github.com/user-attachments/assets/936d21c0-da3e-4b4e-8372-1c62a25846d0" />

9. AIエージェントの[Preview]画面を利用して、アップロードした文書に関する質問を送信しましょう。
* 入力内容: ```IBMの2024 年のフリー・キャッシュ・フローはいくらですか。```
<img width="549" height="66" alt="26Q6CashFlow" src="https://github.com/user-attachments/assets/d48af3b8-fa10-4bac-b6f2-796b6874c5e3" />


10. しばらく待つと、AIエージェントから「$12.7 billion」と回答が表示されます。

<img width="537" height="188" alt="27A6CashFlow" src="https://github.com/user-attachments/assets/09afd159-dee1-41f1-bf30-a916f08e24f0" />

11. 2024-annual-report.pdfを開いて、PDFファイルの3ページ目を開きます。(文書の中に表示されているページ数だと1ページ目です。）
次の内容が確認できます。
```
2024 Performance
For the year, IBM generated $62.8 billion in revenue, up 3%
at constant currency, and $12.7 billion in free cash flow — an
increase of $1.5 billion year-over-year.
```

12. [IBMInfo]の回答時刻の右側に表示されている[Show Reasoning v]をクリックします。

<img width="531" height="463" alt="28A6Reasoning" src="https://github.com/user-attachments/assets/9345c974-0654-4bc6-9db7-07905a66a94a" />

* Step 1に [Tool: knowledge_for_agent_IBMInfo] の文字が見えます。質問に対して、先ほど作成したKnowledgeをツールとして利用したことがわかります。

13. IBMInfoに対して、別の質問を実行してみましょう。 
* 入力内容: ```2024年に前年比でFree cash flowはどれだけ変化しましたか、単位を含めて、金額で答えてください。```
* 上記手順11で確認した文章に含まれている内容についての質問です。

<img width="540" height="278" alt="29QA7IncreasedFreeCashFlow" src="https://github.com/user-attachments/assets/c738f6dc-b8c8-4916-8ee3-c5621ed4b00d" />

14. 違うページに含まれている情報について、質問してみましょう。
* 入力内容: ```Management discussionに書かれている2024年のRevenueは、2023年と比べて何％成長しましたか。```

<img width="537" height="220" alt="30QA8-RevenueYoY2024" src="https://github.com/user-attachments/assets/19b0450c-2b67-49e3-9c78-3c939f54838c" />

15. 2024-annual-report.pdfを開いて、PDFの10ページ(文書の8ページ)を確認します。表にある[Revenue]の行を確認しましょう。

* 情報ソース: [2024 IBM Annual Report](https://www.ibm.com/downloads/documents/us-en/1227c12d3a38b173)
<img width="653" height="492" alt="30-02-DocTable" src="https://github.com/user-attachments/assets/29d18bcd-7f4d-471f-ae08-cffacc26f374" />


16. 作成したIBMInfoエージェントをデプロイします。右上の[Deploy]をクリックします。
<img width="1150" height="997" alt="31Deploy01" src="https://github.com/user-attachments/assets/91cbafb4-d134-4dae-90ef-f08729d10b6b" />

17. [Pre-deployment Summary]の画面が表示されるので、右下にある青色の[Deploy]をクリックします。
<img width="1106" height="953" alt="32Deploy02" src="https://github.com/user-attachments/assets/93013a0a-4a0c-480a-92ac-445258edba8c" />

18. しばらく待つと、画面右上に[Success]と表示されます。作成したAIエージェントが利用できます。
<img width="1150" height="997" alt="33Deployed" src="https://github.com/user-attachments/assets/f2b41f20-aaf4-4aab-b5e5-d745bd212875" />

19. 左上のメニューから[Chat]をクリックします。
<img width="249" height="193" alt="34ChatMenu" src="https://github.com/user-attachments/assets/da98cedc-6c40-4b5c-a08c-8b8635dae80c" />

20. AIエージェント、[IBMInfo]を選択します。
<img width="307" height="277" alt="35ChooseAgent" src="https://github.com/user-attachments/assets/f9113463-e802-4218-89c4-7b62717342d1" />

21.IBMInfoに次の質問を送信します。
* 入力内容: ```IBMの2024 年のフリー・キャッシュ・フローはいくらですか。```
  
<img width="1150" height="997" alt="36Q9FreecashFlow" src="https://github.com/user-attachments/assets/9c82b31b-e764-4adc-93a9-84f45605cef9" />

22. AIエージェントが回答するのを確認します。
<img width="1032" height="328" alt="37A9FreecashFlow" src="https://github.com/user-attachments/assets/9a523eba-6e3e-434e-8566-3d0fe385ccaa" />

23. 👍をクリックして、フィードバックを送信します。
<img width="1150" height="997" alt="38Feedback-Concise" src="https://github.com/user-attachments/assets/0addaf1c-f580-49e9-866f-b0a6b3379c2d" />




