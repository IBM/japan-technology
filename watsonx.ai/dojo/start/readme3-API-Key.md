# IBM CloudのAPIキーの取得方法

1. Webブラウザーから新しいタブ、あるいは新しいウィンドウを開き、 https://cloud.ibm.com/iam/overview へアクセスします。
<img width="1548" alt="wxai-plst-13-CloudIAM" src="https://github.com/user-attachments/assets/6d35dc25-6c76-4310-92f5-4090f600271e">

2. 画面左側のメニューから[APIキー]をクリックします。[APIキー]の画面が表示されたら、[作成 +]をクリックします。
<img width="1548" alt="wxai-plst-14-APIKey" src="https://github.com/user-attachments/assets/f69489fe-976c-4197-8d70-aff66f1b8770">

3. [IBM Cloud API キーの作成]ダイアログ・ウィンドウが表示されるのを確認します。[名前]を「wxdojo」と入力して、[作成]をクリックします。
    <img width="1548" alt="wxai-plst-15-NewAPIKey" src="https://github.com/user-attachments/assets/56ebe4bc-b5bd-4c92-a427-2f5b19ea0692">

4. [APIキーは正常に作成されました]ダイアログ・ウィンドウが表示されるのを確認します。右下にある[ダウンロード]をクリックします。
    
<img width="684" alt="wxai-plst-16-DownloadKey" src="https://github.com/user-attachments/assets/dc0e0a8f-ed16-4943-bcfe-7d419a109032">

5. Visual Studio Codeを使って、ダウンロードした apikey.json を開きます。APIキーを確認します。このキーは他の人に知られないように管理してください。特にインターネットに公開しているGitHubのリポジトリにAPIキーを共有することはお控えください。

```
{
	"name": "wxdojo",
	"description": "",
	"createdAt": "2024-09-14T17:51+0000",
	"apikey": "<ここに表示されている内容がAPIキーとなります>"
}
```
