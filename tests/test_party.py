""" This module tests the party module and routes """

# Third party imports
import json


# Local imports
from tests import TestBaseClass


class TestPartyApiEndPoints(TestBaseClass):
    """ This class handles methods to test version 1 of the api """

    def test_create_party(self):
        """ Tests create party"""

        response = self.client.post(
            'api/v1/parties',
            data=json.dumps(self.demo_party),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data.decode())['data'],
                         'Successfuly created party')

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

    def tests_test_edit_no_party(self):
        """ Tests the response on a non-existant resource  """

        response = self.client.put('api/v1/parties/101/name',
                                   data=json.dumps(
                                       {"new_name": "newest name"}),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def tests_delete_party(self):
        """ Tests the delete party route  """

        response = self.client.delete('api/v1/parties/1')
        self.assertEqual(response.status_code, 200)

    def tests_delete_no_party(self):
        """ Tests the delete on a non-existant resource  """

        response = self.client.delete('api/v1/parties/10/delete')
        self.assertEqual(response.status_code, 404)

    def tests_test_edit_party(self):
        """ Tests the response on a non-existant resource  """

        self.client.post(
            'api/v1/parties',
            data=json.dumps(self.demo_party),
            content_type='application/json'
        )
        response = self.client.put('api/v1/parties/1/name',
                                   data=json.dumps(
                                       {"new_name": "newest name"}),
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_no_keys(self):
        """ Tests the response on a non-existant resource  """

        response = self.client.post(
            'api/v1/parties',
            data=json.dumps(self.missing_key_party),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)

    def test_no_values(self):
        """ Tests the response on a non-existant resource  """

        response = self.client.post(
            'api/v1/parties',
            data=json.dumps(self.missing_value_party),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 400)
