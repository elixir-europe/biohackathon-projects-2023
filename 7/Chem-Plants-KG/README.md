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
| Sabio-RK | TBA                                         | https://biohack2023/sabio-rk | [sabio-rk.ttl](sabio-rk.ttl) |

A public instance of GraphDB with the Chem and Plants KG is available at knowledge.ipk-gatersleben.de (demo/demo).

## KG query

Example SPARQL queries for Chem and Plants KG:

### Which resources mention the compound caffeine?
```sparql
PREFIX schema: <http://schema.org/>
select ?resource where {
    GRAPH ?resource {
		?entry schema:inChIKey ?key .
    }
    BIND("RYYVLZVUVIJVGH-UHFFFAOYSA-N" as ?caffeineChIKey)
    FILTER (?key = ?caffeineChIKey)
} 
limit 100 
```
### Count the number of entries per resource talking about caffeine:
```sparql
PREFIX schema: <http://schema.org/>
select ?resource (COUNT(?entry) as ?entriesAboutCoffe) where {
    GRAPH ?resource {
		?entry schema:inChIKey ?key .
    }
    BIND("RYYVLZVUVIJVGH-UHFFFAOYSA-N" as ?caffeineChIKey)
    FILTER (?key = ?caffeineChIKey)
} 
group by ?resource
limit 100
```
### List chemical pathways in plants:
```sparql
PREFIX biohack23: <https://biohack2023/>
PREFIX schema: <http://schema.org/>
PREFIX up: <http://purl.uniprot.org/core/>
PREFIX taxon: <http://purl.uniprot.org/taxonomy/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select distinct ?pathway ?organismName 
where {
    Graph biohack23:wikipathways {
        ?pathway a schema:Dataset ;
                 schema:taxonomicRange ?taxon .
    }
    {
        SELECT DISTINCT ?taxon ?organismName ?commonName ?ncbiURI
        WHERE {
            {
                SELECT distinct ?taxon ?ncbiURI
                WHERE {
                    Graph biohack23:wikipathways {
                        ?x schema:taxonomicRange ?taxon .
                        BIND(STRAFTER(STR(?taxon), "_") AS ?ncbi)
                        BIND(URI(CONCAT("http://purl.uniprot.org/taxonomy/" ,?ncbi)) AS ?ncbiURI)
                    }
                } 
            }
            SERVICE <https://sparql.uniprot.org/sparql> {
                ?ncbiURI up:scientificName ?organismName ;
                         up:commonName ?commonName .
                # Taxon subclasses are materialized, do not use rdfs:subClassOf+
                FILTER EXISTS {
                    ?ncbiURI rdfs:subClassOf taxon:33090 .
                }
            }
        }
    }
}
```
### List compounds per plant pathway:
```sparql
PREFIX biohack23: <https://biohack2023/>
PREFIX schema: <http://schema.org/>
PREFIX up: <http://purl.uniprot.org/core/>
PREFIX taxon: <http://purl.uniprot.org/taxonomy/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select distinct ?pathway ?organismName ?molecule 
where {
    Graph biohack23:wikipathways {
        ?pathway a schema:Dataset ;
                 schema:taxonomicRange ?taxon .
        ?molecule a schema:MolecularEntity ;
                  schema:includedInDataset ?pathway .
    }
    {
        SELECT DISTINCT ?taxon ?organismName ?commonName ?ncbiURI
        WHERE {
            {
                SELECT distinct ?taxon ?ncbiURI
                WHERE {
                    Graph biohack23:wikipathways {
                        ?x schema:taxonomicRange ?taxon .
                        BIND(STRAFTER(STR(?taxon), "_") AS ?ncbi)
                        BIND(URI(CONCAT("http://purl.uniprot.org/taxonomy/" ,?ncbi)) AS ?ncbiURI)
                    }
                } 
            }
            SERVICE <https://sparql.uniprot.org/sparql> {
                ?ncbiURI up:scientificName ?organismName ;
                         up:commonName ?commonName .
                # Taxon subclasses are materialized, do not use rdfs:subClassOf+
                FILTER EXISTS {
                    ?ncbiURI rdfs:subClassOf taxon:33090 .
                }
            }
        }
    }
}
```
