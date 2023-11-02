"""Fetch ENA forms schema from remote."""

import yaml
import requests

SCHEMA_URL = (
    # 'https://raw.githubusercontent.com/'
    # 'neoformit/ena-upload-template-builder/main/data/example_schema.yml'
    'https://raw.githubusercontent.com/ELIXIR-Belgium/ENA-metadata-templates/'
    'main/templates/{identifier}/{identifier}.yml'
)


def fetch(identifier):
    """Fetch and parse schema definition from YAML."""
    response = requests.get(SCHEMA_URL.format(identifier=identifier))
    return yaml.safe_load(response.text)
