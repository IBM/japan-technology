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

```bash
# Start Bob with checkpointing enabled
bob --checkpointing
```

または、Bob設定で有効にしてから、通常通り`bob`で起動します。

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
bob "Create a REST API endpoint for user login"

# Generate and save to file (with clean output)
bob "Create a React component for a todo list" --yolo --hide-intermediary-output > TodoList.jsx

# Generate with specific language (asking Bob to write to file)
bob "Create a sorting algorithm in Python and write it to sort.py" --yolo

# Generate multiple related files (with clean output)
bob "Create a complete Express.js API with routes, controllers, and models for user management" --yolo --hide-intermediary-output > api-structure.txt

# Generate with specific framework (asking Bob to write to file)
bob "Create a Vue 3 component for user profile using Composition API and write it to UserProfile.vue" --yolo
```

### コード分析

```bash
# Analyze single file
bob analyze ./src/app.js

# Analyze with specific checks
bob "Analyze ./src/app.js focusing on quality, performance, and security issues"

# Analyze directory recursively
bob "Analyze all files in ./src directory recursively"

# Analyze with output format
bob "Analyze ./src and provide results in JSON format" --hide-intermediary-output > analysis.json
bob "Analyze ./src and provide results in markdown format" --hide-intermediary-output > analysis.md
bob "Analyze ./src and provide results in HTML format" --hide-intermediary-output > analysis.html

# Get specific metrics
bob "Analyze ./src and provide complexity, maintainability, and coverage metrics"

# Analyze with threshold
bob "Analyze ./src and fail if quality score is below 80"
```

### コードレビュー

```bash
# Review single file
bob review ./src/components/UserForm.jsx


### コードレビュー

```bash
# Review with style guide
bob "Review ./src following Airbnb style guide"
bob "Review ./src following Google style guide"

# Review git changes
bob "Review the uncommitted changes in my code"
bob "Review the code changes between main and feature-branch"

# Review with specific focus
bob "Review ./src focusing on security, performance, and maintainability" --hide-intermediary-output > review-report.md
```

### コードの説明

```bash
# Explain code in file
bob "Explain what the code in ./src/utils/helper.js does"

# Explain specific function
bob "Explain the calculateTotal function in ./src/utils/helper.js"

# Detailed explanation
bob "Provide a detailed explanation of the algorithm in ./src/complex-algorithm.js" --hide-intermediary-output > explanation.md

# Explain in different language
bob "Explain the code in ./src/app.js in Spanish"
```

### コードリファクタリング

```bash
# Refactor file
bob "Refactor ./src/legacy-code.js to use modern JavaScript patterns"

# Refactor for performance
bob "Refactor ./src/slow-function.js to improve performance"

# Remove dead code
bob "Identify and remove dead code from ./src/app.js"

# Fix style issues
bob "Fix all style issues in ./src/app.js following best practices"
```

### セキュリティスキャン

```bash
# Basic security scan
bob "Scan ./src for security vulnerabilities"

# Scan with severity focus
bob "Scan ./src for high and critical security vulnerabilities"

# Scan for specific vulnerabilities
bob "Check ./src for SQL injection, XSS, exposed secrets, and CSRF vulnerabilities"

# Generate security report
bob "Perform a comprehensive security scan of ./src and generate a detailed report" --hide-intermediary-output > security-report.html
```

### ドキュメント生成

```bash
# Generate API documentation
bob "Generate API documentation for the code in ./src" --hide-intermediary-output > api-docs.md

# Generate architecture documentation
bob "Create architecture documentation for ./src explaining the system design" --hide-intermediary-output > architecture.md

# Generate usage examples
bob "Generate usage examples for the functions in ./src" --hide-intermediary-output > examples.md

# Generate README
bob "Create a comprehensive README for this project based on ./src" --hide-intermediary-output > README.md
```

### テスト

```bash
# Generate tests for file
bob "Generate Jest unit tests for ./src/app.js" --yolo --hide-intermediary-output > ./tests/app.test.js

# Generate tests with specific framework
bob "Generate pytest tests for ./src/app.py with fixtures and mocks" --yolo --hide-intermediary-output > ./tests/test_app.py

# Suggest test improvements
bob "Review ./tests/app.test.js and suggest improvements for better coverage"
```

### コードフォーマット

```bash
# Format file
bob "Format ./src/app.js following Prettier standards"

# Format with specific style
bob "Format ./src/app.py following Black formatting style"

# Check formatting
bob "Check if ./src follows proper formatting standards and suggest fixes"
```

## Gitとの連携

