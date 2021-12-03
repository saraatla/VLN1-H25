class Property:
    def __init__(self,parameters):
        self.destination_id = parameters[0]
        self.address = parameters[1]
        self.squarefoot = parameters[2]
        self.rooms = parameters[3]
        self.type = parameters[4]
        self.property_id = parameters[5]
        self.facilities = parameters[6]

    def __str__(self):
        return f"""Destination_ID: {self.destination_id} 
Address: {self.address} 
Squarefoot: {self.squarefoot} 
Rooms: {self.rooms}
Type: {self.type} 
Property_ID: {self.property_id} 
Facilities: {self.facilities}""" 
