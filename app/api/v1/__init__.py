""" Creates application blueprints and versions """

# Third party imports
from flask_restful import Api
from flask import Blueprint


# Creates blueprint
V1 = Blueprint('version', __name__, url_prefix='/api/v1')
API = Api(V1, catch_all_404s=True)
