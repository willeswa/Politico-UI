""" Defines political office models """

# Local imports
from app.api.v2.dbconfig import Database


class OfficeModel:
    """ Handles operations related to politicsl offices """

    def __init__(self, office_name, office_type):
        """ Defines instance variables """

        self.office_name = office_name
        self.office_type = office_type

    def create_office(self):
        """ Saves an instance of a new office in the database """

        query = """ INSERT INTO offices (office_name, office_type) VALUES (%s, %s); """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (self.office_name, self.office_type,),)
            conn.commit()

        return "Successfully created the '{}'".format(self.office_name)

    @classmethod
    def office_already_created(cls, office_name, office_type):
        """ Checks if an office at of the given type and name is already registered """

        query = """ SELECT EXISTS (SELECT * FROM offices WHERE office_name = %s and office_type = %s ) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (office_name, office_type,),)
            record = curr.fetchone()
        return record[0]

    @classmethod
    def office_exists(cls, office_id):
        """ Checks if an office exists """

        query = """ SELECT EXISTS (SELECT * FROM offices WHERE office_id = %s) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (office_id,),)
            record = curr.fetchone()
        return record[0]

    @classmethod
    def retrieve_all_offices(cls):
        """ Retrieves all offices from the database """

        query = """ SELECT * FROM offices """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query)
            records = curr.fetchall()
        offices = []
        if records:
            column = ('office_id', 'office_type', 'office_name', 'created_on')
            for record in records:
                office = dict(zip(column, record))
                offices.append(office)

        return offices

    @classmethod
    def get_specific_office(cls, office_id):
        """ returns a specific office given office id """

        query = """ SELECT * FROM offices WHERE office_id = %s """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (office_id,),)
            record = curr.fetchone()
            column = ('office_id', 'office_type', 'office_name', 'created_on')
            office = dict(zip(column, record))

        return office

    @classmethod
    def delete_office(cls, office_id):
        """ Deletes a office from the offices table """

        query = """ DELETE FROM offices WHERE office_id = %s """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (office_id,),)
            conn.commit()
        return 'Successfully deleted office {}'.format(office_id)

    
