---
abstract: Join the blockchain revolution! This quick-start guide is for developers
  who are exploring blockchain technology and want to quickly spin up a blockchain
  pre-production network, deploy sample applications, and develop and deploy client
  applications. Simple instructions show you how to activate a blockchain network
  based on the latest Hyperledger Fabric framework, write and install chaincode (business
  logic for the network), and develop client applications to streamline business processes
  and digital interactions.
authors: ''
completed_date: '2019-05-30'
components:
- hyperledger-fabric
- hyperledger
display_in_listing: true
draft: false
excerpt: Build a kick-starter blockchain network and start coding with the next generation
  blockchain platform from IBM.
last_updated: '2021-05-13'
meta_description: This quick-start guide is for application developers who are exploring
  blockchain technology and want to quickly spin up a blockchain pre-production network,
  deploy sample applications, and develop and deploy client applications.
meta_keywords: blockchain, blockchain explained, what is blockchain
meta_title: 'Blockchain 101: Quick-start guide for developers - IBM'
primary_tag: blockchain
private_portals:
- blockchain
pta:
- emerging technology and industry
pwg:
- blockchain
related_content:
- slug: blockchain-learning-path
  type: series
- slug: cl-blockchain-basics-intro-bluemix-trs
  type: tutorials
- slug: ibm-blockchain-platform-vscode-smart-contract
  type: tutorials
related_links:
- title: Build your blockchain skills with the IBM Developer Blockchain learning path
  url: /series/blockchain-learning-path/
- title: IBM Blockchain Platform Console Video Series
  url: /series/ibm-blockchain-platform-console-video-series/
- title: IBM Blockchain Platform overview
  url: https://www.ibm.com/blockchain/platform
- title: IBM Cloud Kubernetes Service
  url: https://cloud.ibm.com/kubernetes/catalog/cluster?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg
- title: IBM Developer Blockchain code patterns
  url: https://developer.ibm.com/patterns/category/blockchain/
services:
- blockchain
subtitle: Build a kick-starter blockchain network and start coding with IBM's next-generation
  blockchain platform
tags:
- cloud
time_to_read: 1 hour
title: 'IBM Blockchain 101: Quick-start guide for developers'
type: tutorial
---

The blockchain revolution continues! If you’re exploring distributed ledger technology for business use and want to build a business blockchain for demos, pilots, or pre-production staging, this guide is for you. We’ll introduce you to several ways to <a href="#start"><strong>get started now</strong></a>, including the next generation IBM Blockchain Platform.

 <button-link> <text>Kick-start your blockchain journey now</text> <url>https://www.ibm.com/blockchain/getting-started</url></button-link>

This guide shows you how to spin up a blockchain network based on the latest open source Hyperledger Fabric framework using the next generation platform, or building it manually component by component. But let's first review key concepts around developing a business blockchain network.

## Business blockchain concepts

### What is a business blockchain network?

A **_business blockchain network_** is a decentralized network that uses distributed ledger technology (DLT) for the efficient and secure transfer of business assets between member organizations in the network. Assets can be physical or digital, such as vehicles, diamonds, fresh produce, or insurance records. A shared, **_distributed ledger_** records an immutable history of all asset transactions between participants in the network, and catalogs the current state (world state) of those assets. The business rules that govern transactions are agreed upon by members and encapsulated in **smart contracts**.

Instead of relying on a central authority or trusted intermediary, such as a bank or brokerage firm, to validate transactions, members of a blockchain network use a **_consensus_** mechanism to improve transaction processing speed, transparency, and accountability across the network. For additional confidentiality, members join one or more **_channels_** that allow for data isolation; a channel-specific ledger is shared by the authenticated peers in that channel.

A blockchain network for business is collectively owned and operated by a group of identifiable and verifiable institutions, such as businesses, universities, or hospitals. In such a **_permissioned network_**, the participants are known to each other, and transactions are processed much faster than in a non-permissioned, public network like the Bitcoin network. In the Bitcoin network, members are anonymous, forcing the reliance on "proof-of-work" and other types of consensus mechanisms that require time-consuming computations to confirm identities and validate transactions.

Need more background?

* Check out our [Introduction to distributed ledgers](/tutorials/cl-blockchain-basics-intro-bluemix-trs/).
* Watch the four-part [IBM Blockchain Platform Console Video Series](/series/ibm-blockchain-platform-console-video-series/), which shows you how to set up a business network on the IBM Blockchain Platform.

### The open source engine of business blockchains: Hyperledger Fabric

