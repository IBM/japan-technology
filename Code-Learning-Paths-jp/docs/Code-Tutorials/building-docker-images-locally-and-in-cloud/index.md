---
also_found_in:
- learningpaths/get-started-containers/
authors: ''
check_date: '2021-12-03'
completed_date: '2019-04-02'
components:
- docker
draft: false
excerpt: Dockerコマンド、Dockerfile、コンテナレジストリーを使ったDockerの使用について学びます。
last_updated: '2020-12-03'
meta_description: コンテナの基本とDockerコマンドを学び、Dockerfileの書き方、Dockerイメージの構築、動作するコンテナインスタンスの作成、Quayコンテナレジストリの使用方法を学びます。
meta_keywords: docker container, dockerfile, docker image, container tutorial, docker
  tutorial
meta_title: コンテナの基礎知識。Dockerfileの作成とDockerイメージの構築
primary_tag: containers
related_content:
- slug: accessing-dockerhub-repos-in-iks
  type: tutorials
- slug: docker-dev-db
  type: tutorials
- slug: introduction-to-containers-with-nodejs-and-kubernetes-on-openshift
  type: videos
related_links:
- title: Install Docker
  url: https://docs.docker.com/get-docker/
- title: Best practices for writing Dockerfiles
  url: https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- title: How to use Docker volumes
  url: https://docs.docker.com/storage/volumes/
- title: Red Hat Quay container registry
  url: https://quay.io/
subtitle: Dockerコマンド、Dockerファイル、コンテナレジストリでのDockerの使用
time_to_read: 45 minutes
title: コンテナ化。Dockerで始めるコンテナ化
---

コンテナ化された世界への旅を始めようとしているなら、最初に出会うのは<a href="(https://www.docker.com/)" target="_blank" rel="noopener noreferrer nofollow">Docker</a>でしょう。このチュートリアルでは、Docker、Dockerfiles、Red Hat Quayコンテナレジストリで遊ぶためのツールを提供することで、迅速なスタートを切ることができます。

## 前提条件

