"""A very crude VRC generation script for demonstration purposes, please don't use this for real data."""

import requests
import json

# generates 5 VRC files
for i in range(1, 6):

    vrc = {}
    vrc["virtualReferenceCollectionMetaData"] = {
        "referenceCollectionID": f"http://dummydomain.referencecollections.org/bombus{i}000",
        "creator": "Elixir Robot",
        "maintainer": "Elixir Robot",
        "copyrightLicense": "CC-BY",
        "copyrightOwner": "ELIXIR",
        "title": f"European Bombus virtual reference collection, test {i}000",
        "description": "A test case involving Bombus virtual reference collection data",
        "area": ["Europe"],
        "includedTaxaDescription": "Bombus",
    }
    vrc["taxa"] = []

    url_species = f"https://api.gbif.org/v1/species/1340278/children?limit=5&offset={i*5}"  # shifted offset by 5 for each iteration
    data_species = requests.get(url_species).json()
    print(f"{len(data_species['results'])} species found")

    url_occurrence = "https://api.gbif.org/v1/occurrence/search?speciesKey=%s&limit=1?continent=EUROPE"
    for species in data_species["results"]:
        if species["species"] == "Bombus applanatus":
            # skip this one, missing some details
            continue
        data_occurrence = requests.get(url_occurrence % species["speciesKey"]).json()
        print(f"{len(data_occurrence['results'])} occurrences found for {species['scientificName']}")
        taxon = {
            "taxonID": f"gbif:{species['speciesKey']}",
            "taxonValidNameID": f"https://www.gbif.org/species/{species['speciesKey']}",
            "taxonName": {
                "taxonNameID": f"https://www.gbif.org/species/{species['speciesKey']}",
                "taxonFullName": species["scientificName"],
                "taxonNameAuthor": species["authorship"],
                "taxonNameYear": int(species["authorship"].split(",")[-1].strip(" ").strip(")")),
                "taxonNameBrackets": species["scientificName"],
            },
            "organisms": [],
        }
        organism = {
            "organismID": species["species"],
            "occurrences": [],
        }
        cur_occ = 0
        max_occ = 2
        for occurrence in data_occurrence["results"]:
            if cur_occ >= max_occ:
                # there are tons of occurrences, let's take only 2
                break
            cur_occ += 1
            occ = {
                "occurrenceID": f"https://api.gbif.org/v1/occurrence/{occurrence['key']}",
                "media": []
            }
            cur_media = 0
            max_media = 2
            for media in occurrence["media"]:
                if cur_media >= max_media:
                    # there are tons of media, let's take only 2
                    break
                cur_media += 1
                med = {
                    "mediaID": media["identifier"],
                    "copyrightLicense": media["license"],
                    "mediaDataURL": media["identifier"],
                    "owner": media.get("creator", media.get("rightsHolder", media.get("publisher", "Unknown"))),
                    "reviewed": False
                }
                occ["media"].append(med)
            if len(occ["media"]) == 0:
                continue
            organism["occurrences"].append(occ)
            taxon["organisms"].append(organism)
        if len(taxon["organisms"]) == 0:
            continue
        vrc["taxa"].append(taxon)

    with open(f"vrc{i}.json", "w") as f:
        f.write(json.dumps(vrc))
