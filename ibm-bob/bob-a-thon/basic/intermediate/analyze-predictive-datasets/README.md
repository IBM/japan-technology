# プロジェクト 4：データサイエンス・ユースケース

**想定所要時間**: 1～2時間
**想定コスト**: 2ドル未満

## 概要

本プロジェクトでは、**data-scientist スキル**を使用して、予測分析のための機械学習モデルを開発します。

探索的データ分析（EDA）からモデル構築・評価まで、**完全なデータサイエンス・ワークフロー**を実演します。Kaggle コンペティションおよび実データセット向けの専用スクリプトやベストプラクティスが含まれています。

本プロジェクトは単発分析ではなく、**再利用可能なワークフロー**として設計されており、分類・回帰のさまざまな問題に適用可能です。

目的は、data-scientist スキルのツールや手法を用いて、**Bob がデータサイエンスのパイプライン全体をオーケストレーションできることを示す**ことです。

## 必要な拡張機能・ツール・ランタイム

- **Python ランタイム**: 3.12 以上
- **Python パッケージ**（Bob がインストールを支援）
  - pandas, numpy, scikit-learn
  - imbalanced-learn（クラス不均衡対応）
  - xgboost, lightgbm, catboost（高度なモデル）
  - openpyxl（Excel サポート）
  - pyarrow（Parquet サポート）

## 手順

### 1. プロジェクトファイルのダウンロード

以下のリポジトリからプロジェクトファイルをダウンロードし、新しい Bob ウィンドウで開きます。

👉 https://github.ibm.com/elowery/WW-Bobathon/tree/main/Project4_Data_science

### 2. data-scientist スキルのディレクトリ構成

```
data-scientist/
├── SKILL.md                  # メインスキルドキュメント
├── scripts/                  # 実行可能な Python スクリプト
│   ├── eda_analyzer.py       # 探索的データ分析
│   ├── data_cleaner.py       # データクレンジング・前処理
│   ├── balance_dataset.py   # クラス不均衡対応
│   ├── feature_engineer.py  # 特徴量エンジニアリング
│   └── model_builder.py     # モデル学習・評価
└── references/
    ├── data_science_methodology.md   # 完全な方法論ガイド
    ├── kaggle_competition_guide.md   # Kaggle 向けベストプラクティス
    └── documentation_best_practices.md # ドキュメント作成ガイドライン
```

### 3. Ask モードでスキルを学習

Bob を **Ask モード**に設定し、以下のプロンプトを入力します。

```
Learn data scientist skills in the skills folder.
```

→ data-scientist スキルの概要と、手動での利用方法が説明されます。

### 4. Kaggle コンペティションへの適用

次に、Kaggle コンペティションに適用するため、以下のプロンプトを入力します。

**日本語版プロンプト**:
```
Python スクリプトを実行する際は、常に仮想環境（virtual environment）を使用してください。
データサイエンティストのスキルを用いて、銀行の定期預金に顧客が申し込むかどうかを予測する機械学習モデルを構築してください（目的変数：y、使用データ：data/playground-series-s5e8/train.csv）。
目標は、ROC 曲線下面積（AUC）に基づく Kaggle リーダーボードで高い順位を獲得することです。
test.csv に対して予測を生成し、出力形式は data/playground-series-s5e8/sample_submission.csv に合わせてください。
スクリプトを実行する際は、必ず Python の仮想環境を使用し、.md 形式の ML レポートを忘れずに作成してください。
```

**原文（英語版）**:
```
Use the data-scientist skill to build a machine learning model that predicts whether a client will subscribe to a bank term deposit (target column: _y_) using _data/playground-series-s5e8/train.csv_.
The objective is to achieve a high ranking on the Kaggle leaderboard based on the Area Under the ROC Curve (AUC).
Generate predictions on _test.csv_ and format the output to match _data/playground-series-s5e8/sample_submission.csv_.
Always use a Python virtual environment to run scripts, and don't forget to generate an ML report in _.md_ format.
```

#### 注意

Bob は仮想環境（virtual environment）の使用を忘れる傾向があります。その場合は、実行前に以下を追加してください。

```
Always use virtual env for python scripts
```

### 5. To-Do リストの確認

Bob が **To-Do リスト**を生成します。内容を確認し、承認してください。

### 6. Code モードへの切り替え

指示が出たら、**Code モードへの切り替え**を承認します。

### 7. EDA および ML パイプライン構築

Code モードでは、Bob と協力して EDA および ML パイプライン構築を進めます。

#### 補足

最初に表示される `=====` 出力は、パイプライン開始を示します。その後、

- `[1/9]` データ読み込み
- `[2/9]` 特徴量エンジニアリング

などの進捗ログが表示され、各ステップが実行されていることが確認できます。

## 完了後

以下がすべて生成されたことを Bob が検証します。

- サブミッション用 CSV
- 詳細な ML レポート（.md）

ML レポートを確認することで、作業内容や結果を深く理解できます。

## 任意（オプション）

- **Ask モードに戻り、以下を質問**：
  - `Did you reference anything from the data-scientist skill?`
  - → スキルの使用内容が要約されます。
- **モデル精度をさらに向上させる方法を Bob と一緒に検討する**。

