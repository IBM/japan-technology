# Bank1-Savings API ユニットテスト

Bank1-Savings のすべての API エンドポイントを対象にした包括的なユニットテストです。

## テストカバレッジ

### テスト対象の API エンドポイント
- ✅ `/api/balance` - 残高取得
- ✅ `/api/transactions` - 取引履歴
- ✅ `/api/analytics` - 支出分析
- ✅ `/api/transfer` - Bank2 への振込
- ✅ `/api/receive_transfer` - Bank2 からの受取
- ✅ `/api/audit_log` - 監査ログ
- ✅ `/health` - ヘルスチェック

### テストカテゴリ

#### 1. Balance エンドポイントテスト（5件）
- 残高取得の成功ケース
- `customer_id` 未指定時のバリデーション
- 無効な顧客のハンドリング
- すべてのデモ顧客の検証
- 残高データ構造の検証

#### 2. Transaction エンドポイントテスト（4件）
- 取引取得の成功ケース
- カスタム `limit` パラメータ
- `customer_id` 未指定時のバリデーション
- 既定の `limit` の挙動

#### 3. Analytics エンドポイントテスト（2件）
- 分析生成の成功ケース
- `customer_id` 未指定時のバリデーション

#### 4. Transfer エンドポイントテスト（4件）
- Bank2 をモックした振込成功ケース
- 必須パラメータ不足時のバリデーション
- 無効な金額（負数、0）のハンドリング
- 残高不足時のバリデーション

#### 5. Receive Transfer テスト（3件）
- 受取成功ケース
- 必須パラメータ不足時のバリデーション
- 無効な金額のハンドリング

#### 6. Audit Log テスト（1件）
- 監査ログ取得と構造の確認

#### 7. Health Check テスト（1件）
- ヘルスエンドポイントの検証

#### 8. Integration テスト（2件）
- 振込のフルワークフロー
- 同時残高チェック

#### 9. Database Function テスト（2件）
- クエリ実行の検証
- 無効な SQL のハンドリング

**合計: 24 件の包括的なテスト**

---

## テストの実行方法

### Option 1: unittest を使う（標準ライブラリ）

```bash
# bank1-savings ディレクトリへ移動
cd bank1-savings

# 詳細出力付きですべてのテストを実行
python test_api.py

# または unittest を直接実行
python -m unittest test_api -v
```

### Option 2: pytest を使う（推奨）

```bash
# pytest が未インストールなら追加
pip install pytest pytest-cov

# pytest でテストを実行
pytest test_api.py -v

# カバレッジレポート付きで実行
pytest test_api.py --cov=app --cov-report=html

# 特定のテストクラスだけ実行
pytest test_api.py::Bank1APITestCase -v

# 特定のテストメソッドだけ実行
pytest test_api.py::Bank1APITestCase::test_get_balance_success -v
```

### Option 3: Docker を使う

```bash
# テスト用イメージをビルド
docker build -t bank1-tests -f Dockerfile.test .

# コンテナ内でテストを実行
docker run --rm bank1-tests
```

---

## テスト出力例

```
test_full_transfer_workflow (test_api.Bank1APITestCase) ... ok
test_get_analytics_missing_customer_id (test_api.Bank1APITestCase) ... ok
test_get_analytics_success (test_api.Bank1APITestCase) ... ok
test_get_audit_log (test_api.Bank1APITestCase) ... ok
test_get_balance_all_customers (test_api.Bank1APITestCase) ... ok
test_get_balance_invalid_customer (test_api.Bank1APITestCase) ... ok
test_get_balance_missing_customer_id (test_api.Bank1APITestCase) ... ok
test_get_balance_success (test_api.Bank1APITestCase) ... ok
test_get_transactions_default_limit (test_api.Bank1APITestCase) ... ok
test_get_transactions_missing_customer_id (test_api.Bank1APITestCase) ... ok
test_get_transactions_success (test_api.Bank1APITestCase) ... ok
test_get_transactions_with_limit (test_api.Bank1APITestCase) ... ok
test_health_check (test_api.Bank1APITestCase) ... ok
test_receive_transfer_invalid_amount (test_api.Bank1APITestCase) ... ok
test_receive_transfer_missing_parameters (test_api.Bank1APITestCase) ... ok
test_receive_transfer_success (test_api.Bank1APITestCase) ... ok
test_transfer_insufficient_balance (test_api.Bank1APITestCase) ... ok
test_transfer_invalid_amount (test_api.Bank1APITestCase) ... ok
test_transfer_missing_parameters (test_api.Bank1APITestCase) ... ok
test_transfer_success (test_api.Bank1APITestCase) ... ok

======================================================================
TEST SUMMARY
======================================================================
Tests run: 24
Successes: 24
Failures: 0
Errors: 0
======================================================================
```

