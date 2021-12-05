import csv
from models.destination_model import Destination

class DestinationDL:
    """destination data layer class; Contains 2 functions: lists, 
    makes new and changes information about a property"""
    def __init__(self):
        self.filepath = "csv/Destinations.csv"


    def list_destinations(self):
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                dest = Destination(row["Destination"], row["Airport"], row["Phone_number"], 
                row["Opening_hours"],row["Manager_ssn"]) # Make an instance of Destination
                return_list.append(dest)
        return return_list
    
    def get_destination(self, id):
        dest_list = self.list_destinations()
        return dest_list[id]
        