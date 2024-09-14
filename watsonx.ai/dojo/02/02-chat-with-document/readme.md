# 文書と言語モデルを利用したチャット
このハンズオンでは、IBM watsonx.aiのプロンプト・ラボを利用し、検索したい文書をアップロードすることで、文書に含まれる内容についてチャットできることを体験します。日本語と英語、それぞれに対応している言語モデルを使って、英語の文書に対して、日本語で質問し、日本語で回答を得るという体験もします。（下記の免責事項をよくお読みください）

事前準備:
* IBM Redbooksのサイトから [Transitioning to Quantum-Safe Cryptography on IBM Z](https://www.redbooks.ibm.com/abstracts/sg248525.html "Q-Safe on Z at IBM Redbooks") の[PDFをダウンロード](https://www.redbooks.ibm.com/redbooks/pdfs/sg248525.pdf "Q-Safe on IBM z")し、PDFをローカル・コンピューター上に保存します。

免責事項: 

* この演習は、IBM watsonx.aiのチャット機能を使って、英語の文書から情報を得るための方法を紹介するものです。言語モデルに含まれている学習データとベクトル化された文書を使って、回答が生成されています。生成された結果をそのまま正解として捉えず、必ず、元の文書に含まれている情報や、信頼できる公開情報を参考にしながら、判断してください。

* この演習で利用しているIBM Redbooksの文書は2023年5月に更新されたものです。言語モデルmixtral-8x7bは2023年12月にリリースされたものです。従って、2024年9月時点での耐量子計算機暗号の標準化についての最新情報は含まれていません。日本語のプロンプトを指定した場合、言語モデル内で英語に翻訳されたプロンプトが実行され、その結果が日本語に翻訳して表示されます。このため、日本語として不自然な結果が出力される可能性があります。プロンプトの中で、文書に含まれていない「英文による省略形」の表現を指定した場合、「ハルシネーション」により事実と異なる間違った結果が出力される場合がありますので、特にご注意ください。


## 

1. プロジェクトの[概要]タブを開きます。
   <img width="1548" alt="wxai-chat2-01-projOverview" src="https://github.com/user-attachments/assets/6741085e-fbdb-4c5c-8959-c20dba87e793">

2. 作業の開始欄にある[ファウンデーション・モデルを使用したチャットとプロンプトの作成]をクリックし、プロンプト・ラボを開きます。
   <img width="1548" alt="wxai-chat2-02-ChatTop" src="https://github.com/user-attachments/assets/aedfa7e8-d5b4-45ba-8598-a65754d60b53">

3. チャット入力欄の左側にある[↑]にマウス・カーソルを近づけて、[文書のアップロード]と表示されることを確認します。
   <img width="895" alt="wxai-chat2-03-UploadDocIcon" src="https://github.com/user-attachments/assets/85465156-d0c4-4090-ba11-73f0e7f6d49a">

4. [↑]アイコンをクリックし、[ドキュメントの追加]と[Add image]というメニューが表示されることを確認し、[ドキュメントの追加]をクリックします。
   
   <img width="854" alt="wxai-chat2-04-UploadMenu" src="https://github.com/user-attachments/assets/6c166302-dac8-4609-a2ac-89622ac6e321">

5. [ベクトル化されたドキュメントを使ったAI]ウィンドウが表示されることを確認し、[ファイルの追加]欄にある[参照]をクリックします。
   <img width="1548" alt="wxai-chat2-05-CreateVectorDb" src="https://github.com/user-attachments/assets/f000bd0f-16c5-41f2-ae78-3647bf36e864">
   
6. OS固有のファイル選択用の機能を利用し、事前準備でダウンロードしたファイルを指定します。[拡張設定]を展開して、[埋め込みモデル]のところに「all-MiniLM-L6-v2」が選択されていることを確認します。パラメータは既定値のままでOKです。最後に[作成]をクリックします。
   <img width="1548" alt="wxai-chat2-06-AddPDF" src="https://github.com/user-attachments/assets/e6697037-38e5-4953-9875-b0db2bb87029">

7. ドキュメントが読み込まれ、メモリ上にベクトル・インデックスが作成されます。[モデル:llama-3-8b-insruct][v]と表示されているところをクリックし、[すべての基盤モデルを表示する」をクリックします。
   <img width="1548" alt="wxai-chat2-07-ChatWithRedbook-toppage" src="https://github.com/user-attachments/assets/00d57687-89de-4591-a521-cc909a110d2c">

8. [基盤モデルの選択]ウィンドウが表示されます。[mixtral-8x7b-instruct-v01]モデルをクリックします。
   <img width="1548" alt="wxai-chat2-08-ChooseMixtral" src="https://github.com/user-attachments/assets/0b2e96ff-14ce-43b9-a629-793ad7dcfbe5">

9. [mixtral-8x7b-instruct-v01]のモデル・カードが表示されます。カード内をスクロールすることで、モデルに含まれている情報を確認できます。最後に[モデルの選択]をクリックします。
   <img width="1548" alt="wxai-chat2-09-MixtralModelCard" src="https://github.com/user-attachments/assets/212eafdd-d9a9-46ec-abec-8a83bad3ad33">

10. チャットで利用するモデルが[mixtral-8x7b-instruct-v01]に変わったことを確認します。
   <img width="1548" alt="wxai-chat2-10-MixtralReady" src="https://github.com/user-attachments/assets/2bd634cc-1f95-403c-804c-e6fc72d9c6a8">

11. ここからは、耐量子計算機暗号 (Quantum Safe Cryptography)について、チャットで聞いてみましょう。

   プロンプトの例を示しておきます。

* Summarize the document.
* What are key features of Quantum Safe Security on IBM Z16?
* 今の内容を日本語で説明してください。
* 耐量子計算機暗号アルゴリズムとは何ですか？
* 企業が耐量子計算機暗号を導入するためには、どのような準備が必要でしょうか？
* DSAとは何ですか？
* ML-KEMとは何ですか？
* FALCONとは何ですか？
* SPHINCS+とは何ですか？
* IBM ADDIは耐量子計算機暗号化の実装にどう役立ちますか？
* ハードウェア暗号化の観点で、IBM Z16がサポートしている耐量子計算機暗号化の技術を教えてください。
* 耐量子計算機暗号化を利用するにあたり、鍵の管理はどのように行うと良いでしょうか？
* セキュアな鍵保管システムについて紹介してください。

参考リソース: 
* [IBMが開発したアルゴリズムが、NISTが初めて公開した耐量子計算機暗号標準に](https://jp.newsroom.ibm.com/2024-08-16-ibm-developed-algorithms-announced-as-worlds-first-post-quantum-cryptography-standards "PQC-NIST-IBM")
* [IBM Quantum Safe Security](https://www.ibm.com/quantum/quantum-safe "IBM Q-Safe")
* [NIST’s post-quantum cryptography standards are here](https://research.ibm.com/blog/nist-pqc-standards "NIST PQC standard")

12. プロンプト・セッションを保存します。名前をQ-Safeとしてください。

<img width="1548" alt="wxai-chat2-11-SaveAsQSafe" src="https://github.com/user-attachments/assets/2a95d7f3-61d9-4eb4-9903-772879342265">




