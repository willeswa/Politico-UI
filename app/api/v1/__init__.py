""" Creates application blueprints and versions """

# Third party imports
from flask import Blueprint

# Local imports
from app.api.v1.views.parties_views import PartyViews
from app.api.v1.views.office_views import OfficeViews


# Creates blueprint
V1 = Blueprint('version', __name__, url_prefix='/api/v1')

# Hook routes
def define_routes(view, endpoint, url, identifier='id', identifier_type='int'):
    """ Creates an api endpoint and assigns route"""
    view_func = view.as_view(endpoint)
    V1.add_url_rule(url, view_func=view_func, defaults={identifier: None}, methods=['GET',])
    V1.add_url_rule(url, view_func=view_func, methods=['POST',])
    V1.add_url_rule('%s/<%s:%s>'%(url, identifier_type, identifier), view_func=view_func, methods=['GET', 'PUT', 'DELETE'])

define_routes(PartyViews, 'parties', '/parties', identifier='party_id')
define_routes(OfficeViews, 'offices', '/offices', identifier='office_id')

