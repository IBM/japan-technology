---
abstract: Kubernetesのラーニングパスの多くは、Linuxのベースレベルの知識を前提としており、すべての人に当てはまるわけではありません。もしあなたがWindowsの世界から来たのであれば、このチュートリアルはあなたのためのものです。このチュートリアルは、Linuxの基本的な概念やコマンドを再確認するためのものであり、Kubernetesの学習パスの前提条件でもあります。
authors: ''
completed_date: '2019-03-21'
components:
- docker
- kubernetes
- istio
draft: false
excerpt: コンテナを使い始めるためのLinuxの基本的なコンセプトとコマンドを学びます。
last_updated: '2019-03-21'
meta_description: Kubernetesの学習に備えて、Linuxの基本的な概念やコマンドを学びます。
meta_keywords: linux, command-line, basics, kubernetes, docker
meta_title: KubernetesとDockerに参入するためのLinuxの前提条件
primary_tag: containers
pta:
- cloud, container, and infrastructure
pwg:
- containers
related_content:
- slug: https://developer.ibm.com/tutorials/yaml-basics-and-usage-in-kubernetes/
  type: tutorials
- slug: kubernetes-learning-path
  type: series
subtitle: Linuxの基本的なコマンドの習得と記憶の更新
tags:
- linux
title: Linuxの基礎知識。コンテナを学ぶ上での前提条件
type: tutorial
---

最新のクラウド技術を導入、管理、保守するために必要なスキルを身につけるためには、そのテーマに関する前提情報をしっかりと知っておく必要があります。Linux&reg;コマンドとコンセプトです。現代のクラウド技術の多くは、その中核にGNU/Linuxオペレーティングシステムを活用しているため、このチュートリアルでは、Linuxコマンドライン・インターフェース（CLI）のいくつかの基本を説明し、いくつかの[記事](/articles/category/containers/?fa=date%3ADESC)で作業する際にCLIを使用する準備をします。fa=date%3ADESC&fb=）や、DockerやKubernetesに関する[チュートリアル](/tutorials/category/containers/?fa=date%3ADESC&fb=)や、初心者向けの[Kubernetes Learning Path](/series/kubernetes-learning-path)を読みながら、CLIを使う準備をします。Linuxを初めて使う方は、このチュートリアルが簡単な入門編として役立つはずです。初めての方には、このチュートリアルでいくつかのコマンドのコンセプトを思い出していただき、また、新しいことを知っていただければと思います。

## ファイルとディレクトリ

