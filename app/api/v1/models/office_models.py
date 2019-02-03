""" Defines political office models """

# Standard imports
import datetime

# Third party imports
from flask import make_response, jsonify

DB = []


class OfficeModel:
    """ Handles operations related to politicsl offices """

    def __init__(self, office_type, name):
        """ Defines instance variables """

        self.office_type = office_type
        self.name = name
        self.office_id = len(DB) + 1
        self.created_on = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")

    def create_office(self):
        """ creates a political office """

        try:
            office = {}
            office['name'] = self.name
            office['office_type'] = self.office_type
            office['office_id'] = self.office_id
            office['created_on'] = self.created_on

            DB.append(office)
            response = make_response(
                jsonify({'status': 201, 'message': 'Successfuly created office'}), 201)
            return response

        except Exception as error:
            raise Exception({'error': error})

    @classmethod
    def retrieve_all_offices(cls):
        """ Retrieves all offices from the database """
        response = make_response(
            jsonify({'status': 200, 'message': DB}), 200
        )
        return response
