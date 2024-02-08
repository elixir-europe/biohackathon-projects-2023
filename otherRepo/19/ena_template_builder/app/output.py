"""Write output to file.

Output file paths can be set with env variables:

- STUDY_OUTPUT_FILE
- EXPERIMENT_OUTPUT_FILE
- RUN_OUTPUT_FILE
- SAMPLE_OUTPUT_FILE

"""

import csv
import os
from pathlib import Path

FORM_NAMES = ('study', 'experiment', 'run', 'sample')
OUTFILES = {
    form_name: Path(
        os.environ.get(
            f'ENA_OUTPUT_{form_name.upper()}',
            f'/tmp/ena-upload-{form_name}.csv'))
    for form_name in FORM_NAMES
}


def write_forms_to_file(data):
    """Write forms data to four tabular files."""
    for form_name in FORM_NAMES:
        print(f"Writing form {form_name}...")
        write_form(
            data[form_name],
            get_colnames(data['schema'], form_name),
            OUTFILES[form_name])


def write_form(data, columns, filepath):
    """Write given form to file."""
    print(f"Writing {len(data)} row to {filepath}...")
    with open(filepath, mode="w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        for row in data:
            writer.writerow([row.get(col) for col in columns])


def get_colnames(schema, form_name):
    """Get column names for given form."""
    return [field['name'] for field in schema[form_name]['fields']]
