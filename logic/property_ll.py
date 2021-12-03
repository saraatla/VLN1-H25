from data_layer.DLAPI import DLAPI
from models.PropertyModel import Property


class PropertyLL:
    def __init__(self):
        self.dlapi = DLAPI()
    
    def get_all_properties(self):
        return self.dlapi.get_all_properties()

    def create_property(self, prop):
        return self.dlapi.create_property(prop)
    
    def edit_property(self, propno, col, newvalue):
        return self.dlapi.edit_property(propno, col, newvalue)

    def search_property(self, search):
        reader = self.dlapi.get_all_properties()
        for row in reader:
            if search == row.property_id:
                return row
        return False

