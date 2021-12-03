class Destination:
    def __init__(self,id,destination,airport,phone,open_hours,manager):
        self.id = id
        self.destination = destination
        self.airport = airport
        self.phone = phone
        self.open_hours = open_hours 
        self.manager = manager

    def __str__(self):
        return f"""ID: {self.id} 
Destination: {self.destination}
Airport: {self.airport} 
Phone: {self.phone} 
Open Hours: {self.open_hours}
Manager: {self.manager}"""
        