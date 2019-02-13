""" This module tests the version 1 of the api """

# Third party imports
import json

# Local imports
from tests import TestBaseClass


class TestVersionOnePoints(TestBaseClass):
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

    def test_missing_keys(self):
        """ Test posting a party with a missing key """

        response = self.client.post(
            'api/v1/offices',
            data=json.dumps(self.missing_key_party),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)


class TestVersionTwoEndPoints(TestBaseClass):
    """ defines testcases for version two of the application """

    def test_post_to_office(self):
        """ Tests create an office """

        response = self.client.post(
            'api/v2/offices',
            data=json.dumps(self.demo_office),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_invalid_office(self):
        """ Tests invalid office post """

        response = self.client.post(
            'api/v2/offices',
            data=json.dumps(self.bad_request),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)

    def test_get_all_offices(self):
        """ Tests retrieve all offices"""

        response = self.client.get('api/v2/offices')
        self.assertEqual(response.status_code, 200)

    def test_get_specific_office(self):
        """ Tests retrieve specific office """

        response = self.client.get('api/v2/offices/1')
        self.assertEqual(response.status_code, 200)

    def tests_not_found_office(self):
        """ Tests the response on a non-existant resource  """

        response = self.client.get('api/v2/offices/10')
        self.assertEqual(response.status_code, 404)

    def test_missing_keys(self):
        """ Test posting a party with a missing key """

        response = self.client.post(
            'api/v2/offices',
            data=json.dumps(self.missing_key_party),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
