""" This module contains tests for version two of the application """

# Local imports
from tests import TestBaseClass
from app.api.v2.dbconfig import DB


class TestVersion2(TestBaseClass):
    """ Contain test cases for version 2 """

    def test_db_connection(self):
        """ tests_db connection """
        with DB as conn:
            self.assertEqual(
                conn.get_dsn_parameters()['dbname'], 'test_politico')
