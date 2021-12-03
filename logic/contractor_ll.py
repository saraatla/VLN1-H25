from data.DLAPI import DLAPI

class ContractorLL:
    """Contractor logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,location):
        self.location = location
        self.dlapi = DLAPI(self.location)

    def list_contractors(self):
        return self.dlapi.list_contractors()

    def create_contractor(self, cont):
        return self.dlapi.create_contractor(cont)

    def edit_contractor(self, contno, col, newvalue):
        return self.dlapi.edit_contractor(contno, col, newvalue)

    def search_contractor(self, search):

        reader = self.dlapi.list_contractors()
        for row in reader:
            if search == row.name:
                return row
        return False
