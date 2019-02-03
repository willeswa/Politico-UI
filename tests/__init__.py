""" Defines base test cases """

# Third party imports
import unittest

# Local imports
from app import create_app
from app.api.v1.models.office_models import OfficeModel


class TestBaseClass(unittest.TestCase):
    """ Creates a base test class """
    test_office_db = [{
        "created_on": "Sunday, 03. February 2019 05:23PM",
        "name": "President of the Republic of Kenya",
        "office_id": 1,
        "office_type": "Valid Office Type"
    }]

    def setUp(self):
        """ Sets up testing client """

        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

        self.demo_office = dict(office_type='County Government Leadership',
                                name='The Governor, County Government of Bungoma')
        self.bad_request = dict(office_type="__",
                                name="Govornor Bungoma")
