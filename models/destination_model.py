class Destination:
    def __init__(self,destination,phone,open_hours,manager):
        self.destination = destination
        self.phone = phone
        self.open_hours = open_hours 
        self.manager = manager

    def __str__(self):
        return f"""Destination: {self.destination} 
Phone: {self.phone} 
Open Hours: {self.open_hours}
Manager: {self.manager}"""
        