---
authors: ''
check_date: '2022-03-01'
collections:
- ibm-research
completed_date: '2021-03-16'
components:
- websphere-hybrid-edition
draft: false
excerpt: Mono2Micro is an evidence-based AI assistant for developers and architects
  to use in application modernization. The goal of Mono2Micro is to provide step-by-step
  guidance to transform your legacy applications in a safe and sound manner with a
  high velocity, rather than try to generate deployable microservices on day one,
  which we believe is not an attainable goal in practice.
last_updated: '2021-03-16'
meta_title: 'A non-disruptive approach to transform Java monoliths to microservices:
  Fast track your application modernization with IBM Mono2Micro'
primary_tag: java
related_content:
- slug: challenges-and-patterns-for-modernizing-a-monolithic-application-into-microservices
  type: articles
- slug: transform-monolithic-java-applications-into-microservices-with-the-power-of-ai
  type: tutorials
subtitle: Fast track your application modernization with IBM Mono2Micro
tags:
- application-modernization
time_to_read: 60 minutes
title: A non-disruptive approach to transform Java monoliths to microservices
---

Many enterprises have business-critical legacy Java EE applications that have been running for a long time, perhaps ten to fifteen years. The applications are difficult to understand, maintain, and enhance, and they are definitely difficult to modernize. Users often want to move these legacy applications to Containers as a Service (CaaS) environments, which is a cloud service model, for agility, selective scalability, maintainability, and economy.

The simple and popular lift-and-shift approach often does not meet the demand for selective scalability and maintainability, which means development teams need to refactor a selected group of applications into microservices. Most of the current approaches to refactoring applications are manual in nature.

