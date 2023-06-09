# Project 27: Multi-Repository Data Submission using ISA-JSON

## Abstract

Brokering data from producers to repositories is an integral service for research data management platforms. However, existing tools are often technique/domain-specific and focused on a single repository. During the BioHackathon 2022, we designed a unified and technique/domain-specific data brokering approach for submitting multi-omics studies to multiple specialized repositories. Briefly, an ISA-JSON file, containing repository required metadata, is processed by an independent upload tool that bundles credentials, data and metadata, and defines the destination repository for each schema. Then, a multi-repository converter applies mapping rules between ISA-JSON schemas and different repositories’ models, initiating the (meta)data submission process. Initial mappings and prototypes for BioSamples and ENA have been made previously.

During this BioHackathon project, we aim to advance the development of the approach defined last year, by including other ELIXIR and non-ELIXIR repositories, namely MetaboLights, BioStudies/ArrayExpress and e!DAL-PGP, to cover multi-omics submission. 

To reinforce the broad applicability of the approach, we will work with ISA-JSON files generated by the ARC data structure, in addition to the ones generated by DataHub. We will also further explore the application of stepwise validated data flows orchestrated through Omnipy to extend the existing prototype of the converter tool. Defining requirements for the implementation of the independent upload tool is also in scope to support the feasibility of a streamlined brokering process.

## More information

### Focus and project plan

 * Mapping of additional repositories’ models to ISA-JSON schemas.
 * Evaluate solutions such as Omnipy and extend the prototype.
 * Define requirements for the independent upload tool.
    
### Short-term

 * Minimum viable products for BioSamples and ENA conversion and submission.
 * Proof-of-concept multi-repository converter including the additional repositories.

### Long-term

 * Uptake of ISA-JSON as standard for multi-repository metadata submission by data producers and repositories.
 * A domain-agnostic toolset that is easy to integrate in different platforms and pipelines.
 * A toolset contributed to by the repositories and open for contributions by the different stakeholders.
    
**Minimum number of people:** 2 software developers and 2 data stewards. We have engaged with the stakeholders described in the collaborations.

**Expertise:** ISA-JSON, data submission to EBI-EMBL repositories and e!DAL-PGP, coding skills (Python, Java and Javascript).

**Methodology:** Building on BioHackathon 2022's success, we will leverage diverse expertise of the participants and use hands-on (pseudo)coding to achieve our development goals.

## Lead(s)

Flora D'Anna, Rafael Andrade Buono, Zahra Waheed


