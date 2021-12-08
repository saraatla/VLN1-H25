import csv
from models.contractor_model import Contractor

class ContractorDL:
    """Contractor data layer class; Contains 4 functions: lists, 
    makes new and changes information about a contractor"""
    def __init__(self):
        self.filepath = "csv/Contractors.csv"

    def list_contractors(self):
        """This function reads the csv file and makes a list with 
        all the contractors along with their information
        Returns:
            list: list of contractor info."""
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:                
                cont = Contractor([row["Contractor_ID"], row["Name"], row["Type"], row["Contact"], row["Contacts_phone"], # Make an instance of Contractor
                row["Address"], row["Open_hours"], row["Review"]])
                return_list.append(cont)
        return return_list

    def create_contractor(self, contractor):
        """This function appends a new contractor to the csv file.
        Args:
            contractor (class): model class attributes"""
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Contractor_ID","Name", "Type", "Contact", "Contacts_phone", "Address", "Open_hours", "Review"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Contractor_ID': contractor.id,'Name': contractor.name, 'Type': contractor.type, 'Contact': contractor.contact, 'Contacts_phone': contractor.contacts_phone, 
            'Address':contractor.address, 'Open_hours':contractor.open_hours, 'Review':contractor.review}) 

    def edit_contractor(self, contractor):
        """This function edits a certain value in the csv file for a certain contractor (input by Managers).
        Args:
            contractor (class): model class attributes"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader) 
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile) # converts the value into delimited string on the csvfile
            for row in data_list:
                if contractor.id == row[0]:
                    writer.writerow([contractor.id, 
                                     contractor.name, 
                                     contractor.type, 
                                     contractor.contact, 
                                     contractor.contacts_phone, 
                                     contractor.address, 
                                     contractor.open_hours, 
                                     contractor.review])
                else:
                    writer.writerow(row)
    

            
