# 環境設定ガイド

このガイドでは、`.env` ファイルを使ってデュアルバンクアプリケーションを設定し、
環境ごとに柔軟にデプロイできるようにする方法を説明します。

## 概要

このアプリケーションは、`.env` ファイルを使った環境ベースの設定に対応しています。
これにより、ソースコードに URL、ポート、そのほかの設定値をハードコードする必要がなくなります。

## クイックセットアップ

### 1. バックエンド設定

#### Bank1 (Savings Bank)
```bash
cd bank1-savings
cp .env.example .env
# Edit .env with your settings
```

#### Bank2 (Investment Bank)
```bash
cd bank2-investment
cp .env.example .env
# Edit .env with your settings
```

### 2. フロントエンド設定
```bash
cd bank1-savings/frontend
cp .env.example .env
# Edit .env with your settings
```

### 3. 依存関係のインストール
```bash
# Bank1
cd bank1-savings
pip install -r requirements.txt

# Bank2
cd bank2-investment
pip install -r requirements.txt

# Frontend
cd bank1-savings/frontend
npm install
```

## 設定ファイル

### Bank1 `.env` 設定

**場所**: `bank1-savings/.env`

```env
# Bank Identity
BANK_NAME=Savings Bank
BANK_ID=bank1
BANK_COLOR=#2E7D32

# Database Configuration
DB_PATH=bank1_savings.db
AUDIT_LOG_PATH=bank1_audit.jsonl

# Server Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
FLASK_DEBUG=False

# Inter-bank Communication
BANK2_URL=http://localhost:5000

# Frontend Configuration (for production builds)
FRONTEND_URL=http://localhost:5173
```

### Bank2 `.env` 設定

**場所**: `bank2-investment/.env`

```env
# Bank Identity
BANK_NAME=Investment Bank
BANK_ID=bank2
BANK_COLOR=#1565C0

# Database Configuration
DB_PATH=bank2_investment.db
AUDIT_LOG_PATH=bank2_audit.jsonl

# Server Configuration
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
FLASK_DEBUG=False

# Inter-bank Communication
BANK1_URL=http://localhost:5001
```

### フロントエンド `.env` 設定

**場所**: `bank1-savings/frontend/.env`

```env
# API Base URL - defaults to relative path for same-origin requests
# For development with separate backend server, use:
# VITE_API_BASE_URL=http://localhost:5001/api

# For production (served by Flask), use relative path:
VITE_API_BASE_URL=/api

# Development server port
VITE_PORT=5173
```

## 環境変数リファレンス

### バックエンド変数

| 変数 | 説明 | 既定値 | 例 |
|----------|-------------|---------|---------|
| `BANK_NAME` | 銀行の表示名 | "Savings Bank" / "Investment Bank" | "My Savings Bank" |
| `BANK_ID` | 銀行を識別する一意 ID | "bank1" / "bank2" | "bank1" |
| `BANK_COLOR` | テーマカラー（16 進数） | "#2E7D32" / "#1565C0" | "#FF5722" |
| `DB_PATH` | SQLite データベースファイルのパス | "bank1_savings.db" | "./data/bank.db" |
| `AUDIT_LOG_PATH` | 監査ログファイルのパス | "bank1_audit.jsonl" | "./logs/audit.jsonl" |
| `FLASK_HOST` | Flask サーバーのホスト | "0.0.0.0" | "127.0.0.1" |
| `FLASK_PORT` | Flask サーバーのポート | 5001 / 5000 | 8080 |
| `FLASK_DEBUG` | Flask のデバッグモードを有効化するか | "False" | "True" |
| `BANK2_URL` | Bank2 API のエンドポイント（Bank1 のみ） | "http://localhost:5000" | "http://bank2:5000" |
| `BANK1_URL` | Bank1 API のエンドポイント（Bank2 のみ） | "http://localhost:5001" | "http://bank1:5001" |

### フロントエンド変数

| 変数 | 説明 | 既定値 | 例 |
|----------|-------------|---------|---------|
| `VITE_API_BASE_URL` | バックエンド API のベース URL | "/api" | "http://localhost:5001/api" |
| `VITE_PORT` | Vite 開発サーバーのポート | 5173 | 3000 |

## よくある利用シナリオ

### シナリオ 1: ローカル開発（既定ポート）

**Bank2**（ポート 5000 で起動）:
```env
FLASK_PORT=5000
BANK1_URL=http://localhost:5001
```

