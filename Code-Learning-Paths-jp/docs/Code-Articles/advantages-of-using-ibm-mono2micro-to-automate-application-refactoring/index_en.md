---
authors: ''
check_date: '2021-08-27'
collections:
- ibm-research
completed_date: '2020-08-27'
components:
- websphere-hybrid-edition
draft: false
excerpt: Accelerate the journey to cloud using IBM Mono2Micro to automate application
  refactoring.
ignore_prod: false
last_updated: '2020-08-27'
meta_description: Accelerate the journey to cloud using IBM Mono2Micro to automate
  application refactoring.
meta_keywords: mono2micro, ibm mono2micro, monoliths, monolithic applications, refactor,
  refactoring, microservices
meta_title: Understand the advantages of using IBM Mono2Micro to automate application
  refactoring
primary_tag: microservices
related_content:
- slug: mono2micro-automate-application-refactoring-using-ai
  type: articles
- slug: introduction-to-mono2micro
  type: videos
- slug: challenges-and-patterns-for-modernizing-a-monolithic-application-into-microservices
  type: articles
subtitle: Accelerate the journey to cloud by quickly refactoring monolithic applications
tags:
- java
title: Understand the advantages of using IBM Mono2Micro to automate application refactoring
---

<!-- ## Before you begin

This tutorial is part of the *[Introduction to IBM Mono2Micro](/series/intro-to-ibm-mono2micro/)* series.

| Level | Topic | Type |
| --- | --- | --- |
| 101 | [Introducing IBM Mono2Micro](/articles/mono2micro-automate-application-refactoring-using-ai/) | Article |
| 101 | [Get a visual introduction to IBM Mono2Micro](/videos/introduction-to-mono2micro/) | Video |
| **102** | **Understand the advantages of using IBM Mono2Micro to automate application refactoring** | **Article** |
| 201 | [Use IBM Mono2Micro to transform monolithic Java applications into microservices with the power of AI](/tutorials/transform-monolithic-java-applications-into-microservices-with-the-power-of-ai/) | Tutorial |

In this series, learn about the key features of IBM Mono2Micro and how to use them to transform monolithic Java applications into microservices. -->

## Introduction

