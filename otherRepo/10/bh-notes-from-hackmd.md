# Project 10: FAIR Workflow Execution with WfExS and Workflow Run Crate

This document will hold all the ideas to create and promote a FAIR workflow executions ecosystem.

## Ideas (2023-10-30)

_(contributions from José Mª Fernández (0000-0002-4806-5140), Paula Iborra (0000-0003-0504-3029), Stian Soiland-Reyes (0000-0001-9842-9718))_

The ecosystem should be based on open standards, like GA4GH and Research Object ones, data providers, and data consumer and generators. It should be a FAIR ecosystem, in the next sense (terms are conveniently disordered):

* **Interoperable**: Different storage providers, like Zenodo or B2SHARE, should be considered. They have a very rich metadata model which could be mapped in some way to some subset of the metadata. Also, different data consumers and generators of WorkflowRun RO-Crate should be involved in the ecosystem's lifecycle.

* **Findable**: Several mechanisms to index places which are full of crates following WorkflowRun RO-Crate should be designed. If an indexing software were designed, maybe it should also implement a GA4GH DRS interface, in order to abstract the way to fetch the crate locations.

* **Accessible**: The ecosystem needs proper documentation about the protocols being used, how they are used, and the best practices to upload contents to data providers, so their inherent metadata search capabilities can be used.

* **Reusable**: Engines and orchestrators should be able to consume those crates, either by themselves, or with some help. WfExS-backend, workflow orchestrator able to generate and consume RO-Crates to reproduce workflow execution. WfExS delegates workflow execution to existing workflow engines (Nextflow, CWL). 



## Ideas (2023-11-02)

_(contributions from José Mª Fernández (0000-0002-4806-5140), Sébastien Moretti (0000-0003-3947-488X), Arun Isaac (0000-0002-6810-8195), Paula Iborra (0000-0003-0504-3029), Paul De Geest (0000-0002-8940-4946))_

* Zenodo allows updating the metadata after the data has been uploaded. Zenodo has the concept of community, where some validation is applied from the community owneres over the entries being attached to that community. Metadata which can be attached goes from references to manuscripts (hopefully the scientific work where the RO-Crate was generated), authorships, funding, data licensing, keywords and so on. There are limitations about the licensing, as a single license can be attached. For restriced access entries the data access conditions can be declared. Sèbastien did the advice that a huge RO-Crate entry (i.e. one with lots of files or huge ones as payload) could have problems, as Zenodo limits to 50GB the total size limit per entry, and 100 files per upload. There is no size limit on the number of entries in communities. 


* A software focused on the generation **and** upload of Workflow Run RO-Crates to Zenodo could book an entry, include the DOI in the generated RO-Crate, reuse part of the metadata already gathered in the execution process, and then decide whether to also skip more or less payloads, based on their public availability, or store them in a separate Zenodo entry.


* B2SHARE is EUDAT’s main platform for storing and publishing research data and is a key starting point for making data FAIR (findable, accessible, interoperable, reusable). Takes in all metadata fields from [DataCite metadata schema definition v4.3](https://schema.datacite.org/meta/kernel-4.3/), improved support for multiple root schema versions and an updated and improved metadata exporter via OAI-PMH protocol.
* B2SHARE supports the concept of communities administering their own metadata schemas and publication requirements. Potential limitations for huge entries, as the maximum size for a record is 20 GB, and the maximum size for a file is 10 GB. ([B2SHARE usage](https://eudat.eu/services/userdoc/b2share-usage#Communities))
    > Interesting training material: [B2SHARE-training](https://github.com/EUDAT-Training/B2SHARE-Training)

* B2FIND is an aggregated metadata domain of EUDAT. Based on comprehensive joint metadata catalogue of research data colletions stored in EUDAT data centes and others. Stores metadata through other EUDAT services (like B2SHARE). 
* B2FIND uses various protocols to aggregate metadata from different data repositories. It can harvest metadata using protocols like OAI-PMH.

* A community page should be established similar to the ([RO-Crate communit page](https://www.researchobject.org/ro-crate/community.html)). Similarly, a slack channel on the Seek workspace could be created.


