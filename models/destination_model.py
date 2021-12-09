class Destination:
    def __init__(self,parameters):
        self.destination = parameters[0]
        self.phone = parameters[1]
        self.open_hours = parameters[2] 
        self.manager = parameters[3]

    def __str__(self):
        return f"""Destination: {self.destination} 
Phone: {self.phone} 
Open Hours: {self.open_hours}
Manager SSN: {self.manager}"""
        