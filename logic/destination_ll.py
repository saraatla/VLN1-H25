from data.DLAPI import DLAPI
from models.destination_model import Destination

class DestinationLL:
    """Destination logic layer class; Contains 3 functions: fetches the functions in the data layer API,
    makes list of destination names and finds information about a destination chosen by user
    Args:
        destination (str): destination chosen by user"""

    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)


    def _list_of_destinations(self):
        """This function makes a list of the destination names
        Returns:
        dest_name_list (list): [name1,name2,name3,etc]"""
        dest_list = self.dlapi.list_destinations()
        dest_name_list = []
        for value in dest_list: 
            dest_name_list.append(value.destination)
        return dest_name_list
    

    def _search_destination(self, destination):
        """This function searches for a employee by his ssn in list of all employees.
        Args:
            destination (str): destination name chosen by user
        Returns: 
            dest (class instance): destination model class"""
        while True:
            reader = self.dlapi.list_destinations()
            for dest in reader:
                if destination == dest.destination:
                    return dest
    
    def create_destination(self, dest):
        self.dlapi.create_destination(Destination(dest))


