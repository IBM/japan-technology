# Lab 3: PythonからJavaScriptへのコード変換

## 概要

このラボでは、Bobを使ってPythonのデータ処理スクリプトをJavaScript（Node.js）に変換します。機能を維持しながら、言語固有のベストプラクティスを両方の言語で適用する方法を学びます。

> Bobの差別化要因: このラボでは、Bobが各変換タスクに適したAIモデルを自動的に選択します。複雑な言語機能のマッピングには精度のために強力なモデルを、単純な構文変換には速度のために軽量なモデルを使います。この 自動モデル選択は透過的に行われ、品質とコストの両方を最適化します。

所要時間: 45分  
難易度: 中級

## 変換する内容

以下の機能を持つPythonデータ処理スクリプトをJavaScript（Node.js）に変換します。

- CSVファイルの読み込み
- 統計計算の実行
- 結果のJSON出力
- 型ヒントと最新のPython機能の使用

## 学習目標

このラボを終えると、BobのAsk・Plan・Agentモードをコード変換に使いこなせるようになります。具体的には、Pythonの型ヒント・コンテキストマネージャー・リスト内包表記をJavaScript同等物にマッピングし、非同期パターンの違いを理解した上で両言語のベストプラクティスを適用できます。

## 前提条件

開始する前に以下を確認してください。

- Lab 1とLab 2を完了している（またはBobのモードに精通している）
- Python 3.8+がインストールされている
- Node.js 14+がインストールされている
- Bobがインストールされ、実行されている
- PythonとJavaScriptの基礎を理解している

## ラボの構成

```
Lab 3 タイムライン（45分）
├── ステップ1: Pythonコードの分析（10分）
├── ステップ2: 変換戦略の計画（10分）
├── ステップ3: 変換の実装（20分）
└── ステップ4: 検証と比較（5分）
```

---

## ステップ1: AskモードでPythonコードを分析する（10分）

変換を始める前に、ソースコードを徹底的に理解します。ここを省くと後で必ず手戻りが出ます。

### 1.1 Pythonコードを読む

`source/data_processor.py` を開いて構造を確認します。注目すべき箇所は次の通りです。

- クラスベースの設計
- 型ヒント（`: str`、`-> Dict`）
- コンテキストマネージャー（`with open()`）
- リスト内包表記と辞書操作
- CSVとJSONの処理

### 1.2 Askモードに切り替える

Bobを開き、Askモードに切り替えます。

### 1.3 コード構造を理解する

次のプロンプトをBobに送ります。

```
source/data_processor.pyのPythonコードを分析して、以下を説明してください:
1. このコードの全体的な目的は何ですか？
2. 主なコンポーネントとその責任は何ですか？
3. どのようなPython固有の機能が使用されていますか？
4. 主要なデータ構造とアルゴリズムは何ですか？
```

Bobはこのコードがロード・分析・エクスポートのメソッドを持つ `DataProcessor` クラスを中心に構成されていること、型ヒントやリスト内包表記といったPython固有の機能が使われていることを説明します。

### 1.4 変換の課題を洗い出す

```
このPythonコードをJavaScriptに変換する際に直面する可能性のある課題は何ですか？
以下を考慮してください:
- 言語構文の違い
- 組み込みライブラリの違い
- 非同期/同期パターン
- 型システムの違い
```

Bobが挙げる主な課題は次の5点です。

1. ファイルI/O: Pythonの `with open()` とNode.jsの非同期ファイル操作
2. CSV解析: Pythonの `csv` モジュールとJavaScriptライブラリ
3. 型ヒント: PythonからJSDocまたはTypeScriptへの変換
4. リスト内包表記: Pythonの簡潔な構文とJavaScriptの配列メソッド
5. 同期vs非同期: PythonのデフォルトI/OとNode.jsの非同期パターン

---

## ステップ2: PlanモードでPythonコードを分析する（10分）

課題が見えたら、詳細な変換計画を立てます。

### 2.1 Planモードに切り替える

