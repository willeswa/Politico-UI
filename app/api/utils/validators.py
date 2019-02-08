""" Contains  classes that handle data validation """
import re
import json

# Third party imports
from marshmallow import Schema, fields, ValidationError, post_load

# Local imports
from app.api.utils.serializer import Serializer
from app.api.v1.models.parties_models import PartyModel


class Validator:

    @classmethod
    def json_has_data(cls, json_dict):
        """ Validates  """
        if not json_dict:
            return 'You cannot submit an empty json'

        return json_dict

    @classmethod
    def field_exists(cls, entity, **data):
        if entity == 'party':
            for key, value in data.items():
                if key not in ('party_name', 'party_official', 'party_hq', 'logo_url'):
                    return 'Missing {} field'.format(key)
                elif Validator.is_valid_word(value) is None:
                    return 'Missing value for the {} field'.format(key)
            return data

        elif entity == 'office':
            for key, value in data.items():
                if key not in ('office_name', 'office_type'):
                    return 'Missing {} field'.format(key)
                elif Validator.is_valid_word(value) is None:
                    return 'Missing value for the {} field'.format(key)
            return data

    @classmethod
    def wrong_url(cls, error):
        return Serializer.serialize('Your url seems to be foreign. Are you sure it is a valid url?', 404, 404)

    @classmethod
    def bad_request(cls, error):
        return Serializer.serialize('Invalid submission. Your submission has no body', 400, 400)

    @classmethod
    def internal_server_error(cls, error):
        return Serializer.serialize('The system broke down', 500, 500)

    @classmethod
    def method_not_allowed(cls, error):
        return Serializer.serialize('Method not allowed. Make sure you are sending the right HTTP request', 405, 405)

    @classmethod
    def is_valid_word(cls, word_entity=''):
        """ validates strings """

        pattern = r'[a-zA-Z]'
        match = re.match(pattern, word_entity)
        return match

# def validate_url(url):
#     """ Validates urls """

#     is_valid_url = urlparse(url)
#     url_scheme = is_valid_url.scheme

#     if url_scheme in ('http', 'https'):
#         return url
#     return 'Invalid url'


# def is_empty(json_dict, key):
#     """ Checks for an empty field """

#     _dict = json.dumps(json_dict)

#     if key in _dict.keys():
#         return True

#     return 'You must provide {}'.format(key)
