# Third party imports
from flask import Flask


def create_app(config_name):
    """ Application factory """

    app = Flask(__name__)

    return app
