""" This module contains tests for version two of the application """

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
