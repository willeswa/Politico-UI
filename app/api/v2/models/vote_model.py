""" This module defines model methods to handle vote requests """

from app.api.v2.dbconfig import Database

class VoteModel:
    """ Contain methods that handle voting """

    def __init__(self, office_id, candidate_id, voter):
        self.office_id = office_id
        self.candidate_id = candidate_id
        self.voter = voter

    def cast_vote(self):
        """ This method creates a new vote """

        query = """ INSERT INTO votes (office, created_by, candidate) VALUES (%s, %s, %s) RETURNING office, created_by, candidate """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (self.office_id, self.candidate_id, self.voter,),)
            conn.commit()
            record = curr.fetchone()
        
        column = ('office', 'candidate', 'voter')

        vote = dict(zip(column, record))

        return vote
    
    @classmethod
    def voted_for(cls, candidate_id):
        """ Checks if a candidate has been voted for """

        query = """ SELECT EXISTS (SELECT * FROM votes WHERE candidate = %s) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (candidate_id,),)
            record = curr.fetchone()

        return record[0]