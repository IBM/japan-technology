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
「Hello World!!」と出力されれば正常です。

### アプリ起動（Codespaces）
こちらはCodespaces上にJavaが自動でインストールされるため、ローカルでの準備は不要です。
- 利用者のGitHubアカウントに、当リポジトリの内容をフォークする。
- japan-technology/liberty-sample/hello-world/.devcontainer のフォルダを、2階層上（japan-technologyの下）に移動する。GitHub上で完結させる場合、リポジトリを表示させた状態で「.」を押してVScode相当の編集画面を起動し、ここから編集（移動とコミットプッシュ）を行なう。
- GitHubのWeb画面で、フォークしたリポジトリの右上にある「Code」から、「Create codespace on main」を選択する。
- 起動するVScodeのターミナルから、次のコマンドを実行する。
- cd liberty-sample/hello-world
- ./mvnw liberty:dev

### アプリ実行確認（Codespaces）
次の手順で、開発コンテナ上のポートをローカルブラウザからアクセスできるようにします。
- ターミナル画面横の「ポート」を開く。
- 「ポートの追加」をクリックし、9080を入力する。
動作確認は、ポート画面の「ローカルアドレス」列に表示されたURLに「/ghcs/api/hello」を追加してアクセスします（例：https://xxx-9080.app.github.dev/ghcs/api/hello）。
「Hello World」と出力されれば正常です。

