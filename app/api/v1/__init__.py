""" Creates application blueprints and versions """

# Third party imports
from flask_restful import Api
from flask import Blueprint

# Local imports
from app.api.v1.views.office_views import OfficeViews, SpecificOfficeViews
from app.api.v1.views.parties_views import PartyViews, SpecificPartyViews

# Creates blueprint
V1 = Blueprint('version', __name__, url_prefix='/api/v1')
API = Api(V1, catch_all_404s=True)


API.add_resource(OfficeViews, '/offices', methods=['POST', 'GET'])
API.add_resource(SpecificOfficeViews,
                 '/offices/<int:office_id>', methods=['GET'])
API.add_resource(PartyViews, '/parties', methods=['GET', 'POST'])
API.add_resource(SpecificPartyViews,
                 '/parties/<int:party_id>', methods=['GET'])
