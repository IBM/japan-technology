# watsonx Orchestrate AI Agent Experience – Part 2

_Last updated: September 29, 2025_

In this exercise, you will extend your AI agent **IBMInfo** (created in Part 1) by adding knowledge using the **RAG (Retrieval-Augmented Generation)** approach. Please ensure that you have completed Part 1 before starting.

* Adding Knowledge

---

### 1. Click **Knowledge** from the left-hand menu on the IBMInfo agent management page, then click **Choose knowledge +** under the *Knowledge source* section.

### 2. In the **Choose knowledge source** window, select **Upload files**, then click **Next**.

### 3. Download the file [2024-annual-report.pdf](https://github.com/IBM/japan-technology/blob/main/watsonxOrchestrate/dojo/1/02RagAgent/2024-annual-report.pdf) to your local computer.

### 4. Drag and drop the downloaded file into the **Drag and drop files here or click to upload** area, or click the link to upload it manually.

### 5. Once the file is uploaded, click **Next**.

### 6. Enter the following description to let the agent know what the document contains, then click **Save**.

* **Description:** `This is IBM’s 2024 Annual Report, including financial information and core business strategy.`

### 7. The *Knowledge source* section will show **Processing...** as the file is being indexed. The system uses the uploaded PDF and description to prepare searchable knowledge for your agent. This may take around one minute.

### 8. When processing is complete, the *Knowledge source* will display **Connected**, and you’ll see the file name `2024-annual-report.pdf` and your description:  
“This is IBM’s 2024 Annual Report, including financial information and core business strategy.”

### 9. Use the **Preview** window to ask a question based on the uploaded document.  
* **Input:** `What was IBM’s free cash flow in 2024?`  
The AI agent will reply with **$12.7 billion**.

### 10. Open *2024-annual-report.pdf* and check page 3 (document page 1). You’ll find the following text:

```
2024 Performance
For the year, IBM generated $62.8 billion in revenue, up 3%
at constant currency, and $12.7 billion in free cash flow — an
increase of $1.5 billion year-over-year.
```

### 11. Click **Show Reasoning v** to the right of the agent’s answer timestamp.

You’ll see “Tool: knowledge_for_agent_IBMInfo,” confirming that the agent used the uploaded knowledge to answer your question.

### 12. Ask another question:  
* **Input:** `How much did free cash flow change year-over-year in 2024? Please include the unit and provide the amount.`  
The answer should reflect the same context found in the report above.

### 13. Ask about a different section of the document:  
* **Input:** `According to the Management Discussion, what was IBM’s revenue growth rate in 2024 compared to 2023?`

You can verify this data by checking the table on page 10 (document page 8) of the Annual Report under **Revenue**.

* **Source:** [2024 IBM Annual Report](https://www.ibm.com/downloads/documents/us-en/1227c12d3a38b173)

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