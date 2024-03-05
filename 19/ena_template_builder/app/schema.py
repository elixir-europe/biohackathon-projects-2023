"""Fetch ENA forms schema from remote."""

import json
import requests

SCHEMA_URL = (
    'https://raw.githubusercontent.com/ELIXIR-Belgium/ENA-metadata-templates/'
    'main/templates/{identifier}/{identifier}.json'
)
README_URL = (
    'https://raw.githubusercontent.com/ELIXIR-Belgium/ENA-metadata-templates/'
    'main/templates/{identifier}/README.md'
)


def fetch(identifier):
    """Fetch and parse schema definition from YAML."""
    # Fetch JSON schema
    r = requests.get(SCHEMA_URL.format(identifier=identifier))
    data = json.loads(r.text)
    data['identifier'] = identifier

    # Get title / description from README
    r = requests.get(README_URL.format(identifier=identifier))
    readme_meta = _parse_readme(r.text)
    data.update(readme_meta)
    return data


def _parse_readme(text):
    """Parse title and description from README."""
    title_desc_block = text.split('#')[1].strip()
    title, description = [
        x.strip(' \n').replace('\n', '')
        for x in title_desc_block.split('\n', 1)
    ]
    return {'title': title, 'description': description}
