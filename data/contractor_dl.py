import csv
from models.contractor_model import Contractor

class ContractorDL:
    def __init__(self):
        self.filepath = "csv/Contractors.csv"

    def list_contractors(self):
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # Náum í csv skránna
            for row in reader:                
                cont = Contractor([row["Name"], row["Type"], row["Contact"], row["Contacts_phone"], # Búum til instance af Contractor
                row["Address"], row["Open_hours"], row["Review"]])
                return_list.append(cont) # Bætum í listann
        return return_list

    def create_contractor(self, cont):
        with open(self.filepath, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Name", "Type", "Contact", "Contacts_phone", "Address", "Open_hours", "Review"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # Náum í csv skránna
            writer.writerow({'Name': cont.name, 'Type': cont.type, 'Contact': cont.contact, 'Contacts_phone': cont.contacts_phone, 
            'Address':cont.address, 'Open_hours':cont.open_hours, 'Review':cont.review}) 
            pass

    def edit_contractor(self, contno, col, newval):
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) 
            data_list = list(reader) 
            data_list[contno][col] = newval
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_list)
    

            
