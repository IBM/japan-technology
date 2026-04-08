# クイックスタートガイド

このガイドでは、クレジットカード管理エージェントシステムを最速でデプロイする方法を説明します。

## 🚀 5分でデプロイ

### 前提条件

- ✅ Watsonx Orchestrate環境へのアクセス
- ✅ Python 3.8以上
- ✅ 認証情報（APIキー）

### ステップ1: 環境の有効化

```bash
# Watsonx Orchestrate環境を有効化
orchestrate env activate wxo-aws
```

プロンプトが表示されたら、APIキーとその他の認証情報を入力してください。

### ステップ2: 自動デプロイ

```bash
# プロジェクトディレクトリに移動
cd credit-card-agent

# デプロイスクリプトを実行
./deploy.sh
```

スクリプトが以下を自動的に実行します：
1. ✅ 8つのツールをインポート
2. ✅ 3つのエージェントをインポート
3. ✅ デプロイメントを確認

### ステップ3: テスト

Watsonx Orchestrateのウェブインターフェースで：

1. **Agents**セクションに移動
2. **credit_card_management_agent**を選択
3. 以下の質問を試す：

```
カードに異常な取引があれば表示してください
```

## 📝 手動デプロイ（詳細制御が必要な場合）

### ツールのインポート

```bash
cd credit-card-agent

# 不正検知ツール
orchestrate tools import -k python -f tools/fraud_tools.py

# サブスクリプション管理ツール
orchestrate tools import -k python -f tools/subscription_tools.py
```

### エージェントのインポート

```bash
# サブエージェントを先にインポート
orchestrate agents import -f agents/fraud_agent.yaml
orchestrate agents import -f agents/manage_subscriptions_agent.yaml

# オーケストレーターを最後にインポート
orchestrate agents import -f agents/credit_card_management_agent.yaml
```

## 🧪 動作確認

### テスト質問

以下の質問で各機能をテストしてください：

#### 1. 不正検知
```
カードに異常な取引があれば表示してください
```

**期待される応答:** 3件の疑わしい取引のリスト

#### 2. サブスクリプション一覧
```
どのサブスクリプションに支払っていますか?
```

**期待される応答:** 5〜7件のアクティブなサブスクリプション

#### 3. カテゴリ別支出
```
ストリーミングサービスにいくら使っていますか?
```

**期待される応答:** ストリーミングカテゴリの月額・年額費用

#### 4. 複合クエリ
```
不正な取引を確認して、すべてのサブスクリプションも表示してください
```

**期待される応答:** 不正取引とサブスクリプションの両方の情報

## ❓ よくある質問

### Q1: 認証エラーが発生する

**A:** 環境を再度有効化してください：
```bash
orchestrate env activate wxo-aws
```

### Q2: ツールのインポートに失敗する

**A:** Pythonファイルの構文を確認してください：
```bash
python -m py_compile tools/fraud_tools.py
python -m py_compile tools/subscription_tools.py
```

### Q3: エージェントがツールを見つけられない

**A:** ツールが先にインポートされているか確認してください：
```bash
orchestrate tools list
```

### Q4: サブエージェントが見つからない

**A:** サブエージェントを先にインポートしてください：
```bash
# 正しい順序
orchestrate agents import -f agents/fraud_agent.yaml
orchestrate agents import -f agents/manage_subscriptions_agent.yaml
orchestrate agents import -f agents/credit_card_management_agent.yaml
```

## 🔧 トラブルシューティング

問題が発生した場合：

1. **DEPLOYMENT_GUIDE.md**の詳細なトラブルシューティングセクションを確認
2. **README.md**の完全なドキュメントを参照
3. ログを確認：
   ```bash
   orchestrate logs --agent credit_card_management_agent
   ```

## 📚 次のステップ

デプロイが成功したら：

1. **README.md**で詳細な機能を確認
2. **ui/test_ui.html**でローカルテストを実行
3. カスタムツールやエージェントを追加して拡張

## 🗑️ クリーンアップ

デプロイメントを削除する場合：

```bash
# エージェントの削除
orchestrate agents delete credit_card_management_agent
orchestrate agents delete manage_subscriptions_agent
orchestrate agents delete fraud_agent

# ツールの削除
orchestrate tools delete check_transactions
orchestrate tools delete report_fraud
orchestrate tools delete freeze_credit_card
orchestrate tools delete cancel_credit_card
orchestrate tools delete send_new_credit_card
orchestrate tools delete get_subscriptions
orchestrate tools delete get_subscription_spend
orchestrate tools delete cancel_subscription
```

## 📞 サポート

- 📖 詳細なドキュメント: **README.md**
- 🚀 デプロイメントガイド: **DEPLOYMENT_GUIDE.md**
- 🌐 テストUI: **ui/test_ui.html**

---

**ヒント:** 初めてデプロイする場合は、`./deploy.sh`スクリプトの使用を推奨します。