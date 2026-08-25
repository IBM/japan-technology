# BobShell基本コマンドリファレンス

## 概要

このドキュメントは、自然言語プロンプトを使用したBobShellの包括的なリファレンスを提供します。 これらの例を独自の自動化とワークフローの出発点として使用してください。

## インストールとセットアップ

### BobShellのインストール

**⚠️ Windowsユーザーへの重要な注意:**

BobShellはWindows上のBobと一緒に自動インストールされません。公式インストールガイドに従って個別にインストールする必要があります：

👉 **[BobShellインストールガイド](https://bob.ibm.com/docs/shell/getting-started/install-and-setup)**

**すべてのユーザー向け**、BobShellがインストールされていることを確認してください：

```bash
# Verify installation
bob --version
```

## インタラクティブモード

### インタラクティブモードの開始

```bash
# Start interactive session
bob
```

**注意:** 単に`bob`と入力するだけでインタラクティブなBobShellセッションが開始されます。

### インタラクティブモードの例

```
# General questions
> What is the difference between let and const in JavaScript?

# Code explanation
> Explain this code: function debounce(func, wait) { ... }

# Code generation
> Create a Python function to validate email addresses using regex

# Code review
> Review this function for potential issues: [paste code]

# Refactoring suggestions
> How can I improve this code: [paste code]

# Exit interactive mode
> exit
> quit
> :q

### チェックポイントの使用

チェックポイントを使用すると、インタラクティブモードで会話状態を保存および復元できます。Bobを起動する際にチェックポイントを有効にします：

```json
// ~/.bob/settings.json または .bob/settings.json に以下を追加
{
  "general": {
    "checkpointing": {
      "enabled": true
    }
  }
}
```

設定後は通常通り `bob` で起動するだけでチェックポイントが有効になります。

**チェックポイントの使用方法:**

有効にすると、Bobは会話状態を自動的に保存します。以前のポイントを自然に参照できます：

```
# Work on your code
> Analyze this code for issues
# Bob provides analysis

> Suggest fixes for the issues
# Bob suggests fixes

> Actually, let's go back to the analysis and try a different approach
# Bob restores to the analysis state

> Instead of fixing, suggest a complete refactor
# Bob provides refactoring suggestions
```

**チェックポイントのユースケース:**
- 異なるアプローチを試す
- 複数の解決パスを試す
- 以前の会話状態に戻る
- 進捗を失わずに代替案を探索

```

## 非インタラクティブモード（自然言語プロンプト）

### ヘルプと情報

```bash
# General help
bob --help
bob -h

# Version information
bob --version
bob -v
```

### コード生成

```bash
# Generate code from description
bob run "Create a REST API endpoint for user login"

# Generate and save to file (with clean output)
bob run "Create a React component for a todo list" --log-level silent > TodoList.jsx

# Generate with specific language (asking Bob to write to file)
bob run "Create a sorting algorithm in Python and write it to sort.py"

# Generate multiple related files (with clean output)
bob run "Create a complete Express.js API with routes, controllers, and models for user management" --log-level silent > api-structure.txt

# Generate with specific framework (asking Bob to write to file)
bob run "Create a Vue 3 component for user profile using Composition API and write it to UserProfile.vue"
```

### コード分析

```bash
# Analyze single file
bob run "Analyze the code quality of ./src/app.js"

# Analyze with specific checks
bob run "Analyze ./src/app.js focusing on quality, performance, and security issues"

# Analyze directory recursively
bob run "Analyze all files in ./src directory recursively"

# Analyze with output format
bob run "Analyze ./src and provide results in JSON format" --log-level silent > analysis.json
bob run "Analyze ./src and provide results in markdown format" --log-level silent > analysis.md
bob run "Analyze ./src and provide results in HTML format" --log-level silent > analysis.html

# Get specific metrics
bob run "Analyze ./src and provide complexity, maintainability, and coverage metrics"

# Analyze with threshold
bob run "Analyze ./src and fail if quality score is below 80"
```

### コードレビュー

```bash
# Review single file
bob run "Review ./src/components/UserForm.jsx for code quality and best practices"

# Review with style guide
bob run "Review ./src following Airbnb style guide"
bob run "Review ./src following Google style guide"

# Review git changes
bob run "Review the uncommitted changes in my code"
bob run "Review the code changes between main and feature-branch"

# Review with specific focus
bob run "Review ./src focusing on security, performance, and maintainability" --log-level silent > review-report.md
```

### コードの説明

```bash
# Explain code in file
bob run "Explain what the code in ./src/utils/helper.js does"

# Explain specific function
bob run "Explain the calculateTotal function in ./src/utils/helper.js"

# Detailed explanation
bob run "Provide a detailed explanation of the algorithm in ./src/complex-algorithm.js" --log-level silent > explanation.md

# Explain in different language
bob run "Explain the code in ./src/app.js in Spanish"
```

### コードリファクタリング

```bash
# Refactor file
bob run "Refactor ./src/legacy-code.js to use modern JavaScript patterns"

# Refactor for performance
bob run "Refactor ./src/slow-function.js to improve performance"

# Remove dead code
bob run "Identify and remove dead code from ./src/app.js"

# Fix style issues
bob run "Fix all style issues in ./src/app.js following best practices"
```

### セキュリティスキャン

```bash
# Basic security scan
bob run "Scan ./src for security vulnerabilities"

# Scan with severity focus
bob run "Scan ./src for high and critical security vulnerabilities"

# Scan for specific vulnerabilities
bob run "Check ./src for SQL injection, XSS, exposed secrets, and CSRF vulnerabilities"

# Generate security report
bob run "Perform a comprehensive security scan of ./src and generate a detailed report" --log-level silent > security-report.html
```

### ドキュメント生成

```bash
# Generate API documentation
bob run "Generate API documentation for the code in ./src" --log-level silent > api-docs.md

# Generate architecture documentation
bob run "Create architecture documentation for ./src explaining the system design" --log-level silent > architecture.md

# Generate usage examples
bob run "Generate usage examples for the functions in ./src" --log-level silent > examples.md

# Generate README
bob run "Create a comprehensive README for this project based on ./src" --log-level silent > README.md
```

### テスト

```bash
# Generate tests for file
bob run "Generate Jest unit tests for ./src/app.js" --log-level silent > ./tests/app.test.js

# Generate tests with specific framework
bob run "Generate pytest tests for ./src/app.py with fixtures and mocks" --log-level silent > ./tests/test_app.py

# Suggest test improvements
bob run "Review ./tests/app.test.js and suggest improvements for better coverage"
```

### コードフォーマット

```bash
# Format file
bob run "Format ./src/app.js following Prettier standards"

# Format with specific style
bob run "Format ./src/app.py following Black formatting style"

# Check formatting
bob run "Check if ./src follows proper formatting standards and suggest fixes"
```

## Gitとの連携

```bash
# Review uncommitted changes
bob run "Review my uncommitted code changes"

# Review changes in branch
bob run "Review the code changes between main and feature-branch"

# Generate commit message
bob run "Generate a commit message for my staged changes"

# Generate changelog
bob run "Generate a changelog for changes since v1.0.0" --log-level silent > CHANGELOG.md
```

## バッチ操作

### 複数ファイルの処理

```bash
# Analyze all JavaScript files
for file in ./src/**/*.js; do
    bob run "Analyze $file for code quality issues" --log-level silent >> analysis-results.txt
done

# Review all Python files
for file in ./src/**/*.py; do
    bob run "Review $file for code quality and best practices in markdown format" --log-level silent > "reviews/$(basename $file).md"
done

# Generate tests for all files
bob run "Generate Jest unit tests for all JavaScript files in ./src and save them to ./tests"

# Refactor all files in directory
bob run "Refactor all files in ./src directory recursively using modern coding patterns and best practices"
```

## 出力形式

### 利用可能な形式

```bash
# JSON output (for programmatic processing)
bob run "Analyze ./src and provide results in JSON format" --log-level silent > analysis.json

# Markdown output (for documentation)
bob run "Review ./src for code quality and output in markdown format" --log-level silent > review.md

# HTML output (for reports)
bob run "Scan ./src for security vulnerabilities and output in HTML format" --log-level silent > security-report.html

# Plain text output (default)
bob run "Explain what the code in ./src/app.js does"
```

## 設定管理

### 設定の管理

v2.0 では設定ファイル (`~/.bob/settings.json` または `.bob/settings.json`) で管理します。

```bash
# Review all Python files
for file in ./src/**/*.py; do
    bob run "Review $file and suggest improvements" --log-level silent >> review-results.md
done
```

## パイプとチェーン

### コマンドの組み合わせ

```bash
# Pipe code to Bob for explanation
cat ./src/app.js | bob run "Explain this code"

# Chain with other tools
bob run "Analyze ./src for quality issues and output as JSON" | jq '.issues[] | select(.severity == "high")'

# Use in scripts
if bob run "Scan ./src for critical security vulnerabilities" | grep -q "CRITICAL"; then
    echo "Security issues found"
    exit 1
else
    echo "Security check passed"
fi

# Combine multiple Bob commands
bob run "Analyze ./src for code quality" --log-level silent > analysis.json && \
bob run "Review ./src for best practices" --log-level silent > review.md && \
bob run "Scan ./src for security vulnerabilities" --log-level silent > security.html
```

## ヒントとコツ

### 生産性のヒント

1. **Use Aliases**: Create shell aliases for common prompts
   ```bash
   alias bob-review='bob run "Review my code changes for quality and best practices"'
   alias bob-scan='bob run "Scan for high and critical security vulnerabilities"'
   ```

2. **Save Common Prompts**: Store frequently used prompts in files
   ```bash
   echo "Analyze this code for quality, performance, and security issues" > analyze-prompt.txt
   bob run "$(cat analyze-prompt.txt) in ./src/app.js"
   ```

3. **Use Variables in Scripts**: Make prompts reusable
   ```bash
   FILE="./src/app.js"
   bob run "Analyze $FILE for code quality and suggest improvements"
   ```

4. **Combine with Git**: Integrate Bob into your git workflow
   ```bash
   # .git/hooks/pre-commit
   #!/bin/bash
   bob run "Review my uncommitted changes and check for issues" | grep -q "ERROR" && exit 1
   ```

## 一般的なパターン

### 便利なワークフローパターン

```bash
# Quick code review workflow
bob run "Review my uncommitted changes" && \
bob run "Scan for security vulnerabilities" && \
npm test

# Documentation update workflow
bob run "Generate API documentation for ./src" --log-level silent > docs/api.md && \
bob run "Create a comprehensive README for this project" --log-level silent > README.md

# Pre-deployment checks
bob run "Analyze ./src and ensure code quality score is above 80" && \
bob run "Scan for critical security vulnerabilities" && \
npm run test

# Code quality improvement workflow
bob run "Analyze ./src for quality issues" --log-level silent > before-analysis.txt && \
bob run "Refactor ./src to use modern best practices" && \
bob run "Analyze ./src for quality issues" --log-level silent > after-analysis.txt
```

## 次のステップ

- [コード生成例](./code-generation.md)を探索
- [分析例](./analysis-examples.md)について学ぶ
- 完全なワークフローについては[Lab 4 README](../README.md)をレビュー

---

**クイックリファレンス**: BobはCLIフラグの代わりに自然言語プロンプトを使用します。必要なものについて具体的に記述し、ファイルパスを言及し、結果を保存するには出力リダイレクト（`>`）を使用してください！