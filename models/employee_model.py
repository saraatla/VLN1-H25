class Employee:
    def __init__(self,parameters, ID):
        self.name = parameters[0]
        self.ssn = parameters[1]
        self.email = parameters[2]
        self.address = parameters[3]
        self.phone = parameters[4]
        self.gsm = parameters[5]
        self.destination = parameters[6]
        self.airport = parameters[7]
        self.title = parameters[8]
        
        
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