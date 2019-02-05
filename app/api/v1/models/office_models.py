""" Defines political office models """

# Standard imports
import datetime


DB = [
    {
        "created_on": "Sunday, 03. February 2019 06:52PM",
        "office_name": "President of the Republic of Kenya",
        "office_id": 1,
        "office_type": "Valid Office Type"
    }
]


class OfficeModel:
    """ Handles operations related to politicsl offices """

    def __init__(self, office_name, office_type):
        """ Defines instance variables """

        self.office_name = office_name
        self.office_type = office_type
        self.office_id = len(DB) + 1
        self.created_on = datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
        

    def create_office(self):
        """ creates a political office """

        try:
            office = {}
            office['office_name'] = self.office_name
            office['office_type'] = self.office_type
            office['office_id'] = self.office_id
            office['created_on'] = self.created_on

            DB.append(office)
            
            return 'Successfuly created an office'

        except Exception as error:
            raise Exception(error)

    @classmethod
    def retrieve_all_offices(cls):
        """ Retrieves all offices from the database """
        return DB

    @classmethod
    def get_specific_office(cls, office_id):
        """ returns a specific office given office id """

        if OfficeModel.office_exists(office_id):
            response = OfficeModel.office_exists(office_id)
            return response
        return 'Office not found'

    @classmethod
    def office_exists(cls, office_id):
        """ Checks if a specific office exists """

        for office in DB:
            if office['office_id'] == office_id:
                return office
        return None
