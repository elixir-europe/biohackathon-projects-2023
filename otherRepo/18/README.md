# Project 18: FAIRification of mass spectral library creation

## Abstract

Accurate chemical compound identification is crucial for multiple areas — from safety regulations to discovering novel natural product-based drugs. High-resolution mass spectrometry (HRMS) enables such identification in a precise and robust manner but, in most cases, a reference spectrum is required to identify an unknown compound. 

Despite recent advances in computational approaches for spectral annotation, well-annotated experimental spectral databases remain crucial for high-confidence compound annotations. Multiple open and commercial mass spectral libraries exist at the moment, but there is a pressing need for the improvement of database interoperability and unification of data representation.

Multiple issues must be addressed to increase the FAIRness (findability, accessibility, interoperability, and reusability) of current spectral databases. Across the spectral databases, there is no agreed unified data representation or data curation protocols. Even if spectra are linked to public resources through universal spectral identifiers (USI), it is frequently impossible to trace a spectrum to the raw instrument data and applied spectral filtering. 

This project will provide a platform to discuss and develop a streamlined workflow to create MS reference libraries with entries linked to public data, and to facilitate library publishing as an open resource to MassBank, GNPS, and other spectral data providers. The groundwork includes the unified MZmine (Java) library creation workflows for GC-EI-MS, LC-MSn, and ion mobility-enabled MS; Python-based projects like matchms, MS2Query, mzSpecLib, and R-based [RMassBank](https://bioconductor.org/packages/release/bioc/html/RMassBank.html). Participants will work on spectral quality, filtering, merging, and representation, which will greatly influence machine learning prospects in the field by providing high-quality reference data.

## More information

* In the long term, our project aims to create a sustainable pipeline for unified spectral database creation and community guidelines for spectral library management and exchange. The immediate goal is to update and introduce to the community a spectral library creation workflow.
 * We will split this goal into smaller objectives and use a scrum-based approach for effective interaction between developers. We intend to form sub-teams based on the specialization, including the DevOps CI/CD pipelines and specific tools.
 * Lead developers of MZmine (Robin Schmid, Olena Mokshyna) and [matchms](https://github.com/matchms/matchms)+[MS2Query](https://github.com/iomega/ms2query) (Florian Huber, Niek de Jonge) plan to support this project.
 * The minimum number is 5 people
 * The project welcomes people with any level of programming skills, and we will prepare a range of tasks with varying difficulty levels.
 * [MZmine 3](https://github.com/mzmine/mzmine3) is a modular Java software built on the JavaFX GUI framework. The source code is hosted on GitHub.

## Communication & Contact

Please join the 18_fairification-mass-spectral-libraries channel in the BioHackEU Slack channel. We will coordinate meetings and activities via Slack to help us keep our on-site and remote participants in sync. If you have any questions, please contact one of the project leads below.

[Our main GitHub used for active development during the BioHackathon is over at the mzmine organization](https://github.com/mzmine/biohack23_p15)

## Lead(s)

[Tomáš Pluskal](https://github.com/tomas-pluskal), [Nils Hoffmann](https://github.com/nilshoffmann), [Justin van der Hooft](https://github.com/justinjjvanderhooft)