---

## テストの特徴

### 1. 分離されたテスト環境
- テスト実行ごとに一時 SQLite データベースを使う
- 監査ログファイルも別に用意する
- 本番データに影響しない

### 2. 外部依存のモック化
- Bank2 API への呼び出しは `unittest.mock` でモック化
- テスト中に実際の HTTP リクエストを送らない
- 再現性のある安定したテストになる

### 3. 包括的な検証
- HTTP ステータスコード
- レスポンス JSON の構造
- データ整合性
- エラーハンドリング
- ビジネスロジックの妥当性

### 4. 統合テスト
- フルワークフローテスト（残高確認 → 振込 → 結果検証）
- 同時リクエストのハンドリング
- 取引記録の検証

---

## 新しいテストの追加方法

新しいテストを追加するときは、次のパターンに従ってください。

```python
def test_your_feature(self):
    """Test description"""
    # Arrange: Set up test data
    customer_id = 1
    
    # Act: Make API call
    response = self.client.post('/api/endpoint',
                               data=json.dumps({'customer_id': customer_id}),
                               content_type='application/json')
    
    # Assert: Verify results
    self.assertEqual(response.status_code, 200)
    data = json.loads(response.data)
    self.assertTrue(data['success'])
```

---

## 継続的インテグレーション

### GitHub Actions の例

```yaml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov
      - name: Run tests
        run: pytest test_api.py --cov=app
```

---

## トラブルシューティング

### 問題: データベースエラーでテストが失敗する
**対処**: ほかのインスタンスが同じデータベースファイルを使っていないことを確認してください。テストは一時データベースを使います。

### 問題: Import エラーが出る
**対処**: `bank1-savings` ディレクトリにいることと、依存関係がすべて入っていることを確認してください。
```bash
pip install -r requirements.txt
```

### 問題: Bank2 呼び出しのモックが効かない
**対処**: `unittest.mock` が正しく import されていること、`patch` デコレータが正しく適用されていることを確認してください。

---

## テスト保守

- コード変更をコミットする前にテストを実行する
- 新しい API エンドポイントを追加したらテストも更新する
- テストカバレッジ 80% 以上を維持する
- 外部 API が変わったらモックも見直す

---

## カバレッジレポート

詳細なカバレッジレポートを作成するには、次を実行してください。

```bash
# Install coverage tool
pip install coverage

# Run tests with coverage
coverage run -m unittest test_api

# Generate HTML report
coverage html

# Open report in browser
open htmlcov/index.html
```

---

## ベストプラクティス

1. **テスト分離**: 各テストは独立しているべき
2. **明確な命名**: テスト名は何を検証するかが分かるようにする
3. **AAA パターン**: Arrange, Act, Assert
4. **外部呼び出しはモックする**: 実際の HTTP リクエストを送らない
5. **境界条件もテストする**: 不正入力や境界値を確認する
6. **エラーハンドリングを検証する**: 成功系と失敗系の両方をテストする

---

## 問い合わせ

テストに関する質問や問題があれば、メインのアプリケーションドキュメントを参照するか、リポジトリに issue を作成してください。
