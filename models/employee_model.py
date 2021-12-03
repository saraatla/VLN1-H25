class Employee:
    def __init__(self,name,ssn,email,address,phone,gsm,location,airport,title):
        self.name = name
        self.ssn = ssn
        self.email = email
        self.address = address
        self.phone = phone
        self.gsm = gsm
        self.location = location
        self.airport = airport
        self.title = title
        
        
    def __str__(self):
        return f"""Name: {self.name} 
SSN: {self.ssn} 
Email: {self.email} 
Address: {self.address} 
Phone: {self.phone}
GSM: {self.gsm}
Location: {self.location} 
Airport: {self.airport} 
Title: {self.title}"""