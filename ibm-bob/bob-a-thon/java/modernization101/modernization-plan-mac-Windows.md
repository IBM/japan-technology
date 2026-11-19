# ClassicJava201 モダナイゼーション計画（Mac / Windows 対応版）

## 概要

**目標:** Java 1.4 + Tomcat 5.5 + Servlet/JSP スタックを、Vue.js + Spring Boot + PostgreSQL 16 のモダンスタックへ移行する。

**スコープ:**
- 移行後アプリは `migrated/` フォルダーに格納（既存コードは変更・削除しない）
- Todo CRUD（一覧・追加・完了トグル・削除）の機能を完全再現
- DBスキーマを拡張（priority / due_date / updated_at 追加）
- Docker Compose でフロントエンド・バックエンド・DB をコンテナとして展開

**非対象:** 認証連携、周辺バッチ、外部連携、双方向同期

> **進捗の注意:** 各タスクの Status は `[ ] pending` から始め、完了時に Bob が `[x] completed`（日時・検証結果つき）に更新する。**着手前に `migrated/` の有無と各 Status を必ず確認し、既に `[x] completed` のタスクを前提に作業を飛ばさない。** 再実行する場合は `migrated/` を削除（`docker compose -f migrated/docker-compose.yml down -v` 後）して Status を `[ ] pending` に戻す。
>
> **自動実行時の記録（移植自動化向け）:** 実行エージェントはサブタスクごとの完了を **プロジェクトルートの `progress.md`（無ければ新規作成）** にシステム時刻（JST。Windows は `Get-Date -Format "yyyy-MM-dd HH:mm:ss"`、Mac / WSL2 は `TZ=Asia/Tokyo date "+%Y-%m-%d %H:%M:%S"` で取得。PowerShell には日本語を含めない）とともに追記し、学び・計画書とのズレを **プロジェクトルートの `LessonLearned.md`（既存ファイルの末尾に追記。既存内容は消さない）** に残す。重大な問題（ポート衝突・Docker 未起動・Linux コンテナ未切替など、計画で定めた停止条件）以外はユーザー確認を取らずに進める。
>
> **並列実行の指針:** タスク 1 完了後は、タスク 2・3・4（さらに契約が固定済みのタスク 6・7・8 のファイル作成）を同時に作成してよい。ビルド系（`npm run build` / `mvn test` / `npm install` + `npx playwright install chromium`）は互いに独立なので同時に実行できる。**ただし `docker compose up` と `docker compose down -v` を同じプロジェクトに並行して実行しない**（ルートと `migrated/` のように別プロジェクト同士は並行してよい）。
>
> **Bob の実行制約:** `execute_command` はフォアグラウンドで居座るコマンド（`docker compose up` の `-d` なし等）や TTY を要求するコマンド（`docker exec -it`）では戻らない／失敗する。常に `-d` / `-T` / `-i` を使う。ホストの JDK / Maven / Ant の有無に依存しないよう、Maven は Docker 経由で実行する（実機では scoop の JDK 21 / Maven があったが、Java 17 とは異なるため使わない。下記「Windows 実機検証結果」#15）。
>
> **既存コードは変更しない:** ルートの `src/` `web/` `sql/` `docker-compose.yml` 等には触れない。
>
> **`AGENTS.md` の位置づけ:** ルートの [`AGENTS.md`](AGENTS.md) は既存アプリ（Java 1.4 / Tomcat 5.5 / Servlet・JSP）向けのガイドで、旧DB（`db`、`todo-net`）の接続情報やURLマッピング（`/list` `/update` `/delete`、コンテキストパス `/todo`）の確認に使う。そこに書かれた Java 1.4 の制約やコーディング規約は `migrated/`（Java 17 / Spring Boot / Vue.js）には適用しない。移行後アプリの規約はこの計画書の各タスクに従う。

**ポート割り当て:**
| サービス | ポート |
|---------|--------|
| フロントエンド (Nginx) | 53080 |
| バックエンド (Spring Boot) | 53081 |
| PostgreSQL 16 (new-db) | 53032 |
| PostgreSQL 9.6 (既存 db) | ホスト公開なし（コンテナ内部のみ、変更なし） |

---

## 実行環境の識別

Bob（実装エージェント）は、**計画の最初のステップとして**以下のコマンドを `execute_command` ツールで実行し、OS を確定してから後続のすべてのコマンドを選択すること。

### 判定手順（必須・タスク1着手前に実行）

**Step 1: `execute_command` で `uname -s` を実行する**

```bash
uname -s
```

| `uname -s` の出力 | 次のアクション |
|-------------------|--------------|
| `Darwin` | **Mac 確定**。各タスクの `# Mac / WSL2` 欄のコマンドを使う |
| `Linux` | Step 2 へ進む（WSL2 か Linux ネイティブかを区別） |
| `MINGW64_NT-*` / `MSYS_NT-*` / `CYGWIN_NT-*`（Git Bash 等） | **Windows 確定**（シェルが Git Bash の場合）。Step 3 へ進む。以降の PowerShell 欄コマンドは Git Bash では動かないため、`execute_command` のシェルが何かをユーザーに確認するか、`powershell -NoProfile -Command "..."` 経由で実行する |
| コマンドが見つからない / エラー | **Windows 確定**。Step 3 へ進む |

**Step 2（`Linux` と出力された場合）: WSL2 か Linux ネイティブかを区別する**

```bash
grep -qi microsoft /proc/version && echo WSL2 || echo Linux-native
```

| 出力 | 環境 | 使用するコマンド欄 |
|------|------|-----------------|
| `WSL2` | **WSL2 確定** | 各タスクの `# Mac / WSL2` 欄。`migrate.sh` もここで実行できる |
| `Linux-native` | **Linux ネイティブ** | 各タスクの `# Mac / WSL2` 欄をそのまま使用 |

**Step 3（`uname -s` がエラーの場合）: `execute_command` で `$env:OS` を確認する**

```powershell
$env:OS
```

出力が `Windows_NT` であれば **Windows PowerShell 確定**。各タスクの `# Windows PowerShell` 欄のコマンドを使う。

出力が文字どおり `$env:OS` だった場合は **cmd.exe**。`echo %OS%` が `Windows_NT` なら Windows 確定だが、本計画の PowerShell 構文（`;` 連結・`Set-Location`）は cmd では動かないため、コマンドは `powershell -NoProfile -Command "..."` で包むか、ユーザーに PowerShell を使うよう依頼する。

> **各 `execute_command` は独立したシェルで実行される前提で書く。** `Set-Location` / `cd` は次のコマンドに持ち越されないため、ディレクトリ移動は同一コマンド内で完結させる（本計画のコマンドは全てそうなっている）。Windows PowerShell 5.1 では `&&` が使えないので `;` で連結する（`;` は前のコマンドが失敗しても続行するため、失敗時は出力を必ず確認する）。**PowerShell 5.1 では `docker` / `npm` / `npx` が進捗を stderr に出すため、赤字の `NativeCommandError` が表示されても実際は成功していることがある。** 成否は表示色ではなく、同一コマンド末尾に `; echo "exit=$LASTEXITCODE"` を付けて終了コード（0 が成功）で判断する。

**Step 4: 前提ツールの確認（Step 1〜3 で OS を確定した後、そのシェルで実行）**

```bash
docker compose version
node --version
npm --version
```

- `docker compose version` が失敗する場合は Docker（Docker Desktop / Rancher Desktop 等）の起動・インストールをユーザーに依頼して中断する（Compose v1 の `docker-compose` しかない場合のみ、本計画の `docker compose` を `docker-compose` に読み替える）
- `node` / `npm` が無い場合: タスク4・8 に必須のため、ユーザーに Node.js 20.x 以上（LTS）のインストールを依頼する
- **`python3` は不要。** タスク6 の `migrate.sh` は SQL 側で補完するため、python3 / awk に依存しない（下記「Windows 実機検証結果」#9）

**Windows 追加チェック（Windows と確定した場合のみ）:**

| 確認コマンド | 期待値 / 失敗時の対応 |
|-------------|---------------------|
| `docker info --format "{{.OSType}}"` | `linux`。`windows` の場合は Windows コンテナモードのため、ユーザーに Linux コンテナへの切替（Docker Desktop なら「Switch to Linux containers」）を依頼して中断する（postgres / nginx / maven の Linux イメージが動かない） |
| `Test-Path "C:\Program Files\Git\bin\bash.exe"` | `True`。**タスク6 の `migrate.sh` は Git Bash で実行する**（WSL2 は不要）。`False` の場合は Git for Windows の導入、または WSL2（Ubuntu）の `bash` の使用をユーザーに依頼する |
| `npm --version` | **「このシステムではスクリプトの実行が無効」エラーが出る場合**（PowerShell 5.1 の既定の実行ポリシー `Restricted` で `npm.ps1` / `npx.ps1` がブロックされる）、本計画の `npm` / `npx` を **`npm.cmd` / `npx.cmd`** に読み替える（ポリシーの変更はユーザーの承諾なしに行わない。実機は `CurrentUser=RemoteSigned` で問題なし） |
| プロジェクトのパス | **ASCII のみか確認する。** パスやユーザー名に日本語が含まれる場合、CP932 制約によりコマンドが文字化けする恐れがあるため、ユーザーに ASCII のみのパス（例: `C:\work\ClassicJava201-handson`）への配置を依頼する |

> **ポート衝突（Windows 固有）:** `docker compose up` が `ports are not available ... forbidden by its access permissions` で失敗する場合、Windows の予約済みポート範囲（Hyper-V / WinNAT）に 53080 / 53081 / 53032 / 8080 が含まれている。`netsh interface ipv4 show excludedportrange protocol=tcp` で確認し、該当する場合はユーザーに報告して指示を仰ぐ（ポートは計画で固定のため Bob が勝手に変更しない）。

**Mac 追加チェック（Mac と確定した場合のみ。Step 4 の後に実行）:**

| 確認コマンド | 期待値 / 失敗時の対応 |
|-------------|---------------------|
| `docker info --format '{{.OSType}} {{.Architecture}}'` | `linux aarch64`（Apple Silicon）または `linux x86_64`（Intel Mac）。**`docker compose version` は Docker デーモンが停止していても成功する**ため、デーモンの起動確認はこのコマンドで行う。`Cannot connect to the Docker daemon` が出たら Docker Desktop（または Rancher Desktop / Colima 等）の起動をユーザーに依頼して中断する |
| `uname -m` | `arm64` なら Apple Silicon。**`platform: linux/amd64` のエミュレーション動作は実機確認済みのため、Bob は再確認しない**（下記「Mac 実機検証結果」#E1〜#E5）。`x86_64` なら Windows と同様にネイティブ実行 |
| `which node npm` | 出力されること。見つからないが nvm / Homebrew 等で導入済みの場合は、`execute_command` の非ログインシェルに PATH が通っていないだけのことがある（`/opt/homebrew/bin/node` / `~/.nvm/versions/node/*/bin/node` を確認し、見つかればユーザーに PATH 設定を依頼する。勝手にシェル設定ファイルを書き換えない） |
| `lsof -nP -iTCP:53080 -iTCP:53081 -iTCP:53032 -iTCP:8080 -sTCP:LISTEN` | 4 ポートとも空であること（この Mac は、ユーザーが別ディレクトリ由来の既存アプリ `classicjava201-app-1` を停止した後、全ポートが空きであることを確認済み。下記 #E7）。出力がある場合は、`ssh ... lima ... ssh.sock [mux]`（Rancher Desktop のポート転送）なら **いずれかのコンテナがそのポートを公開している**ので `docker ps` で公開元を特定し、衝突しているプロセスをユーザーに報告して指示を仰ぐ（ポートは計画で固定のため Bob が勝手に変更しない。他プロジェクトのコンテナを勝手に停止しない） |
| プロジェクトのパス | `/Users/` 配下であること（この Mac の `Downloads/ClassicJava201base` はバインドマウント可を実機確認済み。#E8）。`/tmp` 等ホームの外ではバインドマウントが空ディレクトリになり new-db が起動しない |

### 判定結果に応じた行動ルール

| 判定結果 | `execute_command` のシェル | 各タスクで使うコマンド | `migrate.sh` |
|---------|--------------------------|---------------------|-------------|
| **Mac** | zsh（Mac の既定。本計画の Mac コマンドは bash / zsh 共通で動く） | `# Mac / WSL2` 欄 | `bash migrate.sh` をそのまま実行 |
| **WSL2** | bash (WSL2) | `# Mac / WSL2` 欄 | `bash migrate.sh` をそのまま実行 |
| **Windows** | PowerShell | `# Windows PowerShell` 欄 | `& "C:\Program Files\Git\bin\bash.exe" migrate.sh`（**Git Bash 経由。実機で動作確認済み**）。Git Bash が無い場合のみユーザーに WSL2 / Git Bash での手動実行を依頼する |

> **Windows での `migrate.sh` の扱い（重要）:**
> PowerShell から直接 `migrate.sh` は実行できないが、**Git for Windows 同梱の `bash.exe` 経由なら `execute_command` から実行できる**（実機で `docker exec | docker exec -i` パイプ・日本語データ・シーケンス補正まで成功）。**PowerShell 自身で `docker exec | docker exec -i` のパイプを組まないこと**（日本語を含む行で壊れる。検証結果 #10）。WSL2 は、実機では Rancher Desktop 専用ディストリのみで `bash` が無かったため前提にしない。

> **Windows CP932 制約:** PowerShell スクリプトやコマンドに日本語文字列（コメント含む）を含めると、既定の Code Page 932（Shift_JIS）環境で文字化け・実行エラーが発生する。`execute_command` で Windows に渡すコマンド・スクリプトには**日本語を含めない**こと。

> **ファイル作成は必ず `write_file` / `apply_diff` 等のファイルツールで行う（Windows 重要）:** `Set-Content` / `Out-File` / `echo > file` / `>` リダイレクトは Windows PowerShell 5.1 では UTF-16 LE や BOM 付き / CP932 で書き出すことがあり、Vue・JS・YAML・SQL・Dockerfile・`nginx.conf` が壊れる。Vue/JS/テストコード内の日本語（ボタン文言「追加」等）はファイルツール経由なら UTF-8 で保存されるため問題ない。ファイルは UTF-8（BOM なし）・LF で作成すること。
>
> **`node_modules` の OS 混在禁止（Windows 重要）:** `migrated/frontend` と `migrated/e2e` の `npm install` / `npm run build` / `npx playwright` は、**同一プロジェクトにつき 1 つの環境（Windows ネイティブ、または WSL2）だけで実行する**。Windows と WSL2 の両方で実行すると esbuild / rollup / playwright のネイティブバイナリが OS 不一致で起動しなくなる。混在してしまった場合は `node_modules` を削除して実行環境側で `npm install` をやり直す。Bob が Windows と判定された場合は PowerShell（Windows ネイティブ）で統一する（`migrate.sh` を実行する Git Bash は `npm` を呼ばないため `node_modules` に影響しない）。
>
> **長時間コマンド:** 初回の `docker compose up -d --build`（Maven 依存取得）や `npx playwright install chromium` は数分かかる。`execute_command` がタイムアウトしても処理が継続している場合があるため、その場合は `docker compose ps` / `docker compose logs --tail=100 <service>` で状態を確認し、再実行する前に完了を待つ。

---

## Windows 実機検証結果（計画の前提との差分）