<sidebar>To learn more about refactoring applications into microservices, read these articles: <ul><li>[Monoliths to MicroServices](https://samnewman.io/books/monolith-to-microservices/)</li> <li>[How to break a Monolith to Microservices](https://martinfowler.com/articles/break-monolith-into-microservices.html)</li>
<li>[Challenges and patterns for modernizing a monolithic application into microservices](/articles/challenges-and-patterns-for-modernizing-a-monolithic-application-into-microservices/)</li></ul></sidebar>

Naturally, such manual approaches are time consuming and expensive, and they require specialized skills and experience on the part of the developers. Even after spending significant resources on the manual refactoring, efforts often get abandoned due to complexity, unforeseen patterns or dependencies in the code, and inconsistency between architectural knowledge about the original applications and its current implementations.

Users often rely on using the well-known [strangler pattern](http://heidloff.net/article/strangler-pattern-example/) or a domain-driven design to refactor out a few microservices that typically lie on the edge of the applications, while mostly leaving the core business modules of the applications where the actual complexities reside untouched. It should be noted that the successful refactoring of the core business modules of the legacy monoliths provides the maximum ROI in general.

To help improve on this manual process and make it easier to break monoliths in to microservices, IBM built the [Mono2Micro tool](http://www.ibm.biz/Mono2Micro), which is a part of the IBM WebSphere Hybrid Edition offering. For an evaluation of Mono2Micro against other microservice extraction tools primarily used in academia, see the [this conference presentation](https://video.ibm.com/playlist/635256/video/128768365).

## Why is breaking monoliths into microservices so hard?

To describe what Mono2Micro does and why it can be the right fit for many users, let’s first discuss why breaking apart a monolith in a logical manner is so hard.

First and foremost, the legacy aspects of the applications are overwhelmingly complex. The legacy applications we have come across, and where users are struggling the most, are not only of aged designs, but have also been extended and updated over time beyond their original architectural intents, design, and implementation constraints.

New frameworks or design patterns were frequently added to the application. The extensions often duplicated certain functionalities of the application to fit with the new design patterns, while leaving older functional duplicates in places and operating in tandem. Shortcuts and anti-patterns were introduced to previously well-encapsulated objects and well-defined functional interfaces.
These amalgam implementations are no longer clean realizations of the original application architectures. As a result, it is a tremendously difficult undertaking to fully comprehend the actual operational processes in use by the current applications. However, this understanding is a necessary first step before we can begin to wrestle with the ideas and strategies for refactoring such legacy monolith applications.

The second challenge lies in how the enterprise applications were designed and the object-oriented paradigms these applications were implemented under. A typical enterprise application implements one or more centralized business processes that relies on serialized transactions and commonly shares synchronized data objects and states. In contrast, microservices are based on a distributed computing architecture, which foregoes centralized process models and transactions in favor of eventual synchronization and distributed object states. As such, this is a huge paradigm shift in how applications are designed. Developers need to fully understand most of the transactional and object dependencies (both state and data) existing in the legacy monolith applications to determine what can be refactored and also to look for "natural seams" where object dependencies can be minimized.

Static analysis of a monolith is ill-suited for such discoveries because many of these dependency relationships are not immediately apparent from the call graphs and object exchanges. Traditional object-oriented designs complicate the issue further; for example, objects can have strong dependencies with one another through inheritance relations, objects exchanged through parameter passing not only encapsulate data states but also computational logic, and the exact object types or the specific methods invoked are not always precisely defined due to polymorphisms. Consequently, a specific call from one class to another with objects as parameters in practice might very well exhibit different behaviors and involve different types of objects at runtime. This object orientation makes the task of defining clear APIs among refactored code a daunting challenge.

Even when executed with great care, it is quite usual for a refactoring analysis to miss certain dependencies or dynamic behaviors. The realization might not appear during the analysis phase but rather in the execution phase when developers start to implement the refactored services. Herein we arrive at a catch-22 situation, whereby when a refactored application is shown to be erroneous, it is hard to pinpoint the source of such an error. Is it due to a bug introduced during the code tweaking? Is it because of missed dependencies? Are there broken transactions? Or, what about out-of-sync data? And, the list goes on. As a result, when an application refactoring attempt fails, there are few verifiable insights that can be obtained about exactly what went wrong and how to improve. The entire expensive exercise essentially becomes a "sunk cost."

Mono2Micro is specifically designed to deal with these challenges. It ensures that any refactoring recommendations is arrived at on the basis of verifiable evidence. It also ensures that sufficient data points can be obtained through the refactoring exercise such that when issues and unforeseen dependencies are encountered, they can be rapidly diagnosed and pinpointed. Mono2Micro helps in localizing the impact of code changes to each refactored service. Mono2Micro ensures that the existing test cases for the monolith applications can be largely reused for testing their refactored versions.

## Popular approaches to breaking up monoliths

Before focusing on the refactoring methodology of Mono2Micro, let's describe two strategies that are often attempted when converting monoliths to microservices.

### Domain-Driven Design

The [Domain-Driven Design](/tutorials/cl-domain-driven-design-event-sourcing/) is a well-known strategy for identifying service components that can be refactored out from the monolith. It fits with the requirement of a microservice architecture in that if a specific set of code can be identified that implements a well-defined business domain, and the data and interaction boundary of that domain can be cleanly described, then you have a good chance of building an independent set of microservices from it.

In practice, though, identifying a clean domain boundary in a legacy application can be extremely difficult. Business domains are concepts at the business process and architectural level. The actual implementation of this design in Java EE inevitably introduces various classes, methods, and object state dependencies. Also, as mentioned earlier, the extensions and modifications done to the application over time introduce further dependencies that might not agree with the original architectural designs. Consequently, even when starting with a well-intended domain boundary assumption, it is uncertain whether the current code implementation has such a clean boundary.

Often, in these legacy applications, it is quite difficult to determine precisely what needs to be rewritten, how the APIs can be formed, and how object states should be exchanged when working on refactoring the application. Developers have little evidence to suggest whether the domain breakdown at the code level would be realizable. Ideally, developers and architects would like to observe how an application behaves across the potential domain boundaries under various business use cases and then analyze those observations to make further evidence-based assessments, especially during the refactoring exercise.

We believe that Domain-Driven Design is a valuable approach for developing greenfield applications in microservice forms, but it is not very useful for transforming brownfield monoliths to microservices.  

### Strangling legacy applications

<sidebar> You can learn more about the Strangler Pattern in [Martin Fowler’s article]( https://martinfowler.com/bliki/StranglerFigApplication.html) or in this [IBM Garage practices](https://www.ibm.com/garage/method/practices/code/chunking-strategy-strangler-pattern) article.</sidebar>

The [Strangler Pattern](/articles/cl-strangler-application-pattern-microservices-apps-trs/) attempts to identify parts of the application that can be made independent of the main application without much of an effort and then refactor those parts into microservices. Initially, a strangled monolith can continue to operate as a hybrid model; one or a few microservices taken out of the original monolith in conjunction with a version of the original monolith stripped of the components that have been separated and converted to microservices. Eventually, the entire application might be gradually converted into microservices following the same incremental separation principle.

Even though this approach is widely advocated, in practice, it is not easy to identify such stranglers in a legacy application, especially when it comes to the core business logic.

To make such a strangler truly independent, generally three types of dependencies need to be considered:

* **Process dependencies**: Because Java EE applications typically implement a set of business processes, a strangler is truly independent if it can encapsulate an entire process.
* **Application code dependencies**: The code constructs themselves will have dependencies with each other, such as through inheritance, invocation, containment, and parameter passing. For a strangler to be independent, these dependencies need to be either exposed and rewritten as APIs or removed through code rewriting.
* **Object state dependencies**: Different parts of the application and process might have assumptions on a set of common shared object state. For a strangler to be independent, shared object states need to reside in the same service or they need to be transformed to become independent.

In practice, it is often a very difficult task to successfully identify the dependencies deterministically in large applications. This is especially true when some of these dependencies are not apparent from the analysis of the code base itself. Some say that a legacy application is more similar to an ancient oak tree with many crossing branches rather than a strangler fig tree. To manually trace the branching and account for all of the dependencies in order to arrive at viable stranglers one requires an intelligent solution that can cope with high degrees of complexity at scale.

<sidebar>For an illustration of a simple strangler pattern using Mono2Micro, refer to the [Strangler Pattern Example](http://heidloff.net/article/strangler-pattern-example).</sidebar>

Even if we are able to develop such a solution, chances are that we might miss certain hidden dependencies due to the dynamic nature and legacy aspects of the Java EE applications. Hence there is a need to verify whether a refactored service is indeed valid and if not, one should be able to understand what is missing. Mono2Micro helps with the former problem with an AI-assisted refactoring advisory and follows up with guided code generation and post-refactor testing to address the latter.

## The refactoring approach of Mono2Micro

The Mono2Micro tool is an AI-driven approach to application modernization that helps users assess what segments can be refactored from their legacy applications by looking at:

* How the code implementation reflects intended business processes and domains
* How different components of the application interact with each other sequentially and causally under specific business use cases
* What are the observable code and object state dependencies that need to be handled

In this way, Mono2Micro is a bottom-up, guided refactoring solution that grounds the developer’s domain-driven view of a service in what is actually happening at the code level with data-driven decision support on what is refactorable based on their business, budget, time, and resource constraints. The AI mechanisms provide all the evidence to recommend what are likely the sensible partitions in terms of business logic and what are likely the natural seams to consider for implementation. This guidance can be gathered in either one attempt or in stages depending on the developer’s modernization objectives and the estimated efforts.

<sidebar>For an overview of how and what Mono2Micro generates in terms of recommendations and code generation, refer to the ‘Principles of operation’ section of [this article](/articles/advantages-of-using-ibm-mono2micro-to-automate-application-refactoring/). </sidebar>

Mono2Micro also assists users in refactoring the partitions into independent services by automatically generating the code for the partitions that include automatic interface wrapping, distributed object management including parameter passing, monitoring, and exception handling support to help discover what may be missing and why.

### Mono2Micro combines dynamic and static analyses of the application to provide a comprehensive view of the application

In building Mono2Micro, we relied on our field experiences to learn all we could about legacy applications, and we found it is extremely important to analyze the running applications. Runtime information can tell us how the application components interact with each other under specific business use cases, in what temporal order, and discover causal relations that are difficult to obtain through static code analysis alone (for example, how different components of a Java EE service are used to handle a service session, how objects are shared and accessed through frameworks, and so on). Because runtime tracing is highly dependent on the test cases executed and the set of test cases might be incomplete, static analysis is also applied to understand code-level constructs and metadata that are relevant to refactoring such as inheritance and containment relations, objects passed as actual parameters, and certain Java EE framework specific annotations.

### Mono2Micro uses AI to recommend service partitions at scale

Mono2Micro takes into consideration well-defined business use cases and runtime traces between the classes that are generated from executing the appropriate test cases. Mono2Micro uses an unsupervised approach to create partitions. First, it ingests runtime traces as input data collected by executing one or more business use cases where a runtime trace constitutes a temporal sequence of two or more classes and method calls. Then, it uses those traces to extract spatio-temporal relationships between classes. Based on the relationships, it leverages a hierarchical clustering algorithm to partition classes into desired number of partitions. Each partition generated represents one or more underlying business functionalities of the application.

<sidebar>For Mono2Micro's AI algorithm and sample evaluations of partitions using BCP, ICP, and SM, consult this [ACM conference paper](https://www.researchgate.net/publication/345751911_Mono2Micro_an_AI-based_toolchain_for_evolving_monolithic_enterprise_applications_to_a_microservice_architecture).</sidebar>

The partitions are further verified and evaluated based on three metrics:  

* **Business-context purity (BCP)**, which is a measure of the average entropy of business use cases per partition; that is, the functional cohesiveness of a partition in terms of the business use cases it implements. In Mono2Micro, business-context purity favors partitions that implement few related business use cases and therefore is better aligned to domains.
* **Inter-partition calls (ICP)**, which is the percentage of runtime calls that occur between two partitions. In Mono2Micro, inter-partition calls attempt to identify partitions where the inter-partition interactions are minimized both in terms of the number of methods and the call volume, thereby leading to services with cleaner and fewer required APIs.
* **Structural modularity (SM)**, which is a quantification of the modular quality of partitions in terms of the structural cohesiveness of classes within a partition and the coupling between partitions. In Mono2Micro, structural modularity helps in identifying partitions that are more self-reliant in their operations and hence have higher independence.

Mono2Micro also allows users to specify the maximum desired number of partitions to break the application into. The estimation of this number can be obtained by the user’s initial thoughts on the number of services the application is likely to have. The user can further experiment by changing this parameter to see what outcomes make sense by referring to the three different metrics described earlier. Mono2Micro has been proven effective in creating granular, functionally cohesive, loosely coupled, and explainable microservices.

## Mono2Micro assists in code refactoring and troubleshooting

Mono2Micro can help create independently running partitions by providing a set of auto-generated code covering service conversions, object parameter wrappings, distributed object management, and exception handling. The techniques applied mostly preserve the semantic equivalence of the original code base with no modification to the original application code. Therefore, a user not only verifies that all the dependencies with the new service partition are accounted for, but also executes existing test cases to verify that no hidden dependencies were missed. Thus, Mono2Micro helps the users to fact-check their refactored services and assures that all of the dependencies at process, code, and object state levels are accounted for. Users can then make evidence-based assessments of how good their partitioned service is and precisely what needs to be tweaked or rewritten to make it a cloud-native microservice.

## AI-partitioning
One of the powerful features of Mono2Micro is its AI partitioning mechanism. Architects and developers can use the AI partitioning outcomes while working on refactoring their monoliths.

### Working with the AI recommendations

Through the Mono2Micro UI, a user can customize their partitions by moving classes between partitions or even create completely new partitions and assign classes to them by shifting classes from existing partitions. Any changes at the partition level may impact the metrics: BCP, ICP and SM. Since the AI considers all of the metrics in tandem, it is entirely possible that the user might want to favor one metric over another. By moving the classes between partitions, users can explore the what-if scenarios to see how effective their desired partitioning strategy is in terms of these metrics and whether it makes sense to use the partition customization as it stands.

Another interesting aspect of AI-recommended partitions is the possibility of identifying utility classes. Even though the current Mono2Micro solution does not flag them as such, users can identify one or more classes as potential utility classes if they are invoked by many classes from different partitions and are used under many diverse business use cases. For certain applications, these utility classes can be packaged as libraries or replaced by cloud-native services to achieve better service independence.

### Defining business use cases

Runtime traces of the business use cases are the most important data provided by the users to the Mono2Micro AI engine. Ideally, the business use cases should reflect the business domain functions and services that users want to refactor the application into. This can be a specific functionality, such as 'buy stock' or 'sell stock,' or it can be a specific service, such as 'user login.' Users should have the freedom to create a real-world view of the functionalities that make sense to them. At a granular level, they can think of such functionalities as separate and independent implementations of their applications. Users should provide meaningful use case labels that will help architects clearly understand the partitioning evidence that is displayed in Mono2Micro.

## Fast track your refactoring work with Cardinal

Cardinal is the solution component of Mono2Micro that takes as input the application code base, the application metadata, and the class partitions, and then generates the initial code base for the partitions as services.

<sidebar>Details on Cardinal are in the [Mono2Micro User Guide]( https://epwt-www.mybluemix.net/software/support/trial/cst/programwebsite.wss?siteId=911&h=&tabId=), which you can only access after you’ve accepted the license on the trial version.</sidebar>

With the Cardinal component, users can:

* Understand the implication of a partitioned service in terms of how it interacts with the rest of the application
* Its performance aspects on the refactored application
* Detection of any potential errors and issues associated with the refactored service

These data points serve as an invaluable foundation to determine how to rewrite certain parts of the service to make it scalable and more efficient. More specifically, Cardinal implements a set of protocols that make your application work in partitions like they did as a monolith. The resulting partitioned services are largely semantically equivalent to the original monolith.

Cardinal does not alter the original code base. Therefore, users can clearly understand Mono2Micro-generated refactoring at the code level and can test the refactored code with the original test cases. Cardinal provides the users with the following auto-generated functionalities:

* Service wrappings converting inter-partition method calls into APIs
* Client-side wrapping that turns remote objects into proxies to facilitate inter-partition method calls
* Call parameter resolution that does not serialize application objects, but rather passes a globally addressable object reference which any partition can use through proxy
* Distributed object management and garbage collection that ensure a single object instance state across all the partitions
* Dynamic object type resolution to support polymorphism
* Built-in exception handling to support troubleshooting

A commonly asked question around Cardinal is why not just use a remote object protocol like [Java remote method invocation (RMI)]( https://docs.oracle.com/javase/tutorial/rmi/overview.html). The primary reasons are:

* Mono2Micro wants to have all of the client and service wrappings to be done at the code level of the original monolith such that it is easy for users to understand and troubleshoot. This code level encapsulation is the steppingstone toward the final rewriting of the service.
* Cardinal deals with parameter objects in a much more transparent way than RMI without requiring serialization.
* Remote objects in Cardinal are POJOs, and they look and behave exactly like their original classes. This minimizes the impact of change on the existing codebase, and the risk of the error introduction is also significantly reduced.
* The Cardinal protocol does not require object reference to be bounded by an invocation and allows arbitrary call nesting and self-referencing.

### Categories of Classes Generated by Cardinal

The following are the types of classes that are generated by Cardinal, which are reported in the cardinal summary report and also in the comments of the Mono2Micro generated code.

* **Surface Class**. A surface class is a class that is accessed by more than one partition, either through parameter passing, field declaration, or method invocation. A surface class will have three representations: a physical class, service class and a proxy class.
* **Physical Class**. A physical class is the original class from the monolith. It resides in a single partition service.
* **Service Class**. A service API wrapper class for a physical class in a partition. It facilitates all remote invocations to the instances of the physical class coming from outside the partition through service calls.
* **Proxy Class**. A proxy class is a simple representation of a surface class that does not reside in the same partition. It is used to facilitate object accesses and invocations through remote service calls to the partition containing the physical class.
* **Dummy Class**. A dummy class is a class that is not used in a partition as far as Mono2Micro can observe. It is a fail-safe mechanism provided by Cardinal such that if a dummy class is accessed at runtime, an exception is thrown. Dummy classes help to simplify the compilation and the execution of the refactored partitions as each partition would appear to have the same classes and the declarations as in the original monolith. The dummy classes can be removed from each partition after the completion of testing and verification.

### Using Cardinal generated code as the basis for your refactoring work

Cardinal does not generate deployment-ready microservices. Cardinal accelerates the users' refactoring work. It does much more than generating API templates, as it very quickly provides users with an easy way to build and deploy refactored partitions as services and to experiment with the outcome for validation (using monolith test cases), troubleshooting (detecting missed dependencies), and performance assessment (how chatty are the inter-partition calls).
Based on these data points, users can now plan which partitions make sense to rewrite into better microservices, how much effort it might take, or decide whether they should modify the partition recommendations to reflect a different business domain breakdown. The entire process of code analysis, partition recommendations and adjustments, and the execution for evaluation that is provided by Mono2Micro fast tracks the users with a guided and a data-driven approach to their refactoring efforts.

## Summary and next steps

Mono2Micro is an evidence-based AI assistant for developers and architects to use in application modernization. The goal of Mono2Micro is to provide step-by-step guidance to transform your legacy applications in a safe and sound manner with a high velocity, rather than try to generate deployable microservices on day one, which we believe is not an attainable goal in practice.

Mono2Micro understands application modernization is a journey, but the value needs to be unlocked right away and in the right way. From our experiences in real life customer engagements and also with manual refactoring exercises, we’ve learned that different users often want different short-term benefits from their application modernization efforts, and the state of their legacy applications might not be suitable for their immediate needs. Therefore, Mono2Micro quickly helps developers and architects:

* Clean up their code by identifying possible dead code and anti-patterns, and realize values obtained by simple transformations (for example, changing certain inheritance to compositions)
* Identify business domain oriented microservices and discover code-level dependencies of refactoring
* Assess the effort to refactor and also the efficiency of the refactored partitions.

### Acknowledgements
Authors acknowledge the support received from Melissa Modejski, VP, Application Platform and Integration; Dr. Ruchir Puri, IBM Fellow, Chief Scientist, IBM Research; Dr. Nicholas Fuller, Director, IBM Research; and the entire development team of Mono2Micro. Authors also acknowledge the assistance provided by John Meegan (Offering Manager) and Michelle Corbin (Content Developer) to publish this article on IBM Developer.