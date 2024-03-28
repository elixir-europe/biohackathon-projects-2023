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

# Background

FAIR Computational Workflows [@goble_fair_2020] argues that workflows should be FAIR scholarly community research objects in their own right as a kind of FAIR Research Software [@barker_introducing_2022]. In this project we go one step further, and we argue that workflow executions should also be published with sufficient traces and structured metadata.

Workflow Run RO-Crate [@leo2023recording] (WRROC) is a set of profiles of RO-Crate [@soiland-reyes_packaging_2022] that capture workflow provenance in a lightweight FAIR data package based on existing standards, in order to support traceability, reproducibility and interoperable description of diverse computational analysis. This use of RO-Crate allows the contextualization of a computational workflow and its execution, e.g. relating to people, organisations, projects, funding, data sources and wider research questions and studies.

We have implemented the generation of RO-Crates following this profile in multiple workflow systems, including Galaxy [@galaxy2022galaxy], COMPSs [@lordan2014servicess], StreamFlow [@colonnelli2020streamflow], WfExS [@fernandez_2023_10068956], Sapporo [@suetake2022sapporo] and Autosubmit [@beltran_mora_2023_10199020] [@manubens2016autosubmit]. The command line tool runcrate [@leo_2023_10203433] can convert from the precursor CWLProv and display or validate crates according to the profiles. The crates are compatible with ELIXIR's WorkflowHub [@carole_goble_implementing_2021] and support increasing levels of details, including documenting ad-hoc scripts without a workflow engine.

WfExS-backend is a workflow orchestrator designed for reproducible and secure workflow executions in isolated environments (like HPC). Every input, workflow and container being used in an execution must have either a public or permanent identifier, or at least a resolvable URI, so the execution scenario can be materialised. The execution scenario before and/or after the execution can be saved to RO-Crate.

# Place of workflow executions in a workflow ecosystem

## What is a scientific computational workflow?

A scientific computational workflow is a set of computational procedures which are run either sequentially or in parallel over scientific datasets, composed by either primary data (e.g. raw reads from a sequencer, X-ray or CT-scan images), secondary data (e.g. electronic health records, manuscripts, genomic assemblies, structures, variant databases) or a mix of them. The purpose of an organized execution of this set of computational procedures is providing answers to scientific questions or hypothesis (e.g. is there some mutation related to this disease?).

Although a scientific computational workflow could be a researcher sequentially running the different programs, we are interested on those ones which are represented as a program or a script written in some general purpose computer language, like bash, R or python. A subset of these computational workflows are the ones written using workflow representation languages, which rely on specialized workflow execution engines, usually known as workflow management systems (WMS).

Reproducibility becomes a critical concern in scientific computational analysis. Concerns arise from the complexity of scientific computational workflows, combined with the analysis of datasets being highly dependent on a wide range of software tools, and issues such as variation in operating systems and computational resources, as well as challenges with tool versioning and documentation. WMS have been developed to streamline and automate the process of data analysis chaining multiple steps together, simplifying the development, execution, and reproduction of complex analyses. Thus, we are interested in the subset of scientific computational workflows featuring FAIR characteristics which rely on specialized workflow execution engines.


## Roles in a Scientific Workflow Ecosystem

* **Workflow creator**: The authors of a scientific computational workflow. These authors usually provide their workflows through a code repository, or a common place, like a registry or catalog.
* **Workflow registry / catalog**: Recognized place where workflows from more than one author are registered. Depending on the kind of catalog, different workflows could depend on different workflow engines (or even versions). Some catalogs provide services like embedding either textual or semantic annotations about the workflows, and provide permanent identifiers to the different releases of the registered workflows.
* **Scientific data provider**: scientific analyses both use and consume datasets, and many of them come from scientific data providers. Scientific data providers have several roles: 
  *  They are the authoritative sources of specialized scientific knowledge under the shape of datasets. So, they are data catalogs.
  *  These datasets have attached both permanent identifiers, scientific and technical metadata.
  *  A data provider can also provide some search services, based on the previously mentioned metadata.
  *  When the datasets are under controlled access, they act as proxies between the researcher which needs to use a dataset and the data controller who can grant access to it.
