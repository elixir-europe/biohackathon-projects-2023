---
title: 'Benchmarks for Bioinformatics Workflow Bake Offs'
tags:
  - workflow benchmarks
  - bioinformatics data analysis
authors:
  - name: Vedran Kasalica
    orcid: 0000-0002-0097-1056
    affiliation: 1
  - name: Felipe Morato 
    affiliation: 2
  - name: Anna-Lena Lamrecht
    orcid: 0000-0003-1953-5606
    affiliation: 3
  - name: Magnus Palmblad
    orcid: 0000-0002-5865-8994
    affiliation: 4

affiliations:
 - name: Netherlands eScience Center, Science Park 402, 1098 XH, Amsterdam, Netherlands
   index: 1
 - name: CSC – IT Center for Science, Keilaranta 14, Espoo, Finland
   index: 2
 - name: University of Potsdam, Am Neuen Palais 10, 14469, Potsdam, Germany
   index: 3
 - name: Leiden University Medical Center, Albinusdreef 2, 2333 ZA, Leiden, Netherlands
   index: 4
date: 02 November 2023
bibliography: paper.bib
authors_short: Last et al. (2021) BioHackrXiv  template
group: BioHackrXiv
event: BioHackathon Europe 2021
---

# Introduction or Background

Add to this section a couple of paragraphs introducing the work done dring the BioHackathon, CodeFest, VoCamp or Sprint event. Please add references whenever needed, for instance [@Katayama:2010].

Please separate paragraphs with a double line.

## Subsection level 2

Please keep sections to a maximum of three levels, even better if only two levels.

### Subsection level 3

Please keep sections to a maximum of three levels.

## Task 2

In the second task of the BioHackathon, we discussed the feasibility of mapping EDAM operations to generic or specific technical and scientific run-time benchmarks fit for the purpose of comparing workflows.

During the discussions, we considered three levels of run-time benchmarks:
* Level 0: benchmarks or tests reporting if the component or workflow executed without error or crashing.
* Level 1: benchmarks for a component or workflow that can be computed from any input data
* Level 2: benchmarks for a component or workflow that require ground truth (gold standard) datasets and corresponding expected (correct) output for the component or workflow 

Level 0 may require zero input files (returning a usage string, demonstrating the tool or tools could be accessed and executed), level 1 typically requires at least 1 input file to compute a benchmark dependent only knowing the input file and EDAM operation, and level 2 typically requires at least 2 (the gold standard data and expected output/correct answer). Note that these levels do not correspond to common levels of software testing, but are specifically defined for the testing functionality of individual operations performed by a workflow, where more than one component may be responsible for the output.

### Level 1 benchmarks

The level 1 benchmarks are usually straightforward, such as checking that Format detection [operation:3357] detects a format or Aggregation [operation:3436] outputs a single file. In most cases, the operation itself immediately suggests at least one suitable benchmark that can be checked with a bash command or regular expression. Level 1 benchmarks are purely technical and have no meaningful scientific interpretation. They are similar to the kinds of tests typically performed in automated testing in continuous integration and continuous delivery  pipelines.

### Level 2 benchmarks

The level 2 benchmarks range from the straightforward, such as Format detection determining the correct format or Aggregation output identical to a file provided by the user, to the hard, such as data anonymization [operation:3283], the benchmarking of which has itself been the topic of several recent publications [refs].

To inform discussions, all subclasses Spectral analysis [operation:2945] and Genetic variation analysis [operation:3197], both subclasses of Analysis [operation:2945], and Data handling [operation:2409], in total 28 specific operations in mass spectrometry/proteomics, genomics and general data handling. While some operations, such as Spectrum calculation [operation:3860] and Mass spectra calibration [operation:3627] have unique benchmarks (residual mass measurement error and spectral accuracy respectively), several benchmarks are shared across many operations. Any operation that is expected to output an identifier of a format, gene or protein sequence, or ontology class have the same generic benchmarks, namely whether the output contains an identifier of the correct type (level 1) or the correct identifier (level 2). Similarly, accuracy (fraction correct calls) is a generic benchmark for any operation identifying natural products or peptides from mass spectra, or any type of genomic variants from sequence reads. In situations where the positives and negatives are highly imbalanced, metrics such as the Matthew's correlation coefficient [REF], can be computed from the same information (true and false positives and negatives).

Though preliminary, these results allow us to hypothesize (Figure 2) that the number of generic benchmarks at these levels of the EDAM ontology is an order of magnitude smaller than the number of operations. For the Workflomics project, such mappings between EDAM operations and computable benchmarks are directly useful in benchmarking of automatically generated workflows.

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
A major attraction of a BioHackathon is the opportunity to ask experts in other domains and developers of the resources our project builds on. We are extremely grateful to the BioHackathon organising committee for the opportunity to work on our project in such a stimulating environment. Special thanks to Anna Redondo (BSC, ELIXIR-ES) for liaising between our project, Project #24, the OpenEBench team lead Salvador Capella-Gutierrez and members José Mª Fernández, Eva Martin del Pico, Sergi Aguiló Castillo (on-site) and Dmitry Repchevski (remote) across BioHackathon projects. Thanks to Michael R. Crusoe (VU, ELIXIR-NL/DE) for expert input on CWL and workflow checking, and Hervé Menager (Pasteur, ELIXIR-FR) and Matúš Kalaš (UiB, ELIXIR-NO) for discussions on EDAM and Bioschemas. Thanks also to Project #2 leads Stella Fragkouli (INAB, CERTH GR) and Núria Queralt Rosinach (LUMC, ELIXIR-NL) for expert advice on benchmarking genomic variant calling and discussions on (synthetic) data anonymization with Marcos Casado Barbero (EBI). Finally, thanks to Peter Kok  (eScience Center, NL) for remotely supporting the front-end development.

# References

Leave thise section blank, create a paper.bib with all your references.
