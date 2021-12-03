from data.DLAPI import DLAPI

class ContractorLL:
    def __init__(self):
        self.dlapi = DLAPI()

    def get_all_contractors(self):
        return self.dlapi.get_all_contractors()

    def create_contractor(self, cont):
        return self.dlapi.create_contractor(cont)

    def edit_contractor(self, contno, col, newvalue):
        return self.dlapi.edit_contractor(contno, col, newvalue)

    def search_contractor(self, search):
        reader = self.dlapi.get_all_contractors()
        for row in reader:
            if search == row.name:
                return row
        return False
