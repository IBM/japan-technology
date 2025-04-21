# 文書と言語モデルを利用したチャット

最終更新日: 2025/4/16

このハンズオンでは、IBM watsonx.aiのプロンプト・ラボを利用し、検索したい文書をアップロードすることで、文書に含まれる内容についてチャットできることを体験します。日本語と英語、それぞれに対応している言語モデルを使って、英語の文書に対して、日本語で質問し、日本語で回答を得るという体験もします。（下記の免責事項をよくお読みください）

前提条件:
* IBM watsonx 上に新規プロジェクトを作ってあること (全くない場合:[作成方法](https://github.com/IBM/japan-technology/tree/main/watsonx.ai/dojo/create-new-project "Create New Project"))

事前準備:
* IBM Redbooksのサイトから [Transitioning to Quantum-Safe Cryptography on IBM Z](https://www.redbooks.ibm.com/abstracts/sg248525.html "Q-Safe on Z at IBM Redbooks") の[PDFをダウンロード](https://www.redbooks.ibm.com/redpieces/pdfs/sg248525.pdf "Q-Safe on IBM z")し、PDFをローカル・コンピューター上に保存します。

免責事項: 

* watsonx 30日無料評価版やIBM Cloud からWatson Machine Learning (watsonx.ai Runtime)のライト・プランをお使いの方は、この演習を実行しないでください。PDF文書の登録だけで、無料枠の50,000トークンを使い切ります。

* この演習は、IBM watsonx.aiのチャット機能を使って、英語の文書から情報を得るための方法を紹介するものです。言語モデルに含まれている学習データとベクトル化された文書を使って、回答が生成されています。生成された結果をそのまま正解として捉えず、必ず、元の文書に含まれている情報や、信頼できる公開情報を参考にしながら、判断してください。

* この演習で利用しているIBM Redbooksの文書は2023年5月に更新されたものです。言語モデルGraninte-3.1-8B-Instructは2024年12月にリリースされたものです。従って、2024年9月時点での耐量子計算機暗号の標準化についての最新情報は含まれている可能性が高いです。日本語のプロンプトを指定した場合、言語モデル内で英語に翻訳されたプロンプトが実行され、その結果が日本語に翻訳して表示されます。このため、日本語として不自然な結果が出力される可能性があります。プロンプトの中で、文書に含まれていない「英文による省略形」の表現を指定した場合、「ハルシネーション」により事実と異なる間違った結果が出力される場合がありますので、特にご注意ください。

* 2025年4月16日時点で、Watson Machine Learning ライト・プランを使うと、50,000トークンまで利用できます。(注意：日本語のカタログ・ページには記載されておりません。ブラウザーの言語設定を「英語」にしてWatson Machine Learningの[カタログ・ページ](https://cloud.ibm.com/catalog/services/watson-machine-learning "Watson Machine Learning Catalog")で確認できます)
* トークンは文字数とは異なります。
  参考: [トークンとトークン化](https://www.ibm.com/docs/ja/watsonx/saas?topic=solutions-tokens "token")

## 

1. プロジェクトの[概要]タブを開きます。
   
<img width="1135" alt="wxai02-02-01-projectoverview" src="https://github.com/user-attachments/assets/1e800dc5-7cf1-4587-9a05-99ba8c3200ae" />

2. 作業の開始欄にある[ファウンデーション・モデルを使用したチャットとプロンプトの作成]をクリックし、プロンプト・ラボを開きます。

<img width="1135" alt="wxai02-02-02-chatmode" src="https://github.com/user-attachments/assets/3ac2f922-6af9-4b68-b8dd-06180b23d62b" />


3. チャット入力欄の左側にある[↑]にマウス・カーソルを近づけて、[文書のアップロード]と表示されることを確認します。
   
<img width="767" alt="wxai02-02-03-upload-document" src="https://github.com/user-attachments/assets/baafd038-a106-49a6-aca8-1f8efb4d16db" />

4. [↑]アイコンをクリックし、[ドキュメントの追加]と[Add image]というメニューが表示されることを確認し、[ドキュメントの追加]をクリックします。
   
<img width="716" alt="wxai02-02-04-Add-document" src="https://github.com/user-attachments/assets/f9e6ff76-68f6-4568-bb8c-a2db4b3ed37c" />


5. [ベクトル化されたドキュメントを使ったAI]ウィンドウが表示されることを確認し、[ファイルの追加]欄にある[参照]をクリックします。

<img width="1135" alt="wxai02-02-05-add-document" src="https://github.com/user-attachments/assets/5fb0998d-a191-4dd6-b063-c0770314d802" />
   
6. OS固有のファイル選択用の機能を利用し、事前準備でダウンロードしたファイルを指定します。[拡張設定]を展開して、[埋め込みモデル]のところに「granite-embedding-107m-multilingual」が選択されていることを確認します。パラメータは既定値のままでOKです。最後に[作成]をクリックします。

<img width="1137" alt="wxai02-02-06-specify-pdf" src="https://github.com/user-attachments/assets/a1696dcd-ebb3-4e66-85d6-f190847a2bee" />

7. ドキュメントが読み込まれ、メモリ上にベクトル・インデックスが作成されます。

<img width="1137" alt="wxai02-02-07-ready-to-chat" src="https://github.com/user-attachments/assets/63313854-3f43-461f-aaf0-dda0de6e1314" />

8. ここからは、耐量子計算機暗号 (Quantum Safe Cryptography)について、チャットで聞いてみましょう。

   プロンプトの例を示しておきます。

* Summarize the document.
* What are key features of Quantum Safe Security on IBM Z16?
* What is the objective of this document?
* 今の内容を日本語で説明してください。
* What kind of resources are available for the quantum protection journey?英語と日本語で教えてください。
* この文書に含まれている目次を表示してください。
* What is the IBM Z cryptographic component? 英語と日本語で回答してください。
* 耐量子計算機暗号アルゴリズムとは何ですか？
* 企業が耐量子計算機暗号を導入するためには、どのような準備が必要でしょうか？
* "Example C-1"について説明してください。
* REXXとは何ですか?
* DSAとは何ですか？
* ML-KEMとは何ですか？
* FALCONとは何ですか？
* SPHINCS+とは何ですか？
* IBM ADDIは耐量子計算機暗号化の実装にどう役立ちますか？
* ハードウェア暗号化の観点で、IBM Z16がサポートしている耐量子計算機暗号化の技術を教えてください。
* 耐量子計算機暗号化を利用するにあたり、鍵の管理はどのように行うと良いでしょうか？
* IBM Z16のセキュアな鍵保管システムについて紹介してください。

参考リソース: 
* [IBMが開発したアルゴリズムが、NISTが初めて公開した耐量子計算機暗号標準に](https://jp.newsroom.ibm.com/2024-08-16-ibm-developed-algorithms-announced-as-worlds-first-post-quantum-cryptography-standards "PQC-NIST-IBM")
* [IBM Quantum Safe Security](https://www.ibm.com/quantum/quantum-safe "IBM Q-Safe")
* [NIST’s post-quantum cryptography standards are here](https://research.ibm.com/blog/nist-pqc-standards "NIST PQC standard")

9. プロンプト・セッションを保存します。名前をQ-Safeとしてください。

<img width="1137" alt="wxai02-02-08-save-prompt-session" src="https://github.com/user-attachments/assets/9f6ac2bb-ff75-4fa0-a47b-2545b8ea8c6f" />

ハンズオンはここまでです。
様々な文書をベクトル化して、その情報を利用すると、言語モデルが学習していない内容についても回答ができます。RAG(Retrieval Augmented Generation、検索拡張生成)と呼ばれる手法を、コードを書かないで実験できます。



