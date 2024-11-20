# (オプション) OpenAPI builder
watsonx Orchestrate でカスタムスキルを使う際には、OpenAPIの仕様書が必要です。ただ、時には仕様書がない場合もあります。その際に、仕様書を作成できるのが OpenAPI Builder です。

このLabでは、OpenAPI builder を用いて Open API の仕様書（OAS）の作成、編集、生成を行う方法を練習します。


## 資料の Web ページから OpenAPI 仕様書を生成してみよう
AIを使用して、資料の Web ページから OpenAPI の仕様書を生成できます。手順は以下のようになります。

 1. メニュー(≣)から **Skill studio** を選択します。  
 ![alt text](OpenAPI_images/image-0.png) 

 2. 右上にある **Create** ボタンをクリック、**Import API** をクリックします。  
 ![alt text](OpenAPI_images/image-1.png)

 3. **OpenAPI builder (experimental)** を選択し、**OpenAPI builder** のタイルをクリックします。
 ![alt text](OpenAPI_images/image-2.png)

 4. **AI generate a new OpenAPI spec** を選択します。
    1. **Import URL** の欄にAPI仕様書を作成したい文書のURLを入力します。
          - 例えば、Github の REST API からOpenAPIの仕様書を作りたい場合は次のURLを入力します。<br /> https://docs.github.com/en/enterprise-server@3.5/rest/orgs/orgs
          - 空のボックスをクリックすると、チュートリアル用のURLが候補として表示されます。
    2. **Generate** をクリックします。
 ![alt text](OpenAPI_images/image-3.png)  

 5. OpenAPI の仕様書に入れたいエンドポイントを選択し、**Generate Selected** をクリックします。
 ![alt text](OpenAPI_images/image-4.png)

 7. OpenAPI の仕様書が生成され、選択したエンドポイントが含まれていることが確認できます。
 ![alt text](OpenAPI_images/image-5.png)

以上で、OpenAPI 仕様書を生成し、編集を始められるようになりました。

## 既存のOpenAPI 仕様書を開いてみよう
watsonx Orchestrate では、既存のOpenAPI 仕様書を開いて編集することも可能です。

 1. 先ほどの手順 1~3 を行い、**Open an existing spec** を選択します。
 ![alt text](OpenAPI_images/image-6.png)

 2. 以下のいずれかの手順で、既存のOpenAPI 仕様書を開くことができます。
    1. **Import URL** に仕様書のURLを入力し、**Download from URL** をクリックします。（空のボックスをクリックすると、チュートリアル用のURLが候補として表示されます）  
     ![alt text](OpenAPI_images/image-7.png)

    2. ご自身のローカルシステムから仕様書を開きたい時は、
        1. **ファイルを選択** をクリックします。
        2. 必要なファイルを選択し、**開く** をクリックします。
        3. **Open Local** をクリックします。
     ![alt text](OpenAPI_images/image-8.png)
    
これで、OpenAPI builder上でOpenAPI 仕様書を開くことができました。

## 一から OpenAPI 仕様書を作ってみよう
OpenAPI builder を使用すると、scratch からも OpenAPI 仕様書を作成することができます。

 1. 先ほどの手順 1~3 を行い、**Create a spec** を選択します。
 ![alt text](OpenAPI_images/image-9.png)

 2. 書き始めのテンプレートが表示されるので、仕様を自由に追加します。仕様書の作成方法については、
 <a href="https://www.ibm.com/docs/ja/watson-orchestrate?topic=skills-creating-openapi-specifications" target="_blank" rel="noopener noreferrer">こちら</a>
 もご覧ください。  
 ![alt text](OpenAPI_images/image-10.png)

 3. ファイルの変更を保存するには、**Apply changes** をクリックします。  
 ファイルをダウンロードする際は、**Download spec** をクリックします。
 ![alt text](OpenAPI_images/image-11.jpeg)

ここで作成したOpenAPI 仕様書をインポートし、watsonx Orchestrate にスキルとして追加することも可能です。

## OpenAPI builderのエディターを使ってみよう
OpenAPI builderでは、AIを用いて文書からOpenAPI 仕様書を作成したり、AIの提案をもとに仕様書を編集することが可能です。

以下のフォーマットから、仕様書を確認、編集することができます。

 - **Visual+AI view**<br /> 
 Visual+AI view では、視覚的な表示で API 仕様書を作成することができます。AI による提案を使用することもできます。このエディターで編集する方法については
 <a href="https://www.ibm.com/docs/ja/watson-orchestrate?topic=builder-using-visual-editor-in-openapi" target="_blank" rel="noopener noreferrer">こちら</a>
 をご参照ください。
 ![alt text](OpenAPI_images/image-20.png)

 - **JSON view**<br /> 
 JSON View では、テキスト形式で API 仕様書を作成できます。
 ![alt text](OpenAPI_images/image-21.png)

 - **OpenAPI view**<br /> 
 OpenAPI view では、標準のAPI仕様書の形式に従って表示されます。
 ![alt text](OpenAPI_images/image-22.png)
 
 デフォルトでは、JSON view と OpenAPI view が表示されています。Visual+AI view を表示するには、上部の **Visual+AI view** ボタンをオンにします。  
 ![alt text](OpenAPI_images/image-23.png)

**注釈:** 家のアイコンをクリックすると、OpenAPI builder のホームページが表示されます。

## OpenAPI仕様書を OpenAPI builder からダウンロードしてみよう
OpenAPI builder から、OpenAPI 仕様書を JSON ファイルでローカルにダウンロードし、watsonx Orchestrate や他のツールにインポートすることができます。もちろん、OpenAPI builder に再インポートして編集することも可能です。

ダウンロードするには、エディターの画面で **Download spec** をクリックします。
![alt text](OpenAPI_images/image-24.png)

## お疲れさまでした！
このLabでは、OpenAPI builder を用いて、OpenAPI の仕様書を作成、編集、生成する方法を確認しました。

 - 仕様書はWebページからAIで自動生成できるほか、既存ファイルの編集や、新規作成も可能です。
 - 作成時のビューは、Visual+AI view、JSON view、OpenAPI view の3つを使用でき、AIによる提案も活用できます。
 - 仕様書の作成後は、watsonx Orchestrate にインポートしてスキルとして利用できます。