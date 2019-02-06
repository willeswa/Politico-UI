""" This module handles views related to office data """

# Third party imports
from flask import make_response, jsonify, request
from flask.views import MethodView

# Local imports
from app.api.v1.models.office_models import OfficeModel
from app.api.utils.serializer import Serializer


class OfficeViews(MethodView):
    """ Defines views for office """

    @classmethod
    def post(cls):
        """ Sends a post request to the office models """
        office = request.get_json()
        if not office:
            return make_response(jsonify({'message': 'You cannot submit an empty json',
                                          'status': 'Bad Request'}), 400)

        office_name = office['office_name']
        office_type = office['office_type']

        office_model = OfficeModel(office_name, office_type)
        response = office_model.create_office()
        result = Serializer.serialize(response, 201, 'Created')
        return result

    @classmethod
    def get(cls, office_id):
        """ Sends get requests to the office models """
        if office_id is None:
            response = OfficeModel.retrieve_all_offices()
            result = Serializer.serialize(response, 200)
            return result

        exists = OfficeModel.office_exists(office_id)
        if exists:
            response = OfficeModel.get_specific_office(office_id)
            result = Serializer.serialize(response, 200)
            return result

        result = Serializer.serialize(
            'Office {} is not available'.format(office_id), 404, 'Not Found')
        return result
