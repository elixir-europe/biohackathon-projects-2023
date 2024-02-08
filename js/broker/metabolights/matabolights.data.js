export const Data = {
    "targetRepository": "ena",
    "receipt": { "a": "b" },
    "accessions": [
        {
            "path": [{ "key": "investigation" }],
            "value": "PRJEB100893"
        },
        {
            "path": [
                { "key": "investigation" },
                { "key": "studies", "where": { "key": "title", "value": "Arabidopsis thaliana" } }
            ],
            "value": "ERP201308"
        },
        {
            "path": [
                { "key": "investigation" },
                { "key": "studies", "where": { "key": "title", "value": "Arabidopsis thaliana" } },
                { "key": "assays", "where": { "key": "@id", "value": "#assay/18_20_21" } }
            ],
            "value": "ERR9668871"
        },
        {
            "path": [
                { "key": "investigation" },
                { "key": "studies", "where": { "key": "title", "value": "Arabidopsis thaliana" } },
                { "key": "assays", "where": { "key": "@id", "value": "#assay/18_20_21" } },
                { "key": "materials" },
                { "key": "otherMaterials", "where": { "key": "@id", "value": "#other_material/332" } }
            ],
            "value": "ERX9222846"
        },
        {
            "path": [
                { "key": "investigation" },
                { "key": "studies", "where": { "key": "title", "value": "Arabidopsis thaliana" } },
                { "key": "assays", "where": { "key": "@id", "value": "#assay/18_20_21" } },
                { "key": "materials" },
                { "key": "otherMaterials", "where": { "key": "@id", "value": "#other_material/333" } }
            ],
            "value": "ERX9222847"
        }
    ]
};