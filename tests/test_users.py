""" This module contains test cases for authentication. """

# standard imports
import json

# Local imports
from tests import TestBaseClass


class TestsAuthCases(TestBaseClass):
    """ Test cases for authentication. """

    def test_create_user(self):
        """ Tests if signup works as expected. """

        response = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.new_user2),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_missing_keys(self):
        """ Tests if signup works as expected. """

        response = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(self.missing_keys),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_sign_in(self):
        """Test if signin works as expected. """

        response = self.client.post('/api/v2/auth/signin',
                                    data=json.dumps(self.admin_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_unregistered_user(self):
        """ Tests the response when an unregistered user tries to login. """

        response = self.client.post('/api/v2/auth/signin',
                                    data=json.dumps(
                                        {"email": "jim@kama.com", "password": "passowrd"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_register_candidate(self):
        """ Tests if creating politician works as expected. """

        response = self.client.post('/api/v2/offices/1/register',
                                    data=json.dumps({"party_id": 1,
                                                     "candidate_id": 1}),
                                    headers=self.super_headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data.decode())[
                         'error'], 'Successfully updated the name of the party')

    def test_double_registration(self):
        """ Tests if signup works as expected. """

        response = self.client.post(
            'api/v2/auth/signup',
            data=json.dumps(self.new_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 409)

    def test_bad_password(self):
        """ Tests response when the password is an empty string """

        response = self.client.post(
            'api/v2/auth/signup',
            data=json.dumps({"email": "gwiliez@gmail.com", "password": " "}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
