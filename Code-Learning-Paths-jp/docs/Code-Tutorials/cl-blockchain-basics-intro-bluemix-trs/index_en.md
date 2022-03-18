---
abstract: Everyone is placing bets on how the blockchain technology will revolutionize
  the way organizations and institutions transact business. Let's look at how a blockchain
  network operates, how you can take advantage of it, and how IBM is helping to advance
  the technology.
authors: ''
completed_date: '2018-03-18'
draft: false
excerpt: Everyone is placing bets on how the blockchain technology will revolutionize
  the way organizations and institutions transact business. Let's look at how a blockchain
  network operates, how you can take advantage of it, and how IBM is helping to advance
  the technology.
last_updated: '2019-06-01'
meta_description: Everyone is placing bets on how the blockchain technology will revolutionize
  the way organizations and institutions transact business. Let's look at how a blockchain
  network operates, how you can take advantage of it, and how IBM is helping to advance
  the technology.
meta_keywords: blockchain basics, what is blockchain, blockchain explained
meta_title: 'Blockchain Basics: Introduction to Distributed Ledgers'
primary_tag: blockchain
private_portals:
- blockchain
pta:
- emerging technology and industry
pwg:
- blockchain
related_content:
- slug: cl-blockchain-basics-glossary-bluemix-trs
  type: tutorials
- slug: cl-ibm-blockchain-101-quick-start-guide-for-developers-bluemix-trs
  type: tutorials
- slug: build-a-blockchain-network
  type: patterns
related_links:
- title: More blockchain resources on IBM Developer
  url: https://developer.ibm.com/technologies/blockchain/
- title: 'Blockchain basics: Glossary and use cases'
  url: https://developer.ibm.com/tutorials/cl-blockchain-basics-glossary-bluemix-trs/
- title: 'IBM Blockchain 101: Quick-start guide for developers'
  url: https://developer.ibm.com/tutorials/cl-ibm-blockchain-101-quick-start-guide-for-developers-bluemix-trs/
- title: IBM Blockchain Pulse blog
  url: https://www.ibm.com/blogs/blockchain/
subtitle: Get to know this game-changing technology and how to start using it
tags:
- blockchain
title: 'Blockchain basics: Introduction to distributed ledgers'
type: tutorial
---

Blockchain's distributed ledger technology is revolutionizing the way organizations conduct their business transactions. This tutorial shows you how a blockchain network operates, how you can take advantage of it, and how IBM and other companies are collaborating to advance the technology across a spectrum of industries. First, a little background is in order.

## Distributed ledgers

A **_distributed ledger_** is a type of database that is shared, replicated, and synchronized among the members of a decentralized network. The distributed ledger records the transactions, such as the exchange of assets or data, among the participants in the network.

Participants in the network govern and agree by consensus on the updates to the records in the ledger. No central authority or third-party mediator, such as a financial institution or clearinghouse, is involved. Every record in the distributed ledger has a timestamp and unique cryptographic signature, thus making the ledger an auditable, immutable history of all transactions in the network.

### The role of business ledgers

In today's connected and integrated world, economic activity takes place in business networks that span national, geographic, and jurisdictional boundaries. Business networks typically come together at marketplaces where the _**participants**_, such as producers, consumers, suppliers, partners, market makers/enablers, and other stakeholders own, control, and exercise their rights, privileges, and entitlements on objects of value known as _**assets**_.

Assets can be tangible and physical, such as cars, homes, or strawberries, or intangible and virtual, such as deeds, patents, and stock certificates. Asset ownership and transfers are the _**transactions**_ that create value in a business network.

Transactions typically involve various participants like buyers, sellers, and intermediaries (such as banks, auditors, or notaries) whose business agreements and contracts are recorded in _**ledgers**_. A business typically uses multiple ledgers to keep track of asset ownership and asset transfers between participants in its various lines of businesses. Ledgers are the systems of record for a business's economic activities and interests.

A typical ledger looks something like this:

 <figure> <img alt="blockchain basics - distributed ledger" height="190" src="images/ledger.png" width="639"></img></figure>

### Problems with current business ledgers

Current business ledgers in use today are deficient in many ways. They are inefficient, costly, and subject to misuse and tampering. Lack of transparency, as well as susceptibility to corruption and fraud, lead to disputes. Having to resolve disputes and possibly reverse transactions or provide insurance for transactions is costly. These risks and uncertainties contribute to missed business opportunities.

Furthermore, out-of-sync copies of business ledgers on each network participant’s own systems lead to faulty business decisions made on temporary, incorrect data. At best, the ability to make a fully informed decision is delayed while differing copies of the ledgers are reconciled.

