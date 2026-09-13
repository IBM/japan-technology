# 🔒 包括的セキュリティレビュー報告書
## 金融サービス向けバンキングアプリケーション

**Review Date:** 2026-01-22  
**Application:** Banking Demo - Savings & Investment Banks  
**Reviewer:** Security Assessment Team  
**Severity Levels:** 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low

---

## 📋 Executive Summary

このレビューでは、金融サービス向けアプリケーション内に **10 件の Critical 脆弱性** と **35 件以上の SOX コンプライアンス問題** が存在することを確認しました。特に `app_vulnerable.py` のような意図的に脆弱なコードが本番相当コードと同居している点は、セキュリティとコンプライアンスの両面で重大なリスクです。

### リスク評価
- **Overall Risk Level:** 🔴 **CRITICAL**
- **PCI-DSS Compliance:** ❌ **NON-COMPLIANT**
- **SOX Compliance:** ❌ **NON-COMPLIANT**
- **Production Readiness:** ❌ **NOT READY**

### 指摘事項の集計

| Category | Critical | High | Medium | Low |
|----------|----------|------|--------|-----|
| Security Vulnerabilities | 10 | 5 | 3 | 2 |
| SOX Compliance Issues | 15 | 12 | 8 | 0 |
| **Total Issues** | **25** | **17** | **11** | **2** |

---

## 🔴 Critical なセキュリティ脆弱性

### 1. SQL Injection (CWE-89)
**Location:** `bank1-savings/app_vulnerable.py:309`  
**PCI-DSS:** Requirement 6.5.1  
**CVSS Score:** 9.8

```python
# VULNERABLE CODE
query = f"SELECT customer_id, name, email, ssn, card_number FROM customers WHERE name LIKE '%{search_term}%'"
cursor.execute(query)  # Direct string interpolation - SQL Injection!
```

**Impact**
- SSN やカード番号を含む顧客データ全体が漏えいし得る
- 金融レコードの改ざんや削除が可能
- 認証 / 認可の迂回につながる

**Exploit Example**
```bash
curl -X POST http://localhost:5000/api/search_customer \
  -H "Content-Type: application/json" \
  -d '{"search_term": "' OR '1'='1' UNION SELECT customer_id, name, email, ssn, card_number FROM customers--"}'
```

**Remediation**
```python
query = "SELECT customer_id, name, email FROM customers WHERE name LIKE ?"
cursor.execute(query, (f'%{search_term}%',))
```

### 2. Hardcoded Credentials (CWE-798)
**Location:** `bank1-savings/app_vulnerable.py:25-30`  
**PCI-DSS:** Requirement 8.2.1

```python
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "P@ssw0rd123"
API_KEY = "sk_live_51234567890abcdef"
DATABASE_PASSWORD = "db_secret_2024"
```

**Impact**
- コード参照者が管理者認証情報を取得できる
- API キーや DB パスワードが流出する
- ローテーション不能で長期的に危険

**Remediation**
```python
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
API_KEY = os.getenv('API_KEY')
```

### 3. Unencrypted Sensitive Data Storage (CWE-311)
**Location:** `bank1-savings/app_vulnerable.py:183-190`  
**PCI-DSS:** Requirement 3.4

**Impact**
- SSN や PAN を平文保存している
- データ侵害時の被害が極めて大きい
- 規制罰金・法的責任・信用失墜につながる

**Remediation**
- 保存時暗号化（AES-256-GCM など）
- カード番号は tokenization または last4 のみ保持
- 鍵は KMS / Vault / HSM で管理

### 4. Sensitive Data in Logs (CWE-532)
**Location:** `bank1-savings/app_vulnerable.py:34-37`  
**PCI-DSS:** Requirement 3.4

**Impact**
- カード番号がログに残る
- 集約ログや障害調査経路から漏えいし得る
- PCI-DSS 違反となる

**Remediation**
```python
masked_card = f"****-****-****-{card_number[-4:]}"
```

### 5. Missing Authentication on Critical Endpoints (CWE-306)
**Location:** `bank1-savings/app_vulnerable.py:329-342, 385-395`

**Impact**
- 誰でも顧客削除や詳細参照を実行できる
- 管理機能が公開状態になっている
- データ喪失や不正操作が可能

**Remediation**
- 管理者認証を必須化
- セッション / トークン検証を追加
- 操作ログを残す

### 6. Insecure Direct Object Reference (IDOR) (CWE-639)
**Location:** `bank1-savings/app_vulnerable.py:385-395`  
**PCI-DSS:** Requirement 7.1

**Impact**
- `customer_id` を変えるだけで他人のデータにアクセスできる
- プライバシー侵害、規制違反につながる

**Remediation**
- リソース所有者チェック
- 管理者例外を除き本人データのみに制限

### 7. Weak Session Management (CWE-384)
**Location:** `bank1-savings/app_vulnerable.py:346-364`

