""" This module defines model methods to handle vote requests """

from app.api.v2.dbconfig import Database
from app.api.v2.models.office_models import OfficeModel


class VoteModel:
    """ Contain methods that handle voting """

    def __init__(self, office_id, candidate_id, user_id):
        self.office_id = office_id
        self.candidate_id = candidate_id
        self.user_id = user_id

    def cast_vote(self):
        """ This method creates a new vote """

        query = """ INSERT INTO votes (office, created_by, candidate) VALUES (%s, %s, %s) RETURNING candidate, created_by """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(
                query, (self.office_id, self.user_id, self.candidate_id,),)
            conn.commit()
            record = curr.fetchone()

        column = ('candidate', 'voter')

        vote = dict(zip(column, record))

        return vote

    @classmethod
    def voted_for(cls, office_id, created_by):
        """ Checks if a users as voted for an office """

        query = """ SELECT EXISTS (SELECT * FROM votes WHERE office = %s and created_by = %s ) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (office_id, created_by,),)
            record = curr.fetchone()

        print(record)
        return record[0]

    @classmethod
    def get_votes_for_office(cls, office_id):
        """ Retrieves all votes for a specific office """

        query = """ 
            SELECT candidate, office_name, 
            COUNT (*) FROM (SELECT concat_ws(' ', firstname, othername, lastname) AS candidate, offices.office_name, votes.created_on, votes.vote_id 
            FROM users  INNER JOIN votes ON users.user_id = votes.candidate 
            INNER JOIN offices ON offices.office_id = votes.office WHERE votes.office = %s) AS results 
            GROUP BY candidate, office_name 
            """
        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (office_id,))
            records = curr.fetchall()
        results = []
        column = ('candidate', 'office', 'results')

        if records:
            for row in records:
                result = dict(zip(column, row))
                results.append(result)

        return sorted(results, key=lambda k:k['candidate'])

    @classmethod
    def get_votes_by_specific_user_id(cls, user_id):
        """ Retrieve votes by a specific user """

        query = """ SELECT candidate, office_name, created_on,
        COUNT (*) FROM (SELECT concat_ws(' ', firstname, othername, lastname) AS candidate, offices.office_name, votes.created_on, votes.vote_id 
        FROM users  INNER JOIN votes ON users.user_id = votes.candidate 
        INNER JOIN offices ON offices.office_id = votes.office WHERE votes.created_by = %s) AS results 
        GROUP BY candidate, office_name, created_on  """
        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query,(user_id,))
            records = curr.fetchall()
        results = []
        column = ('candidate', 'office', 'voted_on', 'results')

        if records:
            for row in records:
                result = dict(zip(column, row))
                results.append(result)

        return results
