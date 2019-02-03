""" This module contains classes that handle party related data """

# Standard imports
import datetime

# Local imports
from flask import make_response, jsonify

PARTY_DB = []


class PartyModel:
    """ Defines methods that handle operations regarding parties """

    def __init__(self, party_name, party_official, party_hq, logo_url):
        """ Initializes instance variables """

        self.party_name = party_name
        self.party_official = party_official
        self.party_hq = party_hq
        self.logo_url = logo_url
        self.party_id = len(PARTY_DB) + 1
        self.created_on = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    def create_party(self):
        """ Creates a political party """

        try:
            party = {}

            party['party_id'] = self.party_id
            party['party_name'] = self.party_name
            party['party_official'] = self.party_official
            party['party_hq'] = self.party_hq
            party['logo_url'] = self.logo_url
            party['created_on'] = self.created_on

            PARTY_DB.append(party)

            response = make_response(
                jsonify({'status': 201, 'message': 'Successfuly created party'}), 201)

            return response

        except Exception as error:
            raise Exception(error)
