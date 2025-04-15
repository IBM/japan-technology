# watsonx.ai、新規プロジェクト作成
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


2. [プロジェクトの作成]ページが表示されます。プロジェクトを識別するための名前を入力して[作成]をクリックします。

※ この手順はハンズオン毎に実行するので、ハンズオンのイベント番号にあわせて、Dojo 02, Dojo 03などと命名するとわかりやすいです。

ポイント: 日本語でも英語でも構いません。この名前は、単にユーザーがプロジェクトを識別するためのものです。このため、皆さんは後からいつでも自由にプロジェクトの名前を変更できます。IBM watsonxのシステム側から見ると、プロジェクトごとにGUIDを使って固有の番号を割り当てています。これを「プロジェクト ID」と呼んでいます。IBM watsonx APIを利用する場合は、プロジェクトの名前ではなく、プロジェクトIDを使います。
<img width="1548" alt="wxai-newproject-02-blankproject" src="https://github.com/user-attachments/assets/3a484948-d6ff-4931-bc80-ebbe3e01b0b6">
IBM Technology Zoneを利用している場合、あるいはIBM watsonx 30日無料体験版を利用している場合は、[ストレージ]のところに、Cloud Object Storageの名前が自動的に割り当てられます。

もし次の図のように、表示されている場合は、[追加]をクリックして、ストレージの関連付けが必要です。

※ IBM Technology Zoneをお使いで、この図のようになった場合は、選択しているアカウントをご確認ください。意図せずに、予約した環境ではないアカウントを選択している可能性があります。

<img width="2302" alt="wxai-newproject-03-AddICOS" src="https://github.com/user-attachments/assets/1c56114c-5602-4e28-95ee-65178a5604df">

3. プロジェクトが作成された後、概要ページが表示されます。
 <img width="1548" alt="wxai-newproj-03-overview" src="https://github.com/user-attachments/assets/c75aef56-5a7d-4b92-aabb-8aa0182bd4ae">

4. [管理]タブを開きます。
<img width="1548" alt="wxai-newproj-04-management" src="https://github.com/user-attachments/assets/6f5db7b4-c948-4633-9e42-bf3a80bad790">

   ここで、Webブラウザーに表示されているURLをご覧ください。https://jp-tok.dataplatform.cloud.ibm.com/projects/ の後にGUID形式のIDが表示されています。このIDは、[管理]タブの[一般]-[詳細]タイルに表示されている[プロジェクト ID]と同じです。コピー用のアイコンを使って、プロジェクトIDをクリップボードにコピーできます。コピーしたプロジェクトIDをメモ帳などに貼り付けておきましょう。
   <img width="1548" alt="wxai-newproj-05-projectid" src="https://github.com/user-attachments/assets/925e718b-cba5-47a9-a61a-0dece115f408">

5. 左ペインにある[サービスおよび統合]をクリックします。
<img width="1548" alt="wxai-newproje-06-integration" src="https://github.com/user-attachments/assets/2d49d120-2767-4025-b9ec-dd224e1d8d5e">
6. 画面向かって右上側にある[サービスの関連付け +]という青色のボタンをクリックします。
<img width="1548" alt="wxai-newproje-06-integration" src="https://github.com/user-attachments/assets/0b6de545-7d0a-4ffb-aa8d-442a3cc0d9f6">

7. Watson Machine Learningがサービスの一覧に表示されていることを確認します。
<img width="1548" alt="wxai-newproj-07-wml" src="https://github.com/user-attachments/assets/d7af39a3-38cf-4bc7-b3ab-bd0264d51177">

(この時点でWatson Machine Learningが見つからない場合）
サービスの関連付けから、[新規サービス +]をクリックし、サービスの画面を表示します。
<img width="1548" alt="wxai-newproj-08-newservice" src="https://github.com/user-attachments/assets/54682a10-2e54-44da-9273-ab9d9f502d93">

続いて、[Watson Machine Learning]をクリックします。
<img width="1548" alt="wxai-newproj-09-createWML" src="https://github.com/user-attachments/assets/1a37a12e-f3de-4ed4-991d-df2e41391a83">
Watson Machine Learningの画面の右下にある[作成]をクリックします。

8. サービスの一覧に表示されている Watson Machine Learning の行にチェック☑️を入れて、画面右下の[アソシエイト]をクリックします。
<img width="1548" alt="wxai-newproj-10-associateWML" src="https://github.com/user-attachments/assets/65cc4ffb-c511-4be3-a6af-397b193d49f6">

9. サービスおよび統合の[IBMサービス]タブ内に、関連付けたWatson Machine Learningが表示されていることを確認します。
<img width="1548" alt="wxai-newproj-11-WMLassociated" src="https://github.com/user-attachments/assets/a1263fd2-71e9-4480-8985-5a8b92c939dd">

10. これで新規プロジェクトの準備が整いました。
   watsonx.ai Dojoにオンラインで参加している方で、このプロジェクトの準備がうまくできない方は、チャット欄からお知らせください。

    




