""" This module provides an entry point for the application """

# standard imports
import os

# local imports
from app.api.utils.serializer import Serializer
from app import create_app


app = create_app(os.getenv('FLASK_ENV'))

if __name__ == "__main__":
    app.run()


@app.route('/')
def home():
    return Serializer.serialize({
        "message": "Welcome to Politiko",
        "author": "Willies Wanjala",
        "email": "gwiliez@gmail.com",
        "url-prefix": "api/v2 or api/v1"
    }, 200)