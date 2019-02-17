""" This module contains a class to validate user input and handle various errors"""
# standard imports
import re

# local imports
from app.api.utils.serializer import Serializer


class Validators:
    """ Validates user inputs """

    @classmethod
    def validate_json(cls, entity, entity_data):
        """ Validates the fields/keys and the values of the json object """

        if entity_data:

            if entity is 'party':
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

            elif entity is 'office':
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
                raise Exception('Missing field in the office json')
            elif entity is 'user_signup':
                if {'firstname', 'lastname', 'othername', 'email', 'password',
                        'phone_number', 'passport_url'} <= set(entity_data):

                    passport_url = re.match(
                        r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', entity_data['passport_url'])

                    if passport_url is not None:
                        if entity_data['firstname'].isalpha() and entity_data['othername'].isalpha() and entity_data['lastname'].isalpha():
                            valid_email = re.match(
                                r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', entity_data['email'])
                            if valid_email is not None:
                                return entity_data
                            raise Exception('Invalid email')
                        raise Exception('Names can only be alphabets')
                    raise Exception('Invalid passport url')

                raise Exception('Missing field in the json object')

            elif entity is 'user_login':
                if {'email', 'password'} <= set(entity_data):
                    if entity_data['password'].isalnum():
                        valid_email = re.match(
                            r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', entity_data['email'])
                        if valid_email is not None:
                            return entity_data
                        raise Exception('Invalid email')
                    raise Exception('Password must be atleast 6 characters')
                raise Exception('Missing field in the json object')

            elif entity is 'update_party':
                if {'party_name'} <= set(entity_data):
                    name = re.match(r'\w+ \w+ \bParty\b',
                                    entity_data['party_name'])
                    if name is not None:
                        return entity_data
                    raise Exception(
                        "Party name must be a three phrased name and ends with 'Party'")
                raise Exception("Missing the 'Party Name' field in your json")
            elif entity is 'candidate':
                if {'party_id', 'candidate_id'} <= set(entity_data):
                    if isinstance(entity_data['party_id'], int) and isinstance(entity_data['candidate_id'], int):
                        return entity_data
                    raise Exception('Entry must be integers only')
                raise Exception('Missing fields in your candidate json')
            elif entity is 'vote':
                if {'office_id', 'candidate_id'} <= set(entity_data):
                    if isinstance(entity_data['office_id'], int) and isinstance(entity_data['candidate_id'], int):
                        return entity_data
                    raise Exception(
                        'office_id and candidate_id should be integer')
                raise Exception('Missing fields in your vote json')
        raise Exception('Your json object is empty.')

    @classmethod
    def wrong_url(cls, error):
        """ Handles attempts to visit wrong urls """

        return Serializer.serialize(
            'Your url seems to be foreign. Are you sure it is a valid url?', 404, error)

    @classmethod
    def bad_request(cls, error):
        """ Handles non custom bad requests """
        return Serializer.serialize('Invalid submission. Your submission has no body', 400, error)

    @classmethod
    def internal_server_error(cls, error):
        """ Handles errors related to internal error servers """
        return Serializer.serialize('The system broke down', 500, error)

    @classmethod
    def method_not_allowed(cls, error):
        """ Handles request sent to the wrong routes """
        return Serializer.serialize(
            'Method not allowed. Make sure you are sending the right HTTP request', 405, error)
