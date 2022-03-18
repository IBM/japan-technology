---
authors: ''
collections:
- ibm-research
completed_date: '2021-08-31'
draft: true
excerpt: Learn about Edge AI APIs, a set of RESTful web services with data and AI
  algorithms to support AI applications across distributed hybrid cloud environments.
menu_order: 2
meta_description: Learn about Edge AI APIs, a set of RESTful web services with data
  and AI algorithms to support AI applications across distributed hybrid cloud environments.
meta_keywords: artificial intelligence, API, Edge AI API
meta_title: Get started with Edge AI APIs
primary_tag: artificial-intelligence
subtitle: Learn about Edge AI APIs, a set of RESTful web services with data and AI
  algorithms to support AI applications across distributed hybrid cloud environments
tags:
- deep-learning
- machine-learning
- data-science
- edge-computing
- ibm-research-content
title: Get started with Edge AI APIs
---

The Edge AI API is an early access offering from IBM Research to enable AI at the edge. It packages Edge AI APIs to support AI applications across distributed hybrid cloud environments. These APIs are general purpose and support many modalities of data, for example, visual, acoustic, sensors, network logs, time series, or natural language. Using these APIs, you can create various AI-based applications. The following image shows the Edge AI high-level architecture.

![Edge AI high-level architecture](images/figure1.png)

Starting at the bottom in the figure, it's assumed that at a minimum the edge sites have a Linux&reg;-based server with a container runtime like Docker. There could be additional software such as Red Hat OpenShift or IBM Cloud Pak for Data, but it is not mandatory. Also, it's useful to automate the deployment and management of these containers with IBM Edge Application Manager or Red Hat OpenShift Advanced Cluster Management capabilities.

Above that is the Edge AI Core. It has a few essential services to enable coordination among edge sites and the cloud. The Registry allows discovery and sharing of resources, while the Policy Manager allows specification and enforcement of policies to govern the application behavior. The Group Manager keeps track of all available service end points across the edge and cloud as edge devices join and leave in dynamic environments.

Next are Coresets and Federated Data Ops, the distributed data layer capabilities. Coresets are a set of algorithms to intelligently sub-sample raw data or compute compressed semantic representations of raw data to optimize data collection from the edge. Federated Data Ops can automatically assess data quality, identify issues such as missing or noisy data, and substitute or discard such data.

On top of the data layer are the AI capabilities. The Model Management addresses all of the second pattern questions discussed previously about selecting the most suitable model for an edge site, optimizing the model for the edge site, and monitoring its performance. The Model Fusion is focused on enabling federated learning and federated inferencing in the context of the third pattern where all of the training data cannot be aggregated in one place.

Finally, at the top are Edge AI applications created by using the APIs to solve specific business problems. A few examples have been created to illustrate how the Edge AI APIs work and how you can use them to create applications.

Because some companies have little or no instrumentation in their operations, it can hinder any opportunities for automation. In a recent partnership with Boston Dynamics, IBM demonstrated how Edge AI can help.

Deploying sensors to instrument legacy equipment can be cost prohibitive. However, the SPOT robot from Boston Dynamics is a roaming edge server and a sensor platform. SPOT can walk around and look or listen for anomalies by incorporating visual and acoustic inspection on board, and can interact with equipment where needed. The Edge AI APIs running on the SPOT robot can unlock tremendous opportunities for asset health insights and more timely action.

**Boston Dynamic SPOT Robot demo Video**

## Getting started with Edge AI APIs

Edge AI APIs are a set of RESTful web services with data and AI algorithms to support AI applications across distributed hybrid cloud environments. The algorithms address many challenges that arise in these distributed and heterogeneous environments, for example, semantically sub-sample raw data before transporting it over the network, assess and repair data quality issues, select the best model and optimize the model for the edge, and monitor the model’s performance after deployment. These APIs are designed for general purpose use and support many modalities of data such as visual, acoustic, sensors, network logs, time series, and natural language data. Therefore, you can develop a variety of AI applications based on the APIs.

## Edge AI APIs

The Edge AI APIs are comprised of several libraries, each addressing a part of the challenge in enabling AI at the edge. The Edge AI APIs do not focus on the basic requirements of creating and deploying AI pipelines, for example, model training and model serving. For that, you’d use your favorite open source packages such as TensorFlow and PyTorch. Then, you can containerize your application, including the AI pipeline, and deploy these containers at the edge. In many cases, it’s useful to use a container orchestrator such as Kubernetes or OpenShift operators to automate the deployment process.

The Edge AI APIs help you address non-trivial challenges that are associated with optimizing data management and model management across cloud and edge frameworks. Specifically, it enables the following scenarios:

* When collecting data from edges, semantically compress the data depending on the downstream AI task to minimize the cost and resources spent in moving data

* Identify and repair quality issues, including mismatches in schema across edge sites

* After training the models, optimize them for each unique edge environment to ensure the edge resource constraints are met and adapt them to the edge data distributions

* After the models are deployed, check if a new edge sample is an outlier and if the data distribution has shifted

* If data can never leave the edge sites, enable fusing of local edge models into a global model that can be deployed at each edge site

* Enable edge sites to form logical groups, discover resources across the entire group of sites, and communicate among groups

* Define policies on edge data access and enforce them at the edges

## High-level architecture

![High-level architecture](images/figure2.png)

* Edge AI Core API

    * Distributed Registry: Register and find resources (datasets, models, and others)
    * Group Manager: Keep track of service endpoint status as they join and leave
    * Policy Manager: Author and enforce policy rules
    * Messaging: Pub-sub style messaging across edge sites and the cloud

* Coreset API: Algorithms to intelligently sub-sample data before transporting over the network

* Federated Data Ops API: Algorithms to assess the data quality and repair labels and missing values

* Model Fusion API: Algorithms to train the models while data is resident across many sites

* Model Management API: Algorithms to maintain the most suitable models for each site

## Summary

This article provided an overview of Edge AI APIs, a set of RESTful web services with data and AI algorithms to support AI applications across distributed hybrid cloud environments. By using these algorithms, you can address many challenges that arise in distributed and heterogeneous environments.