> 1 台の実機（下記）で `execute_command` から実際にコマンドを実行して確認した結果。**Docker Desktop 環境では差異があり得る**ため、タスク1着手時に「実行環境の識別」Step 4 と本表の ❌/⚠️ 項目だけ再確認すること。

**検証環境:** Windows 10.0.26300 / Windows PowerShell 5.1（`$PSVersionTable.PSVersion` = 5.1.26100）/ コードページ 932 / 作業パス `C:\share\ClassicJava201-handson`（ASCII のみ）/ Docker は **Rancher Desktop（dockerd）** `docker 29.6.2-rd`・`Compose v5.3.1`・`OSType=linux`・ホスト `x86_64` / Node `v24.22.1`・npm `11.19.1` / Git `2.45.2.windows.1`（Git Bash 同梱）

| # | 計画の前提 | 実機の結果 | 判定 | 計画への影響 |
|---|-----------|-----------|:---:|-------------|
| 1 | `uname -s` で OS 判定、失敗なら Windows | PowerShell で `CommandNotFoundException`、`$env:OS` = `Windows_NT` | ✅ | そのまま有効 |
| 2 | Docker Desktop（Windows コンテナモード注意） | Docker Desktop ではなく **Rancher Desktop**。`docker info --format "{{.OSType}}"` = `linux`。`docker compose version` OK | ⚠️ | 「Switch to Linux containers」の文言は Docker Desktop 限定。判定は `OSType=linux` のみで行う |
| 3 | `wsl docker compose version` が通る（WSL Integration） | WSL ディストリは `rancher-desktop` / `rancher-desktop-data` のみ。**Ubuntu なし、`bash` なし、`python3` なし**（busybox `sh` のみ）。distro 内の `docker` は `docker compose` サブコマンド非対応 | ❌ | **WSL2 + `migrate.sh` 前提は成立しない。** タスク6 は Git Bash 実行に変更（後述 #8） |
| 4 | `python3` が WSL2 側にある | Windows 側にも `python` / `python3` / `py` なし | ❌ | `migrate.sh` から **python3 依存を除去**（後述 #9） |
| 5 | Node.js 20.x LTS | `v24.22.1`。Vite 5.4.21 + `@vitejs/plugin-vue` 5 + Tailwind 3.4 + PostCSS で `npm install` / `npm run build` が成功（`dist/` に `.line-through` を含む CSS が生成） | ✅ | Node は 20.x **以上**でよい。バージョン固定は「技術スタック」節のライブラリ側のみ |
| 6 | `npm` / `npx` が実行ポリシーでブロックされる場合がある | `CurrentUser=RemoteSigned`。`npm` / `npx`（`.ps1`）とも実行可 | ✅ | `.cmd` 読み替えは「エラーが出た場合のみ」のままでよい |
| 7 | `docker` / `npm` の stderr で赤字 `NativeCommandError` が出ても成功のことがある | `2>&1` を付けると実際に発生（`docker compose up`、`npm install` の `npm warn`）。終了コードは 0 | ✅ | 計画の「`exit=$LASTEXITCODE` で判断」は正しい。`npm 11` は `esbuild` の postinstall に関する `npm warn install-scripts` を出すが、ビルドは成功する |
| 8 | `migrate.sh` は WSL2 でのみ実行可、`execute_command` では不可 | **Git Bash（`C:\Program Files\Git\bin\bash.exe`）で実行可能。** `docker` が PATH 上で見え、`docker exec \| docker exec -i` パイプ、日本語データ、`setval` によるシーケンス補正まで成功 | ✅（代替） | Windows の `migrate.sh` 実行は `& "C:\Program Files\Git\bin\bash.exe" migrate.sh` を第一候補にする。ユーザーへの手動依頼は不要になる |
| 9 | CSV 補完を `python3`（csv モジュール）で行う | 補完値（`priority=0` / `due_date=NULL` / `updated_at=created_at`）は**定数と既存列のみ**なので、`COPY (SELECT id, title, done, created_at, 0, NULL, created_at FROM todos) TO STDOUT CSV` で **SQL 側で補完できる**。この方式を Git Bash で実行し 2 行（ASCII 1 + 日本語 1）が一致、`NULL` は空欄として `due_date` に NULL 投入された | ✅（代替） | `awk` / `python3` を使わず、ヘッダなしの 7 列 CSV を直接 new-db へ流す |
| 10 | PowerShell で `docker exec -i … < file` は動かない場合がある | 同様の問題を別形態で確認: **PowerShell の `docker exec … \| docker exec -i …` パイプは日本語を含む行で壊れる**（`invalid input syntax for type boolean`）。ASCII のみなら成功 | ⚠️ | PowerShell でパイプ移行しない。Git Bash パイプ（✅）か、`COPY … TO '/tmp/x.csv'` → `docker cp`（コンテナ→ホスト→コンテナ）→ `COPY … FROM '/tmp/x.csv'` を使う（日本語を含めて成功） |
| 11 | ルートのディレクトリ名は `ClassicJava201base` | 実ディレクトリは **`ClassicJava201-handson`**。Compose プロジェクト名は `classicjava201-handson`、old-db は `classicjava201-handson-db-1`。計画記載の `ROOT_PROJECT` 導出（ディレクトリ名を小文字化）はこの名前と**一致する**が、`classicjava201base` で絞ると空になる | ⚠️ | 計画中の `ClassicJava201base` 固定記述を削除し、導出ロジックに任せる（本文を修正済み） |
| 12 | `docker ps --format '{{.Label "…"}}'` 等を PowerShell から実行できる | PowerShell 5.1 は引数内の二重引用符を落とすため `template parsing error: function "com" not defined` で失敗。`--filter "label=com.docker.compose.service=db"` と `--format "{{.Names}}"` は成功 | ⚠️ | PowerShell では `--format` テンプレートに二重引用符を入れない。コンテナ特定は `docker compose -f docker-compose.yml ps -q db` が使える |
| 13 | Git Bash で bash スクリプトが動く | Git Bash は `docker exec <c> ls /tmp` の **`/tmp` を `C:/Users/.../Temp` に変換**してしまう（MSYS パス変換）。`psql -c "…"` のみの呼び出しは影響なし | ⚠️ | `migrate.sh` 内でコンテナ内の絶対パスを引数に渡さない。必要な場合は `MSYS_NO_PATHCONV=1` を付ける |
| 14 | `.gitattributes` / CRLF 対策が必要 | 既存ファイルは LF・BOM なし（`docker-compose.yml` / `sql/init.sql` / `Dockerfile` の CR 数 0）。グローバル `core.autocrlf=true` だが `.git` が無い。**`write_file` で作成したシェルスクリプトも LF・BOM なし** | ✅ | `.gitattributes` は git 管理下に置く場合のみ意味がある。ファイルツールで作る限り CRLF は入らない（確認コマンドは残す） |
| 15 | ホストに JDK / Maven は無い | ホストには scoop 経由で `java`（Semeru 21）と `mvn` がある（`ant` / `bash` / `sh` は PATH に無い）。ルートの `AGENTS.md`（既存アプリ向けのガイド）は、ビルド・実行を Docker 経由に限定し、ローカルの `ant war` は不可としている | ⚠️ | Maven は計画どおり Docker 経由で実行する（ホスト JDK 21 と Java 17 の差を避けるため）。`AGENTS.md` の規約（Java 1.4 制約・既存コード不変など）は**既存アプリ（`src/` `web/`）にのみ適用**され、`migrated/` の Java 17 / Spring Boot コードには適用しない |
| 16 | `docker run -v "${PWD}\migrated\backend:/app" … mvn test` | Windows パスのバインドマウントは成功（読み書き可、`target/` 相当の書き込みも反映）。`maven:3.9-eclipse-temurin-17` の pull、名前付きボリューム `-v <name>:/root/.m2` も成功。コンテナから Maven Central へ到達可 | ✅ | そのまま有効 |
| 17 | `mvn` に `-D` オプションを渡す | **PowerShell 5.1 は `-Dartifact=org.springframework…` のようにドットを含む未引用の引数を `org .springframework…` に分割**する。`"-Dartifact=…"` と二重引用符で囲むと成功 | ⚠️ | PowerShell で `-Dxxx=a.b` 形式を渡すときは必ず全体を二重引用符で囲む（本計画の `mvn test` / `mvn -B -DskipTests package` はドットを含まない、またはコンテナ内実行なので影響なし） |
| 18 | `platform: linux/amd64` は Windows でネイティブ | ホスト・コンテナとも `x86_64`。`docker run --platform linux/amd64 alpine uname -m` = `x86_64` | ✅ | そのまま有効。なお frontend の `FROM --platform=linux/amd64 nginx:alpine` は BuildKit が `FromPlatformFlagConstDisallowed` 警告を出す（ビルドは成功）。Compose の `platform:` を指定済みなので警告を避けたければ `FROM nginx:alpine` でもよい |
| 19 | Nginx は `backend` を起動時に名前解決する | backend が無い構成で frontend を起動すると `host not found in upstream "backend"` で **Exited (1)**。DB は `healthy`、`53032` はホストから到達可 | ✅ | 計画の「frontend は backend に `depends_on` を持つ」設計は必須。タスク1 の動作確認で backend が起動できないと frontend も落ちる（原因は backend 側のログを見る） |
| 20 | `postgres:16-alpine` + `docker-entrypoint-initdb.d` | 起動して `healthy`、`psql` は `16.16`。初期化 SQL はボリューム新規作成時のみ実行される | ✅ | タスク2 Todo 6 の `down -v` 手順は妥当 |
| 21 | Playwright は Windows ネイティブで動く | `@playwright/test 1.65.1`、`npx playwright install chromium`（Chromium 約 207MB + headless shell 約 124MB）が `execute_command` の制限時間内に成功 | ✅ | ブラウザ取得に加え、テスト実行も #28 で確認済み |
| 22 | 既存アプリの同時起動 | ルートで `docker compose up -d --build` を実行し、`http://localhost:8080/todo/list` が `200`（`127.0.0.1` / `[::1]` でも `200`）。old-db は `healthy` で `5432/tcp` のみ（ホスト非公開）。`docker compose -f docker-compose.yml exec -T db psql …` による INSERT / COUNT も成功 | ✅ | 既存アプリ側は変更不要 |
| 23 | 予約ポートとの衝突 | `netsh interface ipv4 show excludedportrange protocol=tcp` の範囲は 5357 / 28385 / 28390 / 50000–50059 / 51631–52330。**53080 / 53081 / 53032 / 8080 は範囲外**。リッスン中のプロセスもなし | ✅ | この環境ではポート変更不要 |
| 24 | 旧DB(9.6) → 新DB(16) の 2 コンテナ間移行（`migrate.sh`） | 一時ディレクトリに計画どおりの new-db（拡張スキーマ + `update_updated_at` トリガー、`53032`）を立て、旧DBに 4 件（日本語 1 件を含む）投入して Git Bash で実行。`TRUNCATE` → `COPY 4` → `setval` が成功し、旧 4 件 / 新 4 件で一致。`title` の MD5 が新旧で一致（日本語の `移行テスト日本語` は 24 バイト = 8 文字）。`priority=0` / `due_date IS NULL` / `updated_at = created_at` を確認。**再実行しても件数 4・最大 id 14 で冪等**。移行後の INSERT が id 15 で採番され、`UPDATE` で `updated_at > created_at`（トリガー有効） | ✅ | 計画の `migrate.sh` 方式はそのまま有効。一時ディレクトリは階層が 1 つ深く `ROOT_PROJECT=probe-tmp` となり旧DB自動検出は `not found` で正しく `exit 1`、`OLD_DB` 環境変数での上書きは成功した（実リポジトリの階層での導出は #11 で別途確認済み）。PowerShell コンソールは UTF-8 の psql 出力を CP932 で表示するため日本語が `誁E` のように化けて見えるが**表示だけの問題**（MD5 / バイト数で一致を確認する） |
| 25 | frontend の Nginx が `/api` を `http://backend:8080` へプロキシする | backend（スタブ）を置いた構成で `http://localhost:53080/api/todos` が 200 でスタブ応答を返した。SPA フォールバック（`/nope` → `index.html`）も 200 | ✅ | `proxy_pass http://backend:8080;` は正しい |
| 26 | `localhost` が IPv6 に解決されて接続拒否になる場合がある | `http://127.0.0.1:53080/`・`http://localhost:53080/`・`http://[::1]:53080/` のすべてが 200（`docker compose ps` でも `0.0.0.0:53080` と `[::]:53080` の両方で公開）。なお `Get-NetTCPConnection -State Listen -LocalPort 53080` は何も返さなかった（理由は未調査。到達性の判定には `curl.exe` を使う） | ✅ | この環境では `baseURL` の `127.0.0.1` への変更は不要。ただし **#30 の CORS 問題**があるため、変更する場合は Nginx 側の対応が必要 |
| 27 | HTML の日本語表示（ボタン文言「追加」等） | `dist/index.html` を `<meta charset>` なしで UTF-8 保存して Nginx で配信すると、Chromium が文字コードを誤判定し `button "è¿½åŠ"` と化けて、Playwright の `getByRole('button', { name: '追加' })` が見つからずタイムアウトした。`<meta charset="UTF-8">` を付けると解消 | ⚠️ | タスク4 Todo 1 の `index.html` に `<meta charset="UTF-8">` を必須とする（Nginx は `Content-Type: text/html` に charset を付けない）。E2E のロケーターは日本語に依存するため重要 |
| 28 | Playwright が Windows ネイティブで動く | `@playwright/test` 1.65.1 + Chromium で、`baseURL: 'http://localhost:53080'`、`retries: 1`、`getByTestId('title-input')` / `getByRole('button', { name: '追加' })` / `locator('td', { hasText })` / `page.request.get('/api/todos')` を使うスタブテストが **1 passed（約 0.8 秒）**。Windows Defender 等の確認ダイアログは出なかった。`package.json` に `"type": "module"` なしでも `import` 形式の spec と `export default` の config が動いた | ✅ | `getByTestId` の既定属性は `data-testid`（計画どおり）。**未検証:** `完了にする` / `削除` ボタン、`toHaveClass(/line-through/)`（Vue 実装後） |
| 29 | Spring Boot 3.3.5 + Spring Data JDBC + PostgreSQL のビルド・起動 | 計画どおりの最小構成（`pom.xml`、`Todo` に `@Table` / `@Column("due_date")` 等、`TodoRepository` の `@Query`、`TodoController`、`CorsConfig`、`application.yml`）で `docker compose up -d --build`（backend / frontend のビルド込み）が **44 秒**で完了。`Started TodoApplication in 3.5 seconds`。`maven:3.9-eclipse-temurin-17` → `eclipse-temurin:17-jre` のマルチステージが Windows で動作。`depends_on: new-db: service_healthy` も機能 | ✅ | 計画のスタック指定でビルドできる |
| 30 | CORS が `http://localhost:53080` を許可する | 直接（`:53081`）: `Origin: http://localhost:53080` → `Access-Control-Allow-Origin: http://localhost:53080`。プリフライト（`OPTIONS`、`PATCH`）→ 200 + `Access-Control-Allow-Methods: GET,POST,PATCH,DELETE,OPTIONS`。他のオリジン → 403 `Invalid CORS request`。**Nginx 経由（計画どおりの `proxy_pass` のみ）で `http://127.0.0.1:53080` / `[::1]` から POST / DELETE すると、`Origin: http://127.0.0.1:53080` が許可リストに無く 403** になった（`localhost` は 201） | ⚠️ | ブラウザは同一オリジンでも POST / PATCH / DELETE に `Origin` を付ける。Nginx が `Host: backend:8080` で転送するため、Spring は別オリジンと判定する。`http://localhost:53080` で使う限りは問題ないが、`127.0.0.1` / `[::1]` でアクセスすると追加・トグル・削除だけが 403 になる（GET は成功するので気づきにくい）。**対策（検証済み）:** `nginx.conf` の `location /api/` に `proxy_set_header Host $http_host;` を追加すると、`localhost` / `127.0.0.1` / `[::1]` のすべてで 201、`http://evil.example` は 403 のまま |
| 31 | REST API のステータスとボディ | `POST`（`id:999` / `done:true` を送ってもサーバー側で無視。新 id が採番され `done:false`）→ 201、title 空欄 → 400、`PATCH /{id}/toggle` → 200（2 回で `done` が反転）、存在しない id → 404、`DELETE` → 204、再度 `DELETE` / 存在しない id → 404。JSON キーは `id` / `title` / `done` / `priority` / `dueDate` / `createdAt` / `updatedAt`。移行した 4 件（日本語含む）も `GET` で取得できた | ✅ | 計画の契約（タスク3）で実装できる。**観察 1:** POST のレスポンスの `createdAt` は Java の `LocalDateTime.now()` のままナノ秒 9 桁（例 `…06.099775618`）だが、GET では DB の 6 桁（`…06.099776`）。E2E / JUnit で `createdAt` を厳密比較しないこと。**観察 2:** toggle のレスポンスの `updatedAt` は **UPDATE 前に読み込んだ値**（2 回目の toggle のレスポンスが、1 回目のトリガーで更新された値を返した）で、その UPDATE で DB トリガーが更新した値ではない。`save()` の戻り値には DB トリガーの結果が反映されない。トリガー反映後の値が必要なら toggle 後に `findById` し直す（計画のスコープでは不要。`updatedAt` を画面表示しない限り影響なし） |
| 32 | 日本語タイトルの POST | UTF-8 の JSON ファイル（`--data-binary @file`）で POST すると DB に 27 バイト = 9 文字で正しく保存。一方、**PowerShell 5.1 の `[IO.File]::WriteAllText`（既定は Shift_JIS）で作った JSON ファイルを POST すると文字化け**（47 バイト = 16 文字）したまま保存された。API 側の問題ではなくクライアント側のエンコード | ⚠️ | 日本語を含むテスト用の JSON は `write_file` で作る。PowerShell の `Invoke-RestMethod -Body` に日本語の文字列を直接渡すときも注意が必要（本計画の `Invoke-RestMethod` 例は ASCII の `after-migrate` のみ）。E2E は Node（UTF-8）から送るので影響しない |
| 33 | `package.json` に `"type": "module"` が無い場合 | `"type": "module"` なしで `.js` の設定ファイルを `export default` 形式で書いても **`npm run build` は成功（exit 0、`dist/` 生成）**。ただし Node 24 で `MODULE_TYPELESS_PACKAGE_JSON` 警告（「ES module として再解析。性能低下」）と `The CJS build of Vite's Node API is deprecated` 警告が出る | ⚠️ | `"type": "module"` は**必須ではない**が、警告を避けるため付ける（計画どおり）。**Node 20.x での挙動は未検証**（実機は Node 24 のみ。Node 20 の古いマイナーでは `export default` の自動判定がなく失敗する可能性があるため、`"type": "module"` を推奨のまま維持する） |

