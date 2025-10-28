# watsonx Orchestrate AI Agent Experience – Part 1

_Last updated: October 28, 2025_

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
<img width="1110" height="1026" alt="1-6-Description" src="https://github.com/user-attachments/assets/36b94e91-6210-4f49-873b-985e016e4d28" />

* Once you’ve entered the description, click **Create**.

### 7. Confirm that your AI agent has been created. If an error occurs, try using a different name.

<img width="1154" height="1070" alt="1-7-Profile" src="https://github.com/user-attachments/assets/8b3cde2f-6094-435d-ae2b-763e22a4edf6" />


### 8. Test your newly created AI agent. In the **Preview** panel on the right, enter a question.  
* **Input:** 
```
What is IBM?
```

<img width="418" height="778" alt="1-8-whatisIBM" src="https://github.com/user-attachments/assets/1581db20-e4a5-4579-b749-36fb070be4ce" />


After a few moments, the agent will respond using the foundation model **llama-3-2-90b-vision-instruct**.

<img width="422" height="408" alt="1-8-2-result" src="https://github.com/user-attachments/assets/68402f6d-3cad-4c01-8692-f23adcf43971" />


### 9. Try another question.  
* **Input:** 
```
What is IBM’s stock price in dollars?
```

<img width="422" height="63" alt="1-9-1-StockPrice" src="https://github.com/user-attachments/assets/435709be-711d-4419-84f7-83da440e1f2c" />


After a short wait, the AI agent will respond. In both cases, it will indicate that it needs an external tool to retrieve the information, but since no tool is configured, the correct data won’t appear.


> If generation doesn’t stop, click **Reset**<img width="31" height="33" alt="Preview-Reset" src="https://github.com/user-attachments/assets/e838f4b9-767b-4120-9396-0f8f631d6f06" /> in the Preview panel, skip Steps 12–13, and proceed to Step 14.

* **Example Output :** A general description about IBM’s stock.  

<img width="409" height="267" alt="1-9-2-Result" src="https://github.com/user-attachments/assets/f39637fd-0f77-4932-84b4-7423d95070c0" />


### 10. Provide the keyword **NYSE** (New York Stock Exchange) to inform the AI agent where IBM’s stock is traded.  
* **Input:** 
```
NYSE
```

<img width="399" height="256" alt="1-10-NYSE" src="https://github.com/user-attachments/assets/cc1f08f8-a68c-4588-82fc-41e967dd0300" />



The AI agent will attempt to call a tool to fetch the stock price but will fail because no proper tool is defined. This behavior is expected — it shows how the AI agent tries to use external tools to find missing contextual data.

> For reference, if you run the same inference directly on watsonx.ai, it won’t attempt to call tools — it will simply generate a text-based response.
<img width="1256" height="705" alt="13-02-wxaiLLM" src="https://github.com/user-attachments/assets/91987539-9be8-489d-98dc-0872d1e42433" />

### 11. Define the agent’s behavior. Click **Behavior** on the left-hand side.

<img width="1154" height="1070" alt="1-11-Behavior" src="https://github.com/user-attachments/assets/e2ea7546-0042-4ecd-880f-f4b79473e424" />


### 12. In the **Instructions** field, describe how you want the AI agent to behave.

* **Instructions:**  
```
If you don't have any knowledge, tools for stock price or context to answer,
respond with: ‘I cannot answer accurately due to insufficient information'.
Don't simulate the tool execution if you don't have the right tools/knowledge.
Don't ask for additional input if you don't have the stock price tool.

Answer using the same natural language as the question.
If the question is in Japanese, answer in Japanese.
If it’s in English, answer in English.
```

<img width="1154" height="1070" alt="1-12-0Instruction" src="https://github.com/user-attachments/assets/09b744f5-9f85-4d23-bd2d-9f176aff55da" />


### 13. After configuring the behavior, return to the Preview panel and ask again:  
* **Input:** 
```
What is IBM’s stock price in dollars?
```

You’ll notice a different response this time. The AI agent now follows the rules defined in the Behavior section. It no longer tries to launch unavailable tools and instead replies appropriately that it cannot provide a correct answer. This adjustment enhances the overall user experience.

<img width="1154" height="1070" alt="1-13-ChangedRespnse" src="https://github.com/user-attachments/assets/beaeb7c5-b3ef-4c8c-b84e-594e6c135074" />


### 14. Ask the AI agent a question in Japanse.  
* **Input:** 
```
IBMとは何ですか？
```

### 15. Confirm that the AI agent responds in Japanese. It follows the rule you set earlier (“Answer in the same language as the question”).

<img width="409" height="265" alt="1-15-Japanese" src="https://github.com/user-attachments/assets/b216b558-1de8-42f4-9499-4c376ea2d3bb" />

---

**End of Part 1**  
Proceed to [Part 2](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/02RagAgent/readme.md) to continue the hands-on experience.
