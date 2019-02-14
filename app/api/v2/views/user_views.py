""" This module sets up the user views """

# Third office imports
from flask import request
from flask.views import MethodView

# Local imports
from app.api.v2.models.user_models import UserModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import Validators


class SignupViews(MethodView):
    """ Defines views for office """

    @classmethod
    def post(cls):
        """ Sends a post request to the office models """

        user = request.get_json()
        try:
            user_models = UserModel(user['firstname'], user['lastname'], user['othername'],
                                    user['email'], user['phoneNumber'], user['passportUrl'], user['nationalId'])
            if user_models.user_exists(user['email']):
                return Serializer.serialize('Email is already registered', 409)
            else:
                response = user_models.create_user()
                return Serializer.serialize(response, 201)
        except Exception as error:
            return Serializer.serialize(error.args[0], 400)
