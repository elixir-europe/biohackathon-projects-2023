import json
import os

import rdflib as rdf
import requests
from tqdm import tqdm


def get_compounds_ids_with_annotation_level():
    endpoint = "https://dev.coconut.naturalproducts.net/api/v1/search/?limit=1000&page={}"
    base_compound_id = "CNP0{}"
    last_page = 407

    compounds = dict()

    for page in tqdm(range(1, last_page + 1)):
        url = endpoint.format(page)
        response = requests.post(url, json={'query': '', "tagType": None, "type": ""})
        if response.status_code == 200:
            json_response = response.json()
            # Now extract the data
            data = json_response['data']
            for compound in data:
                compounds.setdefault(base_compound_id.format(compound['id']), compound['annotation_level'])

    # Write the compound ids to a file
    with open('filtered_compounds.txt', 'w') as f:
        for compound_id, level in compounds.items():
            f.write("{}\t{}\n".format(compound_id, level))


def get_jsonld():
    # Now for each compound id, get the JSON-LD data from the API
    endpoint = "https://dev.coconut.naturalproducts.net/api/v1/schemas/bioschema/{}"

    jsons = dict()

    for compound_id in tqdm(list(filtered_compounds)[:2000]):
        url = endpoint.format(compound_id)
        response = requests.get(url)
        if response.status_code == 200:
            json_response = response.json()
            jsons[compound_id] = json_response

    # Write the JSON-LD data to a file
    for compound_id, json_data in jsons.items():
        with open('scraped_ld/{}.json'.format(compound_id), 'w') as f:
            f.write(json.dumps(json_data, indent=4))


if __name__ == '__main__':
    # get_compounds_ids_with_annotation_level()
    # Read the file with the compound ids, and filter the ones that have a annotation level of 4 or above
    filtered_compounds = set()
    with open('filtered_compounds.txt', 'r') as f:
        for line in f:
            compound_id, level = line.strip().split('\t')
            if int(level) == 5:
                filtered_compounds.add(compound_id)

    # Load the JSON-LD data from the API
    # get_jsonld()
    # Read the JSON-LD data from the files
    jsons = dict()
    for compound_file in os.listdir('scraped_ld'):
        with open('scraped_ld/{}'.format(compound_file), 'r') as f:
            jsons[compound_file.split('.')[0]] = json.load(f)

    # Now convert the JSON-LD data to turtle format
    graph = rdf.ConjunctiveGraph()
    for compound_id, json_data in tqdm(jsons.items()):
        graph.parse(data=json.dumps(json_data), format='json-ld')
    graph.serialize(destination='coconut.ttl', format='turtle')
