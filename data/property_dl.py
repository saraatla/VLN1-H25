import csv
from models.property_model import Property

class PropertyDL:
    """Property data layer class; Contains 4 functions: lists, 
    makes new and changes information about a property"""
    def __init__(self, destination):
        self.filepath = "csv/Properties.csv"
        self.destination = destination
    
    def list_properties(self):
        """This function reads the csv file and makes a list with 
        all the properties along with their information"""
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                prop = Property([row["Destination"], row["Address"], row["Squarefoot"], 
                row["Rooms"], row["Type"], row["Property_ID"], row["Facilities"]]) # Make an instance of Property
                return_list.append(prop)
        return return_list

    def create_property(self, prop):
        "This function appends a new property to the csv file"
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Destination", "Address", "Squarefoot", "Rooms", "Type", "Property_ID", "Facilities"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Destination': prop.destination, "Address": prop.address, "Squarefoot": prop.squarefoot, 
            "Rooms": prop.rooms, "Type": prop.type, "Property_ID": prop.property_id, "Facilities": prop.facilities})

    def edit_property(self, id, col, newvalue):  
        """This function edits a certain value for a certain property (input by supervisor)"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader)
            for i, prop_value in enumerate(data_list):
                for value in prop_value: 
                    if value == id: 
                        data_list[i][col] = newvalue 
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)  # converts the value into delimited string on the csvfile
            writer.writerows(data_list)