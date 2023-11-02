"""Basic Flask app."""

import csv
import os
from flask import request, jsonify
from pathlib import Path

from . import forms, schema
from .app import app

OUTFILE = '/tmp/ena-upload-output.csv'
if os.environ.get('FLASK_OUTPUT_FILE'):
    OUTFILE = Path(os.environ.get('FLASK_OUTPUT_FILE'))


@app.route('/api/schema/<identifier>', methods=['GET'])
def get_schema(identifier):
    return jsonify({
        "schema": schema.fetch(identifier),
    })


@app.route('/api/submit', methods=['POST'])
def submit():
    """Handle request to submit form and write to CSV.

    TODO: can't use flask forms for this if the schema is dynamically
          generated. Probably better to just use client-side validation.
          Can we make a form factory??
    """
    form = forms.MyForm.from_json(request.json)
    if form.validate():
        name = form.name.data
        age = form.age.data
        with open(OUTFILE, mode="w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Age"])
            writer.writerow([name, age])
        return jsonify({"status": "success"})
    return jsonify({
        "status": "error",
        "message": f"Form data was invalid: {form.errors}"
    })
