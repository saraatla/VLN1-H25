class Contractor:
    def __init__(self,parameters):
        self.name = parameters[0]
        self.type = parameters[1]
        self.contact = parameters[2]
        self.contacts_phone = parameters[3]
        self.address = parameters[4]
        self.open_hours = parameters[5]
        self.review = parameters[6]
        
    def __str__(self):
        return f"Name: {self.name}, Type: {self.type}, Contact: {self.contact}, Contacts_phone: {self.contacts_phone}, Address: {self.address}, Open_hours: {self.open_hours}, Review: {self.review}"