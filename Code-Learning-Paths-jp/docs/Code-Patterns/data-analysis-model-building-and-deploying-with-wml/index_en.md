---
also_found_in:
- /learningpaths/cloud-pak-for-data-learning-path/
authors: ''
completed_date: '2019-10-04'
components:
- cloud-pak-for-data
- jupyter
- watson-machine-learning
draft: false
excerpt: Use IBM Cloud Pak for Data to go through the whole data science pipeline
  to solve a business problem and predict loan default using a German credit risk
  dataset.
github:
- button_title: Get the code
  url: https://github.com/IBM/predict-credit-risk-with-jupyter-on-cloud-pak-for-data
ignore_prod: false
last_updated: '2021-07-22'
meta_description: Use IBM Cloud Pak for Data to go through the whole data science
  pipeline to solve a business problem and predict loan default using a German credit
  risk dataset.
meta_keywords: IBM Cloud Pak for Data, data analysis, model building, Watson machine
  learning
meta_title: Solve a business problem and predict loan default using a German credit
  risk dataset.
primary_tag: analytics
pta:
- cognitive, data, and analytics
pwg:
- analytics
subtitle: Use Watson Machine Learning and Jupyter Notebooks on IBM Cloud Pak for Data
  to predict load default
tags:
- analytics
- data-management
- data-science
- databases
- machine-learning
title: Solve a business problem and predict loan default using a German credit risk
  dataset.
type: default
---

## Summary

In this developer code pattern, we'll use IBM Cloud Pak for Data to go through the whole data science pipeline to solve a business problem and predict loan default using a German credit risk dataset. IBM Cloud Pak for Data is an interactive, collaborative, cloud-based environment. It can help data scientists, developers, and others interested in data science use tools to collaborate, share, and gather insights from their data -- as well as build and deploy machine learning, and deep learning models.

## Description

Predicting loan default is integral to many financial and other related businesses. For this use case, the machine learning model we are building is a classification model that will return a prediction of 'Risk' (the features of the loan applicant predict that there is a good chance of default on the loan) or 'No Risk' (the applicant's inputs predict that the loan will be paid off). The approach we will take in this lab is to use some fairly popular libraries / frameworks to build the model in Python using a Jupyter notebook.

After you've completed this code pattern, you'll understand how to:

* Use [Jupyter Notebooks](https://jupyter.org/) to load, visualize, and analyze data.
* Run Notebooks in [IBM Cloud Pak for Data](https://www.ibm.com/analytics/cloud-pak-for-data).
* Build, test, and deploy a machine learning model using [Spark MLib](https://spark.apache.org/mllib/) on IBM Cloud Pak for Data.
* Deploy a selected machine learning model to production using IBM Cloud Pak for Data.
* Create a front-end application to interface with the client and start consuming your deployed model.

## Flow

![flow](images/datanalarch.png)

1. User loads the Jupyter Notebook into the IBM Cloud Pak for Data platform.
1. [German credit data](https://github.com/IBM/predict-credit-risk-with-jupyter-on-cloud-pak-for-data/blob/main/data/german_credit_data.csv) is loaded into the Jupyter Notebook, either directly from the GitHub repo or as virtualized data after following the previous tutorial.
1. Preprocess the data, build machine learning models, and save to IBM Watson Machine Learning on IBM Cloud Pak for Data.
1. Deploy a selected machine learning model into production on the IBM Cloud Pak for Data platform and obtain a scoring endpoint.
1. Use the model for credit prediction using a front-end application.

## Instructions

Ready to put this code pattern to use? Complete details on how to get started running and using this application are in the [README](https://github.com/IBM/predict-credit-risk-with-jupyter-on-cloud-pak-for-data/blob/master/README.md), including how to:

1. Create a new project.
1. Create a space for machine learning deployments.
1. Upload the dataset if you are not on the IBM Cloud Pak for Data learning path.
1. Import Jupyter Notebook to IBM Cloud Pak for Data.
1. Run the notebook.
1. Deploy the model using the IBM Cloud Pak for Data UI.
1. Test the model.
1. Create a Python Flask app that uses the model.

## Conclusion

This code pattern showed how to use IBM Cloud Pak for Data and go through the whole data science pipeline to solve a business problem and predict loan default using a German credit risk dataset.