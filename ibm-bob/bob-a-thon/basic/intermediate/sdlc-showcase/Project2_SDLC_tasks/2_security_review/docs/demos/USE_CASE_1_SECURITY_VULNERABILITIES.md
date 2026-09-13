# Use Case 1: Security Vulnerability Detection Demo Guide

## 🎯 デモ概要

**目的**: 銀行アプリに対して、Bob がセキュリティ脆弱性、CWE 参照、PCI-DSS コンプライアンス違反をどのように特定できるかを示す。  
**所要時間**: 15〜20 分  
**対象読者**: セキュリティチーム、コンプライアンス担当、開発マネージャー

---

## 📋 デモ前セットアップ

### 前提条件
1. `bank1-savings/app_vulnerable.py`（脆弱版）が存在している
2. 比較用に元の `bank1-savings/app.py` がある
3. IDE 上で Bob AI Coding Assistant が有効になっている

### 準備手順
```bash
# 1. Navigate to the banking demo directory
cd banking-demo

# 2. Backup the original secure version
cp bank1-savings/app.py bank1-savings/app_secure.py

# 3. Replace with vulnerable version for demo
cp bank1-savings/app_vulnerable.py bank1-savings/app.py

# 4. Open the file in your IDE
code bank1-savings/app.py
```

---

## 🎤 デモ進行と話すポイント

### Part 1: 導入（2 分）

**話すポイント**
- 「今日は、Bob が銀行アプリのセキュリティ脆弱性をどう見つけるかを紹介します」
- 「この Flask ベースのアプリは、SSN やカード番号のような機密データを扱います」
- 「Bob は CWE（Common Weakness Enumeration）と PCI-DSS の観点で問題を洗い出せます」
- 「金融機関にとって、こうした検出を開発中に行えることは非常に重要です」

### Part 2: 包括的セキュリティスキャン（5 分）

**Bob へのプロンプト**
```text
Please perform a comprehensive security audit of this banking application (app.py). 
Identify all security vulnerabilities with:
1. CWE (Common Weakness Enumeration) references
2. PCI-DSS compliance violations
3. Severity ratings (Critical, High, Medium, Low)
4. Specific line numbers where issues occur
5. Potential impact of each vulnerability

Focus on:
- Hardcoded credentials
- SQL injection vulnerabilities
- Sensitive data exposure
- Missing authentication
- Weak session management
- Input validation issues
- Insecure direct object references
- Missing encryption
```

**期待される Bob の反応**
Bob は、おおむね次のような主要脆弱性を挙げるはずです。

1. **CWE-798: Hardcoded Credentials**（18〜21 行付近）
   - Severity: CRITICAL
   - PCI-DSS: Requirement 8.2.1

2. **CWE-532: Sensitive Information in Logs**（24〜27 行付近）
   - Severity: HIGH
   - PCI-DSS: Requirement 3.4

3. **CWE-89: SQL Injection**（330〜350 行付近）
   - Severity: CRITICAL
   - PCI-DSS: Requirement 6.5.1

4. **CWE-311: Missing Encryption**（150〜165 行付近）
   - Severity: CRITICAL
   - PCI-DSS: Requirement 3.4

5. **CWE-306: Missing Authentication**（360〜375 行付近）
   - Severity: CRITICAL
   - PCI-DSS: Requirement 8.1

**話すポイント**
- 「Bob は単に脆弱性を列挙するだけでなく、CWE 参照も出せます」
- 「各指摘がどの PCI-DSS 要件に違反するかも示せます」
- 「重大度付きなので、修正優先度づけがしやすいです」
- 「行番号があるので、開発者がすぐ該当箇所を見つけられます」

### Part 3: SQL Injection の深掘り（4 分）

**Bob へのプロンプト**
```text
Focus on the SQL injection vulnerability in the search_customer endpoint. 
Explain:
1. How this vulnerability can be exploited
2. What data could be compromised
3. Provide a specific exploit example
4. Show me the secure code fix with parameterized queries
```

**期待される Bob の反応**
- 文字列連結によるクエリ生成が問題だと説明する
- `' OR '1'='1` のような入力でフィルタを迂回できると示す
- SSN やカード番号を含む顧客情報全体が漏えいし得ると説明する
- パラメータ化クエリを使った安全な修正例を提示する

**話すポイント**
- 「SQL Injection は OWASP Top 10 に入る代表的な脆弱性です」
- 「銀行文脈では、顧客の金融データ全体が漏れる可能性があります」
- 「Bob は問題の説明だけでなく、修正コードまで返せます」
- 「そのまま remediation を加速できるのが強みです」

### Part 4: PCI-DSS コンプライアンス観点（4 分）

**Bob へのプロンプト**
```text
Generate a PCI-DSS compliance report for this application. 
For each violation, specify:
1. The PCI-DSS requirement number
2. What data is at risk
3. The business impact
4. Remediation priority
5. Estimated effort to fix

Create a summary table of all PCI-DSS violations found.
```

**期待される Bob の反応**
- 複数の PCI-DSS 違反を整理したレポート
- データリスクとビジネス影響の説明
- 優先度付きの修正計画
- サマリーテーブル

