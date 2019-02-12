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

    PARTY_DB_TEST = [
        {
            "created_on": "Wednesday, 06. February 2019 10:39PM",
            "logo_url": "link-2",
            "party_hq": "Red Counter",
            "party_id": 1,
            "party_name": "Orange Democratic Movement",
            "party_official": "Raila Odinga"
        }
    ]

    def setUp(self):
        """ Sets up testing client """

        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

        self.demo_office = dict(office_type='Legislative',
                                office_name='Office of the Governor')

        self.bad_party = dict(party_name='The Catwalking Party',
                              hq_address='Party HeadQuaters',
                              logo_url='some')
        self.missing_key_party = dict(party_name='The Catwalking Party',
                                      hq_address='Party HeadQuaters')

        self.demo_party = dict(party_name='The Catwalking Party',
                               hq_address='Nyeri Headquaters',
                               logo_url='https://images.unsplash.com0')

        self.bad_request = dict(office_type="__",
                                office_name="Govornor Bungoma")
