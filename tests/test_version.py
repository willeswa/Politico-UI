""" This module tests the version 1 of the api """

# Third party imports
import json

# Local imports
from tests import TestBaseClass


class TestApiEndPoints(TestBaseClass):
    """ This class handles methods to test version 1 of the api """

    def test_post_to_office(self):
        response = self.client.post(
            'api/v1/offices',
            data=json.dumps(self.demo_office),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_invalid_office(self):
        response = self.client.post(
            'api/v1/offices',
            data=json.dumps(self.bad_request),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_get_all(self):
        response = self.client.get('api/v1/offices')
        self.assertEqual(response.status_code, 200)
