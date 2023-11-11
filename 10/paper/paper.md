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
Here we bring together FAIR Computational Execution practitioners to mature and generalise this approach using Workflow Run Crate.

## Subsection level 2

Please keep sections to a maximum of three levels, even better if only two levels.

### Subsection level 3

Please keep sections to a maximum of three levels.

## Tables, figures and so on

Please remember to introduce tables (see Table 1) before they appear on the document. We recommend to center tables, formulas and figure but not the corresponding captions. Feel free to modify the table style as it better suits to your data.

Table 1
| Header 1 | Header 2 |
| -------- | -------- |
| item 1 | item 2 |
| item 3 | item 4 |

Remember to introduce figures (see Figure 1) before they appear on the document. 

![BioHackrXiv logo](./biohackrxiv.png)
 
Figure 1. A figure corresponding to the logo of our BioHackrXiv preprint.

# Other main section on your manuscript level 1

Feel free to use numbered lists or bullet points as you need.
* Item 1
* Item 2

# Discussion and/or Conclusion

We recommend to include some discussion or conclusion about your work. Feel free to modify the section title as it fits better to your manuscript.

# Future work

And maybe you want to add a sentence or two on how you plan to continue. Please keep reading to learn about citations and references.

For citations of references, we prefer the use of parenthesis, last name and year. If you use a citation manager, Elsevier – Harvard or American Psychological Association (APA) will work. If you are referencing web pages, software or so, please do so in the same way. Whenever possible, add authors and year. We have included a couple of citations along this document for you to get the idea. Please remember to always add DOI whenever available, if not possible, please provide alternative URLs. You will end up with an alphabetical order list by authors’ last name.

# Jupyter notebooks, GitHub repositories and data repositories

* Please add a list here
* Make sure you let us know which of these correspond to Jupyter notebooks. Although not supported yet, we plan to add features for them
* And remember, software and data need a license for them to be used by others, no license means no clear rules so nobody could legally use a non-licensed research object, whatever that object is

# Acknowledgements

We are very grateful to the BioHackathon Europe organising committee for the great opportunity to work on our project in the stimulating environment of this year. Special thanks to Martin Cook (ELIXIR-Hub) for the technical support testing and setting up the needed permissions to successfully synchronize HackMD notes and the repository. Thanks to all the Research Object and Workflow Run RO-Crate communities, because all the invested efforts building these standards have been the starting point of this project.

This work was supported by ELIXIR, the research infrastructure for life-science data.

# References
