"""Fetch ENA forms schema from remote."""

import yaml
import requests

SCHEMA_URL = (
    'https://raw.githubusercontent.com/'
    'neoformit/ena-upload-template-builder/main/data/example_schema.yml'
)


def fetch():
    """Fetch and parse schema definition from YAML."""
    response = requests.get(SCHEMA_URL)
    return yaml.safe_load(response.text)
