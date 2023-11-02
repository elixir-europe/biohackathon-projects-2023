# Repository API Specification (work in progress)

This document is to define the interface between the broker and the repository services.

### Header:
Authorization Bearer 123

Question: What will this be?  Life Sciences RI, webin...


### Body:

```
{
    action: submit,
    isaJson: {...}
}
```
Scope for now is just **submit**.

Question: What other params should we support from the beginning?


### Response:

For BioSamples we will keep this as ISA-JSON as it is currently being created.

For other repositories (ENA & MetaboLights) we plan to have a generic receipt format which we will evolve to in steps.



Current format:

* `targetRepository` (same key as in the ISA-JSON for annotation) should take values from identifiers.org
* `receipt` in this case is free to be whatever is currently provided by the repository
* `accessions` is a list of objects describing what was accessioned by the repository
    * key is JSON path to the object in ISA-JSON being accessioned
    * value is accession (or whatever identifier repository wants to respond with)

(Examples below for illustration only)
```
{ 
    targetRepository: "ena",
    receipt: "...",
    accessions: [
        {
           path: ["studies", "studyId", "sources", "sourceId"],
           value: "SAME..."
         },
         {
            path: ["studies", "studyId", "sources", "sourceId", "samples", "sampleId"],
            value: "...",
         }
    ]
}
```

Future (TBC):

Similar to the above but with a more generic and informative receipt format.
```
{
    submissionDate: 2023-11-02,
    status: private,
    holdDate: 2024-11-02,
    accessions: [
        {
           path: ["studies", "studyId", "sources", "sourceId"],
           value: "SAME..."
         },
         {
            path: ["studies", "studyId", "sources", "sourceId", "samples", "sampleId"],
            value: "...",
         }
    ]
}
```

Advantages of this approach for providing accessions:

- Always well-defined - every repository must accession something in the ISA-JSON
- Generic for broker - does not matter which repo is responding, the JSON path tells you exactly which object in the ISA-JSON to add the `characteristic`


### Enums

Some (hopefully) common values across repositories.

key | value 
-- | --
action | submit, update, publish, delete...
status | private, public
