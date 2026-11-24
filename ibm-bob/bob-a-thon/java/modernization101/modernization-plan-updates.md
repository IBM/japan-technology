# 計画書への反映事項（modernization-plan-mac-Windows.md）

> 実装（Mac / Apple Silicon / Rancher Desktop）中に気づいた、計画書に反映すべき事項の記録。**この記録を先に作成し、その内容を計画書へ反映した。** 反映先と反映済みかどうかは各項目の「計画書への反映」欄を参照。
>
> - 実行環境: macOS arm64 / Docker 29.9.3-rd・Compose v5.7.0 / Node v24.22.1・npm 11.19.1
> - 実行期間: 2026-11-20 12:02 JST（環境判定）〜 2026-11-24 13:13 JST（最終検証）。途中でセッションが中断されたため、日をまたいでいる

## A. 実行方法（`execute_command`）に関する事項

| # | 気づいたこと | 根拠 | 計画書への反映 |
|---|-------------|------|---------------|
| U1 | **フォアグラウンドの `execute_command` は 30 秒（`timeout_seconds` 指定でも最大 270 秒）で打ち切られる。** 初回の `npm install` / `mvn test`（イメージ pull 込み）/ `npx playwright install chromium`（約 192 MiB）はいずれも 180〜270 秒で `TIMED OUT` になり、完了しなかった | 3 コマンドを並列に実行して 3 つとも TIMED OUT | 「Bob の実行制約」に追記: 長時間コマンドは `background: true` で起動し、ログファイルをポーリングする |
| U2 | **`nohup sh -c '…' > log 2>&1 &` をフォアグラウンドの `execute_command` から起動しても、コマンド終了とともにジョブが消える。** ログは更新されず、`ps` にも残らなかった | ジョブ起動後の `ps` / ログ確認 | 同上。**`nohup … &` ではなく `background: true` を使う** |
| U3 | **Mac では `docker compose up -d --build` を `background: true` で実行しても正常に動く**（3 コンテナ作成・`exit=0`）。計画書の「Windows 実機では `background: true` でコンテナが作られなかった」は Windows 固有の観測 | ルート・`migrated/` とも `background: true` で起動成功 | 「実行時の注意」に OS 別の注記を追加 |
| U4 | **1 回のコマンド内で長く待つ（`sleep` / ループで 250 秒前後）と `CANCELED` になり、実行中の処理も失われる。** 1 回の待機は 120 秒程度までにし、その都度ログを読む。キャンセル後は `docker compose ps -a` で状態を確認し、コンテナが無ければ再実行する（今回は `up` が中断され、コンテナが 1 つも残っていなかった） | 250 秒ポーリングが `CANCELED`、再開後に `docker compose ps -a` が空 | 「Bob の実行制約」に追記 |
| U5 | **並列起動のコマンドが共有ディレクトリ（`mkdir -p /tmp/...` など）を作る場合、作成を別コマンドに依存させない。** 並列で起動した 3 コマンドのうち 2 つが、他方の `mkdir` より先に走って `no such file or directory` で失敗した | 初回の並列ジョブ起動 | 「並列実行の指針」に追記（`background: true` ならログパスは自動で用意されるので不要） |
| U6 | **並列にできる / できない整理（今回の実測）。** 並列にした: ファイル作成（タスク 1〜4・6〜8 の約 35 ファイル）、`npm install && npm run build` + `mvn test` + `npx playwright install chromium`、ルートの `docker compose up -d --build` と JUnit。直列にした: `migrated/` の `down -v` → `up`、E2E → `migrate.sh`（同じ new-db を使うため。E2E は一意タイトルだが、`migrate.sh` は `TRUNCATE` する） | 実行ログ | 「並列実行の指針」に追記 |

## B. 計画書の内容そのものの不足・要補足