Askモードから Planモードに変更します。

### 2.2 変換マッピングを作る

```
PythonデータプロセッサーをJavaScriptに変換するための詳細な変換計画を作成してください。
以下を含めてください:
1. 機能ごとのマッピング（Python → JavaScript）
2. ライブラリ/モジュールの同等物
3. 必要な構文変換
4. 推奨されるJavaScriptパターン
5. JavaScriptバージョンのファイル構造
```

Bobが出力するマッピングは以下のようになります。

| Python機能 | JavaScript同等物 | 注記 |
|---|---|---|
| `class DataProcessor` | `class DataProcessor` | クラス構文は両言語で同様 |
| `def __init__(self, filename: str)` | `constructor(filename)` | コンストラクタ構文が異なる |
| `with open(file)` | `fs.promises.readFile()` | JavaScriptでは非同期 |
| `csv.DictReader` | `csv-parser` ライブラリ | npmパッケージが必要 |
| リスト内包表記 | `Array.map()`、`Array.filter()` | より冗長になる |
| 型ヒント | JSDocコメント | オプションだが推奨 |
| `if __name__ == '__main__'` | `if (require.main === module)` | パターンが異なる |

### 2.3 モジュール構造を設計する

```
変換されたコードのJavaScriptモジュール構造を設計してください。
以下を使うべきですか:
- ES6モジュールまたはCommonJS？
- クラスまたは関数型アプローチ？
- Async/awaitまたはPromise？
- 追加のエラー処理？
```

Bobの推奨はNode.js互換性を考慮したCommonJS、ES6クラス構文、非同期コードをシンプルに保つasync/await、そして包括的なエラー処理です。

### 2.4 依存関係を特定する

```
JavaScriptバージョンに必要なnpmパッケージは何ですか？
```

必要なパッケージは `csv-parser`（CSVファイルの解析）のみです。`fs` はNode.js組み込みなので追加インストール不要です。

> コンテキスト管理の実践
> この変換作業を通じて、Bobは動的コンテキストウィンドウ圧縮を使ってPythonとJavaScriptの両コードベースをメモリ内で効率的に管理します。これによりトークン使用量を抑えながら、両方の完全なコンテキストを維持できます。

---

## ステップ3: Agentモード（Codeモード）でPythonコードを変換する（20分）

計画が整ったら実際に変換します。

### 3.1 Agentモードに切り替える

Agentモードに変更します。

### 3.2 パッケージ設定を作る

```
以下を含むJavaScriptデータプロセッサー用のpackage.jsonファイルを作成してください:
- 名前: data-processor
- バージョン: 1.0.0
- 依存関係: csv-parser
- メインエントリポイント: data_processor.js
- プロセッサーを実行するためのスクリプト
```

### 3.3 クラス全体を変換する

```
DataProcessorクラス全体をPythonからJavaScriptに変換してください。
以下を含めてください:
- Pythonの__init__に相当するコンストラクタ
- 同等の機能を持つすべてのメソッド
- 型ドキュメント用のJSDocコメント
- ファイル操作用のasync/await
- エラー処理
- メイン実行ロジック
```

Bobはすべてのメソッドを含む完全なJavaScript実装を一度に作成します。生成されるコードの骨格は次の通りです。

```javascript
/**
 * DataProcessor - CSVファイルを分析し、統計を生成します
 * PythonからJavaScriptに変換
 */
const fs = require('fs').promises;
const { createReadStream } = require('fs');
const csv = require('csv-parser');

class DataProcessor {
    constructor(filename) { ... }
    async loadData() { ... }
    calculateStatistics() { ... }
    async exportResults(outputFile) { ... }
}

// メイン実行ロジック
if (require.main === module) { ... }
```

以降のセクションでは、変換の主要な部分を個別に確認します。

---

### 3.4 ファイルI/O変換を理解する

Askモードに切り替えて、変換されたコードを探索します。

