""" This module contains classes that handle party related data """

# Standard imports
import datetime


PARTY_DB = []


class PartyModel:
    """ Defines methods that handle operations regarding parties """

    def __init__(self, party_name, hq_address, logo_url):
        """ Initializes instance variables """

        self.party_name = party_name
        self.hq_address = hq_address
        self.logo_url = logo_url
        self.party_id = len(PARTY_DB) + 1
        self.created_on = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    def create_party(self):
        """ Creates a political party """

        try:
            party = {}

            party['party_id'] = self.party_id
            party['party_name'] = self.party_name
            party['hq_address'] = self.hq_address
            party['logo_url'] = self.logo_url
            party['created_on'] = self.created_on

            PARTY_DB.append(party)

            return 'Successfuly created party'

        except Exception as error:
            raise Exception(error)

    @classmethod
    def retrieve_all_parties(cls):
        """ Retrieves all parties  """
        return PARTY_DB

    @classmethod
    def get_specific_party(cls, party_id):
        """ returns a specific party given party id """

        party = PartyModel.party_exists(party_id)
        return party

    @classmethod
    def party_exists(cls, party_id):
        """ Checks if a specific party exists """

        for party in PARTY_DB:
            if party['party_id'] == party_id:
                return party
        return None

    @classmethod
    def update_party(cls, party_id, new_name):
        """ Updates party with user defined information """

        party = PartyModel.party_exists(party_id)
        if party:
            party['party_name'] = new_name['new_name']
            return 'Successfully Updated the name of the party'
        raise Exception('Party does not exists')

    @classmethod
    def delete_party(cls, party_id):
        """ Deletes party if exists """

        party = PartyModel.party_exists(party_id)
        if party:
            PARTY_DB.remove(party)
            return 'Successfuly deleted party'
        raise Exception('Party does not exist')