### 実行時の注意（実機で観測）

- **`execute_command` の `background: true` で `docker compose up -d --build` を起動しない。** 実機では終了コード 0 だがログが空で、コンテナが 1 つも作成されなかった。通常実行（`-d` 付き）を使う。
- **初回の `docker compose up -d --build`（ルート、Tomcat / Ant / openjdk:7 の取得を含む）は長い。** `timeout_seconds: 270` を指定しても戻らず `TIMED OUT` になったが、その時点でコンテナは `Up` / `healthy` だった。タイムアウト後は再実行せず `docker compose ps` / `docker compose logs --tail=100 <service>` で状態を確認する。
- **PowerShell で日本語を含む SQL を `-c "..."` で直接渡さない。** CP932 とクォート処理で壊れる。日本語を含む SQL は `write_file` で UTF-8 ファイルにして `docker cp` → `psql -f` で流す（実機で日本語タイトルが UTF-8 で 18 バイト = 6 文字として保存されることを確認）。
- コンテナ内の `todos` に残ったテストデータは、確認後に必ず削除する（今回の検証では削除済み）。
- **backend を再作成した直後は、frontend 経由の API が約数秒 502 になる。** backend コンテナの再作成直後（JVM 起動前）に叩くと Nginx のログに `connect() failed (111: Connection refused) while connecting to upstream` が出て 502 になった。約 5 秒待つと 201 に戻った（backend の起動は約 3.5 秒）。タスク5・8 では `docker compose logs backend` で `Started TodoApplication` を確認してから叩く。backend だけを再作成したときに Nginx が古い IP を保持するかは未検証。
- **PowerShell コンソールに出る日本語は化けて見える。** `execute_command` の出力が CP932 で表示されるため、DB や API の実データが正しくても `誁E` のように見える。正否はバイト数・MD5・`=` 比較で判定する。

### 実装後の確認結果（2026-11-19 実機で実装・検証済み）

以前「未検証」だった項目は `migrated/` の実装後に次のとおり確認した。

- ✅ 実際の Vue フロントエンド（`TodoForm.vue` / `TodoTable.vue`）で、タスク4 の UI セレクター契約（「完了にする」「削除」、`<tr>` への `line-through`）が Playwright で通る
- ✅ Playwright の完全な 3 シナリオ（追加 → 完了トグル → 削除）: 1 passed（約 1.5 秒）
- ✅ `TodoControllerTest`（H2 + `@DirtiesContext` + `MODE=PostgreSQL;DATABASE_TO_LOWER=TRUE;CASE_INSENSITIVE_IDENTIFIERS=TRUE`）での `mvn test`（Docker 経由）: 9 テスト成功、約 43 秒（依存取得キャッシュなしの初回を含む）
- ✅ `migrate.sh` による old-db → new-db の 2 コンテナ間移行（Git Bash 経由、実リポジトリ階層）
- ✅ Nginx 経由で `Origin: http://127.0.0.1:53080` からの POST が 201、`Origin: http://evil.example` が 403（`proxy_set_header Host $http_host;` の効果）
- 未検証: Node 20.x での `npm run build`（実機は Node 24 のみ）
- 未検証: Docker Desktop 環境（実機は Rancher Desktop のみ）
- 未検証: WSL2 / Linux ネイティブ
- Mac（Apple Silicon）: 下記「Mac 実機検証結果」で `platform: linux/amd64` のエミュレーション上の起動・ビルド・API・テストを確認済み。**ただし本計画をタスク1から通して実行したわけではない**（後述の注記を参照）

---


## Mac 実機検証結果（2026-11-19 実測）

> **Apple Silicon 上の `platform: linux/amd64`（エミュレーション）について、以下はすべて実機で確認した事実である。Bob は計画の実行時にこれらを再確認しない（`docker run --platform linux/amd64 ...` の動作確認や、JVM が動くかの事前検証は不要）。**
>
> **検証の範囲（重要）:** 検証には、別ディレクトリ（`/Users/oniak3.ai/modernization/ClassicJava201/migrated`）にあった**既存の移行済み実装**（本計画の出力ではない）を一時ディレクトリ（`/Users/oniak3.ai/probe-emu`、`-p probe-emu`）へ複製して使った。したがって「Mac で本計画どおりに最後まで通した」ことの確認ではなく、「Mac のエミュレーション環境で、同じ技術スタック（Spring Boot 3.3.x / PostgreSQL 16 / Nginx / Vue ビルド）が動く」ことの確認である。検証用のコンテナ・ボリューム・イメージ・ディレクトリは削除済み。

**検証環境:** macOS 27.2（ビルド 26B123）/ `uname -m` = `arm64` / Docker は **Rancher Desktop（Lima VM `lima-rancher-desktop`）** `Docker 29.9.3-rd`・`Compose v5.7.0` / `docker` は `/Users/oniak3.ai/.rd/bin/docker`（`execute_command` の PATH で解決できる）/ `docker info --format '{{.OSType}} {{.Architecture}}'` = `linux aarch64` / Node `v24.22.1`・npm `11.19.1`（`/opt/homebrew/bin`）

| # | 確認項目 | 実機の結果 | 計画への影響 |
|---|---------|-----------|-------------|
| E1 | `docker run --rm --platform linux/amd64 alpine uname -m` | `x86_64`（終了コード 0）。コンテナ内の `/proc/cpuinfo` は ARM の `Features` を示すが、`uname -m` は `x86_64`。初回は `alpine` の pull が入る | `platform: linux/amd64` は動作する。**再確認不要** |
| E2 | `postgres:16-alpine` + `platform: linux/amd64` + `docker-entrypoint-initdb.d` | `PostgreSQL 16.14 on x86_64-pc-linux-musl`。起動後約 5 秒で `healthy`。`init.sql`（拡張スキーマ + `update_updated_at` トリガー）が適用され、`\d todos` で 7 列とトリガー `set_updated_at` を確認。ローカルの `postgres:16-alpine` イメージは `linux/arm64` だったが、`platform: linux/amd64` 指定で amd64 として動いた | 計画どおり。initdb のログに `sh: locale: not found` / `no usable system locales` の警告が出るが無害（`en_US.utf8` で初期化され起動する） |
| E3 | backend（`maven:3.9-eclipse-temurin-17` → `eclipse-temurin:17-jre`、両ステージ `--platform=linux/amd64`）のビルドと起動 | `docker compose up -d --build` のイメージビルドが成功（ビルド込みの初回 `up` は約 1 分 52 秒。この回は new-db のマウント問題 #E8 で `up` 自体は失敗終了したが、ビルドは完了していた。マウントを直した 2 回目はキャッシュで約 7 秒）。**`Started TodoApplication in 16.067 seconds`**（Windows 実機の約 3.5 秒より遅いが、`SIGILL` / `Illegal instruction` 等の JVM クラッシュは発生しなかった）。検証した compose は `_JAVA_OPTIONS: "-Xms128m -Xmx256m -XX:+UseG1GC -XX:MaxGCPauseMillis=50"` を backend に設定していた（本計画の compose には無い） | backend は `Started TodoApplication` が出るまで **数十秒（実測 16 秒）** かかる前提で待つ。E2E / curl の前に必ずログで確認する（502 回避） |
| E4 | frontend のホストビルド | Mac ネイティブ（arm64 / Node 24）で `npm install` + `npm run build` が約 5 秒・終了コード 0。`dist/index.html` + `assets/` が生成された。`npm warn install-scripts`（esbuild / fsevents）は出るが成功する。`nginx:alpine`（`--platform=linux/amd64`）にコピーして起動し、`http://localhost:53080/` が 200。HTML に `<meta charset="UTF-8">` を含む | 計画のホストビルド方式は Mac で動く。（Docker 内の `node:20-alpine` amd64 + esbuild のクラッシュは既知の問題として計画に記載されているが、今回は再現確認していない） |
| E5 | `docker run ... maven:3.9-eclipse-temurin-17 mvn test`（`--platform` 指定なし、名前付きボリューム `-v <name>:/root/.m2`、`$PWD` バインドマウント） | **コンテナは `aarch64`（ネイティブ）で動く**（`uname -m` = `aarch64`）。`Tests run: 7, Failures: 0, Errors: 0` / `BUILD SUCCESS`、所要約 27 秒（ボリューム新規・依存取得込み） | 計画のタスク7 のコマンド（`--platform` なし）はそのままでよい。テストはエミュレーションを使わない |
| E6 | API と Nginx 経由の CORS | `GET http://localhost:53081/api/todos` → 200。Nginx 経由（`:53080`）の `POST`（`Origin: http://localhost:53080`）→ 201 で JSON（`id`/`title`/`done`/`priority`/`dueDate`/`createdAt`/`updatedAt`）。`Origin: http://127.0.0.1:53080` → **403**、`Origin: http://evil.example` → 403。**検証した `nginx.conf` は `proxy_set_header Host $host;`**（本計画の `$http_host` ではない）ため 127.0.0.1 が 403 になった。Windows #30 の再現 | **Mac でも #30 は同じ。** 計画の `nginx.conf` は `proxy_set_header Host $http_host;` を必須とする（タスク1 Todo 8）。この Mac では `localhost` なら通る |
| E7 | ポートと既存コンテナの状態（`docker ps -a` / `lsof`） | 検証時は **8080 を既存アプリ `classicjava201-app-1`（`0.0.0.0:8080->8080`、`lsof` では Rancher Desktop の `ssh ... ssh.sock [mux]` が LISTEN）が使用中**だった。このアプリと `classicjava201-db-1` は **別ディレクトリ `/Users/oniak3.ai/modernization/ClassicJava201`** から起動された Compose プロジェクト **`classicjava201`**。**その後ユーザーが停止した（2026-11-19 実測: 両コンテナ `Exited`、`lsof` で 8080 / 53080 / 53081 / 53032 すべて空き、`http://localhost:8080/todo/list` は接続不可）** | 下記「この Mac 固有の既存環境」を参照 |
| E8 | バインドマウントの場所 | `/Users/oniak3.ai/Downloads/ClassicJava201base/sql/init.sql` はコンテナ内でファイルとして読めた（`Downloads` 配下でも macOS の許可ダイアログは出なかった）。一方、**`/tmp/...`（実体 `/private/tmp`）に置いた compose プロジェクトでは `./database/init.sql` のバインドマウントがディレクトリとして作られ、new-db が `psql: error: could not read from input file: Is a directory` で `Exited (1)` になった**。`/Users/oniak3.ai/probe-emu` に移すと成功 | プロジェクトは `/Users/oniak3.ai/` 配下（本リポジトリの `Downloads/ClassicJava201base` は可）で実行する。**`/tmp` 等ホームの外に複製して `docker compose` を実行しない** |

### この Mac 固有の既存環境（実測。計画の実行に影響する）

