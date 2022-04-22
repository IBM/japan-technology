# パート 1：IBM i用統合Webサービス・サーバーを使用したRESTサービスの構築

### 基礎知識の習得

English Version: https://developer.ibm.com/tutorials/i-rest-web-services-server1/

###### 最新の英語版コンテンツは上記URLを参照してください。

###　Author: Nadir Amra
last_updated: 2015-05-08


## はじめに

ここに進化し続ける新しいアプリケーション・スタイルがあります。それをドライブする力は多岐にわたりながらも収束しつつあります。モバイルとソーシャル・アプリケーションが急速に浸透することで、電子的な手段による人同士の関わり方が促進されています。クラウド、モバイル、およびソーシャルは、APIセントリックやBusiness-as-a-Serviceエコノミーの急激な成長を促しました。これらの分野では、消費しやすいAPIを提供することで、データが重要な価値を持ち、収益化することができます。

通常、API（あるいはWebサービス）はSOAPまたはRESTベースのWebサービスです。RESTはSOAPに替わる簡便な手段としてWebの世界で広く受け入れられています。RESTベースのWebサービスを選択する重要なポイントは、そのシンプルさと浸透度合いです：

* 重要なのは、コンテンツの配信を達成可能な最もシンプルな方法で行うことです
* HTTPはどこでも利用可能で、あたかも私たちの周りの空気のような存在です

数年前から、ILEプログラムとサービス・プログラムを、SOAPプロトコル・ベースのWebサービスとしてデプロイすることが可能でした。それはオペレーティング・システムの一部である統合Webサービス・サーバーを使用したものです。この記事が公開されるまで、統合Webサービス・サーバーはRESTサービスをサポートしていませんでした。

この記事は、統合Webサービス・サーバーにおけるRESTサポートに関するシリーズの最初のパートです。このパートでは、REST Webサービスの基本概念と、統合Webサービス・サーバーがRESTサービスをサポートする方法を説明します。本シリーズの残りのパートは、この基本概念を土台にしています。

* [パート 2](../../Tutorials/i-rest-web-services-server2/)は、簡単なIELアプリケーションをRESTful Webサービスとしてデプロイするための手順を説明します。
* [パート 3](../../Tutorials/i-rest-web-services-server3/)は、より多くのREST機能を使う複雑なILEアプリケーションをデプロイするための手順を説明します。

## 前提条件

### ソフトウェア

統合Webサービス・サーバーにおけるRESTサポートに必要なすべてのPTFを取得するためには、最新のグループPTFをロードする必要があります。表1はIBM iオペレーティング・システムのサポートされる各リリースに必要なHTTPグループPTFです。

 **表 1. ソフトウェア前提条件**
 <table border="0" cellpadding="0" cellspacing="0" class="ibm-data-table" data-widget="datatable" summary=""> <thead> <tr> <th class="ibm-background-neutral-white-30"> IBM i リリース </th> <th class="ibm-background-neutral-white-30"> HTTPグループPTF </th></tr></thead> <tbody> <tr> <td style="vertical-align:top"> IBM i 7.2 </td> <td style="vertical-align:top"> SF99713 （level 6以降） </td></tr> <tr> <td style="vertical-align:top"> IBM i 7.1 </td> <td style="vertical-align:top"> SF99368 （level 32以降） </td></tr></tbody></table>

### 前提知識

この記事を読む前に、RESTの原則に関する基本を理解をしてください。

