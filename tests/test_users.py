""" This module contains test cases for users """

# standard imports
import json

# Local imports
from tests import TestBaseClass


class TestsAuthCases(TestBaseClass):
    """ Test cases for authentication """

    def test_create_user(self):
        """ Tests if signup works as expected """

        response = self.client.post(
            'api/v2/auth/signup',
            data=json.dumps(self.new_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_missing_keys(self):
        """ Tests if signup works as expected """

        response = self.client.post(
            'api/v2/auth/signup',
            data=json.dumps(self.missing_keys),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_bad_user(self):
        """ Test posting a party with a missing key """

        response = self.client.post(
            'api/v1/offices',
            data=json.dumps(self.bad_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_sign_in(self):
        """Test if signin works as expected """

        self.signup()
        response = self.signin()
        self.assertEqual(response.status_code, 200)

    def test_wrong_password(self):
        """Test if signin works as expected """

        self.client.post('/api/v2/auth/signup',
                         data=json.dumps(self.new_user),
                         content_type='application/json')

        response = self.client.post('/api/v2/auth/signin',
                                    data=json.dumps(self.wrong_pass),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_unregistered_user(self):
        """ Tests the response when an unregistered user tries to login """

        response = self.client.post('/api/v2/auth/signin',
                                    data=json.dumps(self.login_data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_register_candidate(self):
        """ Tests if creating politician works as expected """

        self.signup()

        self.signin()

        response = self.client.post('/api/v2/office/1/register')
        self.assertEqual(response.status_code, 201)

    def test_register_more_than_one_office(self):
        self.signup()

        self.signin()

        self.client.post('/api/v2/office/1/register')
        response = self.client.post('/api/v2/office/2/register')
        self.assertEqual(response.status_code, 400)

    def test_double_registration(self):
        """ Tests if signup works as expected """
        self.signup()

        response = self.client.post(
            'api/v2/auth/signup',
            data=json.dumps(self.new_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 409)
