""" This module tests the version 1 of the api """

# Third party imports
import json

# Local imports
from tests import TestBaseClass


class TestApiEndPoints(TestBaseClass):
    """ This class handles methods to test version 1 of the api """

    def test_post_to_office(self):
        """ Tests create an office """

        response = self.client.post(
            'api/v1/offices',
            data=json.dumps(self.demo_office),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_invalid_office(self):
        """ Tests invalid office post """

        response = self.client.post(
            'api/v1/offices',
            data=json.dumps(self.bad_request),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_get_all_offices(self):
        """ Tests retrieve all offices"""

        response = self.client.get('api/v1/offices')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_office(self):
        """ Tests retrieve specific office """

        response = self.client.get('api/v1/offices/1')
        self.assertEqual(response.status_code, 200)

    def tests_not_found_office(self):
        """ Tests the response on a non-existant resource  """

        response = self.client.get('api/v1/offices/10')
        self.assertEqual(response.status_code, 404)

    def test_create_party(self):
        """ Tests create party"""

        response = self.client.post(
            'api/v1/parties',
            data=json.dumps(self.demo_party),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_invalid_party_data(self):
        """ Tests invalid party post """

        response = self.client.post(
            'api/v1/parties',
            data=json.dumps(self.bad_party),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_get_all_parties(self):
        """ Tests retrieve all parties """

        response = self.client.get('api/v1/parties')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_party(self):
        """ Tests retrieve a specific party """

        response = self.client.get('api/v1/parties/1')
        self.assertEqual(response.status_code, 200)

    def tests_not_found_party(self):
        """ Tests the response on a non-existant resource  """

        response = self.client.get('api/v1/parties/10')
        self.assertEqual(response.status_code, 404)
