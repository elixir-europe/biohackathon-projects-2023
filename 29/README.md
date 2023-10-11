# Project 29: Secure data-out API - enabling encrypted htsget transactions

## Abstract

The European Genome-phenome Archive (EGA) is a service for archiving and sharing personally identifiable genetic and phenotypic data, while the The Genomic Data Infrastructure (GDI) project is enabling access to genomic and related phenotypic and clinical data across Europe. Both projects are focused on creating federated and secure infrastructure for researchers to archive and share data with the research community, to support further research.

This project proposal is focusing on the data access part of the infrastructure. The files are encrypted in the archives, using the crypt4gh standard. Currently, there exist data access processes, where the files are either decrypted on the server side and then transferred to the user or re-encrypted server-side and provided to the user in an outbox.

Htsget as a data access protocol also allows access to parts of files, but there’s currently no production-level client tools that support access to encrypted data. Our goal is to create a client tool that can access encrypted data over the htsget protocol. It should also work with the GA4GH Passport and Visa standard so we can then enhance the security of our data access interfaces. We will also modify [htsget-rs](https://github.com/umccr/htsget-rs), a Rust htsget server, and [crypt4gh-rust](https://github.com/umccr/crypt4gh-rust) as required to support the aforementioned standards. Finally, there will be an effort to implement this feature in already existing tools, like samtools and IGV.

## More information

* Short-term we want to have a CLI tool that can retrieve encrypted data over htsget and decrypt it locally.
* Medium-term we want to add support for range requests and
* Long-term to have this work seamlessly in for example samtools, IGV and galaxy.
* Depending on the number of people joining the project, the focus will vary between
  * Creating command line interface that will be able to access retrieve and decrypt the data, and
  * expanding known and widely used tools to support this functionality.
 * The minimum number of people required for the project to achieve one of the above goals, is approximately 5.
 * Experience with programming and preferably golang is welcome, however, input related to the user experience would be appreciated.
 * We will use parts of the scrum methodology, analyzing the requirements in epics and breaking them down to user stories.

## Lead(s)

Johan Viklund, Stefan Negru, Dimitrios Bampalikis


