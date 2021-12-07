import csv
from models.contractor_model import Contractor

class ContractorDL:
    """Contractor data layer class; Contains 4 functions: lists, 
    makes new and changes information about a contractor"""
    def __init__(self):
        self.filepath = "csv/Contractors.csv"

    def list_contractors(self):
        """This function reads the csv file and makes a list with 
        all the contractors along with their information"""
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:                
                cont = Contractor([row["Contractor_ID"], row["Name"], row["Type"], row["Contact"], row["Contacts_phone"], # Make an instance of Contractor
                row["Address"], row["Open_hours"], row["Review"]])
                return_list.append(cont)
        return return_list

    def create_contractor(self, cont):
        "This function appends a new contractor to the csv file"
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Contractor_ID","Name", "Type", "Contact", "Contacts_phone", "Address", "Open_hours", "Review"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Contractor_ID': cont.id,'Name': cont.name, 'Type': cont.type, 'Contact': cont.contact, 'Contacts_phone': cont.contacts_phone, 
            'Address':cont.address, 'Open_hours':cont.open_hours, 'Review':cont.review}) 

    def edit_contractor(self, cont, col, newvalue):
        """This function edits a certain value for a certain contractor (input by Managers)"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader) 
            for index, contractor_value in enumerate(data_list):
                for value in contractor_value:
                    if value == cont:
                        data_list[index][col] = newvalue
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile) # converts the value into delimited string on the csvfile
            writer.writerows(data_list)
    

            
