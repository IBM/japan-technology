---
authors: ''
completed_date: '2020-03-17'
components:
- watson-ml-accelerator
- cloud-pak-for-data
draft: false
excerpt: Get an overview of Watson Machine Learning Accelerator and its capabilities.
last_updated: '2021-06-22'
menu_order: 1
meta_description: Get an overview of Watson Machine Learning Accelerator and its capabilities.
meta_keywords: Watson Machine Learning Accelerator, Introduction, overview, get started
meta_title: An introduction to Watson Machine Learning Accelerator
primary_tag: artificial-intelligence
related_content:
- slug: use-computer-vision-with-dli-watson-machine-learning-accelerator
  type: tutorials
- slug: dynamic-resilient-and-elastic-deep-learning-with-watson-machine-learning-accelerator
  type: tutorials
- slug: accelerate-deep-learning-training-with-watson-studio-and-wml-accelerator
  type: tutorials
subtitle: Get an overview of Watson Machine Learning Accelerator and its capabilities
tags:
- machine-learning
- deep-learning
- data-science
title: An introduction to Watson Machine Learning Accelerator
---

The adoption of artificial intelligence (AI) has been increasing across all business sectors as more industry leaders understand the value that data and machine learning models can bring to their business. Faster times to create accurate models are essential to driving value for time to market. 

IBM Cloud Pak for Data provides a unified platform that integrates data and AI services to help you build, run and manage AI. IBM Watson Machine Learning Accelerator is a capability designed to accelerate deep learning with end-to-end transparency and visibility that enables businesses or organizations to bring AI applications into production while making deep learning and machine learning more accessible.

## What is Watson Machine Learning Accelerator?

Watson Machine Learning Accelerator is an enterprise AI infrastructure to make deep learning and machine learning more accessible and brings the benefits of AI to your business. It combines popular open source deep learning frameworks with efficient AI development tools.

Data scientists can accelerate their AI journey by scaling out their workload such as tuning their hyperparameters, while sharing GPU resources in an elastic manner with a growing number of data scientists based on fair share allocation or priority scheduling without interrupting jobs. To quickly learn more, watch the following video.

<video-container><video-id>ylRRXgp1HfY </video-id><video-title display="yes"></video-title>Watson Machine Learning Accelerator 2.2 introduction</video-container>

Watson Machine Learning Accelerator is now available on IBM Cloud Pak for Data, running on Red Hat OpenShift Container Platform and Intel&reg; servers. Watson Machine Learning Accelerator continues to be available on premise for both accelerated IBM Power Systems&trade; servers and Intel servers.


## Deploying Watson Machine Learning Accelerator 

Watson Machine Learning Accelerator can be deployed as a service from IBM Cloud Pak for Data or installed as a stand-alone offering on-premises. To learn about deploying Watson Machine Learning Accelerator as a service, look at <a href="https://www.ibm.com/docs/en/cloud-paks/cp-data/3.5.0?topic=overview" target="_blank" rel="noopener noreferrer">IBM Cloud Pak for Data</a> and the <a href="https://www.ibm.com/docs/en/cloud-paks/cp-data/3.5.0?topic=catalog-watson-machine-learning-accelerator" target="_blank" rel="noopener noreferrer">Watson Machine Learning service</a>. Or, if you're installing and configuring Watson Machine Learning Accelerator on-premises, see <a href="https://www.ibm.com/docs/en/wmla/1.2.3?topic=planning-wml-accelerator" target="_blank" rel="noopener noreferrer">Planning on installing Watson Machine Learning Accelerator 1.2.3</a>. 

## Watson Machine Learning Accelerator capabilities

The following is an overview of the key capabilities of Watson Machine Learning Accelerator.

### Accelerated deep learning utilizing GPUs

Watson Machine Learning Accelerator runs its deep learning jobs on GPU hardware. GPUs are specialized hardware that businesses do not want to sit idle. These specialized hardware allow for faster deep learning results and higher throughput. View this [video](/components/watson-ml-accelerator/videos/deliver-faster-deep-learning-results-on-gpus/) for a notebook example that showcases the speed differences between running training workloads on GPU and CPU. You see that your deep learning training is up to 10 times faster on GPU.

### Elastic Distributed Training

The Elastic Distributed Training capability in Watson Machine Learning Accelerator enables GPU sharing and reallocation across multiple running jobs using the resource policy defined. Resource policies can be defined between lines of business, projects, or users to ensure fair allocation and priority access to GPU resources. As data scientists submit deep learning training jobs, jobs are automatically allocated across shared resources, simplifying the distribution of training workloads. 

See how Elastic Distributed Training balances deep learning jobs with this [video](/videos/balance-deep-learning-jobs-with-elastic-distributed-training/). 

### Automated hyperparameter optimization

Automated hyperparameter optimization helps data scientists optimize the speed of training by automating hyperparameter searches in parallel. See how by using the Watson Machine Learning Accelerator API, you can [automate hyperparameter optimization training](/videos/automate-hyperparameter-optimization-training-with-the-wml-accelerator-api/).

### Elastic distributed inference

Publish inference models as services. To learn more about downloading and configuring inference in Watson Machine Learning Accelerator for Cloud Pak for Data, see <a href="https://www.ibm.com/docs/en/wmla/2.2.0?topic=inference-download-configure-dlim-cli-tool" target="_blank" rel="noopener noreferrer">Downloading the command line tool</a>. If using  Watson Machine Learning Accelerator on-premises, configure the <a href="https://www.ibm.com/docs/en/wmla/1.2.3?topic=inference-using-services-via-cli" target="_blank" rel="noopener noreferrer">command line tool</a>.

## Conclusion

This article provided an overview of Watson Machine Learning Accelerator and its capabilities. To learn more about installing and configuring Watson Machine Learning Accelerator or how to use it, see [How to use Watson Machine Learning Accelerator](/articles/accelerate-dl-with-wmla-and-cp4d/).