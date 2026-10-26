# 事前課題(当日までに済ませておくこと)

当日の 1 時間を演習に使うために、インストールとダウンロードを含む次の 5 つを、**当日までに**済ませておいてください。所要は 20〜30 分(ダウンロード待ちを含む)です。会社の PC で進める場合は、ネットワークの制限でダウンロードが止まることがあるので、早めに試してください。

| # | やること | できたことの確認 |
|---|---|---|
| 1 | Bob のインストールとサインイン | Bob が起動し、右側にチャットが表示される |
| 2 | Node.js を合格の版にする | `node -v` が合格の条件を満たす |
| 3 | 作業フォルダを作って Bob で開く | Bob のエクスプローラーに空のフォルダ名が表示される |
| 4 | agent-browser(CLI)を入れる | `agent-browser --version` が版を表示する |
| 5 | agent-browser のスキルを Bob に登録する(グローバル) | Bob設定 > スキル に `agent-browser`(スコープ: グローバル)が表示される |

## 1. Bob のインストールとサインイン

[共通準備の 1〜2](common-setup.md) のとおりに進めます。

## 2. Node.js を合格の版にする

[シナリオ2(Node.js コマンドライン版)の事前準備 2〜3](scenario2-nodejs/guide2.md) のとおり、`node -v` を実行して合格の条件(2026-10-23 時点で 22.23.4 以上、24.22.1 以上、26.12.1 以上)を満たしていることを確認します。満たさない場合は、同じページの「Node.js のインストールと更新」で更新します。

## 3. 作業フォルダを作って Bob で開く

[共通準備の 3〜4](common-setup.md) のとおり、空のフォルダ(例: `bob-todo`)を作って Bob で開き、Agent モードと自動承認の設定まで済ませます。

> 当日もこのフォルダを使うので、消さないでください。

## 4. agent-browser を入れる

Bob の中でターミナルを開き(メニューバーの **[ターミナル] > [新しいターミナル]**)、次を 1 行ずつ実行します。

```text
npm install -g agent-browser
```

```text
agent-browser install
```

```text
agent-browser --version
```

- 1 つ目は CLI 本体を入れます(10 秒ほど)。`npm warn install-scripts ... not yet covered by allowScripts` という警告が出ることがありますが、**そのまま次へ進んで問題ありません**。
- 2 つ目はテスト用の Chrome(Chrome for Testing、約 200 MB)をダウンロードします(1〜2 分)。`✓ Chrome ... installed successfully` と出れば完了です。
- 3 つ目で `agent-browser 0.39.2` のような版が表示されれば成功です。

動作も確かめておきます。

```text
agent-browser open https://example.com; agent-browser get title; agent-browser close
```

`[agent-browser] launched browser` に続いて `Example Domain`、最後に `✓ Browser closed` と出れば OK です。画面には何も出ません(見えないブラウザを動かす道具です)。

## 5. agent-browser のスキルを Bob に登録する

同じターミナルで、次を実行します。`-g` を付けると、**どのフォルダで実行しても**自分のユーザー全体(グローバル)に登録されるので、当日どの作業フォルダを開いても使えます。

```text
npx skills add vercel-labs/agent-browser --skill agent-browser -a bob -g
```

質問には次のように答えます。

| 表示 | 答え |
|---|---|
| `Need to install the following packages: skills@... Ok to proceed? (y)`(初回だけ) | `y` を入力して Enter |
| `Security Risk Assessments`(Gen / Socket / Snyk の評価)のあと `Proceed with installation? Yes / No` | `Yes` のまま Enter |
| `Install the find-skills skill?`(初回だけ) | 右矢印キーで `No` にして Enter |

`Installed 1 skill: agent-browser (copied)` と出れば完了です。ファイルは、Windows なら `C:\Users\<ユーザー名>\.bob\skills\agent-browser\SKILL.md`、macOS なら `~/.bob/skills/agent-browser/SKILL.md` にできます。作業フォルダには何も作られません。

登録を Bob に認識させるため、**Bob を一度終了して起動し直します**(または `Ctrl + Shift + P` → 「開発者: ウィンドウの再読み込み」)。起動し直す前は一覧に出ません。そのあと、画面右下の **Bob設定**(歯車)> 左の **スキル** に、`agent-browser`(スコープ: グローバル)が表示されることを確認します。

## うまくいかないとき

| 症状 | 対処 |
|---|---|
| `npm` が認識されない | Node.js を入れ直し、ターミナルと Bob を再起動する |
| `npm install -g` で権限のエラー(macOS) | 当日、講師に声をかける(Homebrew なら `brew install agent-browser` でも入れられます) |
| `agent-browser install` のダウンロードが進まない | ネットワークの制限の可能性。別のネットワークで試すか、当日、講師に声をかける |
| Bob設定 > スキル に出ない | Bob を終了して起動し直したか確認する。それでも出なければ、`C:\Users\<ユーザー名>\.bob\skills\agent-browser\SKILL.md`(macOS は `~/.bob/skills/agent-browser/SKILL.md`)があるか確認し、なければ 5 をやり直す |

当日は、1〜5 ができている前提で始めます。できなかった項目があっても参加できますが、その部分はペアの人の画面で進めることになります。
