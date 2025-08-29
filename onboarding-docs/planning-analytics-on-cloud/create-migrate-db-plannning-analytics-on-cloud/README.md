# 移行または新規作成（Migrate/Create）

> 本ガイドは、2024年5月9日に公開された [Create and Migrate databases to Planning Analytics on Cloud](https://community.ibm.com/community/user/blogs/yin-chu/2024/05/09/create-migrate-db-plannning-analytics-on-cloud) をもとに作成されています。  
> Planning Analytics on Cloud は定期的に更新されていますので、画面表示、データベース作成手順、FTP 移行プロセス、停止・起動操作などが本資料と異なる場合があります。  
> 実際に操作を進める際には、**IBM の最新ドキュメントや公式ガイドを必ず参照**の上、最新版に沿って対応してください。

---

## データベースの作成

新しいプランニングモデルの構築や、既存データベースからの移行を始めるには、まず「データベースの作成」から始めます。手順は以下を参照してください。

[データベースの作成手順（IBM公式）](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=databases-create-database-cloud-only)

既存のデータベースを移行する予定がある場合は、移行元のデータベースと同じ名前を付けて作成することで、データベースを参照しているオブジェクトの修正を最小限にできます。

たとえば、新しいデータベースを「SmartCo」と名付けると、`\\prod\SmartCo\` 配下に共有フォルダが作成され、そこには以下のような構造のサブフォルダが生成されます：

- Data（データファイル格納用）
- Logs（ログファイル格納用）

![データベースフォルダ構成](https://www.ibm.com/docs/en/SSD29G_2.0.0/com.ibm.swg.ba.cognos.tm1_prism_gs.2.0.0.doc/images/data_structure.jpg)

---

## 新しいデータベース

作成が完了したら、データベース内にコンテンツを構築できます。起動・停止・ログ確認・構成については次のセクションを参照してください。

- データベースの停止と開始
- データベースの構成

---

## 既存データベースからの移行

オンプレミスまたは他のクラウド環境から、データベース全体を移行する手順です。セキュリティ構成は新しい環境で再設定することを前提とします。

### 1. データベースを停止

Planning Analytics Workspace の「管理」>「データベース」から、対象のデータベースを停止し、適用します。

![Stop データベース](https://dw1.s81c.com//IMWUC/MessageImages/080e97bdd0fe4fdba2712df3703af00b.png)

### 2. FTPクライアントで共有フォルダへ接続

Welcome Kit に記載された認証情報で FTP クライアントを用いて共有フォルダにアクセスし、該当データベースの Data フォルダに移動します。

例： `\\prod\smartco\Data`

[FTP接続の詳細手順](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/05/02/setup-pa-on-cloud-file-transfer)

### 3. セキュリティ関連ファイルを除いてファイルを削除

Data フォルダ内のファイルは、下記のセキュリティ情報ファイルを除いてすべて削除可能です。

```
}ClientCAMAssociatedGroups.cub
}CAMAssociatedGroups.dim
}Groups.dim
}Clients.dim
}ClientGroups.cub
```

ただし、こちらも IBMid を使用したクラウド環境から移行する場合は、**すべてのファイルを上書きして問題ありません**。

---

### 4. データベースファイルをコピー（必要に応じて上書き）

FTP を使って、移行元データベースの内容を Data フォルダにコピーします。

通常は、**下記のセキュリティファイルを上書きしないように注意**してください。

```
}ClientCAMAssociatedGroups.cub
}CAMAssociatedGroups.dim
}Groups.dim
}Clients.dim
}ClientGroups.cub
```

### 5. 不要ファイルのクリーンアップ

以下のようなファイルは削除してください：

- ログファイル
- 一時ファイル
- tm1s.cfg
- インポート用 CSV 等のソースファイル

判断に迷う場合は IBM または経験あるビジネスパートナーと相談してください。

### 6. データベースを再起動

PAW 管理画面で対象のデータベースを起動します。

起動確認方法：

- ステータスが Healthy
- ログを表示して確認可能

![Started データベース](https://dw1.s81c.com//IMWUC/MessageImages/129a03e5dd8148a7ab84b8081f82d591.png)

### 7. ユーザーセキュリティの再構成

初期状態では Planning Analytics on Cloud 管理者以外のユーザーは存在しません。初期動作確認が完了したら、セキュリティ設定を行います。

- Workspace グループに移行するか、従来のネイティブグループを継続するかを選択
- 参考リンク：
  - [ロール別セキュリティの管理](https://community.ibm.com/community/user/blogs/paul-hart-prieto/2024/02/26/planning-analytics-on-cloud)
  - [ユーザーとグループの管理](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=workspace-administer-users-groups)

### 8. カスタム設定の更新（必要に応じて）

tm1s.cfg などの構成ファイルを変更した場合は、再起動が必要です（静的パラメータのため）。

---

### データベースの停止と起動

データベースは、既存データベースからの移行時や、静的構成パラメータ（`tm1s.cfg`など）を変更した場合に、**一度停止してから再起動**する必要があります。

操作手順は以下を参照してください。  
[データベースの停止と起動手順（IBM公式）](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=databases-start-stop#task_wkn_mzw_1nb__title__1)

---

### データベースの状態確認（PAW 管理画面）

Planning Analytics Workspace の「管理」>「データベース」画面では、各データベースの状態が「Health（状態）」アイコンで表示されます。

- 停止中（Stopped）：

  ![Stopped](https://dw1.s81c.com//IMWUC/MessageImages/aa37bc52a65a4aec9221ec02327f5f5e.png)

- 起動中（Started / Healthy）：

  ![Started](https://dw1.s81c.com//IMWUC/MessageImages/221ebb0da450487b8c61492648e18ffa.png)

---

### ログによる状態確認

ログファイルからも状態を確認できます。以下のリンクを参照してログを取得してください。

- ログをダウンロードして確認する場合  
  [ログのダウンロード手順](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=databases-download-database-log-files#task_ttz_ptv_1nb__title__1)

- PAW の Workbench で確認する場合  
  [ログ確認（Workbench）](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=workspace-view-planning-analytics-database-log-files)

---

### 起動済みデータベースのログ例

```
2024-04-26 13:46:41 GMT Shared memory reader PID 1832 started, for shmem "tm1s.exe-20164_1"
18108 [] INFO 2024-04-26 13:46:40.891 TM1.Server Data Directory: s:\prod\smartco\data
...
21436 [] INFO 2024-04-26 13:46:43.737 TM1.Server TM1 Server load time (secs) = 1
18108 [] INFO 2024-04-26 13:46:45.513 TM1.Server TM1 Server is ready, elapsed time 5.00 seconds
```

---

### 停止済みデータベースのログ例

```
18844 [] INFO 2024-05-10 16:54:33.424 TM1.Server Closing...
18844 [] INFO 2024-05-10 16:54:33.424 TM1.Server Saving...
18844 [] INFO 2024-05-10 16:54:33.424 TM1.Server The server is coming down...
...
18844 [] INFO 2024-05-10 16:54:33.709 TM1.Server Server shutdown, elapsed time 0.00 seconds
```

---

## データベースの構成

tm1s.cfg で設定されたパラメータを、PAW のデータベース構成画面でも設定できます。

詳細は以下を参照してください。

[パラメータ設定方法（IBM公式）](https://www.ibm.com/docs/en/planning-analytics/2.0.0?topic=databases-set-database-configuration-parameters)

なお、PAW 上で設定できないパラメータは、2024年4月30日以降、変更できなくなっています。

[tm1s.cfg ファイル変更廃止に関する案内](https://community.ibm.com/community/user/blogs/sami-el-cheikh1/2023/12/14/using-planning-analytics-administration-to-modify?CommunityKey=8fde0600-e22b-4178-acf5-bf4eda43146b)
