""" This module handles views related to office data """
# Third party imports
from flask_restful import Resource, reqparse
from flask import json

# Local imports
from app.api.v1.models.office_models import OfficeModel
from app.api.utils.validators import Validators


class OfficeViews(Resource):
    """ Handles views related to bundled offices """

    def __init__(self):
        self.parser = reqparse.RequestParser()

    def post(self):
        """ Passes data to the models to create an office """
        self.parser.add_argument('office_type', required=True, type=Validators.validate_word,
                                 help='Provide a valid office type')
        self.parser.add_argument('name', required=True, type=Validators.validate_word,
                                 help='Provide a valid office name')
        office = self.parser.parse_args()

        office_model = OfficeModel(office['office_type'], office['name'])
        response = office_model.create_office()
        return json.loads(response.data), response.status_code

    @classmethod
    def get(cls):
        """ Passes request to retrieve data to the models """
        response = OfficeModel.retrieve_all_offices()
        return json.loads(response.data), response.status_code
