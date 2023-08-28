## シンプルHelloWorldサンプル
### 当プロジェクトについて
このプロジェクトは、OpenLibertyを使用したHelloWorldをクイックに体験する目的で作成されています。
作成内容は、OpenLibertyのサイトにある「Get started」で取得できるものとほぼ同じです。
ローカルのJava環境で実行するパターンと、GitHub Codespacesで実行するパターンの2つが選べます。

### ローカル環境準備
ローカルで実行する場合、[Javaのインストール](https://developer.ibm.com/languages/java/semeru-runtimes/downloads/)が必要です。
当機能はSemeruRuntimeのJava17で動作確認しています。

### アプリ起動（ローカル）
ここではWindows環境を例にとります。
- 当リポジトリのクローンをローカルに作成する。
- コマンドプロンプトでカレントフォルダを当プロジェクトのトップ(READMEが置いてあるフォルダ)に移動する。
- mvnw liberty:dev　を実行する。

### アプリ実行確認（ローカル）
動作確認は、ローカルブラウザから[アプリのURL](http://localhost:9080/ghcs/api/hello)にアクセスします。
「Hello World」と出力されれば正常です。

### アプリ起動（Codespaces）
こちらはCodespaces上にJavaが自動でインストールされるため、ローカルでの準備は不要です。
- 利用者のGitHubアカウントに、当リポジトリの内容をフォークする。
- GitHubのWeb画面で、フォークしたリポジトリの右上にある「Code」から、「Create codespace on main」を選択する。
- 起動するVScodeのターミナルから ./mvnw liberty:dev を実行する。

### アプリ実行確認（Codespaces）
動作確認は、ローカルブラウザから[アプリのURL](http://localhost:9080/ghcs/api/hello)にアクセスします。
「Hello World」と出力されれば正常です。

