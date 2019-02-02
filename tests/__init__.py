# Third party imports
import unittest

# Local imports
from app import create_app


class TestBaseClass(unittest.TestCase):
    """ Creates a base test class """

    def setUp(self):
        """ Sets up testing client """

        self.app = create_app('testing')
        self.client = self.app.test_client()
