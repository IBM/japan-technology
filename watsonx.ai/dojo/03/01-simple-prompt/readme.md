## granite-8b-japanese 言語モデルを使い、プロンプトを改良しながら、静岡県の魅力を伝えるための文章を生成する
IBM watsonx.aiのプロンプト・ラボを使い、言語モデルとチャットしてみましょう。プロンプトは、AIに質問や指示を与えるためにユーザーが入力するものです。
参考URL: [プロンプト・ラボ](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-prompt-lab.html?context=wx&locale=ja "Prompt Lab")

免責事項: 生成AIは事前学習したデータを活用しながらテキストを生成しますが、事実と異なる結果を生成する場合があります。このハンズオンでは、意図しない結果を得ることも含んでいます。

前提条件:
* IBM watsonx 上に新規プロジェクト「Dojo #3」を作ってあること ([作成方法](https://github.com/IBM/japan-technology/tree/main/watsonx.ai/dojo/create-new-project "Create New Project"))

<img width="1524" alt="wxai03-00-newProject" src="https://github.com/user-attachments/assets/3a3a0179-c655-4c57-bc22-b90e15a7da5c">

プロジェクト作成後は、Watson Machine Learningの関連付けを確認してください。
<img width="1524" alt="wxai03-00-associatedML" src="https://github.com/user-attachments/assets/5b3248b6-9683-454b-9ed6-99e439928eff">

##

1. 作成したプロジェクトの[概要]タブを開きます。
<img width="1524" alt="wxai03-01-newproject" src="https://github.com/user-attachments/assets/1f96241e-5b48-4bae-9db2-3069d2ddff5e">

2. 作業の開始欄にある[ファウンデーション・モデルを使用したチャットとプロンプトの作成]をクリックします。
<img width="1524" alt="wxai03-01-02-promptLab" src="https://github.com/user-attachments/assets/bbd2d8fe-07df-4255-8179-24344b98bd95">

3. Prompt Labの[フリー・フォーム]をクリックします。
<img width="1521" alt="wxai03-01-03-Freeform" src="https://github.com/user-attachments/assets/86562be9-7e2e-4363-825a-4b5a51d6e078">

4. プロンプト・テキストとして、次の文字列をコピーして、貼り付けます。
```
静岡県を知らない人に、有名なアーティスト、 アニメの話、美味しい食事、名所、生産品などを含めて、楽しく静岡の魅力を伝えてください。
```

<img width="1524" alt="wxai03-01-04-simple-prompt" src="https://github.com/user-attachments/assets/bdf5cbaa-fc6d-41ed-82d9-0021bda04534">

5. 画面右下にある[生成]をクリックします。しばらく待つと生成結果が表示されます。
<img width="1524" alt="wxai03-01-05-unexpected-result" src="https://github.com/user-attachments/assets/8eaff4b9-86f4-4f7a-bd57-a5a98171b0ce">

6. 意味不明な結果を見て、ここで諦めないでください。ここから、順番に改善していきます。[出力のクリア]をクリックして、生成した内容を消去しましょう。先ほど生成された文字列が消えたことを確認します。
<img width="1521" alt="wxai03-01-06-clearOutput" src="https://github.com/user-attachments/assets/8f979ac3-1b2c-49cb-8c2b-f5ffa6daced3">

7. プロンプト・テキストをすべて消去し、新しいプロンプト・テキストを貼り付けます。
```
以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。

### 指示:
与えられた質問に対して、文脈がある場合はそれも利用し、回答してください。

### 入力:

静岡県を知らない人に、有名なアーティスト、 アニメの話、美味しい食事、名所、生産品などを含めて、楽しく静岡の魅力を伝えてください。

### 応答:

```
<img width="1521" alt="wxai03-01-07-structuredPrompt" src="https://github.com/user-attachments/assets/06b56067-de8c-42e5-afc4-1c1a09e948f8">

8. 画面右下にある[生成]をクリックします。

<img width="1521" alt="wxai03-01-08-newResult" src="https://github.com/user-attachments/assets/62f93932-241d-4209-b99c-4afc2ff819ca">

9. 画面の右上側にあるモデル・パラメータ <img width="54" alt="wxai03-01-09-modelParameters" src="https://github.com/user-attachments/assets/ac1843cb-9473-4f17-9b4d-fae32a3e0ae7">
をクリックして、開きます。

<img width="1521" alt="wxai03-01-10-openedParmeters" src="https://github.com/user-attachments/assets/2cb2d4f6-ef8b-46a4-80a8-5841edf30083">

10. プロンプト・テキストを上記手順7の内容に戻します。モデル・パラメータの小さなウィンドウ内にある最小トークン数を「200」、最大トークン数を「1000」に変更します。
<img width="1521" alt="wxai03-01-11-modifiedParameters" src="https://github.com/user-attachments/assets/c99c666b-6952-40f8-aa27-27400ec8e795">


11. 画面右下の[生成]をクリックして、結果を確認します。内容の妥当性は無視して、手順8より、もっと多くのテキストが生成されたことがわかります。
<img width="1521" alt="wxai03-01-12-resultWithMoreText" src="https://github.com/user-attachments/assets/c444313a-f9a1-49d5-9baa-1378a0700ad2">

12. [出力のクリア]をクリックして、生成されたテキストを消去します。モデル・パラメータにある[反復ペナルティ]を「2」に変更して、画面右下の[生成]をクリックします。
<img width="1521" alt="wxai03-01-13-resultWithPenelty2" src="https://github.com/user-attachments/assets/d1dfd080-e817-4793-8b61-5c476a4e6605">

この時点で、まだ出力内容に不安が残りますが、手順11と文体が変わったことを確認します。

13. プロンプト・テキストの中に、テキストを生成する上でのヒントを文脈として追加します。プロンプト・テキストをすべて消去し、新しいプロンプト・テキストを貼り付けます。

```
以下は、タスクを説明する指示と、文脈のある入力の組み合わせです。要求を適切に満たす応答を書きなさい。

### 指示:
与えられた質問に対して、文脈がある場合はそれも利用し、回答してください。知識にないことは答えないでください。

文脈:
- 静岡県の人気のレストランは「さわやか」です。さわやかには、美味しいハンバーグがあります。
- 静岡市の名所は、「三保の松原」です。海岸から富士山が見えます。
- 静岡県は、令和3年にきはだ・マグロの水揚げで日本一でした。
- 静岡県の県庁所在地は、「静岡市」です。浜松市ではありません。
- 浜松市には世界で有名な企業が複数あります。スズキ、ヤマハ、カワイといった企業は世界で有名です。カワイのピアノは、YOSHIKIさんが使っていることで有名です。
- アニメ作品「ラブライブ！サンシャイン！！」の聖地は、静岡県沼津市が中心です。伊豆・三津シーパラダイスも有名です。
- アニメ作品「ちびまる子ちゃん」の話は、静岡県静岡市清水区（旧清水市）がモデルになっています。

### 入力:
静岡県を知らない人に、有名なアーティスト、 アニメの話、美味しい食事、名所、生産品などを含めて、楽しく静岡の魅力を伝えてください。

### 応答:

```

14. 



