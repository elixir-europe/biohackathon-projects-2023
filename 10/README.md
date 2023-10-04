# Project 10: FAIR Workflow Execution with WfExS and Workflow Run Crate

## Abstract

FAIR Computational Workflows argues that workflows should be FAIR scholarly community research objects in their own right as a kind of FAIR Research Software. In this project we go one step further, and argue that workflow executions should also be published with sufficient traces and structured metadata. 

Workflow Run RO-Crate is a set of profiles of RO-Crate that capture workflow provenance in a lightweight FAIR data package based on existing standards, in order to support traceability, reproducibility and interoperable description of diverse computational analysis. This use of RO-Crate allows the contextualization of a computational workflow and its execution, e.g. relating to people, organisations, projects, funding, data sources and wider research questions and studies.

We have implemented the profile in multiple workflow systems, including Galaxy, COMPSs, StreamFlow, WfExS, Sapporo, Autosubmit. The command line tool runcrate can convert from the precursor CWLProv and display or validate crates according to the profiles. The crates are compatible with ELIXIR's WorkflowHub and support increasing levels of details, including documenting ad-hoc scripts without a workflow engine.

WfExS is a workflow orchestrator designed for reproducible and secure workflow executions in isolated environments (like HPC). Every input, workflow and container being used in an execution must have either a public or permanent identifier, or at least a resolvable URI, so the execution scenario can be materialised. The execution scenario before and/or after the execution can be saved to RO-Crate.  

Here we bring together FAIR Computational Execution practitioners to mature and generalise this approach using Workflow Run Crate.

## More information

**Timeline for long and short-term goals**:
* Long-term: Common approach for interoperable FAIR workflow execution data by any workflow engine
* Short-term: Richer description of workflow executions, increased community participation

**Focus during the BioHackathon**:
* Establishing of FAIR Workflow Execution community
* Sharing workflow definitions and execution in WorkflowHub
* Track resource usage in existing workflow engines
* Display structured workflow provenance in a human-digestible form
* Integrate further with other FAIR standards, tools and repositories

**Minimum number of people to succeed**:
3-5

**Required level of expertise/skills to participate (one or more)**:
* Python (ideal) or other high-level language
* JSON-LD (ideal) or Linked Data in general
* Web development with JSON (schema.org ideal)
* Workflow system development
* Brief experience with writing and executing workflows

**Methodology used**: Pair programming, walk-throughs, brainstorming, Slack chat, Google Docs


## Lead(s)

José María Fernández, Stian Soiland-Reyes


