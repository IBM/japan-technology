#!/bin/bash

echo "=== クレジットカード管理エージェントのデプロイメント ==="
echo ""

# カラーコード
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# エラーハンドリング
set -e
trap 'echo -e "${RED}エラー: デプロイメントに失敗しました${NC}"; exit 1' ERR

# 現在のディレクトリを確認
if [ ! -f "tools/fraud_tools.py" ]; then
    echo -e "${RED}エラー: credit-card-agentディレクトリで実行してください${NC}"
    exit 1
fi

echo -e "${YELLOW}注意: このスクリプトを実行する前に、以下を確認してください:${NC}"
echo "1. orchestrate env activate wxo-aws を実行して認証済み"
echo "2. 必要な権限を持っている"
echo ""
read -p "続行しますか? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "デプロイメントをキャンセルしました"
    exit 0
fi

# ステップ1: ツールのインポート
echo ""
echo "=== ステップ1: ツールをインポート中... ==="
echo ""

echo "不正検知ツールをインポート中..."
if orchestrate tools import -k python -f tools/fraud_tools.py; then
    echo -e "${GREEN}✓ fraud_tools.pyのインポートが完了しました${NC}"
else
    echo -e "${RED}✗ fraud_tools.pyのインポートに失敗しました${NC}"
    exit 1
fi

echo ""
echo "サブスクリプション管理ツールをインポート中..."
if orchestrate tools import -k python -f tools/subscription_tools.py; then
    echo -e "${GREEN}✓ subscription_tools.pyのインポートが完了しました${NC}"
else
    echo -e "${RED}✗ subscription_tools.pyのインポートに失敗しました${NC}"
    exit 1
fi

# ステップ2: エージェントのインポート
echo ""
echo "=== ステップ2: エージェントをインポート中... ==="
echo ""

echo "不正検知エージェントをインポート中..."
if orchestrate agents import -f agents/fraud_agent.yaml; then
    echo -e "${GREEN}✓ fraud_agentのインポートが完了しました${NC}"
else
    echo -e "${RED}✗ fraud_agentのインポートに失敗しました${NC}"
    exit 1
fi

echo ""
echo "サブスクリプション管理エージェントをインポート中..."
if orchestrate agents import -f agents/manage_subscriptions_agent.yaml; then
    echo -e "${GREEN}✓ manage_subscriptions_agentのインポートが完了しました${NC}"
else
    echo -e "${RED}✗ manage_subscriptions_agentのインポートに失敗しました${NC}"
    exit 1
fi

echo ""
echo "オーケストレーターエージェントをインポート中..."
if orchestrate agents import -f agents/credit_card_management_agent.yaml; then
    echo -e "${GREEN}✓ credit_card_management_agentのインポートが完了しました${NC}"
else
    echo -e "${RED}✗ credit_card_management_agentのインポートに失敗しました${NC}"
    exit 1
fi

# ステップ3: 確認
echo ""
echo "=== ステップ3: デプロイメントを確認中... ==="
echo ""

echo "インポートされたツール:"
orchestrate tools list | grep -E "(check_transactions|report_fraud|freeze_credit_card|cancel_credit_card|send_new_credit_card|get_subscriptions|get_subscription_spend|cancel_subscription)" || echo "ツールの確認に失敗しました"

echo ""
echo "インポートされたエージェント:"
orchestrate agents list | grep -E "(fraud_agent|manage_subscriptions_agent|credit_card_management_agent)" || echo "エージェントの確認に失敗しました"

echo ""
echo -e "${GREEN}=== デプロイメントが完了しました ===${NC}"
echo ""
echo "次のステップ:"
echo "1. Watsonx Orchestrateのウェブインターフェースにアクセス"
echo "2. credit_card_management_agentを開く"
echo "3. 以下のサンプル質問を試す:"
echo "   - カードに異常な取引があれば表示してください"
echo "   - どのサブスクリプションに支払っていますか?"
echo "   - ストリーミングサービスにいくら使っていますか?"
echo ""

# Made with Bob