最初に、標準的な GNU/Linux オペレーティングシステムの基本的なファイル構造の操作方法を説明します。標準の GNU/Linux オペレーティングシステムには、コンピュータに保存されているデータを整理するファイル管理階層があります。特定のデータが保存されている場所を特定することは、オペレーティングシステムがどのように構成されているかを理解するための最初のレッスンの一つです。ここでは、今までのLinuxの経験を無駄にしないために、「Linuxファイルシステム階層の紹介」については別の機会にします。それよりも、[File System Hierarchy](https://www.linux.org/threads/file-hierarchy-standard-fhs.9999/)について詳しく説明している記事がありますので、そちらをご覧ください。ここでは、あなたが自分の道を少しは知っていると仮定して、簡単にナビゲートするためのいくつかのヒント（あるいは、いくつかのリマインダー）を提供します。このスキルは、ファイルの編集、ファイルシステムの操作、変更、設定の確認などを求められたときに必要になります。

### cd によるディレクトリの変更

[ターミナルシェル](http://www.linuxcommand.org/lc3_lts0010.php)のカレントディレクトリから目的のディレクトリに移動するには、`cd`コマンドを使用します。このコマンドは、GNU/Linux ファイルシステムのディレクトリ構造を移動する際に非常によく使用されます。構文は以下のとおりです。


[`directory]`というパラメータは、変更したい目的のディレクトリを指し、このディレクトリへのファイルシステム階層を介した**パス**は、さまざまな方法で指定できます。

1. [絶対パス](#absolute-path)
1. [相対パス](#relative-path)
1. [チルダ展開](#tilde-expansions)
1. [特別なinode](#特別なinode)

#### 絶対パス

**絶対パス**とは、[ルートディレクトリ](https://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/the-root-directory.html)から、ファイルシステムの階層に存在する対象のディレクトリやファイルまでの「完全な経路」のことです。(一般的には `/` と表記されます)から、目的のディレクトリやファイルまでの、ファイルシステム階層内に存在する「完全な経路」です。  以下に、絶対パスを表示する簡単な例を示します。

ユーザー名が`jsmith`の場合、標準的なGNU/Linuxオペレーティングシステムでは、彼女の[ホームディレクトリ](https://www.tldp.org/LDP/Linux-Filesystem-Hierarchy/html/home.html)への絶対パスは次のようになります。


_クイックヒント：標準的なGNU/Linuxオペレーティング・システムでは、目的のディレクトリを指定せずに、コマンド・プロンプトで`cd`と入力することで、ホーム・ディレクトリに行くことができます。

上記の例では、対象となるディレクトリへのパスがかなり短くなっていますが、多くの場合、ディレクトリへのパスが非常に長くなることがあります。ここでは、以下のようなファイルシステムの階層構造を利用します。

![file_hierarchy](https://media.github.ibm.com/user/37987/files/b9750700-387e-11e9-94a0-d5a6bb78151c)

このディレクトリ構造の場合、`pacific_rose`ファイルの絶対パスは次のようになります。


#### 相対パス

GNU/Linux オペレーティングシステムの真の力は、そのコマンドラインインターフェース（CLI）にあります。Linux でタスクを実行する際には、コマンドを入力するために CLI を使用することがよくあります。必要なときに毎回コマンドラインにフルパスを入力するのは面倒ですが、ここでは相対パスがサポートしてくれます。

相対パスとは、現在の作業ディレクトリからの相対的なディレクトリ（またはファイル）へのパスのことです。上の例を見てみましょう。現在の作業ディレクトリが `/home/jsmith/grocery_store/foods/produce/` ディレクトリの場合、`fruits` ディレクトリへの移動は非常に簡単です。


現在の作業ディレクトリには `fruits` サブディレクトリが含まれているので、上記のコマンドは相対パスを使用しているために動作します。これは、`cd`コマンドで絶対パスが指定されていない場合に、オペレーティングシステムが行う「仮定」と言ってもよいでしょう。これで、`fruits`ディレクトリに移動したので、`pwd`コマンドでこのディレクトリのフルパスを確認することができます。


`pwd` (print working directory) コマンドは，現在の作業ディレクトリを表示するのに便利ですが，これはしばしば絶対パス形式で表示されます。このように，絶対パスと相対パスを使ってファイルシステムの階層を移動することができます。

#### チルダの拡張子

**Bashシェル**を搭載した標準的なGNU/Linuxオペレーティングシステムでは、ファイル階層のナビゲーションをより簡単にするために、[チルダ拡張](https://www.gnu.org/software/bash/manual/html_node/Tilde-Expansion.html)が用意されています。チルダ拡張とは何かを説明するために、この例を見てみましょう。


上のコマンドのチルダ `~` は，`$HOME` [環境変数](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html#sect_03_02_01)の値に対応しており，通常は現在のユーザのホームディレクトリに設定されています。つまり，この変数の値は，現在ログインしているユーザに応じて変化します。  同じシステム上で、ジェーン・スミスが`cd ~`コマンドを実行すると、`/home/jsmith`ディレクトリに移動しますが、マーク・ジョーンズ（ユーザー名`mjones`でログインしている）が同じコマンドを実行すると、`/home/mjones`ディレクトリに移動します。

ここでは、チルダを使った拡張機能の例をいくつか紹介します。

* `~` - $HOME ディレクトリにマップされます。
* `~/grocery_store` - $HOME ディレクトリに存在する `grocery_store` サブディレクトリです。
* `~mjones/grocery_store` - `mjones` ユーザーの $HOME ディレクトリに _special_ 存在する `grocery_store` サブディレクトリです。

#### 特別なinode

一段と深く掘り下げるために、_inodes_について簡単に説明します。[Ian D. Allen](http://teaching.idallen.com/dat2330/04f/notes/links_and_inodes.html)の定義によると、_「Unixでは、ディレクトリやファイルの内容を構成するデータの集まりは名前ではなく、inodeと呼ばれるデータ構造の一部として格納されています」_要するに、ディレクトリやファイルはinode番号に対応する名前であり、ファイルシステムの階層を移動するために使用できる「特別なinode」がいくつか存在しています。以下にその例を示します。

`...`（ダブルドット）のinodeは、ファイルシステム階層の**親ディレクトリ**（1つ上のレベル）に変更するために使用できます。


また，`..`（ダブルドット）のinodeを連結することで，ファイルシステムの階層を複数のレベルで移動することができます。


ここでは、ファイルシステムの階層を`fruits`ディレクトリから`foods`ディレクトリ（2階層上）に移動しています。

また，`-`（ダッシュ）で前の作業ディレクトリに移動することができます。


あるディレクトリから別のディレクトリに移動してから戻る必要がある場合、`-`（ダッシュ）を使うと、現在作業しているファイルシステムの階層に関係なく、前の作業ディレクトリに戻ることができます。

### pushd/popd によるディレクトリの変更

ここで、Linux ユーザーがファイルシステム階層を移動するための第 2 の手段として、`pushd`、`popd`、`dirs`コマンドがあります。これら3つのシェルビルトインを併用することで、最近訪れたディレクトリのリストである[directory stack](https://www.gnu.org/software/bash/manual/html_node/The-Directory-Stack.html#The-Directory-Stack)を操作することができます。この最近訪問したディレクトリのリストを保存するために使用されるデータ構造は、まさにスタックまたはLIFO (Last in, First out)データ構造です。`pushd` はカレントディレクトリを対象となるディレクトリに変更し、この新しいディレクトリをスタックに追加し、`popd` はスタックの一番上にリストされているディレクトリを削除してから、スタックの一番上にあるディレクトリにディレクトリを変更します。

私の個人的な経験では、`pushd`と`popd`コマンドは、訪問したディレクトリの「パンくずリスト」を作成する方法として、自動化スクリプトで最もよく目にするものです。このリストを利用できるようにしておくと、自動化されたタスクで、特定の方法や順序でファイル（およびディレクトリ）に変更を加える必要がある場合に役立ちます。以前に訪れたディレクトリをスタックから "ポップ "して、簡単に再訪することができます。

`dirs`コマンドは、私が利用したことのあるコマンドではありませんが、とても便利なコマンドです。このコマンドを使うと、ディレクトリスタック自体を表示して、最近訪れたディレクトリのリストを見ることができます。また、このコマンドにはいくつかのオプションがあり、必要に応じてスタックを「管理」することができます。ここでは、`pushd`、`popd`、`dirs`の各コマンドを使った例を紹介します。

`home/jsmith/grocery_store/foods/`から出発して、`pushd`を使って`produce`ディレクトリに変更してみます。


現在のカレントディレクトリは `/home/jsmith/grocery_store/foods/produce` ディレクトリで、`pushd` を使ってこのディレクトリに移動したので、`dirs` コマンドで示すように、ディレクトリスタックに追加されています。


ディレクトリのリストは、左から右へ、最近訪れた順に並んでいることに注意してください。もう一度 `pushd` を使って `meats` ディレクトリに移動してから、ディレクトリスタックをもう一度見てみましょう。


これで、ディレクトリリストは、最近訪れたディレクトリが3つに増えました。ここで、`popd`コマンドを使用すると、ディレクトリスタックの一番上にリストされていたディレクトリが削除され、カレントディレクトリは`/home/jsmith/grocery_store/foods/produce`に戻ります。


また、ディレクトリスタックを見ると、最近アクセスしたディレクトリが2つに減っていることがわかります。


`pushd`, `popd`, `dirs` コマンドで使用できるオプションの一覧については， GNU.org Bash マニュアルの [Directory Stack Builtins](https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html#Directory-Stack-Builtins) の章を参照してください．

この先の記事やチュートリアルでは、ディレクトリ構造を簡単にナビゲートすることは、確かに便利なスキルになります。

### ディレクトリの作成

ナビゲーションについて説明しましたが、次にディレクトリの作成について簡単に説明します。


この例では，`[target]` は，作成したいディレクトリの名前です。実行すると，`mkdir`は，（フルパスが指定されていないので）現在の作業ディレクトリにこのディレクトリを作成します。また，フルパスが特定でき，ユーザアカウントに権限があれば，ファイルシステム階層のどのレベルにも新しいディレクトリを作成することができます。例えば、以下のようになります。


これにより、`home/jsmith/grocery_store/foods/produce`ディレクトリの中に`veggies`ディレクトリが作成されます。ファイルシステムの階層の同じレベルに複数のディレクトリを作成する必要がある場合がよくあります。また、まったく新しいディレクトリ構造を作成しなければならない場合もあります。このような場合には、`-p`コマンドオプションが非常に便利です。より高度な例を挙げてみましょう。


この例では、いくつかのコンセプトがあります。まず、`-p`オプションでは、パスに含まれるディレクトリが以前に作成されていてもいなくても、指定された「パス」を作成することができます。括弧を使うことで、複数のディレクトリを同時に作成することができます。ここでは、`meats`ディレクトリ（事前に作成していない）の中に、`beef`、`fish`、`chicken`、`pork`のサブディレクトリを作成しています。さらに、`pork`ディレクトリの下に、`bacon`と`sausage`の2つのサブディレクトリを作成しています。  このように、たった1つのコマンドで全く新しいディレクトリ構造を作ることができるという、コマンドラインの力を実感していただけると思います。

`mkdir`コマンドの詳細については、[mkdirを使ってディレクトリを作成する方法に関するlifewireの記事](https://www.lifewire.com/create-directories-linux-mkdir-command-3991847)を参照してください。

### ファイルとディレクトリの表示

ここまでは、標準的な GNU/Linux オペレーティングシステムでのディレクトリの移動と作成の方法を説明しました。ここでは、ディレクトリの一覧表示、ファイルの表示、編集について説明します。GUI ベースのアプリケーション以外にも、CLI から直接ファイルやディレクトリを表示する方法がいくつかあります。

#### lsでディレクトリの内容を見る

ディレクトリの内容を表示するには、さまざまな方法で`ls`コマンドを使用できます。コマンドプロンプトでの単純な`ls`は、現在の作業ディレクトリの内容を（水平方向に）表示します。


よく使われるコマンドオプションもいくつかあります。たとえば，コマンドに`-l`フラグを追加すると，対象となるディレクトリの内容（ファイル/ディレクトリ名，パーミッション，所有者，修正日，ファイル/ディレクトリサイズなど）が表示されます。


`a`オプションは、[hidden files](https://www.ghacks.net/2009/04/16/linux-tips-view-hidden-files/)を含むディレクトリの内容を表示します。[hidden files]とは、主にデスクトップのカスタマイズやパーソナライズ、アプリケーションの設定などに使用されるファイルです。


**lsの既知のコマンドオプション**。

これまでに説明してきた`ls`コマンドのオプションは、最も広く使われているものです。しかし、同じように便利なオプションが他にもいくつかあります。以下に簡単なリストを示します。

| ls commmand｜ Description｜説明
|-------------|-------------|
| `ls -lh` | `-l` と `-h` を組み合わせることで、ファイルやディレクトリのサイズを「人間が読める」形式で表示することができます。|
| `ls -F` | 出力にリストアップされたサブディレクトリに `/` を追加します。
| `ls -R` | サブディレクトリの内容を再帰的にリストアップします。
| `ls -r` | 出力を逆順に表示します。
| `ls -lS` | 出力をファイルサイズ順に表示し、最大のファイルを_最初に表示します。
| `ls -ltr`| `-l`, `-t`, `-r` オプションを組み合わせると、修正日順に出力を表示し、最新のものを_last_に表示します。


#### cat でファイルを表示する

ファイルの内容を見るための最もシンプルなコマンドの一つが `cat` コマンドです。`cat`は、_"concatatenate"_の略で、ファイルの内容を見るだけでなく、出力をリダイレクトしてファイルを作成するのにも使われます。


ここでは、`pacific_rose`ファイルに「This is a test file.」というテキストが含まれています。`cat` はこのファイルの内容をターミナルウィンドウに直接表示するので、中身を見るには手っ取り早い方法です。

[リダイレクト演算子](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection)と組み合わせることで、`cat`を使ってファイルを作成することもできます。


上のコマンドは，現在の作業ディレクトリの中に，`granny_smith`という名前の新しいファイルを作成します。


前述のとおり、`cat`は_"concatenate"_の略で、上の例では、`>`リダイレクト演算子を使って、複数のファイルの内容を1つのファイルにまとめる方法を示しています。

また、`cat`コマンドと一緒に使うと便利なコマンドフラグ（またはオプション）の一覧を以下に示します。

* `cat -n` は、ファイル出力の横に行番号を表示します。
* `cat -e` は、ファイル出力の中に、行末や行間スペース（通常は `$` 文字を使用）を表示します。
* `cat -T` は、タブ区切りの行をファイルの出力に表示します。

`cat`コマンドの詳しい使い方については、こちらの[LINFO article on the cat command](http://www.linfo.org/cat.html)をご覧ください。

#### ファイルをmore/lessで表示する

ターミナルで直接ファイルを表示するには、`more`と`less`コマンドを使う方法があります。`more`と`less`の両方とも、ファイルの内容を見ることができ、ファイルの出力が画面のバッファを満たすと一時停止します。ここで一時停止するか、いずれかのキーを押して残りの出力を見て続行するかを選択できます。しかし、`less`コマンドは少し違います。`more`コマンドと同じ機能でファイルを見ることができますが、`less`では、出力を_backwards_（後方）に移動することができます（`more`コマンドでは出力を前方にしか見ることができません）。

#### 端末用テキストエディタ (vim/emacs/pico)

Linux を使った学習では、設定ファイルの作成、更新、削除などを行う必要があります。これらの作業は、ほとんどの Linux オペレーティングシステムに搭載されているテキストエディタを使用して行うことができます。以下のようなものがあります。

* vi/vim
* emacs
* pico

それぞれのエディタには、独自の長所、短所、機能があります。どれか一つのエディタを推奨するのではなく、それぞれのエディタのヒントやコツを教えてくれるリソースの短いリストを紹介します。

**vi/vim:**。
* [Learn vim For the Last Time: Tutorial and Primer](https://danielmiessler.com/study/vim/)

**emacs**.
* [Absolute Beginners Guide to emacs](http://www.jesshamrick.com/2012/09/10/absolute-beginners-guide-to-emacs/)

**pico** （ピコ
* [Basic Pico Commands](https://www.cs.colostate.edu/helpdocs/pico.html)

### ファイルのパーミッション

[学習パス](/series/kubernetes-learning-path/)で学習を進めていくと、ファイルのパーミッションについて理解する必要が出てきます。Linuxユーザーとして、Linuxオペレーティングシステム上に保存されているファイルに対して、ユーザーとして何ができるかを細かく制御することができます。多くの場合、ファイルやディレクトリが機能するためには、特定のレベルのパーミッションが設定されていることが求められます（例えば、スクリプトを実行可能にするなど）。ここでは、ファイルのパーミッションについて簡単に説明します。


このディレクトリ一覧のサンプルでは、ディレクトリに含まれる各ファイルのパーミッションを`-rw-r--`で表しています。ファイルやディレクトリのパーミッションは，user，group，others（all other）の3つのアカウントロールに対して設定されます。与えることのできる権限は、読み取り（r）、書き込み（w）、実行（x）です。各ファイルにアクセスするアカウントやグループに応じて、パーミッションがどのように適用されるかを、以下の表で説明しています。

「brisket.txt」というファイルのパーミッションを左から右に読むと（最初の`-`を省略すると）、ファイルのパーミッションは以下のようになります。

| ユーザー | グループ | その他
|------|-------|--------|
| rw (read/write) | r (read) | r (read) |

ファイルやディレクトリへのフルアクセス権限は，`rwx`と表記されます。この例では，ユーザ `jdoe` には読み取りと書き込みのパーミッションが，`staff` グループには読み取りのパーミッションが，その他のすべての人には読み取りのパーミッションが与えられています。  UGO（ユーザー、グループ、その他）の概念を理解するには、こちらの[Linuxのファイルパーミッションを知るための記事](https://www.linux.com/learn/getting-know-linux-file-permissions)に目を通しておくと、より深く理解できると思います。

#### chmodによるパーミッションの変更

ファイルに適用されているパーミッションを変更する必要がある場合があります。ここで活躍するのが`chmod`コマンドです。前述したように、パーミッションを変更することで、bashスクリプトを実行可能にすることができます（つまり、コマンドラインでスクリプト自体を呼び出すことで「実行」できるようになります）。

上の例では、`script_to_run.sh` にユーザーの `+x` 属性が追加されています。  これは、このスクリプトが `jdoe` ユーザーによって "実行可能" になったことを意味します。


上の例では、`u`（ユーザー）と`g`（グループ）の両方を使って`chmod`コマンドを実行していますが、これは、アカウントの役割を組み合わせて、ファイルのパーミッションを並行して変更することもできることを示しています。また，`+`文字は実行可能属性を付加し，反対に`-`文字はそれを除去します。

ご覧のように、`chmod`は必要に応じてファイルのパーミッションを微調整するのにとても便利なコマンドです。

## Dockerの基本コマンド

ここでは、標準的なGNU/Linuxオペレーティングシステムを使用しながら、ファイルシステムのナビゲーション、ファイルやディレクトリの表示と作成、ターミナルシェルのカスタマイズを始めるためのコマンドラインの例を一通り説明しました。しかし、このチュートリアルは、より高度なDocker、Kubernetes、Istioのチュートリアルやコードパターンを掘り下げるための入門編としての意味合いが強いので、まずは簡単にいくつかのDockerコマンドを列挙してみましょう。

### Dockerイメージの構築

| コマンド | 説明 |
|---------|-------------|
| `docker images` | ローカルに保存されているイメージを一覧表示します。
| `docker rmi [IMG]` | ローカルイメージリポジトリから `[IMG]` イメージを削除します |
| `docker build -t [TAG] .` | 現在の作業ディレクトリにあるDockerfileからDockerイメージをビルドし、`[TAG]`というタグをつける |

### Docker イメージの実行

| コマンド | 説明 |
|---------|-------------|
| `docker run --name [CNT]` | コンテナを実行し、`[CNT]`という名前を付けます。
| `docker run -it` | コンテナのターミナルセッションにアタッチします。
| `docker rm -f $(docker ps -aq)` | すべてのコンテナを削除する |
| `docker ps` | 実行中のコンテナをリストアップする |

### Docker イメージの出荷

| コマンド | 説明 |
|---------|-------------|
| `docker pull` | コンテナレジストリからイメージをプルする |
| `docker push [IMG]` | [IMG]という名前のイメージをレジストリにプッシュする |

## Kubernetesの基本コマンド

さて、ここまでDockerの基本的なコマンドをいくつか紹介してきましたが、ここからはKubernetesの便利なコマンドを紹介します。Kubernetesでは、Kubernetesクラスタに対してコマンドを実行するためのコマンドラインインターフェイスツールである`kubectl`を採用しています。以下では、Kubernetesのデプロイメントを更新したり、データを抽出したりするために頻繁に使用されるコマンドの短いリストを紹介します。

### Kubernetesリソースのリストアップ

| コマンド | 説明 |
|---------|-------------|
| `kubectl get services` | 現在の名前空間内のすべての kubernetes サービスを一覧表示します。
| `kubectl get pods --all-namespaces` | _all_ 名前空間内のすべてのポッドをリストアップする。
| `kubectl get pods -o wide` | 現在のネームスペースから、より詳細なポッドの出力を生成する |
| `kubectl describe nodes [node-name]` | ノード `[node-name]` についての簡単な説明を表示します。
| `kubectl describe pods [pod-name]` | ポッド `[pod-name]` の簡単な説明を表示します。

### Kubernetesのリソースを操作する

| コマンド | 説明 |
|---------|-------------|
| `kubectl create deployment foo --image=foo` | `foo` のインスタンスを 1 つデプロイします。
| `kubectl create -f ./local-manifest.yaml` | `local-manifest.yaml` という名前のKubernetesマニフェストファイルを介してリソースを作成します。
| `kubectl delete -f ./bar.json` | `bar.json` という名前のファイルで定義されているポッドを削除します。
| `kubectl delete pod,service silver gold` | `silver` と `gold` という名前のすべてのポッドとサービスを削除します。

`kubectl`コマンドの一覧については、https://kubernetes.io/docs/reference/kubectl/cheatsheet/。

## まとめ

このチュートリアルは、[Docker](https://www.docker.com/)、[Kubernetes](https://kubernetes.io/)、[Istio](https://istio.io/)などのコンテナ技術について学び続ける際の「氷を割る」ような、コマンドラインのウォーミングアップとしての役割を果たすことを目的としています。新しい技術を習得する前に基本を再確認することは有意義なことです。このチュートリアルで取り上げたトピックが、皆さんの記憶を呼び覚ましたり、何か新しいことを習得するのに役立つことを願っています。

## 次のステップ

このチュートリアルを終えたら、[Kubernetes Learning Path](/series/kubernetes-learning-path/)の次のステップを確認してください。また、コンテナを使ってみたいと思ったら、以下のリソースやコードパターンもチェックしてみてください。

* [Start creating Kubernetes clusters](https://cloud.ibm.com/docs/containers?topic=containers-cs_cluster_tutorial#cs_cluster_tutorial)
* 大規模なマイクロサービスを接続、管理、保護する。[Run Istio on the IBM Cloud Kubernetes Service](https://www.ibm.com/jp-ja/cloud/info/istio)。
* [Manage Docker container images in a fully managed private registry](https://cloud.ibm.com/kubernetes/catalog/registry?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)
* Code pattern:[ Using Istio across private and public clusters](/patterns/istio-for-multi-clusters-across-iks-and-icp/)
* Code pattern:[Run a Drupal website on Kubernetes](/patterns/run-drupal-website-on-kubernetes/)