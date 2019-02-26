""" Configures the database and manages database connection """

# standard imports
import os

# Third party imports
import psycopg2
from werkzeug.security import generate_password_hash


# Local imports
from app.config import APP_CONFIG

CONFIG_NAME = os.getenv('FLASK_ENV')
if CONFIG_NAME is not None:
    URL = APP_CONFIG[CONFIG_NAME].DATABASE_URL
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
                user_id SERIAL PRIMARY KEY,
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
                party_id SERIAL PRIMARY KEY,
                party_name VARCHAR NOT NULL,
                hq_address VARCHAR NOT NULL,
                logo_url TEXT NOT NULL,
                created_on DATE DEFAULT CURRENT_TIMESTAMP
            ); """,
                   """ CREATE TABLE IF NOT EXISTS offices (
                office_id SERIAL PRIMARY KEY,
                office_type VARCHAR NOT NULL,
                office_name VARCHAR NOT NULL,
                created_on DATE DEFAULT CURRENT_TIMESTAMP
            ); """,
                   """ CREATE TABLE IF NOT EXISTS politicians (
                politician_id SERIAL NOT NULL,
                office integer NOT NULL REFERENCES offices (office_id) ON DELETE CASCADE,
                party integer NOT NULL REFERENCES parties (party_id) ON DELETE CASCADE,
                politician integer NOT NULL REFERENCES users (user_id) ON DELETE CASCADE,
                PRIMARY KEY (politician, office)
            ); """,
                   """ CREATE TABLE IF NOT EXISTS votes (
                vote_id SERIAL NOT NULL,
                office integer NOT NULL REFERENCES offices (office_id) ON DELETE CASCADE,
                created_by integer NOT NULL REFERENCES users (user_id) ON DELETE CASCADE,
                candidate integer NOT NULL REFERENCES  users (user_id) ON DELETE CASCADE,
                created_on DATE DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (created_by, office)

            );""",)
        try:
            with Database() as conn:
                curr = conn.cursor()
                for query in queries:
                    curr.execute(query)
                conn.commit()

            return 'Successfuly created tables'
        except Exception as e:
            return e

    @classmethod
    def create_admin(cls):
        """ Creates an admin the system """
        adminpass = generate_password_hash(os.getenv('ADMIN_PASS'))
        admin_email = os.getenv('ADMIN_EMAIL')
        admin = os.getenv('ADMIN')

        query = """ INSERT INTO users (firstname, lastname, othername, email, password, phone_number, passport_url, is_admin) VALUES ({}); """.format(
            admin)

        try:
            with Database() as conn:
                curr = conn.cursor()
                exists = """ SELECT * FROM users WHERE email = %s """
                curr.execute(exists, (admin_email,),)
                record = curr.fetchone()
                if record is None:
                    curr.execute(query, (admin_email, adminpass),)
                    conn.commit()
                    return 'Admin created'
        except Exception as e:
            print(e)

    @classmethod
    def drop_tables(cls):
        """ Deletes all the tables from the database """

        queries = (""" DROP TABLE IF EXISTS users CASCADE; """,
                   """ DROP TABLE IF EXISTS parties CASCADE; """,
                   """ DROP TABLE IF EXISTS offices CASCADE; """,
                   """ DROP TABLE IF EXISTS politicians CASCADE; """,
                   """ DROP TABLE IF EXISTS votes; """)
        with Database() as conn:
            curr = conn.cursor()

            for query in queries:
                curr.execute(query)
                conn.commit()
