""" Configures the database and manages database connection """

# standard imports
import os

# Third party imports
import psycopg2


# Local imports
from app.config import Config

ENV = os.getenv('FLASK_ENV')

if ENV:
    URL = Config.DATABASE_URL
else:
    URL = 'postgresql://postgres:star2030@localhost/test_politico'


class Database:
    """ Returns an instance of the database connection """

    def __init__(self):
        self.conn = psycopg2.connect(URL)

    def __enter__(self):
        """ Instantitiates and returns the db connection """
        return self.conn

    def __exit__(self, exe_typ, exec_value, exec_tb):
        """ Define what the context manager should do before exit """
        self.conn.close()

    @classmethod
    def create_tables(cls):
        """ Creates Tables in the database """

        queries = (""" CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL UNIQUE,
                firstname VARCHAR NOT NULL,
                lastname VARCHAR NOT NULL,
                othername VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                password VARCHAR NOT NULL,
                phone_number VARCHAR(15) NOT NULL,
                passport_url TEXT NOT NULL,
                is_admin BOOLEAN DEFAULT False
            ); """,
                   """
            CREATE TABLE IF NOT EXISTS parties (
                partyId SERIAL UNIQUE,
                partyName VARCHAR NOT NULL,
                hqAddress VARCHAR NOT NULL,
                logoUrl TEXT NOT NULL,
                created_on DATE DEFAULT CURRENT_TIMESTAMP
            ); """,
                   """ CREATE TABLE IF NOT EXISTS offices (
                officeId SERIAL UNIQUE,
                officeType VARCHAR NOT NULL,
                officeName VARCHAR NOT NULL
            ); """,
                   """ CREATE TABLE IF NOT EXISTS politicians (
                politicianId SERIAL UNIQUE,
                office integer REFERENCES offices (officeId) ON DELETE CASCADE,
                party integer REFERENCES parties (partyId) ON DELETE CASCADE,
                candidate integer REFERENCES users (user_id) ON DELETE CASCADE
            ); """,
                   """ CREATE TABLE IF NOT EXISTS votes (
                voteId SERIAL UNIQUE,
                office integer REFERENCES offices (officeId) ON DELETE CASCADE,
                candidate integer REFERENCES politicians (politicianId) ON DELETE CASCADE,
                createdOn DATE DEFAULT CURRENT_TIMESTAMP,
                createdBy integer REFERENCES users (user_id) ON DELETE SET NULL
            );""",)

        with Database() as conn:
            curr = conn.cursor()
            for query in queries:
                curr.execute(query)
            conn.commit()

        return 'Successfuly created tables'

    @classmethod
    def drop_tables(cls):
        """ Deletes all the tables from the database """

        with Database() as conn:
            queries = (""" DROP TABLE IF EXISTS users CASCADE;  """,
                       """  DROP TABLE IF EXISTS parties CASCADE; """,
                       """ DROP TABLE IF EXISTS offices CASCADE; """,
                       """ DROP TABLE IF EXISTS politicians CASCADE; """,
                       """ DROP TABLE IF EXISTS votes; """,)
            with Database() as conn:
                curr = conn.cursor()

                for query in queries:
                    curr.execute(query)
                    conn.commit()


DB = Database()
