---
abstract: Blockchain is a popular topic these days. Take a spin through the lingo
  and see which industries stand to capitalize on this technology.
authors: ''
completed_date: '2016-05-09'
draft: false
excerpt: Blockchain is a popular topic these days. Take a spin through the lingo and
  see which industries stand to capitalize on this technology.
last_updated: '2017-08-21'
meta_description: Blockchain is a popular topic these days. Take a spin through the
  lingo and see which industries stand to capitalize on this technology.
meta_keywords: blockchain, what is blockchain, blockchain technology
meta_title: 'Blockchain basics: Glossary and use cases'
primary_tag: blockchain
pta:
- None
pwg:
- None
related_content:
- slug: cl-ibm-blockchain-101-quick-start-guide-for-developers-bluemix-trs
  type: tutorials
- slug: build-a-blockchain-network
  type: patterns
- slug: ibm-blockchain-platform-vscode-smart-contract
  type: tutorials
related_links:
- title: More blockchain resources on IBM Developer
  url: /technologies/blockchain/
- title: 'Blockchain basics: Introduction to distributed ledgers'
  url: /tutorials/cl-blockchain-basics-intro-bluemix-trs/
- title: 'IBM Blockchain 101: Quick-start guide for developers'
  url: /tutorials/cl-ibm-blockchain-101-quick-start-guide-for-developers-bluemix-trs/
- title: IBM Blockchain Pulse blog
  url: https://www.ibm.com/blogs/blockchain/
- title: Hyperledger Fabric application samples
  url: https://github.com/hyperledger/fabric-samples
subtitle: Key blockchain terms and infinite potential applications
tags:
- blockchain
title: 'Blockchain basics: Glossary and use cases'
type: tutorial
---

Blockchain is a popular topic these days, to put it mildly! Take a spin through the lingo and see how businesses stand to capitalize on this emerging technology.

## 1 Blocks and blockchain networks

A blockchain is a type of distributed ledger that is shared across a business network. Business transactions are permanently recorded in sequential, append-only, tamper-evident _**blocks**_ to the ledger. All the confirmed and validated transaction blocks are hash-linked from the genesis block to the most current block, hence the name _**blockchain**_.

 <sidebar> <heading>All blockchains are NOT created equal</heading> <p>Can you tell the difference between a <a href="https://www.ibm.com/blogs/blockchain/2017/05/the-difference-between-public-and-private-blockchain/">public vs. private blockchain</a>? Between <a href="https://www.ibm.com/blogs/blockchain/2017/05/the-difference-between-bitcoin-and-blockchain-for-business/">bitcoin vs. blockchain for business</a>?</p></sidebar>

A blockchain is thus a historical record of all the transactions that have taken place since the beginning of the blockchain in the network. The blockchain serves as a single source of truth for the network.

A blockchain network can be either permissioned or permissionless. _**Permissionless**_ networks are open to any participants, and transactions are verified against the pre-existing rules of the network. Any participant can view transactions on the ledger, even if participants are anonymous. Bitcoin is the most familiar example of a blockchain network that is permissionless and public.

