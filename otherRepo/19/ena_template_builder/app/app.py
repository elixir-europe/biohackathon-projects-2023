"""Create app."""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS to allow requests from client on different origin
CORS(app, resources={r'/*': {'origins': '*'}})
