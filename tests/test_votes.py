""" This module contains tests for votes """

import json


from tests import TestBaseClass


class TestVoteCases(TestBaseClass):
    """ This module contains tests that tests votes operation """

    def test_cast_vote(self):
        """ Tests if creating politician works as expected """

        response = self.vote('/api/v2/votes')
        self.assertEqual(response.status_code, 201)

    def test_invalid_vote(self):
        """ Tests an invalud vote """
        response = self.client.post('/api/v2/votes',
                                    data=json.dumps(dict(vote='1')),
                                    content_type='application/json')
        data = response.data.decode()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['error'], 'Vote is integer 1')
    
    def test_vote_twice(self):
        response = self.client.post('/api/v2/votes',
                                    data=json.dumps(dict(user_id=1, office_id=1, vote=1)),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get_results(self):
        """ Tests if the returned data in get results works as expected """

        response = self.client.get('/api/v2/office/1/result')
        self.assertEqual(response.status_code, 200)
