""" This module defines classes for  handling votes views """

# Third party imports
from flask.views import MethodView
from flask import request

# Local imports
from app.api.utils.validators import Validators
from app.api.utils.serializer import Serializer
from app.api.v2.models.vote_model import VoteModel
from app.api.v2.models.office_models import OfficeModel
from app.api.v2.models.user_models import PolitcianModel
from app.api.v2.models.user_models import UserModel
from flask_jwt_extended import jwt_required, get_jwt_identity


class VoteViews(MethodView):
    """ This class defines methods handlind vote related request """

    @classmethod
    @jwt_required
    def post(cls):
        """ Sends a post requests for creating a vote """

        current_user = get_jwt_identity()
        raw_vote = request.get_json()
        try:
            vote = Validators.validate_json('vote', raw_vote)
            candidate_exists = PolitcianModel.candidate_exists(
                vote['candidate_id'])
            if candidate_exists:
                if OfficeModel.office_exists(vote['office_id']):
                    if PolitcianModel.candidate_being_voted_for_registered(vote['office_id'], vote['candidate_id']):
                        if VoteModel.voted_for(vote['office_id'], current_user['user_id']):
                            return Serializer.serialize('You have already voted in this office category', 409)
                        vote_model = VoteModel(
                            vote['office_id'], vote['candidate_id'], current_user['user_id'])
                        response = vote_model.cast_vote()
                        return Serializer.serialize(response, 201)
                    raise Exception('No such person is vying for this seat')
                raise Exception('You can only vote for registered candidates')
            return Serializer.serialize('Politician not found', 404)
        except Exception as error:
            return Serializer.serialize(error.args[0], 400)


class ResultsViews(MethodView):
    """ Contains methods that manipulate vote results """

    @classmethod
    def get(cls, office_id):
        """ Sends get requests to the models to get results """

        if OfficeModel.office_exists(office_id):
            response = VoteModel.get_votes_for_office(office_id)
            return Serializer.serialize(response, 200)
        return Serializer.serialize('Results for office {} are not ready'.format(office_id), 404)


class ResultsView(MethodView):
    """ Handles methos to pass request for user specific results """

    @classmethod
    def get(cls, user_id):
        """ Passes request for user specific results to the models """

        if UserModel.user_exists_id(user_id):
            response = VoteModel.get_votes_by_specific_user_id(user_id)
            return Serializer.serialize(response, 200)
        return Serializer.serialize('User does not exist.', 404)
