""" This module creates the base test for version 2 """

# standard imports
import unittest

# Local imports
from app import create_app
from app.api.v2.dbconfig import DB


class TestBaseVersion2(unittest.TestCase):
    """ Creates the app and loads configurations for testing """

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()

        with self.app.app_context():
            with DB as conn:
                return conn
