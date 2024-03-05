"""Basic Flask app."""

import os
from flask import request, jsonify

from . import schema
from .app import app
from .output import write_forms_to_file


@app.route('/api/schema/<identifier>', methods=['GET'])
def get_schema(identifier):

    #! TOOD: frontend or api specifies template ID?
    # identifier = os.getenv('ENA_TEMPLATE_ID')

    return jsonify({
        "schema": schema.fetch(identifier),
    })


@app.route('/api/submit', methods=['POST'])
def submit():
    """Handle request to submit form and write to CSV."""
    print("Writing forms to files...")
    write_forms_to_file(request.json)
    return jsonify({"status": "success"})

    # TODO: Handle formatting errors etc
    return jsonify({
        "status": "error",
        "message": "Form data was invalid..."
    })
