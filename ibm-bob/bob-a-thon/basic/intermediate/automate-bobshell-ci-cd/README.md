# Lab 4: BobShellとコマンドライン使用法

## 概要

このラボでは、BobのCLI（BobShell）を使って開発タスクを自動化する方法を学びます。スクリプトやビルドプロセス、CI/CDパイプラインへの組み込みまで、BobのAI機能をターミナルから直接使えるようになることがゴールです。

> Bob差別化要因: インテリジェントリソース最適化
> BobShellはBobの自動モデル選択を使ってすべてのコマンドを最適化します。コードフォーマットのような単純なタスクには軽量モデルで速度を上げ、複雑な分析にはフロンティアクラスのモデルで精度を確保します。この切り替えはバックグラウンドで自動的に行われ、品質を維持しながらコストを最大60%削減できます。

所要時間: 45〜60分  
難易度: 中級  
前提条件: Lab 1〜3の完了、基本的なコマンドラインの知識

## 学習目標

このラボを終えると、次のことができます：

1. インタラクティブモードと非インタラクティブモードでBobShellを使う
2. BobのAI機能を組み込んだ自動化スクリプトを作る
3. BobをCI/CDパイプラインに統合する
4. CLI経由でコード生成・分析・リファクタリングを行う
5. 自動コードレビューと品質チェックを実装する
6. Bobと他のCLIツールを組み合わせたカスタムワークフローを作る

## BobShellとは？

BobShellはBobのコマンドラインインターフェースです。主に4つの使い方があります：

- ターミナルから直接Bobとチャットする（インタラクティブモード）
- 自動化のための単一コマンド実行（非インタラクティブモード）
- シェルスクリプトや自動化ワークフローへの組み込み
- ビルド・デプロイパイプラインへの統合

## ラボ構成

```
lab4/
├── README.md                 # このファイル
├── examples/                 # コマンド例とユースケース
│   ├── basic-commands.md     # 基本的なBobShellコマンド
│   ├── code-generation.md    # コード生成の例
│   └── analysis-examples.md  # コード分析の例
├── scripts/                  # 自動化スクリプト
│   ├── code-review.sh        # 自動コードレビュースクリプト
│   ├── refactor-batch.sh     # バッチリファクタリングスクリプト
│   └── generate-docs.sh      # ドキュメント生成スクリプト
└── ci-cd/                    # CI/CD統合例
    ├── github-actions.yml    # GitHub Actionsワークフロー
    ├── gitlab-ci.yml         # GitLab CI設定
    └── jenkins-pipeline.txt  # Jenkinsパイプライン例
```

## パート1: BobShellの開始

### ステップ1.1: BobShellのインストールと確認

⚠️ Windowsユーザーへの注意:

BobShellはWindows上のBobと一緒に自動インストールされません。公式インストールガイドに従って個別にインストールする必要があります：

