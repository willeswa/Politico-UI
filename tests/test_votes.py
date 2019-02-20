""" This module contains tests for votes """

import json


from tests import TestBaseClass


class TestVoteCases(TestBaseClass):
    """ This module contains tests that tests votes operation """

    def test_cast_vote(self):
        """ Tests if creating politician works as expected """

        response = self.client.post('/api/v2/votes',
                                    data=json.dumps(self.vote_data),
                                    content_type='application/json',
                                    headers=self.super_headers)
        self.assertEqual(response.status_code, 201)

    def test_not_registered_voter(self):
        """ Tests if creating politician works as expected """

        response = self.client.post('/api/v2/votes',
                                    data=json.dumps(self.vote_data))
        self.assertEqual(response.status_code, 401)

    def test_invalid_vote(self):
        """ Tests an invalid vote """
        response = self.client.post('/api/v2/votes',
                                    data=json.dumps(dict(vote='1')),
                                    content_type='application/json',
                                    headers=self.super_headers)
        self.assertEqual(response.status_code, 400)

    def test_vote_twice(self):
        self.client.post('/api/v2/votes',
                         data=json.dumps(self.vote_data),
                         content_type='application/json',
                         headers=self.super_headers)

        response = self.client.post('/api/v2/votes',
                                    data=json.dumps(self.vote_data),
                                    content_type='application/json',
                                    headers=self.super_headers)
        self.assertEqual(response.status_code, 409)

    def test_get_results(self):
        """ Tests if the returned data in get results works as expected """

        response = self.client.get('/api/v2/office/1/result')
        self.assertEqual(response.status_code, 200)
