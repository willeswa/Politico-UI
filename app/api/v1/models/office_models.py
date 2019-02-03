""" Defines political office models """

# Standard imports
import datetime

# Third party imports
from flask import make_response, jsonify


class OfficeModel:
    """ Handles operations related to politicsl offices """
    office_db = []

    def __init__(self, office_type, name):
        """ Defines instance variables """

        self.office_type = office_type
        self.name = name
        self.office_id = len(self.office_db) + 1
        self.created_on = datetime.datetime.now()

    def create_office(self):
        """ creates a political office """

        try:
            office = {}
            office['name'] = self.name
            office['office_type'] = self.office_type
            self.office_db.append(office)
            response = make_response(
                jsonify({'status': 201, 'message': 'Successfuly created office'}), 201)
            return response

        except Exception as error:
            raise Exception({'error': error})

    def retrieve_all_offices(self):
        """ Retrieves all offices from the database """
        response = make_response(
            jsonify({'status': 200, 'message': self.office_db}), 200
        )

        return response
