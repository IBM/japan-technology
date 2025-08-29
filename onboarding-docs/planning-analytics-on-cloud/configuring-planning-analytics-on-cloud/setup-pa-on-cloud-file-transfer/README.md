# ファイル転送の設定

> 本ガイドは、2024年5月2日に公開された [Setup PA on Cloud file transfer](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/05/02/setup-pa-on-cloud-file-transfer)記事をもとにしています。  
> ただし、Planning Analytics on Cloud 環境では随時更新が行われているため、ファイアウォール設定、FTPeS の構成手順、FTP クライアントの設定画面などが、本資料の記載と一致しない可能性があります。  
> 操作対象の UI や手順に違いが見られる場合は、**IBM の最新ガイドラインや公式ドキュメント**を必ず参照し、最新の情報に基づいてご対応ください。

---

## ファイル転送について

> **ファイアウォール設定**  
> 以下の環境に対して、ポート **21** および **4460〜4500** の送信通信を許可してください（環境は Welcome Kit に記載されています）。  
>  
> **例:**  
> `<non-prod>.planning-analytics.ibmcloud.com`  
>  
> 詳細はこちらをご覧ください:  
> [IBM Docs: Port numbers for Planning Analytics on Cloud](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=cloud-port-numbers-planning-analytics)


Planning Analytics on Cloud とオンプレミス環境（またはその他の自社環境）間でファイルを安全に転送するには、**FTPeS（FTP over explicit TLS/SSL）** を使用します。

転送されるファイルの種類には以下のようなものがあります：

- ディメンションやキューブ用のデータファイル
- 環境間で移動する Planning Analytics データベースファイル（例：PA Local からクラウドへの移行時）

**注記：** エンドユーザーが定期的にファイル転送を行う場合は、**Planning Analytics Workspace（PAW）** から直接操作することも可能です。

---

## 使用する FTP クライアントについて

FTPeS をサポートする FTP クライアントが必要です。  
定期的な転送やスケジューリングが必要な場合は **コマンドラインツール** が使われますが、開発者向けには GUI ベースのクライアントが推奨されます。

一般的に企業で利用可能な GUI クライアントには以下があります：

- **WinSCP**
- **FileZilla**

---

## 設定に必要な情報

ホスト名や認証情報は、**Welcome Kit** に記載されています。

### FileZilla を使った設定例

以下は FileZilla での設定例です。

![FileZilla 接続設定画面](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/KpsPQoGxTyg6YuEEV2gQ_FileZillaConnection-L.png)

**注意：**

- ホスト名には、地域ごとの FTPS/SFTP の URL を指定します（例：ヨーロッパの場合は `ft-EU.planning-analytics.cloud.ibm.com`）。
- 暗号化タイプは **FTP explicit over TLS**（FileZilla では「明示的な FTP over TLS が必要」）を指定してください。

---

## フォルダ構成

接続に成功すると、以下のようなフォルダ構成が表示されます：

- `install`：任意クライアント用のインストールファイル
- `prod`：各データベースごとのフォルダがあり、以下を含みます
  - `logs`：ログファイル
  - `data`：データベースファイル

FileZilla のフォルダビュー例：

![FileZilla フォルダビュー](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/FwrHT25FTPaGkonzGCmB_FileZillaPath-L.png)

---

## 追加のアクセス設定

必要に応じて：

- 追加の FTP ログインのリクエスト
- アクセス制御リスト（ACL）の作成

を行うことができます。

詳細は以下のリンクを参照してください：  
[Controlling access to shared folders（共有フォルダへのアクセス制御）](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=cloud-controlling-access-services-shared-folders)

これにより、ユーザーグループごとのアクセス制限が可能になります。  
例：

- 人事部門には人事用のデータベースフォルダへのアクセスのみ許可
- 財務部門には財務用フォルダのみ許可

また、データベースファイルと分離された「Upload」フォルダの作成など、柔軟な構成が可能です。
