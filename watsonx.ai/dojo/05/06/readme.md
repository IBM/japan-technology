# InstructLab CLI体験その4 (学習用の合成データの作成、モデルの学習）
このハンズオンは、オプション扱いです。

内容としては、InstructLabの学習データの生成、モデルの学習を体験していきます。

* 前提条件: [InstructLab CLI体験その3](https://github.com/IBM/japan-technology/blob/main/watsonx.ai/dojo/05/05/readme.md)が完了していること
* 注意事項: GPUの機能が使えないコンピューターにおいて、データの生成や学習の実行はかなりの時間を要します。
* 体験を目的としてコマンドの実行方法は示しますが、本当に実行するかどうかについては、ご自身で判断してください。
* コマンドは、InstructLab CLIをインストール済みのUbuntuまたはターミナル上で操作してください。

## 全体像
![ilab](https://github.com/user-attachments/assets/3edcea99-7b89-4225-a1a0-fcfceb456d07)

### 学習データの生成
* 公式文書は[こちら](https://github.com/instructlab/instructlab?tab=readme-ov-file#-generate-a-synthetic-dataset)

1. Pythonのienv仮想環境が起動していない場合は、次のコマンドを入力します。
* 重複して実行しても問題ありません
```
cd ~/wxai
source ienv/bin/activate
```

2. 更新されたTaxonomyを利用して、合成データを作成します。
```
ilab data generate
```

3. 作成されたデータセットを確認します。
```
ilab data list
```

出力例:
```
mistral-7b-instruct-v0.2.Q4_K_M 2024-12-17 13:59:03
+-----------------------------------------------------------------------------------+---------------------+-----------+
| Dataset                                                                           | Created At          | File size |
+-----------------------------------------------------------------------------------+---------------------+-----------+
| messages_mistral-7b-instruct-v0.2.Q4_K_M_2024-12-17T13_59_03.jsonl                | 2024-12-17 14:11:29 | 6.10 KB   |
| node_datasets_2024-12-17T13_59_03/compositional_skills_linguistics_synonyms.jsonl | 2024-12-17 14:11:29 | 10.99 KB  |
| skills_train_msgs_2024-12-17T13_59_03.jsonl                                       | 2024-12-17 14:11:34 | 43.52 KB  |
| test_mistral-7b-instruct-v0.2.Q4_K_M_2024-12-17T13_59_03.jsonl                    | 2024-12-17 13:59:04 | 3.26 KB   |
| train_mistral-7b-instruct-v0.2.Q4_K_M_2024-12-17T13_59_03.jsonl                   | 2024-12-17 14:11:29 | 5.51 KB   |
+-----------------------------------------------------------------------------------+---------------------+-----------+
```

### 学習の実行
1. granite-7b-labモデルをダウンロードします。公式文書は[こちら](https://github.com/instructlab/instructlab?tab=readme-ov-file#-before-you-begin-training)。

```
ilab model download --repository instructlab/granite-7b-lab
```
2. 作成された合成データを利用して学習を実行します。
* skills_train_msgs_2024-12-17T13_59_03.jsonl のファイル名はデータセット一覧で表示されているものに置き換えてください。

GPU機能が使えないデバイスの場合
```
ilab model train --pipeline full --device cpu --data-path ~/.local/share/instructlab/datasets/skills_train_msgs_2024-12-17T13_59_03.jsonl
```

Apple M1/M2/M3/M4プロセッサを搭載しているデバイスの場合
```
ilab model train --pipeline full --device mps --data-path ~/.local/share/instructlab/datasets/skills_train_msgs_2024-12-17T13_59_03.jsonl
```
