""" Defines base test cases """

# Third party imports
import unittest

# Local imports
from app import create_app
from app.api.v1.models.office_models import OfficeModel


class TestBaseClass(unittest.TestCase):
    """ Creates a base test class """
    test_office_db = [{
        "office_id": 1,
        "office_type": "County Government Office",
        "name": "Governor Bungoma County",
        "created_on": '2019/2/1'
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
