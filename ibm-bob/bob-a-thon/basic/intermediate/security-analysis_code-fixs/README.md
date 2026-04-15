# 演習 2: セキュリティ分析とコード修正
## Security & Code Analysis - Identify and fix security vulnerabilities

## 概要

この実習では、Bob を使用して既存のコードを分析し、セキュリティ上の脆弱性を特定して修正を実装します。SQL インジェクション、XSS、ハードコードされた秘密情報などの一般的なセキュリティ上の問題点を認識し、Bob のさまざまなモードを使用してそれらを修正する方法を学びます。

> **🔍 Bobの差別化要素: [Bob Findings](../bob-differentiators.md#3--bob-findings-automated-analysis-engine)**
> このラボでは、Bobの自動セキュリティおよびコード品質分析エンジンであるBob Findingsを紹介します。単純なリンターとは異なり、Bob Findingsは継続的かつプロアクティブな分析を提供し、具体的な修正推奨事項、深刻度評価、コード例を示します。まるでセキュリティ専門家がリアルタイムでコードをレビューしているようなものです！

**所要時間**: 45分
**難易度**: 中級

## 分析対象

意図的にセキュリティ上の欠陥が仕込まれた、脆弱なToDoアプリ:
- **SQL インジェクション** データベースクエリにおける脆弱性
- **クロスサイトスクリプティング (XSS)** フロントエンドコード
- **ハードコードされた秘密情報** と認証情報
- **入力検証が欠落しています**
- **安全でないエラー処理**

## 学習目標

この実習を終えるまでに、あなたは以下のことができるようになります。
- ✅ Askモードを使用して既存のコードベースを理解する
- ✅ Architectモードを使用してバグを特定し、修正計画を立てる
- ✅ SQLインジェクションの脆弱性を認識する
- ✅ XSS攻撃ベクトルを特定する
- ✅ ハードコードされた秘密情報と認証情報を見つける
- ✅ Codeモードを使用してセキュリティ修正を実装する
- ✅ 安全なコーディングのベストプラクティスを適用する

## 前提条件

始める前に、以下のものを用意してください:
- [ ] 演習 1を完了していること（またはFlaskとJavaScriptに精通していること）
- [ ] Python 3.8以降がインストールされている
- [ ] Bobがインストールされ、動作している
- [ ] 基本的なウェブセキュリティの概念を理解している

## 演習の構造

```
演習 2 タイムライン (45分)
├── Step 1: コードの探索 (10分)
├── Step 2: バグの特定 (10分)
├── Step 3: セキュリティ分析 (15分)
└── Step 4: 修正の実装 (10分)
```

---

## Step 1: Askモードを使ったコード探索（10分）

### 脆弱なコードベースの理解

この `vulnerable-app/` ディレクトリには、意図的にセキュリティ上の問題が仕込まれたToDoアプリケーションが含まれています。BobのAskモードを使ってコード構造を理解してみましょう。

### 1.1: Askモードに切り替える

Bobを開いて **Ask モード** (❓)に切り替えます。

### 1.2: バックエンドを探索する

**Bobへのプロンプト:**

```
lab2/vulnerable-app/backend/ のコードを分析し、次の点を説明してください。
1. アプリケーション全体の構造はどのようになっていますか？
2. データベースへのクエリはどのように組み立てられていますか？
3. ユーザー入力はどのように扱われていますか？
4. どのようなセキュリティ対策が実装されていますか？
```

**注目すべき点:**

Bobは以下を特定する必要があります。
- REST APIエンドポイントを備えたFlaskアプリケーション
- ユーザー入力を直接SQL文字列に埋め込み ⚠️
- ハードコードされたデータベース認証情報 ⚠️
- 入力検証の欠如 ⚠️

### 1.3: フロントエンドを探索する

**Bobへのプロンプト:**

```
lab2/vulnerable-app/frontend/ にあるフロントエンドコードを分析し、以下の点について説明してください。
1. ユーザー入力はUIにどのように表示されますか？
2. リスクのあるDOM操作メソッドを使用してますか？
3. APIからのデータはどのようにレンダリングされますか？
```

**注目すべき点:**

Bobは以下を特定する必要があります。
- `innerHTML` を使用してユーザーコンテンツのレンダリングに使用 ⚠️
- 入力データのサニタイズが行われていません ⚠️
- ユーザー入力データを直接DOMに挿入 ⚠️

### 1.4: 特定の機能について質問する

**Bobへのプロンプト:**

```
app.pyにあるsearch_todos()関数について説明してください。
この関数は何をするのか、またセキュリティ上の懸念事項はありますか？
```

**期待される応答:**

Bobは、この関数がSQLクエリを構築するために文字列フォーマットを使用しているため、SQLインジェクション攻撃に対して脆弱であることを説明すべきです。

**💡 重要な学習内容**: Askモードは、馴染みのないコードを理解したり、物事がどのように機能するかについての説明を得るのに最適です。

---

## Step 2: 計画モードによるバグの特定（10分）

それでは、アーキテクトモードを使用して、すべての問題を体系的に特定していきましょう。

### 2.1: Planモードに切り替える

質問モードから **Plan モード** に変更します(🎯).

### 2.2: セキュリティ分析の依頼

> **💡 Bob Findingsの活用事例**
> Bob Findings は、セキュリティの脆弱性、コード品質の問題、コンプライアンス違反を自動的にスキャンできます。これからリクエストする分析は、Bob の[セキュリティ脆弱性検出](../bob-differentiators.md#security-vulnerability-detection) 機能を示すもので、基本的な静的分析を超えて、状況に応じた推奨事項を提供します。

**Bobへのプロンプト:**

```
lab2/vulnerable-app/ のコードベースを分析し、セキュリティ脆弱性を特定してください。
以下の項目を含む包括的なレポートを作成してください。
1. 発見されたすべてのセキュリティ問題のリスト
2. 各セキュリティ問題の深刻度評価（重大/高/中/低）
3. 各脆弱性の潜在的な影響
4. 各問題に対する推奨される修正方法
5. 修正の優先順位
```

**期待される出力:**

Bobは次のような構造化された分析を提供する必要があります。

```
lab2/vulnerable-app セキュリティ脆弱性レポート
========================

🔴 重大な脆弱性（即座の対応必須）
1. SQLインジェクション
   - 場所: app.py
   - 問題: f"SELECT * FROM todos WHERE title LIKE '%{query}%'"
   - 影響: データベース全体の侵害、データ削除・窃取
   - 修正: ORMまたはパラメータ化クエリ使用

2. ハードコードされた機密情報
   - 場所: config.py
   - 問題: DB認証情報、APIキー、AWSキーをコードに直接記述
   - 影響: 全システムへのアクセス権限漏洩
   - 修正: 環境変数への移行

3. 機密情報のAPI公開
   - 場所: app.py
   - 問題: /api/admin/configで全設定を認証なしで公開
   - 影響: 認証情報の即座の漏洩
   - 修正: エンドポイント削除または認証追加

4. XSS脆弱性
   - 場所: app.js
   - 問題: innerHTMLでユーザー入力を直接挿入
   - 影響: セッションハイジャック、クッキー窃取
   - 修正: textContent使用またはDOMPurify導入

🟠 高リスクの脆弱性
5. 入力検証の欠如
   - 場所: app.py
   - 影響: DoS攻撃、データ破損
   - 修正: バリデーションライブラリ（Marshmallow等）導入

6. 詳細なエラー情報の漏洩
   - 場所: app.py
   - 影響: システム構造の露呈、攻撃の容易化
   - 修正: 一般的なエラーメッセージのみ返却

7. 認証・認可の欠如
   - 場所: 全エンドポイント
   - 影響: 誰でもデータの作成・変更・削除が可能
   - 修正: JWT認証の実装

8. クライアント側検証の欠如
   - 場所: app.js 全体
   - 影響: 不正データの送信
   - 修正: フロントエンドバリデーション追加
```

### 2.3: 修復計画の作成

**Bobへのプロンプト:**

```
セキュリティ分析に基づき、これらの問題を修正するための詳細な計画を作成してください。
以下の項目を含めてください。
1. 修正の順序（重要度の高いものから順に）
2. 変更が必要なファイル
3. 必要な具体的なコード変更
4. テスト戦略
```

**Bobの返答:**

Bobは必要な修正点をすべて網羅した詳細なTODOリストを作成します。これは、Bobが複雑な問題を具体的な行動ステップに分解する能力を持っていることを示しています。

**⚠️ 重要**: Bobが作成したTODOリストを確認してください。ただし、**まだ修正は実装しないでください。** 次のステップで、変更を加える前に各脆弱性の種類を詳細に検討します。これにより、修正内容とその理由を確実に理解できます。

**💡 重要な学習ポイント**: Planモードは、分析、計画、問題解決のための体系的なアプローチの作成に優れています。TODOリストは、実装フェーズのロードマップとして機能します。

---

## Step 3: セキュリティ脆弱性の詳細分析（15分） - オプション

この手順では、各脆弱性の種類について詳しく説明します。これらのセキュリティ概念を既に理解している場合は、[Step 4：コードモードを使用した修正の実装](#step-4%3A-コードモードを使用した修正の実装（10分）)に進んでください。

**この詳細な解説で学べること:**
- SQLインジェクション攻撃の仕組み
- XSS脆弱性がどのように悪用されるか
- ハードコードされた秘密情報が危険な理由
- 安全なコーディングのためのベストプラクティス

それでは、それぞれの脆弱性の種類を詳しく見ていきましょう。

### 3.1: SQLインジェクションの脆弱性

**場所**: `vulnerable-app/backend/app.py:128`

**脆弱なコード:**
```python
# 🔴 危険！ユーザー入力を直接SQL文字列に埋め込み
sql = f"SELECT * FROM todos WHERE title LIKE '%{query}%'"
result = db.session.execute(sql)
```

**問題:**

攻撃者は次のような悪意のあるクエリを送信する可能性があります：
```
GET /api/todos/search?q='; DROP TABLE todos; --
```

その結果、生成されるSQL：
```sql
SELECT * FROM todos WHERE title LIKE '%'; DROP TABLE todos; --%'
→ todosテーブルが削除される
```

**Bobへのプロンプト（Askモード）:**

```
app.pyにあるsearch_todos()関数について説明してください。
この関数は何をするのか、またセキュリティ上の懸念事項はありますか？
```

**修正方法:**

SQLAlchemy ORM使用
```python
# ✅ 安全な実装
@app.route('/api/todos/search', methods=['GET'])
def search_todos():
    query = request.args.get('q', '')
    
    # 入力検証
    if len(query) > 100:
        return jsonify({'error': 'Query too long'}), 400
    
    # ORM使用（自動的にパラメータ化される）
    todos = Todo.query.filter(
        Todo.title.like(f'%{query}%')
    ).all()
    
    return jsonify([todo.to_dict() for todo in todos]), 200
```

### 3.2: クロスサイトスクリプティング（XSS）の脆弱性

**場所**: `vulnerable-app/frontend/app.js:150-232`

**脆弱なコード:**
```javascript
function displayTodos(todos) {
    const todosList = document.getElementById('todos-list');
    
    // 🔴 脆弱性: innerHTMLでユーザー入力を直接挿入
    todosList.innerHTML = todos.map(todo => createTodoHTML(todo)).join('');
}

function createTodoHTML(todo) {
    // 🔴 脆弱性: エスケープなしでユーザー入力を埋め込み
    return `
        <div class="todo-item">
            <h3 class="todo-title">${todo.title}</h3>
            <p class="todo-description">${todo.description}</p>
        </div>
    `;
}
```

**攻撃例:**
```html
<script>alert('XSS Attack!')</script>
```

**実行される処理**
```html
// createTodoHTML()が生成するHTML
`<h3 class="todo-title"><script>alert('XSS Attack!')</script></h3>`

// innerHTML経由でDOMに挿入
todosList.innerHTML = `<div class="todo-item">
    <h3 class="todo-title"><script>alert('XSS Attack!')</script></h3>
</div>`;

// ブラウザがスクリプトを実行
// → ページ読み込み時に即座にアラートが表示される
```


**Bobへのプロンプト（Askモード）:**

```
displayTodo() 関数における XSS 脆弱性について説明してください。
悪意のあるペイロードの例と、それがどのように実行されるかを示してください。
```

**修正方法:**

`innerHTML`の代わりに`textContent`を使用する:
```javascript
function displayTodos(todos) {
    const todosList = document.getElementById('todos-list');
    todosList.innerHTML = '';  // クリア
    
    todos.forEach(todo => {
        const div = document.createElement('div');
        div.className = 'todo-item';
        
        const title = document.createElement('h3');
        title.className = 'todo-title';
        title.textContent = todo.title;  // ✅ 安全: HTMLとして解釈されない
        
        const desc = document.createElement('p');
        desc.className = 'todo-description';
        desc.textContent = todo.description;  // ✅ 安全
        
        div.appendChild(title);
        if (todo.description) div.appendChild(desc);
        
        todosList.appendChild(div);
    });
}
```

### 3.3: ハードコードされた秘密情報の脆弱性

**場所**: `vulnerable-app/backend/config.py`

**脆弱なコード:**
```python
# 🔴 危険: 秘密情報をコードに直接記述
DATABASE_URL = "postgresql://admin:SuperSecret123@localhost:5432/todos_db"
API_KEY = "sk_live_abc123xyz789_this_is_a_secret_key"
SECRET_KEY = "my-super-secret-key-12345"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
EMAIL_PASSWORD = "EmailPassword123!"
JWT_SECRET_KEY = "jwt-secret-key-not-secure"
```

**問題:**

- バージョン管理システムへの永久保存
- コードアクセス権を持つ人は誰でもシステムへのフルアクセス権を持つ
- 環境間での秘密情報の共有
- コードの変更なしに認証情報を変更することはできません

**Bobへのプロンプト（Askモード）:**

```
ハードコードされた秘密情報はなぜセキュリティリスクとなるのか？
アプリケーションにおける秘密情報の管理に関するベストプラクティスとは何か？
```

**解決策:**

環境変数を使用する:
```python
import os
from dotenv import load_dotenv

load_dotenv()

# セキュア: 環境からロード
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')

# シークレットがロードされているか検証する
if not all([DATABASE_URL, API_KEY, SECRET_KEY]):
    raise ValueError("Missing required environment variables")
```

`.env` ファイルを作成します（絶対にコミットしないでください！）:
```
DATABASE_URL=postgresql://admin:SuperSecret123@localhost/todos
API_KEY=sk_live_abc123xyz789
SECRET_KEY=my-secret-key-12345
```

### 3.4: 脆弱性のテスト

**⚠️ 警告**: 必ずご自身のシステムでテストしてください！

**SQLインジェクションのテスト:**
```bash
# Try to inject SQL
curl "http://localhost:5001/api/todos/search?q=test'%20OR%20'1'='1"
```

**XSSテスト:**
```bash
# スクリプトを使用してToDoを作成する
curl -X POST http://localhost:5001/api/todos \
  -H "Content-Type: application/json" \
  -d '{"title":"警告(\"XSS\")","description":"testです"}'
```

---

## Step 4: コードモードを使用した修正の実装（10分）

それでは、Bobの Codeモードを使ってすべての脆弱性を修正しましょう。

### 4.1: Codeモードに切り替える

**Code モード** に切り替えます(💻).

### 4.2: SQLインジェクションの修正

**Bobへのプロンプト:**

```
vulnerable-app/backend/app.py の SQL インジェクション脆弱性を修正します。
文字列のフォーマットを SQLAlchemy を使用したパラメータ化クエリに置き換えます。
```

Bobは `search_todos()` を安全なクエリを使用するように関数を修正する必要があります。
Bobが修正を反映するには、** python app.py ** を停止して再起動します。

### 4.3: XSS脆弱性の修正

**Bobへのプロンプト:**

```
vulnerable-app/frontend/app.js の XSS 脆弱性を修正します。
innerHTML の使用を textContent を使用した安全な DOM 操作に置き換えます。
ユーザー生成コンテンツを表示するすべての関数を更新します。
```

### 4.4: ハードコードされた秘密情報を修正

**Bobへのプロンプト:**

```
vulnerable-app/backend/config.py にハードコードされている秘密情報を修正してください。
1. 秘密情報を環境変数に移動します。
2. プレースホルダー値を含む .env.example ファイルを作成します。
3. requirements.txt に python-dotenv を追加します。
4. 環境変数から読み込むようにコードを更新します。
```

### 4.5: 入力検証機能の追加

**Bobへのプロンプト:**

```
ToDo作成エンドポイントに、入力値の検証機能を追加してください。
検証項目：
- タイトルは必須項目であり、空欄であってはなりません。
- タイトルの長さは1文字以上200文字以下である必要があります。
- 説明文の長さは1000文字未満である必要があります。
無効な入力に対しては、適切なエラーメッセージを返します。
```

### 4.6: 修正内容の確認

**重要**: Bobは `lab2/vulnerable-app/` 内のファイルに直接修正を加えました（別のソリューションフォルダではなく）。脆弱なコードは安全なコードに置き換えられています。

アプリケーションを実行して、修正内容をテストします:

```bash
# バックエンドを起動 (修正が加えられた vulnerable-app ディレクトリから)
cd lab2/vulnerable-app/backend
python -m venv venv
source venv/bin/activate  # または Windows の場合は venv\Scripts\activate
pip install -r requirements.txt
python app.py # PORTが競合する場合は代わりに以下を実行してください。
FLASK_RUN_PORT=8080 flask run

# フロントエンドを開く (vulnerable-app ディレクトリから)
cd ../frontend
# ブラウザで index.html を開く
```

**セキュリティテスト:**
1. SQLインジェクションを試してみてください。安全に失敗するはずです（データ漏洩はありません）。
2. XSSペイロードを試してみてください。プレーンテキストとして表示されるはずです（実行はされません）。
3. コード内に機密情報が含まれていないか確認する（config.pyが環境変数を使用していることを確認する）
4. 入力値の検証テスト（タイトルが空の場合、タイトルが長すぎる場合など）

**変更前と変更後を比較する:**
元の脆弱なコードを確認したい場合は、修正のリファレンス実装が含まれている `lab2/solution/` ディレクトリを確認してください。

---

## おめでとうございます！ 🎉

演習2を無事完了しました！以下のことを学習しました：

- ✅ Askモードを使用して既存のコードを理解する
- ✅ セキュリティ分析にはArchitectモードを使用する
- ✅ SQLインジェクションの脆弱性を特定する
- ✅ XSS攻撃ベクトルを認識する
- ✅ ハードコードされた秘密情報を見つけて修正する
- ✅ 安全なコーディング手法を導入する
- ✅ Codeモードを使用してセキュリティ問題を修正します

> **🎯 Bob Findingsの活用事例 **
> このラボでは、Bob の [自動セキュリティ分析](../bob-differentiators.md#security-vulnerability-detection) c機能を体験しました。Bob Findings は、コードの脆弱性を継続的に監視し、実行可能な修正ガイダンスを提供します。このプロアクティブなアプローチにより、セキュリティ問題が本番環境に及ぶ前に発見できるため、リスクと技術的負債を軽減できます。

## セキュリティに関するベストプラクティスから学んだこと

### 1. SQLインジェクション対策
- ✅ 常にパラメータ化クエリを使用する
- ✅ ユーザー入力をSQLに連結しないでください
- ✅ ORM機能（SQLAlchemyなど）を使用する
- ✅ 入力内容を検証し、サニタイズする

### 2. XSS対策
- ✅ `innerHTML` の代わりに `textContent` を使う
- ✅ 表示前にユーザー入力をサニタイズする
- ✅ コンテンツセキュリティポリシーのヘッダーを使用する
- ✅ 出力を適切にエンコードする

### 3. 機密情報の管理
- ✅ 認証情報をハードコーディングしない
- ✅ 環境変数を使用する
- ✅ 秘密管理サービスを利用する
- ✅ 秘密を定期的にローテーションする
- ✅ 機密情報をバージョン管理システムにコミットしてはいけない

### 4. 入力値の検証
- ✅ すべてのユーザー入力を検証する
- ✅ ホワイトリスト検証を使用する
- ✅適切な長さ制限を設定する
- ✅ 明確なエラーメッセージを返す

## 比較: ビフォー＆アフター

### ビフォー (脆弱)
```python
# SQL インジェクションリスク
sql = f"SELECT * FROM todos WHERE title LIKE '%{query}%'"

# Hardcoded secrets
DATABASE_URL = "postgresql://admin:password@localhost/db"

# XSS リスク
element.innerHTML = `<h3>${userInput}</h3>`
```

### アフター (セキュア)
```python
# 安全なパラメータ化されたクエリ
results = Todo.query.filter(Todo.title.like(f'%{query}%')).all()

# 環境変数
DATABASE_URL = os.getenv('DATABASE_URL')

# 安全なDOM操作
element.textContent = userInput
```

## 追加のセキュリティリソース

### OWASP Top 10
1. Injection
2. Broken Authentication
3. 機密データの漏洩
4. XML外部エンティティ（XXE）
5. アクセス制御の不具合
6. セキュリティ設定ミス
7. クロスサイトスクリプティング（XSS）
8. 安全でない Deserialization
9. 既知の脆弱性を持つコンポーネントの使用
10. ログ記録と監視が不十分

### おすすめ Reading
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/latest/security/)
- [JavaScript Security Best Practices](https://developer.mozilla.org/en-US/docs/Web/Security)

## 次のステップ

### 学習を続ける
- **[演習 3: Code Translation →](../lab3/README.md)** - 言語間でコードを翻訳する方法を学ぶ

### Practice More
以下の追加の脆弱性を見つけて修正してみてください:
1. **CSRF** - CSRF対策を追加する
2. **Authentication** - ユーザー認証を実装する
3. **Authorization** - ロールベースのアクセス制御を追加する
4. **Rate Limiting** - Prevent brute force attacks
5. **HTTPS** - 安全な接続を強制する

## トラブルシューティング

### バックエンドの問題

**問題**: シークレットを修正した後、インポートエラーが発生する
```bash
# python-dotenv をインストール
pip install python-dotenv
```

**問題**: 環境変数が読み込まれない
```bash
# .env ファイルが存在するか確認します
ls -la .env

# .env ファイルの書式を確認 (=前後にスペースが入らないようにしてください)
DATABASE_URL=value
```

### フロントエンドの問題

**問題**: 修正後もXSSが依然として機能している
- `innerHTML` ではなく `textContent` が使われていることを確認する
- すべてのユーザー入力表示ポイントを確認する
- ブラウザのキャッシュをクリアする

### テストに関する問題

**問題**: SQLインジェクションをテストできない
- まず脆弱性のあるバージョンでテストしていることを確認します
- バックエンドが実行されていることを確認します
- エンドポイントURLが正しいことを確認します

## フィードバック

この実験室はいかがでしたか？ぜひご意見をお聞かせください:
- 脆弱性は全て見つかりましたか？
- 説明は分かりやすかったですか？
- 他にどのようなセキュリティ関連のトピックにご興味がありますか？

---

**次のチャレンジに挑戦する準備はできましたか？** → [演習3 開始: Code Translation](../lab3/README.md)

*最終更新日: 2026年4月*