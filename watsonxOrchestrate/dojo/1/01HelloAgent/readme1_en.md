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

Open watsonx Orchestrate according to your environment.

### 2. Click **Build** from the upper-left menu and select **Agent Builder**.

### 3. On the right-hand side, click **Create agent +**.

### 4. In the “Create an agent” window, select **Create from scratch**.

### 5. Name your AI agent “IBMInfo,” since it will answer questions about IBM.  
* **Name:** `IBMInfo`

### 6. Add a description for your AI agent. The description helps watsonx Orchestrate determine which agent to invoke, so be specific.  
* **Description:** `An agent that answers questions about IBM company information.`  
Once you’ve entered the description, click **Create**.

### 7. Confirm that your AI agent has been created. If an error occurs, try using a different name.

### 8. Test your newly created AI agent. In the **Preview** panel on the right, enter a question.  
* **Input:** `IBMとは何ですか？` (“What is IBM?”)

After a few moments, the agent will respond using the foundation model **llama-3-2-90b-vision-instruct**.

### 9. Try another question.  
* **Input:** `IBMの株価は何ドルですか？` (“What is IBM’s stock price in dollars?”)

After a short wait, the AI agent will respond. In both cases, it will indicate that it needs an external tool to retrieve the information, but since no tool is configured, the correct data won’t appear.

> If generation doesn’t stop, click **Reset** in the Preview panel, skip Steps 12–13, and proceed to Step 14.

* **Example Output 1:** A general description about IBM’s stock.  
* **Example Output 2:** Another variation in generated responses.

### 10. Provide the keyword **NYSE** (New York Stock Exchange) to inform the AI agent where IBM’s stock is traded.  
* **Input:** `NYSE`

The AI agent will attempt to call a tool to fetch the stock price but will fail because no proper tool is defined. This behavior is expected — it shows how the AI agent tries to use external tools to find missing contextual data.

> For reference, if you run the same inference directly on watsonx.ai, it won’t attempt to call tools — it will simply generate a text-based response.

### 11. Define the agent’s behavior. Click **Behavior** on the left-hand side.

### 12. In the **Instructions** field, describe how you want the AI agent to behave.

* **Instructions:**  
  “Answer using the same natural language as the question. If the question is in Japanese, answer in Japanese. If it’s in English, answer in English.  
  If you lack the necessary knowledge or context to answer, respond with: ‘I cannot answer accurately due to insufficient information.’”

### 13. After configuring the behavior, return to the Preview panel and ask again:  
* **Input:** `IBMの株価は何ドルですか？` (“What is IBM’s stock price in dollars?”)

You’ll notice a different response this time. The AI agent now follows the rules defined in the Behavior section. It no longer tries to launch unavailable tools and instead replies appropriately that it cannot provide a correct answer. This adjustment enhances the overall user experience.

### 14. Ask the AI agent a question in English.  
* **Input:** `What is IBM?`

### 15. Confirm that the AI agent responds in English. It follows the rule you set earlier (“Answer in the same language as the question”).

---

**End of Part 1**  
Proceed to [Part 2](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/02RagAgent/readme.md) to continue the hands-on experience.