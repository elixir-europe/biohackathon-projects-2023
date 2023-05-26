# Project 14: Enabling continuous RDM using Annotated Research Contexts with RO-Crate profiles for ISA

## Abstract

A prevailing paradigm in Research Data Management (RDM) is to publish research datasets in designated archives upon conclusion of a research process. However, it is beneficial to abandon the notion of ""final"" or ""static"" data artifacts and instead adopt a continuous approach towards working with research data, where data is constantly archived, versioned, and updated. This ""immutable yet evolving"" perspective allows for the application of existing technologies and processes from software engineering, such as continuous integration, release practices, and version management backed by decades of experience, and adaptable to RDM.

To facilitate this, we propose the Annotated Research Context (ARC), a data and metadata layout convention based on the well-established ISA model for metadata annotation and implemented as Git repositories. ARCs are amenable towards frequent, lightweight data management operations, such as (meta)data validation and transformation. The Omnipy Python library is designed to help develop stepwise validated (meta)data transformations as scalable data flows that can be incrementally designed, updated, and rerun as requirements or data evolve.

To demonstrate the concept of ""continuous RDM"" we will use Omnipy to define and orchestrate Git-backed CI/CD (Continuous Integration/Continuous Delivery) data flows to convert ISA metadata present in ARCs into validated RO-Crate representations adhering to the Bioschemas convention. A RO-Crate package combines the actual research data with its metadata description. Downstream, this allows semantic interpretation by Galaxy for e.g. workflow execution as well as machine-readable data access and data harvesting for search engines such as FAIDARE.

## More information

The short-term goal of this project is to develop a minimum viable prototype to show that the underlying concept of "continuous RDM" works. In the long-term, we aim for full integration of ISA profiles for RO-Crate. Our approach is framework-agnostic, with Omnipy serving as a reference and proof-of-concept but open for extensions and implementations with other frameworks.

If selected for BH2023, our focus will be on realizing a first prototype. To achieve this, we are looking for experts in ISA, RO-Crate, ARC, Omnipy, and metadata formats to join our team. As an additional objective, we are also interested in exploring the potential for connecting RO-Crates to Galaxy and would welcome expertise in this area.

By bringing together a diverse team of experts with complementary skills and knowledge, we believe that we can successfully develop and demonstrate the concept of “continuous RDM” and its potential for research data management and interoperability.

## Lead(s)

Sebastian Beier, Sveinung Gundersen, Stuart Owen


