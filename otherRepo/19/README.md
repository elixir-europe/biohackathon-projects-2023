# Project 19: Galaxy ENA Upload as an Interactive Tool

## Abstract

A requirement of peer reviewed publication is often the deposition of raw data to an publicly available international data repository. Galaxy supports upload to the [EBI-European Nucleotide Archive](https://www.ebi.ac.uk/ena/browser/home) through the [ENA Upload Tool](toolshed.g2.bx.psu.edu/repos/iuc/ena_upload/ena_upload/0.6.1). However, users are still required to have a strong working knowledge of the ENA to navigate the necessary metadata to support an upload. 

Galaxy does not host the metadata templates, requiring users to go through rounds of metadata upload, test, edit (outside of Galaxy), reupload and retest before a submission to ENA will be successful. This project proposes to make use of Galaxy’s Interactive Tools, to support metadata editing inside of Galaxy in an effort to streamline data submission and make Galaxy an end to end solution for data analysis and publication.

## More information

This project has been designed to build on an existing Galaxy tool, Galaxy Interactive Tools and publicly available [template documents](https://github.com/ELIXIR-Belgium/ENA-metadata-templates) created for the ENA upload tool. The short term goal of this project would be to establish access to ENA templates inside Interactive Tools, long term this would be enhanced through training and documentation, to allow more researchers to self-manage data upload to ENA.

A medium size team of 4-8 people with knowledge of the ENA submission process, Galaxy and Github would be able to work F2F and virtually to achieve the project aims.

## Prerequisite knowledge
### About ENA

-   [ENA metadata model](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html#)
-   [How to register samples](https://ena-docs.readthedocs.io/en/latest/submit/samples.html)
-   [ENA Webin REST V2](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/programmatic-v2.html)
-   [Webin REST V2 Service](https://wwwdev.ebi.ac.uk/ena/submit/webin-v2/swagger-ui/index.html#/) (Dev)
-   [XSD template GitHub repo](https://github.com/enasequence/schema/tree/master/src/main/resources/uk/ac/ebi/ena/sra/schema)

### ENA upload tool

-   [usegalaxy-eu/ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli)
-   [ENA-metadata-templates](https://github.com/ELIXIR-Belgium/ENA-metadata-templates)
-   [ENA-upload-cli Galaxy wrapper](https://github.com/galaxyproject/tools-iuc/tree/main/tools/ena_upload)
-   ENA-upload in the [toolshed](https://toolshed.g2.bx.psu.edu/repository?repository_id=0db04aa13ef9d2f8)
-   [Screencast](https://www.youtube.com/watch?v=POiQG-7O7rw) showing all steps to do a submission through Galaxy

### Galaxy Interactive tools

-   [GTN tutorial](https://training.galaxyproject.org/training-material/topics/admin/tutorials/interactive-tools/tutorial.html)

## Lead(s)

Mike Thang, Bert Droesbeke, Gareth Price



