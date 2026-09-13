# クレジットカード管理マルチエージェントシステム

Watsonx Orchestrate用のクレジットカード管理マルチエージェントアプリケーションのプロトタイプです。不正検知、カードセキュリティ、サブスクリプション管理の機能を提供します。

## 📋 目次

- [概要](#概要)
- [アーキテクチャ](#アーキテクチャ)
- [プロジェクト構造](#プロジェクト構造)
- [実装の詳細](#実装の詳細)
- [前提条件](#前提条件)
- [デプロイメント手順](#デプロイメント手順)
- [テストWeb UI](#テストweb-ui)
- [サンプル質問](#サンプル質問)
- [トラブルシューティング](#トラブルシューティング)

## 概要

このプロトタイプは、3つの専門エージェントで構成されるマルチエージェントシステムです：

1. **fraud_agent** - 不正検知とカードセキュリティ
2. **manage_subscriptions_agent** - サブスクリプション管理
3. **credit_card_management_agent** - オーケストレーターエージェント

すべてのデータはハードコードされており、実際のクレジットカードシステムには接続していません。

## アーキテクチャ

```
┌─────────────────────────────────────────────┐
│   credit_card_management_agent              │
│   (オーケストレーター)                        │
└─────────────┬───────────────────────────────┘
              │
      ┌───────┴───────┐
      │               │
┌─────▼─────┐   ┌────▼──────────┐
│fraud_agent│   │manage_         │
│           │   │subscriptions_  │
│           │   │agent           │
└─────┬─────┘   └────┬───────────┘
      │              │
┌─────▼─────┐   ┌────▼───────────┐
│fraud_     │   │subscription_   │
│tools.py   │   │tools.py        │
└───────────┘   └────────────────┘
```

## プロジェクト構造

```
credit-card-agent/
├── agents/
│   ├── fraud_agent.yaml                      # 不正検知エージェント設定
│   ├── manage_subscriptions_agent.yaml       # サブスクリプション管理エージェント設定
│   └── credit_card_management_agent.yaml     # オーケストレーターエージェント設定
├── tools/
│   ├── fraud_tools.py                        # 不正検知ツール実装
│   └── subscription_tools.py                 # サブスクリプション管理ツール実装
├── ui/
│   └── test_ui.html                          # テストWeb UI
└── README.md                                 # このファイル
```

## 実装の詳細

### エージェント

#### 1. fraud_agent（不正検知エージェント）

**責任:**
- 異常な取引の検出と報告
- クレジットカードの凍結・キャンセル
- 新規カード発行の処理

**ツール:**
- `check_transactions()` - 異常な取引を最大3件リスト
- `report_fraud(transaction_id)` - 不正ケースを開く
- `freeze_credit_card(card_number)` - カードを一時凍結
- `cancel_credit_card(card_number, reason)` - カードを永久キャンセル
- `send_new_credit_card(address)` - 新しいカードを送付

#### 2. manage_subscriptions_agent（サブスクリプション管理エージェント）

**責任:**
- アクティブなサブスクリプションの管理
- カテゴリ別支出の分析
- サブスクリプションのキャンセル

**ツール:**
- `get_subscriptions()` - 5〜7件のサブスクリプションをリスト
- `get_subscription_spend(category)` - カテゴリ別支出を計算
- `cancel_subscription(subscription_name)` - サブスクリプションをキャンセル

**サポートされるカテゴリ:**
- `streaming` - ストリーミングサービス（Netflix、Spotifyなど）
- `software` - ソフトウェアサブスクリプション（Adobe、Microsoft 365など）
- `fitness` - フィットネス関連（ジムメンバーシップなど）
- `shopping` - ショッピング関連（Amazon Primeなど）
- `news` - ニュース・メディア（The New York Timesなど）

#### 3. credit_card_management_agent（オーケストレーターエージェント）

**責任:**
- ユーザークエリの適切なエージェントへのルーティング
- 複数エージェントからの情報統合
- 統一された会話型インターフェースの提供

### ツール実装

すべてのツールはPythonで実装され、Watsonx Orchestrate SDKを使用しています。

**サンプルハードコードデータ:**

**不正取引データ:**
```python
{
    "transaction_id": "TXN-2024-001",
    "amount": 1250.00,
    "merchant": "Electronics World Online",
    "location": "Moscow, Russia",
    "reason": "通常と異なる地域からの高額購入"
}
```

**サブスクリプションデータ:**
```python
{
    "subscription_id": "SUB-001",
    "name": "Netflix Premium",
    "category": "streaming",
    "amount": 15.99,
    "frequency": "monthly",
    "next_billing_date": "2024-04-15"
}
```

## 前提条件

### システム要件
- Python 3.8以上
- pip（Pythonパッケージマネージャー）
- Watsonx Orchestrate環境へのアクセス

### 必要なパッケージ
```bash
pip install ibm-watsonx-orchestrate
```

## デプロイメント手順

### ステップ1: 環境のセットアップ

```bash
# Watsonx Orchestrate CLIのインストール（まだの場合）
pip install ibm-watsonx-orchestrate

# 認証情報の設定
orchestrate login
```

### ステップ2: ツールのインポート

```bash
# プロジェクトディレクトリに移動
cd credit-card-agent

# 不正検知ツールをインポート
orchestrate tools import -k python -f tools/fraud_tools.py

# サブスクリプション管理ツールをインポート
orchestrate tools import -k python -f tools/subscription_tools.py
```

### ステップ3: エージェントのインポート

```bash
# 不正検知エージェントをインポート
orchestrate agents import -f agents/fraud_agent.yaml

# サブスクリプション管理エージェントをインポート
orchestrate agents import -f agents/manage_subscriptions_agent.yaml

# オーケストレーターエージェントをインポート
orchestrate agents import -f agents/credit_card_management_agent.yaml
```

### ステップ4: デプロイメントの確認

```bash
# インポートされたツールを確認
orchestrate tools list

# インポートされたエージェントを確認
orchestrate agents list
```

### ステップ5: エージェントのテスト

Watsonx Orchestrateのウェブインターフェースで`credit_card_management_agent`を開き、サンプル質問を試してください。

## テストWeb UI

ローカルでツールをテストするためのWeb UIが提供されています。

### 使用方法

1. ブラウザで`ui/test_ui.html`を開く
2. 各ツールカードで必要なパラメータを入力
3. ボタンをクリックしてツールを実行
4. 結果が画面下部に表示されます

**注意:** このUIはシミュレーションであり、実際のPythonツールは呼び出しません。実際の動作を確認するには、Watsonx Orchestrate環境でエージェントを使用してください。

### UIの機能

- **不正検知ツール（5つ）:**
  - 異常な取引を確認
  - 不正を報告
  - カードを凍結
  - カードをキャンセル
  - 新しいカードを送付

- **サブスクリプション管理ツール（3つ）:**
  - サブスクリプション一覧
  - カテゴリ別支出
  - サブスクリプションをキャンセル

## サンプル質問

以下は、`credit_card_management_agent`で試せるサンプル質問です：

### 不正検知関連

1. **"カードに異常な取引があれば表示してください"**
   - `fraud_agent`が`check_transactions()`を使用して異常な取引を表示

2. **"XYZストアからの不審な請求があります。助けてもらえますか?"**
   - `fraud_agent`が不正の可能性を調査し、適切なアクションを提案

3. **"すぐにクレジットカードを凍結してください"**
   - `fraud_agent`が`freeze_credit_card()`を使用してカードを凍結

4. **"不正取引を報告して新しいカードを送ってください"**
   - `fraud_agent`が`report_fraud()`と`send_new_credit_card()`を順次実行

5. **"カードを紛失しました。キャンセルして代替品を送ってください"**
   - `fraud_agent`が`cancel_credit_card()`と`send_new_credit_card()`を実行

### サブスクリプション管理関連

6. **"どのサブスクリプションに支払っていますか?"**
   - `manage_subscriptions_agent`が`get_subscriptions()`を使用して一覧を表示

7. **"ストリーミングサービスにいくら使っていますか?"**
   - `manage_subscriptions_agent`が`get_subscription_spend(category="streaming")`を実行

8. **"月間のサブスクリプション総額はいくらですか?"**
   - `manage_subscriptions_agent`が`get_subscription_spend()`を実行して総額を計算

9. **"すべてのエンターテインメントサブスクリプションを表示してください"**
   - `manage_subscriptions_agent`がストリーミングカテゴリのサブスクリプションを表示

10. **"ジムのメンバーシップサブスクリプションをキャンセルしてください"**
    - `manage_subscriptions_agent`が`cancel_subscription()`を実行

### 複合クエリ

11. **"不正な取引を確認して、すべてのサブスクリプションも表示してください"**
    - オーケストレーターが両方のエージェントを調整して情報を統合

12. **"カードをキャンセルした後、サブスクリプションはどうなりますか?"**
    - オーケストレーターが両方のエージェントから情報を収集して回答

## トラブルシューティング

### よくある問題

#### 1. ツールのインポートエラー

**問題:** `ModuleNotFoundError: No module named 'ibm_watsonx_orchestrate'`

**解決策:**
```bash
pip install ibm-watsonx-orchestrate
```

#### 2. 認証エラー

**問題:** `Authentication failed`

**解決策:**
```bash
# 再度ログイン
orchestrate login

# 認証情報を確認
orchestrate config show
```

#### 3. エージェントが応答しない

**問題:** エージェントが質問に応答しない

**解決策:**
- エージェントとツールが正しくインポートされているか確認
- Watsonx Orchestrateのログを確認
- エージェントのYAML設定を確認

#### 4. ツールの実行エラー

**問題:** ツールが期待通りに動作しない

**解決策:**
- ツールのPythonコードにエラーがないか確認
- 必要なパラメータがすべて提供されているか確認
- ツールを再インポート

### デバッグのヒント

1. **ログの確認:**
   ```bash
   orchestrate logs --agent credit_card_management_agent
   ```

2. **ツールの個別テスト:**
   ```bash
   orchestrate tools test check_transactions
   ```

3. **エージェントの再デプロイ:**
   ```bash
   orchestrate agents delete fraud_agent
   orchestrate agents import -f agents/fraud_agent.yaml
   ```

## ベストプラクティス

### セキュリティ

- 本番環境では、実際のカード番号を完全に表示しない
- すべての機密データを暗号化
- 適切な認証と認可を実装

### パフォーマンス

- 大量のデータを扱う場合は、ページネーションを実装
- キャッシュを活用して応答時間を改善
- 非同期処理を検討

### 保守性

- コードにコメントを追加
- エラーハンドリングを強化
- ユニットテストを作成

## 今後の拡張

このプロトタイプは以下のように拡張できます：

1. **実際のデータベース統合**
   - PostgreSQL、MongoDBなどのデータベースに接続
   - 実際の取引データとサブスクリプションデータを使用

2. **機械学習モデルの統合**
   - 不正検知のための機械学習モデル
   - サブスクリプション推奨システム

3. **追加機能**
   - 支出分析とレポート
   - 予算管理
   - アラートと通知

4. **外部API統合**
   - 実際のクレジットカード会社のAPI
   - サブスクリプションサービスのAPI

## ライセンス

このプロジェクトはプロトタイプであり、教育目的で提供されています。

## サポート

問題や質問がある場合は、プロジェクトのIssueトラッカーで報告してください。

---

**作成日:** 2024年4月6日  
**バージョン:** 1.0.0  
**プラットフォーム:** IBM Watsonx Orchestrate