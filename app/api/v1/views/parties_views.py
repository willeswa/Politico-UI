""" This module handles views related to office data """

# Third party imports
from flask import request
from flask.views import MethodView


# Local imports
from app.api.v1.models.parties_models import PartyModel
from app.api.utils.serializer import Serializer


class PartyViews(MethodView):
    """ Defines views for office """

    @classmethod
    def post(cls):
        """ Passes request to either get or post data to office models """

        party = request.get_json()
        party_model = PartyModel(
            party['party_name'], party['party_official'], party['party_hq'], party['logo_url'])

        response = party_model.create_party()
        result = Serializer.serialize(response, 201, 'Created')
        return result

    @classmethod
    def get(cls, party_id):
        """ Sends a get request to the part models """

        if party_id is None:
            response = PartyModel.retrieve_all_parties()
            result = Serializer.serialize(response, 200)
            return result

        exists = PartyModel.party_exists(party_id)
        if exists:
            response = PartyModel.get_specific_party(party_id)
            result = Serializer.serialize(response, 200)
            return result

        result = Serializer.serialize(
            'Office {} is not available'.format(party_id), 404, 'Not Found')
        return result

    @classmethod
    def delete(cls, party_id):
        """ sendes a delete request to the party models """

        party = PartyModel.party_exists(party_id)
        if party:
            response = PartyModel.delete_party(party)
            result = Serializer.serialize(response, 200)
            return result

        response = 'Party not found'
        result = Serializer.serialize(response, 404, 'Not Found')
        return result
