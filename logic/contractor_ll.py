from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.contractor_model import Contractor
LINE = '------------------------------------------'

class ContractorLL:
    """Contractor logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,destination):
        self.dlapi = DLAPI(destination)
        self.table = Texttable()

    def list_contractors(self):
        cont_list = []
        for contractor in self.dlapi.list_contractors():
            cont_list.append(contractor)
        return cont_list


    def create_contractor(self, cont):
        return self.dlapi.create_contractor(Contractor(cont))


    def search_contractor(self, cont_id):
        reader = self.dlapi.list_contractors()
        for contractor in reader:
            if contractor.id == cont_id:
                return contractor
        return None
    
    def edit_contractor(self, cont):
        return self.dlapi.edit_contractor(cont)

    def get_new_cont_id(self):
        """Gets the ID of the last contractor in the csv file and
            adds one to get the new contractor id"""
        return 'C' + str(int(self.dlapi.list_contractors()[-1].id[1:])+1)