_**Permissioned**_ networks, on the other hand, are usually private and are limited to participants within a given business network. On permissioned blockchains, participants are allowed to view only the transactions relevant to them. [Hyperledger](https://www.hyperledger.org/) is a collaborative effort, hosted by the Linux Foundation, to support the development of permissioned blockchains for business.

## 2 Distributed ledgers

A **_distributed ledger_** is a type of database, or system of record, that is shared, replicated, and synchronized among the members of a network. The distributed ledger records the transactions, such as the exchange of assets or data, among the participants in the network. This shared ledger eliminates the time and expense of reconciling disparate ledgers.

 <sidebar> <heading>Benefits of distributed ledgers</heading> <p>Explore the problems and solutions to legacy ledgers in this <a href="/tutorials/cl-blockchain-basics-intro-bluemix-trs/">introduction to distributed ledgers</a>. </p></sidebar>

Participants in the network govern and agree by consensus on the updates to the records in the ledger. No central, third-party mediator, such as a bank or government, is involved. Every record in the distributed ledger has a timestamp and unique cryptographic signature, thus making the ledger an auditable history of all transactions in the network.

One implementation of distributed ledger technology is the open source [Hyperledger Fabric](https://www.hyperledger.org/projects/fabric) blockchain, which is one of several open source projects hosted by The Linux Foundation.

## 3 Participants

A blockchain network for business is a collectively owned peer-to-peer network that is operated by a group of identifiable and verifiable **_participants_**. Participants may be individuals or institutions, such as a business, university, or hospital, for example.

## 4 Assets, transactions, and channels

Anything that can be owned or controlled to produce value is an _**asset**_. Assets can be tangible (such as a car or farm-fresh peaches) or intangible (such as a mortgage or patent). A _**transaction**_ is an asset transfer onto or off of the ledger. In a Hyperledger Fabric blockchain, assets are represented as a collection of key-value pairs (for example, vehicleOwner=Daisy) in binary or JSON form, or both.

In a Hyperledger Fabric blockchain, a **_channel_** is a private "subnet" of communication between two or more specific network members, for the purpose of conducting private and confidential transactions. If two participants form a channel, then those participants &mdash; and no others &mdash; must be authenticated and authorized to transact on that channel and share copies of the ledger for that channel. Thanks to channels, the network members who need private and confidential transactions can coexist on the same blockchain network with their business competitors and other restricted members.

## 5 Consensus

 <sidebar> <heading>Pluggable consensus</heading> <p> <a href="https://www.hyperledger.org/projects/fabric">Hyperledger Fabric</a> is a blockchain framework implementation and one of the Hyperledger projects hosted by The Linux Foundation. <a href="https://www.hyperledger.org/projects/fabric">Hyperledger Fabric</a> allows components, such as consensus and membership services, to be plug-and-play.</p></sidebar>

_**Consensus**_ is the collaborative process that the members of a blockchain business network use to agree that a transaction is valid and to keep the ledger consistently synchronized. Consensus mechanisms lower the risk of fraudulent transactions, because tampering with transactions added to the ledger would have to occur across many places at the same time.

To reach consensus, participants agree to the transaction and validate it before it is permanently recorded in the ledger. Participants can also establish rules to verify transactions. No one, not even a system administrator, can delete a transaction that has been added to the ledger. A trusted network of participants reduces the costs of establishing consensus, relative to the higher costs present in permissionless blockchains.

In a business blockchain, a wide variety of consensus mechanisms are available to choose from. Where trust is high, a simple majority voting may suffice, or the network may choose to use a more sophisticated method.

## 6 Smart contracts and chaincode

**_Smart contracts_** govern interactions with the ledger, and they can allow network participants to execute certain aspects of transactions automatically. For example, a smart contract could stipulate the cost of shipping an item that changes depending on when it arrives. With the terms agreed to by both parties and written to the ledger, the appropriate funds change hands automatically when the item is received.

In the context of Hyperledger Fabric, smart contracts are written into chaincode, and the terms are considered essentially synonymous.

 <sidebar> <heading>A simple chaincode sample</heading> <p>Walk through a <a href="https://hyperledger-fabric.readthedocs.io/en/latest/chaincode4ade.html">chaincode sample</a> that shows you how to create assets on the ledger.</p></sidebar>

in Hyperledger Fabric, **_chaincode_** is a piece of code, written in Go, that defines the network assets and the transaction instructions (business logic) for modifying the assets. Chaincode is installed and instantiated onto a channel by an appropriately authorized member. When a transaction is invoked in that channel, a function in chaincode reads and writes values to the ledger.

## 7 Blockchain applications

A blockchain application requires three interdependent components: the user-facing application, the smart contract, and the ledger.

The top layer is the _**user-facing application**_ that meets the needs of the network participants. The application lets users invoke smart contracts that trigger transactions in the business network. The _**smart contract**_ encapsulates the business logic of the network: assets, ownership, and transfers. Each invocation of a smart contract creates a transaction in the network and updates the ledger. The _**ledger**_ holds the current value of smart contract data (for example, vehicleOwner=Daisy), and is distributed across the network.

## Blockchain use cases

Blockchain technology is a powerful game-changer for many industries because it organizes activities with less friction and more efficiency. And it does so at a greater scale among collaborative participants. Blockchain is already helping reshape industries in domains as varied as finance, healthcare, and government. Here's just a sampling of its infinite possibilities:

* [**Internet of Things**](https://www.ibm.com/internet-of-things/trending/blockchain)
  Freight transportation: Move freight with multiple transportation companies, ensuring transparency and timely delivery
  Component tracking and compliance: Store provenance records for original and replacement parts for fleet maintenance
  Log operational maintenance data: Store operational and maintenance records for sharing among business partners or for regulatory purposes
* [**Identity management**](https://www.ibm.com/blockchain/solutions/identity)
  Build a trusted digital identity
* [**Supply chain**](https://www.ibm.com/blockchain/industries/supply-chain)
  Improve traceability, transparency, and efficiency in the food safety network
* [**Financial services**](https://www.ibm.com/blockchain/industries/financial-services)
  Know Your Customer: Access to trusted up-to-date information on customers improves the accuracy of customer services in financial institutions
  Clearing and settlement: Real-time point-to-point transfer of funds between financial institutions accelerates settlement
  More examples: Letters of credit, Corporate debts and bonds, Trading platforms, Payment remittance, Repurchase agreements, and Foreign exchange
* Healthcare
  Electronic medical records
  Virus banks
  Doctor-vendor RFP services and assurance contracts
  Blockchain health research commons
  Blockchain health notaries
* Insurance
  Claims processing
  P2P insurance
  Ownership titles
  Sales and underwriting
* Government
  Government tender processes
  Voting
  Taxes
* Gaming
* Music

And the list goes on! Check out these and many other [**industries**](https://www.ibm.com/blockchain/industries/) and [**use cases**](https://www.ibm.com/blockchain/use-cases/) that are benefiting from blockchain technology.

## Conclusion

By understanding key blockchain terms, you can begin to appreciate how this dramatically disruptive technology works and how it can be applied to productive use in many industries.

## Next steps

Stop by the [**Blockchain Hub on IBM Developer**](/technologies/blockchain/). It's your source for free tools and tutorials, along with code and community support, for developing and deploying blockchain solutions for business.

Happy blockchaining!