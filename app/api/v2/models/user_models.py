""" This module defines classes for Usres, both normal and politcians """
import pdb

# Third party imports
from psycopg2 import Error

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
                                 self.email, self.password, self.phoneNumber, self.passportUrl))
            conn.commit()

        return 'Successfuly created account'

    @classmethod
    def user_exists(cls, email):
        """ This class method checks if user exists """

        query = """ SELECT * FROM users WHERE email=%s """

        with Database() as conn:
            curr = conn.cursor()
            curr.execute(query, (email))
            record = curr.fetchone()
            print(record)
            if record:
                raise Exception('None')
