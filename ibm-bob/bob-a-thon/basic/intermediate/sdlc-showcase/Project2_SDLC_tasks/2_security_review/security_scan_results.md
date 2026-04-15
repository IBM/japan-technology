# セキュリティ脆弱性分析レポート
## 対象アプリケーション: `bank1-savings/app_vulnerable.py`

**Date:** 2026-01-15  
**Analyst:** Bob (Security Assessment)  
**Total Vulnerabilities Found:** 20

---

## Executive Summary

この評価では、銀行アプリケーション内に **20 件の脆弱性** が確認されました。そのうち **5 件が Critical**、**5 件が High** であり、即時対応が必要です。複数の PCI-DSS 要件に違反しており、データ侵害、不正アクセス、不正取引につながる危険があります。

**Risk Level:** 🔴 **CRITICAL** - 本番運用不可

---

## Critical 脆弱性（即時対応）

### 1. Hardcoded Credentials (CWE-798)
**Location:** 25-30 行  
**Severity:** CRITICAL  
**PCI-DSS:** 8.2.1

```python
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "P@ssw0rd123"
API_KEY = "sk_live_51234567890abcdef"
DATABASE_PASSWORD = "db_secret_2024"
```

**Impact**
- システム全体の侵害
- 管理者権限の不正取得
- API キー流出による外部攻撃

**Remediation**
- すべての認証情報を環境変数へ移す
- Secrets Manager / Key Vault / Vault を使う
- ローテーションポリシーを導入する

### 2. Sensitive Data in Logs (CWE-532)
**Location:** 34-37 行  
**Severity:** CRITICAL  
**PCI-DSS:** 3.4

```python
def log_transaction(customer_id, card_number, amount):
    print(f"Transaction: Customer {customer_id}, Card: {card_number}, Amount: ${amount}")
```

**Impact**
- カード番号がログに残る
- 規制違反と漏えいリスク

**Remediation**
- PAN は last4 のみ表示
- セキュアログ基盤を使う
- ログ保存時暗号化とアクセス制御を行う

### 3. Unencrypted Sensitive Data Storage (CWE-311)
**Location:** 181-190 行  
**Severity:** CRITICAL  
**PCI-DSS:** 3.4

**Impact**
- SSN / カード番号の平文保存
- 大規模漏えい、なりすまし、規制罰金

**Remediation**
- AES-256-GCM 等で保存時暗号化
- tokenization
- 鍵は KMS / HSM で管理

### 4. SQL Injection Vulnerability (CWE-89)
**Location:** 303-326 行  
**Severity:** CRITICAL  
**PCI-DSS:** 6.5.1

```python
query = f"SELECT customer_id, name, email, ssn, card_number FROM customers WHERE name LIKE '%{search_term}%'"
cursor.execute(query)
```

**Impact**
- 顧客データ全件漏えい
- 改ざん / 削除
- 権限昇格

**Attack Example**
```text
search_term = "' OR '1'='1' --"
```

**Remediation**
```python
query = "SELECT customer_id, name, email FROM customers WHERE name LIKE ?"
cursor.execute(query, (f'%{search_term}%',))
```

### 5. Missing Authentication on Critical Endpoints (CWE-306)
**Location:** 329-342 行  
**Severity:** CRITICAL  
**PCI-DSS:** 7.1

**Impact**
- 顧客削除や管理操作を誰でも実行できる
- データ完全性の破壊

**Remediation**
- 管理者認証デコレータ
- トークン / セッション検証
- 監査ログ追加

---

## High 脆弱性

### 6. Password Exposure in API Response (CWE-200)
**Location:** 346-364 行  
**Severity:** HIGH

**Impact**
- パスワード漏えい
- アカウント乗っ取り

**Remediation**
- `admin_password` フィールドを削除
- API 応答へ機密情報を返さない

### 7. Weak Session Management (CWE-384)
**Location:** 346-364 行  
**Severity:** HIGH

```python
session_token = f"session_{username}_{datetime.now().strftime('%Y%m%d')}"
```

**Impact**
- 予測可能なトークン
- セッション固定 / 乗っ取り

**Remediation**
```python
import secrets
def generate_session_token():
    return secrets.token_urlsafe(32)
```

### 8. Missing Input Validation (CWE-20)
**Location:** 367-381 行  
**Severity:** HIGH

**Impact**
- マイナス残高
- 業務ロジック回避
- 不正操作

**Remediation**
- 型チェック
- 上限 / 下限制約
- 業務ルールに沿った検証

### 9. Insecure Direct Object Reference (CWE-639)
**Location:** 385-395 行  
**Severity:** HIGH  
**PCI-DSS:** 7.1

