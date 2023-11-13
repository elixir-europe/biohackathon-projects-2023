# Extending BioSamples' records
This python code takes in a dictionary of BioSamples' accessions and their associated external references, and expands the former with the latter.

To summarize, the steps of the code are:
1. Takes the BioSamples' submitter credentials and an input file containing a set of BioSamples accessions and their associated external references
  1. Validates inputs
1. For each BioSamples' accession, it downloads its JSON record from BioSamples
1. Extend the BioSamples' JSON with the ``externalReferences`` of the input file
1. Submit the extended JSON to BioSamples to replace the existing one

## Examples
### BioSamples JSON
Mock example ([``SAMEA112654119``](https://www.ebi.ac.uk/biosamples/samples/SAMEA112654119)):
- Record (JSON) **before** extending with ``externalReferences``:
````
{
  "name" : "AngH91",
  "accession" : "SAMEA112654119",
  ...
}
````
- Record (JSON) **after** extending with ``externalReferences``:
````
{
  "name" : "AngH91",
  "accession" : "SAMEA112654119",
  ...
  "externalReferences" : [ {
    "url" : "https://ega-archive.org/datasets/EGAD00010002458",
    "duo" : [ ]
  }, {
    "url" : "https://ega-archive.org/metadata/v2/samples/EGAN00004248937",
    "duo" : [ ]
  }, {
    "url" : "https://www.ebi.ac.uk/ena/browser/view/SAMEA112654119",
    "duo" : [ ]
  } ]
  ...
}
````
### Script input
In the following example, we would be adding 3 URLs to ``SAMEA112654119`` and one to ``SAMEA419425`` as ``externalReferences``.
````
{
    "biosampleExternalReferences": [
        {
            "biosampleAccession": "SAMEA112654119",
            "externalReferences": [
                {
                    "url": "https://ega-archive.org/datasets/EGAD00010002458"
                },
                {
                    "url": "https://ega-archive.org/metadata/v2/samples/EGAN00004248937"
                },
                {
                    "url": "https://www.ebi.ac.uk/ena/browser/view/SAMEA112654119"
                }
            ]
        },
        {
            "biosampleAccession": "SAMEA419425",
            "externalReferences": [
                {
                    "url": "https://ega-archive.org/datasets/EGAD00010002458"
                }
            ]
        }
    ]
}
````