**話すポイント**
- 「PCI-DSS はカード情報を扱う組織では必須です」
- 「違反すると 1 件あたり最大 50 万ドル規模の罰金になり得ます」
- 「Bob は違反を早期に見つけ、継続的な compliance を支援できます」
- 「優先度付きの remediation plan によって、対応計画が立てやすくなります」

### Part 5: 自動 remediation（5 分）

**Bob へのプロンプト**
```text
Fix the top 3 critical vulnerabilities:
1. Remove hardcoded credentials and use environment variables
2. Fix the SQL injection in search_customer endpoint
3. Add encryption for sensitive data (SSN, card numbers)

Apply the fixes and show me the diff of changes.
```

**期待される Bob の反応**
- ハードコードされた認証情報を `os.getenv()` に置き換える
- SQL Injection をパラメータ化クエリへ修正する
- 機密データ向けの暗号化ロジックを追加する
- 差分を見やすく表示する

**話すポイント**
- 「Bob は検出だけでなく、修正までできます」
- 「差分表示があるので、そのままコードレビューに載せやすいです」
- 「発見から修正までの時間を大きく短縮できます」
- 「開発者はコミット前に内容をレビューして承認できます」

---

## 🎯 見せるべき価値

### Bob が提供するもの

✅ **包括的なセキュリティ分析**
- 10 種類以上の脆弱性パターンを検出
- 各問題に CWE 参照を付与
- PCI-DSS への対応付け
- 重大度評価

✅ **実行可能なインサイト**
- 具体的な行番号
- 攻撃シナリオ
- ビジネス影響の説明
- 修正指針

✅ **自動 remediation**
- セキュアなコード修正の生成
- ベストプラクティスの適用
- 差分の提示
- コード品質の維持

✅ **コンプライアンス支援**
- PCI-DSS 要件への対応付け
- 監査向けの説明材料
- 優先度付き修正計画
- リスク評価

---

## 📊 強調したい指標

**Time Savings**
- 手作業のセキュリティ監査: 4〜8 時間
- Bob を使った監査: 15〜30 分
- **時間削減: 85〜95%**

**Coverage**
- 手作業レビュー: 60〜70%
- Bob レビュー: 95% 以上
- **検出率改善: 25〜35%**

**Remediation Speed**
- 手作業での修正案作成: 脆弱性 1 件あたり 2〜4 時間
- Bob による修正生成: 1 件あたり 5〜10 分
- **12〜48 倍高速**

---

## 🔄 代替デモフロー

### セキュリティチーム向け
脆弱性検出の深さと CWE 対応を中心に見せる

### コンプライアンス担当向け
PCI-DSS レポートと監査証跡を中心に見せる

### 開発者向け
自動 remediation とコード品質維持を中心に見せる

### マネジメント向け
時間削減、リスク削減、ROI を中心に見せる

---

## ❓ 想定 Q&A

**Q: Bob はゼロデイ脆弱性も検出できますか？**  
A: 既知パターンや危険な設計傾向の検出が得意です。ゼロデイそのものを保証するものではありませんが、疑わしいコードパターンを洗い出して人のレビュー対象を絞れます。

**Q: 従来の SAST と何が違いますか？**  
A: Bob は IDE の中で文脈を理解し、自然言語で説明し、修正案まで返せます。従来の SAST は別工程のスキャンになることが多いです。

**Q: 誤検知はどう扱いますか？**  
A: コードの意図や前提を追加で Bob に伝えることで、分析を絞り込めます。設計上意図されたものと実際の欠陥を区別しやすくなります。

**Q: パフォーマンス影響はありますか？**  
A: 解析はオンデマンドで実行するため、開発環境に常時負荷を与える前提ではありません。

**Q: 既存のセキュリティツールと併用できますか？**  
A: できます。Bob は IDE での早期検出を担い、SAST / DAST など既存のパイプラインと補完関係になります。

---

## 🎬 デモ締め

### まとめ
1. Bob は数分で 10 件以上の重大脆弱性を特定できる
2. 各指摘に CWE と PCI-DSS の対応付けを付けられる
3. セキュアな修正コードを自動生成できる
4. 手作業の監査より 85〜95% 速い
5. 脆弱性検出率も向上する

### Call to Action
- 「Bob はセキュリティをボトルネックではなく加速要素に変えます」
- 「IDE 内で早く見つけることで、本番流出を防げます」
- 「自動 remediation により、セキュリティチームの負荷を下げられます」
- 「Compliance を定期作業ではなく継続活動にできます」

### 次のステップ
1. セキュリティチームで Pilot を実施する
2. コードレビュー工程へ組み込む
3. セキュリティスキャンの運用ルールを決める
4. 時間削減と脆弱性削減を測定する

---

## 📝 デモ後の片付け

```bash
# Restore the secure version
cp bank1-savings/app_secure.py bank1-savings/app.py

# Remove vulnerable version
rm bank1-savings/app_vulnerable.py

# Verify restoration
git diff bank1-savings/app.py
```

---

## 📚 追加リソース

- [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/)
- [PCI-DSS Requirements](https://www.pcisecuritystandards.org/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Bob Security Best Practices Guide](../reference/SECURITY_BEST_PRACTICES.md)

---

**Demo Prepared By**: IBM Bob Team  
**Last Updated**: 2024  
**Version**: 1.0
