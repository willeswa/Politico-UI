""" Defines political office models """


class OfficeModel:
    """ Handles operations related to politicsl offices """
    office_db = []

    def __init__(self, office_type, name):
        """ Defines instance variables """

        self.office_type = office_type
        self.name = name

    def create_office(self):
        """ creates a political office """

        office = {}
        office['name'] = self.name
        office['office_type'] = self.office_type
        self.office_db.append(office)
        return 'Successfuly created office'
