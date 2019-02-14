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
            user = Validators.validate_json('user', raw_user)
            if UserModel.user_exists(user['email']):
                return Serializer.serialize('Email: {} is already registered. Login instead! '.format(user['email']), 409)
            user_models = UserModel(user['firstname'], user['lastname'], user['email'], user['password'], user['phone_number'],
                                    user['passport_url'], user['othername'])
            response = user_models.create_user()
            return Serializer.serialize(response, 201)
        except Exception as error:
            print(error)
            return Serializer.serialize(error.args[0], 400, 400)


class LoginViews(MethodView):
    """ Defines views for login """

    def post(self):
        """ Passes login data to models """

        login_data = request.get_json()
        try:
            current_user = Validators.validate_json('user', login_data)

            if UserModel.user_exists(current_user['email']):
                response = UserModel.sigin_user(
                    current_user['email'], current_user['password'])

                return Serializer.serialize(response, 200)

            return Serializer.serialize('Email: {} is not registered'.format(current_user['email']), 404)
        except Exception as error:
            return Serializer.serialize(error.args[0], 400, 400)
