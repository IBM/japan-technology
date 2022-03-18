---
abstract: Learn how to use a Watson Assistant chatbot with a Watson Discovery skill
also_found_in:
- learningpaths/get-started-watson-assistant/
authors: ''
completed_date: '2021-10-11'
components:
- watson-assistant
- watson-discovery
draft: false
excerpt: Use the Watson Discovery search skill to help users find information from
  within the dialog of a chatbot.
ignore_prod: false
meta_description: Use the Watson Discovery search skill to help users find information
  from within the dialog of a chatbot.
meta_keywords: assistant, chatbot, discovery, watson, learning path, getting started,
  beginner, conversation
meta_title: Add Watson Discovery skills to your Watson Assistant chatbot
primary_tag: artificial-intelligence
related_links:
- title: IBM Watson Assistant
  url: https://www.ibm.com/cloud/watson-assistant/
- title: Watson Assistant on IBM Developer
  url: https://developer.ibm.com/components/watson-assistant/
subtitle: Help users find information from within the dialog of a chatbot
tags:
- conversation
title: Add Watson Discovery skills to your Watson Assistant chatbot
type: tutorial
---

IBM Watson Assistant can help you solve a problem by providing an intelligent interface using natural language. The flexibilities of the GUI tools and APIs combine to let you power applications and tools simply and efficiently. After your assistant is published, you can easily embed it into a web page to allow your users to interact.

## Prerequisites

You need a published instance of [Watson Assistant](https://cloud.ibm.com/catalog/services/watson-assistant?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg). If you are following the [Watson Assistant learning path](https://developer.ibm.com/learningpaths/get-started-watson-assistant), then you already have this, but you can use any Assistant chatbot.

You also need an instance of [Watson Discovery](https://cloud.ibm.com/catalog/services/watson-discovery?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg). If you have completed the [Smart Document Understanding search skill](https://developer.ibm.com/learningpaths/get-started-watson-discovery/smart-document-understanding-search-skill/), you can use that skill. Otherwise, you can use one of the sample Discovery projects.

## Steps

### Add the Discovery skill to your chatbot

1. Launch your Assistant instance, and click **Integrations**.

    ![Click Integrations icon](images/click-integrations-tab.png)

1. Scroll down to the **Extensions** section, and click **Add +** under Search.

    ![Add search](images/add-search.png)

1. When the window opens, click **Confirm**.

1. On the **Search Integration** page, choose the Discovery instance that you want to use for this tutorial.

    ![Choose Discovery instance](images/choose-disco-instance.png)

1. Choose which project you want to use. Either choose the one that you created if you have completed the [Smart Document Understanding search skill](https://developer.ibm.com/learningpaths/get-started-watson-discovery/smart-document-understanding-search-skill/) tutorial, or choose **Sample project**.

    ![Choose Discovery project](images/choose-disco-project.png)

1. On the next screen, you can configure the result content. In this example, we removed the title and changed the display text. You can use the preview to test.

    ![Search integration configuration](images/search-integration-config.png)

1. Next, add an action for this search. Go back to the **Actions** tab, and click **New action +**.

    ![Add Action for Search](images/add-action-for-search.png)

1. Name the new action, then click **Save**.

    ![Name and Save new Action](images/new-action-name-and-save.png)

1. Under **Define customer response**, choose **Free text**.

    ![Define customer response as Free text](images/define-customer-repsonse.png)

1. Under **And then**, click **Search for the answer**.

    ![And then Search for the answer](images/and-then-search-for-answer.png)

1. You can click the **Preview** tab and test by entering the text `I'm having trouble with my thermostat`. When asked "What kind of issues are you having?", you can enter `How do I turn on the furnace?`. Note that you can add alternative ways of asking the question and the search skill answers the other questions as well.

    ![Use preview to test](images/use-preview-to-test.jpg)

1. If you are happy with the preview test, you can publish this new action by going to **Publish** and clicking **Publish**.

    ![Publish new action](images/publish-new-action.png)

1. Add a version description, and click **Publish**.

    ![Add version description](images/add-version-description.png)

1. The Search skill is still in draft mode, so you must return to the Integrations and open the search.

    ![Open Search Integration](images/integration-open-search.png)

1. Choose **Live** in the drop-down menu, and click **Confirm**.

    ![Choose Live and Confirm](images/open-search-choose-live.png)

1. If you have created a [deployed app with an embedded chatbot](/learningpaths/get-started-watson-assistant/embed-an-assistant-chatbot/), you can test the new search skill.

    ![Test chat in web page](images/deployed-app-with-chat.png)

1. The dialog can now use the search skill.

    ![Chat dialog with Search](images/chat-with-search.png)

## Conclusion

This tutorial showed how to integrate a Watson Discovery Search skill into a chatbot using the UI tooling in a few minutes. With this feature, the user can get additional information on a product or service without leaving the web chat environment.