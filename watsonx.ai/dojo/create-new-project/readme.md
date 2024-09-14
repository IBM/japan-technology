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
<img width="1548" alt="wxai-newproj-01" src="https://github.com/user-attachments/assets/03d0b453-a1b3-4919-adbf-7f06808ea08d">

2. [プロジェクトの作成]ページが表示されます。プロジェクトを識別するための名前を入力して[作成]をクリックします。

日本語でも英語でも構いません。この名前は、単にユーザーがプロジェクトを識別するためのものです。このため、皆さんは後からいつでも自由にプロジェクトの名前を変更できます。IBM watsonxのシステム側から見ると、プロジェクトごとにGUIDを使って固有の番号を割り当てています。これを「プロジェクト ID」と呼んでいます。IBM watsonx APIを利用する場合は、プロジェクトの名前ではなく、プロジェクトIDを使います。
<img width="1548" alt="wxai-newproject-02-blankproject" src="https://github.com/user-attachments/assets/3a484948-d6ff-4931-bc80-ebbe3e01b0b6">
IBM Technology Zoneを利用している場合、あるいはIBM watsonx 30日無料体験版を利用している場合は、[ストレージ]のところに、Cloud Object Storageの名前が自動的に割り当てられます。

もし次の図のように、表示されている場合は、[追加]をクリックして、ストレージの関連付けが必要です。

※ IBM Technology Zoneをお使いで、この図のようになった場合は、選択しているアカウントをご確認ください。意図せずに、予約した環境ではないアカウントを選択している可能性があります。

<img width="2302" alt="wxai-newproject-03-AddICOS" src="https://github.com/user-attachments/assets/1c56114c-5602-4e28-95ee-65178a5604df">

3. 

