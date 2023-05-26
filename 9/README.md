# Project 9: Cell type-specific and druggable pathway models and maps

## Abstract

During previous BioHackathons, we established computational workflows connecting ELIXIR resources for systems biology molecular analyses. Extending our previous work, we will facilitate the construction and use of advanced pathway models to investigate novel therapeutics.

Normally gene-drug associations are determined at the bulk level, not considering cell-type specificity. We will use single-cell data to establish dedicated pathway and disease maps, and connect them to the HiPathia and other modeling tools and approaches. With this, we will find cell types in which druggable targets are uniquely expressed. The process of visual model construction will be coupled with dedicated training materials describing the refinement process of automatically combined diagrams.

In our project, we will use publicly available single cell data or resources suggested by the Single Cell Omics (SCO) Community. Genes differentially expressed in specific cell types will be used to fetch the content of pathway databases - Reactome (ELIXIR Core Data Resource) and WikiPathways (ELIXIR-NL service) - and disease maps (a service of ELIXIR Luxembourg Node). These diagrams will be assembled into a single resource, and enriched against compounds in DrugBank, ChEMBL and OpenTargets. Such a resource will be available for systems biology analysis and modeling. This way, a disease pathway map will be set up, containing druggable mechanisms specific for cell types specified by scRNASeq data. This workflow will be reproducible and applicable for other scRNASeq data, bringing together a number of ELIXIR resources and communities, and support the developing Systems Biology and SCO Communities.

## More information

The short-term goal is to establish a prototype of the pipeline for two selected datasets and its documentation (up to a month after the BH2023).

Long-term goals are (up to a year after the BH2023):

 * Establish the prototype into a reproducible pipeline
 * Extend the list of use-cases to three sets of novel results
 * Prepare a publication
   
The focus will be on completing an end to end solution, reducing the scope of used drug databases and pathway resources where necessary. We will likely establish three groups, working on i) data, ii) workflow and iii) user specifications and documentation. We will have daily project updates and the groups will be working in parallel but in contact.

**Minimum number of people:** 6 (already committed)

**Expertise:** R, Python, JavaScript (workflow, data), pathway databases, systems biology standards (specs, documentation)

**Methodology:** Seurat, systems biology format conversions, disease maps, pathway databases, drug target analysis

## Lead(s)

Marek Ostaszewski, Martina Summer-Kutmon, Naveed Ishaque


