# Bob AI Coding Assistant - Banking Demo ユースケース集

## 🎯 概要

このディレクトリには、エンタープライズの銀行チームに Bob の能力を紹介するためのデモ資料がまとまっています。各ユースケースには次が含まれます。

- **Demo Guide**: 話すポイント付きの進行スクリプト
- **Executive Summary**: 経営層向けのビジネス価値と ROI の要約
- **Code Examples**: デモ用に意図的に問題を含めたコード
- **Remediation Plans**: 修正方針または修正例

---

## 📚 ユースケース一覧

### [Use Case 1: Security Vulnerability Detection](USE_CASE_1_SECURITY_VULNERABILITIES.md)

**対象読者**: セキュリティチーム、コンプライアンス担当、開発マネージャー  
**所要時間**: 15〜20 分

**見せられる能力**
- CWE 参照付きで 10 件以上の脆弱性を特定
- 検出結果を PCI-DSS 要件に対応付け
- セキュアな修正コードを自動生成
- 包括的なセキュリティ監査レポートを作成

**ビジネス価値**
- セキュリティ監査時間を 85〜95% 削減
- 脆弱性修正を 12〜48 倍高速化
- 年間 99.1 万ドル相当の効果（20 名規模チーム）
- 初年度 ROI 400〜800%

**関連ファイル**
- Demo Guide: [`USE_CASE_1_SECURITY_VULNERABILITIES.md`](USE_CASE_1_SECURITY_VULNERABILITIES.md)
- Executive Summary: [`USE_CASE_1_EXECUTIVE_SUMMARY.md`](USE_CASE_1_EXECUTIVE_SUMMARY.md)
- Vulnerable Code: [`../../bank1-savings/app_vulnerable.py`](../../bank1-savings/app_vulnerable.py)

**主な脆弱性例**
- CWE-798: ハードコードされた認証情報
- CWE-89: SQL Injection
- CWE-311: 暗号化不足
- CWE-306: 認証欠如
- CWE-532: ログへの機密情報出力

---

### [Use Case 2: Legacy Code Modernization](USE_CASE_2_LEGACY_MODERNIZATION.md)

**対象読者**: 開発マネージャー、アーキテクト、技術リード  
**所要時間**: 20〜25 分

**見せられる能力**
- レガシーな実装パターン / アンチパターンを 25 件以上分析
- 非推奨ライブラリと CVE を洗い出す
- コネクションプーリングや async I/O を提案
- Java 8 から Java 21 への近代化を支援

**ビジネス価値**
- モダナイゼーション期間を 90% 短縮
- プロジェクトコストを 85% 削減
- 性能を最大 500% 改善
- アプリ 1 本あたり年間 218 万ドル相当の効果

**関連ファイル**
- Demo Guide: [`USE_CASE_2_LEGACY_MODERNIZATION.md`](USE_CASE_2_LEGACY_MODERNIZATION.md)
- Executive Summary: [`USE_CASE_2_EXECUTIVE_SUMMARY.md`](USE_CASE_2_EXECUTIVE_SUMMARY.md)

---

### [Use Case 3: SOX Compliance Auditing](USE_CASE_3_SOX_COMPLIANCE.md)

**対象読者**: コンプライアンス担当、監査人、CFO、IT ガバナンス担当  
**所要時間**: 15〜20 分

**見せられる能力**
- 35 件以上の SOX コンプライアンス不備を特定
- SOX 302 / 404 / 409 / 802 に対応付け
- 職務分掌（RBAC）や maker-checker を設計
- 取引不変性の不足を指摘して改善案を出す

**ビジネス価値**
- コンプライアンス評価時間を 95% 削減
- 是正対応時間を 85% 削減
- 年間 258 万ドル相当の効果
- 初年度 ROI 2,480%

