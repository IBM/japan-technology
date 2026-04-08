#!/bin/bash

# クレジットカード管理アプリケーション起動スクリプト

echo "🚀 クレジットカード管理アプリケーションを起動しています..."
echo ""

# プロジェクトルートディレクトリに移動
cd "$(dirname "$0")/.."

# 環境変数の確認
if [ ! -f ".env" ]; then
    echo "⚠️  警告: .envファイルが見つかりません"
    echo "認証情報を設定してください"
    echo ""
fi

# 必要なパッケージの確認
echo "📦 必要なパッケージを確認しています..."
python3 -c "import streamlit, pandas, plotly" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  必要なパッケージがインストールされていません"
    echo "以下のコマンドでインストールしてください:"
    echo "  pip install -r custom-ui/requirements.txt"
    echo ""
    exit 1
fi

echo "✅ パッケージの確認完了"
echo ""

# Streamlitアプリケーションを起動
echo "🌐 アプリケーションを起動しています..."
echo "ブラウザで http://localhost:8501 を開いてください"
echo ""
echo "終了するには Ctrl+C を押してください"
echo ""

streamlit run custom-ui/credit_card_ui.py

# Made with Bob
