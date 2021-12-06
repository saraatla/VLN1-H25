class Employee:
    def __init__(self,parameters, ID):
        self.name = parameters[0]
        self.ssn = ID
        self.email = parameters[1]
        self.address = parameters[2]
        self.phone = parameters[3]
        self.gsm = parameters[4]
        self.destination = parameters[5]
        self.airport = parameters[6]
        self.title = parameters[7]
        
        
    def __str__(self):
        return f"""Name: {self.name} 
SSN: {self.ssn} 
Email: {self.email} 
Address: {self.address} 
Phone: {self.phone}
GSM: {self.gsm}
destination: {self.destination} 
Airport: {self.airport} 
Title: {self.title}"""