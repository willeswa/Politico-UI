""" Creates application blueprints and versions """

# Third party imports
from flask import Blueprint

# Local imports
# from app.api.v1.views.office_views import OfficeViews, SpecificOfficeViews
# from app.api.v1.views.parties_views import PartyViews, SpecificPartyViews

# Creates blueprint
V1 = Blueprint('version', __name__, url_prefix='/api/v1')

from app.api.v1.views import office_views