## What is blockchain

 <sidebar> <p> <strong>Now, could you explain "blockchain" to someone?</strong></p> <p>If you hesitated, you're not alone! The <a href="https://developer.ibm.com/learningpaths/get-started-blockchain/" target="new">Get started with blockchain</a> learning path really breaks it down. Read through it, and you'll be ready to regale your family, neighbors, and co-workers with your new-found fluency!</p></sidebar>

A blockchain is a tamper-evident, shared digital ledger that records transactions in a public or private peer-to-peer network. Distributed to all member nodes in the network, the ledger permanently records, in a sequential chain of cryptographic hash-linked _**blocks**_, the history of asset exchanges that take place between the peers in the network.

All the confirmed and validated transaction blocks are linked and chained from the beginning of the chain to the most current block, hence the name _**blockchain**_. The blockchain thus acts as a single source of truth, and members in a blockchain network can view only those transactions that are relevant to them.

## How blockchain networks work

Instead of relying on a third party, such as a financial institution, to mediate transactions, member nodes in a blockchain network use a consensus protocol to agree on ledger content, and cryptographic hashes and digital signatures to ensure the integrity of transactions.

_**Consensus**_ ensures that the shared ledgers are exact copies, and lowers the risk of fraudulent transactions, because tampering would have to occur across many places at exactly the same time. **_Cryptographic hashes_**, such as the SHA256 computational algorithm, ensure that any alteration to transaction input &mdash; even the most minuscule change &mdash; results in a different hash value being computed, which indicates potentially compromised transaction input. **_Digital signatures_** ensure that transactions originated from senders (signed with private keys) and not imposters.

The decentralized peer-to-peer blockchain network prevents any single participant or group of participants from controlling the underlying infrastructure or undermining the entire system. Participants in the network are all equal, adhering to the same protocols. They can be individuals, state actors, organizations, or a combination of all these types of participants.

At its core, the system records the chronological order of transactions with all nodes agreeing to the validity of transactions using the chosen consensus model. The result is transactions that cannot be altered or reversed, unless the change is agreed to by all members in the network in a subsequent transaction.

## Business benefits of blockchain

In legacy business networks, all participants maintain their own ledgers with duplication and discrepancies that result in disputes, increased settlement times, and the need for intermediaries with their associated overhead costs. However, by using blockchain-based shared ledgers, where transactions cannot be altered once validated by consensus and written to the ledger, businesses can **_save time and costs while reducing risks_**.

Blockchain consensus mechanisms provide the benefits of a consolidated, consistent dataset with reduced errors, near-real-time reference data, and the flexibility for participants to change the descriptions of the assets they own.

Because no one participating member owns the source of origin for information contained in the shared ledger, blockchain technologies lead to increased trust and integrity in the flow of transaction information among the participating members.

Immutability mechanisms of blockchain technologies lead to lowered cost of audit and regulatory compliance with improved transparency. And because contracts being executed on business networks using blockchain technologies are automated and final, businesses benefit from increased speed of execution, reduced costs, and less risk, all of which enables businesses to **_build new revenue streams to interact with clients_**.

## Blockchain applications