**Impact**
- 予測可能なセッショントークン
- セッション固定 / 乗っ取りの危険

**Remediation**
- `secrets.token_urlsafe()` などの安全な乱数を使う
- 権限昇格時にセッションローテーションを行う
- 有効期限とサーバー側保存を導入する

---

## 🟠 SOX コンプライアンス問題

### 主な Critical SOX 指摘（`app_sox_issues.py` より）

#### 1. 職務分掌の欠如 - SOX Section 404
- 起票者と承認者が分離されていない
- 単独ユーザーで高リスク操作を完結できる

#### 2. 取引不変性違反 - SOX Section 302
- 取引が更新・削除できる設計
- 正しい訂正履歴が残らない

#### 3. 監査ログの不備 - SOX Section 404
- 誰が・いつ・何をしたかが十分に追えない
- 監査証跡として不十分

#### 4. Maker-Checker の欠如 - SOX Section 404
- 高額取引や重要操作にダブルチェックがない

#### 5. アクセス制御ログの欠如 - SOX Section 404
- 誰が管理機能へアクセスしたかを十分に追跡できない

**推奨対応**
- RBAC の導入
- 取引の immutability 確保
- reversal transaction による訂正
- maker-checker ワークフロー
- アクセス監査ログの強化

---

## 🟡 追加の懸念事項

### Frontend 側
- コンソール出力に機密情報が残る可能性
- CSRF 対策が見当たらない

### Dependencies
- 依存パッケージに既知脆弱性が含まれる可能性
- 継続的な SCA（Software Composition Analysis）が必要

### Docker
- `USER` 指定がなく root 実行になっている
- debug 前提のままイメージが使われるおそれがある

---

## 📊 コンプライアンスマトリクス

### PCI-DSS

| 項目 | 状態 |
|------|------|
| カード番号保護 | ❌ 不適合 |
| 認証・認可 | ❌ 不適合 |
| 暗号化 | ❌ 不適合 |
| 監査ログ | ⚠ 部分的 |
| セキュア開発 | ❌ 不適合 |

### SOX

| 項目 | 状態 |
|------|------|
| 職務分掌 | ❌ 不適合 |
| 取引不変性 | ❌ 不適合 |
| 監査証跡 | ⚠ 不十分 |
| 承認フロー | ❌ 不適合 |
| アクセス統制 | ⚠ 不十分 |

---

## 🎯 Remediation Roadmap

### Phase 1: Critical Security Fixes（Week 1-2）
- `app_vulnerable.py` の使用停止
- 認証情報を環境変数へ移行
- SQL Injection を修正
- 機密データのログ出力を停止

### Phase 2: Authentication & Authorization（Week 3-4）
- セッション管理の強化
- 管理者エンドポイント保護
- IDOR 対策

### Phase 3: Data Protection（Week 5-6）
- 保存時暗号化
- マスキング / tokenization
- 秘密情報管理の仕組み導入

### Phase 4: SOX Compliance（Week 7-10）
- 職務分掌
- maker-checker
- immutable transaction
- 監査ログ強化

### Phase 5: Security Hardening（Week 11-12）
- TLS 終端
- root 実行の排除
- dependency scan / policy enforcement

---

## 🔧 すぐに必要な対応

### 1. `app_vulnerable.py` を使わない
```bash
# Rename or delete vulnerable file
# Use app.py instead
```

### 2. 環境変数の導入
```bash
# Create .env file (never commit to git)
```

### 3. HTTPS/TLS を有効化
```bash
# Generate self-signed certificate for development
```

### 4. Docker 設定を見直す
```bash
# Add non-root user
# Use production WSGI server
```

---

## 📈 推奨モニタリング

- 認証失敗回数
- 機密エンドポイントへのアクセス
- 想定外クエリやエラー率
- 監査ログ整合性
- 脆弱性スキャン結果の推移

## 🎓 トレーニング推奨

### 開発チーム向け
- セキュアコーディング
- PCI-DSS 基礎
- SQL Injection / Auth / Session の実践対策

### 運用チーム向け
- 秘密情報管理
- TLS / 証明書管理
- 監査ログ保全

---

## ✅ 結論

このアプリケーションは現状のままでは本番投入すべきではありません。特に SQL Injection、ハードコード認証情報、平文保存、認証欠如は即時是正が必要です。Bob を使えば、これらの問題を IDE 内で早期に可視化し、修正案まで含めてチームへ返せるため、 remediation の初速を大きく上げられます。

### Key Takeaways
- 重大脆弱性が多く、PCI-DSS / SOX ともに不適合
- `app_vulnerable.py` はデモ専用に隔離すべき
- 認証、暗号化、監査ログ、職務分掌が優先テーマ
- Bob は検出・説明・修正支援の 3 点で有効

### Recommendation
- 本番利用は停止
- Phase 1 の Critical Fix を最優先
- セキュリティと compliance の両面で運用ルールを整備
