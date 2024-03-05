---
title: 'BioHackEU23: FAIR Workflow Execution with WfExS and Workflow Run Crate'
title_short: 'BioHackEU23 #10: FAIR Workflow Ecosystem'
tags:
  - RO-Crate
  - FAIR
  - provenance
  - workflow run
  - workflow ecosystem
authors:
  - name: José M. Fernández
    orcid: 0000-0002-4806-5140
    affiliation: 1
  - name: Paula Iborra
    orcid: 0000-0003-0504-3029
    affiliation: 1
  - name: Sébastien Moretti
    orcid: 0000-0003-3947-488X
    affiliation: 2
  - name: Arun Isaac
    orcid: 0000-0002-6810-8195
    affiliation: 3
  - name: Paul De Geest
    orcid: 0000-0002-8940-4946
    affiliation: 4
  - name: Stian Soiland-Reyes
    orcid: 0000-0001-9842-9718
    affiliation:
      - 5
      - 6

affiliations:
  - name: Barcelona Supercomputing Center (BSC), ELIXIR Spain, Barcelona, Spain
    index: 1
  - name: SIB Swiss Institute of Bioinformatics, Lausanne, VD, Switzerland
    index: 2
  - name: University College London, London, United Kingdom
    index: 3
  - name: ELIXIR@PSB, VIB-UGent Center for Plant Systems Biology, Ghent, Belgium
    index: 4
  - name: Department of Computer Science, The University of Manchester, Manchester, UK
    index: 5
  - name: Informatics Institute, University of Amsterdam, Amsterdam, NL
    index: 6

date: 10 November 2023
authors_short: Fernández \emph{et al.} (2023)
bibliography: paper.bib
event: BioHackEU23
biohackathon_name: "BioHackathon Europe 2023"
biohackathon_url:   "https://biohackathon-europe.org/"
biohackathon_location: "Barcelona, Spain, 2023"
group: Project 10
# URL to project git repo --- should contain the actual paper.md:
git_url: https://github.com/elixir-europe/biohackathon-projects-2023/tree/main/10
---

# Introduction or Background

FAIR Computational Workflows [@goble_fair_2020] argues that workflows should be FAIR scholarly community research objects in their own right as a kind of FAIR Research Software [@barker_introducing_2022]. In this project we go one step further, and argue that workflow executions should also be published with sufficient traces and structured metadata.

Workflow Run RO-Crate is a set of profiles of RO-Crate [@soiland-reyes_packaging_2022] that capture workflow provenance in a lightweight FAIR data package based on existing standards, in order to support traceability, reproducibility and interoperable description of diverse computational analysis. This use of RO-Crate allows the contextualization of a computational workflow and its execution, e.g. relating to people, organisations, projects, funding, data sources and wider research questions and studies.

We have implemented the profile in multiple workflow systems, including Galaxy, COMPSs, StreamFlow, WfExS, Sapporo, Autosubmit. The command line tool runcrate can convert from the precursor CWLProv and display or validate crates according to the profiles. The crates are compatible with ELIXIR's WorkflowHub [@carole_goble_implementing_2021] and support increasing levels of details, including documenting ad-hoc scripts without a workflow engine.

WfExS-backend is a workflow orchestrator designed for reproducible and secure workflow executions in isolated environments (like HPC). Every input, workflow and container being used in an execution must have either a public or permanent identifier, or at least a resolvable URI, so the execution scenario can be materialised. The execution scenario before and/or after the execution can be saved to RO-Crate.

# What is a workflow ecosystem?

## What is a scientific computational workflow?

A scientific computational workflow is a set of computational procedures which are run either sequentially or in parallel over scientific data, like primary data (e.g. raw reads from a sequencer, X-ray or CT-scan images), secondary data (e.g. electronic health records, manuscripts, genomic assemblies, structures, variant databases) or a mix of them. The purpose of an organized execution of this set of computational procedures is providing answers to scientific questions or hypothesis (e.g. is there some mutation related to this disease?).

Although a scientific computational workflow could be a researcher sequentially running the different programs, we are interested on those ones which are represented as a program or a script written in some general purpose computer language, like bash, R or python. A subset of these computational workflows are the ones written using workflow representation languages, which rely on specialized workflow execution engines.

> The complexity of computational workflows, combined with the analysis of biological data being highly dependent on a wide range of software tools, and issues such as variation in operating systems and computational resources, as well as challenges with tool versioning and documentation, resulted in reproducibility becoming a critical concern in computational biology. To address these challenges, computational workflow manager systems (WMS) have been developed to streamline and automate the process of data analysis chaining multiple steps together, simplifying the development, execution, and reproduction of complex computational analyses. We are interested in these subset of FAIR computational workflows that are written using workflow representation languages, which rely on specialized workflow execution engines.


## Roles in a Scientific Workflow Ecosystem

