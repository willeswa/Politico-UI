""" This module defines classes for  handling votes views """

# Third party imports
from flask.views import MethodView
from flask import request

# Local imports
from app.api.utils.validators import Validators
from app.api.utils.serializer import Serializer
from app.api.v2.models.vote_model import VoteModel
from app.api.v2.models.user_models import PolitcianModel
from flask_jwt_extended import jwt_required, get_jwt_identity


class VoteViews(MethodView):
    """ This class defines methods handlind vote related request """

    @jwt_required
    def post(self):
        """ Sends a post request for creating a vote """

        current_user = get_jwt_identity()
        raw_vote = request.get_json()
        try:
            vote = Validators.validate_json('vote', raw_vote)
            candidate_exists = PolitcianModel.candidate_exists(
                vote['candidate_id'])
            if candidate_exists:
                if VoteModel.voted_for(vote['candidate_id']):
                    return Serializer.serialize('You have already voted for this candidate', 409)
                vote_model = VoteModel(
                    vote['office_id'], vote['candidate_id'], current_user['user_id'])
                response = vote_model.cast_vote()
                return Serializer.serialize(response, 201)
            return Serializer.serialize('Politician not found', 404)
        except Exception as error:
            return Serializer.serialize(error.args[0], 400)
