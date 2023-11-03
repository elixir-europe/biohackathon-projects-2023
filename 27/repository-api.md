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
    * key is JSON query to the object in ISA-JSON being accessioned
    * value is accession (or whatever identifier repository wants to respond with)

(Examples below for illustration only)
```
{
   "targetRepository": "ena",
   "receipt": {...}
   "accessions": [
      {
         "path": [{"key": "investigation"}],
         "value": "PRJEB100893"
      },
      {
         "path": [
            {"key": "investigation"}, 
            {"key": "studies", "where": {"key": "title", "value": "Arabidopsis thaliana"}}
        ],
         "value": "ERP201308"
      },
      {
        "path": [
            {"key": "investigation"}, 
            {"key": "studies", "where": {"key": "title", "value": "Arabidopsis thaliana"}},
            {"key": "assays", "where": {"key": "@id", "value": "#assay/18_20_21"}}
        ],
        "value": "ERR9668871"
      },
      {
        "path": [
            {"key": "investigation"}, 
            {"key": "studies", "where": {"key": "title", "value": "Arabidopsis thaliana"}},
            {"key": "assays", "where": {"key": "@id", "value": "#assay/18_20_21"}},
            {"key": "materials"},
            {"key": "otherMaterials", "where": {"key": "@id", "value": "#other_material/332"}}
        ],
        "value": "ERX9222846"
      },
      {
        "path": [
            {"key": "investigation"}, 
            {"key": "studies", "where": {"key": "title", "value": "Arabidopsis thaliana"}},
            {"key": "assays", "where": {"key": "@id", "value": "#assay/18_20_21"}},
            {"key": "materials"},
            {"key": "otherMaterials", "where": {"key": "@id", "value": "#other_material/333"}}
        ],
        "value": "ERX9222847"
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
    accessions: <as above>
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
