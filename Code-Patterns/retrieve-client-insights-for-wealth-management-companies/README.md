# 資産管理会社の顧客に関する洞察を引き出す

### Jupyter Notebook を使用して Client Insight for Wealth Management サービスについて探り、このサービスを利用する Web アプリケーションを作成する

English version: https://developer.ibm.com/patterns/retrieve-client-insights-for-wealth-management-companies
  ソースコード: https://github.com/IBM/client-insight-wealth-management

###### 最新の英語版コンテンツは上記URLを参照してください。
last_updated: 2019-03-28

 ## 概要

Client Insight for Wealth Management は、顧客満足度を向上させて顧客を維持できるよう、資産管理会社にクライアントに関する重要な洞察を提供するサービスです。API 呼び出しを使用してサービスを呼び出すと、特定の顧客に関する情報と、自然減スコアを示し、その特定の顧客の人生におけるイベントを予測するアナリティクスが返されます。このコード・パターンでは Jupyter Notebook とファイナンシャル・アドバイザー向けダッシュボードをデモする Web アプリケーションを使って、Client Insight for Wealth Management サービスを呼び出してデータを取得する例を紹介します。

## 説明

資産管理会社で働くファイナンシャル・アドバイザーの主な職務は、財産を管理するためのガイダンスと選択肢を顧客に提供することです。顧客と顧客の状況を理解していれば、ファイナンシャル・アドバイザーはさらにレベルの高いサービスを提供して顧客の保持率を上げられるようになります。Client Insight for Wealth Management サービスに用意されている一連の分析モデルは、ライフ・イベントの予測、顧客保持率を向上させるための自然減スコア、顧客の現状に関する情報といった重要な洞察を引き出します。

このコード・パターンは、開発者が Client Insights for Wealth Management サービスの機能を理解し、利用できるよう支援することを目的としています。開発者は Client Insights for Wealth Management サービスを利用することで、ファイナンシャル・アドバイザーが顧客にガイダンスを提供する際に使用する、洞察に溢れたダッシュボードを作成できます。

このコード・パターンでは、顧客データとアナリティクスを取得して表示するための Client Insights for Wealth Management サービスについて探ります。サービスから返されるアナリティクスには、自然減スコア、ライフ・イベントの予測、顧客の属性に基づく顧客のセグメント化が含まれます。こうしたデータは、資産管理会社がサービスを向上させて顧客を保持する上で役立つはずです。このコード・パターンではサービスの呼び出しと、サービスから返されるデータを理解するために、Jupyter Notebook 内で Client Insights for Wealth Management サービスをナビゲートします。取得したデータはダッシュボードに表示します。

このコード・パターンの対象読者は、金融サービスに興味を持つ開発者、またはカスタマー・サービスの強化を目指す開発者です。ここではサンプル API キーを利用して Client Insights for Wealth Management サービスからダミーの顧客データを取得しますが、実際の使用ケースでは顧客に関するデータは金融機関から取得します。

このコード・パターンを完了すると、以下の方法がわかるようになります。

* Client Insight for Wealth Management (CIWM) サービスから顧客に関する洞察を取得する
* Jupyter Notebook を通してサービスの利用方法を理解する
* 顧客に関する洞察を表示するダッシュボードを備えた Web アプリケーションを作成する

## フロー

![フロー](../../images/wealth-management-architecture.png)

1. ユーザーが Web インターフェースからアプリケーションにアクセスし、顧客のプロファイルを表示します。
1. アプリケーションが Client Insight for Wealth Management サービスから顧客の情報とアナリティクスを取得します。
1. Jupyter Notebook を探索して Client Insight for Wealth Management サービスの使用ケースを理解します。
1. ユーザーが Jupyter Notebook を使用して Client Insight for Wealth Management サービスを呼び出します。

## 手順

このパターンの詳細な手順については、[README](https://github.com/IBM/client-insight-wealth-management) を参照してください。手順で説明する方法は以下のとおりです。

1. リポジトリーを複製します。
1. Jupyter Notebook 内を探索します。
1. アプリケーションを実行します。
