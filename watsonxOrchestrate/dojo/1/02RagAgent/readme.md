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





