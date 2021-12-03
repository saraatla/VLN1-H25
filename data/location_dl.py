import csv
from models.destination_model import Destination

class LocationDL:
    def __init__(self):
        self.filepath = "csv/Destinations.csv"

    def list_locations(self):
        ret_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                loc = Destination(row["ID"], row["Destination"], row["Airport"], row["Phone_number"], row["Opening_hours"],row["Manager_ssn"])
                ret_list.append(loc)
        return ret_list
        
