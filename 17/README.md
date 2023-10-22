# Project 17: Extending interoperability of experimental data using modular queries across biomedical resources

## Abstract

Integrating experimental data with publicly available resources can provide new insights into biological mechanisms and facilitate scientific discovery. However, the process is complex and time-consuming, especially when dealing with diverse data formats and sources. Here, we propose a modular query-based Python tool to integrate experimental data with existing biomedical resources, focusing on drug discovery. 

This approach employs SPARQL to send queries to different sources and integrates their output. Unlike the Open PHACTS project, which integrated multiple data sources using the RDF data model for drug discovery, we eliminate the need for a data dump thus overcoming the need for sustainability and updation of the RDF dataset. To demonstrate the utility of this approach, we will integrate transcriptomics data from MaayanLab with ELIXIR Core Data Resources like OpenTargets, HPA, and STRING, ELIXIR RIRs such as DisGeNET, ChEMBL, g:Profiler, and ELIXIR-NL resource WikiPathways to enrich the metadata underlying the experimental data to better understand its downstream utility. 

Wherever required, we will use the RIR BridgeDb to map across identifiers from various sources. The tool will assist comprehensive understanding of results from multiple discovery domains. Overall, with the help of the tool, we would improve the accuracy and reliability of drug discovery by enabling researchers to make informed decisions about which candidates to pursue and invest in based on a list of differentially expressed genes. We plan to publish our workflow on WorkflowHub, a registry that enables accessible and interoperable sharing and publishing of computational workflows for reuse.

## More information

Our project requires a minimum of 4-5 participants, including one domain/data expert, Python programmers, topic experts, and individuals knowledgeable in SPARQL and WorkflowHub. 

Our short-term goal is to develop a workflow for modular queries to identify drug candidates from differentially expressed genes. We will prioritize adhering to FAIR principles, ensuring accessibility, interoperability, and reproducibility. 

Our methodology involves integrating data from diverse sources and repurposing existing tools to create a comprehensive drug discovery tool. Our focus during BH 2023, if selected, would be to create and refine the workflow and ensure effective dissemination through platforms such as GitHub and WorkflowHub.

## Lead(s)

Tooba Abbassi-Daloii, Yojana Gadiya, Egon Willighagen ([@egonw](https://github.com/egonw))


