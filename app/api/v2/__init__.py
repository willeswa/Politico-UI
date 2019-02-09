""" Creates blueprints and registers routes for version 2 """

# Thirdy party
from flask import Blueprint


# Create blueprint
v2 = Blueprint('version2', __name__, url_prefix='/api/v2')