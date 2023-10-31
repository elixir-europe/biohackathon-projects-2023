# Project 13: Discovering Bioinformatics Software in Software Heritage

## Abstract

Software Heritage is currently the largest archive of software in source code form, hosting more than 14,000,000,000 source files and 223,000,000 projects. It regularly crawls data from 18 different software platforms such as Github or Gitlab, storing the code of the vast base of developers and organizations nowadays. These sources are used not only for software development, but also for open-source projects, documentation, and other types of collaborative projects. 

Bioinformatics software is no exception when it comes to hosting source code on these platforms. Around 60% of software in bio.tools respectively has an associated repository. However, many softwares hosted in these repositories are still not registered in commonly used registries.

In this project, we will build a software prototype that identifies whether a repository is hosting Bioinformatics Software. We will use Software Heritage API to search for repositories and a combination of strategies, involving NLP and machine learning techniques, to analyze the text in the repository's README and other relevant files, including source code ones and determine if they can be categorized as bioinformatics software. To do so, we will take advantage of the curated data gathered in OpenEBench Tools Monitoring/Software Observatory, which currently monitors over 9,300 bioinformatics tools with an assigned (or valid) GitHub repository.

This implementation would allow us to discover thousands of tools and services, and add them to the EXILIR Tools Ecosystem, making them more findable for the wider community.

## More information

In the short-term we would like to rescue repositories that are not found in any software repository. In the long-term, incorporate the software into the OpenEBench tools monitoring ecosystem to continuously push new tools to either the ELIXIR Tools Ecosystem or to human reviewers for validation.

Activities during the Biohackathon will be:

 * Using the Software Heritage API to extract the data we need, including repositories content and tags. We will focus on repositories from GitHub, and then GitLab in case of successful results.
 * Defining and prioritizing strategies (NLP, ML, etc) to determine if a repository contains bioinformatics software. We will preferentially but not exclusively rely on README and documentation for the inference.
 * Implementation of the strategies by participants.
   
We think that we need around 4-5 people full-time to work on the project. We welcome participants with at least basic expertise in APIs, Machine Learning, NLP, and software metadata.

## Lead(s)

Eva Martin del Pico, Sergi Aguiló-Castillo

## Links

[Project Working Document](https://docs.google.com/document/d/1ziF29-I0ItqKAS1gbF42Pr7Uf6U-SScuomVtd6K5ROM/edit) 

[Working Folder](https://drive.google.com/drive/folders/1xOj7P0nGi1Z-XfB7eK_zsXyXMTK7rvQ4?usp=drive_link)


