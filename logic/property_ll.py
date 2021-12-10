from data.DLAPI import DLAPI
from models.property_model import Property

class PropertyLL:
    """Property logic layer class; Contains 5 functions: fetches the functions in the data layer API,
    lists properties according to destination chosen by user, finds information about a property chosen by user in destination
    Args:
        destination (str): destination chosen by user"""

    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)


    def list_properties(self, destination):
        """This function lists poroperties according to destination.
        Args:
            destination (str) : destination chosen by user
        Returns:
            property_list (list): list of properties in given destination"""
        property_list = []
        for property in self.dlapi.list_properties():
            if destination == 'All destinations' or destination == property.destination:
                property_list.append(property)
        return property_list


    def create_property(self, property):
        """Creates new property"""
        self.dlapi.create_property(Property(property))
        

    def _search_property(self, prop_id, destination):
        """This function searches for a property in destination by it's id in list of all properties,
        returns it's information.
        Args:
            prop_id (str): property id input by user
            destination (str) : destination chosen by user
        Returns: 
            property (class instance): property model class, or
            None"""
        reader = self.dlapi.list_properties()
        for property in reader:
            if property.property_id == prop_id:
                if destination == 'All destinations' or destination == property.destination:
                    return property
        return None
           
    def edit_property(self, property):
        """Edits property info"""
        return self.dlapi.edit_property(property)