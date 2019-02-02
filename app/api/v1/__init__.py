# local imports
from flask_restful import Api
from flask import Blueprint

""" Create blueprints """
v1 = Blueprint('version', __name__, url_prefix='/api/v1')
api = Api(v1, catch_all_404s=True)
