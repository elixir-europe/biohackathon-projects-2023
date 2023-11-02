# Project 1: A "batteries-included" open reference resource for human genomic copy number variants (CNV)

## Abstract

Interpretation of CNV data is challenging. This is mainly due to the large number of potential CNV events initially called in the analysis of a given biological sample, but especially due to a lack of a high-quality open reference database for CNV representing a "normal background" w/o disease association in the general population.

We propose to build an open reference resource for human CNV based on publicly available datasets from which high quelity CNV events will be curated. We will start using a prototype developed within the ELIXIR hCNV community group, work on making this “Proof of Concept” openly available (guidelines from ELIXIR Tools, https://elixir-europe.org/platforms/tools/software-best-practices) to facilitate contributions from users from other communities, identify and increase the number of datasets to integrate, deploy data wrappers for import and upload of data compliant with the latest file format standards (e.g. VCF 4.4; GA4GH BED 1.0); include data discovery and exchange functionalities based on the latest recommendations from international initiatives (e.g. Beacon v2, GA4GH VRS 1.3) and create connectors to facilitate its use through home-made workflows as well as Galaxy instances.

Importantly, the project will for the first time combine recent standard developments relevant to CNV data, especially with respect to VCF4.4, VRS 1.3 and Beacon v2.n, and provide computational tools for standards conform handling of CNV data to the ELIXIR communities and beyond.

## More information

Last year, hCNV community members started prototyping such a resource, designing the database structure and collecting CNV from the 1KGP Dragen reanalysis initiative. Tasks for this project will be to:

* Adapt the prototype, to make it generic
* identify new datasets to include
* Create API connections to other public data resources for CNV (Progenetix, Decipher, EBI EVA, GnomAD)
* develop uploaders/exporters to facilitate and automate data import/export from VCF (new specifications for CNV/SV), and others ELIXIR and GA4GH data format and exchange formalism (BED)
* Create data connector with Galaxy instances for data exploration
* Make the datasets discoverable through Beacon v2 (e.g. as a dedicated resource on the Progenetix platform and as Galaxy hosted data utilizing the Galaxy Beacon adaptor)
* Project outputs (data code) will be made available under the maximally permissive licence in a git repository to encourage contribution and sustainability and communicated through the cnvar.org website and additional channels.

Any person with interest in one or more of the fields above is welcome to contribute to
the project!

## Lead(s)

David Salgado[^1], Krzysztof Poterlowicz, Michael Baudis, Katarzyna Murat

## Project Outcomes

* Nextflow module to import parsed VCFs into MongoDB
* *  MongoDB_importer.py created
* * **[Nextflow module] (https://github.com/kkamieniecka/modules/tree/beacon2-ri-tools)** under development


https://github.com/kkamieniecka/modules/tree/beacon2-ri-tools

Please see the project's emerging **[website](https://cnvar.org/cnv-reference-resources/)** and **[repository](https://github.com/hCNV/cnv-reference-resources)**  and **[google doc](https://docs.google.com/document/d/1nXo5jtzCg5oC0k7r9Jv0QEo-1wJ0BX0iQb3CBMVLUJA/edit)** for detailed outcomes, resources and examples.

[^1]: Involved in the project's design but won't participate at the Biohackaton...

