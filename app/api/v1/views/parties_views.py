""" This module handles views related to office data """
# starndard imports
import json

# Third party imports
from flask import request, jsonify, make_response
from flask.views import MethodView


# Local imports
from app.api.v1.models.parties_models import PartyModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import Validator


class PartyViews(MethodView):
    """ Defines views for office """

    @classmethod
    def post(cls):
        """ Passes request to either get or post data to office models """

        raw_party = request.get_json()
        party = Validator.json_has_data(raw_party)
        try:
            valid_party = Validator.field_exists('party', **party)
            party_model = PartyModel(
                valid_party['party_name'], valid_party['party_official'], valid_party['party_hq'], valid_party['logo_url'])
            response = party_model.create_party()
            result = Serializer.serialize(response, 201, 'Created')
            return result

        except Exception as error:
            return Serializer.serialize(
                "Missing {} field".format(error.args[0]), 400)

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
            'Party {} is not available'.format(party_id), 404, 'Not Found')
        return result

    @classmethod
    def put(cls, party_id):
        """ updates party information """

        raw_updates = request.get_json()

        updates = Validator.json_has_data(raw_updates)

        try:
            party = PartyModel.party_exists(party_id)

            if party:
                response = PartyModel.update_party(party, **updates)
                result = Serializer.serialize(response, 200)
                return result

            return make_response(jsonify({'message': 'Party Does not exist',
                                          'status': 'Not Found'}), 404)
        except Exception:
            return Serializer.serialize(updates, 500)

    @classmethod
    def delete(cls, party_id):
        """ sendes a delete request to the party models """

        party = PartyModel.party_exists(party_id)
        if party:
            response = PartyModel.delete_party(party)
            result = Serializer.serialize(response, 200)
            return result

        return make_response(jsonify({'message': 'Party Does not exist',
                                      'status': 'Not Found'}), 404)