* **Software provider**: The different steps of scientific analyses depend on different software bundles. In case of WMS, depending on the implemented computational language used to represent workflows, usable software bundles can be something like a conda package, a software container, or a module in one or another computer language. 
* **Data deposition facility**: sustained platforms for storing and publishing research data results from scientific analyses. These facilities can be either public or private registries with controlled access. All of them must provide permanent identifiers, which can be used to request access or fetch associated metadata. 
* **Workflow execution deposition**: comprehensive joint metadata catalogue of workflow execution for a data collection. Registry entries can contain either sucessful or failed executions, containing an associated permanent identifier and additional metadata. 

## Requirements for a FAIR Workflow Execution Ecosystem

All the actors involved in any FAIR workflow execution ecosystem should be based on open standards, like GA4GH and Research Object ones. Also, it is highly advisable that both software and data should follow FAIR principles adapted to their landscape, in order to ease the findability and reusability of building blocks (i.e. software or subworkflows) and data.

Therefore, a workflow execution ecosystem could become a FAIR ecosystem, in the next sense (terms are conveniently disordered):

* **Interoperable**: Different storage providers, like Zenodo or B2SHARE, should be considered. They have a very rich metadata model which could be mapped in some way to some subset of the metadata. Also, different data consumers and generators of WorkflowRun RO-Crate should be involved in the ecosystem's lifecycle.

* **Findable**: Several mechanisms and strategies to index places which are full of crates following WorkflowRun RO-Crate should be designed. If a custom indexing service were designed, it should also implement a sibling open proxy interface (for instance, GA4GH DRS), in order to abstract the way to fetch the crate locations.

* **Accessible**: The ecosystem needs proper documentation about the protocols being used, how they are used, and the best practices to upload contents to the most common data providers, so their inherent metadata search capabilities can be used.

* **Reusable**: There should be engines and orchestrators capable to consume those crates, either by themselves, or with some help.


# Discussion

Many of the needed technologies needed for successful workflow executions ecosystems already exist, as well as services which can cover the described roles above.

## Scientific data storage providers exploration

During the BioHackathon 2023 duration we were exploring the capabilities of Zenodo and B2SHARE storage providers.  The objective was to identify their respective key features for facilitating a FAIR workflow execution ecosystem.

Zenodo is an open-access repository supporting the deposition and citation of research outcomes, including datasets, publications, presentations, and software. It offers long term preservation, persistent identifiers (DOIs), versioning capabilities, and community features, promoting open science and facilitating collaboration. Zenodo allows updating the metadata associated to each entry after an official DOI is minted for the entry. Metadata which can be attached goes from references to manuscripts (hopefully the scientific work where the RO-Crate was generated), authorships, funding, data licensing, keywords and so on. There are limitations about the licensing, as only a single license can be attached. For restricted access entries the data access conditions can be declared. Zenodo has the concept of community, where some validation is applied from the community owners over the entries being attached to that community. Zenodo entries can be harvested through OAI-PMH protocol, improving their findability. There is also a bridge between Zenodo and GitHub, which allows promoting releases of repositories to Zenodo entries, using metadata stored at key files of the repository, like `CITATION.cff`.

The main limitations of Zenodo service are related to the name of the files (they cannot contain the 'slash' directory character, so directories are not allowed), the number of files per entry and the maximum individual size of each file. On one hand, part of these limitations can be overcome just using compressing archive formats, like ZIP. And on the other hand, some of these limitations are relaxed or lifted when the entry is associated to a community with laxer restrictions.


