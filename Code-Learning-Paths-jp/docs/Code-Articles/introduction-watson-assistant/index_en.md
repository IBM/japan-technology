---
also_found_in:
- learningpaths/get-started-watson-assistant/
authors: ''
completed_date: '2019-08-06'
components:
- watson-assistant
display_in_listing: true
draft: false
excerpt: Get an overview of Watson Assistant, and learn how it can help you use the
  power of AI to connect customers to service resources, keep them engaged, and solve
  their problems.
last_updated: '2021-10-04'
meta_description: Get an overview of Watson Assistant, and learn how it can help you
  use the power of AI to connect customers to service resources, keep them engaged,
  and solve their problems.
meta_keywords: assistant, chatbot, watson, learning path, getting started, beginner,
  conversation, watson assistant
meta_title: Introduction to Watson Assistant
primary_tag: artificial-intelligence
related_links:
- title: IBM Watson Assistant
  url: https://www.ibm.com/cloud/watson-assistant/
- title: Watson Assistant on IBM Developer
  url: https://developer.ibm.com/components/watson-assistant/
subtitle: Learn the basics of the Watson Assistant Service
tags:
- conversation
- machine-learning
- deep-learning
title: Introduction to Watson Assistant
---

## Overview

IBM Watson Assistant is an AI-powered virtual agent that provides customers with fast, consistent, and accurate answers across any messaging platform, application, device, or channel. Using AI and natural language processing, Watson Assistant learns from customer conversations, improving its ability to resolve issues the first time while removing the frustration of long wait times, tedious searches, and unhelpful chatbots.

With Watson Assistant, you can build conversational interfaces into any application, device, or channel. Most virtual assistants try to mimic human interactions, but Watson Assistant knows when to search for an answer from a knowledge base, when to ask for clarity, and when to direct someone to a human. Like a human personal assistant, the assistant you build helps your customers perform tasks and answer questions. To accomplish this, you define actions for the assistant.

An action represents a discrete outcome that you want your assistant to be able to accomplish in response to a user's request. An action comprises the interaction between a customer and the assistant about a particular question or request. This interaction begins with the user input that starts the action (for example, I want to withdraw money). It might then include additional exchanges as the assistant gathers more information, and it ends when the assistant carries out the request or answers the customer's question.

Here's a video to introduce Watson Assistant.

<iframe src="https://player.vimeo.com/video/590052149?h=05c4576022" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
<p><a href="https://vimeo.com/590052149">IBM Watson Assistant solves customer problems the first time</a> from <a href="https://vimeo.com/watsonassistant">Watson Assistant</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

## Why use Watson Assistant?

Virtual assistants, or chatbots, go far beyond the gimmicky approach that they are often associated with. You can use bots to set appointments, call a car, and so on. It's not a replacement for search. Amazon Echo and Google Home are excellent examples of virtual assistants. There is no interface, so having a well-structured dialog to talk through is essential.

A couple of instances of where Watson Assistant excels are customer self-service and employee self-service. Watson Assistant:

* Knows when to provide a direct answer to a common question or reference more generalized search results for something more complex
* Hands off the issue to a human agent when it's something the virtual assistant can't handle. The new (after October 8, 2021) Watson Assistant instance integrates seamlessly with Genesys, Nice inContact, Twilio, or your own agent.
* Integrates with a phone number to let the user talk to the assistant. Watson Assistant generates a phone number or integrates with an existing SIP provider such as IntelePeer, Genesys, or Twilio.
* Integrates directly with end-channels such as Slack or Facebook Messenger so that you can handle requests wherever it is most convenient for your users
* Stores data within user interactions that can be used to guide and personalize the experience over time

## Architecture

The following figure shows Watson Assistant architecture that's common for all implementations. In this architecture:

* Users interact with the assistant through one or more of these integration points:

    * A web chat code snippet that runs in your existing website

    * A virtual assistant that you publish directly to an existing third-party messaging platform, such as WhatsApp with Twilio, Slack, or Facebook Messenger

    * A voice assistant that the user accesses over the phone

    * A custom application that you develop, such as a mobile app or a robot with a voice interface

* The assistant receives user input and routes it to the dialog skill.

* The dialog skill interprets the user input further, then directs the flow of the conversation. The dialog gathers any information it needs to respond or perform a transaction on the user's behalf.

* Any questions that cannot be answered by the dialog skill are sent to the search skill, which finds relevant answers by searching the company knowledge bases that you configure for the purpose.

![Assistant architecture](https://cloud.ibm.com/docs-content/v1/content/07a736e5918d8c2d1dca127f22a26923060e7653/services/assistant/images/arch-overview-search.png)

*A typical approach used when deploying Watson Assistant*

## Terms

This section covers the terms that you need to know as you follow the learning path to use Watson Assistant in your applications.

| Term | Definition |
| ---  |   ---      |
| [Assistant](https://cloud.ibm.com/docs/services/assistant?topic=assistant-assistants) | Directs requests down the optimal path for solving a customer problem. Add skills so that your assistant can provide a direct answer to a common question or reference more generalized search results for something more complex. |
| Action | Comprises the interaction between a customer and the assistant about a particular question or request. |
| Step | In an action, defines the conversation turns that follow the initial customer input that triggered the action. |
| [Web chat](https://cloud.ibm.com/docs/assistant?topic=assistant-web-chat-basics) | Web chat is a code snippet that you can immediately embed in your website. |
| [Phone integration](https://cloud.ibm.com/docs/assistant?topic=assistant-deploy-phone) | A working phone number that is automatically connected to your assistant. Or, if you prefer, you can connect the assistant to your existing infrastructure by configuring an existing Session Initiation Protocol (SIP). |

## Where is Watson Assistant available?

Watson Assistant is available in both the public and private cloud.

* **Public Cloud**: Watson Assistant is available on [IBM Cloud](https://cloud.ibm.com/catalog/services/watson-assistant?cm_sp=ibmdev-_-developer-articles-_-cloudreg). The Watson Assistant ["Getting started tutorial"](https://cloud.ibm.com/docs/services/assistant?topic=assistant-getting-started) provides additional information on setting up the service.

* **Private Cloud**: Watson Assistant is also available through IBM Private Cloud, on premises or managed, with [IBM Cloud Pak for Data](https://www.ibm.com/products/cloud-pak-for-data).

## SDKs

There are several SDKs available that support the various AI services. They are not limited to the following list.

* [Node SDK](https://github.com/watson-developer-cloud/node-sdk)
* [Python SDK](https://github.com/watson-developer-cloud/python-sdk)
* [Swift SDK](https://github.com/watson-developer-cloud/swift-sdk)
* [Java SDK](https://github.com/watson-developer-cloud/java-sdk)
* [Go SDK](https://github.com/watson-developer-cloud/go-sdk)
* [Ruby SDK](https://github.com/watson-developer-cloud/ruby-sdk)
* [.NET SDK](https://github.com/watson-developer-cloud/dotnet-standard-sdk)
* [Salesforce SDK](https://github.com/watson-developer-cloud/salesforce-sdk)

## APIs

The [Watson Assistant V1 API](https://cloud.ibm.com/apidocs/assistant) is available to help you get started, but we recommend using  the [Watson Assistant V2 API](https://cloud.ibm.com/apidocs/assistant-v2) with your apps.

## Conclusion

This article gave you an introduction to Watson Assistant. It provided an overview of the service, and explained its architecture as well as it terms and concepts. To get a high-level look at Watson Assistant including features and pricing, see the <a href="https://www.ibm.com/cloud/watson-assistant/" target="_blank" rel="noopener noreferrer">Watson Assistant product page</a>.