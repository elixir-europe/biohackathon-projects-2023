---
title: 'BioHackEU23 report: SPLASH - Pushing the boundaries of training development'
title_short: 'BioHackEU23 #34: SPLASH training development'
tags:
  - training
  - life cycle
  - development resources
authors:
  - name: Alexia Cardona
    orcid: 0000-0000-0000-0000
    affiliation: 1
  - name: Alexander Botzki
    orcid: 0000-0001-6691-4233
    affiliation: 2
  - name: Mihail Anton
    orcid: 0000-0002-7753-9042
    affiliation: 3
  - name: Jan Slifka
    orcid: 0000-0002-4941-0575
    affiliation: 4
  - name: Loredana La Pera
    orcid: 0000-0000-0000-0000
    affiliation: 5
  - name: Olivier Sand
    orcid: 0000-0003-1465-1640
    affiliation: 6
  - name: Maria Doyle
    orcid: 0000-0003-4847-8436
    affiliation: 7
  - name: Patricia M. Palagi
    orcid: 0000-0001-9062-6303
    affiliation: 8
  - name: Helena Schnitzer
    orcid: 0000-0002-6382-9452
    affiliation: 9
  - name: Eva Alloza
    orcid: 0000-0000-0000-0000
    affiliation: 10
  - name: Albert Hornos
    orcid: 0000-0002-7330-668X
    affiliation: 10
  - name: Bruna Piereck
    orcid: 0000-0000-0000-0000
    affiliation: 2
  - name: Christof De Bo
    orcid: 0000-0000-0000-0000
    affiliation: 2
  - name: Allegra Via
    orcid: 0000-0000-0000-0000
    affiliation: 11
  - name: Nina Norgren
    orcid: 0000-0000-0000-0000
    affiliation: 12
  - name: Nadja Zlender
    orcid: 0000-0000-0000-0000
    affiliation: 13
  - name: Geert van Geest
    orcid: 0000-0002-1561-078X
    affiliation: 8
  - name: Daniel Wibberg
    orcid: 0000-0002-1331-4311
    affiliation: 9
affiliations:
  - name: ELIXIR-UK, University of Cambridge
    index: 1
  - name: VIB, ELIXIR-BE
    index: 2
  - name: ELIXIR-SE, Chalmers 
    index: 3
  - name: ELIXIR CZ, CTU 
    index: 4
  - name: ELIXIR IT, ISS 
    index: 5
  - name: ELIXIR-FR 
    index: 6
  - name: ELIXIR-IE 
    index: 7
  - name: ELIXIR-CH, SIB Swiss Institute of Bioinformatics 
    index: 8
  - name: ELIXIR-DE, FZJ 
    index: 9
  - name: ELIXIR-ES 
    index: 10
  - name: ELIXIR-SI 
    index: 11
  - name: ELIXIR-DE, FZJ
    index: 12
  - name: ELIXIR-SE, Chalmers 
    index: 13
date: 8 November 2023
cito-bibliography: paper.bib
event: BH23EU
biohackathon_name: "BioHackathon Europe 2023"
biohackathon_url:   "https://biohackathon-europe.org/"
biohackathon_location: "Barcelona, Spain, 2023"
group: Project 34
# URL to project git repo --- should contain the actual paper.md:
git_url: https://github.com/elixir-europe/biohackathon-projects-2023/main/34/paper
# This is the short authors description that is used at the
# bottom of the generated paper (typically the first two authors):
authors_short: First Author \emph{et al.}
---

# Introduction

As part of the BioHackathon Europe 2023, we here report the creation of SPLASH, the one-stop-shop of the ELIXIR Training Platform (ETrP), pushing the boundaries of training development. ETrP services will be promoted on the SPLASH website in order to increase their visibility, accessibility and usage. We also strive to enable more participation within and outside the ELIXIR community.

SPLASH adopts a user-centric approach to present the information sought in a ready-to-use format that will enable the packaging and visibility of the different training resources using the successful model of the RDMkit. 

The ETrP has several successful training products, such as TeSS, the Train-the-Trainer programme, the FAIR training project, relevant papers, a training operational handbook containing guidelines etc. For each of these resources, a single entry point for trainers, training developers,  and training providers has be created.

Furthermore, using the results of brainstorm session preceeding the BioHackathon, a training life cycle with the five stages Plan, Design, Develop, Deliver and Evaluate has been created and the various stages will be linked to the ETrP resources.

SPLASH is based on the ELIXIR Toolkit theme and a beta version is now [available](https://elixir-europe-training.github.io/ELIXIR-Training-SPLASH/). The created digital environment will be connected with the ELIXIR website and TeSS with the possibility to connect to other services in the future. After the BioHackathon, we will also continue to assemble more information for funders of training and the other ELIXIR Platforms and Communities.

# Formatting

This document use Markdown and you can look at [this tutorial](https://www.markdowntutorial.com/).

## Subsection level 2

Please keep sections to a maximum of only two levels.

## Tables and figures

Tables can be added in the following way, though alternatives are possible:

Table: Note that table caption is automatically numbered and should be
given before the table itself.

| Header 1 | Header 2 |
| -------- | -------- |
| item 1 | item 2 |
| item 3 | item 4 |

A figure is added with:

![Caption for BioHackrXiv logo figure](./biohackrxiv.png)

# Other main section on your manuscript level 1

Lists can be added with:

1. Item 1
2. Item 2

# Citation Typing Ontology annotation

You can use [CiTO](http://purl.org/spar/cito/2018-02-12) annotations, as explained in [this BioHackathon Europe 2021 write up](https://raw.githubusercontent.com/biohackrxiv/bhxiv-metadata/main/doc/elixir_biohackathon2021/paper.md) and [this CiTO Pilot](https://www.biomedcentral.com/collections/cito).
Using this template, you can cite an article and indicate _why_ you cite that article, for instance DisGeNET-RDF [@citesAsAuthority:Queralt2016].

The syntax in Markdown is as follows: a single intention annotation looks like
`[@usesMethodIn:Krewinkel2017]`; two or more intentions are separated
with colons, like `[@extends:discusses:Nielsen2017Scholia]`. When you cite two
different articles, you use this syntax: `[@citesAsDataSource:Ammar2022ETL; @citesAsDataSource:Arend2022BioHackEU22]`.

Possible CiTO typing annotation include:

* citesAsDataSource: when you point the reader to a source of data which may explain a claim
* usesDataFrom: when you reuse somehow (and elaborate on) the data in the cited entity
* usesMethodIn
* citesAsAuthority
* citesAsEvidence
* citesAsPotentialSolution
* citesAsRecommendedReading
* citesAsRelated
* citesAsSourceDocument
* citesForInformation
* confirms
* documents
* providesDataFor
* obtainsSupportFrom
* discusses
* extends
* agreesWith
* disagreesWith
* updates
* citation: generic citation


# Results


# Discussion

...

## Acknowledgements

Some of the authors were funded by ELIXIR, the research infrastructure for life-science data, to join the ELIXIR BioHackathon Europe.

## References