Clients are increasingly trying to shift their applications to the cloud. However, the journey is far from complete. In an [interview](https://newsroom.ibm.com/Why-IBMs-acquisition-of-Red-Hat-is-a-game-changer-for-the-cloud-industry), Arvind Krishna, IBM CEO, pointed out that about 80% of the client's applications have not yet been moved to the cloud. A large number of these applications are in operation for quite some time. For various reasons, they are not getting shifted to the cloud. Perhaps they are so large that simple lift-and-shift or its variations, like re-platforming, may not be that attractive. In many cases, customers want to refactor these applications first before deploying the refactored versions in the cloud to get the maximum benefit out of their modernization investments. Unfortunately, refactoring an application is a nontrivial, complex exercise. No sound but simple methodologies exist for refactoring monolithic applications in an economical non-disruptive fashion.

[IBM Mono2Micro](http://ibm.biz/Mono2Micro), a joint venture of IBM Research and IBM Cloud and Cognitive Software is an ambitious AI-guided attempt to automatically refactor Java monolithic applications to microservices. Mono2Micro equally derives its power from AI and its built-in deep knowledge of the semantics of the Java programming language. Using machine learning (ML) and deep learning (DL), Mono2Micro first refactors the monolithic applications into a number of disjoint partitions (groupings of classes). Operating on these partitions and guided by the semantics of the programming language, Mono2Micro automatically generates code for the partitions to realize them as microservices.

This article, after briefly explaining the operating principles of Mono2Micro, notes interesting results obtained from the application of Mono2Micro in the field. This article compares the underlying strategies of Mono2Micro with those of the similar methodologies or tools for transforming monolithic applications, pointing out the practical usefulness, superiority, and hence a better ROI on Mono2micro when compared to other related utilities in refactoring existing monoliths economically in a safe and sound fashion.

## Principles of operation

Mono2Micro, introduced in the article "[Transform monolithic applications to microservices with IBM Mono2Micro](/articles/mono2micro-automate-application-refactoring-using-ai/)" and this video that explains how you can [automate application refactoring with Mono2Micro](/videos/introduction-to-mono2micro/), combines static as well runtime analysis of applications for generating partitions. `mono2micro-bluejay`, the very first component of Mono2Micro instruments the Java source code by inserting simple print statements to record function entries and exits with timestamps. During the instrumentation process, the component also extracts a number of metadata about all of the classes, one of them being the member attributes of classes. Based on such member attributes, Mono2Micro creates a containment data dependency relationship between classes. Formally speaking, there exists a containment data dependency from class `A` to class `B`, if classes `A` and `B` are non-primitive Java types and class `A` contains at least a member `b` of type `B`.

The user executes all the business uses cases of the applications after building and deploying the instrumented code. The JVM log files will record execution traces based on business use cases executed. The log files along with the metadata generated from the static analysis of the source code are fed into `mono2micro-aipl`, the AI component of Mono2Micro. Using temporal flow analysis, and unsupervised machine learning (ML) and deep learning (DL) techniques `mono2micro-aipl` generates two sets of partitions: partitions based on 'business logic' and partitions based on 'natural seams.' In the first iteration, the business logic-based partitions are derived purely based on execution traces. In the next iteration, all inter-partition data dependencies are eliminated by merging all the related partitions together to form larger partitions, thereby arriving at natural seams. Partitions based on natural seams can *naturally* generate stateless and share nothing microservices, which will directly lead to their independent scalability and disposability.

`mono2micro-ui`, the GUI component of Mono2Micro, renders the important outputs of `mono2micro-bluejay` and `mono2micro-aipl` in an intuitive GUI. Two directed graphs corresponding to two different characteristics of the original monolithic application can be seen in the GUI panels: the containment data dependency obtained from static source code analysis and the runtime calls between classes, as obtained from the analysis of the runtime log files. The two categories of partitions can also be inspected in the GUI. `mono2micro-ui` also allows the user to fine-tune the partition recommendations.

Though natural seams-based partitions appear ideal, from our experience in dealing with customer applications and handling internal legacy monolithic applications, the use of natural seams, in general, produces one or two very large partitions containing all the important classes. The business logic-based partitioning typically yields a larger number of partitions and better distribution of classes among partitions. However, the business logic-based partitioning will almost always be associated with inter-partition data dependencies.

Advanced users with deep architectural and domain understanding of the monolithic application may decide to adjust the partitions recommended by Mono2Micro. In the GUI panel, they can pursue a meet-in-the-middle custom partitioning strategy by following this outline:

* Start from either the natural seams- or the business logic-based partitions.
* Move toward the other side.
* Stop at a point where a balance between three metrics is obtained:
   * Business context purity
   * Inter-partition method invocations
   * Inter-partition data dependencies

Reports generated by Mono2Micro are of great help to users in arriving at custom partitions in an iterative fashion.

Finally, `mono2micro-cardinal`, the component of Mono2Micro dealing with the semantics of programming languages, automatically generates the code for the partitions. More specifically, `mono2micro-cardinal` generates the APIs for invoking the microservices and all of the underlying code for handling distributed object management, garbage collection, and remote-local object translations. For a few edge cases where Mono2Micro cannot generate code, prescriptive guidance is provided to the user with suggestions about handling the issue. From our experience so far, we can say `mono2micro-cardinal` generates more than 80% of the code needed to realize microservices from partitions.

The four main components of Mono2Micro are available as containers in Docker Hub. For details of the components and their usage scenario, refer to the "Mono2Micro User Guide," which is available when you [sign up](http://ibm.biz/Mono2Micro) for the Mono2Micro.

## Results

Mono2Micro and its early versions have generated significant interests from users. As an example, a fortune 100 corporation tried an early version of Mono2Micro and the results obtained were very promising. About two dozen partitions were recommended by Mono2Micro for a monolithic application containing more than one million lines of code in a matter of weeks. All of the generated partitions were verified by SMEs of the corporation. This is in sharp contrast to the manual refactoring effort, which is continuing for more than a year. As a byproduct of the analysis, Mono2Micro pointed out the existence of a significant amount of potential dead code in the application that can be removed to reduce the size and the static complexity of the application. Work is under way to use Mono2Micro in a number of Fortune 500 corporations to refactor monolithic applications selected by them. In a future article, we plan to discuss the results in detail.

## Refactoring versus rewriting

Mono2Micro refactors applications, keeping code-tweaking to bare minimum. Mono2Micro never breaks a class apart; it considers a class to be the encapsulated indivisible smallest unit. Conventional manual approaches of converting monolithic applications to microservices based on the bounded-context, domain-driven analysis typically do not preserve the classes. A significant number of classes implementing core business functionalities are broken apart; existing methods of these classes get distributed among different classes, which often reside in different partitions. Brand new classes also get created during the process. This approach can be viewed as creating a different encapsulation model and hence a different architecture of the original monolithic application, which necessitates a significant amount of code rewrite. This rewriting is invasive, expensive, and risky. In contrast, Mono2Micro only considers class-based refactoring, which results in a non-invasive, safe, and highly economical approach, yielding quickly demonstrable results.

We studied a few manual attempts of refactoring simple applications by IBM internal groups, and in all cases, we noticed that the manual refactoring attempts typically involve significant amount rewriting -- classes implementing a majority of the business functionalities of the original monoliths are broken and rewritten into other classes. From the amount of rewriting needed for simple applications, you can easily speculate that real-life applications might need months, if not years, of work. Rewriting classes introduces one more additional issue to handle in most cases: New test cases have to be developed to validate the functionality of the rewritten microservices. Whereas, for refactored microservices created by Mono2Micro, you should be able to use the same existing test cases of the original monolithic applications.

While redesign and rewrite may be appropriate in some cases where new microservices are getting created, for transforming existing monolithic applications, the refactoring approach of Mono2Micro stands out in economy, simplicity, and effectiveness. The AI-driven refactoring scheme of Mono2Micro does not alter the fundamental encapsulation and the architecture of the monolithic application. It:

* minimizes the need to rewrite code, and
* allows one to reuse existing test cases

thereby providing a substantial ROI to the users.

In a future article, we plan to elaborate the refactoring versus rewriting approaches while converting monolithic applications in a more formal, quantified setup with illustrative examples.

## Other approaches for transforming monolithic applications

There are a few existing approaches for transforming monolithic applications to microservices. Most of them are manual guidelines focusing on [domain-driven design](https://martinfowler.com/tags/domain%20driven%20design.html) (DDD). Although DDD provides a good architectural guidance for designing microservices, the decision on how to define the right domain and how to transform a monolithic application to the desired design is completely up to the architect and developers. The entire process is informal and hence somewhat subjective in nature. In practice, the process demands significant manual effort, which often overrun expected budget. The amount of code rewrite can also be extremely high, which results in prolonged debugging, testing, and verification, and, in extreme cases, projects get abandoned. In comparison, Mono2Micro aims at an efficient, consistent, and effective, mostly automated transformation methodology involving minimal code rewrites.

The before-mentioned DDD-based approach can be automated to a certain extent. There exist two categories of tools that use AI to arrive at partitions. The first category uses AI on the results of static code analysis, while the other category uses runtime analysis. Both of these domain-driven approaches suffer from the shortcomings previously mentioned. Static analysis, though outwardly simple, cannot detect or use the actual temporal flow of control and runtime call volumes, thereby possibly resulting in producing inferior quality partitions in most cases. A static analysis-based tool may create partitions consisting of unused classes. The dead code of legacy applications may also influence the partitioning decisions of static analysis-based tools in adverse ways. A purely dynamic analysis-based approach will not be able to take data dependency into account while recommending partitions.

Mono2Micro considers both static as well as runtime analyses to arrive at two categories of partitions, and it also provides the guidance to users to arrive at customized partitions, which is not supported by any available tool.

Apart from the creation of demonstrably superior quality partitions regarding refactoring, Mono2Micro has the unique ability to generate code for realizing the partitions. The code generation capability can seriously accelerate the journey to the cloud of any corporation by quickly refactoring monolithic applications in a sound, non-invasive, safe way.

## Next steps

Try out the powerful refactoring and code generation functionalities of [Mono2Micro](http://ibm.biz/Mono2Micro). You can test drive all the components of Mono2Micro on your own monolithic applications. You can also quickly try out the AI and code generation components of Mono2Micro for an example monolithic application by using the sample data provided.

Presently, Mono2Micro handles only Java applications, but its simple modular architecture allows one to plug in components for other language too.

Mono2Micro is evolving. We intend to automatically generate the configuration information for the microservices along with many other features.

### Acknowledgements

Melissa Modejski, Director, IBM Cloud and Cognitive Software meticulously reviewed the article and provided many suggestions in improving the technical accuracy and quality of presentation. Authors acknowledge all the help and contributions of Danny Mace, VP, IBM Cloud and Cognitive Software; Dr. Ruchir Puri, IBM Fellow, Chief Scientist, IBM Research; Dr. Saurabh Sinha, IBM Research; Dr. Liana Chen; IBM Research; and the entire development team of Mono2Micro. Suggestions from John Meegan, Offering Manager, Cloud Integration and superb copy editing of Sarah Domina improved the quality of presentation.