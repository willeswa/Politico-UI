""" This module handles views related to office data """

# Third party imports
from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity


# Local imports
from app.api.v2.models.parties_models import PartyModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import Validators


class PartyViews(MethodView):
    """ Defines views for office """

    @classmethod
    @jwt_required
    def post(cls):
        """ Passes post request to the party models """

        current_user = get_jwt_identity()

        if current_user['is_admin']:

            raw_party = request.get_json()

            try:
                party = Validators.validate_json('party', raw_party)
                if PartyModel.party_name_taken(party['party_name']):
                    return Serializer.serialize("'{}' is taken. Choose another name!".format(party['party_name']), 409)

                party_models = PartyModel(
                    party['party_name'], party['hq_address'], party['logo_url'])
                response = party_models.create_party()
                return Serializer.serialize(response, 201)
            except Exception as error:
                print(error)
                return Serializer.serialize(error.args[0], 400)
        return Serializer.serialize('You are not authorized to perform this action.', 401)

    @classmethod
    def get(cls, party_id):
        """ Sends a get request to the part models """

        if party_id is None:
            response = PartyModel.retrieve_all_parties()
            return Serializer.serialize(response, 200)

        if PartyModel.party_exists(party_id):
            response = PartyModel.get_specific_party(party_id)
            result = Serializer.serialize(response, 200)
            return result

        result = Serializer.serialize(
            'Party {} is not found'.format(party_id), 404, 404)
        return result

    @classmethod
    @jwt_required
    def put(cls, party_id):
        """ updates party information """

        current_user = get_jwt_identity()

        if current_user['is_admin']:
            if PartyModel.party_exists(party_id):
                update_name = request.get_json()
                try:
                    party = Validators.validate_json(
                        'update_party', update_name)
                    if PartyModel.party_name_taken(party['party_name']):
                        return Serializer.serialize("'{}' is taken. Choose another name!".format(party['party_name']), 409)
                    response = PartyModel.update_party(
                        party_id, party['party_name'])
                    return Serializer.serialize(response, 200)

                except Exception as error:
                    return Serializer.serialize(error.args[0], 404, 404)

            return Serializer.serialize('Party {} not found'.format(party_id), 404, 404)
        return Serializer.serialize('You are not authorized to perform this action.', 401)

    @classmethod
    @jwt_required
    def delete(cls, party_id):
        """ sendes a delete request to the party models """

        current_user = get_jwt_identity()
        if current_user['is_admin']:

            if PartyModel.party_exists(party_id):

                try:
                    response = PartyModel.delete_party(party_id)
                    result = Serializer.serialize(response, 200)
                    return result
                except Exception as error:
                    return Serializer.serialize(error.args[0], 404, 404)
            return Serializer.serialize('Party {} not found'.format(party_id), 404, 404)

        return Serializer.serialize('You are not authorized to perform this action.', 401)
