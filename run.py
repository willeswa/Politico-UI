""" This module provides an entry point for the application """

# standard imports
import os

# local imports
from app import create_app


APP = create_app(os.getenv('FLASK_ENV'))

if __name__ == "__main__":
    APP.run()