**関連ファイル**
- Demo Guide: [`USE_CASE_3_SOX_COMPLIANCE.md`](USE_CASE_3_SOX_COMPLIANCE.md)
- Executive Summary: [`USE_CASE_3_EXECUTIVE_SUMMARY.md`](USE_CASE_3_EXECUTIVE_SUMMARY.md)
- Non-Compliant Code: [`../../bank1-savings/app_sox_issues.py`](../../bank1-savings/app_sox_issues.py)

---

### [Use Case 4: Complex Bug Investigation](USE_CASE_4_BUG_INVESTIGATION.md)

**対象読者**: 運用チーム、SRE、DevOps エンジニア  
**所要時間**: 20〜25 分

**見せられる能力**
- 監視データとコードを一緒に分析
- 連鎖障害の根本原因を特定
- 短期 / 中期 / 長期の解決案を提示
- 修正実装と運用 Runbook の作成を支援

**ビジネス価値**
- MTTR を 90% 削減（8 時間 → 1 時間）
- 重大障害 1 件あたり 31.5 万ドル相当の削減
- 年間 474 万ドル相当の効果（年 10 件想定）
- 初年度 ROI 4,640%

**関連ファイル**
- Demo Guide: [`USE_CASE_4_BUG_INVESTIGATION.md`](USE_CASE_4_BUG_INVESTIGATION.md)
- Executive Summary: [`USE_CASE_4_EXECUTIVE_SUMMARY.md`](USE_CASE_4_EXECUTIVE_SUMMARY.md)

---

## 🎯 デモ選択ガイド

### セキュリティ重視の聴衆向け
**Primary**: Use Case 1（Security Vulnerabilities）  
**Secondary**: Use Case 3（SOX Compliance）  
**所要時間**: 30〜40 分

### モダナイゼーション案件向け
**Primary**: Use Case 2（Legacy Modernization）  
**Secondary**: Use Case 1（Security）  
**所要時間**: 35〜45 分

### 運用チーム向け
**Primary**: Use Case 4（Bug Investigation）  
**Secondary**: Use Case 2（Modernization）  
**所要時間**: 40〜50 分

### 経営層向け
**Focus**: 各ユースケースの Executive Summary を中心に紹介  
**所要時間**: 15〜20 分

### コンプライアンス担当向け
**Primary**: Use Case 3（SOX Compliance）  
**Secondary**: Use Case 1（Security）  
**所要時間**: 30〜40 分

---

## 📊 合算のビジネス価値

### 年間効果の目安（中規模銀行）

| Use Case | Annual Value |
|----------|-------------|
| Security Vulnerability Detection | $991,000 |
| Legacy Code Modernization | $2,180,000 |
| SOX Compliance Auditing | $2,580,000 |
| Complex Bug Investigation | $4,740,000 |
| **Total Annual Value** | **$10,491,000** |

### 合算指標

- **Time Savings**: 全体で 85〜95% の時間削減
- **Cost Reduction**: 関連コストを 80〜90% 削減
- **Quality Improvement**: 項目によって 60〜100% 改善
- **Risk Mitigation**: 回避できる損失は数百万ドル規模

---

## 🚀 クイックスタート

### 前提条件
1. Bob AI Coding Assistant が利用可能であること
2. `banking-demo` リポジトリにアクセスできること
3. 対象となる聴衆の関心や課題感を理解していること

### デモ準備（約 15 分）

```bash
# 1. Clone or navigate to the repository
cd banking-demo

# 2. Review the use case you'll present
code docs/demos/USE_CASE_[NUMBER]_*.md

# 3. Open the relevant code files
# For Use Case 1:
code bank1-savings/app_vulnerable.py

# For Use Case 2:
code legacy-rate-service/src/main/java/com/bank/rates/RateService.java

# For Use Case 3:
code bank1-savings/app_sox_issues.py

# For Use Case 4:
code monitoring-data/production-errors.json
```

