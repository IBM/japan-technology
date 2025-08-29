# Planning Analytics for Excel（PAfE）の設定ガイド

> 本ガイドは、2024年5月2日に公開された [Configure Planning Analytics for Excel](https://community.ibm.com/community/user/blogs/yin-chu/2024/05/02/pafe-configure)記事をもとに作成されています。  
> ただし、Planning Analytics on Cloud 環境や PAfE アドインの仕様、UI、動作手順は継続的に変更される可能性があります。  
> 内容や手順が本ガイドと一致しない場合は、**IBM の最新ドキュメントやサポートページを必ず参照**し、最新版に沿って設定・運用を行ってください。

---

## 概要

**Planning Analytics for Excel（PAfE）** は、IBM Planning Analytics データと対話・分析を行うための Microsoft Excel® アドインです。  
Excel の親しみあるインターフェースを維持しながら、従来のスプレッドシートの課題（古いデータ、整形崩れなど）を解消します。

公式情報はこちら：  
[IBM Planning Analytics for Excel (PAfE)](https://www.ibm.com/products/planning-analytics/excel)

---

## Tips & トラブルシューティング

- 他の Excel アドインとの競合がある場合、単一セッション起動が必要になることがあります。
- アドインとしてインストールする場合、`.xll` ファイルを「IBM_PAfE_x64.xll」などの汎用的な名前に変更することで、将来的なアップグレードが容易になります。
- Planning Analytics Workspace（PAW）との互換性を保つには、±1バージョンの範囲内に保ってください。
- Excel のビット数（32bit／64bit）とアドインのビット数は一致している必要があります。
- 接続URLは環境（オンプレ／クラウド）によって異なります。詳細は「PAW との接続」を参照してください。

---

## ダウンロード手順

1. [こちら](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=components-planning-analytics-microsoft-excel-cloud-only)から Planning Analytics Workspace にアクセス
2. ホーム画面で「Administration（管理）」タイルをクリック
3. 「Excel and Customizations（Excel とカスタマイズ）」を選択
4. 希望のバージョンを選んで「Download Update」をクリック（最新3バージョンが選択可能）
5. `Integration<version>.zip` という名前のアーカイブがダウンロードされます
6. ZIP を展開すると 32bit / 64bit の両方が含まれています

---

## 単一セッションで起動する方法

**※既にアドインとして有効化されている場合は、この方法を使用しないでください。Excel がクラッシュします。**

1. `.xll` ファイルをダウンロードして任意のディレクトリに配置
2. そのディレクトリが Excel の「信頼できる場所」として設定されていることを確認
3. `.xll` ファイルをダブルクリックして起動
4. セキュリティ警告が出た場合は有効化する

---

## アドインとして常時有効にする方法（全セッション対象）

1. `.xll` ファイルをダウンロードし、任意のフォルダに移動
2. ファイル名を汎用名に変更（例：`IBM_PAfE_x64.xll`）
3. Excel を起動
4. 「開発」タブ → 「アドイン」 → 「参照」で `.xll` ファイルを選択
5. 「OK」で有効化完了

---

## Planning Analytics サーバーへの接続方法

どのインストール方法でも接続手順は共通です：

1. Excel を起動し、「IBM Planning Analytics」タブをクリック
2. 「Connect」→「New Connection」を選択
3. 表示されたダイアログで、接続URLを `https://` 付きで貼り付け
4. URLはメールやブラウザのアドレスバーから確認可能

#### 代表的な接続URLの形式：

- **Planning Analytics on Cloud：**  
  （環境ごとにURLが異なる）  

```
https://<myserver>.planning-analytics.ibmcloud.com
https://<myserver>.planning-analytics.cloud.ibm.com
```

- **Planning Analytics as a Service (PAaaS)：**  

```
https://<datacenter>.planninganalytics.saas.ibm.com/?accountId=<accountid>&tenantId=<tenantid>
```


オプション：環境ごとにわかりやすい名前を設定可能  
最後に「Test Connection」で接続を確認 → 「Save」で保存

---

## アドインのアップグレード

1. すべての Excel ウィンドウを閉じる
2. `.xll` ファイルをダウンロード
3. ダウンロードフォルダで、汎用名に変更
4. アドインフォルダに上書きコピー
5. Excel を起動し、「PAfEバージョン確認」で検証

---

## アドインの削除

競合または一時無効化したい場合：

1. `.xll` ファイルの場所を確認
2. Excel をすべて閉じる
3. 保存しておいた `.xll` ファイルを削除
4. Excel 起動時に出る警告に「OK」で対応
5. 「開発」→「アドイン」→「ibm_Pafe_X64」のチェックを外す
6. 削除確認に「Yes」
7. Excel を閉じる

---

## PAfE バージョンの確認

1. Excel リボンの「IBM Planning Analytics」をクリック
2. 「Help」→「About」をクリック
3. 表示されるバージョン番号の「第3項目」が対象（例：65）

---

## Excel のビット数確認（32bit/64bit）

**PAfE と Excel のビット数が一致している必要があります。**

1. Excel を起動
2. 左ナビの「アカウント」をクリック
3. 「Excel について」をクリックして確認

---

## アドインファイルの場所を調べる

すべてのセッションに対して有効にしている場合、以下で場所を確認できます：

1. Excel 起動 → 「ファイル」→「オプション」
2. 「アドイン」をクリック
3. 「IBM アドイン」を選択
4. 画面下にアドインのパスが表示される
