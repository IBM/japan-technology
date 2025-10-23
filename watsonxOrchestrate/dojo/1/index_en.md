# AI Agent Dojo #1

_Last updated: October 23, 2025_
* This is machine translated version.  The original contents is [here](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/index.md) in Japanese.
In this first session, you will build a generative AI agent—**watsonx Orchestrate**—designed to enhance enterprise productivity. Through hands-on exercises, you will create an AI agent that answers questions about IBM, register IBM’s 2024 financial information as knowledge, and learn how to use that knowledge as a tool from your AI Agent.

## Goals:
* Set up an environment for learning while running watsonx Orchestrate.
* Create an AI agent using the Agent Builder.
* Provide knowledge to the AI agent using the RAG (Retrieval-Augmented Generation) method with document files.
* Deploy the AI agent so it can be accessed via chat and other interfaces.

### Notes:
* This hands-on exercise uses the watsonx Orchestrate SaaS environment.
* The screenshots in this guide were taken shortly before the “last updated” date. Since SaaS products are updated frequently, the interface may differ slightly.
* The watsonx Orchestrate **Trial environment** is deployed on **Amazon Web Services** and provided free of charge by IBM. Therefore, no service-level guarantees are offered.
* The **IBM Technology Zone Trial** of watsonx Orchestrate is deployed on **IBM Cloud**. Usage conditions follow the [IBM Technology Zone Terms of Use](https://techzone.ibm.com/terms). It must not be used for production systems. Please also review the [Security Policy](https://techzone.ibm.com/terms/securitypolicy) before using it.
* Depending on the availability of computing resources in the watsonx Orchestrate evaluation environment, unexpected errors or unresponsive behavior may occur. If this happens, please wait and try again later.

## [Prepare the watsonx Orchestrate Environment](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/readme.md)
Prepare your watsonx Orchestrate environment. Once ready, proceed to Part 1 below.

## [watsonx Orchestrate AI Agent Experience – Part 1](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/01HelloAgent/readme1_en.md)

In this exercise, you will create an AI agent called **“IBMInfo”** that answers questions about IBM. You will configure its **Profile** and **Behavior**, and experience how to interact with the AI agent.

## [watsonx Orchestrate AI Agent Experience – Part 2](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/02RagAgent/readme2_en.md)

In this exercise, you will extend the **IBMInfo** agent created in Part 1 by adding knowledge using the **RAG (Retrieval-Augmented Generation)** method. By configuring the agent’s **Knowledge**, you will enable it to respond with corporate and financial information.

### Important Notes and Disclaimers
* IBM watsonx Orchestrate is a SaaS product and is updated regularly. The actual interface may differ from screenshots shown in this document.
* The AI agent combines a foundation model with tools and workflows to generate responses. Depending on internal reasoning, its responses may differ slightly from the examples in this guide.
* This hands-on guide is based on official watsonx Orchestrate training materials. The steps have been verified to work with the evaluation (trial) environment and use the English user interface.
* [Try building your own AI Agent](https://ibm.github.io/ba-handson-jp/wxoagent/agent/)