| # | 気づいたこと | 根拠 | 計画書への反映 |
|---|-------------|------|---------------|
| B1 | **backend の JAR 名が計画に無い。** タスク 1 Todo 5 の Dockerfile は `COPY --from=build /app/target/<jar>` が必要だが、`pom.xml` の `finalName` の指定がなく、`<artifactId>-<version>.jar` に依存して壊れやすい。`<build><finalName>app</finalName>` を指定し、Dockerfile は `target/app.jar` をコピーする構成にした | `migrated/backend/pom.xml` / `Dockerfile` | タスク 1 Todo 3・5 に明記 |
| B2 | **`TodoRepository` の全件取得メソッド名が計画に無い**（`@Query` を付けるとしか書かれていない）。`CrudRepository.findAll()` と衝突しないよう `findAllSorted()` とした。タスク 3 Todo 5 と JUnit が参照する | `TodoRepository.java` | タスク 3 Todo 3 に明記 |
| B3 | **`migrate.sh` の `ROOT_PROJECT` 導出は Mac で実測成功**（`classicjava201base-db-1` を検出。M9 / #「migrate.sh の旧 DB 自動検出」の「未実測」を解消）。`OLD_DB` の上書きは不要だった | `migrate.sh` 実行出力 `old-db: classicjava201base-db-1` | M9・「この Mac 固有の既存環境」を更新 |
| B4 | **ルートの旧アプリは「app だけ Up、db が Exited」の状態になり得る。** 今回 `classicjava201base-app-1` は Up 42 時間のまま `classicjava201base-db-1` が `Exited (0)` で、`http://localhost:8080/todo/list` は **HTTP 500**、`docker compose exec -T db …` は `service "db" is not running`、`migrate.sh` は `old-db / new-db container not found` で終了した。`docker compose up -d`（ルート）で db を `healthy` にすると 200 に戻る。**`ps` で `app` が Up でも、`db` の状態を必ず確認する** | `docker compose -f docker-compose.yml ps -a` | タスク 5 Todo 6 とタスク 6 Todo 4 に事前確認を追記 |
| B5 | **旧 DB（9.6）のテストデータ投入に、日本語を含む SQL を `write_file` で UTF-8 ファイルにし `docker compose exec -T db psql … < file` で流す方法が Mac で成功**（3 件、うち日本語 1 件）。移行後の `md5(title)` / `octet_length(title)` が新旧で一致（日本語は 24 バイト = 8 文字） | 検証クエリ出力 | タスク 6 Todo 2 に Mac の手順として追記。作った一時 SQL は削除する |
| B6 | **`migrate.sh` に件数比較とエラー終了を組み込んだ。** 計画は「検証クエリを組み込む」としか書かれていなかった。`psql -t -A -c "SELECT COUNT(*)…"` で数値だけ取り、不一致なら `exit 1` する。再実行（冪等）しても件数 3 のままで、移行後の POST が id=4 で 201、toggle で `updated_at > created_at`（トリガー有効）を確認 | `migrate.sh` / 検証出力 | タスク 6 Todo 2 に追記 |
| B7 | **旧画面との見た目一致の確認方法**: Playwright（Chromium）で旧画面と新画面の `getComputedStyle` と `getBoundingClientRect` を比較し、body のフォント・サイズ・余白、h1、table 幅 600、th の背景 `rgb(204,204,204)`・罫線 `1px solid rgb(153,153,153)`、td の padding `4px 8px`、テキスト入力 308x21、submit 83x27 が一致した。**【訂正: この説明は誤りだった。B10 を参照】** 表の高さは一致しない（旧 138 / 新 216）。当時の説明（誤り）は新画面の行数が増えたことと、7 列が 600px 幅に収まらず折り返すこと（追加列「優先度」「期限」のため）。計画の「追加列を除き同じ」の範囲内で、不具合ではない | 比較スクリプトの出力 | タスク 4 に確認方法と「表の高さは一致しない」を追記 |
| B8 | **JUnit は 9 件**（GET 空 / GET 1 件 / POST 正常 / POST の `id`・`done` 無視 / POST 空欄 400 / toggle 正常 / toggle 404 / DELETE 正常 / DELETE 404）で、約 5 秒（`@DirtiesContext` でも）。依存取得を含む初回の `mvn test` は、イメージ pull から合わせて数分かかった。ホストに `target/` が残る（`.dockerignore` で Docker ビルドから除外済み） | `Tests run: 9, Failures: 0, Errors: 0` | タスク 7 の期待件数を追記 |
| B9 | **生成物**: `migrated/frontend/node_modules`・`dist`、`migrated/e2e/node_modules`、`migrated/backend/target` が残る。`.gitignore` は無い（プロジェクトは git 管理外）。`test-results/` と `playwright-report/` は削除した | `ls migrated/*` | タスク 8 Relevant Context の既存記述で足りる（変更なし） |

## B 追加（2026-11-24 13:25 JST）: 新画面のタイトル列が旧画面より狭い（B10）

