""" This module handles views related to office data """
# Standard imports
import json

# Third party imports
from flask import make_response, jsonify, request
from flask.views import MethodView

# Local imports
from app.api.v1.models.office_models import OfficeModel
from app.api.utils.validators import Validators
from app.api.utils.serializer import Serializer


class OfficeViews(MethodView):
    """ Defines views for office """

    def post(self):
        """ Sends a post request to the office models """
        office = request.get_json()
        office_model = OfficeModel(
            office['office_name'], office['office_type'])

        response = office_model.create_office()
        result = Serializer.serialize(response, 201, 'Created')
        return result

    def get(self, office_id):
        """ Sends get requests to the office models """
        if office_id == None:
            response = OfficeModel.retrieve_all_offices()
            result = Serializer.serialize(response, 200)
            return result
        else:
            exists = OfficeModel.office_exists(office_id)
            if exists:
                response = OfficeModel.get_specific_office(office_id)
                result = Serializer.serialize(response, 200)
                return result
            else:
                # response = {'message': 'Office not found'}
                result = Serializer.serialize('Office {} is not available'.format(office_id), 404, 'Not Found')
                return result

