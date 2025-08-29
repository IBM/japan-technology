# 構成（Configuration）

> 本ガイドは、2024年5月2日に公開された [Configuring Planning Analytics on Cloud](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/05/02/configuring-planning-analytics-on-cloud) を参照して作成されています。  
> しかし、Planning Analytics on Cloud 環境は随時更新されています。そのため、ユーザーインターフェース、設定プロセス、接続手順などが本ガイドと一致しない可能性があります。  
> 手順や画面表示が異なる場合は、**IBM の最新ドキュメントや公式ガイドラインを必ず参照し、最新の情報に従って対応してください。**

---

## 概要

Planning Analytics on Cloud の構成は、主に**統合**と**接続性**に焦点を当てた複数のステップから構成されます。  
以下のフロー図は、実施すべき主な構成作業を高レベルで示したものです。

![構成フロー全体](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/5PrFTjQpQoeb2RfQp6NJ_new%20PAoC%20conf%20flow.jpeg)

---

## 各ステップの詳細

それぞれの判断ポイントについて、以下のリンクから詳細手順をご確認ください。

---

### 1. IBMサポートのセットアップ

IBM サポートとの連携をセットアップします。

![サポート連携フロー](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/9h0pk0LnS3GvwwWd9dVX_SupportFlow-T.jpeg)

[サポート設定の詳細を見る](./ibm-paoc-support/)

---

### 2. IBMid エンタープライズフェデレーション構成（必要な場合）

フェデレーション（ID連携）が必要な場合は、このステップで構成します。

![フェデレーションフロー](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/c4hvRIKySY24i7bmGCYs_FederateFlow-T.jpeg)

[フェデレーション構成の詳細を見る](./ibmid-federation)

---

### 3. ファイル転送のセットアップ

Planning Analytics on Cloud 環境と外部とのファイル連携に必要な設定を行います。

![ファイル転送フロー](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/B4am4SnSTSZBi7WNZdhA_FileTransferFlow-T.jpeg)

[ファイル転送の設定手順を見る](./setup-pa-on-cloud-file-transfer/)

---

### 4. データベースアクセスの構成（必要な場合）

PA データベースへのアクセス設定を行います。

![データベースアクセスフロー](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/z1Jn8djSSJmCrtiqgj22_ConfDBFlow-T.jpeg)

[データベースアクセス構成の詳細を見る](./configure-paoc-satellite-connector-agent/)

---

### 5. Planning Analytics for Excel（PAfE）の構成（Excel使用時）

Excelから接続するための PAfE 構成を行います。

![PAfE構成フロー](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/Mtq8ZeL2Q8KmSRvJu8yc_ConfPAfEFlow-T.jpeg)

[PAfE 構成の詳細を見る](./pafe-configure/)

---

### 6. その他のコンポーネント構成（必要に応じて）

Workspace 以外の拡張機能やツールなど、追加コンポーネントの設定が必要な場合はこちらを参照してください。

![その他コンポーネントの構成フロー](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/LCMwsSb6QeSRTxHhoAHN_OtherComponentsFlow-T.jpeg)

[その他構成項目の詳細を見る](./paoc-other-components/)

---

### 7. 管理者設定（必須）

環境の管理に関する設定を行います。

![管理者設定フロー](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/Jgei3mmQxS0k8xlgv2ie_AdministrationFlow-T.jpeg)

[管理者設定の詳細を見る](./pa-on-cloud-admin-overview/)

---

## 備考

- 各構成要素は、個別のニーズやセキュリティ要件に応じてスキップ・調整が可能です。
- 手順の正確さを期すため、IBMの[公式ドキュメント](https://www.ibm.com/docs/ja/planning-analytics)を随時確認してください。

