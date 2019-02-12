""" This module contains a class to validate user input and handle various errors"""
# standard imports
import re

# local imports
from app.api.utils.serializer import Serializer


class Validators:
    """ Validates user inputs """

    @classmethod
    def checks_for_keys(cls, entity, entity_data):

        if entity == 'party':
            if {'party_name', 'hq_address', 'logo_url'} <= set(entity_data):
                name = re.match(r'\w+ \w+ \bParty\b',
                                entity_data['party_name'])
                if name is not None:
                    hq_address = re.match(
                        r'[a-zA-Z09]', entity_data['hq_address'])
                    if hq_address is not None:
                        logo_url = re.match(
                            r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', entity_data['logo_url'])
                        if logo_url is not None:
                            return entity_data
                        raise Exception('Invalid Url for the logo')
                    raise Exception(
                        'Your party head quaters address is invalid')
                raise Exception(
                    "Your party name must be three phrased and end with 'Party'")
            raise Exception('Missing party field')

        elif entity == 'office':
            if {'office_name', 'office_type'} <= set(entity_data):

                match = re.match(r'\bOffice\b \bof\b \bthe\b \w+',
                                 entity_data['office_name'])
                if match is not None:
                    if entity_data['office_type'.lower()].lower() not in (
                            'federal', 'legislative', 'state', 'local government'):
                        raise Exception("Invalid 'Office Type' choice ")
                    return entity_data

                raise Exception(
                    "Enter office name in the formart of 'Office of the president'")
            raise Exception('Missing field in the Json Object')

    @classmethod
    def wrong_url(cls, error=404):
        return Serializer.serialize('Your url seems to be foreign. Are you sure it is a valid url?', 404, 404)

    @classmethod
    def bad_request(cls, error=400):
        return Serializer.serialize('Invalid submission. Your submission has no body', 400, 400)

    @classmethod
    def internal_server_error(cls, error=500):
        return Serializer.serialize('The system broke down', 500, 500)

    @classmethod
    def method_not_allowed(cls, error=405):
        return Serializer.serialize('Method not allowed. Make sure you are sending the right HTTP request', 405, 405)
