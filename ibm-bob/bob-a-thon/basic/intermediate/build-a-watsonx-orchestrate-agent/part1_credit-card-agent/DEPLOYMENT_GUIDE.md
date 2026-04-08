# Watsonx Orchestrateデプロイメントガイド

このガイドでは、クレジットカード管理マルチエージェントシステムをWatsonx Orchestrateにデプロイする手順を説明します。

## 前提条件の確認

デプロイを開始する前に、以下を確認してください：

1. ✅ Python 3.8以上がインストールされている
2. ✅ Watsonx Orchestrate環境へのアクセス権限がある
3. ✅ 必要な認証情報（APIキー、環境URL）を持っている

## デプロイメント手順

### ステップ1: 環境の準備

```bash
# プロジェクトディレクトリに移動
cd credit-card-agent

# Watsonx Orchestrate SDKがインストールされているか確認
pip list | grep ibm-watsonx-orchestrate

# インストールされていない場合
pip install ibm-watsonx-orchestrate
```

### ステップ2: 環境の有効化

```bash
# Watsonx Orchestrate環境を有効化
orchestrate env activate wxo-aws

# プロンプトが表示されたら、認証情報を入力してください
# - API Key
# - Environment URL
```

**注意:** 認証情報は安全に保管し、共有しないでください。

### ステップ3: ツールのインポート

#### 3.1 不正検知ツールのインポート

```bash
orchestrate tools import -k python -f tools/fraud_tools.py
```

**期待される出力:**
```
✓ Successfully imported 5 tools from fraud_tools.py:
  - check_transactions
  - report_fraud
  - freeze_credit_card
  - cancel_credit_card
  - send_new_credit_card
```

#### 3.2 サブスクリプション管理ツールのインポート

```bash
orchestrate tools import -k python -f tools/subscription_tools.py
```

**期待される出力:**
```
✓ Successfully imported 3 tools from subscription_tools.py:
  - get_subscriptions
  - get_subscription_spend
  - cancel_subscription
```

### ステップ4: インポートの確認

```bash
# インポートされたツールを確認
orchestrate tools list

# 特定のツールの詳細を確認
orchestrate tools describe check_transactions
```

### ステップ5: エージェントのインポート

#### 5.1 不正検知エージェントのインポート

```bash
orchestrate agents import -f agents/fraud_agent.yaml
```

**期待される出力:**
```
✓ Successfully imported agent: fraud_agent
```

#### 5.2 サブスクリプション管理エージェントのインポート

```bash
orchestrate agents import -f agents/manage_subscriptions_agent.yaml
```

**期待される出力:**
```
✓ Successfully imported agent: manage_subscriptions_agent
```

#### 5.3 オーケストレーターエージェントのインポート

```bash
orchestrate agents import -f agents/credit_card_management_agent.yaml
```

**期待される出力:**
```
✓ Successfully imported agent: credit_card_management_agent
```

### ステップ6: デプロイメントの確認

```bash
# インポートされたエージェントを確認
orchestrate agents list

# 特定のエージェントの詳細を確認
orchestrate agents describe credit_card_management_agent
```

### ステップ7: エージェントのテスト

#### 7.1 Webインターフェースでのテスト

1. Watsonx Orchestrateのウェブインターフェースにアクセス
2. 「Agents」セクションに移動
3. `credit_card_management_agent`を選択
4. チャットインターフェースでサンプル質問を試す

#### 7.2 CLIでのテスト（オプション）

```bash
# エージェントとの対話を開始
orchestrate agents chat credit_card_management_agent

# サンプル質問を入力
> カードに異常な取引があれば表示してください
```

## デプロイメント後の確認事項

### ✅ チェックリスト

- [ ] すべてのツール（8個）が正常にインポートされた
- [ ] すべてのエージェント（3個）が正常にインポートされた
- [ ] fraud_agentが不正検知ツールにアクセスできる
- [ ] manage_subscriptions_agentがサブスクリプション管理ツールにアクセスできる
- [ ] credit_card_management_agentが両方のサブエージェントを調整できる
- [ ] サンプル質問に対して適切な応答が返される

### 動作確認用サンプル質問

以下の質問で各機能をテストしてください：

1. **不正検知のテスト:**
   ```
   カードに異常な取引があれば表示してください
   ```

2. **サブスクリプション管理のテスト:**
   ```
   どのサブスクリプションに支払っていますか?
   ```

3. **オーケストレーションのテスト:**
   ```
   不正な取引を確認して、すべてのサブスクリプションも表示してください
   ```

## トラブルシューティング

### 問題1: 認証エラー

**症状:**
```
[ERROR] - The token found for environment 'wxo-aws' is missing or expired
```

**解決策:**
```bash
# 環境を再度有効化
orchestrate env activate wxo-aws

# 認証情報を再入力
```

