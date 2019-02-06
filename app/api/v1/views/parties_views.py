""" This module handles views related to office data """

# Third party imports
from flask import request, jsonify, make_response
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

        if not party:
            return make_response(jsonify({'message': 'You cannot submit an empty party',
                                          'status': 'Bad Request'}), 400)

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

        else:
            exists = PartyModel.party_exists(party_id)
            if exists:
                response = PartyModel.get_specific_party(party_id)
                result = Serializer.serialize(response, 200)
                return result
            else:
                result = Serializer.serialize(
                    'Office {} is not available'.format(party_id), 404, 'Not Found')
                return result

    def put(self, party_id):
        """ updates party information """

        updates = request.get_json()
        
        response = PartyModel.update_party(party_id, **updates)
        result = Serializer.serialize(response, 200)
        return result
