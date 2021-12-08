from data.DLAPI import DLAPI
from models.property_model import Property
LINE = '------------------------------------------'

class PropertyLL:
    """Property logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)

    
    def list_properties(self, destination):
        property_list = []
        for property in self.dlapi.list_properties():
            if destination == 'All destinations' or destination == property.destination:
                property_list.append(property)
        return property_list


    def create_property(self, prop):
        self.dlapi.create_property(Property(prop))


    def edit_property(self, prop):
        return self.dlapi.edit_property(prop)
        

    def search_property(self, prop_id, destination):
        reader = self.dlapi.list_properties()
        for property in reader:
            if property.property_id == prop_id:
                if destination == 'All destinations' or destination == property.destination:
                    return property
        return None
           