* **Workflow creator**: The authors of a scientific computational workflow. These authors usually provide their workflows through a code repository, or a common place, like a registry or catalog.
* **Workflow registry / catalog**: Recognized place where workflows from more than one author are registered. Depending on the kind of catalog, different workflows could depend on different workflow engines (or even versions). Some catalogs provide services like embedding either textual or semantic annotations about the workflows, and provide permanent identifiers to the different releases of the registered workflows.
* **Scientific data provider**: Workflows both use and consume datasets, and many of them come from scientific data providers. Scientific data providers have several roles: 
  *  They are the authoritative sources of specialized scientific knowledge under the shape of datasets. So, they are data catalogs.
  *  These datasets have attached both permanent identifiers, scientific and technical metadata.
  *  A data provider can also provide some search services, based on the previously mentioned metadata.
  *  When the datasets are under controlled accesss, they act as proxies between the researcher which needs to use a dataset and the data controller who can grant access to it.
* **Software provider**: The different steps of a workflow depend on different software bundles. Depending on the computational language used to represent the workflow, one of these software bundles can be something like a conda package, a software container, or a module in one or another computer language. It is important
* Data deposition facility.
* Workflow execution deposition facility.
* Data indexer.

## Requirements for a FAIR Workflow Ecosystem

All the actors involved in a future FAIR workflow ecosystem should be based on open standards, like GA4GH and Research Object ones. Also, it is highly advisable that both software and data should follow FAIR principles adapted to their landscape, in order to ease the findability and reusability of both software and data.

So, a workflow execution ecosystem could a FAIR ecosystem, in the next sense (terms are conveniently disordered):

* **Interoperable**: Different storage providers, like Zenodo or B2SHARE, should be considered. They have a very rich metadata model which could be mapped in some way to some subset of the metadata. Also, different data consumers and generators of WorkflowRun RO-Crate should be involved in the ecosystem's lifecycle.

* **Findable**: Several mechanisms to index places which are full of crates following WorkflowRun RO-Crate should be designed. If an indexing software were designed, maybe it should also implement a GA4GH DRS interface, in order to abstract the way to fetch the crate locations.

* **Accessible**: The ecosystem needs proper documentation about the protocols being used, how they are used, and the best practices to upload contents to data providers, so their inherent metadata search capabilities can be used.

* **Reusable**: Engines and orchestrators should be able to consume those crates, either by themselves, or with some help. WfExS-backend, workflow orchestrator able to generate and consume RO-Crates to reproduce workflow execution. WfExS delegates workflow execution to existing workflow engines (Nextflow, CWL). 


## Storage providers

B2SHARE is an EUDAT’s mained platform for storing and publishing research data and is a key starting point for making data FAIR. Takes in all metadata fields from [DataCite metadata schema definition v4.3](https://schema.datacite.org/meta/kernel-4.3/), improved support for multiple root schema versions and an updated and improved metadata exporter via OAI-PMH protocol.

B2FIND is an aggregated metadata domain of EUDAT. Based on comprehensive joint metadata catalogue of research data colletions stored in EUDAT data centes and others. Stores metadata through other EUDAT services (like B2SHARE). 


## Ideas: discussion and limitations

* Zenodo allows updating the metadata after the data has been uploaded. Zenodo has the concept of community, where some validation is applied from the community owneres over the entries being attached to that community. Metadata which can be attached goes from references to manuscripts (hopefully the scientific work where the RO-Crate was generated), authorships, funding, data licensing, keywords and so on. There are limitations about the licensing, as a single license can be attached. For restriced access entries the data access conditions can be declared. Sèbastien did the advice that a huge RO-Crate entry (i.e. one with lots of files or huge ones as payload) could have problems, as Zenodo limits to 50GB the total size limit per entry, and 100 files per upload. There is no size limit on the number of entries in communities. 

* A software focused on the generation **and** upload of Workflow Run RO-Crates to Zenodo could book an entry, include the DOI in the generated RO-Crate, reuse part of the metadata already gathered in the execution process, and then decide whether to also skip more or less payloads, based on their public availability, or store them in a separate Zenodo entry.

* B2SHARE supports the concept of communities administering their own metadata schemas and publication requirements. Potential limitations for huge entries, as the maximum size for a record is 20 GB, and the maximum size for a file is 10 GB. ([B2SHARE usage](https://eudat.eu/services/userdoc/b2share-usage#Communities))
    > Interesting training material: [B2SHARE-training](https://github.com/EUDAT-Training/B2SHARE-Training)


* B2FIND uses various protocols to aggregate metadata from different data repositories. It can harvest metadata using protocols like OAI-PMH.

* A community page should be established similar to the ([RO-Crate communit page](https://www.researchobject.org/ro-crate/community.html)). Similarly, a slack channel on the Seek workspace could be created.



<!--
# Discussion

Here we bring together FAIR Computational Execution practitioners to mature and generalise this approach using Workflow Run Crate.
-->

# Acknowledgements

We are very grateful to the BioHackathon Europe organising committee for the great opportunity to work on our project in the stimulating environment of this year. Special thanks to Martin Cook (ELIXIR-Hub) for the technical support testing and setting up the needed permissions to successfully synchronize HackMD notes and the repository. Thanks to all the Research Object and Workflow Run RO-Crate communities, because all the invested efforts building these standards have been the starting point of this project.

This work was supported by ELIXIR, the research infrastructure for life-science data.

# References
