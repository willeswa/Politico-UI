""" This module defines classes for Usres, both normal and politcians """

# Third party imports
from psycopg2 import Error
from flask_jwt_extended import create_access_token

# Local imports
from app.api.v2.dbconfig import Database
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel:
    """ This class defines attributes and methods for normal users """

    def __init__(self, firstname, lastname, email, password, phoneNumber, passportUrl, othername):
        """ Instance variable for users """

        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.password = generate_password_hash(password)
        self.email = email
        self.phoneNumber = phoneNumber
        self.passportUrl = passportUrl

    def create_user(self):
        """ Creates new user in the database """

        with Database() as conn:
            query = """ INSERT INTO users (firstname, lastname, othername, email, password, phone_number, passport_url) VALUES (%s, %s, %s, %s, %s, %s, %s); """
            curr = conn.cursor()
            curr.execute(query, (self.firstname, self.lastname, self.othername,
                                 self.email, self.password, self.phoneNumber, self.passportUrl,))
            conn.commit()

        return 'Successfully created account'

    @classmethod
    def sigin_user(cls, email, password):
        """ Approves user sign in given the email and password are correct """

        with Database() as conn:
            query = """ SELECT  user_id, password, is_admin FROM users where email = %s """
            curr = conn.cursor()
            curr.execute(query, (email,),)
            record = curr.fetchone()

        if check_password_hash(record[1], password):
            token = create_access_token(
                {'user_id': record[0], 'is_admin': record[2]})
            result = [
                {
                    "token": token,
                    "user": {'user_id': record[0], 'is_admin': record[2]}
                }
            ]
            return result
        raise Exception('wrong password')

    @classmethod
    def user_exists(cls, email):
        """ This class method checks if user exists """

        query = """ SELECT EXISTS (SELECT * FROM users WHERE email = %s) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (email,),)
            record = curr.fetchone()
        return record[0]

    @classmethod
    def get_specific_user(cls, user_id):
        """ returns a specific office given office id """

        query = """ SELECT * FROM offices WHERE user_id = %s """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (user_id,),)
            record = curr.fetchone()
            column = ('firstname', 'lastname', 'email', 'password',
                      'phoneNumber', 'passportUrl', 'othername')
            user = dict(zip(column, record))

        return user

    @classmethod
    def user_exists_id(cls, user_id):
        """ Checks if a candidate exists """

        query = """ SELECT EXISTS (SELECT * FROM users WHERE user_id = %s) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (user_id,),)
            record = curr.fetchone()
        return record[0]


class PolitcianModel(UserModel):
    """ Defines a model for politcians """

    def __init__(self, candidate_id, office_id, party_id):
        self.office_id = office_id
        self.party_id = party_id
        self.candidate_id = candidate_id

    def create_politician(self):
        """ Creates a new instance of a politician in the database """

        if UserModel.user_exists_id(self.candidate_id):
            try:
                with Database() as conn:
                    query = """ INSERT INTO politicians (office, party, politician) VALUES (%s, %s, %s) """
                    curr = conn.cursor()
                    curr.execute(
                        query, (self.office_id, self.party_id, self.candidate_id),)
                    conn.commit()
                return 'Successfully registered candidate'
            except Exception as error:
                print(error)

        raise Exception('Political candidates must be registered users')

    @classmethod
    def candidate_exists(cls, candidate_id):
        """ Checks if a candidate exists """

        query = """ SELECT EXISTS (SELECT * FROM politicians WHERE politician = %s ) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (candidate_id,),)
            record = curr.fetchone()
        return record[0]
    
    @classmethod
    def retrieve_all_politicians(cls, office_id):
        """ Retrieves all politicians from the database. """

        query = """ SELECT party, politician FROM politicians WHERE office = %s """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (office_id,),)
            records = curr.fetchall()
        politicians = []
        if records:
            column = ('party_id', 'politician_reg_id')
            for record in records:
                politician = dict(zip(column, record))
                politicians.append(politician)

        return politicians

    @classmethod
    def candidate_being_voted_for_registered(cls, office_id, candidate_id):
        """ checks if a candidated is regstered for that specific seat """

        query = """ SELECT EXISTS (SELECT * FROM politicians WHERE politician = %s AND office = %s ) """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (candidate_id, office_id,),)
            record = curr.fetchone()
        return record[0]