```
load_dataメソッドをPythonからJavaScriptにどのように変換しましたか？
Pythonのコンテキストマネージャーと JavaScriptのストリームベースのアプローチの主な違いは何ですか？
```

Pythonはファイルを開いてそのまま読み込みますが、JavaScriptではストリームとイベントを使います。

```python
# Python
def load_data(self) -> None:
    with open(self.filename, "r") as file:
        reader = csv.DictReader(file)
        self.data = [row for row in reader]
```

```javascript
// JavaScript
async loadData() {
    return new Promise((resolve, reject) => {
        const results = [];
        createReadStream(this.filename)
            .pipe(csv())
            .on('data', (row) => results.push(row))
            .on('end', () => {
                this.data = results;
                resolve();
            })
            .on('error', reject);
    });
}
```

### 3.5 統計計算変換を理解する

```
calculate_statisticsメソッドをどのように変換しましたか？
Pythonのリスト内包表記と組み込み関数をJavaScriptにどのように変換しましたか？
```

リスト内包表記は `Array.map()` と `Array.filter()` に対応し、`sum()`・`min()`・`max()` は `reduce()` と `Math.min()`・`Math.max()` に置き換わります。

```python
# Python
def calculate_statistics(self) -> Dict:
    numeric_fields = [
        k for k in self.data[0].keys() if self.data[0][k].replace(".", "").isdigit()
    ]
    values = [float(row[field]) for row in self.data]
    stats[field] = {
        "mean": sum(values) / len(values),
        "min": min(values),
        "max": max(values),
    }
```

```javascript
// JavaScript
calculateStatistics() {
    const numericFields = Object.keys(this.data[0])
        .filter(key => !isNaN(parseFloat(this.data[0][key])));
    const values = this.data.map(row => parseFloat(row[field]));
    stats[field] = {
        mean: values.reduce((a, b) => a + b, 0) / values.length,
        min: Math.min(...values),
        max: Math.max(...values)
    };
}
```

### 3.6 JSONエクスポート変換を理解する

```
export_resultsメソッドをどのように変換しましたか？
Pythonの同期ファイル書き込みとJavaScriptの非同期アプローチの違いは何ですか？
```

### 3.7 メイン実行ロジックを理解する

```
Pythonのif __name__ == '__main__'パターンをJavaScriptにどのように変換しましたか？
なぜ非同期IIFE（即時実行関数式）を使いましたか？
```

```javascript
// メイン実行
if (require.main === module) {
    (async () => {
        try {
            const processor = new DataProcessor('data.csv');
            await processor.loadData();
            await processor.exportResults('statistics.json');
            console.log('処理完了');
        } catch (error) {
            console.error('エラー:', error.message);
            process.exit(1);
        }
    })();
}

module.exports = DataProcessor;
```

---

## ステップ4: 検証と比較（5分）

### 4.1 サンプルデータを作る

テスト用のCSVファイルを作成します。

```csv
name,age,score,grade
Alice,25,95.5,A
Bob,30,87.3,B
Charlie,22,92.1,A
Diana,28,88.7,B
```

### 4.2 Pythonバージョンを実行する

```bash
cd source
python data_processor.py
```

正常に動けば `statistics.json` が生成されます。

```json
{
  "age": {
    "mean": 26.25,
    "min": 22,
    "max": 30,
    "count": 4
  },
  "score": {
    "mean": 90.9,
    "min": 87.3,
    "max": 95.5,
    "count": 4
  }
}
```

### 4.3 JavaScriptバージョンを実行する

BobはJavaScriptの変換を `` ディレクトリに作成します。

```bash
npm install
node data_processor.js
```

### 4.4 結果を比較する

```
PythonとJavaScriptの実装を比較してください。
以下の主な違いは何ですか:
1. コード構造
2. 構文
3. 非同期処理
4. エラー処理
5. パフォーマンス特性
```

### 4.5 機能の検証

両バージョンが同一の出力を生成することを確認します。統計計算・JSON構造・ファイル処理・エラー処理のすべてが一致すれば変換成功です。

