""" This module handles views related to office data """

# Third office imports
from flask import request
from flask.views import MethodView

# Local imports
from app.api.v1.models.office_models import OfficeModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import Validators


class OfficeViews(MethodView):
    """ Defines views for office """

    @classmethod
    def post(cls):
        """ Sends a post request to the office models """

        raw_office = request.get_json()
        try:
            office = Validators.validate_json('office', raw_office)
            office_models = OfficeModel(office['office_name'], office['office_type'])
            response = office_models.create_office()
            return Serializer.serialize(response, 201)
        except Exception as error:
            return Serializer.serialize(error.args[0], 400)

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
