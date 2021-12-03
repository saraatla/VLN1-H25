from data.DLAPI import DLAPI

class PropertyLL:
    """Property logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,location):
        self.location = location
        self.dlapi = DLAPI(location)
    
    def list_properties(self):
        return self.dlapi.list_properties()

    def create_property(self, prop):
        return self.dlapi.create_property(prop)
    
    def edit_property(self, propno, col, newvalue):
        return self.dlapi.edit_property(propno, col, newvalue)

    def search_property(self, search):
        reader = self.dlapi.list_properties()
        for row in reader:
            if search == row.property_id:
                return row
        return False