Blockchain was first introduced to the market as the [technology underpinning Bitcoin exchanges](https://www.ibm.com/blogs/blockchain/2017/05/the-difference-between-bitcoin-and-blockchain-for-business/), but its practical uses in the world of business extend far beyond cryptocurrency transactions. For example, in finance, blockchain networks allow securities trades to be settled in minutes rather than days. In supply chains, blockchain networks allow the flow of goods and payments to be tracked and logged in real time.

To determine whether your use case is a good fit for blockchain, ask yourself these questions:

1. Is a business network involved?
2. Is consensus used to validate transactions?
3. Is an audit trail, or provenance, required?
4. Must the record of transactions be immutable, or tamper proof?
5. Should dispute resolution be final?

If you answered yes to the first question and to at least one other, then your use case would benefit from blockchain technology. A network always needs to be involved for blockchain to be the right solution, but the network can take many forms. The network can be _between organizations_, such as a supply chain, or the network can be _within an organization_. Within an organization, a blockchain network could be used to share reference data between divisions or to create an audit or compliance network, for example. The network can also exist _between individuals_, who might need to store data, digital assets, or contracts on the blockchain, for example.

See [industry examples](https://www.ibm.com/blockchain/industries/) of how diverse organizations &mdash; in banking and financial markets, supply chain, healthcare, and transportation, for example &mdash; are adopting blockchain to support new business models.

## What is Hyperledger

[Hyperledger](https://www.hyperledger.org/) is an open source effort to advance cross-industry blockchain technologies for business use. It's a global collaboration, hosted by The Linux Foundation&reg;, including leaders in finance, banking, Internet of Things, supply chain, manufacturing, and technology. These 183+ diverse members and nine ongoing projects, including Hyperledger Fabric, work in concert to create an open, standardized, and enterprise-grade distributed ledger framework and code base.

The [Hyperledger Fabric](https://www.hyperledger.org/projects/fabric) framework supports distributed ledger solutions on permissioned networks, where the members are known to each other, for a wide range of industries. Its modular architecture maximizes the confidentiality, resilience, and flexibility of blockchain solutions.

The IBM Blockchain Platform runs on the Hyperledger Fabric framework. Learn more about [Hyperledger Fabric](https://www.hyperledger.org/projects/fabric) and the [IBM Blockchain Platform](https://www.ibm.com/blockchain/platform).

### Enterprise blockchain requirements

We believe that blockchain is a truly disruptive technology that can transform business networks. We also believe that this innovation has to happen in the open, collaborating with other technology companies and industries. To this end, IBM continues to contribute code to several active Hyperledger projects.

From IBM's perspective, industrial-grade blockchain technologies have the following characteristics:

* A **shared, permissioned ledger** is the append-only system of record (SOR) and single source of truth. It is visible to the authenticated members in the business network channels.
* A **consensus protocol** agreed to by all participating members of the business network ensures that the ledger is updated only with network-verified transactions.
* **Cryptography** ensures tamper-proof security, authentication, and integrity of transactions.
* **Chaincode** (also called smart contracts) encapsulates participant terms of agreement for the business that takes place on the network; chaincode is stored on the validating peer nodes in the blockchain.

In addition to these attributes, enterprise blockchain technology needs to meet key industry requirements such as performance, verified identifies, and private and confidential transactions. Hyperledger Fabric has been architected to meet these needs. It is also designed with a pluggable consensus model, allowing businesses to select an optimal algorithm for their networks.

## Get started with blockchain

IBM is the leader in secure open-source blockchain solutions built for the enterprise. As an early member of the Linux Foundation's Hyperledger Project, IBM is dedicated to supporting the development of openly governed blockchains. IBM has worked with over 400 clients across financial services, supply chains, IoT, risk management, digital rights management, and healthcare to implement blockchain applications delivered via the IBM Cloud.

IBM offers a flexible platform and secure infrastructure to help you develop, govern, and operate your enterprise blockchain network. Over 40 active networks with multiple organizations are using the IBM Blockchain Platform to exchange assets every day and improve business processes ranging from food safety to trade efficiencies and digital payments. Learn about [IBM Blockchain solutions](https://www.ibm.com/blockchain/solutions), and see how you can [start using blockchain in your business](https://www.ibm.com/blockchain/getting-started) today.

If you’re a developer, the easiest, most economical way to learn your way around a real business blockchain and start developing blockchain skills and applications now is to install the [Visual Studio (VS) Code extension](https://www.ibm.com/blockchain/getting-started). With the VC Code extension, you can create, test, and debug smart contracts, connect to Hyperledger Fabric environments, and build applications that transact on your blockchain network.

## Conclusion

Blockchain technologies represent a fundamentally new way to transact business. They usher in a robust and smart next generation of applications for the registry and exchange of physical, virtual, tangible, and intangible assets. Thanks to the key concepts of cryptographic security, decentralized consensus, and a shared public ledger (with its properly controlled and permissioned visibility), blockchain technologies can profoundly change the way we organize our economic, social, political, and scientific activities. <br/>  <br/>

## Next steps

We'll conclude this introduction to distributed ledgers with some great ways to continue your blockchain odyssey:

* Stop by the [**Blockchain hub on IBM Developer**](/technologies/blockchain/). It's your source for free tools and tutorials, along with code and community support, for developing and deploying blockchain solutions for business. <br/>  <br/>
* Start working with IBM Blockchain. Our [**IBM Blockchain 101**](/tutorials/cl-ibm-blockchain-101-quick-start-guide-for-developers-bluemix-trs/) tutorial shows you how to build a kick-starter blockchain network and start coding with IBM's next-generation Blockchain platform. <br/>  <br/>
* Watch the four-part [**IBM Blockchain Platform Console Video Series**](/series/ibm-blockchain-platform-console-video-series/), which shows you in detail how to set up a business network on the IBM Blockchain Platform. <br/>  <br/>
* Check out the many [**blockchain code patterns**](/patterns/category/blockchain/), which provide roadmaps for solving complex problems, and include overviews, architecture diagrams, process flows, repo pointers, and additional reading.<br/>  <br/>
* Check out the [**past issues**](/newsletters/blockchain/) of the IBM Developer Blockchain newsletter.<br/>