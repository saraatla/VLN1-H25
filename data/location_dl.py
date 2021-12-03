import csv
from models.destination_model import Destination

class LocationDL:
    """Location data layer class; Contains 2 functions: lists, 
    makes new and changes information about a property"""
    def __init__(self):
        self.filepath = "csv/Destinations.csv"

    def list_locations(self):
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                loc = Destination(row["ID"], row["Destination"], row["Airport"], row["Phone_number"], 
                row["Opening_hours"],row["Manager_ssn"]) # Make an instance of Destination
                return_list.append(loc)
        return return_list
        
