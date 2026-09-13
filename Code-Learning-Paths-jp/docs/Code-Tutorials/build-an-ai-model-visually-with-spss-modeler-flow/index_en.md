---
abstract: In this tutorial, we will use IBM Cloud Pak for Data to build a predictive
  machine learning model (with IBM SPSS Modeler) to decide whether a customer will
  default on a loan or not. IBM Cloud Pak for Data is an interactive, collaborative,
  cloud-based environment that allows developers and data scientists to work collaboratively,
  gain insight from data and build machine learning models.
also_found_in:
- /learningpaths/cloud-pak-for-data-learning-path/
authors: ''
completed_date: '2020-02-25'
components:
- cloud-pak-for-data
- spss-modeler
draft: false
excerpt: In this tutorial, we will use IBM Cloud Pak for Data to build a predictive
  machine learning model (with IBM SPSS Modeler) and decide whether a customer will
  default on a loan or not. IBM Cloud Pak for Data is an interactive, collaborative,
  cloud-based environment that allows developers and data scientists to work collaboratively,
  gain insight from data and build machine learning models.
ignore_prod: false
last_updated: '2021-07-22'
meta_description: Build a predictive machine learning model quickly and easily with
  IBM SPSS Modeler.
meta_keywords: machine learning, AI, IBM SPSS modeler, IBM Cloud Pak for Data
meta_title: Build a predictive machine learning model with IBM SPSS Modeler
primary_tag: analytics
related_content:
- slug: Fraud Detection with SPSS modeler https://developer.ibm.com/tutorials/fraud-detection-with-spss-modeler/
  type: tutorials
- slug: Build, train, and evaluate a machine learning product-based classifier on
    a customer profile https://developer.ibm.com/tutorials/promoting-financial-products-to-bank-customers/
  type: tutorials
subtitle: Tap into data assets and modern applications with ready-to-use algorithms
  and models
tags:
- analytics
title: Build a predictive machine learning model quickly and easily with IBM SPSS
  Modeler
type: tutorial
---

