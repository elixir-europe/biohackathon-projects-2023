from json import loads

from jsonschema import validate

schema = {}
data = {}

with open("schema.json", "r") as f:
    schema = loads(f.read())

with open("data.json", "r") as f:
    data = loads(f.read())

validate(instance=data, schema=schema)
