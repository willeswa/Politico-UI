# Third party imports
import os
from flask import Flask

# Local imports
from app.config import app_config
from dotenv import load_dotenv


def create_app(config_name='development'):
    """ Application factory """

    app = Flask(__name__)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    app_root = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(app_root, '.env')
    load_dotenv(dotenv_path)

    return app
