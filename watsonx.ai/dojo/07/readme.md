# AI エージェントを試してみる

最終更新日: 2026/1/21

前提条件:
* IBM watsonx as a Serviceの環境にアクセスできること

免責事項:
* AIエージェントは2026/1/21時点で、まだベータ版の状態です。
* 英語での問い合わせを推奨しますが、この演習では言語モデルによる翻訳機能を通じて、日本語の問い合わせを、基盤モデル内部で英語に解釈して、英語でエージェントを実行しています。
* 開発途中の機能であるため、予告なく仕様変更が生じたり、期待通りに動作しない場合があります。ベータ版は、製品サポート対象外のため、ご注意ください。
* Google検索した結果を利用しているため、IBMが管理していないWebサイトの情報を用いて、結果が生成されます。エージェントが生成する内容は、Google検索で見つかった記事に依存した結果となりますので、得られた結果については、ご自身で事実を確認してください。

1. https://jp-tok.dataplatform.cloud.ibm.com/wx/home?context=wx を開いて、watsonxのホームページに移動します。

<img width="1093" alt="aia-01-home" src="https://github.com/user-attachments/assets/0f608599-e2ae-4593-ab57-c8a2e2b92987" />

* まだ何もプロジェクトを作っていない場合は、[新規プロジェクトの作成](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/create-new-project/readme.md)を参照して、新しいプロジェクトを作ってください。
* SkillsBuildのAIセミナーのハンズオンに参加している方は、特に作業不要です。これまでの演習で使ってきたプロジェクトをそのまま利用してください。

2. [AIエージェントを構築してタスクを自動化する]と書かれたタイルをクリックします。

<img width="1137" alt="aia-02-launch-aiagent" src="https://github.com/user-attachments/assets/dcc1ff49-1775-4b04-8626-ec989a248107" />

3. [エージェント・ラボへようこそ]の画面が表示されるので、それぞれ ☑️ を入れて同意します。

<img width="1137" alt="aia-03-welcome" src="https://github.com/user-attachments/assets/4a5f63ef-71b9-42ed-bca2-84907a593d8c" />

4. エージェント・ラボのツアーを順に進めます。

<img width="1137" alt="aia-04-tour01" src="https://github.com/user-attachments/assets/b11d2d8a-2c8e-4f6a-9a16-797f48c157e1" />

<img width="1137" alt="aia-04-tour02" src="https://github.com/user-attachments/assets/e158ac16-3853-4ddf-814e-21781f0fb19d" />

<img width="1137" alt="aia-04-tour03" src="https://github.com/user-attachments/assets/c3b702c0-fe57-4c63-a2ae-2a30bf8e16a9" />

<img width="1137" alt="aia-04-tour04" src="https://github.com/user-attachments/assets/4dd8b7d0-9db0-4d5a-be48-5a885f04a51e" />

5. [何かを入力してください]という入力欄に次のプロンプトを入力し、[Enter] キーを押します。

```
Apple Watch, Pixel Watch, Fitbitの比較表を作成してください。
```

6. 結果を確認します。

<img width="1137" alt="aia-06-result" src="https://github.com/user-attachments/assets/f33acf21-714f-4a6c-bc09-5a6bd020062d" />

7. [この答えはどうやって得たのでしょうか？]と表示されているところをクリックして内容を確認します。
* Google検索の結果を取得し、基盤モデルに存在しない情報を取得
* 得られた結果を使って基盤モデルで回答を生成

8. 英語を使って、エージェントに問い合わせしてみましょう。

プロンプト例を示します。

```
Google, Who is the CEO of IBM Corporation?
```

```
Google, please find the long history of IBM.
```

```
Google, please let me know the brief history of IBM 8 Bar logo.
```

```
Google, what is "Aitokukai"?
```

```
Google, what is "IBM watsonx.ai"?
```

```
Google, what is "IBM TechXchange Summit Japan"?
```

9. <img width="34" height="29" alt="5-1-8-reset" src="https://github.com/user-attachments/assets/e4f8a5cc-614f-4de5-81d2-dedd8c4ee2ee" />をクリックして、チャット履歴を消去します。

10. [ツールを追加する]をクリックします。
<img width="1238" height="1041" alt="5-1-10-AddTools" src="https://github.com/user-attachments/assets/ff6a9d84-3f58-4aed-bc79-0fd86b00c5e4" />

11. [Google検索]をオフ、[ウィキペディア検索]をオンにします。[ツールを選択]の右上にある[x]をクリックして、画面を閉じます。
<img width="1238" height="1041" alt="5-1-11-ToolsSetting" src="https://github.com/user-attachments/assets/3df99ec6-503f-4e9b-9c40-a56406d22c00" />

12. エージェント・ラボの画面に戻ると、[ウィキペディア検索]がツールとして追加されていることがわかります。
<img width="1238" height="1041" alt="5-1-12-WikipediaReady" src="https://github.com/user-attachments/assets/c60b46c3-d88d-448d-adc3-8af9a2562fd0" />

13. 英語を使って、エージェントに問い合わせしてみましょう。
* プロンプト:
```
Wikipedia, Who is the CEO of IBM Corporation?
```
* チャットに出力された結果に表示されている[この答えはどうやって得たのでしょうか？]をクリックして、Wikipediaツールが使われていることを確認します。
<img width="1238" height="1041" alt="5-1-13-WikipediaResult" src="https://github.com/user-attachments/assets/8d4be247-c1e3-4f8a-b2a7-9a30a16ff69a" />

