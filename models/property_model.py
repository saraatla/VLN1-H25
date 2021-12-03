class Property:
    def __init__(self,destination_id,address,squarefoot,rooms,type,property_id,facilites): #self, parameters og parameter[0] og upp í self hér fyrir neðan
        self.destination_id = destination_id
        self.address = address
        self.squarefoot = squarefoot
        self.rooms = rooms
        self.type = type
        self.property_id = property_id
        self.facilities = facilites

    def __str__(self):
        return f"""Destination_ID: {self.destination_id} 
Address: {self.address} 
Squarefoot: {self.squarefoot} 
Rooms: {self.rooms}
Type: {self.type} 
Property_ID: {self.property_id} 
Facilities: {self.facilities}""" 
