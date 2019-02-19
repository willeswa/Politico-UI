""" This module sets up the user views """

# Third office imports
from flask import request
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity

# Local imports
from app.api.v2.models.user_models import UserModel, PolitcianModel
from app.api.v2.models.parties_models import PartyModel
from app.api.v2.models.office_models import OfficeModel
from app.api.utils.serializer import Serializer
from app.api.utils.validators import Validators


class SignupViews(MethodView):
    """ Defines views for user signup """

    @classmethod
    def post(cls):
        """ Sends a post request to the office models """

        raw_user = request.get_json()
        try:
            user = Validators.validate_json('user_signup', raw_user)
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
            current_user = Validators.validate_json('user_login', login_data)

            if UserModel.user_exists(current_user['email']):
                response = UserModel.sigin_user(
                    current_user['email'], current_user['password'])

                return Serializer.serialize(response, 200)

            return Serializer.serialize('Email: {} is not registered'.format(current_user['email']), 404)
        except Exception as error:
            return Serializer.serialize(error.args[0], 400, 400)


class CandidateViews(MethodView):
    """ Handles views related to candidate """

    @jwt_required
    def post(self, office_id):
        """ Passes data to the views to create a new candidate """

        current_user = get_jwt_identity()

        if current_user['is_admin']:

            candidate = request.get_json()
            try:
                candidate_data = Validators.validate_json('candidate', candidate)
                if PolitcianModel.candidate_exists(candidate_data['candidate_id'], office_id):
                    return Serializer.serialize('Politician already registered', 409)

                
                if OfficeModel.office_exists(office_id):
                    if PartyModel.party_exists(candidate_data['party_id']):
                        politician = PolitcianModel(
                            candidate_data['candidate_id'], office_id, candidate_data['party_id'])
                        return Serializer.serialize(politician.create_politician(), 201)

                    return Serializer.serialize('Party does not exists', 404)
                return Serializer.serialize('Non-existant office', 404)

            except Exception as error:
                return Serializer.serialize(error.args[0], 400)

        return Serializer.serialize('You are not authorized to perfom this action', 401)
