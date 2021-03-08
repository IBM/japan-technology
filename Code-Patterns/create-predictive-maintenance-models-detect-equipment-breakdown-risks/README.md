# アプリケーション間でデータを同期し、機器のメンテナンスの必要を予測するモデルを作成する

### OSLC と Watson IoT ルールによる Maximo イベントのトリガー

English version: https://developer.ibm.com/patterns/create-predictive-maintenance-models-detect-equipment-breakdown-risks
  ソースコード: https://github.com/IBM/iotp-oslc

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2019-10-18

 ## 概要

このコード・パターンに従うと、標準的な OSLC API を使用して Watson IoT Platform と IBM Maximo EAM 内でアセットを作成する方法、アセットに対してクエリーを実行する方法、アセットを変更する方法を学べます。

## 説明

このコード・パターンでは、アセットのモニタリングと通知のトリガーを効率化するために Maximo と Watson IoT Platform を統合する方法を紹介します。

また、サービス間でやり取りする共通の方法として [OSLC (Open Services for Lifecycle Collaboration)](https://www.ibm.com/support/knowledgecenter/ja/SSYQBZ_9.5.0/com.ibm.help.common.oslc.doc/topics/c_oslc_overview.html) API を使用する方法も説明します。この使用ケースでは、この API を使用してサービス間でアセット・データを同期します。

さらに、[Watson IoT Platform 内の組み込みビジネス・ルール](https://www.ibm.com/support/knowledgecenter/ja/SSQP8H/iot/platform/reference/embeddedrules/rules_api.html)を使用して、ルールの条件に一致した時点でイベントをトリガーする方法も紹介します。例えば、アセットが正常に機能していない場合、問題に対処するために両方のサービス内で同時にアクションをトリガーできます。具体的には、自動化されたアクションによって IBM Maximo EAM 内で作業指示書を作成し、すべての関係者に SMS アラートを送信できます。

## フロー

![フロー](../../images/predictive-maintenance-oslc-iot-maximo.png)

1. Watson IoT Platform 用の OSLC ラッパーを作成してデプロイします。
1. IBM Maximo EAM と Watson IoT Platform にデバイスを登録するスクリプトを実行します。
1. Watson IoT Platform 内の組み込みルールを設定します。
1. センサー・データを Watson IoT Platform で受信すると、そのデータがルールに照合されて条件と一致するかどうかが確認されます。1 つ以上の条件と一致すると、対応するアクションが実行されます。

## 手順

このコード・パターンの技術的な詳細手順については、[README.md](https://github.com/IBM/iotp-oslc/blob/master/README.md) を参照してください。
