""" Defines base test cases """

# Third party imports
import json
import unittest

# Local imports
from app import create_app
from app.api.v1.models.office_models import OfficeModel
from app.api.v2.dbconfig import DB
from app.api.utils.validators import Validators

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


class TestBaseClass(unittest.TestCase):
    """ Creates a base test class """

    test_office_db = [{
        "created_on": "Sunday, 03. February 2019 05:23PM",
        "name": "President of the Republic of Kenya",
        "office_id": 1,
        "office_type": "Valid Office Type"
    }]

    demo_office = dict(office_type='Legislative',
                       office_name='Office of the Governor')

    bad_party = dict(party_name='The Catwalking Party',
                     hq_address='Party HeadQuaters',
                     logo_url='some')

    missing_key_party = dict(party_name='The Catwalking Party',
                             hq_address='Party HeadQuaters')

    missing_value_party = dict(party_name='The Catwalking Party',
                               hq_address='Party HeadQuaters',
                               logo_url="")

    demo_party = dict(party_name='The Catwalking Party',
                      hq_address='Nyeri Headquaters',
                      logo_url='https://images.unsplash.com0')

    bad_request = dict(office_type="__",
                       office_name="Govornor Bungoma")

    login_data = dict(email='gwiliez@gmail.com',
                      password='password')
                    
    wrong_pass = dict(email='gwiliez@gmail.com',
                      password='pass')

    vote_data = dict(user_id=1,
                     office_id=1,
                     vote=1)

    new_user = dict(firstname='Godfrey',
                    lastname='Wanajala',
                    othername='Willies',
                    email='gwiliez@gmail.com',
                    password='password',
                    phone_number='0725171175',
                    passport_url='http://logo.com')

    bad_user = dict(firstname='Godfrey',
                    lastname='Wanajala',
                    othername='Willies',
                    email='gwiliez@gmail.com',
                    password='password',
                    phone_number='0725171175',
                    passport_url='logo')

    missing_keys = dict(firstname='Godfrey',
                        lastname='Wanajala',
                        othername='Willies',
                        email='gwiliez@gmail.com',
                        password='password')

    def setUp(self):
        """ Sets up testing client """

        DB.drop_tables()
        DB.create_tables()
        self.app = create_app('testing')
        self.client = self.app.test_client()

        self.app_context = self.app.app_context()
        self.app_context.push()

    def signup(self):
        return self.client.post('/api/v2/auth/signup',
                                data=json.dumps(self.new_user),
                                content_type='application/json')

    def signin(self):
        return self.client.post('/api/v2/auth/signin',
                                data=json.dumps(self.login_data),
                                content_type='application/json')

    def vote(self, url):
        return self.client.post('/api/v2/votes',
                                data=json.dumps(self.vote_data),
                                content_type='application/json')

    def test_empty_json(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps({}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
