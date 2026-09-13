---
abstract: Learn the benefits of integrating data science tools and platforms with
  the database compared with in-database analytics, along with features available
  with Netezza Analytics.
authors: ''
completed_date: '2020-12-01'
components:
- netezza-performance-server
draft: false
excerpt: Learn the benefits of integrating data science tools and platforms with the
  database compared with in-database analytics, along with features available with
  Netezza Analytics.
meta_description: Learn the benefits of integrating data science tools and platforms
  with the database compared with in-database analytics, along with features available
  with Netezza Analytics.
meta_keywords: netezza, analytics
meta_title: Access and analyze data in Netezza Performance Server
primary_tag: analytics
related_links:
- description: Netezza Performance Server Community
  title: Netezza Performance Server Community
  url: https://community.ibm.com/community/user/hybriddatamanagement/communities/community-home?CommunityKey=d9f9d5de-e89f-4a6a-84a0-31df8b81f182
subtitle: Explore how in-database analytics compares with integrating tools and platforms
title: Access and analyze data in Netezza Performance Server
---

Data infrastructure is becoming increasingly powerful in order to support the growing need and adoption of analytics. Analytics tools have come a long way, from pulling data from the data source into a separate environment, to pushing analytics into the data source to avoid the overhead in moving data. The same can be said for databases and data warehouses, which have continuously evolved and been able to stay on top of a rapidly changing market. They’re not just used to store large volumes of data; they're critical in maintaining data security and integrity of growing volumes of data, while powering the applications that run our world.

As the world embraced the AI era, these critical systems evolved yet again to support analytics use cases and the heavy demands they require of data management systems. Today, vendors have started to move away from selling a database or data warehouse to marketing and selling the data and analytics solution. While some have tried to integrate data science tools and platforms with the database to make it easier for them to talk to the database, others chose the path of in-database analytics. In this article, we'll talk about both of these methods, their benefits, and when to pick one over the other, with a focus on the features available with Netezza Analytics.

## Netezza Analytics

Netezza&reg; Analytics uses Netezza’s asymmetric massively parallel processing (AMPP) architecture to deliver high throughput on large amounts of data. It encompasses in-database analytics delivered through SQL objects, the support for analytics with Python, R, and Lua, and the ability to run all of this inside the Netezza engine.

### In-database analytics

In-database analytics brings analytic logic to where data resides, and applies (but is not limited) to:

* Data preparation — Involves data cleaning and quality checks, data labeling, feature engineering to improve accuracy, eliminate bias and handle skewed data.
* Model building — Machine learning algorithms access the tables and views directly and use the database’s infrastructure for processing. Machine learning models can be stored and re-trained as new data enters the system.
* Model deployment — Develop sophisticated machine learning models outside the database using dedicated tools in-database to score new data.
* Workload management, query optimization, and automation of tasks inside the database — These smart databases learn from historic behavior and adapt and assign database resources according to the change in workload.

In-database analytics in Netezza Performance Server is delivered through user-defined SQL objects. You can use the in-built algorithms available on Netezza for data preparation, data mining, predictive modeling, and optimization. They range from statistical functions for correlation analysis and hypotheses testing to complex ML algorithms like decision trees and clustering. You can use larger datasets (or the entire dataset) to train your models for more accurate results, re-train your models as new data enters the system, and score new data in real time.

In-database analytics is suitable for complex analytics involving large amounts of data or data that may be updated frequently because it:

* Eliminates the overhead of moving large quantities of data out of the database
* Enables enterprises to protect sensitive data and stay compliant by not having them move data out of the database
* Leverages the computational power and parallelization mechanisms provided by the Netezza appliance

### Integrating data science tools and languages

While the benefits of in-database analytics facilitates and secures complex analytics, along with enabling data scientists to focus on the analytics life cycle, rather than on housekeeping, it isn't suitable for data visualization and exploration. Since these operations aren't typically supported inside databases, and can apply to a subset of the data, we use the support of languages and data science tools, while making this integration seamless and simple to use.

In addition to JDBC and ODBC support, Netezza has native drivers and language support for Python and Go. This native drivers integration empowers data scientists to leverage support for summarization, visualization, and analysis of these languages and their libraries, while keeping the filtering, aggregation, and analytics of terabyte-scale data within Netezza.

For example, the nzpy Python library enables direct integration with Python's pandas data analytics suite, with rich summarization and visualization techniques on top of the large-scale data analytics, preparation, and mining capabilities of Netezza itself. With this library, you can pull filtered or aggregated subsets of data from Netezza into pandas for data exploration and visualization of results to gain insights, distribution of data, or to represent results in a form that's more consumable by different audiences.

### Integrating data warehousing and analytics in one platform

Netezza is tightly integrated in IBM Cloud&reg; Pak for Data, unifying data and AI services spanning the entire analytics lifecycle from data management, data operations, and governance to automated AI in one platform. It allows you to collect data residing on multiple clouds and data management products -- in various formats and with various needs for access control -- and work with all of the data wherever it resides. For example, you could implement data protection rules using IBM Watson&reg; Knowledge Catalog and then use Cognos&reg; Analytics for business intelligence to generate reports or dashboards for different departments.

## Next steps

In this article, I’ve covered a lot of ground, from data science tool integration and in-database analytics to their respective benefits to Netezza Analytics. As a next step, you can investigate these concepts in more depth and get some hands-on experience with the relevant technologies by:

1. Loading and accessing data from Netezza on IBM Cloud Pak for Data by using the nzpy Python library to load the data from CSV files into external tables or IBM Cloud Object Storage.
1. Executing SQL statements to access a subset of the data and visualize the results.