# Project 25: Increasing the findability, visibility, and impact of Galaxy tools for specialised scientific Communities

## Abstract

Galaxy offers almost 10,000 tools that are developed in different Git repositories.

Furthermore, Galaxy also embraces granular implementation of software tools as sub-modules combined in suites. Some key examples of suites include Mothur and OpenMS. The decentralised development and the sub-module architecture make it difficult for Galaxy users to find and reuse tools, or to filter e.g. for all tools available for a specific research community. It may also result in Galaxy developers replicating effort by simultaneously wrapping new tools.

We propose to combine preliminary work from the Freiburg Galaxy team, the Australian BioCommons, and the ELIXIR Tools Platform, in order to collect the available Galaxy tools for a target community, automatically extract their metadata (including Conda version, Bio.tools identifiers, and EDAM annotations), render the data as an interactive table on the Galaxy Hub, and put in place systems that keep the information up to date.

In parallel, we will work on improving tools metadata on Bio.tools and the ToolShed, so that they can be interactively filtered and compared. For Bio.tools, this effort will include a refinement of the annotation practices, a crowdsourced community effort to add and curate tools, and an assessment of the impact of this effort on the generated Galaxy tool list for a specific Community.

This project will directly engage with the ELIXIR Biodiversity and the emerging Microbiome Communities, to improve the findability, visibility, comparability, and accessibility of their tools.

## More information

In the short-term, we will focus on moving the prototype to production by adding the required features, developing a working example, and on curating the Bio.tools annotations. To achieve this, a small group (~4) with basic programming knowledge in Python and some expertise in web development will be sufficient. For the curation, we will convene a larger group composed of Community champions (Biodiversity and Microbiome), and Tools Ecosystem experts from Bio.tools and EDAM.

We will also engage with core Galaxy developers to extend the tool metadata exposed by the ToolShed, exploiting the recent efforts to completely refactor the ToolShed codebase.

The long-term goals will be the reuse of the comprehensive Galaxy tool table by any Community (e.g. Single cell), and the reuse of the curation process by the broader Tools Ecosystem and its user community.

## Lead(s)

Paul Zierep, Johan Gustafsson, Nicola Soranzo


