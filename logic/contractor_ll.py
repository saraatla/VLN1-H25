from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.contractor_model import Contractor

class ContractorLL:
    """Contractor logic layer class; Contains 6 functions: fetches the functions in the data layer API, 
    search for a contractor by id and finds the last contractor id in csv file"""
    def __init__(self,destination):
        self.dlapi = DLAPI(destination)
        self.table = Texttable()


    def _list_contractors(self):
        """This function makes a list of contractor info"""
        return self.dlapi._list_contractors()


    def _create_contractor(self, contractor): 
        """Creates new contractor"""
        self.dlapi._create_contractor(Contractor(contractor))


    def _search_contractor(self, cont_id):
        """This function searches for a contractor by his id in list of all contractors.
        Args:
            cont_id (str): contractor id input by user
        Returns: 
            contractor (class instance): contractor model class"""
        reader = self.dlapi._list_contractors()
        for contractor in reader:
            if contractor.id == cont_id:
                return contractor
        return None
    

    def _edit_contractor(self, contractor):
        """Edits contractor info"""
        return self.dlapi._edit_contractor(contractor)


    def _get_new_cont_id(self):
        """Gets the ID of the last contractor in the csv file and
        adds one to get the new contractor id.
        Returns:
            the next contractor id (str)"""
        return 'C' + str(int(self.dlapi._list_contractors()[-1].id[1:])+1)