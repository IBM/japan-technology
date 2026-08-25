# BobShellコード分析例

## 概要

このドキュメントは、自然言語プロンプトを使用したBobShellによるコード分析、レビュー、品質評価の包括的な例を提供します。 問題を特定し、コード品質を向上させ、コードベース全体で高い基準を維持する方法を学びます。

## 目次

1. [コード品質分析](#コード品質分析)
2. [セキュリティ分析](#セキュリティ分析)
3. [パフォーマンス分析](#パフォーマンス分析)
4. [コードレビュー](#コードレビュー)
5. [複雑性分析](#複雑性分析)
6. [ベストプラクティスチェック](#ベストプラクティスチェック)

## コード品質分析

### 基本的な品質チェック

```bash
# Analyze single file
bob "Analyze the code quality of ./src/app.js"

# Analyze with specific checks
bob "Analyze ./src/app.js for quality, maintainability, and readability issues"

# Analyze entire directory
bob "Analyze all files in ./src recursively for code quality issues"

# Get detailed report
bob "Perform a comprehensive code quality analysis of ./src and provide a detailed report" > quality-report.md
```

**出力例:**
```markdown
# コード品質レポート

## 総合スコア: 78/100

### 発見された問題:
- **高優先度 (3)**
  - 循環的複雑度15の複雑な関数
  - 非同期関数でエラーハンドリングが不足
  - 一貫性のない命名規則

- **中優先度 (7)**
  - 長い関数（50行以上）
  - 重複したコードブロック
  - JSDocコメントが不足

- **低優先度 (12)**
  - 本番コードにconsole.log文
  - 未使用の変数
  - 定数化されていないマジックナンバー
```

### 品質メトリクス

```bash
# Get specific metrics
bob "Analyze ./src and provide metrics on complexity, maintainability, coverage, and code duplication"

# Set quality threshold
bob "Analyze ./src and ensure the code quality score is at least 80"

# Compare before and after
bob "Analyze ./src for code quality and output as JSON" > before.json
# Make changes
bob "Analyze ./src for code quality and output as JSON" > after.json
# Compare results
diff before.json after.json
```

### コードスメルの検出

```bash
# Detect code smells
bob "Detect code smells in ./src and provide detailed analysis"

# Focus on specific smells
bob "Check ./src for long methods, large classes, and duplicate code"

# Generate refactoring suggestions
bob "Analyze ./src for code smells and suggest refactoring strategies" > refactoring-plan.md
```

**出力例:**
```markdown
# 検出されたコードスメル

## 長いメソッド
**ファイル:** src/services/userService.js
**行:** 45-120
**重大度:** 中
**説明:** メソッド`processUserData`は75行の長さ
**提案:** 検証、変換、永続化のためのヘルパーメソッドを抽出

## 重複コード
**ファイル:**
- src/utils/validator.js (20-35行)
- src/utils/sanitizer.js (45-60行)
**重大度:** 高
**提案:** 共通の検証ロジックを共有ユーティリティ関数に抽出
```

## セキュリティ分析

### 脆弱性スキャン

```bash
# Basic security scan
bob "Scan ./src for security vulnerabilities"

# Scan with severity focus
bob "Scan ./src for high and critical security vulnerabilities"

# Scan for specific vulnerabilities
bob "Check ./src for SQL injection, XSS, CSRF, and exposed secrets"

# Generate security report
bob "Perform a comprehensive security scan of ./src and generate an HTML report" > security-report.html
```

**出力例:**
```
セキュリティスキャン結果
=====================

クリティカルな問題: 2
高い問題: 5
中程度の問題: 12
低い問題: 8

クリティカル: SQLインジェクション脆弱性
ファイル: src/api/users.js
行: 45
コード: db.query(`SELECT * FROM users WHERE id = ${userId}`)
修正: パラメータ化されたクエリを使用

クリティカル: ハードコードされたシークレット
ファイル: src/config/database.js
行: 12
コード: const API_KEY = "sk_live_abc123xyz"
修正: 環境変数を使用
```

### 一般的な脆弱性チェック

```bash
# Check for SQL injection
bob "Check ./src for SQL injection vulnerabilities and provide detailed examples"

# Check for XSS vulnerabilities
bob "Scan ./src for XSS vulnerabilities with examples of how to fix them"

# Check for exposed secrets
bob "Check ./src for exposed secrets, credentials, and API keys"

# Check authentication issues
bob "Analyze ./src for authentication, session management, and JWT security issues"
```

### セキュリティベストプラクティス

```bash
# Check OWASP Top 10
bob "Scan ./src for OWASP Top 10 vulnerabilities"

# Check for insecure dependencies
bob "Check ./package.json for security vulnerabilities in dependencies"

# Validate security headers
bob "Review ./src/middleware for proper security headers implementation"

# Check for sensitive data exposure
bob "Check ./src for sensitive data exposure and logging issues"
```

## パフォーマンス分析

### パフォーマンスプロファイリング

```bash
# Analyze performance
bob "Analyze ./src for performance issues and provide detailed recommendations"

# Identify bottlenecks
bob "Identify performance bottlenecks in ./src"

# Memory leak detection
bob "Check ./src for memory leaks and resource leaks"

# Async/await optimization
bob "Analyze ./src for async/await performance issues and optimization opportunities"
```

**出力例:**
```markdown
# パフォーマンス分析

## 発見されたパフォーマンス問題: 8

### 高影響 (2)
1. **同期ファイル操作**
   - ファイル: src/utils/fileHandler.js
   - 行: 23
   - 問題: 非同期コンテキストでfs.readFileSyncを使用
   - 影響: イベントループをブロック
   - 修正: fs.promises.readFileを使用

2. **N+1クエリ問題**
   - ファイル: src/api/posts.js
   - 行: 67
   - 問題: ループ内でコメントを読み込み
   - 影響: 複数のデータベースクエリ
   - 修正: JOINまたはバッチロードを使用

### 中影響 (6)
- 非効率的な配列操作
- データベースインデックスの不足
- 大きなバンドルサイズ
```

### 最適化の提案

```bash
# Get optimization recommendations
bob "Analyze ./src for performance and provide optimization recommendations" > optimizations.md

# Analyze bundle size
bob "Analyze ./src for bundle size issues and tree-shaking opportunities"

# Database query optimization
bob "Review ./src/models for database query optimization opportunities"

# Caching opportunities
bob "Identify caching opportunities in ./src"
```

## コードレビュー

### 自動コードレビュー

```bash
# Review single file
bob "Review ./src/components/UserForm.jsx for code quality and best practices"

# Review with style guide
bob "Review ./src following Airbnb style guide"

# Review git changes
bob "Review my uncommitted code changes"

# Review pull request
bob "Review the code changes between main and feature-branch" > pr-review.md
```

**出力例:**
```markdown
# コードレビュー: UserForm.jsx

## 概要
- **総合評価:** B+
- **発見された問題:** 8 (高2、中4、低2)
- **強み:** 良好なコンポーネント構造、適切なprop types
- **改善領域:** エラーハンドリング、アクセシビリティ

## 詳細レビュー

### 高優先度の問題

1. **エラーバウンダリーの欠如** (15行目)
   ```javascript
   // 現在
   const UserForm = () => {
     const [data, setData] = useState({});
   
   // 提案
   const UserForm = () => {
     const [data, setData] = useState({});
     const [error, setError] = useState(null);
     
     if (error) return <ErrorDisplay error={error} />;
   ```

2. **検証されていないユーザー入力** (45行目)
   - 入力フィールドに検証が不足
   - 提案: YupやJoiのような検証ライブラリを追加

### 中優先度の問題

1. **アクセシビリティ属性の欠如** (30-40行目)
   - フォーム入力にaria-labelsが不足
   - キーボードナビゲーションのサポートなし
   
2. **非効率的な再レンダリング** (25行目)
   - キーストロークごとにコンポーネントが再レンダリング
   - 提案: デバウンスまたはReact.memoを使用

### 肯定的な側面
- クリーンなコンポーネント構造
- フックの適切な使用
- 良好な命名規則
```

### 特定の側面のレビュー

```bash
# Focus on specific aspects
bob "Review ./src focusing on security and performance"

# Review documentation
bob "Review ./src and check if documentation is adequate"

# Review test coverage
bob "Review ./tests and assess test coverage quality"

# Review API design
bob "Review ./src/api for API design and REST principles compliance"
```

### スタイルガイド準拠

```bash
# Check Airbnb style guide
bob "Review ./src following Airbnb style guide and suggest fixes"

# Check Google style guide
bob "Review ./src following Google style guide"

# Check Standard JS
bob "Review ./src following Standard JS style guide"
```

## 複雑性分析

### 循環的複雑度

```bash
# Analyze complexity
bob "Analyze ./src for cyclomatic complexity metrics"

# Find complex functions
bob "Find functions in ./src with complexity greater than 10"

# Detailed complexity report
bob "Analyze ./src for complexity and provide a detailed report" > complexity-report.md
```

**出力例:**
```markdown
# 複雑性分析

## しきい値を超える関数 (複雑度 > 10)

1. **processOrderData** - 複雑度: 18
   - ファイル: src/services/orderService.js
   - 行: 45-120
   - 推奨: より小さな関数に分割
   - 提案されるリファクタリング:
     - extractValidation()
     - calculateTotals()
     - applyDiscounts()
     - persistOrder()

2. **validateUserInput** - 複雑度: 15
   - ファイル: src/utils/validation.js
   - 行: 30-85
   - 推奨: 検証ライブラリを使用するかルールを抽出

## 複雑度の分布
- 低 (1-5): 145関数 (72%)
- 中 (6-10): 45関数 (22%)
- 高 (11-15): 10関数 (5%)
- 非常に高 (>15): 2関数 (1%)
```

### 認知的複雑度

```bash
# Analyze cognitive complexity
bob "Analyze ./src for cognitive complexity"

# Compare cyclomatic vs cognitive
bob "Analyze ./src and compare cyclomatic complexity with cognitive complexity"
```

### 保守性指標

```bash
# Calculate maintainability index
bob "Calculate the maintainability index for ./src"

# Find hard-to-maintain code
bob "Find code in ./src with maintainability index below 65"

# Generate maintainability report
bob "Analyze ./src for maintainability and generate an HTML report" > maintainability.html
```

## 依存関係分析

### 依存関係チェック

```bash
# Analyze dependencies
bob "Analyze dependencies in ./package.json"

# Find outdated dependencies
bob "Check ./package.json for outdated dependencies"

# Security vulnerabilities in dependencies
bob "Check ./package.json for security vulnerabilities in dependencies"

# Unused dependencies
bob "Find unused dependencies in ./package.json"
```

**出力例:**
```markdown
# 依存関係分析

## 古い依存関係 (12)
- express: 4.17.1 → 4.18.2 (マイナーアップデート利用可能)
- react: 17.0.2 → 18.2.0 (メジャーアップデート利用可能)
- lodash: 4.17.20 → 4.17.21 (セキュリティパッチ)

## 脆弱な依存関係 (3)
- **minimist** (クリティカル)
  - 現在: 1.2.5
  - 修正版: 1.2.6
  - 脆弱性: プロトタイプ汚染
  
## 未使用の依存関係 (5)
- moment (代わりにdate-fnsを使用)
- request (非推奨、axiosを使用)
- gulp (ビルドプロセスで未使用)

## 推奨事項
1. lodashを直ちに更新（セキュリティ）
2. React 18への移行を計画
3. 未使用の依存関係を削除
4. 依存関係のサイズへの影響を考慮
```

### インポート分析

```bash
# Analyze imports
bob "Analyze imports in ./src"

# Find circular dependencies
bob "Check ./src for circular dependencies"

# Unused imports
bob "Find unused imports in ./src"

# Import organization
bob "Check if imports in ./src are properly organized"
```

## ベストプラクティスチェック

### 言語固有のベストプラクティス

```bash
# JavaScript/TypeScript best practices
bob "Check ./src for JavaScript and TypeScript best practices"

# Python best practices (PEP 8)
bob "Check ./src for Python best practices and PEP 8 compliance"

# Java best practices
bob "Check ./src for Java best practices"

# React best practices
bob "Check ./src for React best practices and patterns"
```

### フレームワーク固有のチェック

```bash
# Express.js best practices
bob "Check ./src for Express.js best practices"

# React best practices
bob "Analyze ./src React code for best practices and common patterns"

# Vue.js best practices
bob "Check ./src for Vue.js best practices"

# Django best practices
bob "Check ./src for Django best practices"
```

### コード構成

```bash
# Check file structure
bob "Review the file structure of ./src and suggest improvements"

# Check naming conventions
bob "Check ./src for consistent naming conventions"

# Check module organization
bob "Analyze ./src for proper module organization"

# Check separation of concerns
bob "Check ./src for proper separation of concerns"
```

## バッチ分析

### 複数プロジェクトの分析

```bash
# Analyze multiple directories
for dir in project1 project2 project3; do
    bob "Analyze ./$dir for code quality and output as JSON" > ${dir}-analysis.json
done
```

### スケジュール分析

```bash
# Create analysis script
cat > daily-analysis.sh << 'EOF'
#!/bin/bash
DATE=$(date +%Y%m%d)
bob "Analyze ./src for code quality and output as JSON" > reports/analysis-$DATE.json
bob "Analyze ./src for code quality and generate HTML report" > reports/analysis-$DATE.html

# Check for critical issues
if grep -q "CRITICAL" reports/analysis-$DATE.json; then
    echo "Critical issues found!" | mail -s "Code Analysis Alert" team@example.com
fi
EOF

# Schedule with cron
# 0 2 * * * /path/to/daily-analysis.sh
```

## CI/CDとの統合

### プリコミット分析

```bash
# Pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
echo "Running code analysis..."

# Analyze staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|jsx|ts|tsx)$')

if [ -n "$STAGED_FILES" ]; then
    for file in $STAGED_FILES; do
        bob "Analyze $file and fail if any high severity issues are found"
        if [ $? -ne 0 ]; then
            echo "Analysis failed for $file"
            exit 1
        fi
    done
fi

echo "Analysis passed!"
EOF

chmod +x .git/hooks/pre-commit
```

### プルリクエスト分析

```bash
# Analyze PR changes
bob review --git-diff origin/main...HEAD \
    --format markdown \
    --output pr-analysis.md

# Check for regressions
bob analyze ./src --compare-with baseline-analysis.json \
    --fail-on-regression
```

## 分析のベストプラクティス

### 1. 定期的な分析

```bash
# Daily analysis
bob "Analyze ./src and provide comprehensive results in JSON format" > daily-$(date +%Y%m%d).json

# Weekly detailed report
bob "Analyze ./src with verbose details and provide comprehensive report in HTML format" > weekly-report.html
```

### 2. 重大な問題に焦点を当てる

```bash
### プリコミット分析

```bash
# Pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
echo "Running code analysis..."

# Get staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(js|jsx|ts|tsx)$')

if [ -n "$STAGED_FILES" ]; then
    for file in $STAGED_FILES; do
        bob "Analyze $file for critical issues" | grep -q "CRITICAL" && exit 1
    done
fi

echo "Analysis passed!"
EOF

chmod +x .git/hooks/pre-commit
```

### プルリクエスト分析

```bash
# Analyze PR changes
bob "Review the code changes between origin/main and HEAD" > pr-analysis.md

# Check for regressions
bob "Analyze ./src and compare with previous quality baseline"
```

## 分析のベストプラクティス

### 1. 定期的な分析

```bash
# Daily analysis
bob "Analyze ./src for code quality" > daily-$(date +%Y%m%d).json

# Weekly detailed report
bob "Perform comprehensive analysis of ./src with detailed recommendations" > weekly-report.html
```

### 2. 重大な問題に焦点を当てる

```bash
# Prioritize critical and high severity
bob "Analyze ./src and focus on critical and high severity issues"

# Focus on security first
bob "Scan ./src for critical security vulnerabilities"
```

### 3. 改善を追跡

```bash
# Baseline analysis
bob "Analyze ./src for code quality and output as JSON" > baseline.json

# After improvements
bob "Analyze ./src for code quality and output as JSON" > improved.json

# Compare manually or ask Bob
bob "Compare the code quality between baseline.json and improved.json"
```

### 4. すべてを自動化

```bash
# Automated workflow
bob "Analyze ./src for code quality" > analysis.json && \
bob "Scan ./src for security vulnerabilities" > security.json && \
bob "Review my uncommitted changes" > review.md && \
bob "Create an executive summary from analysis.json, security.json, and review.md" > summary.md
```

## より良い分析のためのヒント

1. **具体的にする**: 分析したい側面を明確に記述
2. **コンテキストを提供**: テクノロジースタックとフレームワークを言及
3. **優先順位を設定**: まずクリティカルな問題に焦点を当てる
4. **定期的なチェック**: ワークフローに分析を統合
5. **進捗を追跡**: 時間の経過とともに改善を追跡するために分析結果を保存

## 次のステップ

- より多くのプロンプトパターンについては[基本コマンド](./basic-commands.md)をレビュー
- コード作成については[コード生成](./code-generation.md)を探索
- 完全なワークフローについては[Lab 4 README](../README.md)を確認
- 実際のコード例で練習

---

**プロのヒント**: 分析したい内容を正確に記述するために自然言語を使用してください。プロンプトが具体的であるほど、分析結果は良くなります！