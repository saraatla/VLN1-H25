import csv
from models.destination_model import Destination

class DestinationDL:
    """Destination data layer class; Contains 2 functions: lists, 
    makes new and changes information about a property"""
    def __init__(self):
        self.filepath = "csv/Destinations.csv"


    def _list_destinations(self):
        """This function reads the csv file and makes a list with 
        all the destinations along with their information.
        Returns:
            return_list: list of destination info."""
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                dest = Destination([row["Destination"], row["Phone_number"], 
                row["Opening_hours"],row["Manager_SSN"]]) # Make an instance of Destination
                return_list.append(dest)
        return return_list

    def _create_destination(self,destination):
        """This function appends a new employee to the csv file
        Args:
            employee (class instance): employee model class"""
        with open(self.filepath,'a', newline='') as csvfile:
            fieldnames = ['Destination', 'Phone_number', 'Opening_hours', 'Manager_SSN']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Destination': destination.destination, 'Phone_number': destination.phone, 'Opening_hours': destination.open_hours, 'Manager_SSN': destination.manager})
    

        