```bash
# Review uncommitted changes
bob "Review my uncommitted code changes"

# Review changes in branch
bob "Review the code changes between main and feature-branch"

# Generate commit message
bob "Generate a commit message for my staged changes"

# Generate changelog
bob "Generate a changelog for changes since v1.0.0" --hide-intermediary-output > CHANGELOG.md
```

## バッチ操作

### 複数ファイルの処理

```bash
# Analyze all JavaScript files
for file in ./src/**/*.js; do
    bob "Analyze $file for code quality issues" --hide-intermediary-output >> analysis-results.txt
done

# Review all Python files
for file in ./src/**/*.py; do
    bob "Review $file for code quality and best practices in markdown format" --hide-intermediary-output > "reviews/$(basename $file).md"
done

# Generate tests for all files
bob test-generate ./src/**/*.js --output-dir ./tests

# Refactor all files in directory
bob "Refactor all files in ./src directory recursively using modern coding patterns and best practices"
```

## 出力形式

### 利用可能な形式

```bash
# JSON output (for programmatic processing)
bob analyze ./src --format json

# Markdown output (for documentation)
bob review ./src --format markdown

# HTML output (for reports)
bob security-scan ./src --format html

# Plain text output (default)
bob explain ./src/app.js --format text

# YAML output
bob analyze ./src --format yaml
```

## 設定管理

### 設定の管理

```bash
# View current configuration
bob config list

# Get specific config value
bob config get api-key
bob config get default-mode

# Set configuration value
bob config set cache-ttl 3600
bob config set max-tokens 4096

# Reset configuration
bob config reset

# Review all Python files
for file in ./src/**/*.py; do
    bob "Review $file and suggest improvements" --hide-intermediary-output >> review-results.md
done
```

## パイプとチェーン

### コマンドの組み合わせ

```bash
# Pipe code to Bob for explanation
cat ./src/app.js | bob "Explain this code"

# Chain with other tools
bob "Analyze ./src for quality issues and output as JSON" | jq '.issues[] | select(.severity == "high")'

# Use in scripts
if bob "Scan ./src for critical security vulnerabilities" | grep -q "CRITICAL"; then
    echo "Security issues found"
    exit 1
else
    echo "Security check passed"
fi

# Combine multiple Bob commands
bob "Analyze ./src for code quality" --hide-intermediary-output > analysis.json && \
bob "Review ./src for best practices" --hide-intermediary-output > review.md && \
bob "Scan ./src for security vulnerabilities" --hide-intermediary-output > security.html
```

## ヒントとコツ

### 生産性のヒント

1. **Use Aliases**: Create shell aliases for common prompts
   ```bash
   alias bob-review='bob "Review my code changes for quality and best practices"'
   alias bob-scan='bob "Scan for high and critical security vulnerabilities"'
   ```

2. **Save Common Prompts**: Store frequently used prompts in files
   ```bash
   echo "Analyze this code for quality, performance, and security issues" > analyze-prompt.txt
   bob "$(cat analyze-prompt.txt) in ./src/app.js"
   ```

3. **Use Variables in Scripts**: Make prompts reusable
   ```bash
   FILE="./src/app.js"
   bob "Analyze $FILE for code quality and suggest improvements"
   ```

4. **Combine with Git**: Integrate Bob into your git workflow
   ```bash
   # .git/hooks/pre-commit
   #!/bin/bash
   bob "Review my uncommitted changes and check for issues" | grep -q "ERROR" && exit 1
   ```

## 一般的なパターン

### 便利なワークフローパターン

```bash
# Quick code review workflow
bob "Review my uncommitted changes" && \
bob "Scan for security vulnerabilities" && \
npm test

# Documentation update workflow
bob "Generate API documentation for ./src" --hide-intermediary-output > docs/api.md && \
bob "Create a comprehensive README for this project" --hide-intermediary-output > README.md

# Pre-deployment checks
bob "Analyze ./src and ensure code quality score is above 80" && \
bob "Scan for critical security vulnerabilities" && \
npm run test

# Code quality improvement workflow
bob "Analyze ./src for quality issues" --hide-intermediary-output > before-analysis.txt && \
bob "Refactor ./src to use modern best practices" && \
bob "Analyze ./src for quality issues" --hide-intermediary-output > after-analysis.txt
```

## 次のステップ

- [コード生成例](./code-generation.md)を探索
- [分析例](./analysis-examples.md)について学ぶ
- 完全なワークフローについては[Lab 4 README](../README.md)をレビュー

---

**クイックリファレンス**: BobはCLIフラグの代わりに自然言語プロンプトを使用します。必要なものについて具体的に記述し、ファイルパスを言及し、結果を保存するには出力リダイレクト（`>`）を使用してください！