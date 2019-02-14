""" This module sets up the user views """

# Third office imports
from flask import request
from flask.views import MethodView

# Local imports
from app.api.v2.models.user_models import UserModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import Validators


class SignupViews(MethodView):
    """ Defines views for user signup """

    @classmethod
    def post(cls):
        """ Sends a post request to the office models """

        raw_user = request.get_json()
        try:
            user = Validators.checks_for_keys('user', raw_user)
            print(type(user))
            user_models = UserModel(user['firstname'], user['lastname'], user['email'], user['password'], user['phone_number'],
                                    user['passport_url'], user['othername'])
            response = user_models.create_user()
            return Serializer.serialize(response, 201)
        except Exception as error:
            print(error)
            return Serializer.serialize(error.args[0], 400, 400)