👉 [BobShellインストールガイド](https://bob.ibm.com/docs/shell/getting-started/install-and-setup)

📚 公開Bobドキュメントはこちら: https://ibm.biz/bob-doc

まず、BobShellがインストールされてPATHに通っているか確認してください：

```bash
# Check BobShell version
bob --version

# View help information
bob --help
```

期待される出力:
```
Bob CLI v1.x.x
Usage: bob [options] [command]
...
```

「command not found」が表示される場合は：
- Windowsユーザーは[インストールガイド](https://bob.ibm.com/docs/shell/getting-started/install-and-setup)に従ってBobShellをインストールしてください
- macOS/Linuxユーザーは、BobがインストールされてシェルコンポーネントがPATHに含まれているか確認してください

`--version` はインストール済みのバージョンを、`--help` は利用可能なすべてのコマンドとオプションを表示します。

### ステップ1.2: インタラクティブモード

ターミナルから直接チャットするには、次のコマンドでBobをインタラクティブモードで起動します：

```bash
# Start interactive BobShell session
bob
```

起動するとプロンプトが表示され、Bobと直接チャットできます。Bobのすべての機能が自然言語で使える状態になります。

インタラクティブモードで試してみてください：

```
# Ask Bob to explain a concept
> Explain what a closure is in JavaScript

# Request code generation
> Create a Python function to calculate fibonacci numbers

# Ask for code review
> Review this code: [paste code here]
```

終了は `Ctrl+C` を2回押します。

インタラクティブモードはターミナル内で会話型インターフェースを提供します。完全なIDEを開かずに素早くクエリを実行したい場面に最適で、会話中はセッション履歴が保持されます。

### ステップ1.3: 非インタラクティブモード

インタラクティブモードに入らずに単一のコマンドを実行したい場合に使います。まず簡単なテストファイルを作成してください：

```bash
# Create a simple Python file to work with
echo 'def add(a, b):
    return a + b

def multiply(x, y):
    return x * y' > calculator.py
```

次に、非インタラクティブコマンドを試してみましょう：

```bash
# Explain code in a file
bob "Explain what the calculator.py file does"

# Ask for code review
bob "Review calculator.py and suggest improvements"

# Generate new code
bob "Create a Python function that calculates the factorial of a number" --yolo --hide-intermediary-output > factorial.py

# Ask a quick question
bob "What is the difference between a list and a tuple in Python?"
```

非インタラクティブモードは単一のコマンドを実行して終了します。`bob "your prompt"` の形式で使います。特定のツールを呼び出す際に明示的な承認が必要な場合は `--yolo` を追加してください。結果はstdoutに出力されるので、パイプや他のCLIツールとも組み合わせやすいです。

### ステップ1.5: 出力リダイレクトの理解

BobShellで出力リダイレクト（ `>` ）を使う場合、クリーンなコードファイルを得るための注意点があります。

⚠️ 出力リダイレクトの動作について

デフォルトでは、Bobの出力をファイルにリダイレクトすると、Bobの思考プロセスと中間出力が生成されたコードと一緒にファイルに含まれます。コードのみを取得するには2つの方法があります。

オプション1: `--hide-intermediary-output` フラグを使う
```bash
# Generate code with clean output
bob "Create a Python function that calculates the factorial of a number" --yolo --hide-intermediary-output > factorial.py
```

オプション2: プロンプトにファイル書き込み指示を含める
```bash
# Ask Bob to write directly to the file
bob "Create a Python function that calculates the factorial of a number and write it to factorial.py" --yolo
```

これらのアプローチを使わない場合、ファイルにはBobの思考プロセス、ツール使用メッセージ、ステータス更新も含まれます。使った場合は、クリーンな生成コードだけが入り、すぐに使えるファイルになります。

```bash
# ❌ This includes Bob's thinking in the file
bob "Create a sorting function" --yolo > sort.py

# ✅ This creates a clean code file
bob "Create a sorting function" --yolo --hide-intermediary-output > sort.py

# ✅ This also creates a clean code file
bob "Create a sorting function and write it to sort.py" --yolo
```

💡 ファイルにリダイレクトする際は常に `--hide-intermediary-output` を使うか、プロンプトでBobに明示的にファイルへの書き込みを指示してください。

### ステップ1.4: セッション再開の使用

Bobはインタラクティブセッションを自動的に保存するので、以前の会話を再開して中断したところから続けられます。

```bash
# List available sessions
bob --list-sessions

# Resume the most recent session
bob --resume latest

# Resume a specific session by index
bob --resume 5
```

ワークフローでの使い方：

```
# Start a new session
bob

# Work on your code
> Review calculator.py and suggest improvements

# Bob provides suggestions...

# Exit the session (Ctrl+C twice)

# Later, resume the same session
bob --resume latest

# Continue from where you left off
> Let's implement those suggestions now
```

仕組みはシンプルで、Bobはすべてのインタラクティブセッションを自動保存します。各セッションはインデックス化され、 `--list-sessions` でリスト表示できます。最新の作業を続けるには `--resume latest` 、特定のセッションに戻るには `--resume <index>` を使います。

```bash
# List all available sessions
bob --list-sessions

# Delete a specific session
bob --delete-session 3

# Resume and continue working
bob --resume latest
```

セッション再開が役立つ場面：

1. 休憩後に中断したところから再開したい
2. セッション間で会話コンテキストを保持したい
3. 複数プロジェクト間でセッションを切り替えたい
4. 以前の探索内容に戻りたい

ワークフロー例：

```bash
# Start working on a feature
bob
> Analyze myapp.js for performance issues
# Bob identifies several issues
> Suggest optimizations for the database queries
# Exit session

# Later, resume to continue
bob --resume latest
> Let's implement those database optimizations now
# Bob remembers the previous analysis and continues
```

💡 最新の作業を続けるなら `--resume latest` 、過去のセッションを選んで再開するなら `--list-sessions` を使ってください。


## パート2: CLI経由のコード生成

### ステップ2.1: 個別ファイルの生成

コマンドラインから自然言語プロンプトで完全なコードファイルを生成できます：

```bash
# Generate a Python class (using --hide-intermediary-output for clean output)
bob "Create a Python class for managing a shopping cart with add, remove, and calculate total methods" --yolo --hide-intermediary-output > cart.py

# Generate a React component (asking Bob to write to file)
bob "Create a React component for a user profile card with avatar, name, and bio and write it to UserProfile.jsx" --yolo

# Generate a test file (using --hide-intermediary-output)
bob "Create unit tests for the cart.py file using pytest" --yolo --hide-intermediary-output > test_cart.py
```

クリーンなコードファイルを得るには `>` リダイレクトと `--hide-intermediary-output` フラグを使います。またはプロンプトに「[ファイル名]に書き込む」を含めてBobに直接書き込ませることもできます。言語、フレームワーク、要件は具体的に書くほど良い結果が得られます。

### ステップ2.2: 複数の関連ファイルの生成

複数ファイルを持つプロジェクトの場合、完全な構造をそのまま記述します：

```bash
# Generate a complete API module
bob "Create a complete REST API for a todo application in Python with routes, models, and database setup. Provide all necessary files."

# Generate frontend components
bob "Create a set of React components for a dashboard: Header, Sidebar, MainContent, and Footer. Provide each component in a separate code block."
```

プロンプトで完全なプロジェクト構造を記述すると、Bobは複数のコードブロックまたはファイルを返します。各部分を個別に保存するか、Bobに整理を依頼することもできます。

💡 複数ファイルのプロジェクトでは、まずBobにファイル構造を提示してもらい、その後各ファイルを個別に生成すると整理しやすいです。

### ステップ2.3: 保存されたプロンプトで一貫性を保つ

繰り返し使う共通のプロンプトをファイルに保存しておくと便利です：

```bash
# Create a prompt file for consistent API generation
cat > api-prompt.txt << 'EOF'
Create a REST API endpoint with:
- Request validation
- Error handling
- Response formatting
- Proper HTTP status codes
EOF

# Use the saved prompt with specific details (with clean output)
bob "$(cat api-prompt.txt) Create a POST endpoint at /api/users for creating new users" --yolo --hide-intermediary-output > user-endpoint.js

# Or combine with additional context (asking Bob to write to file)
bob "$(cat api-prompt.txt) Create a GET endpoint at /api/products for listing products with pagination and write it to products-endpoint.js" --yolo
```

共通の要件をテキストファイルに保存しておくことで、コードベース全体で一貫性を保てます。プロンプトの繰り返しも減らせます。

## パート3: コード分析とレビュー — ユースケース例

📝 このセクションは、実際のプロジェクトでコード分析とレビューにBobShellをどう使えるかを示すプロンプト例です。これらはあくまで参考例であり、このラボの一部として実行するコマンドではありません。

### ステップ3.1: コード品質分析の例

自然言語プロンプトを使ってコードの品質問題を分析できます。プロジェクトで使えるプロンプト例を以下に示します：

```bash
# Example: Analyze a single file
bob "Analyze the code quality, performance, and security of ./src/app.js"

# Example: Analyze entire directory and save as JSON
bob "Analyze all files in ./src recursively and provide a detailed report" > analysis-report.json

# Example: Get specific metrics
bob "Analyze ./src and provide metrics on complexity, maintainability, and test coverage"
```

Bobに分析してほしい内容を自然言語で記述するだけです。品質、パフォーマンス、セキュリティなどの側面を具体的に書くほど精度が上がります。結果をファイルに保存するには出力リダイレクト（ `>` ）を使ってください。

### ステップ3.2: 自動コードレビューの例

会話型プロンプトで包括的なコードレビューを実行できます。プロンプト例：

```bash
# Example: Review changes in a branch
bob "Review the code changes between main and feature-branch"

# Example: Review specific files with style guide
bob "Review the React components in ./src/components following Airbnb style guide"

# Example: Review with specific focus
bob "Review ./src for code quality issues and provide suggestions in markdown format" > review-report.md
```

レビューしたいコード（ファイル、ディレクトリ、git変更）を記述し、従うべきスタイルガイドや基準（Airbnb、Googleなど）を指定してください。セキュリティ、パフォーマンスなど焦点領域を絞ることもできます。

### ステップ3.3: セキュリティ分析の例

自然言語でコードのセキュリティ脆弱性をスキャンできます。プロンプト例：

```bash
# Example: Security scan with severity focus
bob "Scan ./src for high and critical security vulnerabilities"

# Example: Check for specific vulnerabilities
bob "Check ./src for SQL injection, XSS, and exposed secrets"

# Example: Generate security report
bob "Perform a comprehensive security analysis of ./src and generate an HTML report" > security-report.html
```

重大度レベル（高、クリティカル）や脆弱性タイプを指定できます。出力形式（HTML、markdown、JSON）もリクエストできます。Lab 2で修正した脆弱性と同様のアプローチです。

💡 これらのプロンプトが活きる場面：
- プルリクエストをマージする前のコードレビュー
- CI/CDパイプラインでの自動品質チェック
- 既存コードベースのセキュリティ監査
- コンプライアンスとセキュリティレポートの生成

## パート4: 自動化スクリプト

### ステップ4.1: 自動コードレビュースクリプト

変更されたファイルに対して自動コードレビューを実行するスクリプトを見てみましょう：

ファイル: `scripts/code-review.sh`

```bash
#!/bin/bash
# Automated Code Review Script
# Reviews all changed files in the current branch

# Configuration
BRANCH="${1:-main}"
OUTPUT_DIR="./review-reports"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Get list of changed files
echo "Comparing against branch: $BRANCH"
CHANGED_FILES=$(git diff --name-only "$BRANCH"...HEAD | grep -E '\.(js|jsx|ts|tsx|py|java)$')

if [ -z "$CHANGED_FILES" ]; then
    echo "No code files changed"
    exit 0
fi

echo "Files to review:"
echo "$CHANGED_FILES"

# Review each file
for file in $CHANGED_FILES; do
    if [ -f "$file" ]; then
        echo "Reviewing: $file"
        bob "Review $file for code quality, potential bugs, and best practices. Output in markdown format." > "$OUTPUT_DIR/${file//\//_}_review_$TIMESTAMP.md"
    fi
done

# Generate summary report
echo "Generating summary report..."
bob "Create a summary of all code reviews in $OUTPUT_DIR" > "$OUTPUT_DIR/summary_$TIMESTAMP.md"

echo "Review complete! Reports saved to $OUTPUT_DIR"
```

使い方：
```bash
# Review changes against main branch
./scripts/code-review.sh

# Review changes against different branch
./scripts/code-review.sh develop
```

git diffで変更されたコードファイルをすべて特定し、各ファイルをBobで個別にレビューします。レビュー結果はタイムスタンプ付きのmarkdownファイルとして保存され、最後にサマリーレポートが集約されます。プリコミットやプリマージのチェックに最適です。

### ステップ4.2: バッチリファクタリングスクリプト

ファイル: [`scripts/refactor-batch.sh`](scripts/refactor-batch.sh)

Bobの自然言語インターフェースを使って、複数のファイルを安全にリファクタリングするスクリプトです。

主な機能：
- リファクタリング前の自動バックアップ作成
- 複数のリファクタリングタイプに対応: modernize、optimize、cleanup、security
- 複数ファイルをバッチ処理
- 詳細なログとエラーハンドリング
- 失敗時の自動復元
- 実行前の確認プロンプト

使い方：
```bash
# Modernize code in current directory
./scripts/refactor-batch.sh modernize .

# Optimize performance in src directory
./scripts/refactor-batch.sh optimize ./src

# Clean up code
./scripts/refactor-batch.sh cleanup ./lib

# Fix security issues
./scripts/refactor-batch.sh security ./src
```

出力例：
```
Batch Refactoring
================================
Refactor Type: modernize
Target Directory: ./src
Backup Directory: ./refactor-backups/20240202_143000

Creating Backup ... ✓ Done
Finding Files ... ✓ Found 15 file(s)

Refactoring Files
Processing: ./src/app.js ... ✓ Done
Processing: ./src/utils.js ... ✓ Done
...

Refactoring Complete
Successful: 15
Failed: 0
```

スクリプトは変更前に完全なバックアップを作成し、各ファイルをエラーハンドリング付きで個別に処理します。失敗したファイルはバックアップから自動復元され、すべての変更の詳細なレポートも生成されます。

💡 Bobの自然言語インターフェースがバッチリファクタリングをどう処理しているかは[完全なスクリプト](scripts/refactor-batch.sh)で確認できます。

### ステップ4.3: ドキュメント生成スクリプト

ファイル: [`scripts/generate-docs.sh`](scripts/generate-docs.sh)

Bobの自然言語インターフェースでコードベースの完全なドキュメントを自動生成するスクリプトです。

主な機能：
- APIドキュメントの生成
- アーキテクチャドキュメントの作成
- 使用例の生成
- README、CHANGELOG、CONTRIBUTINGガイドの生成
- FAQとトラブルシューティングガイドの作成
- markdownとHTML出力形式のサポート
- 詳細なログとエラーハンドリング

使い方：
```bash
# Generate docs for current directory (markdown format)
./scripts/generate-docs.sh

# Generate docs for specific directory
./scripts/generate-docs.sh ./src ./documentation

# Generate HTML documentation
./scripts/generate-docs.sh ./src ./docs html
```

出力例：
```
Documentation Generation
================================
Source: ./src
Output: ./docs
Format: markdown

Generating API Documentation ... ✓ Done
Generating Architecture Documentation ... ✓ Done
Generating Usage Examples ... ✓ Done
Generating README ... ✓ Done
Generating Changelog ... ✓ Done
Generating Contributing Guide ... ✓ Done

Documentation Generation Complete
Generated 8 documentation file(s)
```

gitヒストリーからREADMEとchangelogを生成し、markdown・HTMLの両形式に対応しています。生成後はHTMLインデックスページも作られるので、ドキュメントのナビゲーションが楽になります。

💡 自動ドキュメント生成の仕組みは[完全なスクリプト](scripts/generate-docs.sh)を参照してください。

## パート5: CI/CD統合

### ステップ5.1: GitHub Actions統合

完全なGitHub Actionsワークフロー設定は[`ci-cd/github-actions.yml`](ci-cd/github-actions.yml)を参照してください。

主な機能：
- すべてのプルリクエストとmain/developへのプッシュで実行
- CI環境でBob CLIをインストールして設定
- 自然言語プロンプトで変更されたファイルのコードレビューを実行
- セキュリティスキャンと品質分析を実行
- レポートをアーティファクトとしてアップロード
- プルリクエストに直接レビューコメントを投稿
- クリティカルなセキュリティ問題が見つかった場合はビルドを失敗させる

クイックスタート：
1. `ci-cd/github-actions.yml` をリポジトリの `.github/workflows/bob-ci.yml` にコピー
2. `BOB_API_KEY` をリポジトリシークレットに追加（Settings > Secrets and variables > Actions）
3. 必要に応じて品質しきい値と分析レベルをカスタマイズ

### ステップ5.2: GitLab CI統合

完全なGitLab CI設定は[`ci-cd/gitlab-ci.yml`](ci-cd/gitlab-ci.yml)を参照してください。

主な機能：
- マルチステージパイプライン: setup、review、security、quality、documentation、report
- 各ステージはレビュー用のアーティファクトを生成
- セキュリティスキャンはクリティカルな問題でパイプラインを失敗させる
- 品質チェックは最小品質スコアを強制
- 複雑性と依存関係の分析も含む
- mainブランチではドキュメントを自動生成
- すべての結果を含むサマリーレポートを出力

クイックスタート：
1. `ci-cd/gitlab-ci.yml` をリポジトリルートの `.gitlab-ci.yml` にコピー
2. `BOB_API_KEY` をCI/CD変数として追加（Settings > CI/CD > Variables）
3. 必要に応じてアーティファクト保持期間と品質しきい値を設定

### ステップ5.3: Jenkinsパイプライン統合

完全なJenkinsパイプライン設定は[`ci-cd/jenkins-pipeline.txt`](ci-cd/jenkins-pipeline.txt)を参照してください。

主な機能：
- Bob統合を含むマルチステージパイプライン
- Jenkinsを通じて安全に管理される認証情報
- プルリクエスト時のみコードレビューを実行
- セキュリティスキャンはクリティカルな問題でビルドを失敗させる
- 品質分析はしきい値を下回る場合ビルドを不安定としてマーク
- 複雑性と依存関係の分析ステージ
- mainブランチでドキュメントを生成して公開
- カスタマイズ可能な分析レベルのビルドパラメータ
- すべてのステージのアーティファクトをアーカイブ
- 実行後にワークスペースをクリーンアップ

クイックスタート：
1. `ci-cd/jenkins-pipeline.txt` の内容をリポジトリルートの `Jenkinsfile` にコピー
2. Bob APIキーをID `bob-api-key` でJenkins認証情報として追加（Jenkins > Credentials > System > Global credentials）
3. 必要なJenkinsプラグインをインストール: Pipeline、Git、HTML Publisher、Email Extension
4. 自動ビルドのためのwebhookを設定
5. 必要に応じて品質しきい値と分析レベルをカスタマイズ

## パート6: 高度なワークフロー

### ステップ6.1: Bobと他のツールの組み合わせ

Bobを他のCLIツールと組み合わせると強力なワークフローを作れます：

```bash
# Find TODO comments and create tasks
grep -r "TODO" ./src | bob "Convert these TODO comments into GitHub issues with proper formatting in JSON format" --hide-intermediary-output > issues.json

# Analyze git history and generate insights
git log --since="1 month ago" --pretty=format:"%h %s" | bob "Analyze these commit messages and provide insights on development patterns in markdown format" --hide-intermediary-output > dev-insights.md

# Process test results
npm test -- --json | bob "Analyze these test results and suggest improvements in markdown format" --hide-intermediary-output > test-analysis.md

# Code coverage analysis
npm run coverage -- --json | bob "Create a coverage report with recommendations for improving test coverage in markdown format" --hide-intermediary-output > coverage-report.md
```

標準ツールからの出力をBobにパイプすることで、AI分析を組み込んだワークフローを作れます。非構造化データを実行可能なインサイトに変換し、レポートや推奨事項を自動生成できます。

### ステップ6.2: カスタムワークフロー例

完全なプリコミットワークフローの例：

```bash
#!/bin/bash
# Pre-commit workflow with Bob

echo "Running pre-commit checks with Bob..."

# 1. Format code
echo "Formatting code..."
bob "Format all code in ./src directory using Prettier style guidelines"

# 2. Lint code
echo "Linting code..."
bob lint ./src --fix

# 3. Review changes
echo "Reviewing changes..."
bob "Review uncommitted changes (git diff HEAD) for code quality issues. Output in markdown format." --hide-intermediary-output > pre-commit-review.md

# 4. Security check
echo "Security scan..."
bob "Perform security scan of ./src focusing on high and critical severity vulnerabilities. Output in JSON format." --hide-intermediary-output > security-check.json

# 5. Check for critical issues
CRITICAL=$(jq '.critical | length' security-check.json)
if [ "$CRITICAL" -gt 0 ]; then
    echo "❌ Critical security issues found! Commit blocked."
    cat security-check.json
    exit 1
fi

# 6. Run tests
echo "Running tests..."
npm test

# 7. Generate commit message suggestion
echo "Generating commit message suggestion..."
bob "Based on the staged changes, suggest a conventional commit message" --hide-intermediary-output > suggested-commit.txt

echo "✅ Pre-commit checks passed!"
echo "Suggested commit message:"
cat suggested-commit.txt
```

このワークフローは、コードのフォーマット・リント・レビュー・セキュリティスキャン・テスト実行・コミットメッセージ提案までを一連の流れで自動化します。クリティカルなセキュリティ問題があればコミット自体をブロックするので、コード品質をコミット時に確保できます。

## パート7: ベストプラクティス

### 7.1: BobShellのベストプラクティス

1. プロンプトを具体的に書いてください。リクエストが具体的なほど良い結果が得られます
   ```bash
   # Good
   bob generate "Create a React component for user authentication with email and password fields, validation, and error handling"
   
   # Less specific
   bob generate "Create a login form"
   ```

2. 出力形式を使い分けましょう
   ```bash
   # JSON for programmatic processing
   bob "Analyze ./src and provide results in JSON format" --hide-intermediary-output > analysis.json
   
   # Markdown for documentation
   bob "Review ./src for code quality and output in markdown format" --hide-intermediary-output > review.md
   
   # HTML for reports
   bob "Perform security scan of ./src and output in HTML format" --hide-intermediary-output > security-report.html
   ```

> 💡 自動最適化について
> BobShellコマンドを実行すると、Bobの[インテリジェントリソース最適化](../bob-differentiators.md#2--intelligent-resource-optimization)が各タスクに最適なモデルを自動的に選択します。使用するモデルを指定する必要はありません。品質とコストの両方を透過的に最適化してくれます。

3. git統合を使って変更されたコードだけをレビューしましょう
   ```bash
   # Review changes in current branch
   bob "Review code changes between main and HEAD branches"

   # Review uncommitted changes
   bob "Review uncommitted changes (git diff HEAD)"
   ```

4. 繰り返し操作にはキャッシングを設定しましょう
   ```bash
   # Enable caching
   bob config set cache-enabled true
   bob config set cache-ttl 3600
   ```

### 7.2: 自動化のベストプラクティス

1. 自動リファクタリングの前に必ずバックアップを作成してください
2. 自動変更を実行する前にバージョン管理にコミットしておいてください
3. 自動化後は常にテストを実行して変更が機能するか確認してください
4. 自動操作のログをすべて保持してください
5. スクリプトに適切なエラーハンドリングを実装してください

### 7.3: CI/CDのベストプラクティス

1. Bob APIキーにはシークレット管理を使ってください
2. 品質とセキュリティのしきい値を明確に定義してください
3. 監査とレビューのためにレポートを保持してください
4. クリティカルな問題が見つかったらパイプラインを早期に止めてください
5. レビュー結果をPRコメントとしてフィードバックしてください

> 🔍 CI/CDでのBob Findingsについて
> 自動セキュリティスキャンとコード品質チェックには、[Bob Findings](../bob-differentiators.md#3--bob-findings-automated-analysis-engine)をCI/CDパイプラインに組み込みましょう。本番環境に到達する前に脆弱性とコード問題を検出でき、パイプラインレポートに具体的な修復推奨事項が含まれます。

## 演習

### 演習1: カスタムレビュースクリプトの作成

以下を行うスクリプトを作成してみてください：
1. ディレクトリ内のすべてのPythonファイルをレビュー
2. PEP 8準拠をチェック
3. 潜在的なバグを特定
4. サマリーレポートを生成

### 演習2: CI/CDパイプラインの構築

以下を行う完全なCI/CDパイプラインをセットアップしてください：
1. プルリクエストで実行
2. コードレビューを実行
3. セキュリティスキャンを実行
4. コード品質をチェック
5. 結果をPRコメントとして投稿

### 演習3: ドキュメントの自動化

以下を行うワークフローを作成してください：
1. APIドキュメントを生成
2. 使用例を作成
3. READMEを更新
4. ドキュメント変更をコミット

## トラブルシューティング

### 一般的な問題

1. Bob CLIが見つからない
   ```bash
   # Verify installation
   which bob
   
   # Reinstall if needed
   npm install -g @ibm/bob-cli
   ```

2. 認証エラー
   ```bash
   # Check API key configuration
   bob config get api-key
   
   # Reconfigure if needed
   bob config set api-key YOUR_API_KEY
   ```

3. レート制限
   ```bash
   # Check rate limit status
   bob status
   
   # Use caching to reduce API calls
   bob config set cache-enabled true
   ```

## 次のステップ

- Lab 5: BobでJavaアプリケーションをモダナイズする方法を学ぶ
- Lab 6: カスタムMCPサーバーとモードを作成する
- ドキュメントで高度なBobShell機能を探索する
- 自動化スクリプトをチームと共有する

## 追加リソース

- [BobShellドキュメント](https://ibm.com/bob/docs/cli)
- [CI/CD統合ガイド](https://ibm.com/bob/docs/cicd)
- [自動化例リポジトリ](https://github.com/ibm/bob-automation-examples)
- [BobShell APIリファレンス](https://ibm.com/bob/docs/api)

---

問題が発生した場合は、上記のトラブルシューティングセクションを確認するか、BobShellドキュメントを参照してください。解決しない場合はBobコミュニティフォーラムで質問するか、IBMサポートに連絡してください。

このラボの改善に向けて、うまくいったことと改善できることについてフィードバックをいただけると助かります。
