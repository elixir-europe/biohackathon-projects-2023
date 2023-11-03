"""Fetch ENA forms schema from remote."""

import json
import requests

SCHEMA_URL = (
    'https://raw.githubusercontent.com/ELIXIR-Belgium/ENA-metadata-templates/'
    'main/templates/{identifier}/{identifier}.json'
)


def fetch(identifier):
    """Fetch and parse schema definition from YAML."""
    response = requests.get(SCHEMA_URL.format(identifier=identifier))
    return json.loads(response.text)
