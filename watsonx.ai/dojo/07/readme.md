# AI エージェントを試してみる

前提条件:
* IBM watsonx as a Serviceの環境にアクセスできること

免責事項:
* AIエージェントは2025/4/21時点で、まだベータ版の状態です。
* 英語での問い合わせを推奨しますが、この演習では言語モデルによる翻訳機能を通じて、日本語の問い合わせを英語として解釈しています。
* 開発途中の機能であるため、予告なく仕様変更が生じたり、期待通りに動作しない場合があります。サポート対象外のため、ご注意ください。

1. https://jp-tok.dataplatform.cloud.ibm.com/wx/home?context=wx を開いて、watsonxのホームページに移動します。

<img width="1093" alt="aia-01-home" src="https://github.com/user-attachments/assets/0f608599-e2ae-4593-ab57-c8a2e2b92987" />


2. [AIエージェントを構築してタスクを自動化する]と書かれたタイルをクリックします。

<img width="1137" alt="aia-02-launch-aiagent" src="https://github.com/user-attachments/assets/dcc1ff49-1775-4b04-8626-ec989a248107" />

3. [エージェント・ラボへようこそ]の画面が表示されるので、それぞれ ☑️ を入れて同意します。

<img width="1137" alt="aia-03-welcome" src="https://github.com/user-attachments/assets/4a5f63ef-71b9-42ed-bca2-84907a593d8c" />

4. エージェント・ラボのツアーを順に進めます。

<img width="1137" alt="aia-04-tour01" src="https://github.com/user-attachments/assets/b11d2d8a-2c8e-4f6a-9a16-797f48c157e1" />

<img width="1137" alt="aia-04-tour02" src="https://github.com/user-attachments/assets/e158ac16-3853-4ddf-814e-21781f0fb19d" />

<img width="1137" alt="aia-04-tour03" src="https://github.com/user-attachments/assets/c3b702c0-fe57-4c63-a2ae-2a30bf8e16a9" />

<img width="1137" alt="aia-04-tour04" src="https://github.com/user-attachments/assets/4dd8b7d0-9db0-4d5a-be48-5a885f04a51e" />

5. エージェントに次のプロンプトを入力し、[Enter] キーを押します。

```
Apple Watch, Pixel Watch, Fitbitの比較表を作成してください。
```

6. 結果を確認します。

<img width="1137" alt="aia-06-result" src="https://github.com/user-attachments/assets/f33acf21-714f-4a6c-bc09-5a6bd020062d" />

7. [この答えはどうやって得たのでしょうか？]と表示されているところをクリックして内容を確認します。
* Google検索の結果を取得し、言語モデルに存在しない情報を取得
* 得られた結果を使って言語モデルで回答を生成

このハンズオンは以上となります。

watsonx エージェント・ラボは、LangGraphを用いて、様々なツールを組み合わせて、複雑な問い合わせに対応できるように設計されています。
特にビジネスのためのAI開発においては、企業や組織のデータにアクセスするツールを準備して、エージェントから利用できるようにしていくことが求められます。
LangGraphについて詳しく知りたい方は、https://www.langchain.com/langgraph へアクセスしてください。




