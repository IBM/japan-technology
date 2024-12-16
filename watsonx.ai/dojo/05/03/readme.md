# InstructLab CLI体験

このハンズオンでは、InstructLabの主な機能を体験していきます。公式文書はこちら。
* 注意事項: GPUの機能が使えないコンピューターにおいて、データの生成や学習の実行はかなりの時間を要します。
* 体験を目的としてコマンドの実行方法は示しますが、本当に実行するかどうかについては、ご自身で判断してください。
* コマンドは、InstructLab CLIをインストール済みのUbuntuまたはターミナル上で操作してください。

## 全体像
![ilab](https://github.com/user-attachments/assets/3edcea99-7b89-4225-a1a0-fcfceb456d07)

### 環境の初期化
* 公式文書は[こちら](https://github.com/instructlab/instructlab/tree/main?tab=readme-ov-file#%EF%B8%8F-initialize-ilab)
1. Python仮想環境 ilabが有効になっていることを確認します。
2. InstructLabの環境を初期化します。

ilab config init

3. ガイドに従って操作を進めます。。Enterキーを押すと、既定の値が設定されます。
* こちらは、Apple M3 Maxを搭載したmacの例です

----------------------------------------------------
         Welcome to the InstructLab CLI
  This guide will help you to setup your environment
----------------------------------------------------

Please provide the following values to initiate the environment [press 'Enter' for default options when prompted]

Path to taxonomy repo [/Users/<ユーザー名>/.local/share/instructlab/taxonomy]: Enter

Should I clone https://github.com/instructlab/taxonomy.git for you? [Y/n]: Y

Cloning https://github.com/instructlab/taxonomy.git...
Path to your model [/Users/<ユーザー名>/.cache/instructlab/models/granite-7b-lab-Q4_K_M.gguf]: Enter

Generating config file:
    /Users/<ユーザー名>/.config/instructlab/config.yaml

We have detected the APPLE M3 MAX profile as an exact match for your system.

--------------------------------------------
    Initialization completed successfully!
  You're ready to start using `ilab`. Enjoy!
--------------------------------------------

### 環境の初期化