---

## Lab 3 完了

2つの言語にまたがるコード変換を通じて、次のことが実践できました。

- AskモードでPythonコードの構造と意図を読み解く
- Planモードで言語間のマッピングを体系的に設計する
- Codeモードで機能を維持しながら変換を実装する
- 非同期パターンの違いを実際のコードで確認する

> Bobのインテリジェント最適化について
> このラボ全体を通じて、Bobのインテリジェントリソース最適化が舞台裏で機能していました。複雑な変換決定（Pythonのコンテキストマネージャーを JavaScriptの非同期パターンにマッピングするなど）にはフロンティアクラスのモデルを、単純な構文変換には軽量なモデルを自動的に選択します。

---

## 変換パターン早見表

変換後に振り返るための参考として、主要なパターンをまとめます。

### クラス

```python
# Python
class DataProcessor:
    def __init__(self, filename: str):
        self.filename = filename
```

```javascript
// JavaScript
class DataProcessor {
    constructor(filename) {
        this.filename = filename;
    }
}
```

### リスト内包表記

```python
# Python
values = [float(row[field]) for row in self.data]
```

```javascript
// JavaScript
const values = this.data.map(row => parseFloat(row[field]));
```

### ファイルI/O

```python
# Python
with open(filename, "r") as file:
    data = file.read()
```

```javascript
// JavaScript
const data = await fs.promises.readFile(filename, 'utf8');
```

### 型ヒント

```python
# Python
def calculate_statistics(self) -> Dict:
    pass
```

```javascript
// JavaScript
/**
 * @returns {Object} 統計オブジェクト
 */
calculateStatistics() {
    // ...
}
```

### 言語比較

| 機能 | Python | JavaScript |
|---|---|---|
| 型付け | オプションの型ヒント | JSDocまたはTypeScript |
| 非同期 | デフォルトで同期 | デフォルトで非同期（Node.js） |
| ファイルI/O | 組み込み、同期 | fsモジュール、非同期 |
| CSV | 組み込みcsvモジュール | csv-parserが必要 |
| 配列操作 | リスト内包表記 | map・filter |
| モジュール | import/from | require/module.exports |

---

## トラブルシューティング

### Pythonの問題

`ModuleNotFoundError: No module named 'csv'` が出る場合、`csv` はPython標準ライブラリなのでPythonバージョンを確認します。

```bash
python --version  # 3.x である必要があります
```

型ヒントでエラーになる場合、型ヒントはオプションです。Python 3.8+を使っていれば基本的に問題ありません。

### JavaScriptの問題

`Cannot find module 'csv-parser'` が出る場合は `npm install csv-parser` を実行します。

async/awaitが動作しない場合、Node.js 14+が必要です。

```bash
node --version
```

ファイルが見つからないエラーが出る場合、実行ディレクトリからの相対パスを確認します。`path.join()` を使うとクロスプラットフォームで安全です。

```javascript
const path = require('path');
const filePath = path.join(__dirname, 'data.csv');
```

---

## 追加リソース

- [Pythonドキュメント](https://docs.python.org/)
- [型ヒントガイド](https://docs.python.org/3/library/typing.html)
- [Node.jsドキュメント](https://nodejs.org/docs/)
- [MDN JavaScriptガイド](https://developer.mozilla.org/ja/docs/Web/JavaScript)
- [csv-parser](https://www.npmjs.com/package/csv-parser)
- [非同期パターン](https://javascript.info/async-await)
- [JSDocガイド](https://jsdoc.app/)

---

## Bob Bootcamp 全3ラボ完了

Lab 1でのアプリケーション構築、Lab 2でのセキュリティ分析と修正、そして今回のLab 3でのコード変換を通じて、Bobを使った実践的な開発ワークフローを一通り体験しました。実際のプロジェクトで活用してみてください。

このラボについて気になった点や改善案があれば、フィードバックをお寄せください。

---

*最終更新: 2026年10月*
