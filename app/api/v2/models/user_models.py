""" This module defines classes for Usres, both normal and politcians """

# Local imports
from app.api.v2.dbconfig import DB


class UserModel:
    """ This class defines attributes and methods for normal users """

    def __init__(self, othername='', *args):
        """ Instance variable for users """

        self.othername = othername
        self.args = args

    def create_user(self):
        """ Creates new user in the database """
        try:
            query = """ INSERT INTO users (firstname, lastname, othername, email, phonenumber, passporturl, nationalid) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s ) """

            with DB as conn:
                curr = conn.cursor()
                curr.execute(query, (self.othername, *self.args))
                conn.commit()
                curr.close()

            return 'Successfuly created account'
        except Exception as error:
            return error

    def user_exists(self, email):
        """ This class method checks if user exists """

        query = """ SELECT email FROM users WHERE email = %s"""

        with DB as conn:
            curr = conn.cursor()
            curr.execute(query, (email))
            record = curr.fetchone()
        if email in record:
            return True
        else:
            return False