### 問題2: ツールのインポートエラー

**症状:**
```
[ERROR] - Failed to import tools from fraud_tools.py
```

**解決策:**
```bash
# Pythonファイルの構文を確認
python -m py_compile tools/fraud_tools.py

# 依存関係を確認
pip install ibm-watsonx-orchestrate --upgrade

# 再度インポートを試行
orchestrate tools import -k python -f tools/fraud_tools.py
```

### 問題3: エージェントがツールにアクセスできない

**症状:**
エージェントがツールを呼び出せない

**解決策:**
```bash
# ツールが正しくインポートされているか確認
orchestrate tools list

# エージェントのYAML設定を確認
cat agents/fraud_agent.yaml

# エージェントを再インポート
orchestrate agents delete fraud_agent
orchestrate agents import -f agents/fraud_agent.yaml
```

### 問題4: サブエージェントが見つからない

**症状:**
```
[ERROR] - Sub-agent 'fraud_agent' not found
```

**解決策:**
```bash
# サブエージェントが先にインポートされているか確認
orchestrate agents list | grep fraud_agent

# サブエージェントを先にインポート
orchestrate agents import -f agents/fraud_agent.yaml
orchestrate agents import -f agents/manage_subscriptions_agent.yaml

# その後、オーケストレーターをインポート
orchestrate agents import -f agents/credit_card_management_agent.yaml
```

## デプロイメントスクリプト

手動でのデプロイが面倒な場合は、以下のスクリプトを使用できます：

### deploy.sh

```bash
#!/bin/bash

echo "=== クレジットカード管理エージェントのデプロイメント ==="
echo ""

# 環境変数の確認
if [ -z "$WXO_API_KEY" ]; then
    echo "エラー: WXO_API_KEY環境変数が設定されていません"
    exit 1
fi

# ステップ1: ツールのインポート
echo "ステップ1: ツールをインポート中..."
orchestrate tools import -k python -f tools/fraud_tools.py
if [ $? -ne 0 ]; then
    echo "エラー: fraud_tools.pyのインポートに失敗しました"
    exit 1
fi

orchestrate tools import -k python -f tools/subscription_tools.py
if [ $? -ne 0 ]; then
    echo "エラー: subscription_tools.pyのインポートに失敗しました"
    exit 1
fi

echo "✓ ツールのインポートが完了しました"
echo ""

# ステップ2: エージェントのインポート
echo "ステップ2: エージェントをインポート中..."
orchestrate agents import -f agents/fraud_agent.yaml
if [ $? -ne 0 ]; then
    echo "エラー: fraud_agentのインポートに失敗しました"
    exit 1
fi

orchestrate agents import -f agents/manage_subscriptions_agent.yaml
if [ $? -ne 0 ]; then
    echo "エラー: manage_subscriptions_agentのインポートに失敗しました"
    exit 1
fi

orchestrate agents import -f agents/credit_card_management_agent.yaml
if [ $? -ne 0 ]; then
    echo "エラー: credit_card_management_agentのインポートに失敗しました"
    exit 1
fi

echo "✓ エージェントのインポートが完了しました"
echo ""

# ステップ3: 確認
echo "ステップ3: デプロイメントを確認中..."
echo ""
echo "インポートされたツール:"
orchestrate tools list
echo ""
echo "インポートされたエージェント:"
orchestrate agents list
echo ""

echo "=== デプロイメントが完了しました ==="
echo ""
echo "次のステップ:"
echo "1. Watsonx Orchestrateのウェブインターフェースにアクセス"
echo "2. credit_card_management_agentを開く"
echo "3. サンプル質問を試す"
```

### 使用方法

```bash
# スクリプトに実行権限を付与
chmod +x deploy.sh

# 環境変数を設定
export WXO_API_KEY="your-api-key-here"

# スクリプトを実行
./deploy.sh
```

## アップデート手順

既存のデプロイメントを更新する場合：

```bash
# ツールの更新
orchestrate tools update -k python -f tools/fraud_tools.py
orchestrate tools update -k python -f tools/subscription_tools.py

# エージェントの更新
orchestrate agents update -f agents/fraud_agent.yaml
orchestrate agents update -f agents/manage_subscriptions_agent.yaml
orchestrate agents update -f agents/credit_card_management_agent.yaml
```

## クリーンアップ

デプロイメントを削除する場合：

```bash
# エージェントの削除（オーケストレーターから先に削除）
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

## サポート

デプロイメントに関する問題や質問がある場合：

1. このガイドのトラブルシューティングセクションを確認
2. README.mdの詳細なドキュメントを参照
3. Watsonx Orchestrateの公式ドキュメントを確認
4. プロジェクトのIssueトラッカーで報告

---

**最終更新:** 2024年4月6日  
**バージョン:** 1.0.0