* Dockerアカウント。[Free Pricing Plan](https://www.docker.com/pricing/)が利用できます。
* [Red Hat Quay.io](https://quay.io/)のアカウント。[30日間の無料トライアル](https://quay.io/plans/)が可能です。

## 見積もり時間

このチュートリアルを完了するには、約45分かかります。

## Docker

まず最初に、Docker をインストールします。いくつかの方法がありますが、最初で最良の方法は、メインの<a href="https://docs.docker.com/get-docker/" target="_blank" rel="noopener noreferrer nofollow">Docker documentation site</a>に行くことです。最新バージョンのDockerを使用し、メンテナンスするようにし、特定のオペレーティングシステム用にインストールしてください。

このチュートリアルを書いている時点では、Dockerには主に2つのエディションがあります。ここでは、それぞれのバージョンについて少し触れてみたいと思います。Docker Community Edition (docker-ce`)とDocker Enterprise Edition (docker-ee`)です。どちらも利点があり、異なるユースケースを対象としています。このチュートリアルを一通り終えたら、`docker-ce`と`docker-ee`のどちらが自分に合っているかを再検討することを強くお勧めします。

以下の手順とコマンドは、どちらのバージョンでも動作するはずですので、進めていきましょう。

### Docker CLI

`docker`のインストールが完了したら、コマンドプロンプトを立ち上げます。インストール中に、ドキュメントで実行を求められることがあるサニティチェックがあります。ここでは、すべてが期待通りに動作していることを確認するために、再度以下を実行してみます。


以下のような出力が表示されるはずです。(もしエラーが出たり、以下のようなものではない場合は、インストールが正しく設定されていないので、先に進む前に解決する必要があります)。


おめでとうございます。これで`docker`インスタンスが動き出しました。早速、遊んでみましょう。

次に試していただきたいのは、以下のコマンドです。インターネットのアクセス状況によっては、実行に少し時間がかかるかもしれませんが、幸いにもあなたのマシンにキャッシュされますので、その後、少しずつ見直していきましょう。


これが実行されると、何が起こっているのかを説明しましょう。`docker`コマンドを実行すると。公開されているDockerハブから最新のコピーを取得し、それを `/bin/bash` というシェルで実行することをDockerに伝えています。
このコマンドはインターネットに接続し、あなたが持っているバージョンを確認し、キャッシュイメージのSHAと照合し、もし持っていなければDocker Hubからダウンロードします。
わかりやすくするために、`-it`は`interactive`として実行し、コンテナの`tty`を作成します。
これで以下のように表示されるはずです。


おめでとうございます。これで、2つ目のDockerコンテナが起動しました。先に進んで `exit` と入力し、もう一度 `docker` コマンドを実行してください。


ルートが `@2de726a5fcb8` と `@583c6cec5d41` で異なることに気付きましたか？これは、この方法でコンテナをスピンアップすると、それらがエフェメラルになるからです。エフェメラルとは、実行している間だけ生き続けるという意味で、終了するとすぐに消えてしまいます。長寿命のコンテナを作る方法は、もう少し後にご紹介します。

それでは、コンテナの中でちょっと遊んでみましょう。<a href="https://www.centos.org/" target="_blank" rel="noopener noreferrer">CentOSマシン</a>では、`yum`がありますので、何かをインストールしてみましょう。


これで、コンテナ内で `vim` を実行できるようになりました!ぜひ試してみてください。


もし、`vim`を終了する方法がわからない場合は、`:q`と入力してください。と入力すると、コマンドプロンプトが再び表示されます。

ここでもう一度 `exit` と入力してください。


念のために言っておきますが、コンテナがなくなると、その中のすべての変更も消えてしまいます。

### Dockerfile

さて、コンテナを起動して変更を加えることはできましたが、変更を維持するにはどうすればよいのでしょうか？いくつかの方法がありますので、ご自身で調べてみることをお勧めします。しかし、ここでは最も一般的な方法である、`Dockerfile`を使った方法を説明します。

コマンドプロンプトに戻って、新しいディレクトリを作り、お好みの`$EDITOR`を使って、`Dockerfile`という新しいファイルを開いて、ディレクトリを変更します。


ここでは`Dockerfiles`のハイライトを紹介しますが、そのパワーに触れるためには、<a href="https://docs.docker.com/develop/develop-images/dockerfile_best-practices/" target="_blank" rel="noopener noreferrer nofollow">Best practices for writing Dockerfiles</a>のドキュメントに目を通すことを強くお勧めします。

あなたの`Dockerfile`に、以下のように書き出します。


ファイルを保存し、ファイル名が `Dockerfile` であることを確認してください。

前の4行の意味を説明しましょう。

* `FROM` : `centos`:`latest` のDockerイメージからレイヤーを作成します。
* `RUN` : コンテナに `vim` をインストールし、`/vim` というディレクトリを作成してコンテナをビルドします。
* `WORKDIR` : コンテナの作業ディレクトリを通知します。
* `ENTRYPOINT` : コンテナの起動時に実行されるコマンドで、上記のように `/bin/bash` の代わりに実行されます。

では、これをローカルにビルドしてみましょう。`Dockerfile`があるディレクトリで以下を実行して、これが完成するのを見てみましょう。
を実行してみましょう。


**注意**:ハッシュが異なる `eda2652aa25e` になっているはずなので、その点に注意してください。

おめでとうございます。最初の `Dockerfile` とカスタマイズされた Docker コンテナを構築しました。

では、実際に動かしてみましょう。次のコマンドを実行してください。


すると、`vim` が起動するのがわかるはずです!そして、再びコマンドプロンプトが表示されます。これは何度でも実行することができ、毎回新しい `vim` のインスタンスが作成されますが、コンテナなので実際には何も保存できませんし、何も読むことができませんよね？これを修正しましょう。

ローカルディレクトリをコンテナにマウントするために、bind mountとvolumeを追加しましょう。マウントとボリュームについてもっと詳しく知りたい方は、<a href="https://docs.docker.com/storage/volumes/" target="_blank" rel="noopener noreferrer nofollow">Docker documentation about how to use volumes</a>から始めることをお勧めします。難しい概念の1つですが、時間をかける価値はあります。

コマンドラインで `hello` という名前のファイルを作成し、その中に `hello world` という言葉を保存します。


それでは、ローカルディレクトリをコンテナにマウントしてみましょう。


「vim」の中で、「:e hello」と入力します。すると、`hello world`と表示されるはずです。ご覧のように、ホストマシンで作成したファイルを開き、`vim`の入ったコンテナを作成し、ディレクトリをマウントして、ファイルを開くことができました!

よろしければ、`i`と入力して何かを打ち出してみてください。そして、終わったら `:wq` と入力してください。コンテナが終了して、コマンドラインで次のように入力できるようになります。


**注**:明らかに、`I added this line from my container`は私が書いたものです。あなたが書いたものは何でも表示されます。

すばらしい!では、このコンテナを世界に向けて発信する方法を考えてみましょう。

## コンテナ登録

Red Hatが提供しているQuay.ioというものを紹介しましょう。これはクラウドベースでオープンソースのパブリックコンテナレジストリで、いくつかの優れた機能が組み込まれています。必要であれば自分でホストすることもできますが、この例では公開されているものを使用します。

まず、<a href="https://quay.io/" target="_blank" rel="noopener noreferrer nofollow">Quay.io</a>にアクセスし、アカウントを作成します。

では、ログインして、環境を整えましょう。


私のユーザ名は `jjasghar` です。ユーザー名をあなたのものに変更してください。素晴らしい！これでログインできました。

コンテナを作成してQuayにプッシュしたい場合は、実はとても簡単です。コマンドを見せてから説明しましょう。


ご覧の通り、先ほどと同じようにコンテナを構築しましたが、"タグ "として `-t quay.io/jjasghar/vim:latest` を追加しています。`docker`には、別のレジストリに送り、次にデフォルトのDocker Hubに送り、そして_my_namespaceに送ることを伝えます。

ビルドが終わったら、`docker push quay.io/jjasghar/vim:latest`とするだけで、ビルドが完了します。(デフォルトでは、最初のコンテナをQuay.ioにプッシュする際には、それをパブリックにしなければなりません)。

<a href="https://quay.io/repository/jjasghar/vim?tab=settings" target="_blank" rel="noopener noreferrer nofollow">`https://quay.io/repository/jjasghar/vim?tab=settings`</a>のウェブサイトをチェックして（`jjasghar`をあなたの名前空間に置き換えてください）、__Make public__をクリックします。これで、インターネットに接続できるあらゆるマシンにプルすることができます。

次に、以下のコマンドを実行して、コンテナをプルダウンしてみましょう。


成功です!これで、コンテナを作成してQuay.ioに公開する方法がわかりました。

## まとめ

ここまで一緒に見ていただきありがとうございました。一般的な `docker` コマンドや `Dockerfile` の動作方法、そして最後にコンテナレジストリの使い方を理解していただけたと思います。ご質問やご意見がありましたら、Twitterで<a href="https://twitter.com/jjasghar/" target="_blank" rel="noopener noreferrer nofollow">@jjasghar</a>までお気軽にお問い合わせください。

さて、このチュートリアルを終えて、Dockerとコンテナレジストリの使い方がわかったところで、次は何をすればいいのでしょうか？私たちの[Kubernetes learning path](/series/kubernetes-learning-path)を通過することで、コンテナやオーケストレーションに関する個人的な学習をさらに進めることができます。もしDockerをもう少し試してみたいという方は、以下のチュートリアルを試してみてください。

* [Gain access to your Docker Hub public and private repos](/tutorials/accessing-dockerhub-repos-in-iks/)
* [Create a database in a Docker container for local development](/tutorials/docker-dev-db/)