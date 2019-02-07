""" This module handles views related to office data """

# Third party imports
from flask import request, jsonify, make_response
from flask.views import MethodView
from marshmallow import ValidationError


# Local imports
from app.api.v1.models.parties_models import PartyModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import schema


class PartyViews(MethodView):
    """ Defines views for office """

    @classmethod
    def post(cls):
        """ Passes request to either get or post data to office models """

        raw_party = request.get_json()

        if not raw_party:
            return make_response(jsonify({'message': 'Your json file is empty',
                                          'status': 400}), 400)
        try:
            schema_data = schema.dump(raw_party)
            party = schema_data.data
            party_model = PartyModel(
                party['party_name'], party['party_official'], party['party_hq'], party['logo_url'])

            response = party_model.create_party()
            result = Serializer.serialize(response, 201, 'Created')

            return result
        except (KeyError, ValidationError) as error:
            if error is KeyError:
                return make_response(jsonify({'message': 'Missing field for {}'.format(error.args[0]),
                                              'status': 400}), 400)
            return make_response(jsonify({'message': '{}'.format(error.args[0]['{}'.format(raw_party.value)][0]),
                                          'status': 422}), 422)

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
    def put(cls, party_id):
        """ updates party information """

        updates = request.get_json()

        party = PartyModel.party_exists(party_id)

        if party:
            response = PartyModel.update_party(party, **updates)
            result = Serializer.serialize(response, 200)
            return result

        return make_response(jsonify({'message': 'Party Does not exist',
                                      'status': 'Not Found'}), 404)

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
