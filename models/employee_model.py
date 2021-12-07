class Employee:
    def __init__(self,parameters):
        self.name = parameters[0]
        self.ssn = parameters[1]
        self.email = parameters[2]
        self.address = parameters[3]
        self.phone = parameters[4]
        self.gsm = parameters[5]
        self.destination = parameters[6]
        self.title = parameters[7]
        
        
    def __str__(self):
        return f"""Name: {self.name} 
SSN: {self.ssn} 
Email: {self.email} 
Address: {self.address} 
Phone: {self.phone}
GSM: {self.gsm}
Destination: {self.destination} 
Title: {self.title}"""