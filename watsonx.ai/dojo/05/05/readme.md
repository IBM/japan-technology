# InstructLab CLI体験その3 (Taxonomyの確認とデータ変更)

このハンズオンでは、InstructLabの主な機能を体験していきます。公式文書はこちら。
* コマンドは、InstructLab CLIをインストール済みのUbuntuまたはターミナル上で操作してください。
* Visual Studio Codeがインストールされていると想定しています。

## 全体像
![ilab](https://github.com/user-attachments/assets/3edcea99-7b89-4225-a1a0-fcfceb456d07)

### taxonomyフォルダーの確認

1. Taxnomyが格納されているフォルダーをVisual Studio Codeで開きます。
```
cd ~/wxai
code ../.local/share/instructlab/taxonomy
```
* このフォルダーは信頼できるフォルダーとして取り扱ってください

2. Visual Studio Codeの拡張機能 (Extension) から Trailing Spaceをインストールします。
* YAMLファイル内の行末に不要な空白文字列が入っているのを見つけやすくなります。
<img width="2168" alt="Install-TrailingSpaces" src="https://github.com/user-attachments/assets/08b8d5c4-661d-4ee2-9acf-64b7d1d9a6a5" />

インストールが完了している状態:
<img width="2168" alt="TrailingSpaces" src="https://github.com/user-attachments/assets/30e73bc9-a235-469c-838f-5d653f10ed45" />

3. Visual Studio Codeを使い、Taxonomyが格納されているフォルダー内の構造を確認します。
<img width="426" alt="Taxonomy-Folder" src="https://github.com/user-attachments/assets/a3daf517-9b56-41f9-b866-b2ba78bd3993" />

### taxonomyフォルダー内のファイルの変更

1. Visual Studio CodeのExploreを使い、
taxonomy>compositional_skills>linguistics>synonyms>qna.yaml を開きます。

あるいは、次のコマンドで開きます。
```
code ../.local/share/instructlab/taxonomy/compositional_skills/linguistics/synonyms/qna.yaml
```
2. Visual Studio Codeを使って、qna.yamlの内容を確認します。
<img width="2104" alt="synonyums-qanda-yaml" src="https://github.com/user-attachments/assets/a729e947-8c02-4178-b5d5-bd88c1f0d551" />

3. ショートカットキーを使い、ファイル内の置換機能を呼び出します。

Ubuntuの場合: [Ctrl]+[Shift]+[H]
Macの場合: [Shift]+[Command]+[H]

4.  "take part in" を "sit in on" に置き換えます。
<img width="2104" alt="replace" src="https://github.com/user-attachments/assets/0b5f786a-4f26-4544-9789-69257c726455" />

5. ショートカットキーを使い、一括置換 (Replace All)を実行します。

Ubuntuの場合: [Ctrl]+[Alt]+[Enter]
Macの場合: [Option]+[Command]+[Enter]

6. 確認のダイアログ・ウィンドウが表示されるので、[Replace]をクリックします。

<img width="2104" alt="Okay-to-replace" src="https://github.com/user-attachments/assets/d2c3e13e-03ca-4de6-a004-e7e1b72b91c8" />

7. ファイルを保存します。
   

8. 次のコマンドを実行して、taxonomyフォルダー内の変更を確認します。

```
ilab taxonomy diff
```

出力例:
```
compositional_skills/linguistics/synonyms/qna.yaml
Taxonomy in /home/ilab/.local/share/instructlab/taxonomy is valid :)
```

* 通常はTaxonomyフォルダー内に独自の知識やスキルを定義していきますが、このハンズオンでは、Taxonomyフォルダー内のファイルを一部修正することで、変更を確認するという体験に留めています。

* Taxonomyについて、詳しく知りたい方は、[こちら](https://github.com/instructlab/taxonomy?tab=readme-ov-file#instructlab--taxonomy)の文書を読んでください。 
