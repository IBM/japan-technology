---
abstract: Watson Discoveryスキルを使ったWatson Assistantチャットボットの使い方をご紹介します。
also_found_in:
- learningpaths/get-started-watson-assistant/
authors: ''
completed_date: '2021-10-11'
components:
- watson-assistant
- watson-discovery
draft: false
excerpt: 検索スキル「Watson Discovery」を使って、ユーザーがチャットボットのダイアログ内から情報を見つけられるようにします。
ignore_prod: false
meta_description: 検索スキル「Watson Discovery」を使って、ユーザーがチャットボットのダイアログ内から情報を見つけられるようにします。
meta_keywords: assistant, chatbot, discovery, watson, learning path, getting started,
  beginner, conversation
meta_title: Watson AssistantのチャットボットにWatson Discoveryのスキルを追加する
primary_tag: artificial-intelligence
related_links:
- title: IBM Watson Assistant
  url: https://www.ibm.com/cloud/watson-assistant/
- title: Watson Assistant on IBM Developer
  url: https://developer.ibm.com/components/watson-assistant/
subtitle: チャットボットのダイアログ内でユーザーが情報を見つけられるようにする
tags:
- conversation
title: Watson AssistantのチャットボットにWatson Discoveryのスキルを追加する
type: tutorial
---

IBM Watson Assistantは、自然言語を用いたインテリジェントなインターフェースを提供することで、問題解決を支援します。GUI ツールと API の柔軟性を組み合わせることで、アプリケーションやツールをシンプルかつ効率的に強化することができます。アシスタントを公開した後は、簡単に Web ページに埋め込んで、ユーザーが対話できるようにすることができます。

## 前提条件

[Watson Assistant](https://cloud.ibm.com/catalog/services/watson-assistant?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)の公開されたインスタンスが必要です。[Watson Assistant ラーニングパス](https://developer.ibm.com/learningpaths/get-started-watson-assistant) に従っている場合はすでに持っていますが、どの Assistant チャットボットでも使用できます。

また、[Watson Discovery](https://cloud.ibm.com/catalog/services/watson-discovery?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg)のインスタンスも必要です。[スマートドキュメント理解検索スキル](https://developer.ibm.com/learningpaths/get-started-watson-discovery/smart-document-understanding-search-skill/)を完了している場合は、そのスキルを使用できます。それ以外の場合は、Discoveryプロジェクトのサンプルの1つを使用できます。

## ステップ

### チャットボットにディスカバリースキルを追加する

1. アシスタントのインスタンスを起動し、**統合**をクリックします。

    ![統合アイコンをクリック](images/click-integrations-tab.png)

1. **拡張機能**セクションまでスクロールダウンして、検索の下にある**Add +**をクリックします。

    ![検索の追加](images/add-search.png)をクリックします。

1. ウィンドウが開いたら、「**Confirm**」をクリックします。

1. **Search Integration**ページで、このチュートリアルで使用するDiscoveryインスタンスを選択します。

    ![Choose Discovery instance](images/choose-disco-instance.png)をクリックします。

1. 使用したいプロジェクトを選択します。チュートリアルの[スマートドキュメント理解検索スキル](https://developer.ibm.com/learningpaths/get-started-watson-discovery/smart-document-understanding-search-skill/)を完了している場合は自分で作成したものを選ぶか、**サンプルプロジェクト**を選びます。

    ![ディスカバリープロジェクトを選択](images/choose-disco-project.png)

1. 次の画面では、結果の内容を設定することができます。この例では、タイトルを削除し、表示テキストを変更しました。プレビューを使ってテストすることができます。

    ![検索統合設定](images/search-integration-config.png)

1. 次に、この検索のアクションを追加します。**Actions**タブに戻り、**New action +**をクリックします。

    ![検索用アクションの追加](images/add-action-for-search.png)

1. 新しいアクションに名前を付けて、**Save**をクリックします。

    ![新規アクションの名前と保存](images/new-action-name-and-save.png)

1. **Define customer response**で、**Free text**を選択します。

    ![Define customer response as Free text](images/define-customer-repsonse.png)

1. **And then**の下で、**Search for the answer**をクリックします。

    ![And then Search for the answer](images/and-then-search-for-answer.png)をクリックします。

1. **プレビュー**タブをクリックして、テキスト`I'm having trouble with my thermostat`を入力してテストすることができます。と聞かれたら、「How do I turn on the furnace?」と入力してください。なお、質問の別の方法を追加することができ、検索スキルは他の質問にも答えてくれます。

    ![プレビューを使用してテスト](images/use-preview-to-test.jpg)

1. プレビューテストに問題がなければ、**公開**にアクセスして**公開**をクリックすることで、この新しいアクションを公開できます。

    ![Publish new action](images/publish-new-action.png)

1. バージョンの説明を追加して、**Publish**をクリックします。

    ![Add version description](images/add-version-description.png)

1. 検索スキルはまだドラフトモードなので、Integrationsに戻って検索を開く必要があります。

    ![検索統合を開く](images/integration-open-search.png)

1. ドロップダウンメニューで **Live** を選択し、**Confirm** をクリックします。

    ![Choose Live and Confirm](images/open-search-choose-live.png)

1. [チャットボットを組み込んだデプロイ済みのアプリ](/learningpaths/get-started-watson-assistant/embed-an-assistant-chatbot/)を作成している場合は、新しい検索スキルをテストできます。

    ![Test chat in web page](images/deployed-app-with-chat.png)

1. ダイアログで検索スキルが使えるようになりました。

    ![検索付きチャットダイアログ](images/chat-with-search.png)

## 結論

このチュートリアルでは、UI ツールを使用して Watson Discovery Search スキルをチャットボットに数分で統合する方法を紹介しました。この機能を使えば、ユーザーはウェブチャット環境を離れることなく、製品やサービスに関する追加情報を得ることができます。