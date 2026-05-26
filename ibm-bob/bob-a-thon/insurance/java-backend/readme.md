# Backend API ハンズオン: IBM Bobで学ぶ運用・保守・開発

## 📋 目次

1. [ハンズオン概要](#ハンズオン概要)
2. [事前準備](#事前準備)
3. [シナリオ1: 運用 - SlowResponseTimeアラート対応](#シナリオ1-運用---slowresponsetimeアラート対応)
4. [シナリオ2: 保守 - パフォーマンス問題の修正](#シナリオ2-保守---パフォーマンス問題の修正)
5. [シナリオ3: 新規機能追加 - 契約キャンセルAPI実装](#シナリオ3-新規機能追加---契約キャンセルapi実装)
6. [まとめ](#まとめ)

---

## ハンズオン概要

### 目的

IBM Bobを活用して、実際のJava Spring Bootアプリケーション（Backend API）で以下を体験します：

1. **運用**: Prometheusアラート対応とパフォーマンス調査
2. **保守**: コードリファクタリングとパフォーマンス改善
3. **新規機能追加**: RESTful APIエンドポイントの実装

### 対象者

- ITエンジニア（Java経験者・未経験者混在OK）
- Spring Boot、REST API、データベースの基礎知識があると理想的
- IBM Bobの基本操作を理解している方

### 所要時間

- **合計**: 30分
  - 事前準備: 5分
  - シナリオ1（運用）: 8分
  - シナリオ2（保守）: 8分
  - シナリオ3（新規機能）: 8分
  - まとめ: 1分

### 使用技術

- **言語**: Java 21
- **フレームワーク**: Spring Boot 3.2.5
- **データベース**: PostgreSQL 15
- **監視**: Prometheus + Actuator
- **ビルドツール**: Maven
- **AI支援**: IBM Bob

---

## 事前準備

### 必要な環境

#### ソフトウェア要件

- **Java 21** (OpenJDK推奨)
- **Docker Desktop** または **Rancher Desktop**
- **Maven 3.8+**
- **AI支援**: IBM Bob IDE
- **Git**
- **curl** または **Postman**（API動作確認用）

#### 環境確認コマンド

**Mac/Linux:**
```bash
# Java確認
java -version
# 期待: openjdk version "21.x.x"

# Maven確認
mvn -version
# 期待: Apache Maven 3.8.x以上

# Docker確認
docker --version
# 期待: Docker version 20.x以上
```

**Windows (PowerShell):**
```powershell
# Java確認
java -version
# 期待: openjdk version "21.x.x"

# Maven確認
mvn -version
# 期待: Apache Maven 3.8.x以上

# Docker確認
docker --version
# 期待: Docker version 20.x以上
```

### 環境確認

#### 1. Java 21環境の確認

IBM Bobを使ってJava 21が正しくインストールされているか確認します。

**Bobプロンプト:**
```
このMacにJava 21のランタイムとSDKが入っていることを確認して。
以下のコマンドを実行して結果を教えてください：
- java -version
- javac -version

期待する結果：
- Java version: 21.x.x
- Javac version: 21.x.x
```

**期待される出力例:**
```
openjdk version "21.0.10" 2026-01-20
OpenJDK Runtime Environment (build 21.0.10)
OpenJDK 64-Bit Server VM (build 21.0.10, mixed mode)

javac 21.0.10
```

もしJava 21がインストールされていない場合は、講師に確認してください。

### プロジェクトの起動

#### 1. 作業ディレクトリの確認

ソースコードが展開されたディレクトリに移動します。

**Mac/Linux:**
```bash
cd /path/to/JavaModern101
ls -la
```

**Windows (PowerShell):**
```powershell
cd C:\path\to\JavaModern101
Get-ChildItem
```

#### 2. データベース起動

**Mac/Linux:**
```bash
# データベース起動スクリプトを実行
./db_start.sh
```

**Windows (PowerShell):**
```powershell
# データベース起動スクリプトを実行
.\db_start.ps1
```

このスクリプトは以下を自動実行します：
- Docker Desktopの起動確認
- PostgreSQL, Prometheus, AlertManagerのコンテナ起動
- サービスの起動確認（最大30秒待機）
- 起動状態の表示

#### 3. Backend API起動

**Mac/Linux:**
```bash
# Backend API起動スクリプトを実行
./be_start.sh
```

**Windows (PowerShell):**
```powershell
# Backend API起動スクリプトを実行
.\be_start.ps1
```

このスクリプトは以下を自動実行します：
- Docker起動確認
- PostgreSQL起動確認（未起動の場合は自動起動）
- 既存プロセスの停止（ポート52080使用中の場合）
- Backend APIのビルド（`mvn clean package -DskipTests`）
- Backend APIの起動
- ヘルスチェックで起動確認（最大30秒待機）
- 起動成功メッセージとURL表示

#### 4. Grafana起動（オプション）

Prometheusは `db_start.sh` / `db_start.ps1` で既に起動済みです。
Grafanaを使用する場合は以下を実行：

**Mac/Linux:**
```bash
# Grafana起動
docker compose up -d grafana

# Grafanaダッシュボード確認
open http://localhost:52091
# 初回ログイン: admin/admin（パスワード変更を求められます）
```

**Windows (PowerShell):**
```powershell
# Grafana起動
docker compose up -d grafana

# Grafanaダッシュボード確認
Start-Process http://localhost:52091
# 初回ログイン: admin/admin（パスワード変更を求められます）
```

### IBM Bob IDE設定

1. IBM Bob IDEで `JavaModern101` フォルダを開く
2. Bob機能が有効になっていることを確認
3. Bobチャットを開く

---

## シナリオ1: 運用 - SlowResponseTimeアラート対応

### 🎯 学習目標

- Prometheusアラートの確認方法を理解する
- Bobを使ってログ分析とパフォーマンス調査を行う
- メトリクスからボトルネックを特定する

### 📖 シナリオ背景

**状況**: Prometheusから `SlowResponseTime` アラートが発生しました。

### ⚠️ 事前準備: アラート発火用の負荷生成

SlowResponseTimeアラートを発火させるため、遅延が発生するエンドポイントに**1分間継続的にリクエスト**を送ります。

> **注意**: この手順は講師が事前に実行するか、ハンズオン開始時に受講者全員で実行してください。

#### 負荷生成スクリプト実行

> **重要**: 遅延が発生する顧客契約一覧API (`GET /api/customers/1/policies`) を呼び出します。
>
> **アラートを維持するため、継続的な負荷生成スクリプトを使用します。**

**Mac/Linux:**
```bash
# 新しいターミナルを開いて実行
./continuous_load.sh
```

**Windows (PowerShell):**
```powershell
# 新しいPowerShellウィンドウを開いて実行
.\continuous_load.ps1
```

このスクリプトは以下を自動実行します：
- Backend API起動確認
- 15秒ごとに10回リクエスト送信（無限ループ）
- テストユーザーでログイン（yamada@example.com / Password1）
- 各リクエストのレスポンスタイム表示
- サイクル番号表示
- **Ctrl+Cで停止**

> **💡 ヒント**: このスクリプトは無限ループで実行されるため、アラートが継続的に維持されます。調査が終わるまで実行し続けてください。

#### アラート発火確認（1分後）

負荷生成開始から**約1分後**、Prometheusでアラートが発火していることを確認します：

> **重要**: 新しいターミナルを開いて以下のコマンドを実行してください。

**Mac/Linux:**
```bash
# 新しいターミナルを開いて実行
# アラート状態確認
curl -s http://localhost:52090/api/v1/alerts | jq '.data.alerts[] | select(.labels.alertname=="SlowResponseTime") | {state: .state, value: .value}'
```

**Windows (PowerShell):**
```powershell
# 新しいPowerShellウィンドウを開いて実行
# アラート状態確認
$response = Invoke-WebRequest -Uri http://localhost:52090/api/v1/alerts
$alerts = ($response.Content | ConvertFrom-Json).data.alerts
$alerts | Where-Object { $_.labels.alertname -eq "SlowResponseTime" } | Select-Object state, value
```

**期待される出力:**
```json
{
  "state": "firing",
  "value": "3.5"
}
```

> **💡 ヒント**: `state: "pending"` の場合は、まだ30秒経過していません。`state: "firing"` になるまで待ちましょう（最大1分）。

---

### 🚨 シナリオ開始

```
Alert: SlowResponseTime
Severity: warning
Service: backend-api
Description: P95レスポンスタイムが3秒を超えています
```

あなたは運用担当者として、この問題を調査し、原因を特定する必要があります。

### 🔍 ステップ1: アラート内容の確認（1分）

#### Prometheusでアラート確認

**Mac/Linux:**
```bash
# 発火中のアラート確認
curl -s http://localhost:52090/api/v1/alerts | jq '.data.alerts[] | select(.labels.alertname=="SlowResponseTime")'
```

**Windows (PowerShell):**
```powershell
# 発火中のアラート確認
$response = Invoke-WebRequest -Uri http://localhost:52090/api/v1/alerts
$response.Content | ConvertFrom-Json | Select-Object -ExpandProperty data | Select-Object -ExpandProperty alerts | Where-Object { $_.labels.alertname -eq "SlowResponseTime" }
```

#### Bobに質問

Bobチャットで以下を入力：

```
/ask monitoring/prometheus-alerts.yml を確認して、SlowResponseTimeアラートの詳細を教えてください。
どのような条件で発火しますか？
```

**期待される回答のポイント**:
- APIエンドポイント (`/api/*`) の平均レスポンスタイムが3秒以上で30秒間継続
- 警告レベル（warning）
- エンドポイント別に監視（`uri` ラベルで識別）
- 実際の値: 約3.52秒（`/api/customers/{customerId}/policies`）

### 🔍 ステップ2: メトリクス確認（2分）

#### Actuatorでメトリクス取得

**Mac/Linux:**
```bash
# HTTPリクエストメトリクス確認
curl -s http://localhost:52080/actuator/metrics/http.server.requests | jq '.'

# 特定エンドポイントのレスポンスタイム（契約一覧API）
curl -s 'http://localhost:52080/actuator/metrics/http.server.requests?tag=uri:/api/customers/%7BcustomerId%7D/policies' | jq '.measurements'
```

**Windows (PowerShell):**
```powershell
# HTTPリクエストメトリクス確認
$response = Invoke-WebRequest -Uri http://localhost:52080/actuator/metrics/http.server.requests
$response.Content | ConvertFrom-Json

# 特定エンドポイントのレスポンスタイム（契約一覧API）
$response = Invoke-WebRequest -Uri "http://localhost:52080/actuator/metrics/http.server.requests?tag=uri:/api/customers/%7BcustomerId%7D/policies"
($response.Content | ConvertFrom-Json).measurements
```

#### Bobでメトリクス分析

Bobチャットで以下を入力：

```
backend-api/src/main/resources/application.yml のActuator設定を確認して、
どのようなメトリクスが公開されているか教えてください。
また、パフォーマンス問題を調査するために有効なメトリクスは何ですか？
```

### 🔍 ステップ3: ログ分析（3分）

#### ログファイル確認

**Mac/Linux:**
```bash
# 最新のログを確認
tail -50 backend-api/logs/backend-api.log

# レスポンスタイムが3秒以上のリクエストを抽出
grep "Request completed" backend-api/logs/backend-api.log | \
  jq -r 'select(.message | contains("duration")) | select((.message | capture("duration=(?<dur>[0-9]+)ms").dur | tonumber) > 3000) | [."@timestamp", (.message | capture("uri=(?<uri>[^,]+)").uri), (.message | capture("duration=(?<dur>[0-9]+)ms").dur)] | @tsv'
```

**Windows (PowerShell):**
```powershell
# 最新のログを確認
Get-Content backend-api/logs/backend-api.log -Tail 50

# レスポンスタイムが3秒以上のリクエストを抽出
Get-Content backend-api/logs/backend-api.log |
  Where-Object { $_ -match "Request completed" } |
  ConvertFrom-Json |
  Where-Object { $_.message -match "duration=(\d+)ms" -and [int]$Matches[1] -gt 3000 } |
  ForEach-Object {
    $_.message -match "uri=([^,]+)" | Out-Null
    $uri = $Matches[1]
    $_.message -match "duration=(\d+)ms" | Out-Null
    $duration = $Matches[1]
    [PSCustomObject]@{
      Timestamp = $_.'@timestamp'
      Uri = $uri
      Duration = $duration
    }
  }
```

#### Bobでログ分析

Bobチャットで以下を入力：

```
/ask backend-api/logs/backend-api.log を分析して、
レスポンスタイムが遅いエンドポイントを特定してください。
特に3秒以上かかっているリクエストに注目してください。
```

### 🔍 ステップ4: 原因特定（2分）

#### Bobで原因調査

Bobチャットで以下を入力：

```
/ask backend-api/src/main/java/com/insurance/service/PolicyService.java を確認して、
パフォーマンス問題の原因となりそうなコードを特定してください。
特にデータベースクエリに注目してください。
```

**期待される発見**:
- `getPoliciesByCustomerId` メソッドでN+1問題の可能性
- ページネーション処理でのデータ取得量
- インデックスの有無

### 📝 シナリオ1のまとめ

**学んだこと**:
- ✅ Prometheusアラートの確認方法
- ✅ Actuatorメトリクスの読み方
- ✅ JSON形式ログの分析手法
- ✅ Bobを使った効率的な調査方法

**次のステップ**: シナリオ2で特定した問題を修正します。

---

## シナリオ2: 保守 - パフォーマンス問題の修正

### 🎯 学習目標

- Bobを使って問題コードを修正する
- Before/Afterの定量的な比較を行う
- Grafanaでパフォーマンス改善を可視化する

### 📖 シナリオ背景

シナリオ1で特定したパフォーマンス問題の原因は、`PolicyService.java` に追加した意図的な遅延コード（`Thread.sleep(3500)`）でした。
この遅延コードをコメントアウトして、パフォーマンスを改善します。

### 🔧 ステップ1: 問題コードの確認（1分）

#### 現在のコード確認

IBM Bob IDEで `backend-api/src/main/java/com/insurance/service/PolicyService.java` を開き、`getPoliciesByCustomerId` メソッドを確認します。

シナリオ1で特定した通り、以下の遅延コードが含まれています：

```java
// 意図的な遅延（ハンズオン用）
Thread.sleep(3500);
```

### 🔧 ステップ2: コード修正（2分）

#### Bobでコード修正

Bobチャットで以下を入力：

```
/code backend-api/src/main/java/com/insurance/service/PolicyService.java の
getPoliciesByCustomerId メソッドを修正してください：

意図的な遅延コード（Thread.sleep(3500)）をコメントアウトしてください。
既存の動作を維持し、コンパイルエラーが出ないように注意してください。
```

#### 生成されたコードの確認

Bobが生成したコードを確認し、以下をチェック：
- [ ] `Thread.sleep(3500)` がコメントアウトされている
- [ ] 既存のロジックが維持されている
- [ ] コンパイルエラーがない

### 🔧 ステップ3: 修正適用と負荷生成（2分）

#### 修正適用

Bobが生成したコードを適用します（IBM Bob IDEで自動適用されます）。

#### 継続的な負荷生成の開始

修正後のパフォーマンスを測定するため、継続的な負荷生成を開始します。

**Mac/Linux:**
```bash
# 新しいターミナルを開いて実行
./continuous_load.sh
```

**Windows (PowerShell):**
```powershell
# 新しいPowerShellウィンドウを開いて実行
.\continuous_load.ps1
```

このスクリプトは以下を自動実行します：
- Backend API起動確認（未起動の場合はエラー表示）
- Backend APIの自動再起動（ビルド含む）
- 15秒ごとに10回リクエスト送信
- 各リクエストのレスポンスタイム表示

修正後は、各リクエストが0.5秒以下で完了することを確認できます。

> **💡 ヒント**: このスクリプトは無限ループで実行されます。次のステップでメトリクスを確認した後、Ctrl+Cで停止してください。

#### 個別のレスポンスタイム測定（オプション）

continuous_load.sh/ps1とは別に、個別にレスポンスタイムを測定したい場合は、**新しいターミナル/PowerShellウィンドウを開いて**以下のコマンドを実行してください。

**Mac/Linux:**
```bash
# 新しいターミナルを開いて実行
# JWTトークン取得
TOKEN=$(curl -s -X POST http://localhost:52080/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"yamada@example.com","password":"Password1"}' | jq -r '.token')

# レスポンスタイム計測（修正後）
time curl -s -H "Authorization: Bearer $TOKEN" \
  "http://localhost:52080/api/customers/1/policies" | jq '.policies | length'

# 期待結果: real 0m0.020s 前後（99%改善！）
```

**Windows (PowerShell):**
```powershell
# JWTトークン取得
$response = Invoke-WebRequest -Uri "http://localhost:52080/api/auth/login" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"email":"yamada@example.com","password":"Password1"}'
$token = ($response.Content | ConvertFrom-Json).token

# レスポンスタイム計測（修正後）
Measure-Command {
  $headers = @{ Authorization = "Bearer $token" }
  Invoke-WebRequest -Uri "http://localhost:52080/api/customers/1/policies" -Headers $headers
} | Select-Object TotalMilliseconds

# 期待結果: 20ミリ秒前後（99%改善！）
```

### 🔧 ステップ4: Grafanaで可視化確認（3分）

#### Grafana起動確認

まず、Grafanaが起動しているか確認します。

**Mac/Linux:**
```bash
# Grafanaコンテナの状態確認
docker ps | grep grafana

# 起動していない場合は起動
docker compose up -d grafana
```

**Windows (PowerShell):**
```powershell
# Grafanaコンテナの状態確認
docker ps | Select-String grafana

# 起動していない場合は起動
docker compose up -d grafana
```

Grafanaが起動するまで約10秒待機してから、次に進みます。

#### Grafanaダッシュボードを開く

**Mac/Linux:**
```bash
open http://localhost:52091
```

**Windows (PowerShell):**
```powershell
Start-Process http://localhost:52091
```

> **💡 初回アクセス時**: ログイン画面が表示された場合、ユーザー名: `admin`、パスワード: `admin` でログインしてください。パスワード変更を求められた場合はスキップできます。

#### ダッシュボードで確認する項目

**Mac/Linux:**
```bash
open http://localhost:52091
```

**Windows (PowerShell):**
```powershell
Start-Process http://localhost:52091
```

1. **レスポンスタイムグラフ（平均）**:
   - 左メニュー → Explore
   - データソース: Prometheus
   - クエリ入力:
   ```promql
   rate(http_server_requests_seconds_sum{uri="/api/customers/{customerId}/policies"}[1m])
   /
   rate(http_server_requests_seconds_count{uri="/api/customers/{customerId}/policies"}[1m])
   ```
   - Before: 3.5秒以上 → After: 0.5秒以下

2. **レスポンスタイムグラフ（最大値）**:
   ```promql
   http_server_requests_seconds_max{uri="/api/customers/{customerId}/policies"}
   ```

3. **リクエスト数グラフ**:
   ```promql
   rate(http_server_requests_seconds_count{uri="/api/customers/{customerId}/policies"}[1m])
   ```

4. **エラー率グラフ（参考）**:
   ```promql
   rate(http_server_requests_seconds_count{uri="/api/customers/{customerId}/policies",status=~"5.."}[1m])
   /
   rate(http_server_requests_seconds_count{uri="/api/customers/{customerId}/policies"}[1m])
   ```
   - **注**: エラーが発生していない場合は「No data」と表示されます（正常な状態）

5. **アラート状態確認**:
   - 左メニュー → Alerting → Alert rules
   - SlowResponseTimeアラートが解消されていることを確認

> **💡 ヒント**: continuous_load.sh/ps1を実行中の場合は、Ctrl+Cで停止してください。

#### 改善結果の比較表

| 指標 | Before（遅延あり） | After（修正後） | 改善率 |
|------|------------------|----------------|--------|
| レスポンスタイム（平均） | 3.5秒 | 0.25秒 | **93%改善** |
| P95レスポンスタイム | 3.8秒 | 0.5秒 | **87%改善** |
| Prometheusアラート | 🔴 発火中 | ✅ 正常 | 解決 |
| ユーザー体験 | ⚠️ 遅い | ✅ 快適 | 大幅改善 |

### 🔧 ステップ5: テスト実行（1分）

#### 単体テスト実行

修正が既存の機能を壊していないことを確認するため、単体テストを実行します。

**Mac/Linux:**
```bash
./be_test.sh
```

**Windows (PowerShell):**
```powershell
.\be_test.ps1
```

このスクリプトは以下を自動実行します：
- backend-apiディレクトリに移動
- PolicyServiceTestを実行
- テスト結果を表示

**期待される結果**:
```
✅ テスト成功
```

すべてのテストがパスすれば、修正が正しく適用され、既存の機能が維持されていることが確認できます。

### 📝 シナリオ2のまとめ

**学んだこと**:
- ✅ 問題コードの特定と修正
- ✅ Bobを使った効率的なコード修正
- ✅ Grafanaでの可視化による改善確認
- ✅ Before/Afterの定量的な比較

**改善結果**:
- レスポンスタイム: 3.5秒 → 0.25秒（**93%改善**）
- P95レスポンスタイム: 3.8秒 → 0.5秒（**87%改善**）
- Prometheusアラート: 解消
- ユーザー体験: 大幅改善

---

### 📚 参考: N+1問題について

**N+1問題とは**:
データベースから親レコードをN件取得した後、各親レコードに対して子レコードを取得するクエリを実行することで、合計N+1回のクエリが発生する問題です。

**例**:
```java
// N+1問題が発生するコード例
List<Policy> policies = policyRepository.findByCustomerId(customerId); // 1回目のクエリ
for (Policy policy : policies) {
    policy.getPremiums().size(); // 各Policyに対してクエリ実行（N回）
}
```

**解決方法**:
1. **Fetch Join**: JPQLで `JOIN FETCH` を使用
   ```java
   @Query("SELECT p FROM Policy p LEFT JOIN FETCH p.premiums WHERE p.customerId = :customerId")
   List<Policy> findByCustomerIdWithPremiums(@Param("customerId") Long customerId);
   ```

2. **@EntityGraph**: エンティティに `@EntityGraph` アノテーションを使用
   ```java
   @EntityGraph(attributePaths = {"premiums"})
   List<Policy> findByCustomerId(Long customerId);
   ```

**注意**: 今回のハンズオンでは、意図的な遅延コードの削除のみを行いました。実際の開発現場では、N+1問題の修正も重要なパフォーマンス改善手法です。

---

## シナリオ3: 新規機能追加 - 契約キャンセルAPI実装

### 🎯 学習目標

- RESTful APIエンドポイントの設計を理解する
- Bobを使って新機能を実装する
- テストファーストでの開発を体験する

### 📖 シナリオ背景

**要件**: 顧客が契約をキャンセルできる新しいAPIエンドポイントを追加します。

**ビジネスルール**:
1. アクティブな契約のみキャンセル可能
2. キャンセル時に契約ステータスを `CANCELLED` に変更
3. キャンセル日時を記録
4. 監査ログに記録

### 🚀 ステップ1: API設計（2分）

#### Bobで設計相談

Bobチャットで以下を入力：

```
/plan 契約キャンセルAPIを実装したいです。以下の要件を満たすRESTful APIを設計してください：

要件:
- エンドポイント: POST /api/policies/{id}/cancel
- リクエストボディ: { "reason": "キャンセル理由" }
- レスポンス: 更新された契約情報
- エラーハンドリング: 契約が見つからない、既にキャンセル済み、など

既存のコード構造（Controller、Service、Repository）に従ってください。
```

**期待される設計**:
1. `PolicyController` に新しいエンドポイント追加
2. `PolicyService` にビジネスロジック実装
3. `Policy` エンティティに `cancelledAt` フィールド追加（必要に応じて）
4. バリデーションとエラーハンドリング
5. 単体テスト作成

### 🚀 ステップ2: DTOとエンティティ拡張（2分）

#### Bobでコード生成

Bobチャットで以下を入力：

```
/code 以下のファイルを作成してください：

backend-api/src/main/java/com/insurance/dto/CancelPolicyRequest.java
   - reason フィールド（必須、最大500文字）
   - バリデーションアノテーション付き
```

#### 生成されたコードの確認

- [ ] `CancelPolicyRequest` に `@NotBlank` などのバリデーションがある
- [ ] Lombokアノテーションが適切に使用されている

### 🚀 ステップ2.5: データベースマイグレーション作成（2分）

> **重要**: `ddl-auto: validate` 設定のため、エンティティ変更時は**必ず**Flywayマイグレーションが必要です。

#### Flywayマイグレーション作成

Bobチャットで以下を入力：

```
/code backend-api/src/main/resources/db/migration/V12__add_policy_cancellation_fields.sql を作成してください：

ALTER TABLE policy ADD COLUMN cancelled_at TIMESTAMP;
ALTER TABLE policy ADD COLUMN cancelled_reason VARCHAR(500);
```

#### Policyエンティティ更新

Bobチャットで以下を入力：

```
/code backend-api/src/main/java/com/insurance/entity/Policy.java を修正してください：

以下のフィールドを追加：
- cancelledAt フィールド（LocalDateTime型、nullable、カラム名: cancelled_at）
- cancelledReason フィールド（String型、nullable、最大500文字、カラム名: cancelled_reason）

既存のフィールドとアノテーションの形式に従ってください。
```

#### 生成されたコードの確認

- [ ] マイグレーションSQLが作成されている
- [ ] `Policy` エンティティに新しいフィールドが追加されている
- [ ] `@Column` アノテーションでカラム名が正しく指定されている

#### Backend API再起動

マイグレーションを適用するため、Backend APIを再起動します：

**Mac/Linux:**
```bash
./be_start.sh
```

**Windows (PowerShell):**
```powershell
.\be_start.ps1
```

起動ログで以下を確認：
```
Flyway: Successfully applied 1 migration to schema "public", now at version v12
```

### 🚀 ステップ3: ステータス管理の確認（1分）

#### 契約ステータスの確認

Bobチャットで以下を入力：

```
/ask backend-api/src/main/java/com/insurance/entity/Policy.java のstatusフィールドを確認してください。
どのような値が使用されていますか？ CANCELLEDステータスは既存のデータで使用されていますか？
```

> **注**: `status`フィールドはString型で、enumではありません。"ACTIVE", "EXPIRED", "CANCELLED"などの文字列値を使用します。

### 🚀 ステップ3.5: GlobalExceptionHandler拡張（1分）

> **重要**: ビジネスルール違反（既にキャンセル済み等）を適切なHTTPステータスで返すため、`IllegalStateException`のハンドラーを追加します。

#### IllegalStateExceptionハンドラー追加

Bobチャットで以下を入力：

```
/code backend-api/src/main/java/com/insurance/exception/GlobalExceptionHandler.java に
IllegalStateExceptionのハンドラーを追加してください：

要件:
- HTTPステータス: 400 Bad Request
- エラーメッセージ: 例外メッセージをそのまま返す
- ログレベル: WARN
- 既存のハンドラー（IllegalArgumentExceptionなど）と同じ形式で実装
- @ExceptionHandlerアノテーション使用

メソッド名: handleIllegalStateException
```

#### 生成されたコードの確認

- [ ] `@ExceptionHandler(IllegalStateException.class)`アノテーションがある
- [ ] HTTPステータスが400 Bad Requestになっている
- [ ] ログ出力がある
- [ ] ErrorResponseを返している

#### 動作確認（オプション）

Backend APIを再起動して、エラーハンドリングが正しく動作することを確認：

**Mac/Linux:**
```bash
./be_start.sh
```

**Windows (PowerShell):**
```powershell
.\be_start.ps1
```

### 🚀 ステップ4: ビジネスロジック実装（2分）

#### Bobでサービス層実装

Bobチャットで以下を入力：

```
/code backend-api/src/main/java/com/insurance/service/PolicyService.java に
cancelPolicy メソッドを追加してください：

要件:
1. 契約IDで契約を取得（存在しない場合はResourceNotFoundException）
2. ステータスが "ACTIVE" でない場合はIllegalStateException（HTTPステータス400）
3. ステータスを "CANCELLED" に変更
4. cancelledAt に現在日時を設定
5. cancelledReason を設定
6. 保存して返却

@Transactional アノテーションを忘れずに。

エラーハンドリング:
- ResourceNotFoundException → 404 Not Found
- IllegalStateException → 400 Bad Request（GlobalExceptionHandlerで処理）
```

#### Bobでコントローラー実装

Bobチャットで以下を入力：

```
/code backend-api/src/main/java/com/insurance/controller/PolicyController.java に
契約キャンセルエンドポイントを追加してください：

- パス: POST /api/policies/{id}/cancel
- リクエストボディ: CancelPolicyRequest
- レスポンス: PolicyDetailResponse
- HTTPステータス: 200 OK
- @Timed アノテーションでメトリクス収集
```

### 🚀 ステップ5: テスト作成と実行（2分）

#### Bobでテスト生成

Bobチャットで以下を入力：

```
/code backend-api/src/test/java/com/insurance/service/PolicyServiceTest.java に
cancelPolicy メソッドのテストケースを追加してください：

テストケース:
1. 正常系: アクティブな契約をキャンセル
2. 異常系: 存在しない契約ID
3. 異常系: 既にキャンセル済みの契約
4. 異常系: アクティブでない契約（EXPIRED等）
```

#### テスト実行

**Mac/Linux:**
```bash
cd backend-api
mvn test -Dtest=PolicyServiceTest#testCancelPolicy
```

**Windows (PowerShell):**
```powershell
cd backend-api
mvn test -D"test=PolicyServiceTest#testCancelPolicy"
```

#### 動作確認

> **注**: 既存のテストデータ（policyId=1）は既にキャンセル済みの可能性があります。
> 確実に動作確認するため、アクティブな契約を確認してから実行してください。

**Mac/Linux:**
```bash
# JWTトークン取得
source get_token.sh

# アクティブな契約を検索
ACTIVE_POLICY=$(curl -s "http://localhost:52080/api/customers/1/policies" \
  -H "Authorization: Bearer $TOKEN" | \
  jq -r '.content[] | select(.status=="ACTIVE") | .id' | head -1)

echo "アクティブな契約ID: $ACTIVE_POLICY"

# 契約キャンセルAPI呼び出し
if [ -n "$ACTIVE_POLICY" ]; then
  curl -X POST "http://localhost:52080/api/policies/$ACTIVE_POLICY/cancel" \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $TOKEN" \
    -d '{"reason":"顧客都合によるキャンセル"}' | jq '.'
  
  # キャンセル後の契約確認
  curl -s "http://localhost:52080/api/policies/$ACTIVE_POLICY" \
    -H "Authorization: Bearer $TOKEN" | jq '.status'
else
  echo "アクティブな契約が見つかりません"
fi
```

**Windows (PowerShell):**
```powershell
# JWTトークン取得
. .\get_token.ps1

# アクティブな契約を検索
$response = Invoke-WebRequest -Uri "http://localhost:52080/api/customers/1/policies" `
  -Headers @{"Authorization" = "Bearer $env:TOKEN"}
$policies = ($response.Content | ConvertFrom-Json).content
$ACTIVE_POLICY = ($policies | Where-Object { $_.status -eq "ACTIVE" } | Select-Object -First 1).id

Write-Host "アクティブな契約ID: $ACTIVE_POLICY"

# 契約キャンセルAPI呼び出し
if ($ACTIVE_POLICY) {
  $body = @{
      reason = "顧客都合によるキャンセル"
  } | ConvertTo-Json
  
  $headers = @{
      "Content-Type" = "application/json"
      "Authorization" = "Bearer $env:TOKEN"
  }
  
  $response = Invoke-WebRequest -Uri "http://localhost:52080/api/policies/$ACTIVE_POLICY/cancel" `
    -Method POST -Body $body -Headers $headers
  $response.Content | ConvertFrom-Json
  
  # キャンセル後の契約確認
  $response = Invoke-WebRequest -Uri "http://localhost:52080/api/policies/$ACTIVE_POLICY" `
    -Headers @{"Authorization" = "Bearer $env:TOKEN"}
  ($response.Content | ConvertFrom-Json).status
} else {
  Write-Host "アクティブな契約が見つかりません"
}
```

#### エラーケースの確認

**既にキャンセル済みの契約を再度キャンセル:**
```bash
# 同じ契約IDで再度キャンセル実行
curl -X POST "http://localhost:52080/api/policies/$ACTIVE_POLICY/cancel" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"reason":"再キャンセル"}' | jq '.'

# 期待結果: 400 Bad Request
# {"error": "Contract is not in ACTIVE status"}
```

**存在しない契約ID:**
```bash
curl -X POST "http://localhost:52080/api/policies/99999/cancel" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"reason":"テスト"}' | jq '.'

# 期待結果: 404 Not Found
# {"error": "Policy not found with id: 99999"}
```

### 📝 シナリオ3のまとめ

**学んだこと**:
- ✅ RESTful API設計の基本
- ✅ Bobを使った効率的な新機能実装
- ✅ データベースマイグレーションの重要性
- ✅ エラーハンドリングの適切な実装
- ✅ テストファーストでの開発手法
- ✅ エンドツーエンドでの動作確認

**実装した機能**:
- 契約キャンセルAPI（POST /api/policies/{id}/cancel）
- Flywayマイグレーション（V12__add_policy_cancellation_fields.sql）
- GlobalExceptionHandlerの拡張（IllegalStateException対応）
- ビジネスルールに基づくバリデーション
- 包括的な単体テスト

**技術的なポイント**:
- `ddl-auto: validate`環境でのマイグレーション必須
- ビジネスルール違反は400 Bad Request（IllegalStateException）
- リソース不在は404 Not Found（ResourceNotFoundException）
- 動的なテストデータ検索で再現性確保

---

## まとめ

### 🎓 ハンズオンで学んだこと

#### 1. 運用スキル
- Prometheusアラートの確認と対応
- Actuatorメトリクスの活用
- JSON形式ログの分析手法
- パフォーマンス問題の調査方法

#### 2. 保守スキル
- N+1問題の特定と修正
- JPA Fetch Joinの実装
- コードリファクタリングのベストプラクティス
- テスト駆動での修正検証

#### 3. 開発スキル
- RESTful API設計
- Spring Bootでの新機能実装
- DTOとエンティティの設計
- 包括的なテストの作成

### 🤖 IBM Bobの活用ポイント

#### 効果的な使い方
1. **コンテキストを明確に**: ファイルパスや要件を具体的に指定
2. **段階的に進める**: 設計 → 実装 → テストの順で依頼
3. **既存コードを尊重**: 「既存のコード構造に従って」と指示
4. **検証を忘れない**: 生成されたコードを必ず確認・テスト

#### Bobが得意なこと
- ✅ コード分析と問題特定
- ✅ ボイラープレートコードの生成
- ✅ テストケースの作成
- ✅ リファクタリング提案
- ✅ ドキュメント参照と説明

#### 人間が確認すべきこと
- ⚠️ ビジネスロジックの正確性
- ⚠️ セキュリティ要件の充足
- ⚠️ パフォーマンスへの影響
- ⚠️ エッジケースの処理

### 📚 参考資料

#### プロジェクト内ドキュメント
- [API仕様書](docs/api-specification.md)
- [運用監視ガイド](docs/operations-monitoring-guide.md)
- [アーキテクチャ概要](docs/architecture-overview.md)
- [データベーススキーマ](docs/database-schema.md)

#### 外部リソース
- [Spring Boot公式ドキュメント](https://spring.io/projects/spring-boot)
- [Prometheus公式ドキュメント](https://prometheus.io/docs/)
- [JPA/Hibernateベストプラクティス](https://vladmihalcea.com/tutorials/hibernate/)

### 🚀 次のステップ

#### さらに学びたい方へ
1. **BFFハンズオン**: BFF層でのリトライ機構とエラーハンドリング
2. **Frontendハンズオン**: Vue.jsでのUI実装
3. **セキュリティハンズオン**: JWT認証とOWASP対策
4. **パフォーマンスチューニング**: JVMチューニングとキャッシング戦略

#### 実践課題
1. 契約更新API（PUT /api/policies/{id}）の実装
2. 保険料計算ロジックの追加
3. Grafanaダッシュボードの作成
4. E2Eテストの追加

---

## トラブルシューティング

### よくある問題と解決方法

#### 1. Backend APIが起動しない

**症状**: `mvn spring-boot:run` でエラー

**原因と解決**:
```bash
# PostgreSQLが起動していない
docker ps | grep postgres
# → 起動していなければ: ./db_start.sh (Mac/Linux) または .\db_start.ps1 (Windows)

# ポート52080が使用中
lsof -i :52080  # Mac/Linux
netstat -ano | findstr :52080  # Windows
# → プロセスを終了するか、別のポートを使用

# Java 21がインストールされていない
java -version
# → Java 21をインストール
```

#### 2. Bobが期待通りに動作しない

**症状**: Bobの回答が不正確

**解決方法**:
1. より具体的な指示を与える
2. ファイルパスを明示的に指定
3. 既存コードの構造を説明
4. 段階的に小さなタスクに分割

#### 3. テストが失敗する

**症状**: `mvn test` でエラー

**解決方法**:
```bash
# テストデータベースの確認
cat backend-api/src/test/resources/application-test.yml

# 特定のテストのみ実行
mvn test -Dtest=PolicyServiceTest#testGetPolicyById

# デバッグモードで実行
mvn test -X
```

#### 4. メトリクスが表示されない

**症状**: Prometheusでメトリクスが見えない

**解決方法**:
```bash
# Actuatorエンドポイント確認
curl http://localhost:52080/actuator/prometheus

# Prometheus設定確認
cat monitoring/prometheus.yml

# Prometheusターゲット確認
open http://localhost:52090/targets
```

---

## 付録

### A. 環境変数一覧

```bash
# データベース接続
DB_HOST=localhost
DB_PORT=52432
DB_NAME=insurance_db
DB_USER=insurance_user
DB_PASSWORD=insurance_pass

# サーバー設定
SERVER_PORT=52080

# JWT設定（64文字以上必須）
JWT_SECRET=your-secret-key-change-in-production-min-512-bits-for-hs512-algorithm-security

# 環境識別
ENVIRONMENT=dev
```

### B. 主要なエンドポイント一覧

#### Backend API (ポート: 52080)

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/actuator/health` | ヘルスチェック |
| GET | `/actuator/metrics` | メトリクス一覧 |
| GET | `/actuator/prometheus` | Prometheus形式メトリクス |
| POST | `/api/auth/login` | ログイン |
| GET | `/api/customers/{id}` | 顧客情報取得 |
| GET | `/api/policies` | 契約一覧取得 |
| GET | `/api/policies/{id}` | 契約詳細取得 |
| POST | `/api/policies/{id}/cancel` | 契約キャンセル（新規） |

#### Prometheus (ポート: 9090)

| パス | 説明 |
|------|------|
| `/` | ダッシュボード |
| `/targets` | 監視対象一覧 |
| `/alerts` | アラート一覧 |
| `/graph` | メトリクスグラフ |

### C. Bobプロンプト例集

#### コード分析
```
/ask [ファイルパス] を分析して、[観点] について教えてください。
```

#### コード生成
```
/code [ファイルパス] に以下の要件で[機能] を実装してください：
1. [要件1]
2. [要件2]
既存のコード構造に従ってください。
```

#### リファクタリング
```
/code [ファイルパス] の [メソッド名] を [改善内容] にリファクタリングしてください。
既存の動作を変えないように注意してください。
```

#### テスト生成
```
/code [テストファイルパス] に [対象メソッド] のテストケースを追加してください：
- 正常系: [シナリオ]
- 異常系: [シナリオ]
```

#### 計画立案
```
/plan [タスク内容] を実現するための計画を立ててください。
既存のコード構造と制約を考慮してください。
```

---

**ハンズオン作成日**: 2026-05-14  
**対象バージョン**: Backend API 1.0.0-SNAPSHOT  
**作成者**: IBM Bob + Human Collaboration