IBM DeveloperにはRESTに関する豊富な情報があります。仮に1つの記事を選択するならば、[_RESTful Web services: The basics_](https://developer.ibm.com/articles/ws-restful/)がお勧めです。[参考情報](#_Resources)セクションには、RESTに関するたくさんの情報があります。また、JavaScript Object Notation（JSON）とXMLに関する基本的なコンセプトを理解しておいてください。

## RESTful Webサービスの基礎

要約すると、RESTはアーキテクチャ上の原則の集まりを定めたものです。これによって、システムのリソースに重点を置いたWebサービスを設計することができます。この設計には、さまざまな言語で書かれた幅広いクライアントが、リソース状態の把握方法とHTTPを通した転送方法の決定を含みます。

最も純粋な様式として、RESTのWebサービス実装は3つの基本的な設計原則に従います：

* 明示的にHTTPメソッドを使い分ける。
  * サーバー上にリソースを作成する場合は、POSTを使用する。
  * リソースを取得する場合は、GETを使用する。
  * リソースの状態を変えたり更新する場合は、PUTを使用する。
  * リソースを取り除いたり削除する場合は、DELETEを使用する。
* ステートレスにする。
* ディレクトリー構造を模したURI（Uniform Resource Identifiers）を公開する。
  * 名詞を用いる。動詞は使わない (`/accounts/{id}`を使うが、`/getaccount?id=nn`は使わない)
  * リクエストの内容を推測可能にする
  * よく使われているAPIを参考にする（Google、Facebook、Twitterなど）

実例を見れば、これらの点が明確になります。ソフトウェア障害管理アプリケーションで、アプリケーション・データベース内のデータ再利用や操作を行うことを考えます。URLエンドポイント（仮に `/defects` とします）を外部に公開し、開発者が種々のHTTPメソッドとコンテンツでこのエンドポイントにアクセスします。HTTPメソッドとコンテンツに基づいて、リクエストする操作を推測し、データに対する適切なアクションを行うことができます。以下はいくつかの例です：

* `GET /defects`：全ての障害をリストする。
* `GET /defects/123`：障害番号123を取得する。
* `POST /defects/123`：POSTリクエストの本体にある情報で新しい障害番号123を作成する。
* `PUT /defects/123`：PUTリクエストの本体にある情報で障害番号123を更新する。
* `DELETE /defects/123`：障害番号123を削除する。

## 統合WebサービスにおけるRESTサポートの基礎

ここまでで、RESTfulサービスに関する基本的な理解ができました。ここで、いくつかの新しい用語と、それがRESTful Webサービスのデプロイ時にどのように使われるかを説明します。RESTfulサービスをデプロイする際に、このセクションで説明するコンセプトが必要になるでしょう。

### ルート・リソース

統合Webサービス・サーバーでは、 _ルート・リソース_ はILEプログラム・オブジェクト（つまりILEプログラムあるいはサービス・プログラム）であり、それをRESTful Webサービスとしてデプロイします。

### リソース・メソッド

_リソース・メソッド_ はルート・リソースでのメソッドで、HTTPメソッドにバインドされます。統合Webサービス・サーバーでは、リソース・メソッドはILEプログラムのエントリー・ポイント、あるいはエクスポートされたILEサービス・プログラムのプロシージャーに対応します。

統合Webサービス・サーバーがリソース・メソッドと紐づけることができるのは、以下のHTTPメソッドです： GET, PUT, POST and DELETE.

リソース・メソッドとHTTPメソッドのバインド以外に、リソース・メソッドがクライアントから受け付けるコンテンツ・タイプを指定する必要があります。統合Webサービスは `*`ALL（"`*`/`*`"のコンテンツ・タイプ）、`*`XML（"`application/xml`"のコンテンツ・タイプ）、`*`JSON（"`application/json`"のコンテンツ・タイプ）、そして `*`XML_AND_JSON（"`application/xml,application/json`"のコンテンツ・タイプ）をサポートします。

クライアントからのリクエストが来ても、HTTPメソッドを処理するリソース・メソッドが無いために対応できない、あるいはHTTPリクエストのコンテンツ・タイプがリソース・メソッドによってコンシュームできない場合、エラーHTTPステータス・コードをクライアントに返します。

また、リソース・メソッドが生成するデータのコンテンツ・タイプも指定しなければなりません。可能な値は、`*`XML、`*`JSON、および `*`XML_AND_JSONです。リソース・メソッドがどのようにXMLとJSONを生成するのか、疑問に思うかもしれません。 `*`XML_AND_JSONを指定した場合、レスポンスのコンテンツ・タイプは、クライアントがHTTPコンテンツ・ネゴシエーションを通じて指定するタイプに依存します（HTTPコンテンツ・ネゴシエーションについては、<a href="#_Resources">参考情報</a> のセクションを参照してください）。クラアントが受け付けないコンテンツ・タイプをリソース・メソッドに指定すると、クライアントはエラーのHTTPレスポンス・コードを受け取ります。

### リソース・メソッドの入力パラメーター

各リソース・メソッドにおいて、以下の点を決めなければなりません：

* 入力パラメーターのラップあるいはアンラップ。
* 入力パラメーターをアンラップする場合、入力ソースからパラメーターに値をインジェクトするかどうか。

ILEプログラム・オブジェクトをデプロイする際に、どのパラメーターが入力パラメーターで、どれが出力パラメーターになるかを指定できます。パラメーターのデータ型によっては、入力パラメーターをラップする、あるいはアンラップすることを決める必要があります。

入力パラメーターをラップするように指定すると、全てのパラメーターは構造体でカプセル化されます。このため、統合Webサービス・サーバーのRESTサービスに対するHTTPリクエストは、リクエストの中にペイロードを含む必要があります。そして、リクエストのコンテンツ・タイプはXML（`application/xml`のコンテンツ・タイプ）あるいはJSON（`application/json`のコンテンツ・タイプ）でなければなりません。コンテンツ・タイプがJSONあるいはXMLでなければ、クライアントはエラーHTTPレスポンスを受信します。

パラメーターをアンラップするように指定すると、入力パラメーターは構造体でラップされません。また、サポートする全プリミティブ・パラメーター（`char`、`int`、`float`、`packed`、`zoned`、および`byte`型のパラメーター）に、以下のいずれかの入力ソースから値をインジェクトしなければなりません：

* URIパス・テンプレート内の変数（詳細は後述）
* 変数から（`<input type="text" name="lastname">`）
* 照会ストリング変数変数（`/cars/new?`**`color`**`=blue`）
* マトリックス・パラメーター（`/cars;`**`color`**`=blue/new`）
* HTTPヘッダー
* HTTP Cookie変数

以下の条件ではパラメーターをアンラップできません：

* 構造体パラメーターが複数ある。
* パラメーター・リストに配列がある。
* パラメーター型がプリミティブであるが、アンラップの対象ではない。

### リソース・メソッド出力パラメーター

全ての出力パラメーターは構造体でラップされます。これに対する例外は、出力パラメーターとして、HTTPヘッダーまたはHTTPレスポンス・コード（この場合はステータス・コード）を含むものを指定した場合です。

統合WebサービスにおけるRESTサポートでは、文字型（`char`）配列の出力パラメーターを、HTTPヘッダーを含むパラメーターとして指定できます。このHTTPヘッダーは、（メッセージ本体では無く）レスポンスのHTTPヘッダーとしてクライアントに返されます。配列内の各要素は以下の形式になります：

<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;&lpar;less-thanheader&#8209;name&lpar;greater-than: &lpar;less-thanheader&#8209;value&lpar;greater-than&lpar;newline&rpar;</pre></code-listing>

RESTでのHTTPヘッダーをセットする使用例として、HTTPキャッシングに関するHTTPヘッダーのセットがあります。

統合WebサービスにおけるRESTサポートでは、整数型（`int`）出力パラメーターを、クライアントに返すHTTPレスポンス・コードを持つパラメーターに指定できます。HTTPヘッダー同様、パラメーターはメッセージ本体内では返されません。

ステータス・コードに従って、以下のアクションを行います：

* ステータス・コードのカテゴリーが _成功_（200番台）または _リダイレクト_（300番台）、およびステータス・コードが204（no content）以外の場合、メッセージ本体の処理を行い、クライアントに返します。
* ステータス・コードのカテゴリーが _クライアント・エラー_（400番台）、_サーバー・エラー_（500番台）、またはステータス・コードが204の場合、クライアントにメッセージ本体を返しません。

サポートするステータス・コードを表2に示します。認識できないステータス・コードの場合、クライアントは500（internal server error）ステータス・コードを受け取ります。

 **表 2. サポートされるHTTPステータス・コード**
 <table border="0" cellpadding="0" cellspacing="0" class="ibm-data-table" data-widget="datatable" summary=""><thead> <tr> <th class="ibm-background-neutral-white-30"></th></tr></thead> <tbody> <tr> <td style="vertical-align:top"> 200 OK </td> <td style="vertical-align:top"> 307 Temporary Redirect </td> <td style="vertical-align:top"> 410 Gone </td></tr> <tr> <td style="vertical-align:top"> 201 Created </td> <td style="vertical-align:top"> 400 Bad Request </td> <td style="vertical-align:top"> 412 Precondition Failed </td></tr> <tr> <td style="vertical-align:top"> 202 Accepted </td> <td style="vertical-align:top"> 401 Unauthorized </td> <td style="vertical-align:top"> 415 Unsupported Media Type </td></tr> <tr> <td style="vertical-align:top"> 204 No Content </td> <td style="vertical-align:top"> 403 Forbidden </td> <td style="vertical-align:top"> 500 Internal Server Error </td></tr> <tr> <td style="vertical-align:top"> 301 Moved Permanently </td> <td style="vertical-align:top"> 404 Not Found </td> <td style="vertical-align:top"> 503 Service Unavailable </td></tr> <tr> <td style="vertical-align:top"> 303 See Other </td> <td style="vertical-align:top"> 406 Not Acceptable </td> <td style="vertical-align:top"></td></tr> <tr> <td style="vertical-align:top"> 304 Not Modified </td> <td style="vertical-align:top"> 409 Conflict </td> <td style="vertical-align:top"></td></tr></tbody></table>

## REST URLとURIパス・テンプレート

URLはリソースの場所を指定するために使用されます。サーバー・クライアント間のやり取りは、URLに対するHTTP操作の発行が基本となります。URLパターンを定義することは重要です。クライアントがリソースを特定した後、かなり時間が経過してからそのリソースを直接アドレスすることがあるので、URLの存在期間が長くなるからです。

Webサービス・エンジンは、入力のURLに基づいて、ルート・リソースにHTTPリクエストを送ります。URLの形式は以下のとおりです：

<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;&lpar;http&rpar;&lpar;less-thanhost&lpar;greater-than:&lpar;less-thanport&lpar;greater-than/&lpar;less-thancontext&#8209;root&lpar;greater-than/&lpar;less-thanroot&#8209;resource&lpar;greater-than/&lpar;less-thanuri&#8209;path&#8209;template&lpar;greater-than </pre></code-listing>

統合Webサービス・サーバーを構築すると、統合Webサービス・サーバーでデプロイしたサービスのデフォルトのコンテキスト・ルートは `/web/services` になります。サーバーのコンテキスト・ルートは、サーバーのプロパティを修正することで変更できます。

ルート・リソースは、RESTful Webアプリケーション用に選択する名前です。

_URIパス・テンプレート_ はURIの一部であり、リクエストをどのようにリソースとリソース・メソッドにマップするかを明確化します。URIパス・テンプレートは、URI構文に埋め込まれた変数を含むことができます。これらの変数は実行時に代入され、代入されたURIを基にしてリソースがリクエストに応答します。変数は中括弧（`{` と `}`）で表記されます。例えば、URIパス・テンプレート `/defects/{id}` をルート・リソースに関連づけた場合、`/defects/123` のURIを含むHTTPリクエストは、URIパス・テンプレートにマッチし、リクエストをリソースに転送します。

デフォルトでは、URI変数は正規表現"`[^/]+?`"（最初のスラッシュまでの1つ以上の文字）にマッチしなければなりません。変数名の後ろに異なる正規表現を指定することで、正規表現をカスタマイズすることができます。例えば、`id` を数値にしたいなら、変数定義におけるデフォルトの正規表現をオーバーライドして、次のように指定できます： `/defects/{id: \d+}`。クライアントが送ったURLのパスの最後のセグメントに数字以外の文字が入っていると、エラーHTTPステータス・コードをクライアントに返します。正規表現に関する詳しい情報は、<a href="#_Resources">参考情報</a> セクションのJava regular expressionsを参照してください。

上述のように、URIパス・テンプレートはルート・リソースのレベルで指定できます。また、URIパス・テンプレートはリソース・メソッドに対しても指定できます。このようなメソッドを通常サブリソース・メソッドと呼びます。これによって、複数のリソース・メソッドを判別でき、たくさんのルート・デバイスを作る（つまり、たくさんのRESTfulサービスをデプロイする）ことなく、共通する部分をグループ化できます。例えば、CONVERTTEMPというILEサービス・プログラムと、その中に2つのプロシージャーFTOCとCTOFがあると仮定します。URIパス・テンプレート"/`ctof`"をCTOFに関連づけると、`/CONVERTTEMP` へのHTTPリクエストはプロシージャーFTOCにマップされますが、`/CONVERTTEMP/ctof` はプロシージャーCTOFにマップされます。

## 構造化されたメッセージの形式

 <sidebar>ID生成<br/><br/><p>XMLエレメント名やJSONフィールド名のためのIDは、プロシージャー名、構造体名、および構造体中フィールド名に基づいて生成されます。最初の2文字が大文字でない限り、IDの最初の大文字は小文字に変換されます。最初の2文字が大文字の場合は、そのままIDとして使用されます。</p> <p>新しいRPG拡張がIBM i リリース7.1と7.2用にリリースされ、パラメーター名のIDの大/小文字の制御ができます。</p></sidebar>

クライアント・リクエストを正しく行うために、XMLやJSONのメッセージ本体形式を知りたいかもしれません。SOAPと異なり、現時点では（まさに着手をしている最中ですが）、メッセージ形式を説明する文書はありません。しかし、統合WebサービスにおけるRESTサポートがどのように入力と出力パラメーターを扱っているかを理解すれば、XMLやJSONメッセー形式を推測することができるはずです。

以下の説明では、CONVERTTEMPと呼ばれるプロシージャーをエクスポートし、それには文字型（`char`）のTEMPINという入力パラメーターがあると仮定します。また、文字型（`char`）のTEMPOUTという出力パラメーターがあります。

### XMLメッセージ形式

1つの入力パラメーターだけがXMLのメッセージ・コンテンツを受け取ることができ、それは構造体でなければなりません。

入力パラメーターがXML形式のメッセージ本体を受け取るとき、クライアントが送るべきXML文書形式は、入力パラメーターのラップあるいはアンラップに依存しています。

CONVERTTEMPプロシージャーで、パラメーターのアンラップを選択すると、リソース・メソッドはプリミティブ型の入力パラメーターをとります。したがってXML文書を入力としては受け付けません。また、入力パラメーターのラップを選択すると、CONVERTTEMPInputという名前のラッパー構造体が生成され、そこに全ての入力パラメーターが含まれます。このケースでは1個のみでTEMPINです。これにより、クライアントが送信する必要のあるXML文書はリスト1で示されるような形式になります。

**リスト 1. 入力 XML形式サンプル – ラップ指定**
<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;&lpar;less-thanCONVERTTEMPInput&lpar;greater-than &lpar;newline&rpar;    &lpar;less-thanTEMPIN&lpar;greater-than23&lpar;less-than/TEMPIN&lpar;greater-than&lpar;newline&rpar;&lpar;less-than/CONVERTTEMPInput&lpar;greater-than &lpar;newline&rpar;</pre></code-listing>

CONVERTTEMPが2つのパラメーターをとると仮定します。文字型（`char`）のTEMPINと構造体のSTRUCT1で、STRUCT1は2つの整数型（`int`）のフィールドFLD1とFLD2を持ちす。 パラメーターのラップを選択すると、前例のように全入力パラメーター用にCONVERTTEMPInputラッパー構造体が生成されます。XML文書形式はリスト2のようになります。

**リスト 2. 入力XML形式サンプル – ラップ指定の構造体**
<code-listing html-highlight="all-highlighting-off"><pre> &lpar;newline&rpar;&lpar;less-thanCONVERTTEMPInput&lpar;greater-than &lpar;newline&rpar;    &lpar;less-thanTEMPIN&lpar;greater-than23&lpar;less-than/TEMPIN&lpar;greater-than&lpar;newline&rpar;    &lpar;less-thanSTRUCT1&lpar;greater-than &lpar;newline&rpar;        &lpar;less-thanFLD1&lpar;greater-than00&lpar;less-than/FLD1&lpar;greater-than&lpar;newline&rpar;        &lpar;less-thanFLD2&lpar;greater-than01&lpar;less-than/FLD2&lpar;greater-than&lpar;newline&rpar;    &lpar;less-than/STRUCT1&lpar;greater-than&lpar;newline&rpar;&lpar;less-than/CONVERTTEMPInput&lpar;greater-than </pre></code-listing>

入力パラメーターのアンラップを選択すると、TEMPINパラメーターをソース入力（例えばCookieやパス変数）からの値でインジェクトしなければなりません。入力XML文書はリスト3のような形式となります。

**リスト 3. 入力XML形式サンプル – アンラップ指定の構造体**
<code-listing html-highlight="all-highlighting-off"><pre> &lpar;newline&rpar;&lpar;less-thanSTRUCT1&lpar;greater-than &lpar;newline&rpar;    &lpar;less-thanFLD1&lpar;greater-than00&lpar;less-than/FLD1&lpar;greater-than&lpar;newline&rpar;    &lpar;less-thanFLD2&lpar;greater-than01&lpar;less-than/FLD2&lpar;greater-than &lpar;newline&rpar;&lpar;less-than/STRUCT1&lpar;greater-than </pre></code-listing>

出力パラメーターにおいては、常にラッパー構造体が生成されます。この例では、リスト4に示すXMLドキュメンが戻されます。

**リスト 4. 出力XML形式サンプル**
<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;&lpar;less-thanCONVERTTEMPResult&lpar;greater-than &lpar;newline&rpar;    &lpar;less-thanTEMPOUT&lpar;greater-than23&lpar;less-than/TEMPOUT&lpar;greater-than&lpar;newline&rpar;&lpar;less-than/CONVERTTEMPResult&lpar;greater-than </pre></code-listing>

### JSONメッセージ形式

XMLと同じように、1つの入力パラメーターだけがJSONのメッセージ・コンテンツを受け取り、それは構造体でなければなりません。

JSON形式であるメッセージ本体を入力パラメーターが受け取るとき、クライアントが送るべきJSON文書形式は、入力パラメーターのラップあるいはアンラップに依存します。

CONVERTTEMPプロシージャーで、パラメーターのアンラップを選択すると、リソース・メソッドはプリミティブ型の入力パラメーターをとります。したがってJSONデータを入力としては受け付けません。また、入力パラメーターのラップを選択すると、CONVERTTEMPInputという名前のラッパー構造体が生成され、それが全ての入力パラメーターを含みます。このケースでは、1個のみでTEMPINです。これにより、クライアントが送信する必要のあるJSON文書はリスト5のようになります。

**リスト 5. 入力 JSON形式サンプル – ラップ指定**
<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;{"TEMPIN": "2337"}&lpar;newline&rpar;</pre></code-listing>

ラッパー構造体の名前はJSONデータの中に含まれないことに注意してください。

ここで、CONVERTTEMPが2つのパラメーターを持つと仮定します。文字型（`char`）のTEMPINと構造体のSTRUCT1で、STRUCT1は2つの整数型（`int`）のフィールドFLD1とFLD2を持ちます。パラメーターのラップを選択すると、前例のように全入力パラメーター用にCONVERTTEMPInputラッパー構造体が生成されます。JSON文書形式はリスト6のようになります。

**リスト 6. 入力JSON形式サンプル – ラップ指定の構造体**
<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;{&lpar;newline&rpar;    "TEMPIN": "23",&lpar;newline&rpar;    "STRUCT1": &lpar;newline&rpar;    {&lpar;newline&rpar;        "FLD1": "00",&lpar;newline&rpar;        "FLD2": "01" &lpar;newline&rpar;    }&lpar;newline&rpar;} &lpar;newline&rpar;</pre></code-listing>

入力パラメーターのアンラップを選択すると、TEMPINパラメーターをソース入力（例えばCookieやパス変数）からの値でインジェクトしなければなりません。入力JSON文書はリスト7のような形式になります。

**リスト 7. 入力JSON形式サンプル – アンラップ指定の構造体**
<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;{&lpar;newline&rpar;    "FLD1": "00",&lpar;newline&rpar;    "FLD2": "01"&lpar;newline&rpar;}</pre></code-listing>

出力パラメーターにおいては、常にラッパー構造体が生成されます。この例ではリスト8に示すJSON文書が戻されます。

**リスト 8. 出力JSON形式サンプル**
<code-listing html-highlight="all-highlighting-off"><pre>&lpar;newline&rpar;{"TEMPOUT": "1280.55"}&lpar;newline&rpar;</pre></code-listing>

## まとめ

この記事では、RESTの基本概念と統合Webサービス・サーバーにおけるRESTサポートについて説明しました。すでに数年前から、統合Webサービス・サーバーを用いてILEプログラムとサービス・プログラムをSOAPプロトコルのWebサービスとして公開することが可能でした。他に類を見ないシンプルさで、SOAPベースのWebサービスでアセット（例えばデータやサービス）公開を可能にしてきましたが、対象がRESTベースのWebサービスに拡張されました。

REST APIは、データの共有と再利用を促進する素晴らしい方法です。さらに重要なことは、これによって企業が新しい市場のお客様と関わりを持つことができるということです。REST経由でデータにアクセスできるようになれば、外部の開発者が素晴らしいアプリケーションを簡単に構築したり、製品やデータを有効活用する面白い方法を容易に考案できるようになります。手元にあるリソースを解き放ちませんか？

[パート 2](../../Tutorials/i-rest-web-services-server2/)は、簡単なILEアプリケーションをRESTful Webサービスとしてデプロイする手順を説明します。

<a id="_Resources" />

## 参考情報

* IBM iの統合Webサービスのサポートに関しては、[製品のWebページ](https://www.ibm.com/systems/power/software/i/iws/)を参照してください。
* 本シリーズの[パート 2](../../Tutorials/i-rest-web-services-server2/)は、簡単なILEアプリケーションをRESTful Webサービスとしてデプロイする手順を説明します。
* [RESTful Web services: The basics](https://developer.ibm.com/articles/ws-restful/)は、RESTの概要について説明しています。
* HTTPプロトコルとコンテンツ・ネゴシエーションについては、[RFC 2616](https://www.w3.org/Protocols/rfc2616/rfc2616.html)を参照してください。
* Java正規表現については、Javaチュートリアルが提供する[regular expressions](https://docs.oracle.com/javase/tutorial/essential/regex/)のレッスンを参照してください。