### デモ中
1. Demo Guide の流れに沿って進行する
2. 用意されたプロンプトを Bob に入力する
3. 話すポイントを押さえる
4. ビジネス価値の数値を強調する
5. 想定質問に対応する

### デモ後
1. 経営層には Executive Summary を共有する
2. デモ資料へのアクセス方法を案内する
3. フォローアップの打ち合わせを設定する
4. Pilot 実施計画へつなげる

---

## 📝 デモのベストプラクティス

### 準備
- ✅ Demo Guide を十分に読み込む
- ✅ Bob に投げるプロンプトを事前に試す
- ✅ 聴衆の課題を理解する
- ✅ 想定質問に備える
- ✅ 予備の例を用意する

### プレゼン
- ✅ まずビジネス課題から入る
- ✅ 実際のコードを見せる
- ✅ Bob の能力をライブで見せる
- ✅ 時間削減とコスト削減を明確にする
- ✅ 聴衆の課題に結びつける

### フォローアップ
- ✅ Executive Summary を共有する
- ✅ デモ録画を共有する
- ✅ Pilot プログラムの案内をする
- ✅ 技術的な深掘りの場を設定する
- ✅ フィードバックを集める

---

## 🎓 トレーニングリソース

### デモ実施者向け
- すべての Demo Guide を確認する
- 事前に Bob を使って練習する
- ビジネス価値の説明を理解する
- 技術質問に備える
- ROI の考え方を把握する

### Pilot 参加者向け
- まず Use Case 4（即効性がある）
- 次に Use Case 1（セキュリティ）
- その後 Use Case 2（モダナイゼーション）
- 最後に Use Case 3（コンプライアンス）

---

## 📞 サポートと追加資料

### デモ支援
- Technical Questions: [Solutions Engineering Team]
- Business Questions: [Sales Team]
- Pilot Programs: [Customer Success Team]

### 追加資料
- ROI Calculator: [Access Tool]
- Case Studies: [View Library]
- Product Documentation: [Read Docs]
- Training Videos: [Watch Tutorials]

---

## 🔄 デモ更新情報

**Version**: 1.0  
**Last Updated**: 2024  
**Next Review**: Quarterly

### Changelog
- **v1.0** (2024): 4 つのユースケースを含む初版
  - Use Case 1: Security Vulnerability Detection
  - Use Case 2: Legacy Code Modernization
  - Use Case 3: SOX Compliance Auditing
  - Use Case 4: Complex Bug Investigation

---

## 📚 関連ドキュメント

- [Main Project README](../../README.md)
- [System Architecture](../architecture/SYSTEM_ARCHITECTURE.md)
- [API Reference](../reference/API_REFERENCE.md)
- [Deployment Guide](../guides/LOCAL_DEPLOYMENT.md)

---

## 🎯 成功指標

デモ中およびデモ後に、次の指標を追うと効果を測りやすくなります。

**Engagement Metrics:**
- 質問数と会話の深さ
- フォローアップ面談の依頼数
- Pilot 申し込み件数
- Executive Summary の参照数

**Business Metrics:**
- Pilot への転換率
- 初回価値実現までの時間
- 顧客満足度
- 継続率

**Technical Metrics:**
- Use Case の採用率
- 実際に達成された時間削減
- 品質改善量
- ROI 実現度

---

**Prepared By**: IBM Bob Solutions Team  
**For**: Enterprise Banking Demonstrations  
**Classification**: Internal Use  
**Distribution**: Sales, Solutions Engineering, Customer Success

---

## 🎬 デモ準備 OK?

上のユースケースから 1 つ選び、対応する Demo Guide に従って進めてください。各ユースケースは次の条件を満たすよう設計されています。

- ✅ **Self-contained**: 15〜25 分で完結
- ✅ **Audience-specific**: 役割別に刺さる構成
- ✅ **Value-focused**: ビジネス価値が明確
- ✅ **Actionable**: 次のアクションにつながる

**デモ成功を祈っています。**