B2SHARE is EUDAT’s maintained platform for storing and publishing research data. In some sense, it has similar purpose and capabilities to Zenodo: long term preservation, DOIs, versioning capabilities and communities. Unlike Zenodo, B2SHARE enforces the adherence of the created entry to one of the existing communities, in order to enforce custom metadata checks and file size restrictions. As Zenodo, B2SHARE allows updating metadata related to already published entries. Metadata fields are based on [DataCite metadata schema definition v4.3](https://schema.datacite.org/meta/kernel-4.3/). B2SHARE also has improved support for multiple root schema versions and an updated and improved metadata exporter via OAI-PMH protocol. Supporting several root schemas, as well as the definition of custom metadata schemas associated to communities allow customizing it for community specific purposes.

As all the B2SHARE entries have to be associated to a community, their managers created an EUDAT community for those entries which cannot be associated to other scientific communities, limiting the file size to 10GB and the size of all the files in the record to 20GB. The names of the files in B2SHARE do not have character restrictions, and there is no limitation in the number of files. Record size limitations can be relaxed on specific communities, and also upon request.

## Scientific data storage providers indexation services

Among all the existing indexation services, we were researching about B2FIND and DataCite services during the BioHackathon 2023 duration.

B2FIND is an aggregated metadata domain of EUDAT. Based on comprehensive joint metadata catalogue of research data collections stored in EUDAT data centres and others. Stores metadata through other EUDAT services (like B2SHARE). B2FIND uses various protocols to aggregate metadata from different data repositories. It can harvest metadata using protocols like OAI-PMH.

[DataCite](https://datacite.org/what-we-do/) is global community aimed to ensure that research outputs and resources are openly available and connected. As a community, they promote a more effective research through the metadata that connects research outputs and resources–from samples and images to data and preprints. One of their main functionalities is the creation and management of persistent identifiers (PIDs), integrate services to improve research workflows, and facilitate the discovery and reuse of research outputs and resources.

## Adoption of Workflow Run RO-Crate

Workflow Run RO-Crate can be naturally used as a reproducible way to describe workflow execution examples and tests. As it was described in the Background section, when BioHackathon Europe 2023 was performed, there were already several programming libraries, WMS and workflow orchestrators implementing WRROC standard. Generated RO-Crates obtained through them hold all the provenance metadata describing workflow or process executions. Although some of the WMS and orchestrators were able to partially consume RO-Crate metadata, no one was able yet to consume already generated WRROC crates in order to reproduce the computational analysis.

In order to improve the adoption, both consumers and WRROC visibility should be improved. Communities of curated RO-Crates focused on either scientific or technical areas should be created in scientific data storage providers, in order to gain traction. A first step is the already existing Research Object community in Zenodo.

Either scientific data storage providers supporting WRROC or specialized WRROC publishing software is needed to ease WRROC distribution. A WRROC publishing software should be able to book an entry, obtain the book permanent id, embed it in the input WRROC and publish it. An advanced WRROC publishing software should be able to also understand and then decide whether to also skip more or less payloads, based on their public availability, or store them in separate records from one or more scientific data storage providers.

# Future work

Although there are several WMS and workflow orchestrators capable to generate WRROC bundles, no one of them had in the event timeframe the capabilities to generate and publish them in coordination with an storage provider. This means that the generated RO-Crates do not contain the permanent identifier assigned to them.

There is a work in progress in WfExS, in order to be able to interleave the generation and upload of WRROC bundles to Zenodo and B2SHARE scientific data storage providers. The milestone is to be able to book an entry along with a DOI, include the DOI in the generated RO-Crate, reuse part of the metadata already gathered in the execution process, and optionally include copies of several parts (i.e. workflow, containers, inputs, outputs, ...) in the RO-Crate bundle.

Also, another scheduled development in WfExS is the capability to consume already generated WRROC crates by WfExS in order to reproduce the computational analysis, allowing the automation of scientific analysis reproducibility.

Last, but not the least important, a community page should be established similar to the ([RO-Crate community page](https://www.researchobject.org/ro-crate/community.html)). Similarly, a slack channel on the Seek workspace could be created.

# Materials and methods

We have used the available documentation provided by the different scientific data storage providers and indexers, both the one describing their capabilities and the one describing their REST APIs.

Proof of concept developments which are being integrated into WfExS-backend are under Apache2 licence.

# Acknowledgements

We are very grateful to the BioHackathon Europe organising committee for the great opportunity to work on our project in the stimulating environment of this year. Special thanks to Martin Cook (ELIXIR-Hub) for the technical support testing and setting up the needed permissions to successfully synchronize HackMD notes and the repository. Thanks to all the Research Object and Workflow Run RO-Crate communities, because all the invested efforts building these standards have been the starting point of this project.

This work was supported by ELIXIR, the research infrastructure for life-science data.

# References
