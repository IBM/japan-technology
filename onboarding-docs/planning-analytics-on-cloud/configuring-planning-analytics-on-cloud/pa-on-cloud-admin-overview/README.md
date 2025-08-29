# Planning Analytics on Cloud 管理概要

> 本ガイドは、2024年5月2日に公開された [PA on Cloud Administration overview](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/05/02/pa-on-cloud-admin-overview)記事をもとにしています。  
> ただし、Planning Analytics on Cloud 環境では随時更新が行われているため、ファイアウォール設定、FTPeS の構成手順、FTP クライアントの設定画面などが、本資料の記載と一致しない可能性があります。  
> 操作対象の UI や手順に違いが見られる場合は、**IBM の最新ガイドラインや公式ドキュメント**を必ず参照し、最新の情報に基づいてご対応ください。

---

## はじめに

管理者は、Planning Analytics のステータスページを購読することを推奨します：  
[https://status.ai-apps-comms.ibm.com/planninganalytics](https://status.ai-apps-comms.ibm.com/planninganalytics)

このページでは、Planning Analytics およびそのコンポーネントの現在のヘルス情報や保守情報を確認できます。  
参考までに、計画されたメンテナンスは**毎月第3土曜日**に実施されます：  
[Maintenance](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=SSD29G_2.0.0/com.ibm.swg.ba.cognos.tm1_cloud_mg.2.0.0.doc/c_tm1_cloud_support_maintenance.htm)

---

## 管理画面へのアクセス

Planning Analytics Workspace（PAW）にログインする必要があります。  
ブラウザで以下にアクセスしてください：
https://www.planning-analytics.ibmcloud.com


アクセス可能な環境が一覧表示されます。

![環境セレクター](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/hlxdWGEsTn6U3QYkB41x_EnvSelector-L.png)

---

## 管理タイルの選択

Planning Analytics のランディングページで **[Administration]** タイルを選択します。

![Adminタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/vsxL2oBuQsuHC9F44krT_AdminTile-M.png)

---

## 管理画面

管理セクションに移動します。

![管理画面](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/1tIVRNLWR3afCZbYvsiw_AdministrationScreen-L.png)

右上には鍵アイコンがあります（※これはサブスクリプション管理者にのみ表示され、ユーザーの招待や Welcome Kit の再生成、Modeler パスワードの再発行が可能です）。

Welcome Kit 再取得:  
[Download a Welcome Kit from Planning Analytics Administration](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=workspace-download-welcome-kit-from-planning-analytics-administration)

---

## 各タイルの概要

### サブスクリプション使用状況

![Subscriptionタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/rTB27mxQyeG3GQCvBCzE_SubscriptionTile-T.jpeg)

現在利用中のサブスクリプション数や、超過（オーバーエンタイトルメント）があるかを確認できます。

---

### データベース管理

![データベースタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/At0eY2YwSgoy1b6Ciwdu_DBTile-T.png)

データベースの追加・削除・名前変更・監視・設定が可能です。  
しきい値アラートを設定することで問題の早期発見が可能となるため、**構成することを推奨**します。

詳細ドキュメント：  
[Monitor and administer databases](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=workspace-monitor-administer-databases)

---

### ユーザーとグループの管理

![Users and Groupsタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/NT1sCazRbqCMHMc8IQtw_UsersandGroupsTile-T.png)

ユーザー、ロール、セキュリティの管理に関する詳細：  
[Administer users and groups](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=workspace-administer-users-groups)

サブスクリプション、ロール、ユーザーセキュリティの管理についてのブログも参照ください：  
[Planning Analytics on Cloud - Subscriptions, Roles and Data security.](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/02/26/planning-analytics-on-cloud)

---

### インテグレーション（統合）

![Integrationsタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/zzxIrzBjQG2u8X2q60UD_IntegrationsTile-T.png)

IBM Cloud Pak for Data の IBM Decision Optimization と統合し、計画データに対する高度な機械学習と最適化を実行可能です。

詳細：  
[Manage integrations](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=workspace-manage-integrations)

---

### ライフサイクル管理

![Lifecycleタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/LDYq7XmOR9CRV0GgLbLd_LifecycleTile-T.png)

開発環境から本番環境への移行など、PA Workspace コンテンツのパッケージングと移行に使用します。

詳細：  
[Copy and deploy assets with Lifecycle Management in Planning Analytics Workspace](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=apaw-copy-deploy-assets-lifecycle-management-in-planning-analytics-workspace)

---

### Excel & カスタマイズ

![Excelタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/FJ99TA8fRWmdgewrhQgW_ExcelTile-T.png)

- Planning Analytics for Excel（PAfE）のダウンロード  
- システム全体のパレット、フォント、テーマの構成

テーマの作成と適用：  
[Create and apply a custom theme for Planning Analytics Workspace](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=SSD29G_2.0.0/com.ibm.swg.ba.cognos.tm1_prism_gs.2.0.0.doc/c_paw_nf_creating_a_custom_theme.htm)

インターフェースのカスタマイズ：  
[Customize the interface for your company](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=workspace-customize-interface-your-company)

---

### 機能と構成

![Featuresタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/VhoaPFnqR1yU5mAvkK37_FeaturesTile-T.png)

- ワークスペース全体の構成パラメータ（例：非アクティブ時間の設定）  
- 機能フラグ（近日強制される機能を事前に有効化）

※データベースごとの設定は、データベース管理セクションで行います。

---

### リモートDBアクセスの構成

![SGタイル](https://higherlogicdownload.s3.amazonaws.com/IMWUC/UploadedImages/7zbbGbZXTSyunaurfLPi_SGTile-T.png)

Planning Analytics からリモートデータベースへアクセスする設定。  
詳細：  
[https://ibm.biz/CS_PAoC_Conf_DBAccess](https://ibm.biz/CS_PAoC_Conf_DBAccess)

---

## その他参考リンク

- Planning Analytics コミュニティに参加：  
  [Planning Analytics コミュニティ](https://community.ibm.com/community/user/communities/community-home?CommunityKey=8fde0600-e22b-4178-acf5-bf4eda43146b)

- Business Analytics ニュースレター購読：  
  [https://imwuc.informz.net/imwuc/pages/Business_Analytics_Newsletter_Subscribe](https://imwuc.informz.net/imwuc/pages/Business_Analytics_Newsletter_Subscribe)

- 製品ロードマップ：  
  [Planning Analytics Roadmap](https://bigblue.aha.io/published/30f7b700d5eb7d18cfdd19c793f4a10d?page=1)

- アイデアポータル：  
  [IBM Data Platform Ideas Portal for Customers](https://ibm-data-and-ai.ideas.ibm.com/)
