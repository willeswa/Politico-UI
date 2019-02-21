""" This module handles views related to office data """

# Third office imports
from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity

# Local imports
from app.api.v2.models.office_models import OfficeModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import Validators


class OfficeViews(MethodView):
    """ Defines views for office """

    @classmethod
    @jwt_required
    def post(cls):
        """ Sends a post request to the office models """

        current_user = get_jwt_identity()

        if current_user['is_admin']:

            raw_office = request.get_json()

            try:
                office = Validators.validate_json('office', raw_office)

                if OfficeModel.office_already_created(office['office_name'], office['office_type']):
                    return Serializer.serialize("'The {} {}' is already created!".format(office['office_type'], office['office_name']), 409)

                office_models = OfficeModel(
                    office['office_name'], office['office_type'])
                response = office_models.create_office()
                return Serializer.serialize(response, 201)
            except Exception as error:
                return Serializer.serialize(error.args[0], 400)

        return Serializer.serialize('You are not authorized to perform this action.', 401)

    @classmethod
    def get(cls, office_id):
        """ Sends get requests to the office models """
        if office_id is None:
            response = OfficeModel.retrieve_all_offices()
            result = Serializer.serialize(response, 200)
            return result

        if OfficeModel.office_exists(office_id):
            response = OfficeModel.get_specific_office(office_id)
            result = Serializer.serialize(response, 200)
            return result

        result = Serializer.serialize(
            'Office {} is not available'.format(office_id), 404, 'Not Found')
        return result

    @classmethod
    @jwt_required
    def delete(cls, office_id):
        """ sendes a delete request to the office models """

        current_user = get_jwt_identity()
        if current_user['is_admin']:

            if OfficeModel.office_exists(office_id):

                try:
                    response = OfficeModel.delete_office(office_id)
                    result = Serializer.serialize(response, 200)
                    return result
                except Exception as error:
                    return Serializer.serialize(error.args[0], 404)
            return Serializer.serialize('office {} not found'.format(office_id), 404)

        return Serializer.serialize('You are not authorized to perform this action.', 401)