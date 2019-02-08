""" Powers up the application
Creates the application and loads configurations
 """

# Third party imports
import os
from flask import Flask
from dotenv import load_dotenv

# Local imports
from app.config import APP_CONFIG


def create_app(config_name='development'):
    """ Application factory """

    app = Flask(__name__)

    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')

    # Register blueprints and errors
    from app.api.v1 import V1
    from app.api.utils.validators import Validator

    app.register_blueprint(V1)
    app.register_error_handler(404, Validator.wrong_url)
    app.register_error_handler(500, Validator.internal_server_error)
    app.register_error_handler(405, Validator.method_not_allowed)
    app.register_error_handler(400, Validator.bad_request)

    app_root = os.path.join(os.path.dirname(__file__), '..')
    dotenv_path = os.path.join(app_root, '.env')
    load_dotenv(dotenv_path)

    return app