| 項目 | 実測の状態 | Bob の扱い |
|------|-----------|-----------|
| ルートの既存アプリ（別ディレクトリ由来） | `classicjava201-app-1` / `classicjava201-db-1` は、ユーザーが**停止済み**（`Exited`）。8080 は空き。ボリューム `classicjava201_db-data` は残っている | **本リポジトリのルートで通常どおり `docker compose up -d --build` を実行してよい**（Compose プロジェクト名は `classicjava201base` となり、停止中の `classicjava201` プロジェクトとは別。ポート 8080 は空いている）。**停止中の `classicjava201-*` コンテナ・ボリュームは削除・再起動しない**（別作業のものであり、ユーザーが意図して停止した）。ルートの起動後に `http://localhost:8080/todo/list` が 200 になることを確認する |
| `migrate.sh` の旧 DB 自動検出 | ルートを本リポジトリから起動すると、旧 DB は `classicjava201base-db-1`（ラベル `com.docker.compose.project=classicjava201base`）になり、導出した `ROOT_PROJECT` と一致する見込み（**この点は Mac で未実測**）。自動検出は `docker ps`（稼働中のみ）が対象のため、停止中の `classicjava201-db-1` を誤って拾うことはない | まず `bash migrate.sh` をそのまま実行する。`exit 1`（`old-db / new-db container not found`）になった場合のみ、`docker ps` で実コンテナ名を確認して `OLD_DB=<name> bash migrate.sh` で上書きする |
| 古い `migrated` プロジェクト | 別ディレクトリ（`/Users/oniak3.ai/modernization/ClassicJava201/migrated`）に由来する停止済みコンテナ `migrated-backend-1` / `migrated-frontend-1` / `migrated-new-db-1`（`Exited (255)`）、ボリューム `migrated_new-db-data`（PostgreSQL 16 のデータ入り）、ネットワーク `migrated_migrated-net` が残っている。本計画の compose は `name: migrated` のため**同じプロジェクト名・同じボリューム名を使う** | **初回の `docker compose up` の前に、古いデータが `init.sql` を上書きしない（initdb がスキップされる）ことに注意。** 計画のタスク2 Todo 6 / 再実行ルールの `down -v` を最初に実行すれば解消するが、これは**別の作業で作られた既存データの削除**であり、**ユーザー承認済み（2026-11-19）。Bob はこれ以上ユーザーへ確認しない。** 実行はタスク1 Todo 10 の直前（`migrated/docker-compose.yml` 作成後）、削除対象は `migrated_new-db-data` と同名プロジェクトの停止済みコンテナのみ（`classicjava201_*` など他のボリュームには触れない） |

---

## Mac 環境の注意

> 以下は Mac 固有のリスクと、Bob が迷わないための対処。上の「Mac 実機検証結果」で確認済みの項目は事実として扱い、再確認しない。**Windows 専用の記述（PowerShell・CP932・Git Bash・MSYS パス変換・`.cmd` 読み替え・CRLF）は Mac では無視してよい。**

| # | リスク | 対処 |
|---|--------|------|
| M1 | **全コマンドはプロジェクトルート起点。** 各 `execute_command` は独立したシェルのため、`cd` は同一コマンド内で完結させる（本計画の Mac コマンドは全てそうなっている）。`execute_command` の既定シェルは zsh だが、本計画のコマンドは bash / zsh 共通で動く | 計画のコマンドをそのまま使う。`migrate.sh` だけは必ず `bash migrate.sh` と明示する（zsh で実行しない） |
| M2 | **Docker デーモン未起動。** `docker compose version` はデーモン停止中でも成功する | 「Mac 追加チェック」の `docker info` で確認し、失敗なら中断してユーザーに起動を依頼（この Mac では `linux aarch64` が返ることを確認済み） |
| M3 | **backend の起動に時間がかかる（エミュレーション）。** 実測 16 秒（#E3。JVM クラッシュなし）。**エミュレーション自体は確認済みのため、`platform: linux/amd64` を外す・変更する・事前検証する必要はない** | 長時間コマンドは `execute_command` が戻っても完了とは限らないため、`docker compose ps` / `docker compose logs --tail=100 <service>` で状態を確認してから進める。`Started TodoApplication` がログに出るまで待ち（目安 30 秒以内。`for` ループで 5 秒間隔のポーリング可）、その後に E2E / curl を実行する（502 回避） |
| M4 | **frontend の Node/Vite を Docker 内で動かさない。** | 計画どおり、ホスト（Mac ネイティブ）で `npm run build` → `dist/` を Nginx にコピーする方式を維持する（ホストビルドは #E4 で成功を確認済み） |
| M5 | **`docker` の PATH / 認証ヘルパー。** この Mac では `docker` は `~/.rd/bin/docker`（Rancher Desktop）で、`execute_command` から解決でき、`alpine` の pull も成功した | 他の Mac（Docker Desktop 等）で `command not found` / `error getting credentials` になった場合のみ、ユーザーに PATH の設定を依頼する。シェル設定ファイルを勝手に書き換えない |
| M6 | **バインドマウントの場所。** `Downloads` 配下は問題なし（#E8）。`/tmp` などホームの外はマウントが空ディレクトリになる | プロジェクトのコピーを `/tmp` に作って `docker compose` を実行しない。`init.sql` が反映されない場合は、マウント元が `/Users/` 配下か確認する |
| M7 | **`.DS_Store`。** `src/` 等に既に存在する（`COPY` されても無害） | 削除しない・コミットしない。`migrated/` の `.dockerignore` に `.DS_Store` を足す必要はない |
| M8 | **Mac 標準の bash は 3.2。** `migrate.sh` で bash 4+ 機能（`${var,,}` / `mapfile` / 連想配列）を使うと失敗する | 計画の `migrate.sh`（`tr 'A-Z' 'a-z'`・`head -n1`・`set -e -o pipefail`）は bash 3.2 で動作する書き方。計画外の機能を足さない |
| M9 | **`ROOT_PROJECT` の導出。** このリポジトリのルートは `ClassicJava201base` のため、導出結果は `classicjava201base` になる。ルートを本リポジトリから起動していれば旧 DB は `classicjava201base-db-1` で一致する見込み（未実測）。別ディレクトリ由来の `classicjava201-db-1` は停止済みで、検出対象外 | まず `bash migrate.sh` をそのまま実行し、`exit 1` になった場合のみ `docker ps` で実コンテナ名を確認して `OLD_DB=<name> bash migrate.sh` で上書きする |
| M10 | **`MS Gothic` フォントが Mac に無い。** 旧画面（`list.jsp`: `font-family: "MS Gothic", monospace`）も新画面（`font-legacy`）も同じ `monospace` にフォールバックする | 旧画面と新画面は同じ Mac のブラウザで比較する（Windows 実機の寸法値とは一致しなくてよい）。フォント指定自体は変更しない |
| M11 | **IPv6 の `localhost`。** Mac では `localhost` が `::1` を先に引くことがある | Nginx の `proxy_set_header Host $http_host;`（必須、検証結果 #30）があれば、`localhost` / `127.0.0.1` / `[::1]` のどれでも CORS で 403 にならない。`baseURL` は `http://localhost:53080` のまま変更しない |

---

## Windows 環境の前提条件

> **Mac ユーザーはこのセクションを読み飛ばしてください。**

### 必須ソフトウェア

| ソフトウェア | 用途 | 入手先 |
|------------|------|--------|
| Docker Desktop for Windows **または** Rancher Desktop（dockerd モード）。Linux コンテナ・Compose v2 が使えること | コンテナ実行（実機は Rancher Desktop で検証） | https://docs.docker.com/desktop/install/windows-install/ |
| Git for Windows（**Git Bash 同梱**） | `migrate.sh` 実行環境、git 操作 | https://git-scm.com/ |
| Node.js 20.x 以上（Windows ネイティブ） | `npm run build` / Playwright 実行 | https://nodejs.org/ |

> **WSL2 / Ubuntu / python3 は必須ではない。** 実機（Rancher Desktop）では WSL ディストリが `rancher-desktop` 系のみで `bash` / `python3` が無く、WSL2 前提では `migrate.sh` を実行できなかった。WSL2（Ubuntu）がある環境では、`bash migrate.sh` をそちらで実行してもよい。

### `migrate.sh` は Git Bash から実行する

`migrate.sh` は bash スクリプトのため、**PowerShell / cmd では直接実行できない。** Git for Windows 同梱の `bash.exe` を経由する（`execute_command`（PowerShell）から実行可能。実機で確認済み）。

```powershell
# Windows PowerShell (project root)
Set-Location migrated\database; & "C:\Program Files\Git\bin\bash.exe" migrate.sh; echo "exit=$LASTEXITCODE"
```

> **Git Bash の MSYS パス変換に注意:** `docker exec <c> ls /tmp` のようにコンテナ内の絶対パス（`/tmp` 等）を引数に渡すと、Git Bash が `C:/Users/.../Temp` に書き換える。`migrate.sh` ではコンテナ内の絶対パスを引数にしない（`psql -c "..."` と標準入力パイプのみ使う）。必要な場合は `MSYS_NO_PATHCONV=1` を付ける。
>
> **`bash` を PATH 経由で呼ばない:** 実機の PowerShell では `Get-Command bash` / `sh` が見つからなかった（Git Bash の `bash.exe` は `C:\Program Files\Git\bin\` にあるが PATH に入っていない）。フルパスで呼ぶ。

### 改行コード（CRLF）への注意

Windows の Git は `core.autocrlf=true` がデフォルトのため、シェルスクリプトや設定ファイルが CRLF に変換されることがある。**Windows の場合のみ**、タスク1 の最初に（Mac は不要）プロジェクトルートへ `.gitattributes` を作成して LF 固定にすること（既に存在する場合は追記。**現在のリポジトリには `.git` も `.gitattributes` も存在しない**ため、git 管理外のままなら `.gitattributes` は効果がない。その場合は下記の確認で代替する）:

```
# .gitattributes
*.sh        text eol=lf
*.conf      text eol=lf
*.sql       text eol=lf
Dockerfile  text eol=lf
```

**`migrate.sh` に CRLF が混入していないかの確認（Windows 必須）:** CRLF のままだと bash が `$'\r': command not found` で失敗する。`write_file` で作成した場合は LF・BOM なしで保存されることを実機で確認済み（CR 数 0）だが、念のため PowerShell で確認する（Git Bash / WSL2 のコマンドは不要）:

```powershell
# Windows PowerShell, from the project root. CR count must be 0
$b=[IO.File]::ReadAllBytes("$PWD\migrated\database\migrate.sh"); "CR=$(($b | Where-Object {$_ -eq 13}).Count) BOM=$($b[0] -eq 0xEF)"
```

---

## アーキテクチャ

```
【ホスト】                     【コンテナ内部 (migrated-net)】
:53080 ──→ frontend(Nginx):80
               │ /api プロキシ → backend(Spring Boot):8080
                                      │ JDBC → new-db(PostgreSQL 16):5432

                      【コンテナ内部 (todo-net)】
                      db(PostgreSQL 9.6):5432
                        ↑ migrate.sh がホストから docker exec で接続（ネットワーク直結ではない）

ホスト公開ポート対応:
  frontend  ホスト:53080 → コンテナ:80
  backend   ホスト:53081 → コンテナ:8080
  new-db    ホスト:53032 → コンテナ:5432
  db(既存)  ホスト公開なし（コンテナ内部 todo-net のみ）
```

> パッケージ名: `modernized.example.todo`

**コンテナ構成 (`migrated/docker-compose.yml`):**
- `frontend`: Nginx + Vue.js 静的ファイル
- `backend`: Spring Boot 実行可能 JAR
- `new-db`: PostgreSQL 16

---

## ディレクトリ構成（移行後）

```
migrated/
├── docker-compose.yml            # 全サービス定義（:53080 / :53081 / :53032）
├── frontend/                     # Vue.js 3 + Vite + Tailwind CSS
│   ├── Dockerfile                # ホストビルド dist/ を Nginx にコピー
│   ├── index.html                # Vite エントリーポイント
│   ├── nginx.conf
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── package.json
│   ├── dist/                     # npm run build 生成物（Docker ビルド前に要生成）
│   └── src/
│       ├── main.js               # Vue アプリエントリー
│       ├── style.css             # Tailwind ディレクティブ
│       ├── App.vue
│       ├── components/
│       │   ├── TodoForm.vue
│       │   └── TodoTable.vue
│       └── api/
│           └── todoApi.js
├── backend/                      # Spring Boot (Java 17)
│   ├── Dockerfile                # Maven マルチステージビルド → JRE 実行
│   ├── pom.xml
│   └── src/
│       ├── main/
│       │   ├── java/modernized/example/todo/
│       │   │   ├── TodoApplication.java
│       │   │   ├── model/Todo.java
│       │   │   ├── repository/TodoRepository.java
│       │   │   └── controller/
│       │   │       ├── TodoController.java
│       │   │       └── CorsConfig.java
│       │   └── resources/
│       │       └── application.yml
│       └── test/
│           ├── java/modernized/example/todo/controller/
│           │   └── TodoControllerTest.java
│           └── resources/
│               ├── application-test.yml
│               └── schema-h2.sql
├── database/                     # PostgreSQL 16 初期化スクリプト
│   ├── init.sql                  # 拡張済みスキーマ
│   └── migrate.sh                # データ移行スクリプト（タスク6）
├── e2e/                          # Playwright E2E テスト（タスク8）
│   ├── package.json
│   ├── playwright.config.js
│   └── tests/
│       └── todo.spec.js
└── docs/                         # 移行後アプリのドキュメント
    ├── README.md                 # 起動手順・ポート一覧・テスト実行手順
    ├── architecture.md           # アーキテクチャ説明
    ├── api.md                    # REST API 仕様
    └── migration.md              # データ移行手順（旧DB → 新DB）
```

> **注意:** `migration/` スクリプト（旧DB→新DB移行ツール）は `migrated/docs/migration.md` に手順を記載し、スクリプト本体は `migrated/database/migrate.sh` に格納する。

---

## タスク実行順序と並行化方針

```
[タスク 1: 骨格作成]
        │
        ├─────────────────────┬──────────────────────┐
        ▼                     ▼                      ▼
[タスク 2: DB スキーマ]  [タスク 3: Spring Boot]  [タスク 4: Vue.js]
        │                     │                      │
        └─────────────────────┴──────────────────────┘
                              │
                      [タスク 5: 統合確認]
                              │
        ┌─────────────────────┼──────────────────────┐
        ▼                     ▼                      ▼
[タスク 7: JUnit]  [タスク 8: Playwright E2E]  [タスク 6: データ移行]
                                               （タスク5完了後から並行可）
