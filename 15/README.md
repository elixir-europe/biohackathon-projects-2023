# Project 15: Enabling FAIR Digital Objects with RO-Crates, Signposting and Bioschemas

## Abstract

RO-Crate [1] is a lightweight method to package research outputs along with their metadata. Bioschemas [3] provides metadata schemas to add structured metadata to webpages on Life Science. Signposting [2] provides a lightweight yet powerful approach to increase the FAIRness of scholarly objects.

The combination of RO-Crates, Bioschemas and Signposting make resources easy to navigate by machines, provide an unambiguous way for machines to access FAIR metadata and content in a single request, and reduce content-negotiation hassle that can give unpredictable results.

This tripartite combination is of benefit for repositories and publishers as they can non-disruptively add FAIR Signposting headers for machine navigation, support RO-Crate imports and align with Bioschemas specifications, making FAIR Digital Objects achievable with existing technologies over HTTP.

FAIR tooling implementers can also benefit as they could create, improve or integrate Signposting clients combined with RO-Crate libraries implementing Bioschemas specifications. On its side, FAIR data implementers could support consumption of FAIR Signposting and create Knowledge Graphs from RO-Crates.

While Bioschemas has been adapted by many repositories, the methods for its consumption have largely been focused on discoverability. Now we focus on integrations, such as building scholarly knowledge graphs from multiple Bioschemas sources.

Finally, FAIR outreach practitioners showcase uses of FAIR Signposting to navigate and consume RO-Crates making FAIR closer to the community. This project will continue the effort started as part of FDO2022 and FAIR-IMPACT to enable FAIR Signposting and RO-Crate for content/metadata discovery and consumption.

### References

 1. https://www.researchobject.org/ro-crate/ [https://www.researchobject.org/ro-crate/]
 2. https://signposting.org/FAIR/ [https://signposting.org/FAIR/]
 3. https://bioschemas.org/ [https://bioschemas.org/]

## More information

### Timeline for long and short-term goals
   
* Long-term: Improvement of FAIRness for digital objects.     
* Short-term: Improve the metadata exchange between the three technologies

### Focus during the BioHackathon

* Add metadata markup/headers to landing pages of at least one website
* Improve at least one Signposting client
* Prototype a knowledge graph from pages using any of the technologies
* Improve Bioschemas/RO-Crate validation for at least one profile

#### Minimum number of people to succeed

* 5

### Required level of expertise/skills to participate

* Some knowledge in JSON-LD, HTML structured markup, HTML headers, structured metadata, Python would be helpful
* For webpage providers, their preferred programming language
 
### Methodology used
   
* Bring-your-own-Repository, pair-programming, feature-driven development

## Lead(s)

Stian Soiland-Reyes, Herbert Van de Sompel, Leyla Jael Castro


