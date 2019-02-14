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

    def test_sign_in(self):
        """Test if signin works as expected """

        self.client.post('/api/v2/auth/signup',
                         data=json.dumps(self.new_user),
                         content_type='application/json')

        response = self.client.post('/api/v2/auth/signin',
                                    data=json.dumps(self.login_data),
                                    content_type='application/json')

        data = json.loads(response.data.decode())
        self.assertTrue(data['access_token'])
        self.assertEqual(response.status_code, 200)

    def test_register_candidate(self):
        """ Tests if creating politician works as expected """

        self.signup('/api/v2/auth/signup')

        self.signin('/api/v2/auth/signin')

        response = self.client.post('/api/v2/office/1/register')
        self.assertEqual(response.status_code, 201)

    def test_register_more_than_one_office(self):
        self.signup('/api/v2/auth/signup')

        self.signin('/api/v2/auth/signin')

        self.client.post('/api/v2/office/1/register')
        response = self.client.post('/api/v2/office/2/register')
        self.assertEqual(response.status_code, 400)

    def test_double_registration(self):
        """ Tests if signup works as expected """
        self.signup('api/v2/auth/signup')

        response = self.client.post(
            'api/v2/auth/signup',
            data=json.dumps(self.new_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 409)
