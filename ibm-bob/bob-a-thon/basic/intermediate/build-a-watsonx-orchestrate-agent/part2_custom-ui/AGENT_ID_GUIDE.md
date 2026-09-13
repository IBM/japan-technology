# WxO Agent ID 取得ガイド

このガイドでは、watsonx Orchestrate (WxO) のAgent IDを取得し、`.env`ファイルに正しく設定する方法を説明します。

## 📋 前提条件

- watsonx Orchestrateのアカウントとアクセス権限
- デプロイ済みのAgent（credit_card_management_agent）

## 🔍 Agent IDの取得方法

### 方法1: WxO Orchestrate UIから取得

1. **watsonx Orchestrateにログイン**
   - ブラウザで watsonx Orchestrate にアクセス
   - 認証情報でログイン

2. **Agentビルダーを開く**
   - 左側のメニューから「Agent builder」または「エージェント」を選択
   - デプロイ済みのAgentリストが表示されます

3. **対象のAgentを選択**
   - `credit_card_management_agent` を探してクリック

4. **Agent IDを確認**
   - Agent詳細ページのURLを確認します
   - URLの形式: `https://{region}.dl.watson-orchestrate.ibm.com/build/agent/edit/{AGENT_ID}`
   - 例: `https://ap-southeast-1.dl.watson-orchestrate.ibm.com/build/agent/edit/001cf13e-46cc-41ff-b993-9e9e96934e42`
   - この場合、Agent IDは: `001cf13e-46cc-41ff-b993-9e9e96934e42`

5. **API URLを構築**
   - 以下の形式でAPI URLを作成します：
   ```
   https://api.{region}.dl.watson-orchestrate.ibm.com/instances/{instance_id}/v1/agents/{agent_id}/generation_stream
   ```

### 方法2: デプロイスクリプトの出力から取得

`credit-card-agent/deploy.sh`を実行した際の出力を確認します：

```bash
cd credit-card-agent
./deploy.sh
```

デプロイが成功すると、以下のような出力が表示されます：

```
✅ Agent deployed successfully!
Agent ID: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
Agent URL: https://...
```

この`Agent ID`をコピーします。

### 方法3: WxO CLIを使用（もし利用可能な場合）

```bash
# Agentリストを取得
wxo agent list

# 特定のAgentの詳細を取得
wxo agent get credit_card_management_agent
```

## ⚙️ .envファイルの設定

### 現在の設定（不完全）

```env
AGENT_URL = "https://api.ap-southeast-1.dl.watson-orchestrate.ibm.com/instances/20250508-0745-2006-9056-1f0c833127e3"
```

### 正しい設定

取得したAgent IDを使用して、以下の形式で設定します：

```env
AGENT_URL = "https://api.ap-southeast-1.dl.watson-orchestrate.ibm.com/instances/20250508-0745-2006-9056-1f0c833127e3/v1/agents/{YOUR_AGENT_ID}/generation_stream"
```

**例**（Agent IDが`001cf13e-46cc-41ff-b993-9e9e96934e42`の場合）：

```env
AGENT_URL = "https://api.ap-southeast-1.dl.watson-orchestrate.ibm.com/instances/20250508-0745-2006-9056-1f0c833127e3/v1/agents/001cf13e-46cc-41ff-b993-9e9e96934e42/generation_stream"
```

## 🔧 設定手順

1. **プロジェクトルートの`.env`ファイルを開く**
   ```bash
   cd /Users/aa469668/0_CSE/Bob_wxO_実行用0406
   nano .env
   # または
   code .env
   ```

2. **AGENT_URLを更新**
   - 上記の正しい形式でURLを設定
   - Agent IDを実際の値に置き換える

3. **ファイルを保存**

4. **Web UIを再起動**
   ```bash
   streamlit run custom-ui/credit_card_ui.py
   ```

## ✅ 動作確認

1. ブラウザで http://localhost:8501 を開く
2. ページ下部のチャット入力欄に質問を入力
   - 例: "サブスクリプション料金は何ですか？"
3. エラーなくAIが応答すれば成功です

## 🐛 トラブルシューティング

### エラー: 404 Not Found

**原因**: Agent IDが正しくない、またはAgentが存在しない

**解決方法**:
1. WxO Orchestrate UIでAgent IDを再確認
2. Agentがデプロイされているか確認
3. `.env`ファイルのURLが正しい形式か確認

### エラー: 401 Unauthorized

**原因**: 認証情報が正しくない

**解決方法**:
1. `.env`ファイルの`WXO_API_KEY`を確認
2. API Keyが有効期限内か確認
3. 必要に応じて新しいAPI Keyを生成

### エラー: 403 Forbidden

**原因**: Agentへのアクセス権限がない

**解決方法**:
1. WxO Orchestrateでアクセス権限を確認
2. 必要に応じて管理者に権限を依頼

## 📝 完全な.envファイルの例

```env
# Agent API URL（Agent IDを含む完全なURL）
AGENT_URL = "https://api.ap-southeast-1.dl.watson-orchestrate.ibm.com/instances/20250508-0745-2006-9056-1f0c833127e3/v1/agents/001cf13e-46cc-41ff-b993-9e9e96934e42/generation_stream"

# API Key
WXO_API_KEY = "azE6dXNyXzJmYjY0NjVhLTUxMDUtM2Y4Yy1iYWZjLTkyY2E4NzM3Y2E5ZTpOcTBja241b1dtaEhXZXNLU29UN2E5Q0dLaWdHanBITkhTYTVveDF2MzRnPTpyNlhF"

# Cloud Provider
CLOUD_PROVIDER="aws"

# 認証エンドポイント
IBM_AUTH_ENDPOINT="https://iam.cloud.ibm.com/identity/token"
AWS_AUTH_ENDPOINT="https://iam.platform.saas.ibm.com/siusermgr/api/1.0/apikeys/token"
```

## 🔗 関連リンク

- [watsonx Orchestrate Documentation](https://www.ibm.com/docs/en/watsonx/watson-orchestrate)
- [Agent Builder Guide](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/agent-builder)

## 💡 ヒント

- Agent IDは通常、UUID形式（8-4-4-4-12の文字列）です
- 複数のAgentがある場合は、正しいAgentのIDを使用していることを確認してください
- `.env`ファイルを変更した後は、必ずアプリケーションを再起動してください

---

**作成日**: 2026-04-07  
**最終更新**: 2026-04-07