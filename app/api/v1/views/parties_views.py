""" This module handles views related to office data """

# Third party imports
from flask import request
from flask.views import MethodView


# Local imports
from app.api.v1.models.parties_models import PartyModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import Validators


class PartyViews(MethodView):
    """ Defines views for office """

    @classmethod
    def post(cls):
        """ Passes request to either get or post data to office models """

        raw_party = request.get_json()

        try:
            party = Validators.validate_json('party', raw_party)
            party_models = PartyModel(
                party['party_name'], party['hq_address'], party['logo_url'])
            response = party_models.create_party()
            return Serializer.serialize(response, 201)
        except Exception as error:
            print(error)
            return Serializer.serialize(error.args[0], 400)

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
            'Party {} is not available'.format(party_id), 404, 404)
        return result

    @classmethod
    def put(cls, party_id):
        """ updates party information """

        update_name = request.get_json()

        try:
            response = PartyModel.update_party(party_id, update_name)
            result = Serializer.serialize(response, 200)
            return result
        except Exception as error:
            return Serializer.serialize(error.args[0], 404, 404)

    @classmethod
    def delete(cls, party_id):
        """ sendes a delete request to the party models """

        try:
            response = PartyModel.delete_party(party_id)
            result = Serializer.serialize(response, 200)
            return result
        except Exception as error:
            return Serializer.serialize(error.args[0], 404, 404)
