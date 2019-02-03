""" This module handles views related to parties data """
# Standard imports
import json

# Third party imports
from flask_restful import Resource, reqparse

# Local imports
from app.api.v1.models.parties_models import PartyModel
from app.api.utils.validators import Validators


class PartyViews(Resource):
    """ Handles views related to hundled parties """

    def __init__(self):
        """ initializes instance variables """

        self.parser = reqparse.RequestParser()

    def post(self):
        """ Passes data to the models to create a party """

        self.parser.add_argument('party_name', required=True, type=Validators.validate_word,
                                 help='Provide a valid party name')
        self.parser.add_argument('party_official', required=True, type=Validators.validate_word,
                                 help='Provide a valid name for party official')
        self.parser.add_argument('party_hq', required=True, type=Validators.validate_word,
                                 help='Provide a valid address')
        self.parser.add_argument('logo_url', required=True, type=Validators.validate_url,
                                 help='Provide a valid url for logo')
        party = self.parser.parse_args()

        party_model = PartyModel(
            party['party_name'], party['party_official'], party['party_hq'], party['logo_url'])
        response = party_model.create_party()
        return json.loads(response.data), response.status_code

    @classmethod
    def get(cls):
        """ Passes request to retrieve parties to the models """
        response = PartyModel.retrieve_all_parties()
        return json.loads(response.data), response.status_code
