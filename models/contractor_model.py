class Contractor:
    def __init__(self,parameters):
        self.id = parameters[0]
        self.name = parameters[1]
        self.type = parameters[2]
        self.contact = parameters[3]
        self.contacts_phone = parameters[4]
        self.address = parameters[5]
        self.open_hours = parameters[6]
        self.review = parameters[7]
        
    def __str__(self):
        return f"""ID: {self.id}
Name: {self.name}
Type: {self.type} 
Contact: {self.contact} 
Contacts_phone: {self.contacts_phone} 
Address: {self.address} 
Open_hours: {self.open_hours} 
Review: {self.review}"""