14. 他のプロンプトも試してみましょう。
* プロンプト例:
```
Wikipedia, who is Kenjiro Takayanagi?
```

```
Wikipedia, what is NHK?
```

```
Wikipedia, what is key challenge of 8K broadcasting?
```

## (オプション) Wikipediaエージェントを使います。興味のある方は、試してください。

15. エージェント・ラボの[セットアップ]を展開します。
<img width="1197" height="1041" alt="5-1-15-Setup" src="https://github.com/user-attachments/assets/af664244-aae4-4e70-9c63-475a1e482e4f" />

* 名前:
```
Wikipediaエージェント
```

* 説明:
```
Wikipediaにある情報を調べます
```

16. 画面を下にスクロールし、[クイック・スタートに関する質問]を追加します。チャット欄の質問の例も自動的に更新されます。
* 質問1:
```
TVとは
```
* 質問2:
```
量子コンピューターとは
```
<img width="1474" height="1063" alt="5-1-16-QuickStart" src="https://github.com/user-attachments/assets/2f16fc62-620e-49b0-a1db-8a5fccf34c4c" />


17. 追加した質問[TVとは]をチャット欄でクリックしてみましょう。
* 応答例:
```
TVとは、映像と音を伝送する遠隔通信手段である。テレビは、広告、娯楽、ニュース、スポーツなどのマスメディアである。テレビは、1920年代に初期の実験的な形態で利用可能になったが、数年間の開発を経て、消費者向けに販売されるようになった。第二次世界大戦後、黒白テレビ放送がイギリスとアメリカで人気になり、テレビセットは家庭、事業所、機関で一般的になった。1950年代、テレビは世論を形成する主要な手段となった。1960年代中盤、カラーテレビ放送がアメリカで導入され、ほとんどの発展途上国でも同様であった。さまざまな種類のアーカイブストレージメディア（ベータマックス、VHSテープ、レーザーディスク、ハードディスクドライブ、CD、DVD、フラッシュドライブ、HD DVD、ブルーレイディスク、クラウドデジタルビデオレコーダー）が利用可能になり、視聴者は自宅で事前に録画した素材（映画など）を視聴できるようになった。リモート检索の便利さなど、さまざまな理由により、テレビおよびビデオプログラムのストレージはクラウド（Netflixのビデオオンデマンドサービスなど）でも行われるようになった。2010年代初頭、デジタルテレビ放送が大幅に普及した。別の開発は、標準解像度テレビ（SDTV）（576i、480i）から高解像度テレビ（HDTV）への移行であり、解像度が大幅に高くなった。HDTVは、1080p、1080i、720pなどの異なる形式で送信される場合がある。2010年以降、スマートテレビの発明により、Netflix、Amazon Prime Video、iPlayer、Huluなどのストリーミングビデオサービスを介して、インターネットを介したテレビ番組や映画の視聴が容易になった。2013年には、世界の79%の家庭がテレビセットを所有していた。以前のブラウン管（CRT）スクリーン表示の代替として、コンパクトで省エネルギーのフラットパネル技術（LCD、LED、OLEDディスプレイ、プラズマディスプレイ）が導入され、2000年代以降、テレビセットの販売はCRTからフラットパネルテレビに移行した。主要メーカーは、2010年代中盤にCRT、デジタルライトプロセッシング（DLP）、プラズマ、蛍光バックライトLCDの生産を終了すると発表した。LEDはOLEDに置き換えられつつある。主要メーカーは、2010年代中盤以降、スマートテレビの生産を増やしている。スマートテレビは、インターネットやWeb 2.0機能を統合したもので、2010年代後半には主要なテレビ形式となった。テレビ信号は、当初、地上波テレビ放送としてのみ配信され、高出力のラジオ周波数テレビ送信機を使用して、個々のテレビ受信機に信号を放送していた。代わりに、テレビ信号は、同軸ケーブル、光ファイバーケーブル、衛星システム、2000年代以降はインターネットを介して配信される。2000年代初頭まで、これらはアナログ信号として送信されていたが、2010年代後半までに世界中でデジタルテレビ放送への移行が完了する予定だった。標準的なテレビセットには、放送信号の受信と解码を行うチューナーを含む複数の内部電子回路が含まれている。チューナーが内蔵されていない視覚表示デバイスは、テレビではなく、ビデオモニターと呼ばれる。テレビ放送は、主に単方向放送であるため、送信機は受信できず、受信機は送信できない。
```
<img width="1474" height="1063" alt="5-1-17-AboutTV" src="https://github.com/user-attachments/assets/f3541de1-98e5-4b13-8970-ab4713590754" />


18. チャットをクリアし、[量子コンピューターとは]をクリックしてみましょう。ツールに渡すキーワードが判別できないため、おそらく動作しません。

19.　[量子コンピューターとは]、このクイック・スタートに関する質問を変更します。
* 質問2:
```
Quantum Computerとは
```

20. 追加した質問をチャット欄でクリックしましょう。


このハンズオンは以上となります。

## まとめ
* watsonx エージェント・ラボは、LangGraphを用いて、様々なツールを組み合わせて、複雑な問い合わせに対応できるように設計されています。
* 特にビジネスのためのAI開発においては、企業や組織のデータにアクセスするツールを準備して、エージェントから利用できるようにしていくことが求められます。
* LangGraphについて詳しく知りたい方は、https://www.langchain.com/langgraph へアクセスしてください。