**Bank1**（ポート 5001 で起動）:
```env
FLASK_PORT=5001
BANK2_URL=http://localhost:5000
```

**Frontend**（ポート 5173 で起動）:
```env
VITE_API_BASE_URL=/api
VITE_PORT=5173
```

### シナリオ 2: カスタムポート

Bank2 をポート 8080 で動かす場合:

**Bank2**:
```env
FLASK_PORT=8080
```

**Bank1**:
```env
BANK2_URL=http://localhost:8080
```

### シナリオ 3: Docker デプロイ

**Bank1**:
```env
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
BANK2_URL=http://bank2:5000
```

**Bank2**:
```env
FLASK_HOST=0.0.0.0
FLASK_PORT=5000
BANK1_URL=http://bank1:5000
```

### シナリオ 4: 本番デプロイ

**Bank1**:
```env
FLASK_DEBUG=False
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
BANK2_URL=https://bank2.example.com
```

**Frontend**（本番ビルド）:
```env
VITE_API_BASE_URL=https://bank1.example.com/api
```

## アプリケーションの起動

### 環境変数ファイルを使う場合

**Terminal 1 - Bank2**:
```bash
cd bank2-investment
python app.py
# Reads from .env file automatically
```

**Terminal 2 - Bank1**:
```bash
cd bank1-savings
python app.py
# Reads from .env file automatically
```

**Terminal 3 - Frontend**:
```bash
cd bank1-savings/frontend
npm run dev
# Reads from .env file automatically
```

### コマンドラインから上書きする場合

環境変数を使えば、`.env` の値をコマンドラインから上書きできます。

**Windows PowerShell**:
```powershell
$env:FLASK_PORT="8080"
python app.py
```

**Windows CMD**:
```cmd
set FLASK_PORT=8080
python app.py
```

**Linux/Mac**:
```bash
FLASK_PORT=8080 python app.py
```

## トラブルシューティング

### 問題: "Connection refused" エラーが出る

**症状**: 振込時に Bank1 から Bank2 に接続できない。

**対処**: Bank1 の `.env` にある `BANK2_URL` が、Bank2 の実際のホストとポートに一致しているか確認してください。
```bash
# Check Bank2 is running
curl http://localhost:5000/health

# Update Bank1's .env
BANK2_URL=http://localhost:5000
```

### 問題: フロントエンドがバックエンドに接続できない

**症状**: API 呼び出しが CORS エラーまたは接続エラーで失敗する。

**対処**: フロントエンドの `.env` を更新してください。
```env
# For separate backend server
VITE_API_BASE_URL=http://localhost:5001/api
```

### 問題: ポートがすでに使われている

**症状**: サーバー起動時に "Address already in use" エラーが出る。

**対処**: `.env` 内のポート番号を変更してください。
```env
FLASK_PORT=5002
```

### 問題: 変更が反映されない

**症状**: `.env` を変更しても新しい値が使われない。

**対処**:
1. アプリケーションを再起動する（Ctrl+C で停止して再度起動）
2. `.env` ファイルが正しいディレクトリにあることを確認する
3. 変数名にタイプミスがないか確認する

## セキュリティのベストプラクティス

1. **`.env` ファイルは絶対にコミットしない** - すでに `.gitignore` に含まれています
2. **`.env.example` を使う** - テンプレートとしてこれをコミットします
3. **シークレットを定期的にローテーションする** - 機密値は定期的に変更します
4. **権限を制限する** - Unix 系では `chmod 600 .env` を推奨します
5. **環境ごとに値を分ける** - 本番環境でサンプル値を使わないでください

## ハードコードされた値から移行する場合

以前のハードコードされた設定から移行する場合は、次の順で進めてください。

1. `.env.example` から `.env` ファイルを作成する
2. 必要な値を設定する（特に既定以外のポートを使う場合の `BANK2_URL`）
3. すべてのサービスを再起動する
4. 銀行間振込が正常に動くことを確認する

## 追加リソース

- [python-dotenv Documentation](https://github.com/theskumar/python-dotenv)
- [Vite Environment Variables](https://vitejs.dev/guide/env-and-mode.html)
- [Flask Configuration](https://flask.palletsprojects.com/en/3.0.x/config/)

## サポート

環境設定に関する質問や問題がある場合は、メインの `application_desc.md` を参照するか、プロジェクトのリポジトリに issue を作成してください。
