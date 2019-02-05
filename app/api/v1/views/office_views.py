""" This module handles views related to office data """
# Standard imports
import json

# Third party imports
from flask import make_response, jsonify, request


# Local imports
from app.api.v1 import V1
from app.api.v1.models.office_models import OfficeModel, DB
from app.api.utils.validators import Validators


class OfficeViews:
    """ Defines views for office """

    @V1.route('/offices', methods=['POST'])
    def post_offices():
        """ Passes request to either get or post data to office models """
        office = request.get_json()
        office_model = OfficeModel(
            office['office_name'], office['office_type'])

        response = office_model.create_office()
        result = make_response(
            jsonify({'status': 'Created', 'message': response}), 201
        )
        return result

    @V1.route('/offices', methods=['GET'])
    def get_offices():
        response = OfficeModel.retrieve_all_offices()
        result = make_response(
            jsonify({'status': 'success', 'message': response}), 200
        )
        return result
