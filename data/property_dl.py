import csv
from models.property_model import Property

class PropertyDL:
    """Property data layer class; Contains 3 functions: lists, 
    makes new and changes information about a property"""
    def __init__(self):
        self.filepath = "csv/Properties.csv"
    
    def list_properties(self):
        """This function reads the csv file and makes a list with 
        all the properties along with their information"""
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                prop = Property([row["Destination_ID"], row["Address"], row["Squarefoot"], row["Rooms"], row["Type"], row["Property_ID"], row["Facilities"]])
                return_list.append(prop)
        return return_list

    def create_property(self, prop):
        "This function appends a new property to the csv file"
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Destination_ID", "Address", "Squarefoot", "Rooms", "Type", "Property_ID", "Facilities"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Destination_ID': prop.destination_id, "Address": prop.address, "Squarefoot": prop.squarefoot, "Rooms": prop.rooms, "Type": prop.type, "Property_ID": prop.property_id, "Facilities": prop.facilities})
            pass

    # def search_property(self, search):

    #     with open(self.filepath, "r", newline="", encoding='utf-8') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             if search == row[5]:
    #                 return row
    #         return False

    def edit_property(self, propno, col, newvalue):  
        """This function edits a certain value for a certain property (input by supervisor)"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data_list = list(reader)
            # for index, row in enumerate(data_list): #
                #if row[col] == propno: #
                    #print(index)
                    #return index #
            data_list[propno][col] = newvalue #index = propno
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_list)