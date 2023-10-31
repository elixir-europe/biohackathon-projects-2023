---
title: 'Ontologies for single cell experiments'
title_short: 'Ontologies for single cell experiments'
tags:
  - single cell
  - ontologies
  - metadata
  - ISA
  - MAGE-TAB
  - plant
authors:
  - name: Hannah Dörpholz
    orcid: 0000-0002-0476-9699
    affiliation: 1
  - name: Sami Saarenpää
    orcid: 0000-0003-4731-6857
    affiliation: 2
  - name: Maja Križnik
    orcid: 0000-0002-5710-9117
    affiliation: 3
  - name: Naveed Ishaque
    orcid: 0000-0002-8426-901X
    affiliation: 4
  - name: Sara Carsanaro
    orcid: 0009-0002-8634-7138
    affiliation: 5

affiliations:
  - name: Forschungszentrum Juelich, CEPLAS, BioSC, Institute of Bio- and Geosciences, IBG-4 Bioniformatics, 52428 Juelich, Germany
    index: 1
  - name: SciLifeLab, KTH Royal Institute of Technology, Solna, Sweden
    index: 2
  - name: National Institute of Biology, Slovenia
    index: 3
  - name: Berlin Institute of Health at Charité – Universitätsmedizin Berlin, Center of Digital Health, Germany
    index: 4
  - name: Department of Ecology and Evolution, University of Lausanne, 1015 Lausanne, Switzerland
    index: 5

date: 30 October 2023
cito-bibliography: paper.bib
event: BioHackEU23
biohackathon_name: "BioHackathon Europe 2023"
biohackathon_url:   "https://biohackathon-europe.org/"
biohackathon_location: "Barcelona, Spain, 2023"
group: Project 30/35
# URL to project git repo --- should contain the actual paper.md:
git_url: https://github.com/elixir-europe/biohackathon-projects-2023/tree/main/30
# This is the short authors description that is used at the
# bottom of the generated paper (typically the first two authors):
authors_short: We dont care about authorship order \emph{et al.} **all authors are in alphabetical order**
---

# Abstract

Research data management is becoming increasingly important in the scientific community. A critical challenge in this field is making research data FAIR (findable, accessible, interoperable and reusable, [pmid:26978244]). Metadata plays a vital role in this challenge as it allows researchers to accurately understand and recreate experiments. To tackle this challenge, various approaches are being taken towards this goal, including the development of domain-overarching and domain-specific standards.

In the plant science community, multiple domain-specific minimal information standards have been developed, such as MIAPPE, MIAME and MINSEQE. These standards are designed to describe specific types of experiments. Recently, a minimal standard for single-cell experiments, minSCe (minimal information about a single-cell experiment), has been introduced [pmid:33188371]. However, it is not yet widely used.

While minimal standards are important, they are only part of the solution. The use of controlled vocabularies and ontology terms is also essential. Ontology terms have a persistent identifier, an expressive name and a curated definition. Using these terms enables different researchers to understand and recreate annotated experiments. In this BioHackathon Europe project, we propose to expand biological and technical metadata schema as well as ontologies for single-cell experiments across domains with a focus on transcriptomics. This will facilitate the sharing and reuse of single-cell data and promote collaboration among researchers in different domains. Our goal is to improve data management practices and enhance the reproducibility of single-cell research.

# Introduction

Here we report the progress made at BioHackathon Europe 2023 for our project titled "Standards and ontologies for single cell experiments". Our project was planned around three work packages: (i) ontologies; (ii) meta-data standard convertors; and (iii) re-annotation of public single-cell datasets.

In the planning phase of the project, we had identified a minSCe [pmid:33188371] and ... **(@Hannah, @Sara, @Mara, @Sami)** as key reference metadata standards to build upon. We wanted the focus to be specifically on establishing a minimal set of terms for single-cell experimentation and not upstream (e.g. organims related) or downstream (e.g. data processing) as to limit the scope of the project to something achievable. 

**@Someone - something about ontologies? We never really discussed this in the planning phase**

 - interactions with other projects and wider initiatiave (not prospective)

In the early planning phases of the project we identified a number of other BioHackathon projects for which there would be potnetial synergies:
 - [Cell type-specific and druggable pathway models and maps (project 09)](https://github.com/elixir-europe/biohackathon-projects-2023/tree/main/9)
 - **@Someone ...?**

To maximise interactions and reduce redundancies between projects, the co-leads met and exchanged updates and progress on prject planning. As such, we organised **a number of/one/two** guest presentations that were develivered to both projects:
 - cellxgene
 - BeeGees

Two weeks before the BioHackathon, the ELIXIR Single Cell Omics community met at Hinxton to address [best practices for single-cell metadata](https://elixir-europe.org/events/elixir-single-cell-omics-community-f2fhybrid-meeting-0) as a part of the [ELIXIR SCONE Implementation Study](https://elixir-europe.org/internal-projects/commissioned-services/2023-SCONE). The participants worked towards establishing a "Rosetta Stone" for translation of metadata standards between major single-cell initiatives (e.g. minSCe, HCA), which methodologically inspired our own project. 

# Heading 2

# Heading 3


## Sub-Heading 3.1

# Results

## Result 1 - Landscaping of existing metadata standards

Trivia: did yo know that organism part is an OTPIONAL metadata term?

## Result 2

## Result 3


## ... Tool Documentation

# Discussion and/or Conclusion

... transgenes ontology?

# Future Tasks: Addressing Shortcomings and Expanding Functionality (old title, but could be used)

.. interaction with ontologists at other institutions e.g. EBI
.. interaction with plant communities (e.g. GRAMENE)

# Jupyter notebooks, GitHub repositories and data repositories

* Please add a list here
* Make sure you let us know which of these correspond to Jupyter notebooks. Although not supported yet, we plan to add features for them
* And remember, software and data need a license for them to be used by others, no license means no clear rules so nobody could legally use a non-licensed research object, whatever that object is

## Acknowledgements
We would like to thank...

@Hannah ... XYZ from the [cellXgene](https://cellxgene.cziscience.com/) initiative for presenting something...

@Sara ... XYZ from the BeeGee project for presenting ...

@Naveed ... members of the ELIXIR Single Cell Omics Community workshop who made the prototype  min single cell metadata sheet

ELIXIR BioHackathon organisers and Chateuform Campus Belloch...

## References

