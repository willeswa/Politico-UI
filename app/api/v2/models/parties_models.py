""" This module defines party models for version 2 """

# Local imports
from app.api.v2.dbconfig import Database


class PartyModel:
    """ This class defines methods that handles party requests """

    def __init__(self, party_name, hq_address, logo_url):
        """ Initializes instance variables """

        self.party_name = party_name
        self.hq_address = hq_address
        self.logo_url = logo_url

    def create_party(self):
        """ Saves an new instance of a party in the database """

        query = """ INSERT INTO parties (party_name, hq_address, logo_url) VALUES (%s, %s, %s); """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(
                query, (self.party_name, self.hq_address, self.logo_url,))
            conn.commit()

        return 'Successfully created party'

    @classmethod
    def party_name_taken(cls, party_name):
        """ Checks if the name is taken """

        query = """ SELECT EXISTS (SELECT * FROM parties WHERE party_name = %s) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (party_name,),)
            record = curr.fetchone()
        return record[0]

    @classmethod
    def party_exists(cls, party_id):
        """ Checks if the name is taken """

        query = """ SELECT EXISTS (SELECT * FROM parties WHERE party_id = %s) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (party_id,),)
            record = curr.fetchone()
        return record[0]

    @classmethod
    def retrieve_all_parties(cls):
        """ Retrieves all parties from the database. """

        query = """ SELECT * FROM parties """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query)
            records = curr.fetchall()
        parties = []
        if records:
            column = ('party_id', 'party_name', 'hq_address', 'logo_url', 'created_on')
            for record in records:
                party = dict(zip(column, record))
                parties.append(party)

        return parties

    @classmethod
    def get_specific_party(cls, party_id):
        """ Gets a specific party from the databse """

        query = """ SELECT * FROM parties WHERE party_id = %s """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (party_id,),)
            record = curr.fetchone()
            column = ('party_id', 'party_name', 'hq_address', 'logo_url', 'created_on')
            party = dict(zip(column, record))

        return party

    @classmethod
    def update_party(cls, party_id, new_name):
        """ Updates the name of a party """

        query = """ UPDATE parties SET  party_name = %s WHERE party_id = %s """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (new_name, party_id,),)
            conn.commit()

        return 'Successfully updated the name of the party'

    @classmethod
    def delete_party(cls, party_id):
        """ Deletes a party from the parties table """

        query = """ DELETE FROM parties WHERE party_id = %s """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (party_id,),)
            conn.commit()
        return 'Successfully deleted party {}'.format(party_id)
