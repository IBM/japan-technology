---
authors: ''
completed_date: '2021-07-08'
draft: false
excerpt: Learn how the Data Quality for AI Toolkit provides a systematic way to assess
  and remediate data with well-specified APIs.
menu_order: 1
meta_description: Improve your data quality management, and learn how the Data Quality
  for AI Toolkit provides a systematic way to assess and remediate data with well-specified
  APIs.
meta_keywords: artificial intelligence, APIs, data quality, data quality APIs
meta_title: Data Quality for AI
primary_tag: artificial-intelligence
subtitle: Learn how the Data Quality for AI Toolkit provides a systematic way to assess
  and remediate data with well-specified APIs
tags:
- deep-learning
- machine-learning
- data-science
- data
- ibm-research-content
title: Data Quality for AI
---

If we were in a movie on AI, the main character of our story would be a data scientist - let's call her Ria. Ria works in a multinational company, and one Monday morning she receives a request for her help on a project to build an AI model. The project is a high-visibility project and has the possibility of large revenue savings for the company if Ria and her team can build an AI model to solve the problem. Ria is excited and immediately starts asking for data access so that she and her team can get started on the project. Ria and her team analyze the data to find data quality issues, clean the data, build features, and build a model. After several months, Ria and her team are struggling to build a high-accuracy model. With every iteration, they discover more data quality issues, go back to the design table to brainstorm the issue, figure out ways to fix it, and write the code for data remediation. After weeks and months of effort, Ria believes that the entire project would have been more streamlined if they had gotten a report on the data quality when they had gotten the data at the beginning. Does this sound familiar?

Many <a href="https://www.datanami.com/2020/07/06/data-prep-still-dominates-data-scientists-time-survey-finds/" target="_blank" rel="noopener noreferrer">studies</a> have shown that data preparation is one of the most time-consuming pieces of the machine learning lifecycle. One reason is that the data issues are discovered in a trial and error fashion, new code must be written for every issue found, and someone must keep a manual log of all of the changes applied to the data so that there is a lineage of how the data was changed over the course of building a machine learning pipeline. However, this information, unless explicitly recorded, might not be available. 

While data scientists solve these problems today by writing custom scripts or manual analyses, this is a time-consuming process, and some challenges such as finding class overlap or label noise can, by themselves, be AI-based algorithms that might take several months to develop before they can be used in a business project. Moreover, there are other challenges like a large number of metrics to check for, different modalities of data like tabular data and time series data, which make this problem even harder. Therefore, there is a need for automation in this space to consistently assess data across different modalities, explain the assessment, suggest recommendations, and code to run these recommendations.

To overcome these challenges, IBM Research has developed a Data Quality for AI Toolkit that is built using novel algorithms and provides a systematic way to assess and remediate data with well-specified APIs. The Toolkit is built to serve a wide variety of use cases such as:

* Building supervised classification models
* Providing data quality for application workflows with intuitive mechanisms to take domain inputs
* Working in the presence of strict privacy constraints by data synthesis
* Automatically reporting on the data quality and capturing the lineage for the data

The toolkit has the following features:

1. Validators: Algorithms that perform data quality assessment and output a data quality score from 0 - 1. 
1. Remediators: Algorithms to provide corrective actions to fix the data quality and impact on the data quality score.
1. Constraints: Explicit input provided by domain experts or implicitly derived by analyzing the data characteristics.
1. Data Synthesizer: In the event that data cannot be shared due to strict privacy constraints, it provides a capability to synthesize data by learning constraints from real data so that it mimics real data.
1. Pipeline: Combines validators and remediators with constraints to address a use case or application workflow and outputs an overall data quality score.
1. Data Readiness Report: Automated documentation of changes that records delta changes in quality metrics and data transformations applied.

For more details on the product, see <a href="https://www.ibm.com/products/dqaiapi" target="_blank" rel="noopener noreferrer">https://www.ibm.com/products/dqaiapi</a>.

The APIs to check the data quality for building a supervised classification model are available on the <a href="https://developer.ibm.com/apis/catalog/dataquality4ai--data-quality-for-ai/Introduction" target="_blank" rel="noopener noreferrer">IBM API Hub</a> as a trial version. You can use these APIs at step zero of the AI lifecycle to find the quality of the data set. There are several APIs available that assess the data from different dimensions like labels, challenges with respect to data distribution, and data cleanliness. Additionally, it can also profile the data sets to understand the data characteristics. All of the APIs have a standard response structure in the form of a JSON object, which gives a data quality score, points to regions that are responsible for low data quality, and gives recommendations to improve the data. The data quality score is a real value between 0 – 1, with 1 indicating perfect quality. For every API, details around how the score is calculated is well documented. You can use these APIs to systematically understand data issues and fix them to improve the data set and accelerate to the next steps of the lifecycle. Take a look at the details of how to <a href="https://developer.ibm.com/apis/catalog/dataquality4ai--data-quality-for-ai/Getting%20Started" target="_blank" rel="noopener noreferrer">access the APIs and the result objects</a>.

## Demo 

<iframe width="480" height="270" src="https://www.ustream.tv/embed/recorded/130008974" scrolling="no" allowfullscreen webkitallowfullscreen frameborder="0" style="border: 0 none transparent;"></iframe>

## Summary

This article described the features of the Data Quality for AI Tookit, which allow a data scientist to understand and systematically address the data quality issues and address them in their data science pipelines as well as how some of these APIs can be accessed through [IBM APIHub](https://developer.ibm.com/apis/catalog/dataquality4ai--data-quality-for-ai/Introduction). If you have any questions, suggestions for other features to be available in a trial mode, or issues, let us know by joining the [Data Quality for AI](https://join.slack.com/t/dqai/shared_invite/zt-ra98jfbm-KgZwRlokg~5_3_A7FyFm3g) Slack workspace.