To meet modern business demands, IBM has joined with other companies to collaboratively develop an open source, production-ready, business blockchain framework, called **_Hyperledger Fabric_**&trade;, one of the Hyperledger&reg; projects hosted by The Linux Foundation&reg;. Hyperledger Fabric supports distributed ledger solutions on permissioned networks for a wide range of industries. Its modular architecture maximizes the confidentiality, resilience, and flexibility of blockchain solutions. 159 engineers from 27 organizations contributed to Hyperledger Fabric v1.0. This signified the first production-ready business blockchain framework. In January of 2019, Hyperledger Fabric announced the release of the first Long Term Supported (LTS) project with v1.4. With subsequent LTS releases following, find the latest information from the [official site](https://github.com/hyperledger/fabric#releases). In January of 2020 on the 4th birthday of Hyperledger Fabric, V2 became generally available, introducing some tremendous new capabilities.

Dive deeper:

* [Hyperledger Fabric project overview](https://www.hyperledger.org/projects/fabric)
* [Top 6 technical advantages of Hyperledger Fabric for blockchain networks](https://developer.ibm.com/articles/top-technical-advantages-of-hyperledger-fabric-for-blockchain-networks/)

### IBM's enterprise-ready platform: The IBM Blockchain Platform

The [IBM Blockchain Platform](https://www.ibm.com/blockchain/platform/) is a blockchain offered in two ways: either software-as-a-service offering on the IBM Cloud or via software to be deployed on any Kuberenetes cluster v1.17 or higher.  It's the only fully integrated, enterprise-ready blockchain platform that's designed to simplify the development, governance, and operation of a decentralized, multi-institution, multi-cloud business network. The IBM Blockchain Platform accelerates collaboration in this decentralized world by leveraging open source technology from the Hyperledger Fabric framework.

The IBM Blockchain Platform makes it fast and easy for network members to start developing and quickly move to a collaborative environment with the performance, privacy, and security for even the most demanding use cases and regulated industries.

#### Start small and grow

The IBM Blockchain Platform allows you to deploy only what you need and dynamically add to your environment; you can alter the resources (CPU/Memory/Storage) on the individual nodes, or you can add more nodes in and of themselves. You can migrate from proof-of-concept to pilot to production on a secure, high-performance, and fully scalable network that you can’t outgrow. The newest options give you the flexibility to bring your own infrastructure and deploy anywhere. This means deploy on-prem, or another hosting provider, while connecting your blockchain nodes and members together to transact. All this with the same look, feel and easy to use tooling that the IBM Blockchain Platform provides. The platform is designed to be an easy and economical on-ramp to developing and testing pre-production applications through growing production ecosystems.

Discover the IBM Blockchain Platform:

* [IBM Blockchain Platform overview](https://www.ibm.com/blockchain/platform)
* [Develop, govern, and operate your business network with the IBM Blockchain Platform](/tutorials/cl-ibm-blockchain-platform-develop-govern-operate-your-business-network/)

## What's in the IBM Blockchain Platform {: #sp}

The easiest and most economical way for developers to get started with blockchain development is the [IBM Blockchain Platform on Red Hat Marketplace](https://marketplace.redhat.com/en-us/products/ibm-blockchain). This development and testing environment is ideal for network operators and developers who are exploring blockchain technology or want to build a blockchain network for demos, pilots, or proof of concepts.

Any developer &mdash; whether enterprise, start-up, academic, novice, or experienced &mdash; can deploy code to a full-function, multi-organization blockchain network with the IBM Blockchain Platform.

With the IBM Blockchain Platform, you get:

**Build**

* [Ability to deploy on any cloud or in your own private cloud](https://www.ibm.com/blogs/blockchain/2019/02/taking-the-next-step-towards-deploying-blockchain-anywhere/)
* [VS Code IDE plug-in and code samples](/tutorials/ibm-blockchain-platform-vscode-smart-contract/) make it easier to develop smart contracts
* Single-node deployment enables more granular control
* Management of your infrastructure and sole access to your private keys
* Dev-to-test in a single instance helps shorten time to market

**Operate and govern**

* Unlimited use cases, channels, and configurations in a single instance enable flexibile network configurations
* Identities, ledgers, and smart contracts allow for better control and ownership
* Current Hyperledger Fabric capabilities offer the benefits of more up-to-date technology

**Grow**

* Ability to connect a single peer to multiple ordering services enables flexible network configurations
* Infrastructure via IBM Kubernetes Service allows for better control and ownership
* Flexible pricing allows you to start small and pay as you grow for what you use with no up-front investment

## Start now! Kick-start your blockchain network using the IBM Blockchain Platform on Red Hat Marketplace {: #start}

The easiest, most economical way to learn your way around a real business blockchain and start developing blockchain skills and applications now is to sign up for the IBM Blockchain Platform on Red Hat Marketplace.

### Deploy a sample business network

Step-by-step, learn how to deploy a sample network to the IKS Free Tier. Then you can start developing, demoing, and staging your blockchain applications on a simulated multi-organization network.

1. Sign up for a [free trial](https://marketplace.redhat.com/en-us/products/ibm-blockchain) using your Red Hat account.
1. When you see the launch button, you can enter the blockchain console where you will see a quick-start tutorial, along with the different nodes that you can deploy.
1. If you select the quick start, you'll be guided through a series of easy steps to "Build a network," "Join a network," or "Deploy a smart contract on the network."

For complete details, see the IBM Blockchain Platform documentation. Here’s a preview of what you'll be guided to do:

* **Deploy** a certificate authority, ordering service node, or peers.
* **Create** identities and channels.
* **Model** your business network by defining the asset classes, participant classes, transaction classes, event classes, and access control rules.
* **Write** a smart contract, install a smart contract, instantiate a smart contract, and send a transaction using your client application.

## What's *not* in the free tier?

The Free Tier is optimized to give you a view into the operational tooling, and to help you do quick development and testing. It differs from the Standard plans in several ways:

* It will be automatically removed after one month, and there is no way to migrate to a Standard tier -- so don't plan on the data remaining beyond this one-month threshold as the entire instance will disappear.
* It should not be used for stress testing. This is a free resource and IBM is incurring all of the costs, so to make this available at no cost IBM has to limit the resources allocated to these instances.
* There is no maintenance applied to these deployments. If a new version of Hyperledger Fabric becomes available, IBM will not upgrade the Free Tier instances to this new level; you will need to delete and restart the IBM Blockchain Platform instance anew.

## What's beyond the free tier?

When you're ready to really get going, grow your network, and deploy your network definition, smart contract, and applications to a production environment with added layers of hardened security and premium support, you'll want the [IBM Cloud](https://cloud.ibm.com/catalog/services/blockchain-platform?cm_sp=ibmdev-_-developer-tutorials-_-cloudreg).

With a Standard plan, you get the ability to add more IBM Blockchain Platform nodes, more resources (compute and storage), plus a crash-tolerant, production-level infrastructure that runs in a secure-cloud, Kubernetes-based portable environment. This includes runtime/data isolation, high availability for the ordering service and certificate authority, and the ability to use multiple zones for disaster recovery.

## Why not just use open source technologies directly on your own computer?

A locally deployed blockchain based on the Hyperledger Fabric framework can be a terrific simulation. But without access to other member organizations, you can't experience or test the scalability and power of a multi-organization network. In addition, using the open source technologies locally requires a bit more patience and dexterity with command-line coding.

Conversely, with the IBM Blockchain Platform, you get a scalable, reliable, fully integrated set of operational and governance tools that guide you through network creation, deployment, monitoring, and governance with simple clicks and easy instructions. The code and skills you develop are easily transferable to production environments, so when you're ready to move to a full-scale network in production you will have the exact same experience.

In addition, you get direct access to experts who continue to be dedicated and contribute to the open source code base along with the IBM Blockchain Platform tooling we provide.

## Looking to quickly develop and/or test a smart contract?

The easiest, most economical way to learn more about developing smart contracts for Hyperledger Fabric is to get the free [IBM Blockchain Platform VS Code extension](https://marketplace.visualstudio.com/items?itemName=IBMBlockchain.ibm-blockchain-platform). There are several built-in samples that can help you get started, including commercial paper and FabCar. Once you install the extension, you can create your first smart contract by walking through [this tutorial](/tutorials/ibm-blockchain-platform-vscode-smart-contract/).

With the VS Code extension, you can quickly develop, package, and deploy your smart contracts with easy management of multiple workspaces. Plus, the extension has a built-in local Hyperledger Fabric installation to test your smart contract quickly. In addition, you can easily connect to remote networks, which enables you to deploy your packaged smart contracts to any network in which you participate.

## Get help and support

There are lots of ways to get support and answers to your questions.

1. For general blockchain questions: <br/> Search the [IBM Community](https://community.ibm.com/community/user/ibmz-and-linuxone/groups/topic-home/discussions?communitykey=d92f829f-9174-4aa9-9ee3-54da65afaf87&tab=discussions). Browse questions that have already been asked, or submit a new question (include the keyword **blockchain**). <br/>  <br/>
2. For help with the IBM Blockchain Platform: <br/> The **Support** section in the UI provides many resources for self-help as well as release notes. For software defects or a problem that eludes the given resources, you'll find instructions to submit a support case in the IBM Cloud Service Portal. When you submit a support case, you get an email response within minutes. <br/>  <br/>
3. For specific Hyperledger Fabric implementation questions: <br/> The [Hyperledger Rocket.Chat channels](https://chat.hyperledger.org/home) and [Stack Overflow](https://stackoverflow.com/questions/tagged/hyperledger-fabric) are your best bets. <br/>  <br/>

## Next steps

We'll conclude with some great ways to build your blockchain skills:

* Take the next steps in your blockchain learning journey -- follow along with the [IBM Developer Blockchain learning path](/series/blockchain-learning-path/).
<br/>
* Stop by the [Blockchain content hub](/technologies/blockchain/) on IBM Developer. It's your source for tools and tutorials, along with code and community support, for developing and deploying blockchain solutions for business. <br/>  <br/>
* Watch the four-part [IBM Blockchain Platform Console Video Series](/series/ibm-blockchain-platform-console-video-series/), which shows you in detail how to set up a business network on the IBM Blockchain Platform. <br/>  <br/>
* Check out the many [blockchain code patterns](/patterns/category/blockchain/) on IBM Developer, which provide roadmaps for solving complex problems, and include overviews, architecture diagrams, process flows, repo pointers, and additional reading.