| # | 気づいたこと | 根拠 | 計画書への反映 |
|---|-------------|------|---------------|
| B10 | **表を `w-[600px]` のままにすると、列が 5 → 7 に増えた分、既存列が縮む。** タイトル列は旧 142px → 新 118px（左右 padding と罫線で文字領域は約 100px）。各列の必要幅（max-content）の合計は 609px で 600px を超えており、日本語タイトル（「移行テスト日本語」約 112px）と作成日時（`yyyy-MM-dd HH:mm:ss.SSSSSS`）が折り返した。ユーザーがスクリーンショットで指摘。**「旧画面と同じ見た目」の要件に対し、B7 の「表の高さは追加列のため一致しない（折り返しのため）」は不具合を見落とした説明だった** | 旧画面・新画面の列幅実測（旧 ID34/タイトル142/作成日時219/完了133/削除70、新 29/118/182/113/60 + 優先度 55・期限 42） | タスク 4 Todo 7 の表幅を `w-[720px]` に変更。Todo 10 の B7 注記を修正 |
| B10-結果 | 候補幅の実測（新画面）: 650px → タイトル 129、700px → 139、**720px → 143（旧 142）**、750px → 149。720px を採用。修正後の比較（Playwright、viewport 1200）: 旧 `table:600 ID:35 タイトル:137 作成日時:239 完了:123 削除:65`、新 `table:720 ID:36 タイトル:140 優先度:62 期限:48 作成日時:243 完了:125 削除:66`。**全行が 36px（折り返しなし）**。既存列は旧画面と ±数 px で一致。E2E は引き続き 1 passed。ブラウザ（フォント）が違うと旧・新の絶対値は変わるが、同じブラウザでの比較で一致した | `npm run build` → `docker compose up -d --build frontend`（backend / DB は再作成なし） | Todo 10 に反映 |

## C. 実機で確認できた値（計画書「Mac 実機検証結果」の E9〜E15 として反映済み）

| 計画書 # | 項目 | 実測 |
|---|------|------|
| E9 | 本計画をタスク 1 から通して実行（Mac / Apple Silicon） | 3 コンテナ起動（new-db は `healthy`）、スキーマ（7 列 + トリガー）、API（GET 200 / POST 201 / 空欄 400 / 不明 id 404）、Nginx 経由（`127.0.0.1` Origin で 201、`evil.example` で 403）を確認。**計画を通して実行して成功した初の実測** |
| E10 | backend 起動時間（`platform: linux/amd64`） | `Started TodoApplication in 14.99 seconds` |
| E11 | Playwright E2E（Mac ネイティブ） | `1 passed`（約 3.5 秒）。`@playwright/test` 1.65.1 |
| E12 | JUnit（Docker 経由） | 9 テスト成功、`BUILD SUCCESS` |
| E13 | フロントエンドのビルド | `vite build` 約 0.9 秒、`exit=0`。Vite 5.4.21 / Vue 3.5.45 / Tailwind 3.4.19 |
| E14 | `migrate.sh` の旧 DB 自動検出（B3） | `old-db: classicjava201base-db-1` / `new-db: migrated-new-db-1`。再実行しても件数 3（冪等）。`md5(title)` 一致、日本語 24 バイト |
| E15 | 古い `migrated_new-db-data` の削除 | 削除済み（残件数 0）。他のボリュームには触れていない |

## D. 反映状況

| 区分 | 反映先（計画書） | 状態 |
|------|-----------------|------|
| U1〜U6 | 冒頭の引用ブロック「並列実行の指針」「Bob の実行制約」、Windows「実行時の注意」への OS 注記 | 反映済み |
| B1 | タスク 1 Todo 3・5 | 反映済み |
| B2 | タスク 3 Todo 3 | 反映済み |
| B3 | M9、「この Mac 固有の既存環境」、E14 | 反映済み |
| B4 | タスク 5 Todo 6 の注記 | 反映済み |
| B5・B6 | タスク 6 Todo 2 | 反映済み |
| B7 | タスク 4 Todo 10（B10 で訂正） | 反映済み |
| B10 | タスク 4 Todo 7・10・Status | 反映済み |
| B8 | タスク 7 Expected Outcomes | 反映済み |
| B9 | （計画書の既存記述で足りるため変更なし） | — |
| C | 「Mac 実機検証結果」E9〜E15 | 反映済み |
| 各タスクの Status | 8 タスクすべて `[x] completed`（日時・検証結果つき） | 反映済み |
