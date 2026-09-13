# クレジットカード管理アプリケーション

Streamlitベースのクレジットカード管理ダッシュボードのプロトタイプ実装です。

## 機能

### 📊 ダッシュボード
- **概要統計**: 総支出、取引件数、平均取引額、今月の支出を表示
- **カテゴリ別支出**: 円グラフで支出の内訳を可視化
- **時系列分析**: 折れ線グラフで支出トレンドを表示

### 📋 取引管理
- 15-20件のモックトランザクションデータ
- カテゴリ別フィルタリング機能
- ソート可能なデータテーブル
- 以下のカテゴリをサポート:
  - 小売 (retail)
  - サブスクリプション (subscription)
  - 旅行 (travel)
  - 食料品 (groceries)
  - ガソリン (gas)

### 💬 AIアシスタント
- WxO Agent統合によるインテリジェントなチャット機能
- 取引に関する質問に回答
- 会話履歴の保持
- ストリーミングレスポンス

### ⚙️ サイドバー機能
- チャット履歴のクリア
- 統計情報の表示
- カテゴリ別サマリー

## 必要な環境

### Pythonパッケージ
```bash
pip install streamlit pandas plotly
```

### 依存モジュール
このアプリケーションは以下のモジュールに依存しています:
- `wxo/wxo_agent_adapter.py` - WxO Agent API統合
- `utils/` - 認証とトークン管理

## セットアップ

### 1. 環境変数の設定
プロジェクトルートの `.env` ファイルに以下の環境変数が設定されていることを確認してください:
```
WXO_API_KEY=your_api_key
WXO_AGENT_URL=your_agent_url
# その他の必要な認証情報
```

### 2. ディレクトリ構造
```
/Users/aa469668/0_CSE/Bob_wxO_実行用0406/
├── custom-ui/
│   ├── credit_card_ui.py      # メインアプリケーション
│   └── README.md              # このファイル
├── wxo/
│   └── wxo_agent_adapter.py   # WxO Agent Adapter
└── utils/
    ├── credentials_manager.py
    ├── token_manager.py
    └── wxo_config.py
```

## 実行方法

### プロジェクトルートから実行
```bash
cd /Users/aa469668/0_CSE/Bob_wxO_実行用0406
streamlit run custom-ui/credit_card_ui.py
```

### custom-uiディレクトリから実行
```bash
cd custom-ui
streamlit run credit_card_ui.py
```

アプリケーションはデフォルトで `http://localhost:8501` で起動します。

## 使用方法

### ダッシュボードの閲覧
1. アプリケーションを起動すると、自動的にダッシュボードが表示されます
2. 概要統計、グラフ、取引履歴を確認できます

### 取引のフィルタリング
1. 「カテゴリでフィルタ」ドロップダウンから希望のカテゴリを選択
2. テーブルが自動的に更新されます

### AIアシスタントの使用
1. ページ下部のチャット入力欄に質問を入力
2. 例:
   - "サブスクリプション料金は何ですか？"
   - "旅行費用を表示してください"
   - "最大の取引は何でしたか？"
   - "今月の食料品の支出はいくらですか？"
3. AIアシスタントがストリーミング形式で回答します

### チャット履歴のクリア
1. サイドバーの「チャット履歴をクリア」ボタンをクリック
2. 会話がリセットされます

## 技術詳細

### アーキテクチャ
- **フロントエンド**: Streamlit
- **データ可視化**: Plotly
- **データ処理**: Pandas
- **AI統合**: WxO Agent API (ストリーミング)

### データモデル
各トランザクションは以下の構造を持ちます:
```python
{
    "transaction_id": str,    # 一意のID
    "date": str,              # YYYY-MM-DD形式
    "merchant": str,          # 加盟店名
    "category": str,          # カテゴリ
    "amount": float,          # 金額
    "description": str,       # 説明
    "status": str            # ステータス
}
```

### セッション状態管理
- `st.session_state.messages`: チャット履歴
- `st.session_state.thread_id`: 会話スレッドID
- `st.session_state.transactions_df`: トランザクションデータ

### WxO Agent統合
アプリケーションは `WxOAgentAdapter` クラスを使用してWxO Agent APIと通信します:
- **メソッド**: `route_to_wxo_streaming(user_message, thread_id)`
- **機能**: ストリーミングレスポンス、会話の継続性
- **認証**: 自動的に管理

## トラブルシューティング

### インポートエラー
```
ModuleNotFoundError: No module named 'wxo'
```
**解決方法**: プロジェクトルートから実行していることを確認してください。

### 認証エラー
```
Authentication failed
```
**解決方法**: `.env` ファイルの認証情報を確認してください。

### ポートが使用中
```
Port 8501 is already in use
```
**解決方法**: 別のポートを指定して実行:
```bash
streamlit run custom-ui/credit_card_ui.py --server.port 8502
```

## カスタマイズ

### トランザクションデータの変更
`generate_mock_transactions()` 関数を編集して、独自のトランザクションデータを追加できます。

### スタイルのカスタマイズ
ファイル内の `st.markdown()` セクションでカスタムCSSを編集できます。

### 新しいグラフの追加
Plotlyを使用して追加のグラフを作成し、レイアウトに追加できます。

## 制限事項

- これはプロトタイプ実装です
- トランザクションデータはハードコードされています
- データベース永続化は実装されていません
- 実際の決済処理機能はありません

## 今後の改善案

- [ ] SQLiteデータベース統合
- [ ] トランザクションの追加/編集/削除機能
- [ ] PDFレポートのエクスポート
- [ ] より高度なフィルタリングオプション
- [ ] ユーザー認証
- [ ] マルチユーザーサポート

## ライセンス

このプロトタイプはデモンストレーション目的で作成されています。

## サポート

問題が発生した場合は、プロジェクトの管理者に連絡してください。

---

**作成者**: Bob AI Assistant  
**バージョン**: 1.0.0  
**最終更新**: 2026-04-07