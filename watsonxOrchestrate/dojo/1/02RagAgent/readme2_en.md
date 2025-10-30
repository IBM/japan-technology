# watsonx Orchestrate AI Agent Experience – Part 2

_Last updated: October 30, 2025_

In this exercise, you will extend your AI agent **IBMInfo** (created in Part 1) by adding knowledge using the **RAG (Retrieval-Augmented Generation)** approach. Please ensure that you have completed Part 1 before starting.

* Adding Knowledge

---

### 1. Click **Knowledge** from the left-hand menu on the IBMInfo agent management page, then click **Choose knowledge +** under the *Knowledge source* section.

<img width="1174" height="932" alt="2-1-ChooseKnowledge" src="https://github.com/user-attachments/assets/c6862030-32c4-48a8-9053-c83e27d67ebe" />


### 2. In the **Choose knowledge source** window, select **Upload files**, then click **Next**.

<img width="1174" height="1036" alt="2-2-SelectUploadFile" src="https://github.com/user-attachments/assets/02843008-2765-4723-bfa3-85555769acc5" />


### 3. Download the file [2024-annual-report.pdf](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/02RagAgent/2024-annual-report.pdf) to your local computer.

### 4. Drag and drop the downloaded file into the **Drag and drop files here or click to upload** area, or click the link to upload it manually.



<img width="1181" height="974" alt="2-4-ClickToUpload" src="https://github.com/user-attachments/assets/5386cef9-bd34-45e3-838b-37e71ec51319" />

### 5. Once the file is uploaded, click **Next**.

<img width="1181" height="974" alt="2-5-FileUploaded" src="https://github.com/user-attachments/assets/a887f454-2c0c-45b9-a7dd-4f193b306f8c" />

### 6. Enter the following description to let the agent know what the document contains, then click **Save**.

* **Description:** 
```
This is IBM’s 2024 Annual Report, including financial information and core business strategy.
```
<img width="1181" height="974" alt="2-6-FileDescription" src="https://github.com/user-attachments/assets/afcffba8-1fc7-4bc0-ac16-75e79167f647" />



### 7. The *Knowledge source* section will show **Processing...** as the file is being indexed. The system uses the uploaded PDF and description to prepare searchable knowledge for your agent. This may take around two minutes.

<img width="377" height="400" alt="2-7-Processing" src="https://github.com/user-attachments/assets/0989ead6-2017-4581-ad0f-24bf79bef107" />

### 8. When processing is complete, the *Knowledge source* will display **Connected**, and you’ll see the file name `2024-annual-report.pdf` and your description:  
“This is IBM’s 2024 Annual Report, including financial information and core business strategy.”

<img width="1181" height="974" alt="2-8-Connected" src="https://github.com/user-attachments/assets/5690c741-ae4c-427e-b534-9538e5a41c51" />


### 9. Use the **Preview** window to ask a question based on the uploaded document.  
* **Input:** 
```
What was IBM’s free cash flow in 2024?
```

The AI agent will reply with **$12.7 billion**.

<img width="1181" height="974" alt="2-10-FreeCashFlowResult" src="https://github.com/user-attachments/assets/4a20654a-955a-43d8-a904-93798cf7f213" />

### 10. Open *2024-annual-report.pdf* and check page 3 (document page 1). You’ll find the following text:

```
2024 Performance
For the year, IBM generated $62.8 billion in revenue, up 3%
at constant currency, and $12.7 billion in free cash flow — an
increase of $1.5 billion year-over-year.
```

### 11. Click **Show Reasoning v** to the right of the agent’s answer timestamp.

You’ll see “Tool: knowledge_for_agent_IBMInfo,” confirming that the agent used the uploaded knowledge to answer your question.

<img width="399" height="480" alt="2-12-Reasoning" src="https://github.com/user-attachments/assets/4330d500-dee7-4dc5-9351-87f89f5288d8" />


### 12. Ask another question:  
* **Input:** 
```
How much did free cash flow change year-over-year in 2024? Please include the unit and provide the amount.
```  
The answer should reflect the same context found in the report above.

<img width="404" height="296" alt="2-13-CashFlowYtY" src="https://github.com/user-attachments/assets/de1f4fe9-113a-4ee2-b6f6-01bd3f0f8589" />

### 13. Ask about a different section of the document:  
* **Input:** 
```
What was Revenue in 2024?
```

```
What was Net income in 2024?
```

```
What was Net income in 2023?
```

You can verify this data by checking the table on page 10 (document page 8) of the Annual Report under **Revenue**.

* **Source:** [2024 IBM Annual Report](https://www.ibm.com/downloads/documents/us-en/1227c12d3a38b173)
<img width="653" height="492" alt="30-02-DocTable" src="https://github.com/user-attachments/assets/29d18bcd-7f4d-471f-ae08-cffacc26f374" />
---

## Deploying the AI Agent

### 14. Click **Deploy** in the upper-right corner.

### 15. On the **Pre-deployment Summary** page, click the blue **Deploy** button in the lower right corner.

### 16. Wait until the message **Success** appears in the upper-right corner. Your AI agent is now deployed and ready for use.

### 17. From the top-left menu, click **Chat**.

### 18. Select your AI agent **IBMInfo**.

### 19. Ask a question in the chat:  
* **Input:** `What was IBM’s free cash flow in 2024?`

### 20. Confirm that the AI agent responds correctly.

### 21. Click the 👍 icon to send feedback.

> Note: Feedback cannot be viewed directly from the watsonx Orchestrate management console.  
> You can access it through the API [Get messages to a specific thread](https://developer.ibm.com/apis/catalog/watsonorchestrate--custom-assistants/api/API--watsonorchestrate--agentic-experience#Get_Message_by_ID_v1_threads__thread_id__messages__message_id__get), where it’s stored as a `feedback` object inside `message_state`.

---

## Optional Exercise – Trace the Agent’s Workflow

You can trace the behavior of your **IBMInfo** agent using **LangGraph**, a workflow framework for LLM-based applications.

* Reference: [LangGraph](https://www.langchain.com/langgraph) – a framework for designing and managing AI workflows using large language models.

### 22. From the top-left menu, click **Build → Agent Builder**, then click **View all →**.

### 23. The **Agent Analytics** screen will appear. Click **Close** or **×** to dismiss it.

### 24. In the **Agents** list, select **IBMInfo**. If multiple agents appear, open each and find the one with the most recent timestamp under **Traces**.

### 25. Click the most recent trace result in the **Traces** list.

### 26. The **Trace Detail** screen will open (Public Preview feature). This view shows the internal workflow of the AI agent.

### 27. Under **Service & Operation**, find the blue bold line labeled **wxo-server LangGraph.workflow** and click it.

### 28. The **LangGraph.workflow** timeline expands. Click **Tags** to reveal details under the *Tags* section.

### 29. Scroll down to find your input question.

### 30. Continue scrolling until you see **tool_calls:**. Inside **function:**, you’ll find a name starting with **knowledge_for_agent_IBMInfo_** — indicating that your agent used the uploaded Knowledge as a tool.

---

✅ **End of Part 2**  
You have successfully built, enhanced, and deployed your watsonx Orchestrate AI agent with knowledge integration and workflow tracing.
