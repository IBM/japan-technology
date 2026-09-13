---
abstract: Learn how to make the most of Hyperledger Fabric, a versatile blockchain
  framework.
authors: ''
completed_date: '2018-07-01'
copyright:
  years: '2018'
draft: false
excerpt: Learn how to make the most of Hyperledger Fabric, a versatile blockchain
  framework.
last_updated: '2018-07-01'
meta_description: Learn how to make the most of Hyperledger Fabric, a versatile blockchain
  framework.
meta_keywords: blockchain, Shikha Maheshwari, hyperledger
primary_tag: blockchain
pta:
- emerging technology and industry
pwg:
- blockchain
related_content:
- slug: cl-blockchain-basics-intro-bluemix-trs
  type: tutorials
- slug: code-pattern-series-build-your-first-blockchain-application
  type: series
- slug: ibm-blockchain-platform-for-icp-full-fabric-deployment
  type: tutorials
related_links:
- title: Hyperledger
  url: https://www.hyperledger.org/
- title: Hyperledger Fabric
  url: https://www.hyperledger.org/projects/fabric
- title: Hyperledger Fabric architecture
  url: https://hyperledger-fabric.readthedocs.io/en/release-1.4/arch-deep-dive.html
subtitle: Learn how to make the most of this versatile blockchain framework
tags:
- blockchain
title: 'Blockchain basics: Hyperledger Fabric'
---

Blockchain technology presents abundant opportunities for innovation. It has the power to revolutionize businesses by fundamentally changing the way business transactions are done.

So what’s the best way for developers to begin developing code for blockchain networks? I recommend starting with a firm grasp of the Hyperledger Fabric project.

[Hyperledger](https://www.hyperledger.org/) is an open source collaborative effort created to advance cross-industry blockchain technologies for business use. This global collaboration is hosted by The Linux Foundation.

Hyperledger incubates and supports a range of blockchain business technologies, frameworks, libraries, and applications. The [Hyperledger project](https://www.hyperledger.org/projects) hosts several blockchain frameworks, including Hyperledger Fabric. This article gives you an overview of what Hyperledger Fabric is, how to use it to build solutions, and how a transaction gets executed in Hyperledger Fabric.

## What is Hyperledger Fabric?

[Hyperledger Fabric](https://www.hyperledger.org/projects/fabric) is an open source framework implementation for private and permissioned business networks, where the member identities and roles are known to the other members. It's designed as a foundation for developing solutions with a modular architecture. It allows components, such as ledger database, consensus mechanism, and membership services, to be plug-and-play. It leverages container technology and delivers enterprise-ready network security, scalability, and confidentiality.

A Hyperledger Fabric network has these components:

* **Assets**. An asset is anything that has value. An asset has state and ownership. Assets are represented in Hyperledger Fabric as a collection of key-value pairs.
* **Shared ledger**. The ledger records the state and ownership of an asset. The ledger consists of two components:

  * The _world state_ describes the state of the ledger at a given point in time. It's the database of the ledger.
  * The _blockchain_ is a transaction log history that records all transactions.

* **Smart contract**. Hyperledger Fabric smart contracts are called _chaincode_. Chaincode is software that defines assets and related transactions; in other words, it contains the business logic of the system. Chaincode is invoked when an application needs to interact with the ledger. Chaincode can be written in Golang or Node.js.
* **Peer nodes**. Peers are a fundamental element of the network because they host ledgers and smart contracts. A peer executes chaincode, accesses ledger data, endorses transactions, and interfaces with applications. Some peers can be _endorsing peers_, or endorsers. Every chaincode may specify an endorsement policy, which defines the necessary and sufficient conditions for a valid transaction endorsement.
* **Channel**. Channels are a logical structure formed by a collection of peers. This capability allows a group of peers to create a separate ledger of transactions.
* **Organizations**. The Hyperledger Fabric network is built from the peers owned and contributed by the different organizations that are members of the network. The network exists because organizations contribute their individual resources to the collective network. Peers have an identity (_digital certificate_) assigned by a Membership Service Provider from its owning organization. Peers of different organizations can be on the same channel.
* **Membership Services Provider (MSP)**. The MSP is implemented as a _Certificate Authority_ to manage certificates used to authenticate member identity and roles. No unknown identities can transact in the Hyperledger Fabric network. It manages user IDs and authenticates all participants on the network which enables Hyperledger Fabric as a Private and Permissioned network.
* **Ordering service**. The ordering service packages transactions into blocks to be delivered to peers on a channel. It guarantees the transaction delivery in the network. It communicates with peers and endorsing peers. The supported configuration mechanisms for the Ordering service are Solo and Kafka.

**Figure 1. The components of a Hyperledger Fabric network (for simplicity, channels are not shown)**

![The components of a Hyperledger Fabric network](images/fig1.png)

## How a blockchain solution works

In a blockchain solution, the Hyperledger Fabric network serves as a back end with an application front-end to communicate with the network. SDKs help you set up the communication between front and back end, such as the Node.js SDK and Java SDK. The SDK provides a way to execute user chaincode, perform transactions in the network, monitor events, etc.

To write a blockchain application, you need to:

1. Write chaincode in a supported programming language like Go.
2. Deploy chaincode on Hyperledger Fabric network.
3. Develop a client application using an SDK.

## How a blockchain transaction is executed

The high-level request flow of a transaction in a Hyperledger Fabric network goes like this:

1. The client connects to a Hyperledger Fabric network using the Node.js or Java&trade; SDK. Using the SDK API, the client creates a transaction and sends it to the endorsing peer.
2. The endorsing peer verifies the client's signature, simulates a transaction, and sends an endorsement signature.
3. If the transaction is endorsed, the client submits the transaction to the ordering service. Otherwise, the transaction is cancelled.
4. The ordering service delivers a transaction to the peers. All peers commit and apply the same sequence of transactions and update their state.

## Summary

Hyperledger Fabric is a blockchain framework implementation. IBM Blockchain solutions and Blockchain Platform as a Service on IBM Cloud both leverage Hyperledger Fabric. Now that you understand what Hyperledger Fabric is and how it works, you're ready to start developing blockchain applications -- so dive in and start experimenting!

## Next steps

* Kick-start your blockchain network now with the [**IBM Blockchain Platform**](https://www.ibm.com/blockchain/getting-started).

* Check out the many blockchain [**code patterns**](/patterns/category/blockchain/) on IBM Developer. They provide roadmaps for solving complex problems with blockchain technology, and include architecture diagrams, code repos, and additional reading.

* Stop by the [**IBM Developer Blockchain hub**](/technologies/blockchain/). It's your source for free tools and tutorials, along with code and community support, for developing and deploying blockchain solutions for business.

## Learn more

* [A deep dive into Hyperledger Fabric architecture](https://hyperledger-fabric.readthedocs.io/en/release-1.4/arch-deep-dive.html)
* [What is Hyperledger?](https://blockgeeks.com/guides/what-is-hyperledger/)