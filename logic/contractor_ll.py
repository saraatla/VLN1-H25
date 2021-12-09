from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.contractor_model import Contractor
LINE = '------------------------------------------'

class ContractorLL:
    """Contractor logic layer class; Contains 6 functions: fetches the functions in the data layer API, 
    search for a contractor by id and finds the last contractor id in csv file"""
    def __init__(self,destination):
        self.dlapi = DLAPI(destination)
        self.table = Texttable()


    def list_contractors(self):
        return self.dlapi.list_contractors()
        #cont_list = []
        #for contractor in self.dlapi.list_contractors():
            #cont_list.append(contractor)
        #return cont_list


    def create_contractor(self, contractor): 
        """Creates new contractor"""
        self.dlapi.create_contractor(Contractor(contractor))


    def search_contractor(self, cont_id):
        """This function searches for a contractor by his id in list of all contractors.
        Args:
            cont_id (str): contractor id input by user
        Returns: 
            contractor (class instance): contractor model class"""
        reader = self.dlapi.list_contractors()
        for contractor in reader:
            if contractor.id == cont_id:
                return contractor
        return None
    

    def edit_contractor(self, contractor):
        """Edits contractor info"""
        return self.dlapi.edit_contractor(contractor)


    def get_new_cont_id(self):
        """Gets the ID of the last contractor in the csv file and
        adds one to get the new contractor id.
        Returns:
            the next contractor id (str)"""
        return 'C' + str(int(self.dlapi.list_contractors()[-1].id[1:])+1)