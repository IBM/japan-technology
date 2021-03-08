---
type: default
draft: false
title: "機械学習アルゴリズムのトレーニングを高速化する"
subtitle: "IBM PowerAI 上で Google TensorFlow を使用して、機械学習アルゴリズムを迅速にトレーニングする"
excerpt: "Nimbix による PowerAI 仮想化ソフトウェアを使用して迅速に機械学習アルゴリズムをトレーニングする方法を開発者向けに説明します。"
authors:
- name: "Rich Hagarty"
  email: "Rich.Hagarty@ibm.com"
- name:  "Scott DAngelo"
  email: "Scott.DAngelo@ibm.com"
- name: "Franck Barillaud"
  email: "fbarilla@us.ibm.com"
completed_date: "2017-05-15"
last_updated: "2017-05-16"
meta_title: "機械学習アルゴリズムのトレーニングを高速化する"
meta_description: "IBM PowerAI 上で Google TensorFlow を使用して、機械学習アルゴリズムを迅速にトレーニングする"
meta_keywords: "machine learning, create machine learning application, machine learning tensorflow"

pwg:
 - "power ai"
pta:
 - "cognitive, data, and analytics"
github:
- url: "https://github.com/IBM/powerai-market-sentiment"
  button_title: "コードを入手する"

demo:
  - type: "youtube"
    url_or_id: "1nnWj6W7QJI"
    button_title: "デモをみる"
related_links:
  - title: "Putting the 'AI' in PowerAI"
    url: "https://www.ibm.com/blogs/research/2016/11/powerai/"
    description: "IBM's latest Power servers, the world's fastest deep learning servers, come with an AI twist. Learn more."
  - title: "PowerAI Now Includes Newly Announced TensorFlow 1.0"
    url: "https://www.ibm.com/developerworks/community/blogs/fe313521-2e95-46f2-817d-44a4f27eba32/entry/PowerAI_Now_Includes_Newly_Announced_TensorFlow_1_0?lang=en"
    description: "As the TensorFlow ecosystem grows, IBM brings its features to PowerAI to give deep-learning developers a high-performance turnkey system."
  - title: "Cognitive for intelligence and insights from data"
    url: "https://www.ibm.com/cloud/garage/architectures/cognitiveArchitecture"
    description: "Unlock new intelligence from vast quantities of structured and unstructured data and  develop deep, predictive insights."

# related_content:        # OPTIONAL - Note: zero or more related content
#   - type: announcements|articles|blogs|patterns|series|tutorials|videos
#     slug:

# social-media-meta:
#   - type: twitter
#     title:
#     abstract:
#     img:
#    - height:
#      width:
#      src:

primary_tag: "artificial-intelligence"

tags:
  - "analytics"
  - "systems"
  - "machine-learning"
  - "data-science"
  - "deep-learning"

# service-id:
services:
  - "natural-language-understanding"
components:
  - "ibm-power-ai"
  - "jupyter"
runtimes:
  - "community-buildpacks"
---
## 概要

このコード・パターンでは、Nimbix による PowerAI 仮想化ソフトウェアを使用して迅速に機械学習アルゴリズムをトレーニングする方法を開発者向けに説明します。NVIDIA GPU と CUDA 並列コンピューティング・プラットフォームを使用して教師なし機械学習の繰り返し処理を実行すると、Power 以外のアーキテクチャーよりも処理を高速化できるようになります。

## 説明

このコード・パターンは、機械学習のスピードアップを目指すあらゆる開発者を対象に、IBM の新しい機械学習向けプラットフォーム、PowerAI を利用する方法を説明します。IBM Power8&reg; システム上で時系列データの機械学習を行う例を紹介するために、Jupyter Notebook を使用します。このノートブックでフォーカスするのは、再生可能エネルギー分野における将来の金融市場価格の予測可能性を評価することです。そのために、関連する市場と、*The New York Times* のニュース記事内から検出されたセンチメントを調べます。

このコード・パターンをひととおり完了すると、以下の方法がわかるようになります。

* 各種の外部リソースから構造化データを抽出してフォーマット化する
* 非構造化データを抽出してフォーマット化し、IBM Watson&trade; のコグニティブ・サービスを利用してデータのセンチメントを分析する
* ニューラル・ネットワークを作成してトレーニングする
* Jupyter Notebook 内で結果を表示して共有する

このコード・パターンは、強力な深層学習アプリケーションを効率的に作成して機械学習を加速化させるというニーズを持つ開発者に役立つはずです。また、データ・サイエンスの経験が限られている開発者にも理想的な学習機会になります。

## フロー

![フロー](../../images/tensorflow-arch.png)

1. 開発者が、用意されているノートブックをロードします。このノートブックは PowerAI システム上で稼働します。
2. 実行中のノートブックは *The New York Times* からのデータと市場データを使用します。
3. ノートブックが IBM Watson Natural Language Understanding サービスを利用してテキストを分析します。
4. ノートブックが TensorFlow と機械学習を使用してモデルを発展させ、予測を立てます。
