""" Defines base test cases """

# Third party imports
import json
import unittest

# Local imports
from app import create_app
from app.api.v1.models.office_models import OfficeModel
from app.api.v2.dbconfig import Database
from app.api.utils.validators import Validators

DB = Database()

class TestBaseClass(unittest.TestCase):
    """ Creates a base test class """

    def setUp(self):
        """ Sets up testing client """

        self.app = create_app('testing')
        self.app.config['JWT_SECRET_KEY'] = 'super secret'
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        with self.app.app_context():
            self.db = DB
            self.db.drop_tables()
            self.db.create_tables()
            self.db.create_admin()

        response = self.client.post('/api/v2/auth/signin',
                                    data=json.dumps(self.admin_data),
                                    content_type='application/json')

        super_token = response.get_json()['data'][0]['token']

        self.super_headers = {"Authorization": "Bearer {}".format(super_token)}

        self.client.post('/api/v2/auth/signup',
                         data=json.dumps(self.new_user),
                         content_type='application/json')

        user_response = self.client.post('/api/v2/auth/signin',
                                         data=json.dumps(self.login_data),
                                         content_type='application/json')

        user_token = user_response.get_json()['data'][0]['token']

        self.normal_headers = {"Authorization": "Bearer {}".format(user_token)}

        self.client.post('/api/v2/parties',
                         data=json.dumps(self.demo_party),
                         content_type='application/json',
                         headers=self.super_headers)

        self.client.post('/api/v2/offices',
                         data=json.dumps(self.demo_office2),
                         content_type='application/json',
                         headers=self.super_headers
                         )

    test_office_db = [{
        "created_on": "Sunday, 03. February 2019 05:23PM",
        "name": "President of the Republic of Kenya",
        "office_id": 1,
        "office_type": "Valid Office Type"
    }]

    party_test = [
        {
            "created_on": "Wednesday, 06. February 2019 10:39PM",
            "logo_url": "link-2",
            "party_hq": "Red Counter",
            "party_id": 1,
            "party_name": "Orange Democratic Movement",
            "party_official": "Raila Odinga"
        }
    ]

    demo_office = dict(office_type='Legislative',
                       office_name='Office of the Governor')
    
    demo_office2 = dict(office_type='Federal',
                       office_name='Office of the Senator')

    bad_party = dict(party_name='The Catwalking Party',
                     hq_address='Party HeadQuaters',
                     logo_url='some')

    missing_key_party = dict(party_name='The Catwalking Party',
                             hq_address='Party HeadQuaters')

    missing_value_party = dict(party_name='The Catwalking Party',
                               hq_address='Party HeadQuaters',
                               logo_url="")

    demo_party = {
        "party_name": "The Catwalking Party",
        "hq_address": "Nyeri Headquaters",
        "logo_url": "https://images.unsplash.com"
    }

    demo_party2 = {
        "party_name": "The Datwalking Party",
        "hq_address": "Nyeri Headquaters",
        "logo_url": "https://images.unsplash.com"
    }

    bad_request = dict(office_type="__",
                       office_name="Govornor Bungoma")

    login_data = dict(email='gwiliez@gmail.com',
                      password='password')

    admin_data = dict(email='gwiliez@ymail.com',
                      password='admin')

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

    new_user2 = dict(firstname='Godfrey',
                    lastname='Wanajala',
                    othername='Willies',
                    email='gwiliez@mail.com',
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

    def vote(self, url):
        return self.client.post('/api/v2/votes',
                                data=json.dumps(self.vote_data),
                                content_type='application/json')

    def test_empty_json(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=json.dumps({}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
