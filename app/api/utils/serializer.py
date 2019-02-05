""" This module serializes responses """

# Third party imports
from flask import jsonify, make_response

class Serializer:
    """ Contains method that serializes data """

    @classmethod
    def serialize(self, response, status_code, message='Success',):
        result = make_response(
            jsonify({'status': message, 'message': response}), status_code
        )
        return result
        