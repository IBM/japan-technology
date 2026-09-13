# Bank 1 - Savings Bank フロントエンド

## React + Material-UI フロントエンド

React と Material-UI で構築された、モダンで業務利用を意識したバンキング UI です。

## 機能

- 📊 **Dashboard** - 残高カードを含む口座概要
- 💳 **Transactions** - 絞り込み付きの詳細な取引履歴
- 💸 **Transfers** - Investment Bank への簡単な銀行間振込
- 📈 **Analytics** - 対話的なチャートによる支出分析

## 技術スタック

- **React 18** - Hooks を使ったモダン React
- **Material-UI (MUI)** - 業務アプリ向け UI コンポーネント
- **Recharts** - レスポンシブなチャート表示
- **React Router** - クライアントサイドルーティング
- **Axios** - API 呼び出し用 HTTP クライアント
- **Vite** - 高速なビルドツールと開発サーバー

## 開発

### 前提条件

- Node.js 18+ と npm
- ポート 5001 で動作する Bank 1 Flask バックエンド

### 依存関係のインストール

```bash
npm install
```

### 開発サーバーの起動

```bash
npm run dev
```

アプリは `http://localhost:3000` で利用できます。

Vite の開発サーバーは、API リクエストを `http://localhost:5001` の Flask バックエンドへプロキシします。

### 本番用ビルド

```bash
npm run build
```

最適化された本番ビルドが `dist/` ディレクトリに生成されます。

### 本番ビルドのプレビュー

```bash
npm run preview
```

## プロジェクト構成

```text
frontend/
├── src/
│   ├── components/          # React components
│   │   ├── Dashboard.jsx    # Main dashboard
│   │   ├── TransactionList.jsx
│   │   ├── TransferForm.jsx
│   │   └── Analytics.jsx
│   ├── services/
│   │   └── api.js          # API service layer
│   ├── App.jsx             # Main app with routing
│   └── main.jsx            # Entry point
├── index.html              # HTML template
├── package.json            # Dependencies
└── vite.config.js          # Vite configuration
```

## API 連携

フロントエンドは API サービスレイヤー（`src/services/api.js`）を通して Flask バックエンドと通信します。

開発中の API 呼び出しは、Vite によって次のようにプロキシされます。

- `/api/*` → `http://localhost:5001/api/*`
- `/health` → `http://localhost:5001/health`

## 利用可能なルート

- `/dashboard` - 口座概要
- `/transactions` - 取引履歴
- `/transfer` - 振込
- `/analytics` - 支出分析

## カスタマイズ

### テーマ

Material-UI のテーマは `src/App.jsx` で定義されています。Savings Bank のブランドに合わせ、プライマリカラーには緑（`#2E7D32`）を使っています。

### API エンドポイント

バックエンド API の接続先を変える場合は、`vite.config.js` を更新してください。

```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://your-backend-url',
      changeOrigin: true,
    }
  }
}
```

## デプロイ

本番ビルドは次の方法で配信できます。

1. Flask（静的ファイル配信）
2. Nginx
3. 任意の静的ファイルサーバー

Flask バックエンドは、`dist/` ディレクトリに生成された React ビルドを配信できるよう設定されています。
