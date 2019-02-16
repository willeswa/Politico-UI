""" This module serializes responses """

# Third party imports
from flask import jsonify, make_response


class Serializer:
    """ Contains method that serializes data """

    @classmethod
    def serialize(cls, response, status_code, message=200):
        """ Serializes output to json format """
        if status_code in (404, 400, 405, 409, 401):
            return make_response(jsonify({'status': status_code, 'error': response}), status_code)

        return make_response(jsonify({'status': status_code, 'data': response}), status_code)