In this tutorial, we will use [IBM Cloud Pak for Data](https://www.ibm.com/products/cloud-pak-for-data) to build a predictive machine learning model with [IBM SPSS Modeler](https://www.ibm.com/products/spss-modeler) and decide whether a bank customer will default on a loan. IBM Cloud Pak for Data is an interactive, collaborative, cloud-based environment that allows developers and data scientists to work collaboratively, gain insight from data and build machine learning models.

## Learning objectives

After completing this tutorial, you will learn how to:

* Upload data to [IBM Cloud Pak for Data](https://www.ibm.com/products/cloud-pak-for-data).
* Create an SPSS Modeler flow.
* Use the SPSS tool to inspect data and glean insights.
* Modify and prepare data for AI model creation using SPSS.
* Train a machine learning model with SPSS and evaluate the results.

## Prerequisites

* [IBM Cloud Pak for Data](https://www.ibm.com/products/cloud-pak-for-data)
* [SPSS Modeler Deployed on IBM Cloud Pak for Data](https://www.ibm.com/docs/en/cloud-paks/cp-data/4.0?topic=modeler-installing-spss)

## Estimated time

Completing this tutorial should take about 30 minutes.

## Steps

1. [Create a project and upload the data](#step-1-create-a-project-and-upload-the-data)
2. [Create an SPSS Modeler Flow](#step-2-create-an-spss-modeler-flow)
3. [Import the data](#step-3-import-the-data)
4. [Inspect the data](#step-4-inspect-the-data)
5. [Data preparation](#step-5-data-preparation)
6. [Train the ML model](#step-6-train-the-ml-model)
7. [Evaluate the results](#step-7-evaluate-the-results)

### Step 1. Create a project and upload the data

If you have not already created a project for this learning path, follow the instructions below to create one. Otherwise, you can skip to [Create an SPSS Modeler Flow](#step-2-create-an-spss-modeler-flow).

### Create an IBM Cloud Pak for Data project

In Cloud Pak for Data, we use the concept of a project to collect / organize the resources used to achieve a particular goal (resources to build a solution to a problem). Your project resources can include data, collaborators, and analytic assets like notebooks and models, etc.

* Go the (☰) navigation menu and under the *Projects* section click on *`All Projects`*.

  ![(☰) Menu -> Projects](images/menu-projects.png)

* Click on the **`New project`** button on the top right.

  ![Start a new project](images/new-project.png)

* Select the `Analytics project` radio button and click the **`Next`** button.

  ![New analytics project](images/new-project-type.png)

* Select **`Create an empty project`**.

  ![Create empty project](images/cpd-create-empty-project.png)

* Provide a name and optional description for the project and click **`Create`**.

  ![Pick a name](images/project-name.png)

### Download the dataset for this experiment and load it into you project.

* Download the [german_credit_data.csv](static/german_credit_data.csv) dataset.

* Upload the dataset to the analytics project by clicking on **Browse** and selecting the downloaded file.

### Step 2. Create an SPSS Modeler flow

1. From the Project home page, click **Add to Project +** and choose **Modeler flow**.

    ![Add modeler flow](images/spss-add-modeler-flow.png)

1. Give the flow a meaningful name, such as `Credit Risk Flow`, then click **Create**.

    ![Create flow](images/spss-create-flow.png)

### Step 3. Import the data

1. In the left-hand pane, expand **Import**, then drag and drop a Data Asset node on the canvas. Double-click on the node that was dropped on the canvas and click **Change data asset**.

    ![Data asset](images/spss-data-asset.png)

1. On the Assets page, open the **Data Assets** tab, choose the german_credit_data.csv file you previously uploaded and click **Select**.

    ![Import data](images/spss-import-data.png)

1. When the data is imported, click **Save**.

    ![Save data](images/spss-save-data.png)

### Step 4. Inspect the data

1. To gain insight into your data, open the **Output** tab and drag and drop the data audit node onto the canvas. Hover over the Data Asset node that was dragged and dropped on the canvas earlier, and it should show a blue circular icon on the side. Click on the icon and drag over to the Data Audit node. This will connect the two nodes.

    ![Data Audit](images/spss-data-audit.png)

1. Hover over the Data Audit node and click on the three vertical dots to open the menu for the node. Alternatively, right-click on the Data Audit node and click **Run**. 

    ![Data inspection](images/spss-data-inspection.png)

1. Once it is ready, the output can be viewed by opening the Outputs menu on the right. Click on the "eye" icon to open the Data Audit (Data Audit of [21 fields]) to view statistics about the data.

    ![Open Data inspection] (images/spss-data-inspection-2.png)

    ![Data inspection statistics](images/spss-data-inspection-statistics.png)

1. Click **X** in the upper right corner to close the window.

### Step 5. Data preparation

1. Expand the Field Operations tab and drag and drop the Type node onto the canvas. Connect the Data Asset node with the Type node, then double-click on the Type node to make the necessary configurations.

    ![Type](images/spss-type.png)

1. Click on **Read Values**. Once the read operation completes, check that the measure and role for each field is correct. Change the role of Risk from `Input` to `Target`, then click **Save** to close the tab.

    ![Data preparation](images/spss-data-preparation.png)

### Step 6. Train the ML model

1. Expand the Modeling tab, then drag and drop the Random Forest node onto the canvas. Connect the Type node to the Random Forest node. The Random Forest node will automatically be renamed Risk.

    ![Random Forest](images/spss-random-forest.png)

1. Right-click on the Random Forest node and click **Run**. When the execution is done, you will see a new golden nugget-like Risk node added to the canvas.

    ![Start training](images/spss-start-training.png)

1. Right-click on the new Risk golden nugget node and choose **Preview** to inspect the output results.

    ![Preview Random Forest result](images/spss-preview-random-forest-result.png)

### Step 7. Evaluate the results

1. Expand the Outputs tab, then drag and drop an analysis node onto the canvas. Connect the Risk golden nugget node to the Analysis node. Right-click on the Analysis node and click **Run**.

    ![Analysis](images/spss-analysis.png)

1. From the Outputs tab on the right, click on the "eye" icon next to **analysis of [Risk]** to gain insight into the accuracy of the results.

    ![Analysis output](images/spss-open-analysis.png)

    ![Analysis output](images/spss-output-analysis.png)

1. Click on **Return to flow** to go back.

1. Expand the Graphs tab, then drag and drop the Evaluation node onto the canvas. Connect the Risk golden nugget node with the Evaluation node. The Evaluation node will automatically be renamed $R-Risk. Right-click on the node and click **Run**.

![Evaluation](images/spss-evaluation.png)

1. Double-click on the "eye" icon next to the $R-Risk output (evaluation of [$R-Risk]: Gains) to visualize the graph for the Gains. This will give the Predicted Positive Rate (or support of the classifier) vs. True Positive Rate (or sensitivity of the classifier).

    ![Evaluation graph](images/spss-evaluation-graph.png)

## Summary

This tutorial demonstrated a small example of creating a predictive machine learning model on IBM SPSS Modeler on IBM Cloud Pak for Data. It went over importing the data into the project and the modeler flow, and preparing the data for modeling, then over the steps of choosing an appropriate algorithm for the data and training a prediction model. The last step explained how to visualize and evaluate the results of the trained model.