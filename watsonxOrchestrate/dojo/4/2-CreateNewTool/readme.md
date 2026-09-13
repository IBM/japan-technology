# ADKとPythonでツールを作る
* 最終更新日: 2025/12/16
* 参考ソース: [ツールを作ってみよう](https://github.ibm.com/ba-techsales-jp/ba-handson-jp/blob/main/docs/wxo_adk/tools.md)

## 前提条件
* watsonx Orchestrate ADK 2.1.0 がインストール済みである。
* watsonx Orchestrate Developer版が動作している
* Visual Studio Codeにwatsonx Orchestrate ADK拡張機能がインストールされている
* Windowsの場合、PowerShellを通じてコマンドを実行
* macOSの場合、ターミナルを通じてコマンドを実行

これらの条件が整っていない場合、[watsonx Orchestrate ADK環境構築](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/4/readme.md) を実行して、環境を整えてください。

### ADKがインストール済みで、ローカル版のwatsonx Orchestrateが起動していない場合の対処方法
* macOSの場合:

```
cd ~/wxo
source venv/bin/activate
orchestrate server start -e .\.env
```

* Windowsの場合 (PowerShell):

```
chcp 65001
```

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

```
cd ~/wxo
venv\Scripts\activate
orchestrate server start -e .\.env
```

* (mac/Windows共通) localのwatsonx Orchestrateを有効にする
```
orchestrate env activate local
```

* (mac/Windows共通) localのwatsonx OrchestrateのUI機能を起動する
```
orchestrate chat start
```

## ツールの確認
1. Visual Studio Codeを開きます。
コマンドを入力し、Visual Studio Codeを開きます。

```
cd ~/wxo
code .
```
2. Visual Studio Code内の<img width="40" height="41" alt="wxo" src="https://github.com/user-attachments/assets/7ff0b277-720b-47f1-8c3c-0c9309a0178b" />アイコンをクリックして、watsonx OrchestrateのExplorerを開きます。[EXPLORER]>[Tools]のフォルダーを見ると、ツールは作成されていないことがわかります。

3. コマンドを入力し、ツールの一覧を確認します。この時点では、おそらく何も表示されません。

```
orchestrate tools list
```

## ツールの作成
* Pythonを用いて、AIエージェント用のツールを作成してみます。ここでは、[yfinance](https://pypi.org/project/yfinance/)というPythonのパッケージを使用して、企業の株価情報を取得するツールを作成します。

4. 作成するツールの名前を名前をクリップボードにコピーします。
```
yfinance_tools
```

5. Visual Studio Codeに戻り、コマンド・パレットを開きます。
＊　macOS: [Shift]+[command]+[p] キー
* Windows: [ctrl]+[Shift]+[p]キー

6. コマンド・パレット内で[watsonx Orchestrate: Create new tool]を選び、[Enter]キーを入力します。
<img width="604" height="108" alt="create-newTool" src="https://github.com/user-attachments/assets/6d48e38b-f655-44af-9c9a-7df7bd36b512" />

7. 作成するツールの名前を入力するテキストボックスが表示されるので、コピー済みの名前を貼り付けます。
* コマンド・パレットを選択した直後
<img width="597" height="119" alt="cnt-Name" src="https://github.com/user-attachments/assets/7714aee4-306d-404b-8091-9e880c938405" />

* yfinance_toolsと入力（クリップボードから貼り付け)した直後
<img width="603" height="65" alt="cnt-yfinance" src="https://github.com/user-attachments/assets/916b4d86-c4a9-4525-a3ca-9b9004ecab41" />

8. Visual Studio Code上に yfinance_tools.pyのテンプレートが展開されます。
<img width="1426" height="863" alt="yfinance-tools-template" src="https://github.com/user-attachments/assets/f311676c-532f-429f-83bc-f61106053087" />

```
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from ibm_watsonx_orchestrate.run import connections
from ibm_watsonx_orchestrate.agent_builder.connections import ConnectionType

@tool(
  permissions=ToolPermission.READ_ONLY,
  expected_credentials=[
    {"app_id": "", "type": ConnectionType.}
  ]
)
def (:) -> :
    """
    

    Args:
        : 

    Returns:
        
    """

    return 
```

9. yfinance_tools.py を次の内容で上書きして、保存します。

```
import yfinance as yf
from pydantic import Field, BaseModel
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool
def get_stock_quote(symbol:str) -> str:

    """
    企業のTickerSymbolを用いて株価を取得します。
    Args:
        symbol: Symbol of the company.
    Returns:
        Price of the stock.
    """
    try:
        ticker=yf.Ticker(symbol) 
        print(ticker)

        current_price = ticker.fast_info.last_price
        return "{:.2f}".format(current_price)
    except Exception as e:
        return e


class TickerInfo(BaseModel):
    """
    Represents the details of a company info.
    """
    longBusinessSummary: str = Field(description='business summary of the company')
    sector: str = Field(description='sector of the company')
    industry: str = Field(description='industry of the company')
    fullTimeEmployee: int = Field(description='number of the fulltime employee of the company')
    per: float = Field(description='price earning ratio of the company')
    pbr: float = Field(description='price book ratio of the company')
    analyst_price_targets: dict = Field(description='analyst_price_targets')


@tool
def get_company_info(symbol:str) -> TickerInfo:

    """
    企業のTickerSymbolを用いて企業情報を取得します。
    Args:
        symbol: Symbol of the company.
    Returns:
        TickerInfo: company info of the company.
    """
    try:
        ticker=yf.Ticker(symbol) 
        print(ticker.actions)
        return TickerInfo(analyst_price_targets=ticker.analyst_price_targets,longBusinessSummary=ticker.info['longBusinessSummary'],fullTimeEmployee=ticker.info['fullTimeEmployees'],sector=ticker.info['sector'],industry=ticker.info['industry'],per=ticker.info['trailingPE'],pbr=ticker.info['priceToBook'])
    except Exception as e:
        return e

if __name__ == '__main__':
    price = get_stock_quote('IBM')
    print(price)

    info = get_company_info('IBM')
    print(info)
```

10. Pythonコマンドを使って、今、作成したツールを実行します。

macOS (ターミナル):
```
python  ./tools/yfinance_tools.py
```

Windows (PowerShell):
```
python  .\tools\yfinance_tools.py
```

実行例 (macOS):
* Python環境に yfinance パッケージがインストールされていないので、これは期待通りの動作です。
* ツールを作成する際は、Python環境で正しく動作することを事前に検証しましょう。watsonx Orchestrateが問題なのか、ツールが問題なのか、切り分けが容易になります。
```
(venv) oniak3.ai@ambp16 wxo % python ./tools/yfinance_tools.py
Traceback (most recent call last):
  File "/Users/oniak3.ai/Devenv/wxo/./tools/yfinance_tools.py", line 1, in <module>
    import yfinance as yf
ModuleNotFoundError: No module named 'yfinance'
```

11. pipコマンドを使って、yfinanceパッケージをインストールします。

```
pip install yfinance
```

12. Pythonコマンドを使って、動作確認しましょう。

macOS (ターミナル):
```
python  ./tools/yfinance_tools.py
```

Windows (PowerShell):
```
python  .\tools\yfinance_tools.py
```

実行結果の例 (macOS):

```
(venv) oniak3.ai@ambp16 wxo % python ./tools/yfinance_tools.py
yfinance.Ticker object <IBM>
308.66
                           Dividends  Stock Splits
Date                                              
1962-02-06 00:00:00-05:00   0.000956           0.0
1962-05-08 00:00:00-04:00   0.000956           0.0
1962-08-07 00:00:00-04:00   0.000956           0.0
1962-11-05 00:00:00-05:00   0.000956           0.0
1963-02-05 00:00:00-05:00   0.001275           0.0
...                              ...           ...
2024-11-12 00:00:00-05:00   1.670000           0.0
2025-02-10 00:00:00-05:00   1.670000           0.0
2025-05-09 00:00:00-04:00   1.680000           0.0
2025-08-08 00:00:00-04:00   1.680000           0.0
2025-11-10 00:00:00-05:00   1.680000           0.0

[262 rows x 2 columns]
longBusinessSummary="International Business Machines Corporation, together with its subsidiaries, provides integrated solutions and services in the Americas, Europe, the Middle East, Africa, and the Asia Pacific. It operates through Software, Consulting, Infrastructure, and Financing segments. The Software segment offers hybrid cloud and AI platforms that allows clients to realize their digital and AI transformations across the applications, data, and environments in which they operate. Its Consulting segment focuses on skills integration for strategy, experience, technology, and operations by domain and industry. The Infrastructure segment provides on-premises and cloud based server, and storage solutions, as well as life-cycle services for hybrid cloud infrastructure deployment. Its Financing segment offers client and commercial financing, facilitates IBM clients' acquisition of hardware, software, and services. It has strategic partnership with various companies, including hyperscalers, service providers, system integrators, and software and hardware vendors that includes Adobe, Amazon Web services, Microsoft, Oracle, Salesforce, Samsung Electronics and SAP, and others. The company was formerly known as Computing-Tabulating-Recording Co. International Business Machines Corporation was incorporated in 1911 and is headquartered in Armonk, New York." sector='Technology' industry='Information Technology Services' fullTimeEmployee=270300 per=36.74524 pbr=10.33933 analyst_price_targets={'current': 308.66, 'high': 360.0, 'low': 198.0, 'mean': 293.89316, 'median': 300.0}

```
13. ツールが動作していることを確認できたら、Visual Studio Codeに戻り、toolsフォルダーに requirement.txt を作成します。中身は yfinance のみです。
```
yfinance
```
14. 次のコマンドを実行し、作成したツールをインポートします。

* macOS (ターミナル):
```
orchestrate tools import -k python -f ./tools/yfinance_tools.py -r ./tools/requirement.txt
```

* Windows (PowerShell):
```
orchestrate tools import -k python -f .\tools\yfinance_tools.py -r .\tools\requirement.txt
```

## ツールの実行
* インポートしたツールをエージェントから実行してみましょう。AgentBuilderを用いてfinance_agentにツールを追加することもできますが、今回はADKを用いて追加をしてみます。

15. Visual Studio Codeからfinance_agent.yamlを開き、末尾に、次の3行を追加して保存してください。
```
tools:
  - get_stock_quote
  - get_company_info
```
16. コマンド・パレットを開きます。
＊　macOS: [Shift]+[command]+[p] キー
* Windows: [ctrl]+[Shift]+[p]キー

17. [watsonx Orchestrate: Import Current File]を選び、[Enter]キーを入力します。
<img width="598" height="62" alt="Import-CurrentFile2" src="https://github.com/user-attachments/assets/8f69c8a7-28cd-4d42-892d-eb32e9139a73" />

18. watsonx Orchestarate Explorerから finance_agent を見つけ、<img width="20" height="22" alt="chat-icon" src="https://github.com/user-attachments/assets/c0d9886c-8521-4c1b-ba56-7dcc3879fd10" /> をクリックします。

19. [企業情報エージェント]のチャット欄に質問を入力します。finance_agentがyfinance_toolsを使って、株価を取得し、結果を表示します。

```
本日のIBMの株価は？
```
<img width="1198" height="959" alt="IBMStockPrice" src="https://github.com/user-attachments/assets/e567162c-8d66-480c-ba94-ced13c1b01ee" />

* もし、yfinanceのエラーが発生している場合、ツールのインポートがうまく行ってない可能性があります。手順11から確認してください。


##

以上、AIエージェントにPythonで作ったツールを連携させる方法を体験しました。ぜひ、皆さんも必要な情報を取得するツールを作り、AIエージェントから呼び出しを行いましょう。

