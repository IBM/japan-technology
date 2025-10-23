# watsonx Orchestrate AI Agent Experience – Part 1

_Last updated: September 24, 2025_

In this exercise, you will create an AI agent named **IBMInfo** that can answer questions about IBM. Let’s explore the basics of building and interacting with an AI agent.

* Setting up the **Profile**
* Setting up the **Behavior**

> **Note:** In this exercise, the AI agent uses generative AI to produce responses. Since generative AI generates text probabilistically, the answers may differ from those shown in the screenshots.  
> If the generation does not stop, click the **Reset** button <img width="31" height="33" alt="Preview-Reset" src="https://github.com/user-attachments/assets/e838f4b9-767b-4120-9396-0f8f631d6f06" /> in the Preview window.

---

## Hands-On Exercise

### 1. Open watsonx Orchestrate

URLs:  
* Free Trial (Singapore): https://ap-southeast-1.dl.watson-orchestrate.ibm.com/chat  
* TechZone (Dallas): https://us-south.watson-orchestrate.cloud.ibm.com/chat  
* Open watsonx Orchestrate according to your environment.

   <img width="1136" height="1030" alt="01wxoChat" src="https://github.com/user-attachments/assets/5f012966-bb2c-45f0-9a0f-b53798c00d02" />


### 2. Click **Build** from the upper-left menu and select **Agent Builder**.

<img width="250" height="259" alt="02MenuAgentBuilder" src="https://github.com/user-attachments/assets/b57b7c9d-9f26-4c55-8a3c-d03e0c282528" />

### 3. On the right-hand side, click **Create agent +**.

<img width="1136" height="1030" alt="03CreateAgent" src="https://github.com/user-attachments/assets/552cc1e2-fd36-4d6d-8dc3-84d64eda281d" />

### 4. In the “Create an agent” window, select **Create from scratch**.

<img width="1136" height="1030" alt="04CreateFromScratch" src="https://github.com/user-attachments/assets/d5dbcf14-f0af-4641-a157-25e3562c7f74" />

### 5. Name your AI agent “IBMInfo,” since it will answer questions about IBM.  
* **Name:** 
```
IBMInfo
```

<img width="1136" height="1030" alt="05AgentName" src="https://github.com/user-attachments/assets/92ee17e7-67aa-44a2-bf6c-2ca36a33dc26" />

### 6. Add a description for your AI agent. The description helps watsonx Orchestrate determine which agent to invoke, so be specific.  
* **Description:** 
```
An agent that answers questions about IBM company information.
```

* Once you’ve entered the description, click **Create**.

### 7. Confirm that your AI agent has been created. If an error occurs, try using a different name.

<img width="1136" height="1030" alt="07AgentCreated" src="https://github.com/user-attachments/assets/76bf6bc8-c4f9-4a99-ae43-624b55404ca4" />

### 8. Test your newly created AI agent. In the **Preview** panel on the right, enter a question.  
* **Input:** 
```
What is IBM?
```
<img width="409" height="734" alt="08Q1WhatIsIBM" src="https://github.com/user-attachments/assets/1a282d37-4569-4446-9fe5-4a9c35930eb6" />

After a few moments, the agent will respond using the foundation model **llama-3-2-90b-vision-instruct**.

<img width="406" height="362" alt="09A1IBMis" src="https://github.com/user-attachments/assets/ae43888d-e1fc-4d4e-8afb-54d4c510fc66" />

### 9. Try another question.  
* **Input:** 
```
What is IBM’s stock price in dollars?
```
<img width="395" height="58" alt="10Q2StockPrice" src="https://github.com/user-attachments/assets/d0d23ccc-e033-4d88-a9c5-8d8b1f756c56" />

After a short wait, the AI agent will respond. In both cases, it will indicate that it needs an external tool to retrieve the information, but since no tool is configured, the correct data won’t appear.

> If generation doesn’t stop, click **Reset**<img width="31" height="33" alt="Preview-Reset" src="https://github.com/user-attachments/assets/e838f4b9-767b-4120-9396-0f8f631d6f06" /> in the Preview panel, skip Steps 12–13, and proceed to Step 14.

* **Example Output 1:** A general description about IBM’s stock.  
<img width="391" height="277" alt="11A2StockPrice" src="https://github.com/user-attachments/assets/224a5fd4-b6c4-4c0b-8219-641e5e5089ae" />

* **Example Output 2:** Another variation in generated responses.
<img width="349" height="637" alt="11-02A2StockPrice" src="https://github.com/user-attachments/assets/a27c7b63-fcdf-4872-a7a4-0eaf6257e657" />


### 10. Provide the keyword **NYSE** (New York Stock Exchange) to inform the AI agent where IBM’s stock is traded.  
* **Input:** 
```
NYSE
```

<img width="392" height="76" alt="12Q3NYSE" src="https://github.com/user-attachments/assets/0dc50a79-7424-4915-8ae6-db4386453d0a" />


The AI agent will attempt to call a tool to fetch the stock price but will fail because no proper tool is defined. This behavior is expected — it shows how the AI agent tries to use external tools to find missing contextual data.

> For reference, if you run the same inference directly on watsonx.ai, it won’t attempt to call tools — it will simply generate a text-based response.
<img width="1256" height="705" alt="13-02-wxaiLLM" src="https://github.com/user-attachments/assets/91987539-9be8-489d-98dc-0872d1e42433" />

### 11. Define the agent’s behavior. Click **Behavior** on the left-hand side.
<img width="1136" height="1030" alt="14Behavior" src="https://github.com/user-attachments/assets/3eb3f867-ca05-402a-8e86-aa0a4fb39376" />

### 12. In the **Instructions** field, describe how you want the AI agent to behave.

* **Instructions:**  
```
Answer using the same natural language as the question. If the question is in Japanese, answer in Japanese. If it’s in English, answer in English.  
If you lack the necessary knowledge or context to answer, respond with: ‘I cannot answer accurately due to insufficient information.
```

<img width="373" height="329" alt="15SetBehavior" src="https://github.com/user-attachments/assets/5e12a344-e4de-4dd3-8652-a21789f0b074" />

### 13. After configuring the behavior, return to the Preview panel and ask again:  
* **Input:** `IBMの株価は何ドルですか？` (“What is IBM’s stock price in dollars?”)

You’ll notice a different response this time. The AI agent now follows the rules defined in the Behavior section. It no longer tries to launch unavailable tools and instead replies appropriately that it cannot provide a correct answer. This adjustment enhances the overall user experience.

### 14. Ask the AI agent a question in English.  
* **Input:** `What is IBM?`

### 15. Confirm that the AI agent responds in English. It follows the rule you set earlier (“Answer in the same language as the question”).

---

**End of Part 1**  
Proceed to [Part 2](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/02RagAgent/readme.md) to continue the hands-on experience.
