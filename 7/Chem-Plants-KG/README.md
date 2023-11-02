# Chem and Plants KG
This folder contains dumps and queries that showcase the creation and use of a KG that links Plants and Chem communities 

## KG creation

We prepared RDF data dumps of several resources exposing Bioschemas markup.

The data dumps are in Turtle format and can be imported directly into a triple store like GraphDB.

Available data dumps:

| Resource     | Description                                                               | Import as named graph            | File                                 |
|--------------|---------------------------------------------------------------------------|----------------------------------|--------------------------------------|
| Coconut      | Database of natural products                                              | https://biohack2023/coconut      | [coconut.ttl](coconut.ttl)           |
| EDAL-PGP     | e!DAL - Plant Genomics & Phenomics Research Data Repository               | https://biohack2023/edal         | [edal.ttl](edal.ttl)                 |
| MassBank     | Mass spectra database                                                     | https://biohack2023/massbank     | [massbank.ttl](massbank.ttl)         |
| MetaNetX     | Platform for genome annotation and large-scale metabolic network analysis | https://biohack2023/metanetx     | [metanetx.ttl](metanetx.ttl)         |
| nmrXiv       | NMR spectroscopy data repository                                          | https://biohack2023/nmrxiv       | [nmrxiv.ttl](nmrxiv.ttl)             |
| WikiPathways | Platform for biological pathways                                          | https://biohack2023/wikipathways | [wikipathways.ttl](wikipathways.ttl) |

A public instance of GraphDB with the Chem and Plants KG is available at knowledge.ipk-gatersleben.de (demo/demo).

## KG query

Example SPARQL queries for Chem and Plants KG:

- Which resources mention the compound caffeine?
```sparql

```
- Which pathways contain the compound caffeine?
```sparql

```
- Which plant species mention the compound caffeine?
```sparql

```