**Impact**
- 他人の顧客データへアクセス可能
- プライバシー違反

**Remediation**
- 認証必須化
- 所有者チェック
- 管理者権限例外のみ許可

### 10. Missing HTTPS/TLS (CWE-319)
**Location:** 397-399, 815 行  
**Severity:** HIGH  
**PCI-DSS:** 4.1

**Impact**
- MITM
- 認証情報窃取
- セッション乗っ取り

**Remediation**
- TLS 終端
- HSTS
- 本番用 WSGI + reverse proxy

---

## Medium 脆弱性

### 11. Debug Mode Enabled in Production (CWE-489)
- スタックトレース露出
- デバッグ情報の漏えい

### 12. Missing Rate Limiting (CWE-307)
- ブルートフォース
- Credential stuffing
- DoS

### 13. Incomplete Transaction Rollback
- 取引不整合
- 監査ギャップ

### 14. Missing CORS Configuration
- 不正なフロントエンドからの呼び出しリスク

### 15. Verbose Error Messages (CWE-209)
- 内部構造の露出
- 攻撃者へのヒント提供

---

## Low 脆弱性

### 16. Missing Security Headers
- CSP, X-Frame-Options, X-Content-Type-Options など不足

### 17. Unprotected Audit Log Endpoint
- 監査ログ閲覧への追加制御が必要

### 18. Import Inside Function
- パフォーマンスと可読性の悪化

### 19. Missing Request Size Limits
- 大きなリクエストによる負荷

### 20. No Input Sanitization for XSS (CWE-79)
- 表示系が増えた場合に XSS の踏み台になり得る

---

## PCI-DSS / プライバシー観点

### PCI-DSS 違反の主な論点
- 3.4: PAN / 機密データ保護不足
- 4.1: TLS 不足
- 6.5.1: SQL Injection
- 7.1: アクセス制御不足
- 8.2.1 / 8.2.3: 認証情報・セッション管理不足

### GDPR / Privacy の観点
- SSN やカード番号の過剰保持
- 権限制御なしでの顧客情報参照
- ログ経由の個人情報露出

---

## Remediation Roadmap

### Phase 1: Immediate（Week 1）- CRITICAL
- 認証情報を環境変数へ移行
- SQL Injection を修正
- ログのマスキング
- `app_vulnerable.py` の利用停止

### Phase 2: Critical（Week 2）- HIGH
- セッション管理強化
- 認証 / 認可追加
- HTTPS/TLS 導入

### Phase 3: Important（Weeks 3-4）- MEDIUM
- Rate limiting
- Rollback 強化
- エラーメッセージ最適化

### Phase 4: Enhancement（Month 2）- LOW
- セキュリティヘッダ
- リクエストサイズ制限
- XSS 対策の明文化

---

## Risk Assessment

### Current Risk Level: 🔴 CRITICAL

**主なリスク要因**
- 機密データを扱う銀行アプリである
- 管理系エンドポイントが無防備
- 平文保存とログ出力が同時に存在する
- SQL Injection により横断的被害が起きる

### Recommended Actions
- 本番配備を停止する
- Critical 項目を最優先で是正する
- Compliance 観点で再監査する
- 修正後に再テストする

---

## テスト推奨

### 必要なセキュリティテスト
- 認証 / 認可テスト
- SQL Injection テスト
- 機密情報露出チェック
- セッション管理テスト
- TLS / ヘッダ確認

### 推奨ツール
- 静的解析
- 依存脆弱性スキャン
- API セキュリティテスト
- コンテナスキャン

---

## Compliance Requirements

### PCI-DSS Certification Path
1. Critical 項目修正
2. 保存データ保護
3. アクセス制御強化
4. 監査証跡整備

### GDPR Compliance Path
1. 収集データの最小化
2. 保存データ暗号化
3. 閲覧権限の制御
4. ログから個人情報を排除

---

## Conclusion

`app_vulnerable.py` は教育用・デモ用の脆弱コードとしては有効ですが、運用コードと混在させるべきではありません。Bob を使うことで、これらの問題を短時間で一覧化し、CWE / PCI-DSS と紐づけ、 remediation の初動まで含めて支援できます。

### 要点
- 20 件の脆弱性、うち 10 件が Critical / High
- 最優先は SQL Injection、認証情報、認証欠如、平文保存
- 修正は 4 フェーズで段階的に進める
- 修正後は再スキャンと再監査が必須

---

## Appendix: References

- CWE Top 25
- PCI-DSS Requirements
- OWASP Top 10
- Secure Coding Guidelines
