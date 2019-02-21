""" This module contains tests for version two of the application """

import json

# Local imports
from tests import TestBaseClass
from app.api.v2.dbconfig import Database

DB = Database()


class TestVersion2(TestBaseClass):
    """ Contain test cases for version 2 """

    def test_db_connection(self):
        """ tests_db connection """
        print()
        with DB as conn:
            self.assertEqual(
                conn.get_dsn_parameters()['dbname'], 'test_politico')

    def test_wrong_method(self):
        response = self.client.post('api/v2/parties/1',
                                   data=json.dumps(
                                       {"party_name": "The Glue Party"}),
                                   content_type='application/json',
                                   headers=self.super_headers)
        self.assertEqual(response.status_code, 405)

    def test_wrong_url(self):
        response = self.client.put('api/v2/partieszz')
        self.assertEqual(response.status_code, 404)
