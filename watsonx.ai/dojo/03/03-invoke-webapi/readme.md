## watsonx.ai にデプロイ済みのWebサービスを呼び出す


前提条件: [watsonx.ai Dojo #3 パート2](https://github.com/IBM/japan-technology/tree/main/watsonx.ai/dojo/03/02-structured-prompt) を完了し、depWSがデプロイできていること。

免責事項: 生成AIは事前学習したデータを活用しながらテキストを生成します。言語モデルに含まれている言葉が確率で選択されるため、生成AIは事実と異なる結果を生成する場合があります。生成AIのハルシネーションから間違った内容が伝わらないよう、生成された内容をそのまま利用するのではなく、必ず、事実確認を行なってください。

振り返り: プロジェクト、スペース、デプロイメントの関係を理解して進めましょう。
それぞれの繋がりがわかりづらいので、図で整理しておきます。理解すべき点は、２つあります。

* スペースとプロジェクトは独立した関係であり、１つのスペースには、複数のプロジェクトから資産をプロモートすることができます
* スペースにプロモートされた資産のみがデプロイメントできます（プロジェクトから直接デプロイメントはできません）

<img width="2107" alt="wxai03-02-project-space-deployment" src="https://github.com/user-attachments/assets/cb899e48-af8f-4823-8a1c-3075cbb76622">


#

1. Webブラウザーから https://jp-tok.dataplatform.cloud.ibm.com/ml-runtime/dashboard?context=wx へアクセスし、[デプロイメント]のページを開きます。
[スペース]タグをクリックします。
<img width="1399" alt="wxai03-03-01-DepDashboard" src="https://github.com/user-attachments/assets/ff97dd35-da97-4b4f-93a3-28a79a980308">


2. wxaiSpace-という名前で始まる[スペース]が一覧に表示されていることを確認し、その名前をクリックします。
<img width="1397" alt="wxai03-03-02-listDeployment" src="https://github.com/user-attachments/assets/d7da2dcc-45d0-4e59-988c-8da345431260">

wxaiSpace-という名前の画面が表示されます。続けて[管理]タブをクリックします。[詳細]欄に[スペース GUID]が表示されているので、メモ帳などに控えておきます。後述の(param2)となります。
<img width="1401" alt="wxai03-03-02-Manage" src="https://github.com/user-attachments/assets/2ca660fe-edf8-45eb-b904-3bf640f600fc">


3. [資産]タブをクリックします。資産の中に[Welcome-Shizuoka-template]が表示されていることを確認します。
<img width="1396" alt="wxai03-03-03-wxaiSpace" src="https://github.com/user-attachments/assets/571f5737-1e31-43b8-9a48-983a46c2340f">

4. [デプロイメント]タブをクリックし、[depWS]がデプロイ済みであることを確認します。[depWS]をクリックします。
<img width="1397" alt="wxai03-03-04-deployedWS" src="https://github.com/user-attachments/assets/e70df30c-493a-4ba7-8a5d-eddcf5cf240c">

5. [depWS]の画面が表示されます。これまでの手順を確認して、デプロイ済みのサービスを見つける方法を覚えておきましょう。[デプロイメントID:]の右側にあるIDをクリックして、メモ帳などに控えておきましょう。後述の(param3)となります。

<img width="1399" alt="wxai03-03-05-detail-depWS" src="https://github.com/user-attachments/assets/29ffa3ff-fb4f-4c06-a41b-f891f4d698dc">

* パブリック・エンドポイントURLの例: https://jp-tok.ml.cloud.ibm.com/ml/v1/deployments/wst01_ao_20241016/text/generation?version=2021-05-01

* wst01_のところは、皆さんが指定したwst01_で始まる文字列が表示されるはずです。

6. 続けて、[テスト]タブをクリックします。テスト画面が表示されるので、右下の[生成]をクリックします。
<img width="1400" alt="wxai03-03-06-test-depWS" src="https://github.com/user-attachments/assets/0e0b0770-1936-41b7-8eca-ea099f7ca706">


7. しばらく待つと、[プロンプト結果]が表示されます。

<img width="1272" alt="wxai03-03-07-promptResultV3" src="https://github.com/user-attachments/assets/7a6f26d3-0a15-42f2-ba77-98b3a5509b89">

8. [JSONビュー]をクリックして、結果をJSON形式で確認しましょう。[JSONファイルのダウンロード]をクリックして、ファイルをローカル・コンピュータに保存します。

<img width="1275" alt="wxai03-03-08-viewJson" src="https://github.com/user-attachments/assets/09d7bab4-151c-4e08-9460-d928b5c6dc1c">


9. 右上の[x]をクリックして、結果を閉じます。

10. [ストリーム]タブをクリックし、手順6と同様に、右下の[生成]をクリックします。

<img width="1401" alt="wxai03-03-10-test-Stream" src="https://github.com/user-attachments/assets/8afd1138-d25b-4ff7-b04c-686456c5d834">

11. しばらく待つと、[プロンプト結果]が表示されます。手順7や手順8とは異なり、文章が細かく分割されて送られてきているのを確認できます。
<img width="1275" alt="wxai03-03-11-streamingResult" src="https://github.com/user-attachments/assets/209c958f-c00b-476e-a341-ebf71d1259c5">


12. [テキスト・ビュー]をクリックして、内容を確認します。右下にある[テキスト・ファイルのダウンロード]をクリックして、ファイルをローカル・コンピュータに保存します。

<img width="1276" alt="wxai03-03-12-streamTextView" src="https://github.com/user-attachments/assets/7eb8f890-a598-4266-8f6c-d9eb6f8c377c">


13. 右上の[x]をクリックして、結果を閉じます。
14. [JSON]タブをクリックして、手順6や手順10と同様に、右下の[生成]をクリックします。
<img width="1401" alt="wxai03-03-14-json-input" src="https://github.com/user-attachments/assets/3648b59d-64d9-440a-a02f-a2d9e6b242e6">

15. しばらく待つと、[プロンプト結果]が表示されます。手順7と同じ結果が得られていることを確認します。

<img width="1275" alt="wxai03-03-15-result-json" src="https://github.com/user-attachments/assets/fbdef6a8-4f44-4061-9d89-b291c78ee10c">

16. Pythonのコードを使って、デプロイ済みのプロンプト・テンプレートを呼び出します。
* (param1) IBM CloudのAPIキー: ```XXXXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-XXX```
  
[IBM CloudのAPIキーの取得方法](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/start/readme3-API-Key.md "API Key")を参考にして、APIキーを取得してください。APIキーは安全な場所に保管し、皆さんと関係のない人には決して共有しないでください。

* (param2) wxaiSpace-で始まる名前のスペース GUID:　```XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX```
上記の手順2を確認してください。

* (param3) depWSのデプロイメントID:　```XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX```

上記の手順5を確認してください。

17. ターミナル(Mac)またはUbuntu(Windows)を開き、次のコマンドを実行します。
```
cd ~/wxai
source venv/bin/activate
pip install ibm_watsonx_ai
code shizchat.py
```

18. Visual Studio Codeが開くので、次のコードを貼り付けます。api_key, space_id, deployment_id は手順16で取得した値を設定してください。
shizchat.pyの編集が終わったら、必ず[保存]してください。
```
# shizchat.py
import requests, json 
from ibm_watsonx_ai import APIClient
from ibm_cloud_sdk_core import IAMTokenManager
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

# api_key: IBM Cloud IAMから取得したAPIキーを入れてください (param1)
api_key = "XXXXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-XXX"
# space_id: wxaiSpaceのスペース GUIDを指定してください (param2)
space_id ="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
# deployment_id: depWSのデプロイメントIDを指定してください (param3)
deployment_id="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"

# wml_urlは 東京リージョンと想定します。
# 米国ダラスの場合は、"https://us-south.ml.cloud.ibm.com"とします。
wml_url ="https://jp-tok.ml.cloud.ibm.com"

# アクセス・トークンの取得用関数(IBM CloudのIAMからAPIキーを取得すること)
def get_auth_token():
    access_token = IAMTokenManager(apikey=api_key,url="https://iam.cloud.ibm.com/identity/token").get_token()
    print ("access_token:"+access_token)
    return access_token

# プロンプト・テンプレートの呼び出し
def invoke_prompt_template(url, api_key,space_id, deployment_id, prompt_vars):
    credentials = {
        "url": url,
        "apikey": api_key
    }
    client = APIClient(credentials)
    client.set.default_space(space_id)
    params={"prompt_variables": prompt_vars}
    generated_response = client.deployments.generate_text(deployment_id, params=params)

    print("--- プロンプト・テンプレートのWeb API呼び出し ---")
    print("Response: " + generated_response)
    print("-------------------------------------------")

    return generated_response

headers = {
	"Accept": "application/json",
	"Content-Type": "application/json",
	"Authorization": "Bearer "+get_auth_token()
}
# プロンプト変数の設定
prompt_var = {
    "your_input": "静岡県を知らない人に向けて、静岡県への旅行をお勧めする文章を作ってください。例があればその例を参考にして、次の「見出し一覧」にある項目を含めて書いてください。文章の最後は「魅力あふれる静岡県にお越しください！」としてください。同じ内容を繰り返さないでください。\n\n「見出し一覧」:\n- 静岡県にある観光名所3ヶ所\n- 静岡県出身の有名人、芸能人4人\n- 静岡県で有名なレストラン3つ\n- 静岡県がモデルとなっているアニメ作品3つ"
}     
print("prompt_var = "+json.dumps(prompt_var, indent=2))
# デプロイ済みのプロンプト・テンプレートの呼び出し
resString = invoke_prompt_template(wml_url, api_key, space_id, deployment_id, prompt_var)

```
19. ターミナル(Mac)またはUbuntu(Windows)に戻り、次のコマンドを実行します。エラーが表示される場合は、後述の[Pythonコードのトラブルシューティング](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/03/03-invoke-webapi/readme.md#python%E3%82%B3%E3%83%BC%E3%83%89%E3%81%AE%E3%83%88%E3%83%A9%E3%83%96%E3%83%AB%E3%82%B7%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0 "Python Trouble shooting")を参考にしてください。

```
python shizchat.py 
```

実行例: (アクセス・トークンの表示は省略します）
* Ubuntu + Python 3.12
<img width="1679" alt="wxaiDojo03-ResultsWithPython3-12" src="https://github.com/user-attachments/assets/a2e99cff-e34e-4838-8485-9384e33220f8">

* mac (Intel) + Python 3.10
<img width="2222" alt="wxaiDojo03-ResultsWithPython3-10-mac" src="https://github.com/user-attachments/assets/de0a6b5d-d9f9-46b3-be70-61d28f1966f0">

* 生成例:
```
prompt_var = {
  "your_input": "\u9759\u5ca1\u770c\u3092\u77e5\u3089\u306a\u3044\u4eba\u306b\u5411\u3051\u3066\u3001\u9759\u5ca1\u770c\u3078\u306e\u65c5\u884c\u3092\u304a\u52e7\u3081\u3059\u308b\u6587\u7ae0\u3092\u4f5c\u3063\u3066\u304f\u3060\u3055\u3044\u3002\u4f8b\u304c\u3042\u308c\u3070\u305d\u306e\u4f8b\u3092\u53c2\u8003\u306b\u3057\u3066\u3001\u6b21\u306e\u300c\u898b\u51fa\u3057\u4e00\u89a7\u300d\u306b\u3042\u308b\u9805\u76ee\u3092\u542b\u3081\u3066\u66f8\u3044\u3066\u304f\u3060\u3055\u3044\u3002\u6587\u7ae0\u306e\u6700\u5f8c\u306f\u300c\u9b45\u529b\u3042\u3075\u308c\u308b\u9759\u5ca1\u770c\u306b\u304a\u8d8a\u3057\u304f\u3060\u3055\u3044\uff01\u300d\u3068\u3057\u3066\u304f\u3060\u3055\u3044\u3002\u540c\u3058\u5185\u5bb9\u3092\u7e70\u308a\u8fd4\u3055\u306a\u3044\u3067\u304f\u3060\u3055\u3044\u3002\n\n\u300c\u898b\u51fa\u3057\u4e00\u89a7\u300d:\n- \u9759\u5ca1\u770c\u306b\u3042\u308b\u89b3\u5149\u540d\u62403\u30f6\u6240\n- \u9759\u5ca1\u770c\u51fa\u8eab\u306e\u6709\u540d\u4eba\u3001\u82b8\u80fd\u4eba4\u4eba\n- \u9759\u5ca1\u770c\u3067\u6709\u540d\u306a\u30ec\u30b9\u30c8\u30e9\u30f33\u3064\n- \u9759\u5ca1\u770c\u304c\u30e2\u30c7\u30eb\u3068\u306a\u3063\u3066\u3044\u308b\u30a2\u30cb\u30e1\u4f5c\u54c13\u3064"
}
--- プロンプト・テンプレートのWeb API呼び出し ---
Response:  静岡県は、富士山や伊豆半島などの豊かな自然と、徳川家康公が築いた歴史ある都市が調和した魅力的な県です。

静岡県にある観光名所3ヶ所

1. 富士山：静岡県と山梨県に跨る日本最高峰の独立峰で、日本の象徴ともいえる名峰です。
2. 三保の松原：静岡県静岡市清水区の三保半島にある景勝地です。富士山と羽衣伝説で知られる松林が見られます。
3. 修善寺：静岡県伊豆市にある温泉街です。伊豆最古の温泉と言われ、多くの観光客が訪れます。

静岡県出身の有名人、芸能人4人

1. 広瀬 すず：静岡県静岡市清水区出身。女優、ファッションモデルとして活躍中。
2. 長澤 まさみ：静岡県磐田市出身。女優として数々の話題作に出演している。
3. 百田 夏菜子：静岡県浜松市出身。ももいろクローバーZのリーダーで、女優としても活躍中。
4. 久保田 利伸：静岡県静岡市清水区出身。歌手、音楽プロデューサーとして活躍中。

静岡県で有名なレストラン3つ

1. 炭焼きレストランさわやか：げんこつハンバーグが名物の静岡県内に展開するファミリーレストラン。県内に多くの店舗がある。
2. 中華ファミリーレストラン五味八珍：静岡県内に展開する中華ファミリーレストラン。浜松餃子が名物で、多くの観光客が訪れます。
3. 元祖丁子屋：静岡県静岡市駿河区丸子にあるとろろ汁の専門店。東海道五十三次にも指定されている。

静岡県がモデルとなっているアニメ作品3つ

1. ラブライブ！サンシャイン!!：静岡県沼津市が舞台。伊豆・三津シーパラダイスも有名で、多くのファンが訪れています。
2. ちびまる子ちゃん：静岡県静岡市清水区が舞台。エスパルス・ドリームプラザ内に「ちびまる子ちゃんランド」があり、多くのファンが訪れています。
3. シュート！：静岡県掛川市が舞台。作品内の掛川高校は、掛川西高校がモデルと言われています。
-------------------------------------------
```

PythonコードとIBM watsonx (Watson Machine Learning)との関係を図にまとめましたので、参考にしてください。
<img width="1700" alt="wxaiDojo03-03-python-services" src="https://github.com/user-attachments/assets/4679f893-508c-46ef-9bbe-4082f8f150c3">


## Pythonコードのトラブルシューティング
* ModuleNotFoundError: No module named 'ibm_watsonx_ai' が表示される場合

  → 手順17を確認してください。ibm_watsonx_ai パッケージのインストールを実行してください。
```
cd ~/wxai
source venv/bin/activate
pip install ibm_watsonx_ai
```
* ModuleNotFoundError: No module named 'requests' と表示される場合、あるいは ModuleNotFoundError: No module named 'ibm_cloud_sdk_core' と表示される場合
  
  → ibm_cloud_sdk_core のインストールを実行してください。
```
pip install ibm_cloud_sdk_core
```
* ibm_cloud_sdk_core.api_exception.ApiException: Error: Provided API key could not be found., Status code: 400 と表示される場合

  → APIキーの指定が間違っていますので、ご確認ください。
    よくある間違いとして、APIキーには "<" や ">" の記号は含まれていません。APIキーを入れる際には、"<" や ">" の記号は削除してください。

* ibm_watsonx_ai.wml_client_error.CannotSetProjectOrSpace: Cannot set Project or Space
Reason: Space with id '<XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX>' does not exist と表示される場合

  → スペース GUIDの指定が間違っていますので、ご確認ください。
    よくある間違いとして、APIキーには "<" や ">" の記号は含まれていません。下記のようなコードに対してAPIキーを入れる際には、"<" や ">" の記号は削除してください。

* ibm_watsonx_ai.wml_client_error.ApiRequestFailure: Failure during getting deployments details. (GET https://jp-tok.ml.cloud.ibm.com/ml/v4/deployments/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX?version=2024-10-01&space_id=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX)
Status code: 404, body: {"trace":"7c593149a718dcaeaf87d1e288736654","errors":[{"code":"deployment_does_not_exist","message":"Deployment with id 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX' does not exist. Re-try with a valid deployment id."}]} のようなエラーが表示される場合

  → デプロイメントIDの指定が間違っていますので、ご確認ください。