```

- **タスク 1 完了後**、タスク 2・3・4 は並行して作業可能
- **タスク 5** はタスク 2・3・4 がすべて完了してから着手
- **タスク 7・8・6** はタスク 5 完了後にすべて並行して実施可能（6はテストの完了を待たずに実行可）
- **推奨の実行順（Bob が逐次作業する場合）:** 1 → 2 → 3 → 4 → 5 → 7 → 8 → 6（文書上の記載順と同じ。タスク6 は本書の末尾に置かれているが、番号どおり 6 が 7・8 より先でも問題はない）
- 1 タスク完了ごとに Status を `[x] completed` に更新し、`progress.md` に時刻つきで記録する。自動実行では、重大な問題（停止条件）が無い限りユーザー確認を取らずに次へ進む
- **タスク 7（JUnit）は H2 インメモリで動くため、実際にはタスク 3 完了後すぐ実行できる**（コンテナ不要）。タスク 5 を待つ必要はない
- **タスク 6 の `migrate.sh` 作成はタスク 2 完了後に前倒しできる**が、動作確認（旧 DB・新 DB の両方が起動済み）はタスク 5 の後に行う

---

## サブタスク一覧

---

### タスク 1: `migrated/` プロジェクト骨格の作成

**Intent:** 移行後アプリのディレクトリ構造と Docker Compose の枠組みを用意し、後続タスク（2・3・4）が並行作業できる基盤を作る。

**Expected Outcomes:**
- `migrated/` 配下に frontend / backend / database / docs の4サブフォルダーが存在する
- `migrated/docker-compose.yml` が3サービスを定義している
- 各 Dockerfile が存在しビルドできる（backend は `@SpringBootApplication` のメインクラスを含む最小限の実装が必須。空ソースでは Maven ビルドが失敗する）
- ポート 53080 / 53081 / 53032 でコンテナが起動する（backend は最小の `application.yml`（DB 接続設定 + 既定値）がないと DataSource 作成に失敗して起動しないため、Todo 3 で一緒に作成する）

**Todo List:**
1. `migrated/` ディレクトリ配下に `frontend/` / `backend/` / `database/` / `docs/` を作成する

   **OS別コマンド:**
   ```bash
   # Mac / WSL2
   mkdir -p migrated/frontend migrated/backend migrated/database migrated/docs
   ```
   ```powershell
   # Windows PowerShell
   New-Item -ItemType Directory -Force -Path migrated\frontend, migrated\backend, migrated\database, migrated\docs
   ```

2. `migrated/docker-compose.yml` を作成する（先頭に `name: migrated` を記載してプロジェクト名を固定する。frontend / backend / new-db の3サービス、ネットワーク `migrated-net`、ボリューム `new-db-data`。**全サービスに `platform: linux/amd64`、new-db は `image: postgres:16-alpine`、環境変数 `POSTGRES_DB=tododb` / `POSTGRES_USER=todouser` / `POSTGRES_PASSWORD=todopass`、ポート `53032:5432`、backend は `53081:8080`、frontend は `53080:80`**）。`new-db` サービスには以下の healthcheck を設定する（既存 `docker-compose.yml` と同形式）:
   ```yaml
   healthcheck:
     test: ["CMD-SHELL", "pg_isready -U todouser -d tododb"]
     interval: 5s
     timeout: 5s
     retries: 10
   ```
   `backend` の `depends_on` に `new-db: condition: service_healthy` を設定し、DB 起動前に backend が接続を試みないようにする
3. `migrated/backend/` を Spring Boot プロジェクトとして初期化する（Maven / Java 17 / Spring Boot 3.3.5 / Spring Web / Spring Data JDBC / PostgreSQL ドライバ / pom.xml。バージョンは「技術スタック」節に従う）。`TodoApplication.java`（`@SpringBootApplication` のメインクラス）を作成する。これがないとタスク1の動作確認で Maven ビルドが失敗する。あわせて最小の `src/main/resources/application.yml`（`spring.datasource.url/username/password` を `${DB_URL:jdbc:postgresql://new-db:5432/tododb}` / `${DB_USER:todouser}` / `${DB_PASS:todopass}` で設定）を作成し、docker-compose.yml の backend に同名の環境変数を設定する（タスク3 Todo 10・11 で最終確認）
4. `migrated/frontend/` を Vite + Vue.js 3 + Tailwind CSS プロジェクトとして初期化する（package.json / vite.config.js / tailwind.config.js / postcss.config.js）。依存（バージョンは「技術スタック」節に従う）: dependencies に `vue` / `axios`、devDependencies に `vite` / `@vitejs/plugin-vue` / `tailwindcss`（3.x）/ `postcss` / `autoprefixer`。scripts に `"build": "vite build"` / `"dev": "vite"`。**`package.json` に `"type": "module"` を指定し、設定ファイルは `export default` 形式で書く**（実機で Node 24 + Vite 5.4.21 + Tailwind 3.4 の組み合わせでビルド成功を確認した構成）。`npm install` を実行して `package-lock.json` を生成しておくこと（`npm ci` は `package-lock.json` がないと失敗するため必須）。`npm` が `npm warn install-scripts`（esbuild の postinstall）を出しても、終了コード 0 ならビルドは成功する

   **OS別コマンド:**
   ```bash
   # Mac / WSL2
   cd migrated/frontend && npm install
   ```
   ```powershell
   # Windows PowerShell (requires Node.js installed)
   Set-Location migrated\frontend; npm install
   ```

5. `migrated/backend/Dockerfile` を作成する（マルチステージ: `maven:3.9-eclipse-temurin-17` でビルド → `eclipse-temurin:17-jre` で実行。**両ステージの `FROM` に `--platform=linux/amd64` を明記する**。例: `FROM --platform=linux/amd64 maven:3.9-eclipse-temurin-17 AS build` / `FROM --platform=linux/amd64 eclipse-temurin:17-jre`）。ビルドは `mvn -B -DskipTests package` とする（テストは Docker ビルド内ではなくタスク7 で別途実行する。Docker ビルドをテスト失敗で止めないため）。`pom.xml` → `src` の順に `COPY` するとレイヤーを分けられる
6. `migrated/frontend/Dockerfile` を作成する。**Apple Silicon (arm64) ホストでは `node:20-alpine` の `linux/amd64` エミュレーション上で esbuild がクラッシュするため、マルチステージビルドは使用しない。** ホストで `npm run build` を実行して `dist/` を生成してから Nginx にコピーする単一ステージ方式とする:
   ```dockerfile
   FROM --platform=linux/amd64 nginx:alpine
   COPY dist /usr/share/nginx/html
   COPY nginx.conf /etc/nginx/conf.d/default.conf
   EXPOSE 80
   ```
   `dist/` は `docker compose up --build` 時に Docker ビルドコンテキストに含まれる必要がある。タスク1 の動作確認（Todo 10）前に以下でダミーの空ディレクトリを作成しておくこと（タスク4 Todo 9 で本物の `npm run build` 出力に置き換える）。**`COPY dist ...` は空ディレクトリでもエラーにならないが、`dist` ディレクトリ自体が無いと `COPY failed: file not found` で失敗する。** `migrated/frontend/.dockerignore` に `dist` を書かないこと:

   ```bash
   # Mac / WSL2
   mkdir -p migrated/frontend/dist
   ```
   ```powershell
   # Windows PowerShell
   New-Item -ItemType Directory -Force -Path migrated\frontend\dist
   # (dummy empty directory; replaced by real npm run build output in Task 4 Todo 9)
   ```

7. `migrated/database/init.sql` をプレースホルダーとして作成する（タスク2で内容確定）。あわせて `migrated/frontend/.dockerignore`（`node_modules`）と `migrated/backend/.dockerignore`（`target`）を作成し、ビルドコンテキストの肥大化を防ぐ（`dist/` は除外しないこと）
8. `migrated/frontend/nginx.conf` を**構文的に有効な最小構成**で作成する（`server { listen 80; root /usr/share/nginx/html; location / { try_files $uri /index.html; } location /api/ { proxy_pass http://backend:8080; proxy_set_header Host $http_host; } }`。**`proxy_set_header Host $http_host;` は必須**（無いと `127.0.0.1` / `[::1]` からの POST / PATCH / DELETE が CORS で 403 になる。検証結果 #30）。`backend` ホスト名が解決できないと Nginx 起動に失敗するため、`depends_on` で backend を先に起動させる。内容はタスク4 Todo 8 で確定。`dist/` と同様に Docker ビルドコンテキストに必須）。**LF・UTF-8（BOM なし）で作成する**（BOM / CRLF が混入すると nginx が `unknown directive` で起動しない）。Dockerfile・`migrate.sh` も同様
9. `migrated/docs/README.md` に起動手順の骨格を記載する
10. 動作確認: **（Mac のみ・初回の 1 回だけ）最初の `docker compose up` の前に、古い `migrated_new-db-data` ボリュームを削除する。** ユーザー承認済み（「Mac 実機検証結果」の「古い `migrated` プロジェクト」参照）。`migrated/docker-compose.yml` を作成済みの状態で、次を実行する。`migrated/` で `down -v` を実行すると、このプロジェクト名 `migrated` のボリューム `migrated_new-db-data` と、同名プロジェクトの古い停止済みコンテナ `migrated-*-1` が除去される。**Windows では実行不要**（古いボリュームが無い）:
    ```bash
    # Mac only. Project root; after migrated/docker-compose.yml exists
    cd migrated && docker compose down -v --remove-orphans; docker volume ls -q | grep -c "^migrated_new-db-data"
    ```
    末尾の件数が `0` であること（`1` なら削除できていない。`docker volume rm migrated_new-db-data` を直接実行する。`grep -c` は 0 件のとき終了コード 1 を返すが、これは正常）。

    その後、`migrated/` ディレクトリで **`docker compose up -d --build`（`-d` 必須。フォアグラウンド実行は `execute_command` が戻らなくなる）** を実行し、`docker compose ps` で 3 コンテナが起動（new-db は healthy）していること。この時点では frontend は空ページでよい。CRUD 動作確認はタスク4 Todo 10 / タスク5 で実施。失敗時は `docker compose logs --tail=100 <service>` で原因を確認する（**タスク2〜4 を並列で実装する場合は、この単体起動確認を省略してタスク5 の統合起動で代替してよい。** 骨格だけの起動確認は、後続タスクのファイルが揃うと上書きされて意味を失うため）

    **OS別コマンド:**
    ```bash
    # Mac / WSL2
    cd migrated && docker compose up -d --build && docker compose ps
    ```
    ```powershell
    # Windows PowerShell
    Set-Location migrated; docker compose up -d --build; docker compose ps
    ```

**Relevant Context:**
- 既存 `docker-compose.yml` の `platform: linux/amd64` 設定を踏襲（Apple Silicon 対応）
- ネットワーク名 `migrated-net`（既存の `todo-net` と衝突しない）
- ボリューム名 `new-db-data`（既存の `db-data` と衝突しない）
- `platform: linux/amd64` は backend の Dockerfile と docker-compose.yml の全サービスに設定が必要（frontend は単一 `FROM nginx:alpine` ステージのみのため Dockerfile 先頭の `--platform=linux/amd64` 指定で完結。Node ビルドステージは存在しない）
- **`npm ci` を使う場合は `package-lock.json` が必須。** `package.json` のみ存在する状態では `npm ci` は実行できない。初期化直後は `npm install` で `package-lock.json` を生成すること
- **Apple Silicon + Docker での esbuild 問題:** `node:20-alpine (linux/amd64)` をエミュレーションで動かすと esbuild の Go ランタイムが `lfstack.push` でクラッシュする既知の問題がある。frontend の Docker ビルドステージで Node/Vite を動かさず、ホストビルド + `dist/` コピー方式で回避する
- **Windows の `platform: linux/amd64` について:** Windows（Docker Desktop / Rancher Desktop の WSL2 バックエンド、x86_64 ホスト）では `linux/amd64` イメージはネイティブに動作する（実機で確認）。Apple Silicon 向けのエミュレーション問題は発生しないが、`platform` 指定を統一することで Mac/Windows 間の Dockerfile 互換性を保てる。frontend の Dockerfile の `FROM --platform=linux/amd64 nginx:alpine` は BuildKit が `FromPlatformFlagConstDisallowed` 警告を出すが、ビルドは成功する（実機確認済み）
- **frontend は backend 起動前に起動できない:** Nginx は設定読み込み時に `proxy_pass http://backend:8080` の `backend` を名前解決するため、backend コンテナが存在しないと `host not found in upstream "backend"` で `Exited (1)` になる（実機で再現）。タスク1 Todo 10 では backend も同時に起動できる状態にしてから確認する

**Status:** [ ] pending

---

### タスク 2: PostgreSQL 16 スキーマ設計と DB 初期化（タスク1完了後、並行可）

**Intent:** 既存スキーマを拡張した新スキーマを定義し、new-db コンテナ起動時に自動初期化されるようにする。

**Expected Outcomes:**
- `migrated/database/init.sql` に拡張済みスキーマが記述されている
- `docker compose up -d` 後に new-db の `todos` テーブルが正しいカラム構成で作成されている
- 既存 PostgreSQL 9.6 コンテナは変更されず正常動作している

**Todo List:**
1. 既存スキーマ（`sql/init.sql`）を確認する（既存: `id SERIAL PK / title VARCHAR(200) NOT NULL / done BOOLEAN NOT NULL DEFAULT false / created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP`）
2. 拡張カラムを設計する:
   - `priority` INTEGER NOT NULL DEFAULT 0（0=低 / 1=中 / 2=高）
   - `due_date` DATE（NULL 許容）
   - `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
3. `migrated/database/init.sql` を作成する（CREATE TABLE todos + 全カラム）
4. `updated_at` 自動更新トリガーを作成する。`moddatetime` 拡張は `postgres:16-alpine` に含まれないため、独自 PL/pgSQL トリガー関数で実装する:
   ```sql
   CREATE OR REPLACE FUNCTION update_updated_at()
   RETURNS TRIGGER AS $$
   BEGIN NEW.updated_at = CURRENT_TIMESTAMP; RETURN NEW; END;
   $$ LANGUAGE plpgsql;
   CREATE TRIGGER set_updated_at BEFORE UPDATE ON todos
     FOR EACH ROW EXECUTE FUNCTION update_updated_at();
   ```
5. `migrated/docker-compose.yml` の `new-db` サービスへ `migrated/database/init.sql` をマウントする
6. 動作確認: **Task1 で空の `init.sql` のまま起動済みの場合、`new-db-data` ボリュームは初期化済みで `init.sql` の変更が反映されない。** 先に `migrated/` で `docker compose down -v` を実行してボリュームを削除し、`docker compose up -d --build` で再起動する。その後 `\d todos` でスキーマを確認する

   このコマンドは Mac / WSL2 / Windows PowerShell いずれでも同一（`migrated/` ディレクトリで実行）。**`-it` は TTY のない `execute_command` で失敗するため使わない。** コンテナ名に依存しない `docker compose exec -T` を使う:
   ```bash
   docker compose exec -T new-db psql -U todouser tododb -c "\d todos"
   ```
   > `docker exec` を使う場合は `docker ps` で実コンテナ名を確認し、`-it` ではなく `-i` を使う。

**Relevant Context:**
- 既存スキーマ（`sql/init.sql` 実物より）: `id SERIAL PK / title VARCHAR(200) NOT NULL / done BOOLEAN NOT NULL DEFAULT false / created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP`
- PostgreSQL 16 イメージ: `postgres:16-alpine`
- `docker-entrypoint-initdb.d/` マウントはボリューム空の初回起動時のみ実行される

**Status:** [ ] pending

---

### タスク 3: Spring Boot REST API の実装（タスク1完了後、並行可。ただし `Todo.java` のフィールド定義はタスク2 Todo 2「拡張カラム設計」完了後に着手すること）

**Intent:** Todo CRUD に対応する REST API を Spring Boot で実装し、new-db に JDBC で接続する。

**Expected Outcomes:**
- 以下のエンドポイントが機能する（JSON レスポンス。**ステータスコードとボディは下記に固定**。`api.md`・JUnit・フロントはこれに合わせる）:
  - `GET  /api/todos` — 全件取得（id 昇順）。200 + Todo の JSON 配列（0 件は `[]`）
  - `POST /api/todos` — 新規作成（title 必須、priority / dueDate 任意）。**201 + 作成した Todo の JSON**。title 空欄は 400
  - `PATCH /api/todos/{id}/toggle` — done フラグトグル（updated_at は DB トリガーが自動更新するため Java 側では更新しない）。**200 + 更新後の Todo の JSON**。存在しない id は 404
  - `DELETE /api/todos/{id}` — 削除。**204（ボディなし）**。存在しない id は 404
- Todo の JSON キーは camelCase: `id` / `title` / `done` / `priority` / `dueDate` / `createdAt` / `updatedAt`（フロント・JUnit・E2E・`api.md` で共通）
- CORS 設定でフロントエンド（:53080）からのアクセスを許可
- DB 接続情報は環境変数から取得する（ハードコードしない）

**Todo List:**
1. `migrated/backend/pom.xml` に `spring-boot-starter-validation` を追加する（`@NotBlank` / `@Valid` に必要。`spring-boot-starter-web` には含まれないため明示必須）。`spring-boot-starter-parent` は 3.3.5、Java 17 を指定する。依存は `spring-boot-starter-web` / `spring-boot-starter-data-jdbc` / `postgresql`（runtime）/ `spring-boot-starter-validation`
2. `migrated/backend/src/main/java/modernized/example/todo/model/Todo.java` を作成する（拡張カラム含む `@Table("todos")` / `@Id` / `@Column`。クラスに `@Table("todos")` を明示する）。**`Todo` はエンティティ兼リクエストボディとして使い、`@NotBlank` は `title` フィールドに直接付ける**（別 DTO は作らない）。Spring Data JDBC は `null` フィールドも明示的に INSERT するため DB の `DEFAULT` は使われない。`created_at` / `updated_at` は **Java 側で `LocalDateTime.now()` をセット**する。`@Id` フィールドは `Long`（`null` で INSERT すると DB の `SERIAL` が採番される）。`done` は `boolean`、`priority` は `int`。**Jackson のデシリアライズと toggle の簡素化のため、「デフォルトコンストラクタ + 全フィールドの getter/setter」で実装する**
3. `migrated/backend/src/main/java/modernized/example/todo/repository/TodoRepository.java` を作成する（Spring Data JDBC の `CrudRepository<Todo, Long>`。全件ソートは `@Query("SELECT * FROM todos ORDER BY id ASC")` アノテーションで定義する）
4. `migrated/backend/src/main/java/modernized/example/todo/controller/TodoController.java` を作成する（`@RestController` / `@RequestMapping("/api/todos")`）
5. `GET /api/todos` — `@Query` アノテーション付きリポジトリメソッドを呼び出し全件返す
6. `POST /api/todos` — リクエストボディ（`title` / `priority` / `dueDate`）を `@Valid @RequestBody Todo` で受け取り INSERT。JSON キーは camelCase（`dueDate`）であることに注意（DB列名 `due_date` とは異なる）。`title` の `@NotBlank` を `@Valid` で検証し、空欄の場合は 400 を返す。**クライアントが `id` / `done` / `createdAt` / `updatedAt` を送ってきても無視する**（`id` が非 null だと `save()` が UPDATE になるため必ず `setId(null)`、`done=false`、`created_at` / `updated_at` は `LocalDateTime.now()` をコントローラー側で上書きセット）してから `save()` する（`@ResponseStatus(HttpStatus.CREATED)` で 201、作成した Todo を返す）
7. `PATCH /api/todos/{id}/toggle` — `findById(id)` で取得 → `setDone(!isDone())` で反転 → `save()` で UPDATE（200 + 更新後の Todo を返す）。Spring Data JDBC の `save()` は `@Id` フィールドが非 `null` の場合 UPDATE を実行する。`updated_at` の更新は DB トリガーが担うため Java 側では更新しない。`findById` が空（存在しない id）の場合は `404 Not Found` を返す（`ResponseStatusException(HttpStatus.NOT_FOUND)` をスロー）
8. `DELETE /api/todos/{id}` — id で DELETE。`existsById(id)` で存在確認し、存在しない場合は `404 Not Found` を返す（`PATCH` と同様に `ResponseStatusException(HttpStatus.NOT_FOUND)` をスロー）。削除成功時は `204 No Content`（`@ResponseStatus(HttpStatus.NO_CONTENT)`）を返す
9. CORS 設定: `WebMvcConfigurer` で `http://localhost:53080` を許可。`TodoController.java` に直接書かず、`CorsConfig.java` という独立した `@Configuration` クラスとして `controller/` パッケージ配下に作成する
10. `migrated/backend/src/main/resources/application.yml` に DB 接続設定（`${DB_URL:jdbc:postgresql://new-db:5432/tododb}` / `${DB_USER:todouser}` / `${DB_PASS:todopass}` のように環境変数参照 + 既定値。既定値はテスト・タスク1 起動確認時の未解決プレースホルダー失敗を防ぐための安全策。実運用値は docker-compose.yml の環境変数で渡す）
11. `migrated/docker-compose.yml` の backend サービスに環境変数（DB_URL / DB_USER / DB_PASS）を設定する
12. 動作確認: `docker compose up -d --build`（`migrated/` で実行）後、`curl http://localhost:53081/api/todos` で JSON が返ること。backend の起動に数十秒かかるため、失敗時は直後に判断せず `docker compose logs --tail=100 backend` を確認し、`Started TodoApplication` が出るまで待ってから再実行する

    **OS別コマンド:**
    ```bash
    # Mac / WSL2
    curl http://localhost:53081/api/todos
    ```
    ```powershell
    # Windows PowerShell
    # 'curl' is an alias for Invoke-WebRequest; use curl.exe or Invoke-RestMethod instead
    curl.exe http://localhost:53081/api/todos
    # or
    Invoke-RestMethod http://localhost:53081/api/todos
    ```

**Relevant Context:**
- パッケージ名: `modernized.example.todo`（既存の `com.example.todo` とは別）
- Spring Data JDBC のカラムマッピング: フィールド名がDB列名と完全一致する場合（`title`、`done`、`priority`）は `@Column` 不要。**camelCase フィールドと snake_case DB列名が異なる場合**（`dueDate`→`due_date`、`createdAt`→`created_at`、`updatedAt`→`updated_at`）は `@Column("列名")` を必ず付ける（Spring Data JDBC はデフォルトで camelCase→snake_case の自動変換を行わない）
- DB URL（コンテナ間通信）: `jdbc:postgresql://new-db:5432/tododb`
- DB 認証情報: `todouser` / `todopass`（docker-compose.yml の環境変数として定義）

**Status:** [ ] pending

---

### タスク 4: Vue.js フロントエンドの実装（タスク1完了後、並行可）

**Intent:** list.jsp の構造・機能を Vue.js 3 + Tailwind CSS で再現する。Tailwind の基本スタイルを適用して見た目を整える。

**Expected Outcomes:**
- `http://localhost:53080` でTodoリストが表示される
- 新規追加・完了トグル・削除がすべて動作する
- 拡張カラム（priority / due_date）の表示・入力ができる
- 既存の「タイトル + 追加フォーム + テーブル」レイアウト構成を踏襲しつつ、拡張カラム（優先度・期限）をテーブルとフォームに追加する（既存 list.jsp のカラム: ID / タイトル / 作成日時 / 完了 / 削除 → 移行後: ID / タイトル / 優先度 / 期限 / 作成日時 / 完了 / 削除）
- **見た目（フォント・表の罫線・ヘッダ色・ボタン・入力欄・打消し線）が旧画面 `http://localhost:8080/todo/list` と同じである**（追加列「優先度」「期限」を除く）。Tailwind を使うが、既定の見た目ではなく旧画面に合わせる（Todo 7）

**Todo List:**
1. `migrated/frontend/index.html`（Vite エントリーポイント。**`<html>` に `lang` を付けない**（旧画面と行高を一致させるため。Todo 7）。**`<head>` に `<meta charset="UTF-8">` を必ず入れる**。Nginx は charset を付けないため、無いと日本語が文字化けし、E2E の `getByRole('button', { name: '追加' })` が見つからずタイムアウトする。検証結果 #27）/ `src/main.js`（`createApp(App).mount('#app')`）/ `src/style.css`（`@tailwind base; @tailwind components; @tailwind utilities;`）を作成する
2. `migrated/frontend/src/api/todoApi.js` を作成する（Axios ラッパー: **`baseURL = '/api'`** とする。本番コンテナでは Nginx が `/api` を `http://backend:8080` にプロキシする。開発時は `vite.config.js` の `proxy` 設定（`/api` → `http://localhost:53081`）で吸収する）
3. `migrated/frontend/src/components/TodoForm.vue` を作成する（title 必須テキスト入力 / priority セレクト 低・中・高 / due_date 日付入力 / 追加ボタン）。priority の `<select>` は `value` を数値（0/1/2）で束縛し（`:value="0"` ではなく `v-model.number` を使用）、API へ送る JSON の `priority` フィールドが `Integer` になるようにする。**UI セレクター契約（タスク8 E2E が依存するため必ずこの通りにする）:** title 入力に `data-testid="title-input"`、追加ボタンの文言は「追加」（既存 list.jsp 準拠）。due_date は `<input type="date">`（`dueDate` として送信。未入力は `null`）
4. `migrated/frontend/src/components/TodoTable.vue` を作成する（テーブル: ID / タイトル / 優先度 / 期限 / 作成日時 / 完了ボタン / 削除ボタン）。**UI セレクター契約:** ボタン文言は既存 list.jsp 準拠で、完了ボタンは未完了時「完了にする」・完了済み時「未完了に戻す」、削除ボタンは「削除」（**旧画面と同じ見た目にするため `<button>` ではなく `<form><input type="submit" value="…"></form>` で実装する。** Todo 7）。データ行は `<tbody>` 内の `<tr>`、各セルは `<td>`（ヘッダは `<thead>` の `<th>`）とし、タイトルは `<td>` のテキストとして描画する。JSON は camelCase（`dueDate` / `createdAt`）
5. 完了済みTodo のスタイル: **タイトルを `<td>` 内の `<span>` で包み、完了時のみその `<span>` に `line-through text-[#999999]` を `:class` で適用する**（旧画面 list.jsp の `<span class="done-text">` と同じ構造。`<tr>` 全体には付けない。E2E の `toHaveClass` 検証もこの `<span>` に対して行う）
6. `migrated/frontend/src/App.vue` でコンポーネントを統合し、CRUD 操作をリアクティブに処理する。レイアウトは旧画面と同じ「`<h1>` → 追加フォーム → `<br>` → テーブル」の順にし、ラッパーに余白クラスを付けない
7. **旧画面（list.jsp）と見た目を一致させる**（「完了」「削除」ボタン、追加ボタン、入力欄、表を含む）。Tailwind の既定スタイルをそのまま使うと、ボタンが丸く白い独自デザインになり旧画面と異なるため、次のとおりにする（実機で旧画面と寸法・計算済みスタイルを比較して一致を確認済み）:
   - **`tailwind.config.js` に `corePlugins: { preflight: false }` を設定する**（Preflight がボタン・入力欄のブラウザ標準の見た目を消すため。旧画面はブラウザ標準のボタン）。`content` は `["./index.html", "./src/**/*.{vue,js}"]` を必ず設定する（未設定だとクラスが生成されず、`line-through` も効かない）。`theme.extend.fontFamily.legacy` に `['"MS Gothic"', 'monospace']` を定義する
   - **ボタンは `<button>` ではなく、旧画面と同じ `<form><input type="submit" value="…"></form>` で作る**（完了/削除とも各行に `<form @submit.prevent="…">` を置く。追加ボタンも `<input type="submit" value="追加">`）。`<button>` にクラスを付けて装飾しない。E2E の `getByRole('button', { name })` は `input[type=submit]` にも一致するため契約は変わらない
   - `<body>` → `m-5 font-legacy text-[13px]`（`margin: 20px; font: "MS Gothic", monospace 13px`）。`<html>` に `lang` は付けない（付けると既定の行高が変わり、旧画面と 1px ずれる）
   - `<h1>` → `text-[16px]`（太字・上下余白はブラウザ既定のまま。`font-bold` / `my-*` は付けない）
   - `<table>` → `border-collapse w-[600px]`
   - `th` / `td` 共通 → `src/style.css` に `@layer components { .cell { @apply border border-solid border-[#999999] px-2 py-1 text-left; } }` を定義して `class="cell"` を付ける（Preflight 無効のため `border-solid` が必須）。`th` はさらに `bg-[#cccccc]`
   - テキスト入力 → `w-[300px]`。priority の `<select>` と日付入力には余白クラスを付けない（旧画面の追加フォームと同じ並び）
   - 完了済み → `line-through text-[#999999]`（タイトルの `<span>` のみ）
8. `migrated/frontend/nginx.conf` を作成する（静的ファイル配信 + `/api` → **`http://backend:8080`** プロキシ。`53081` はホスト公開ポートであり、コンテナ間通信では Spring Boot のデフォルトポート `8080` を使う）
9. `npm run build` を実行して `dist/` を生成する（Dockerfile が `dist/` を Nginx にコピーするため、Docker ビルド前に必須）

   **OS別コマンド:**
   ```bash
   # Mac: direct path
   # WSL2: only when Bob's shell itself is WSL2. Do NOT mix with node_modules installed from Windows native (see OS-mix rule)
   cd migrated/frontend && npm run build
   ```
   ```powershell
   # Windows PowerShell
   # npm run build works natively; Node.js / Vite handle path separators automatically
   Set-Location migrated\frontend; npm run build
   ```

10. 動作確認: `http://localhost:53080` でブラウザ CRUD 確認（new-db・backend が稼働している必要があるため、タスク2・3 完了後、またはタスク5 で実施する。タスク4 単独の段階では `npm run build` 成功までを完了条件としてよい）

**Relevant Context:**
- 既存 list.jsp の構成:「TODO リスト」タイトル → 追加フォーム → Todoテーブル
- 削除確認ダイアログは既存に合わせて「なし」（オプションCに含める）
- `vite.config.js` の dev proxy（`/api` → `http://localhost:53081`）は開発時のみ使用
- コンテナ内の Nginx は `/api` を backend コンテナ名でプロキシする

**Status:** [ ] pending

---

### タスク 5: Docker Compose 統合・エンドツーエンド確認（タスク2・3・4完了後）

**Intent:** 全コンテナが連携して正常に動作することを確認し、エンドツーエンドの動作を担保する。

**Expected Outcomes:**
- `docker compose up -d --build`（`migrated/` ディレクトリ内）一発で全サービスがバックグラウンド起動する
- `http://localhost:53080` でTodo CRUD アプリが動作する
- `http://localhost:53081/api/todos` が JSON を返す
- new-db `:53032` に接続してテーブルを確認できる
- 既存アプリ `http://localhost:8080/todo/list` が引き続き正常動作する

**Todo List:**
1. `migrated/docker-compose.yml` の依存関係（`depends_on` / `healthcheck`）を最終確認する（new-db が `service_healthy` になってから backend が起動。frontend は backend の `depends_on` を持つが condition 指定なし＝`service_started`のため、backend コンテナが作成・起動された時点で frontend も起動開始する。Nginx は起動時に `backend` を名前解決するだけで接続はしないため、Spring Boot の起動完了を待つ必要はない）
2. backend の `DB_URL` が `jdbc:postgresql://new-db:5432/tododb` を参照していることを確認する
3. frontend の Nginx が `/api` リクエストを **`http://backend:8080`** にプロキシしていることを確認する（コンテナ間通信は内部ポート `8080` を使用）
4. Spring Boot の CORS 設定が `http://localhost:53080` を許可していることを確認する
5. 全コンテナ起動後にブラウザで CRUD 操作（追加・完了トグル・削除）を確認する
6. 既存アプリとの同時起動確認: 既存 `docker-compose.yml`（ルート）の app サービスは `ホスト:8080`、migrated の backend は `ホスト:53081` を使用するためポート衝突なし。**Mac では、別ディレクトリ由来の既存アプリ（`classicjava201-app-1`）はユーザーが停止済みで 8080 は空いているため、ルートで通常どおり起動する**（停止中の `classicjava201-*` は触らない。「Mac 実機検証結果」の「この Mac 固有の既存環境」参照）。**`execute_command` はフォアグラウンドプロセスが終了しないと戻らないため、両方とも `-d`（デタッチ）で起動する。**（別ターミナルは使えない）。`http://localhost:8080/todo/list`（既存）と `http://localhost:53080`（移行後）が同時に動作することを確認する

   **OS別コマンド（ルート側の既存アプリ起動）:**
   ```bash
   # Mac / WSL2 - project root
   docker compose up -d --build
   # then migrated/
   cd migrated && docker compose up -d --build
   ```
   ```powershell
   # Windows PowerShell - project root
   docker compose up -d --build
   # then migrated/
   Set-Location migrated; docker compose up -d --build
   ```

   **コンテナ状態の確認コマンド:**
   ```bash
   # Mac / WSL2 / Windows PowerShell 共通（各 compose ディレクトリで実行）
   docker compose ps
   # 全コンテナを見る場合
   docker ps
   ```
   起動失敗時は `docker compose logs --tail=100 <service>` で原因を確認する。

7. `migrated/docs/README.md` に最終的な起動手順・ポート一覧・各サービスの説明を記載する。**起動手順には `cd migrated/frontend && npm install && npm run build`（`dist/` 生成）を `docker compose up -d --build` の前に必ず含める**（frontend の Dockerfile は `COPY dist` のため、`dist/` が無い・古いと空ページまたはビルド失敗になる）
8. `migrated/docs/api.md` に REST API 仕様（エンドポイント / リクエスト / レスポンス）を記載する（API 仕様はタスク3で実装済みの内容を転記する）
9. `migrated/docs/architecture.md` にアーキテクチャ図と技術スタックを記載する（実装済みの構成を反映する）

**Relevant Context:**
- ネットワーク: `migrated-net`
- ボリューム: `new-db-data`
- `platform: linux/amd64` が全 Dockerfile と docker-compose.yml に設定されていること
- **Compose コマンド表記:** v2 の `docker compose`（スペース区切り）に統一する。事前に `docker compose version` で利用可否を確認すること（使えない場合のみ `docker-compose` を代替とする）
- **`--format "table ...\t..."` は使わない:** PowerShell では `\t` がタブに展開されないため、`docker compose ps` / `docker ps` で代替する

**Status:** [ ] pending

---

### タスク 7: JUnit バックエンドテスト（タスク5完了後、タスク8と並行可）

**Intent:** Spring Boot REST API の各エンドポイントを JUnit + MockMvc で自動テストし、コード変更時のリグレッションを検出できるようにする。DB は H2 インメモリを使用し、コンテナ不要で `mvn test` 単体で完結させる。

**Expected Outcomes:**
- `mvn test`（`migrated/backend/` 直下）がコンテナなしでパスする
- 以下の4エンドポイントに対するテストが存在する:
  - `GET /api/todos` — 空リスト・1件以上の場合を確認
  - `POST /api/todos` — 正常追加 / title 空欄の場合に 400 を返すことを確認
  - `PATCH /api/todos/{id}/toggle` — done が反転することを確認 / 存在しない id に 404 を返すことを確認
  - `DELETE /api/todos/{id}` — 削除後に GET で件数が減ることを確認 / 存在しない id に 404 を返すことを確認

**Todo List:**
1. `migrated/backend/pom.xml` に以下のテスト用依存を追加する:
   - `spring-boot-starter-test`（`@SpringBootTest` / MockMvc / JUnit 5 を含む）
   - `com.h2database:h2`（テストスコープ）
   - `spring-boot-starter-validation` は**タスク3 Todo 1 で本番依存として追加済みのため、テスト側への重複記載は不要**（Maven テスト実行時は本番の compile スコープ依存が classpath に含まれる）
2. `migrated/backend/src/test/resources/application-test.yml` を作成する（H2 識別子大文字変換問題を回避するため `MODE=PostgreSQL;DATABASE_TO_LOWER=TRUE;CASE_INSENSITIVE_IDENTIFIERS=TRUE` を URL に付加すること）。`application.yml` の `${DB_USER}` / `${DB_PASS}` は既定値なしだと未解決のままテストが失敗するため、`username` / `password` も必ず上書きする（本番側 `application.yml` にも `${DB_USER:todouser}` のように既定値を付けておくとさらに安全）:
   ```yaml
   spring:
     datasource:
       url: jdbc:h2:mem:testdb;MODE=PostgreSQL;DATABASE_TO_LOWER=TRUE;CASE_INSENSITIVE_IDENTIFIERS=TRUE
       driver-class-name: org.h2.Driver
       username: sa
       password: ""
     sql:
       init:
         mode: always
         schema-locations: classpath:schema-h2.sql
   ```
   （`spring.datasource.platform` は Spring Boot 3.x で廃止済みのため使用しない）
3. `migrated/backend/src/test/resources/schema-h2.sql` を作成する（H2 互換の `CREATE TABLE todos` 定義）:
   - PostgreSQL の `SERIAL` は H2 では使用不可。`id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY` に置換する
   - トリガーは不要（`updated_at` は H2 テストでは自動更新しない）
   - `TIMESTAMP` は H2 でも同じ構文で問題なし
4. `migrated/backend/src/test/java/modernized/example/todo/controller/TodoControllerTest.java` を作成する（`@SpringBootTest` + `@AutoConfigureMockMvc` + `@ActiveProfiles("test")` + `@DirtiesContext(classMode = DirtiesContext.ClassMode.BEFORE_EACH_TEST_METHOD)`）。ステータスはタスク3で固定した値で検証する:
   - `GET /api/todos` のテスト（初期空リスト → 200 + `[]`）
   - `POST /api/todos` の正常系（title="テスト", priority=0 → 201 + 作成 Todo の JSON）/ 異常系（title 空欄 → 400）
   - `PATCH /api/todos/{id}/toggle` の正常系（200、`done` が反転）/ 異常系（id=99999 → 404）。事前データは POST で作成して id を取得する
   - `DELETE /api/todos/{id}` の正常系（204、GET で件数減少）/ 異常系（id=99999 → 404）
5. 動作確認: `mvn test` を実行し、グリーンで終了すること。**ホストの JDK / Maven に依存せず Docker 経由で実行する**（実機のホストは JDK 21 のため Java 17 と一致しない。`mvnw` は生成しない）:

   **OS別コマンド:**
   ```bash
   # Mac / WSL2 (run from project root). Named volume caches ~/.m2 so dependencies are not re-downloaded every run
   docker run --rm -v "$PWD/migrated/backend":/app -v migrated-m2:/root/.m2 -w /app maven:3.9-eclipse-temurin-17 mvn test
   ```
   ```powershell
   # Windows PowerShell (run from project root)
   docker run --rm -v "${PWD}\migrated\backend:/app" -v migrated-m2:/root/.m2 -w /app maven:3.9-eclipse-temurin-17 mvn test
   ```
   > ホストに `mvn` が既にある場合のみ `cd migrated/backend && mvn test` でも可。初回は依存取得で数分かかる。Windows では `${PWD}` のパスに日本語・空白が含まれるとマウントに失敗する（ASCII パス前提）。`target/` がホスト側に作られるが `.dockerignore` で Docker ビルドからは除外される。

**Relevant Context:**
- Spring Boot 3.x では `spring-boot-starter-test` に JUnit 5（Jupiter）が含まれる
- H2 の `SERIAL` は使用不可。`BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY`（SQL標準、H2 2.0+対応）を使う
- `spring.datasource.platform` は Spring Boot 3.x で廃止済み。スキーマ初期化は `spring.sql.init.schema-locations` を使う
- `@ActiveProfiles("test")` を付けることで `application-test.yml` が `application.yml` を上書きする
- `@NotBlank` は `spring-boot-starter-validation` が必要（`spring-boot-starter-web` には含まれない）。タスク3 Todo 1（依存追加）・Todo 2（`@NotBlank` 付与）・Todo 6（`@Valid`）はセットで行う
- **テスト間の状態分離:** H2 インメモリ DB は `@SpringBootTest` でコンテキストが共有されるため、テスト間でデータが残留する。`TodoControllerTest` クラスに `@DirtiesContext(classMode = DirtiesContext.ClassMode.BEFORE_EACH_TEST_METHOD)` を付与し、各テスト前にコンテキストをリセットすること
- **H2 の識別子大文字変換問題:** H2 はデフォルトで識別子を大文字に正規化するため、Spring Data JDBC が生成する小文字テーブル名 `"todos"` が H2 上で `"TODOS"` not found エラーになる。`application-test.yml` の JDBC URL に `MODE=PostgreSQL;DATABASE_TO_LOWER=TRUE;CASE_INSENSITIVE_IDENTIFIERS=TRUE` を付加することで回避する:
  ```yaml
  spring:
    datasource:
      url: jdbc:h2:mem:testdb;MODE=PostgreSQL;DATABASE_TO_LOWER=TRUE;CASE_INSENSITIVE_IDENTIFIERS=TRUE
  ```

**Status:** [ ] pending

---

### タスク 8: Playwright E2E テスト（タスク5完了後、タスク7と並行可）

**Intent:** 全コンテナが起動した状態で、ブラウザ操作による CRUD のエンドツーエンドテストを Playwright で自動化する。手動確認（タスク5）をスクリプト化してリグレッション検出に使えるようにする。

**Expected Outcomes:**
- `migrated/e2e/` に Playwright プロジェクトが存在する
- `npx playwright test`（`migrated/e2e/` 直下、コンテナ起動済み前提）がパスする
- 以下のシナリオが自動実行される:
  1. Todo を1件追加 → リストに表示されることを確認
  2. 追加した Todo の完了ボタンをクリック → 打消し線スタイルが適用されることを確認
  3. 追加した Todo の削除ボタンをクリック → リストから消えることを確認

**Todo List:**
1. `migrated/e2e/` ディレクトリを作成し、Playwright を初期化する:
   - `package.json` に `@playwright/test` を追加
   - `playwright.config.js` を作成（`baseURL: 'http://localhost:53080'`、ブラウザ: `chromium` のみ、`retries: 1`）
   - `npm install` 後に `npx playwright install chromium` を実行してブラウザバイナリを取得する（初回のみ必須。これを省略すると `npx playwright test` 実行時にブラウザが見つからずエラーになる）

   **OS別コマンド:**
   ```bash
   # Mac / WSL2
   cd migrated/e2e && npm install && npx playwright install chromium
   ```
   ```powershell
   # Windows PowerShell
   # Playwright runs natively on Windows; WSL2 is not required
   Set-Location migrated\e2e; npm install; npx playwright install chromium
   ```
   > 事前に `docker compose ps`（`migrated/` で実行）で frontend / backend / new-db が起動済みであることを確認する。未起動なら `docker compose up -d --build` を実行する。

2. `migrated/e2e/tests/todo.spec.js` を作成する。以下の3シナリオをひとつの `test` ブロックで順番に実行する。**タイトルは実行ごとに一意にする**（`const title = 'E2Eテスト用Todo-' + Date.now();`）。前回の失敗で残った行があると `page.locator('td', ...)` が複数一致して strict mode violation になるため。ロケーターはタスク4で固定した契約（タスク4 Todo 3〜4 の「UI セレクター契約」）を使う:
   - **追加**: `getByTestId('title-input')` に title を入力 → `getByRole('button', { name: '追加' })` をクリック → `expect(page.locator('td', { hasText: title })).toBeVisible()` で確認
   - **完了トグル**: `const row = page.locator('tr').filter({ hasText: title });` → `row.getByRole('button', { name: '完了にする' })` をクリック → `expect(row.locator('td span', { hasText: title })).toHaveClass(/line-through/)` で確認（`<tr>` ではなくタイトルの `<span>` に付く。タスク4 Todo 5）
   - **削除**: `row.getByRole('button', { name: '削除' })` をクリック → `expect(page.locator('td', { hasText: title })).toHaveCount(0)` で消えたことを確認
3. `migrated/e2e/package.json` にテスト実行スクリプト `"test": "playwright test"` を追加する
4. `migrated/docs/README.md` に E2E テストの実行手順を追記する:
   - Mac / WSL2: `cd migrated/e2e && npx playwright test`
   - Windows PowerShell: `Set-Location migrated\e2e; npx playwright test`
5. 動作確認: コンテナ起動済みの状態で `npx playwright test` がグリーンで終了すること

   **OS別コマンド:**
   ```bash
   # Mac / WSL2
   cd migrated/e2e && npx playwright test
   ```
   ```powershell
   # Windows PowerShell
   Set-Location migrated\e2e; npx playwright test
   ```

**Relevant Context:**
- E2E テストはコンテナが起動済みであることを前提とする（`docker compose up -d --build` 後に実行）。コンテナ起動は Playwright の `globalSetup` では管理しない
- `migrated/e2e/` はディレクトリ構成図に記載済み
- **Windows の注意:** 実機では `localhost` / `127.0.0.1` / `[::1]` のすべてで 53080 に到達できたため、`baseURL` は `http://localhost:53080` のままでよい（検証結果 #26・#28）。繋がらない環境で `http://127.0.0.1:53080` に変更する場合は、Nginx に `proxy_set_header Host $http_host;` が入っていることが前提（無いと追加・削除だけ 403 になる。#30）。初回は `npx playwright install chromium` のダウンロードに数分かかる（実機では確認ダイアログは出なかった）
- **backend 起動待ち:** backend の再作成直後は frontend 経由の API が数秒 502 になる（検証結果「実行時の注意」）。E2E 実行前に `docker compose logs --tail=100 backend` で `Started TodoApplication` を確認する
- 完了後のスタイル確認は `page.locator('tr').filter({ hasText: title })`（`title` は実行ごとに一意な `'E2Eテスト用Todo-' + Date.now()`）の中の **タイトルの `<span>`**（`row.locator('td span', { hasText: title })`）に対して `toHaveClass(/line-through/)` で検証する（旧画面 list.jsp の `.done-text` と同じく、打消し線は `<tr>` ではなくタイトルの `<span>` に付くため）。あわせて `row.getByRole('button', { name: '未完了に戻す' })` が表示されることも確認する
- テスト後のクリーンアップ（追加したデータの削除）はシナリオ内の「削除」ステップで兼ねる
- `migrated/e2e/test-results/`・`playwright-report/`・`node_modules/` は実行時の生成物。リポジトリに含める場合は `.gitignore` で除外するか、確認後に削除する（`.last-run.json` が残る）

**Status:** [ ] pending

---

### タスク 6: データ移行スクリプトの作成（タスク5完了後、タスク7・8と並行可）

**Intent:** 既存 PostgreSQL 9.6 のデータを新 PostgreSQL 16 へ片方向に移行・検証する。

**Expected Outcomes:**
- `migrated/database/migrate.sh` が存在し実行可能である
- スクリプト実行後、old-db の全 todos が new-db に移行されている
- 移行件数の検証で old-db / new-db の件数が一致することを確認できる
- 拡張カラム（priority / due_date / updated_at）はデフォルト値で補完される

**Todo List:**
1. `migrated/database/migrate.sh` を作成する:
   - **実行環境:** ホストに `psql` がインストールされていない前提とし、`docker exec` 経由で実行する（`-it` は使わず `-i` のみ。TTY なし環境で失敗するため）
   - **コンテナ名はハードコードしない。** プロジェクト名はディレクトリ名から決まる（実機のこのリポジトリは `ClassicJava201-handson` → プロジェクト `classicjava201-handson` → old-db は `classicjava201-handson-db-1`。別名で配置・clone された場合は変わる）。Compose のバージョンや起動場所で名前が変わるため、スクリプト冒頭で次のように動的に解決する（導出ロジックは実機の Git Bash で `classicjava201-handson` を得られることを確認済み。`--format '{{.Names}}'` は bash 内ではシングルクォートで問題ない）:
     ```bash
     SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"   # 実行場所に依存しないようスクリプト基準にする
     ROOT_PROJECT="$(basename "$(cd "$SCRIPT_DIR/../.." && pwd)" | tr 'A-Z' 'a-z')"
     OLD_DB=${OLD_DB:-$(docker ps --filter "label=com.docker.compose.service=db" --filter "label=com.docker.compose.project=$ROOT_PROJECT" --format '{{.Names}}' | head -n1)}
     NEW_DB=${NEW_DB:-$(docker ps --filter "label=com.docker.compose.service=new-db" --filter "label=com.docker.compose.project=migrated" --format '{{.Names}}' | head -n1)}
     [ -n "$OLD_DB" ] && [ -n "$NEW_DB" ] || { echo "old-db / new-db container not found. Run: docker ps"; exit 1; }
     ```
     （`migrated/docker-compose.yml` の先頭に `name: migrated` を書いておくと new-db のプロジェクト名が固定される。ルート側 `docker-compose.yml` は変更しない。ルート側の project 名が上記の導出と合わない場合は、`docker ps` で実名を確認して環境変数 `OLD_DB` で上書きできるようにする）
   - **冪等化:** 先に new-db を `TRUNCATE todos RESTART IDENTITY;` する（再実行・Task5/8 で入ったデータとの PK 衝突を防ぐ）
   - **拡張カラムは old-db 側の SELECT で補完する（python3 / awk を使わない）。** priority=0 / due_date=NULL / updated_at=created_at は定数と既存列だけで表現できるため、エクスポートの SELECT に直接書く。**ヘッダなし**の 7 列 CSV を new-db へパイプで流す（実機の Git Bash で ASCII・日本語の両行が一致し、`NULL` は空欄 → `due_date` の NULL として投入されることを確認済み）:
     ```bash
     docker exec "$OLD_DB" psql -U todouser tododb -c "COPY (SELECT id, title, done, created_at, 0, NULL, created_at FROM todos ORDER BY id) TO STDOUT CSV" \
       | docker exec -i "$NEW_DB" psql -U todouser tododb -c "COPY todos(id, title, done, created_at, priority, due_date, updated_at) FROM STDIN CSV"
     ```
     `set -e -o pipefail` を先頭に置き、どちらかの `docker exec` が失敗したらスクリプトも失敗させる。`COPY` 内の `-c "..."` の引数にコンテナ内の絶対パスは含めない（Git Bash の MSYS パス変換を避ける）
   - **シーケンス補正（必須）:** `COPY` で id を直接投入するとシーケンスが 1 のままで、移行後の新規追加が PK 重複になる。インポート後に必ず実行する:
     `docker exec "$NEW_DB" psql -U todouser tododb -c "SELECT setval(pg_get_serial_sequence('todos','id'), COALESCE((SELECT MAX(id) FROM todos), 1), (SELECT COUNT(*) > 0 FROM todos));"`

   > **Windows での実行方法（実機検証済み）:**
   > `migrate.sh` は bash スクリプトのため、**PowerShell / cmd からは直接実行できない。** Git for Windows 同梱の Git Bash を `execute_command`（PowerShell）から呼び出す。
   >
   > ```powershell
   > # Windows PowerShell
   > Set-Location migrated\database; & "C:\Program Files\Git\bin\bash.exe" migrate.sh; echo "exit=$LASTEXITCODE"
   > ```
   >
   > - **PowerShell 自身で `docker exec | docker exec -i` のパイプを組まないこと。** 日本語を含む行で `invalid input syntax for type boolean` になり壊れる（ASCII のみなら成功するため気づきにくい）。必ず bash の中でパイプする。
   > - `ROOT_PROJECT` はスクリプトの 2 階層上のディレクトリ名から導出する。Git Bash でも `C:\share\ClassicJava201-handson` から `classicjava201-handson` が得られ、Windows 側から起動したルートの compose プロジェクト名と一致する。ルート側を別名のディレクトリ・`-p` 指定で起動していた場合は一致しないため、その場合は `OLD_DB=<実コンテナ名> bash migrate.sh` で上書きする。
   > - Git Bash が無い環境では WSL2（Ubuntu）の `bash` でも同じスクリプトが動く（`/mnt/c/...` に移動して `bash migrate.sh`）。
   > - **フォールバック（bash が一切無い場合）:** 日本語データを含めて動作確認済みの方式は `COPY (SELECT ...) TO '/tmp/out.csv' CSV` → `docker cp <old>:/tmp/out.csv <host>` → `docker cp <host> <new>:/tmp/in.csv` → `COPY todos(...) FROM '/tmp/in.csv' CSV`（PowerShell から実行可能。コンテナ内ファイルの `COPY ... TO/FROM` はスーパーユーザー権限が必要で、`todouser` は `POSTGRES_USER` のためスーパーユーザー）。

2. 検証クエリを組み込む（移行前後の件数比較）:
   - old-db: `SELECT COUNT(*) FROM todos;`
   - new-db: `SELECT COUNT(*) FROM todos;` で件数一致を確認
   - **テストデータ:** `sql/init.sql` にシードデータはなく old-db は空のため、動作確認前に old-db へ数件投入しておく（0 件同士の一致は検証にならない）:
     `docker exec "$OLD_DB" psql -U todouser tododb -c "INSERT INTO todos(title, done) VALUES ('migrate-test-1', false), ('migrate-test-2', true), ('migrate-test-3', false);"`
     （`$OLD_DB` は `migrate.sh` 内の変数。**Bob が単体で実行する場合は、Mac / WSL2 / Windows 共通で `docker compose -f docker-compose.yml exec -T db psql -U todouser tododb -c "INSERT ..."`（プロジェクトルートで実行）を使う**。PowerShell ではシングルクォートを含む SQL を `-c "..."` の二重引用符で囲む形で問題ないが、`$` を含む式は書かない）
3. `migrated/docs/migration.md` に移行手順（前提条件・実行コマンド・確認手順・ロールバック方針）を記載する。**Windows ユーザー向けに「Git Bash（または WSL2 の bash）から実行する。PowerShell のパイプでは実行しない」旨を前提条件に明記すること。**
4. 動作確認: 両 DB が稼働中に（ルートの `docker compose up -d` と `migrated/` の `docker compose up -d --build` の両方が起動済み）、テストデータ投入後に `migrate.sh` を実行し、件数が一致（かつ 1 件以上）すること。移行後に API から 1 件追加して 500 にならないこと（シーケンス補正の確認）。API 追加は次のコマンドで行う:
   ```bash
   # Mac / WSL2
   curl -X POST -H "Content-Type: application/json" -d '{"title":"after-migrate","priority":0}' http://localhost:53081/api/todos
   ```
   ```powershell
   # Windows PowerShell (curl.exe + escaped quotes is error-prone; use Invoke-RestMethod)
   # NOTE: curl.exe -d "{\"title\":\"x\"}" loses the inner quotes in PowerShell 5.1 and the API returns 400.
   #       If curl.exe is needed, write the JSON with write_file and pass it via --data-binary "@file.json".
   Invoke-RestMethod -Method Post -Uri http://localhost:53081/api/todos -ContentType "application/json" -Body '{"title":"after-migrate","priority":0}'
   ```
   > 確認後、不要なテストデータ（`migrate-test-*` / `after-migrate`）は残してよいが、Task8 の E2E は一意タイトルのため影響しない。

   **OS別対応:**
   - **Mac / WSL2:** Bob が `execute_command` で直接実行できる（`bash migrate.sh` と明示して呼ぶので `chmod +x` は不要。Mac 標準の bash は 3.2 のため、`migrate.sh` には bash 4 以降の機能（`${var,,}` / `mapfile` / 連想配列）を使わない）
     ```bash
     cd migrated/database && bash migrate.sh; echo "exit=$?"
     ```
     件数確認（プロジェクトルートで実行。下記 Windows 欄と同一コマンドで、Mac / WSL2 でもそのまま使える）:
     ```bash
     docker compose -f migrated/docker-compose.yml exec -T new-db psql -U todouser tododb -c "SELECT COUNT(*) FROM todos;"
     docker compose -f docker-compose.yml exec -T db psql -U todouser tododb -c "SELECT COUNT(*) FROM todos;"
     ```
   - **Windows:** Bob が `execute_command`（PowerShell）から Git Bash 経由で実行する（ユーザーへの手動依頼は不要）:
     ```powershell
     Set-Location migrated\database; & "C:\Program Files\Git\bin\bash.exe" migrate.sh; echo "exit=$LASTEXITCODE"
     ```
     Git Bash が存在しない場合のみ、ユーザーに WSL2 / Git Bash ターミナルでの手動実行を依頼する。件数確認は Bob が PowerShell から実行できる。**old-db 側と new-db 側を両方確認し、件数を比較する**（`-f` で compose ファイルを指定。プロジェクトルートで実行）:
     ```powershell
     # new-db (migrated)
     docker compose -f migrated/docker-compose.yml exec -T new-db psql -U todouser tododb -c "SELECT COUNT(*) FROM todos;"
     # old-db (root compose)
     docker compose -f docker-compose.yml exec -T db psql -U todouser tododb -c "SELECT COUNT(*) FROM todos;"
     ```

**Relevant Context:**
- 移行は片方向のみ。双方向同期は行わない
- old-db は `ports:` 設定がなくホストから直接接続不可。`migrate.sh` は `docker exec` 経由でコンテナ内から操作する（`localhost:5432` への直接接続は不可）
- new-db はホスト公開ポート `53032` があるため、ホストから `postgresql://todouser:todopass@localhost:53032/tododb` で接続可能（検証用途）
- `docker compose down -v`（`migrated/` で実行）で new-db のボリュームを削除するとデータが消える点に注意。old-db を消すのはルートで `docker compose down -v` を実行した場合のみ
- ロールバック: new-db のデータを削除して再実行するだけでよい（旧DBは常に正）
- **Windows 固有の注意まとめ（実機検証ベース）:**
  - `migrate.sh` は Git Bash（`C:\Program Files\Git\bin\bash.exe`）から実行する。WSL2 は不要（実機は Rancher Desktop 専用ディストリのみで `bash` / `python3` が無かった）
  - パイプは bash 内で行う。PowerShell の `docker exec | docker exec -i` は日本語で壊れる
  - Git Bash は `docker exec <c> ls /tmp` の `/tmp` を `C:/Users/.../Temp` に変換する。コンテナ内絶対パスを引数にしない（必要なら `MSYS_NO_PATHCONV=1`）
  - 日本語を含む SQL を PowerShell の `-c "..."` で渡さない（CP932 とクォート処理で壊れる）。必要なら `write_file` で UTF-8 の `.sql` を作り `docker cp` → `psql -f` で流す
  - **検証の範囲:** old-db（9.6）→ new-db（16）の 2 コンテナ間を、実リポジトリの階層（`ROOT_PROJECT=classicjava201-handson` が旧 DB に一致）で Git Bash 経由に実行し、`COPY 3`・件数一致（3 / 3）・`setval` 後の API 追加 201（id=4）を確認済み（2026-11-19）。日本語データを含む 2 コンテナ間移行は、事前の一時構成による検証（#24）で MD5 一致を確認済み

**Status:** [ ] pending

---

## オプション計画: Tailwind CSS デザイン改良

> **本計画のタスク1〜8の実装対象外。** ユーザーから明示的に依頼があるまで Bob は着手しないこと。基本機能の実装が完了した後、以下のデザイン改善を段階的に適用できる。

### Option A: レスポンシブ対応
- テーブルをモバイルでカード表示に切り替え（`sm:hidden` / `hidden sm:table`）
- フォームを縦積みレイアウトに対応

### Option B: ダークモード対応
- `dark:` バリアントで背景・テキスト・ボーダー色を調整
- `darkMode: 'class'` 設定 + トグルボタン

### Option C: インタラクション強化
- 追加フォームのバリデーション表示（title 空欄エラー）
- 削除前の確認ダイアログ（Vue モーダル）
- Todo 追加・削除時のフェードアニメーション（`transition` / `opacity`）

### Option D: 優先度・期限の視覚化
- 優先度バッジ: `bg-red-100 text-red-700`（高）/ `bg-yellow-100`（中）/ `bg-gray-100`（低）
- 期限切れ行を `bg-red-50` でハイライト
- 期限3日以内の行を `bg-yellow-50` でハイライト

---

## 技術スタック（移行後）

バージョンは以下に固定する（Bob が推測で選ばないこと）。

| レイヤー | 技術 | バージョン |
|---------|------|---------|
| フロントエンド | Vue.js 3 + Vite + `@vitejs/plugin-vue` + Tailwind CSS（+ PostCSS / Autoprefixer） | vue `^3.4` / vite `^5` / `@vitejs/plugin-vue` `^5` / tailwindcss `^3.4` |
| HTTP クライアント | Axios | `^1` |
| バックエンド | Spring Boot + Spring Data JDBC | 3.3.x（`spring-boot-starter-parent` 3.3.5 を推奨）/ Java 17 |
| DB | PostgreSQL | 16 (alpine) |
| ビルドツール | Maven (backend) / Vite (frontend) | Maven 3.9 / Vite 5 |
| コンテナ | Docker Compose v2（`docker compose` コマンド） | — |

---

## OS別コマンド早見表

| 操作 | Mac / WSL2 | Windows PowerShell |
|------|-----------|-------------------|
| ディレクトリ作成 | `mkdir -p migrated/frontend/dist` | `New-Item -ItemType Directory -Force -Path migrated\frontend\dist` |
| コンテナ起動（バックグラウンド） | `cd migrated && docker compose up -d --build` | `Set-Location migrated; docker compose up -d --build` |
| コンテナ一覧 | `docker compose ps` | `docker compose ps` |
| API 確認 | `curl http://localhost:53081/api/todos` | `Invoke-RestMethod http://localhost:53081/api/todos` |
| Maven テスト（Docker 経由・推奨） | `docker run --rm -v "$PWD/migrated/backend":/app -v migrated-m2:/root/.m2 -w /app maven:3.9-eclipse-temurin-17 mvn test` | `docker run --rm -v "${PWD}\migrated\backend:/app" -v migrated-m2:/root/.m2 -w /app maven:3.9-eclipse-temurin-17 mvn test` |
| npm ビルド | `cd migrated/frontend && npm run build` | `Set-Location migrated\frontend; npm run build` |
| migrate.sh 実行 | `cd migrated/database && bash migrate.sh` | `Set-Location migrated\database; & "C:\Program Files\Git\bin\bash.exe" migrate.sh`（Git Bash 経由。WSL2 不要） |
| E2E テスト | `cd migrated/e2e && npx playwright test` | `Set-Location migrated\e2e; npx playwright test` |
| 時刻取得（`progress.md` 用、JST） | `TZ=Asia/Tokyo date "+%Y-%m-%d %H:%M:%S"` | `Get-Date -Format "yyyy-MM-dd HH:mm:ss"` |
