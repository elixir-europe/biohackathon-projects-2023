# Project 15: Enabling FAIR Digital Objects with RO-Crates, Signposting and Bioschemas

## Abstract

[RO-Crate](https://www.researchobject.org/ro-crate/) is a lightweight method to package research outputs along with their metadata. [Bioschemas](https://bioschemas.org/) provides metadata schemas to add structured metadata to webpages on Life Science. [Signposting](https://signposting.org/FAIR/) provides a lightweight yet powerful approach to increase the FAIRness of scholarly objects.

The combination of RO-Crates, Bioschemas and Signposting make resources easy to navigate by machines, provide an unambiguous way for machines to access FAIR metadata and content in a single request, and reduce content-negotiation hassle that can give unpredictable results.

This tripartite combination is of benefit for repositories and publishers as they can non-disruptively add FAIR Signposting headers for machine navigation, support RO-Crate imports and align with Bioschemas specifications, making FAIR Digital Objects achievable with existing technologies over HTTP.

FAIR tooling implementers can also benefit as they could create, improve or integrate Signposting clients combined with RO-Crate libraries implementing Bioschemas specifications. On its side, FAIR data implementers could support consumption of FAIR Signposting and create Knowledge Graphs from RO-Crates.

While Bioschemas has been adapted by many repositories, the methods for its consumption have largely been focused on discoverability. Now we focus on integrations, such as building scholarly knowledge graphs from multiple Bioschemas sources.

Finally, FAIR outreach practitioners showcase uses of FAIR Signposting to navigate and consume RO-Crates making FAIR closer to the community. This project will continue the effort started as part of FDO2022 and FAIR-IMPACT to enable FAIR Signposting and RO-Crate for content/metadata discovery and consumption.


## Related hackathon projects

* [#7 Bioschemas resource index for chem and plants](../7/)
* [#10 FAIR Workflow Execution with WfExS and Workflow Run Crate](../10/)
* [#14 Enabling continuous RDM using Annotated Research Contexts with RO-Crate profiles for ISA](../14/)
* [#22 Improved linking from sequence data to specimens and samples repositories](../22/)
* [#23 Improving Bioschemas creation and community adoption through process improvements and tool development, and advancing compliance to FAIR standards](../23/)

## More information

### Timeline for long and short-term goals
   
* Long-term: Improvement of FAIRness for digital objects. Formalize FDO using Web technologies.
* Short-term: Improve the metadata exchange between the three technologies. Demonstrate FDO capability of Signposting.

### Focus during the BioHackathon

* Add metadata markup/headers to landing pages of at least one website
  - Drop-in for anyone to add FAIR Signposting for existing persistent identifiers and metadata resources
  - Drop-in for adding Bioschemas metadata to website
  - Drop-in for RO-Crate support  
* Improve at least one Signposting client
  - https://signposting.readthedocs.io/ (Python)
  - https://github.com/markwilkinson/linkheader-processor (Ruby)
  - Javascript?
  - Java/Jena?
  - Your language!
* Improve Bioschemas/RO-Crate validation for at least one profile (working with [#7](../17/))
* Prototype FAIR Digital Object (FDO) implementation using Signposting, PIDs and RO-Crate
* Conceptualise and draft FDO "configuration type" profile for Signposting-based FDO implementation
* Write up a BioHackrXiv preprint!
* Other ideas
  -  Prototype a knowledge graph from pages using any of the technologies (working with [#7](../17/))
  -  Build a validator for FAIR Signposting level 1, then level 2 - may be based on https://github.com/stain/signposting/ 


#### Minimum number of people to succeed

* 5

### Required level of expertise/skills to participate

* Some knowledge in HTTP, JSON-LD, HTML structured markup, HTML headers, structured metadata
* Java, Python or other scripting languages
* For webpage providers, their preferred programming language or HTML template language

### Useful training resources

* [RO-Crate tutorials](https://www.researchobject.org/ro-crate/tutorials.html)
* [Bioschemas tutorial](https://bioschemas.org/tutorials/)

### Related software
https://bioschemas.org/developer/liveDeploys
* [Signposting adopters](https://signposting.org/adopters/) including
  - [Python Signposting client library](https://signposting.readthedocs.io/en/latest/readme.html) <https://github.com/stain/signposting>
  - [Ruby Signposting client](https://github.com/markwilkinson/linkheader-processor)
  - [Signposting Benchmarks](https://w3id.org/a2a-fair-metrics/)
* [RO-Crate tools](https://www.researchobject.org/ro-crate/tools/) including:
  - [Crate-O](https://github.com/Language-Research-Technology/crate-o) – browser-based editor for Research Object Crates (for Chrome-based browsers)
  - [ro-crate-js](https://www.npmjs.com/package/ro-crate) – JavaScript/NodeJS library for RO-Crate rendering as HTML. (~ beta)
  - [ro-crate-ruby](https://github.com/fbacall/ro-crate-ruby) - Ruby library to consume/produce RO-Crates (~ beta)
  - [ro-crate-py](https://github.com/researchobject/ro-crate-py) – Python library to consume/produce RO-Crates (~ beta)
  - [ro-crate-java](https://github.com/kit-data-manager/ro-crate-java) – Java API for creating and modifying RO-Crate using builder pattern
* [Bioschemas software](https://bioschemas.org/developer/software) including
  - [Bioschemas generator](http://www.macs.hw.ac.uk/SWeL/BioschemasGenerator/)
  - [schema.org validator/visualizer](https://validator.schema.org/)
  - [FAIR checker](https://fair-checker.france-bioinformatique.fr/)
  - [Bioschemas scraper](https://github.com/HW-SWeL/BMUSE)
* FDO (DOIP) implementations
  - [Cordra](https://www.cordra.org/) <https://gitlab.com/cnri/cordra/cordra>

# Potential test data

* [Bioschemas deployments](https://bioschemas.org/developer/liveDeploys)
* [RO-Crate examples](https://www.researchobject.org/ro-crate/examples.html)
* [WorkflowHub RO-Crate](https://doi.org/10.48546/workflowhub.workflow.549.1) reachable [by signposting](https://signposting.org/adopters/#workflowhub)
* Some FDO examples from <https://doi.org/10.3897/rio.8.e96014>

 
### Methodology used
   
* Bring-your-own-Repository, pair-programming, feature-driven development

## Lead(s)

Stian Soiland-Reyes, Leyla Jael Castro, Claus Weiland

## Hackathon Notes

Ongoing notes are in Google Docs: <https://docs.google.com/document/d/1OIm81bicLYih-pKKjlnppX-LV2hBFxKnSVggCuvscrc/edit>

## Slack & Virtual participation

Join channel `#15_enabling-fair-digital-objects` on the Biohackathon Slack. Most of the participants are in person, virtual participants will be involved on ad-hoc basis coordinated on Slack.

