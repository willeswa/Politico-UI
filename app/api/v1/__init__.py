""" Creates application blueprints and versions """

# Third party imports
from flask_restful import Api
from flask import Blueprint

# Local imports
from app.api.v1.views.office_views import OfficeViews, SpecificOfficeViews

# Creates blueprint
V1 = Blueprint('version', __name__, url_prefix='/api/v1')
API = Api(V1, catch_all_404s=True)


API.add_resource(OfficeViews, '/offices')
API.add_resource(SpecificOfficeViews, '/offices/<int:office_id>')
