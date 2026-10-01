# IBM Bob で学ぶ Backend API ハンズオン（2 時間版）

生命保険契約管理システムの Backend API（Java 21 / Spring Boot）を題材に、IBM Bob と一緒に「配属 1 週目のエンジニア」の仕事を 2 時間で一通り体験するハンズオンです。設計書のないコードから設計文書を復元し、アラート対応・性能改善・新機能開発・フロントエンド実装までを、Bob の Ask / Plan / Agent の 3 つのモードを使い分けながら進めます。

## ダウンロード

このフォルダーにある 2 つのファイルを受講者 PC に保存してください。

| ファイル | 内容 | ダウンロード |
|---|---|---|
| `JavaBackend101-handson-start-20260930.zip` | ハンズオン一式（ソースコード、起動スクリプト、`frontend/node_modules` 同梱、ガイド HTML 入り）。約 25 MB | [ダウンロード](https://github.com/IBM/japan-technology/raw/main/ibm-bob/bob-a-thon/insurance/java-backend/JavaBackend101-handson-start-20260930.zip) |
| `hands-on-guide.html` | ハンズオンガイド（受講者版）。zip の中にも同じものが入っています。事前に読む・印刷する場合はこちら | [ダウンロード](https://github.com/IBM/japan-technology/raw/main/ibm-bob/bob-a-thon/insurance/java-backend/hands-on-guide.html)（リンクを右クリック →「リンク先を保存」） |

> zip の SHA-1: `228eb557b888906a00048663b5c393625040e753`（`shasum JavaBackend101-handson-start-20260930.zip` / `Get-FileHash -Algorithm SHA1` で確認できます）

**展開して開くまで**

1. zip を任意の場所に展開します（パスに日本語や空白を含めないことを推奨）
2. 展開したフォルダーを IBM Bob IDE で開き、`hands-on-guide.html` をブラウザで開きます
3. ガイドの **Part 0** に沿って環境を確認し、`db_start` → `be_start` で起動します

ガイドの HTML は上部のタブで **Mac/Linux（bash）** と **Windows（PowerShell）** を切り替えられます。コマンドはすべて両 OS 分を載せています。

## 学べること

| # | パート | 時間 | Bob のモード | できるようになること |
|---|---|---|---|---|
| 0 | 準備・イントロ | 8 分 | — | 環境を起動し、Bob の 3 つのモードを使い分ける |
| 1 | リバースエンジニアリング | 25 分 | Ask → Agent | 設計書のないコードから API 仕様書・アーキテクチャ概要書・基本設計書・オンボーディングガイドを復元し、生成物をレビューする |
| 2 | 運用: SlowResponseTime アラート対応 | 10 分 | Ask | アラート → メトリクス → ログ → コードの順に原因を絞り込む |
| 3 | 保守 A: 遅延除去とコネクションプール | 12 分 | Agent → Ask | 遅延コードを除き、並列負荷で HikariCP の挙動を Before / After で比べる |
| 4 | 保守 B: N+1 問題の検出と修正 | 18 分 | Ask → Plan → Agent | SQL の「本数」で性能問題を測り、一括取得に直す |
| 5 | 開発: 契約キャンセル API | 20 分 | Plan → Agent | DTO / Flyway / Service / Controller / テスト / E2E を Bob と進める |
| 6 | Vue.js フロントエンド | 22 分 | Ask → Plan → Agent | ログイン → 顧客情報と契約一覧の 1 画面ダッシュボードを実装する |
| 7 | まとめ | 5 分 | — | Bob の使いどころと、人間が確認すべきことを整理する |
| | 合計 | 120 分 | | |

### シナリオ

あなたは今日、生命保険契約管理システムの Backend API チームに配属されました。設計書は残っていません。運用チームからはアラートが上がり、保守案件と新機能の要望が積まれ、フロントエンドは骨組みのまま止まっています。

- **Part 1** では、まず Bob の Ask モードでコードを読み解き、4 つの設計文書を `docs/` に復元します。「コードにないことは『不明』と書く」をプロンプトの基本として、生成物を自分でレビューします
- **Part 2〜3** では、Prometheus の `SlowResponseTime` アラートを起点にメトリクスとログをたどり、トランザクションの中で待っている遅延コードを見つけて除去します。並列負荷をかけて HikariCP の接続枯渇が解消されたことを確かめます
- **Part 4** では、契約一覧 API の N+1 問題を Hibernate 統計の SQL 本数で可視化し（200 本超 → 3 本）、ページサイズ上限とあわせて修正します
- **Part 5** では、契約キャンセル API を設計からマイグレーション・実装・テスト・E2E まで Bob と進めます
- **Part 6** では、配布済みの Vue 3 の骨組みにログイン画面と契約ダッシュボードを実装し、Backend API とつなぎます

### 持ち帰る学び

- Bob の生成物は必ずレビューする。事実（コード）に基づいているかを人間が確かめる
- 調査はアラート → メトリクス → ログ → コードと上流から下流へ
- 性能は体感ではなく **本数**（SQL の本数、コネクションの active / pending）で測り、Before / After で証明する
- Ask は調査とレビュー、Plan は 3 ファイル以上にまたがる変更や選択肢の相談、Agent は計画が固まってから。差分は `git diff` で読む

## 対象者と使用技術

- IT エンジニア（Java 経験の有無は問いません。Spring Boot / REST API / データベースの基礎知識があると理解が早くなります）
- IBM Bob IDE の基本操作（フォルダを開く、チャットに入力する）ができる方

Java 21 / Spring Boot 3.2.5 / PostgreSQL 15 / Flyway / Hibernate / HikariCP / Prometheus + AlertManager + Grafana / Vite + Vue 3 + vue-router / IBM Bob

## 事前準備（受講者 PC）

ハンズオン開始前に次が導入済みであることを確認してください。詳細はガイドの Part 0.1 と付録 A にあります。

| ソフトウェア | 確認コマンド | 期待する結果 |
|---|---|---|
| Java 21 | `java -version` | `openjdk version "21.x.x"` |
| Maven 3.8 以上 | `mvn -version` | `Apache Maven 3.8.x` 以上 |
| Docker Desktop または Rancher Desktop | `docker --version` / `docker info` / `docker compose version` | エラーにならず、`docker compose`（v2 サブコマンド）が使える。Rancher Desktop は Kubernetes を無効にする |
| Node.js 20 LTS 以上 | `node -v` | `v20.x.x` 以上（22 / 24 LTS でも可） |
| git | `git --version` | バージョンが表示される |
| IBM Bob IDE | 起動できる | Ask / Plan / Agent モードのある版 |
| **Mac/Linux のみ** curl と jq | `jq --version` | バージョンが表示される（`brew install jq`） |

- OS: macOS または Windows 10/11（PowerShell 5.1 以上）。Windows は追加ツール不要です
- コンテナ環境: PostgreSQL / Prometheus / AlertManager / Grafana / Backend API はすべて `docker compose` でコンテナとして起動します（起動スクリプト `db_start` / `be_start` が内部で `docker compose up` を実行）。Docker Desktop または Rancher Desktop（Windows は WSL 2 バックエンド）で `docker compose version` が通ることを確認してください
- メモリ: ハンズオン一式（Docker の VM + Bob IDE + Maven + Node）で約 6 GB を使います。16 GB 機を想定しています
- ネットワーク: 初回の Maven ビルドで Maven Central に接続します。`frontend/node_modules` は zip に同梱済みのため `npm install` は不要です（Mac Apple シリコン / Intel、Windows x64）

## 使用するポート

| サービス | ポート |
|---|---|
| Backend API | 52080 |
| PostgreSQL | 52432 |
| Prometheus | 52090 |
| Grafana | 52091（admin / admin） |
| AlertManager | 9093 |
| Frontend（Vite dev） | 5173 |

## 講師の方へ

受講者には上の 2 ファイルを配布してください。zip は `handson-start`（受講者の開始状態）の内容だけを含み、完成状態や講師用資料は入っていません。受講者がやり直すときは、ガイドの Part 0.2 の手順（`git checkout -B work handson-start` → `db_start --reset` → `be_start`）で何度でも開始状態に戻せます。
