# Jupyter Notebook を使用して Starcraft II リプレイを分析する

### Data Science Experience を利用して Starcraft II リプレイのデータ視覚化を作成する

English version: https://developer.ibm.com/patterns/analyze-starcraft-ii-replays-with-jupyter-notebooks
ソースコード: https://github.com/IBM/starcraft2-replay-analysis/

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2017-05-19

 
## 概要

私たちが Starcraft II ファンのために作成したこのコードでは、実際にゲームに改善を加えることができます。このコード・パターンは、リプレイ分析によって興味深い洞察を見つけたいと思っている開発者にとっても、ゲームのスキル向上を目指すプロのプレイヤーにとっても、目標達成に役立つはずです。IBM Watson Studio の機能を利用し、Jupyter Notebook を使用してデータ視覚化を作成する方法を学び、Starcraft II のデータを分析できるようになってください。

## 説明

Starcraft II は、世界中で 240,000 人の熱烈なファンがプレイしているリアルタイム・ストラテジー・ビデオ・ゲームです。ゲーマーのストラテジーを競い合う数々のコンテストも開催されています。この開発者コード・パターンでは、Jupyter Notebook を使って StarCraft II のリプレイを分析し、プレイヤーのアクティビティーに基づくデータ視覚化を作成して、勝者と敗者に関する興味深い洞察を引き出します。

このコード・パターンをひと通り完了すると、以下の方法がわかるようになります。

* IBM Watson&trade; Studio 内で Jupyter Notebook を作成して実行する
* Watson Studio Object Storage を利用してリプレイ・データにアクセスする
* sc2reader を使用してリプレイを Python オブジェクトにロードする
* 結果に含まれている基本的なリプレイ情報を調査する
* 対戦の詳細を有用なオブジェクトに解析する
* Bokeh グラフを使用して対戦内容を視覚化する
* 処理したリプレイを Cloudant&reg; 内に保管する


## フロー

![フロー](../../images/Starcraft-Journey.png)

1. 用意されているノートブックを IBM Watson Studio プラットフォームにロードします。
2. Starcraft II のリプレイが IBM Cloud Object Storage にロードされます。
3. ノートブックが IBM Cloud Object Storage からリプレイをプルして分析します。
4. ノートブックが Cloudant NoSQL データベースを使用して結果と分析を保管します。

## 手順

このコード・パターンに取り組む準備はできましたか？アプリケーションを起動して使用する方法について詳しくは [README](https://github.com/IBM/starcraft2-replay-analysis/blob/master/README.md) を参照してください。
