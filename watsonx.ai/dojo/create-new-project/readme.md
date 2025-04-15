# watsonx.ai、新規プロジェクト作成
最終更新日: 2025/4/15

このパートでは、次の操作を学びます。
* 新規プロジェクトの作成
* プロジェクトとWatson Machine Learningサービスの関連付け

参考URL: IBM watsonx as a Service 、[プロジェクトの作成](https://dataplatform.cloud.ibm.com/docs/content/wsj/getting-started/projects.html?context=wx&audience=wdp, "create new project")

## プロジェクトとは
プロジェクトとは、特定の目標を達成するために、データ、プロンプト、コードを実行する資産などを含めることができるものです。
プロジェクトは他のユーザーと共同作業することができます。またプロジェクトをZIPファイルとしてエクスポートし、他のユーザーへ共有することもできます。

参考URL:
* [プロジェクト資産のインポート](https://dataplatform.cloud.ibm.com/docs/content/wsj/manage-data/import-project-assets.html?context=wx&audience=wdp, "import project")
   
* [プロジェクト資産のエクスポート](https://dataplatform.cloud.ibm.com/docs/content/wsj/manage-data/export-project.html?context=wx&audience=wdp, "export project")

## 新規プロジェクトの作成
1. IBM watsonx のトップページから、[最近の作業]欄にある[プロジェクト]のタイルを見つけ、[+]をクリックします。マウス・カーソルを[+]に近づけると、[新規プロジェクトの作成]というヒントが表示されます。
<img width="1328" alt="wxai00-create-new-project-plus" src="https://github.com/user-attachments/assets/2226a6a1-3bd3-4996-acd1-88ba3d7bfc61" />

* 別の方法として、https://jp-tok.dataplatform.cloud.ibm.com/projects/new-project?context=wx をブラウザーで開くと、[プロジェクトの作成]のページを表示できます。

2. [プロジェクトの作成]ページが表示されます。[詳細の定義]欄で、プロジェクトを識別するための[名前]を入力して[作成]をクリックします。

※ この手順はハンズオン毎に実行するので、ハンズオンのイベント番号にあわせて、Dojo 02, Dojo 03などと命名するとわかりやすいです。

ポイント: プロジェクトの名前は、日本語でも英語でも構いません。この名前は、単にユーザーがプロジェクトを識別するためのものです。このため、皆さんは後からいつでも自由にプロジェクトの名前を変更できます。IBM watsonxのシステム側から見ると、プロジェクトごとにGUID(グローバル 一意識別子)を使って固有の番号を割り当てています。これを「プロジェクト ID」と呼んでいます。IBM watsonx APIを利用する場合は、プロジェクトの名前は利用せず、プロジェクトIDを使います。

<img width="1328" alt="wxai00-02-newproject" src="https://github.com/user-attachments/assets/38f80216-f9cd-4ab3-a0e3-5d587ee713dc" />


IBM Technology Zoneを利用している場合、あるいはIBM watsonx 30日無料体験版を利用している場合は、[ストレージ]のところに、Cloud Object Storageの名前が自動的に割り当てられます。

もし次の図のように、表示されている場合は、[追加]をクリックして、ストレージの関連付けが必要です。

※ IBM Technology Zoneをお使いで、この図のようになった場合は、選択しているアカウントをご確認ください。意図せずに、予約した環境ではないアカウントを選択している可能性があります。

<img width="2302" alt="wxai-newproject-03-AddICOS" src="https://github.com/user-attachments/assets/1c56114c-5602-4e28-95ee-65178a5604df">

3. プロジェクトが作成された後、概要ページが表示されます。
<img width="1328" alt="wxai00-03-project-overview" src="https://github.com/user-attachments/assets/22f33a66-44fe-4a4b-9808-bcc22cf0fad7" />


4. [管理]タブを開きます。

<img width="1328" alt="wxai00-04-manage-project" src="https://github.com/user-attachments/assets/8a05a8a2-8f49-4f33-9c69-298c40414931" />


   ここで、Webブラウザーに表示されているURLをご覧ください。https://jp-tok.dataplatform.cloud.ibm.com/projects/ の後にGUID形式のIDが表示されています。このIDは、[管理]タブの[一般]-[詳細]タイルに表示されている[プロジェクト ID]と同じです。コピー用のアイコンを使って、プロジェクトIDをクリップボードにコピーできます。コピーしたプロジェクトIDをメモ帳などに貼り付けておきましょう。

<img width="1328" alt="wxai00-05-copy-projectid" src="https://github.com/user-attachments/assets/50da09c1-93e7-47ba-ab98-396d27e8169b" />

* ご注意: プロジェクトを作成した段階では、watsonx.aiを使った推論機能は有効になっていません。この後の手順で、watsonx.ai Runtime (Watson Machine Learning)をプロジェクトに関連付けして、推論機能を使えるようにします。

5. 左ペインにある[サービスおよび統合]をクリックします。

<img width="1328" alt="wxai00-06-service-integration" src="https://github.com/user-attachments/assets/60f3ddae-9c07-464c-87f6-08e698f47659" />


6. 画面向かって、右上側にある[サービスの関連付け +]という青色のボタンをクリックします。

<img width="1328" alt="wxai00-07-associate-new-service" src="https://github.com/user-attachments/assets/2062bc1a-ed9e-4316-957f-ec1de178637c" />


7. Watson Machine Learningがサービスの一覧に表示されていることを確認します。

<img width="1328" alt="wxai00-08-list-services" src="https://github.com/user-attachments/assets/642caf7d-3afe-4a17-ad88-8189551b96a8" />


(この時点で一覧の中にWatson Machine Learningが見つからない場合）
サービスの関連付けから、[新規サービス +]をクリックし、サービスの画面を表示します。
<img width="1548" alt="wxai-newproj-08-newservice" src="https://github.com/user-attachments/assets/54682a10-2e54-44da-9273-ab9d9f502d93">

続いて、[Watson Machine Learning]をクリックします。
<img width="1548" alt="wxai-newproj-09-createWML" src="https://github.com/user-attachments/assets/1a37a12e-f3de-4ed4-991d-df2e41391a83">
Watson Machine Learningの画面の右下にある[作成]をクリックします。

8. サービスの一覧に表示されている Watson Machine Learning の行にチェック☑️を入れて、画面右下の[アソシエイト]をクリックします。

<img width="1328" alt="wxai00-09-associate-wml" src="https://github.com/user-attachments/assets/18d7cef4-59ea-4129-88d3-37f53b349944" />


9. サービスおよび統合の[IBMサービス]タブ内に、関連付けたWatson Machine Learningが表示されていることを確認します。[サービス・タイプ]がwatsonx.ai Runtime と表示されています。

<img width="1328" alt="wxai00-10-wml-associated" src="https://github.com/user-attachments/assets/186505e5-09e0-4249-81de-defe1791a12f" />

* ご注意: これまでのIBM Watsonの技術にWatson Machine Learningという機械学習、推論エンジンがありました。IBM watsonx.aiにおいては、このWatson Machine Learningをwatsonx.ai Runtimeと名称変更しています。現時点では、IBM Watson Machine LearningとIBM watsonx.ai Runtimeは同じものです。

10. これで新規プロジェクトの準備が整いました。
   watsonx.ai Dojoにオンラインで参加している方で、このプロジェクトの準備がうまくできない方は、チャット欄からお知らせください。
　　ハンズオン会場で参加している方で、この準備がうまくできない方は、近くにいるサポート・スタッフにお声がけください。

    




