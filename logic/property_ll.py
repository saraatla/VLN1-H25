from data.DLAPI import DLAPI
LINE = '------------------------------------------'

class PropertyLL:
    """Property logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,location):
        self.location = location
        self.dlapi = DLAPI(self.location)
    
    def list_properties(self):
        return self.dlapi.list_properties()

    def create_property(self, prop):
        return self.dlapi.create_property(prop)
    
    def edit_property(self, prop, col, newval):
        while True:
            prop = input('Which property would you like to change?: ')
            fieldnames = ['Destination_ID', 'Address', 'Squarefoot', 'Rooms', 'Type', 'Property_ID', 'Facilities']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What would you want to change? ')
            try:
                prop = int(prop)
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                return self.dlapi.edit_property(prop, col, newval)
            except:
                print('Invalid input, try again!')
        

    def search_property(self, search):
        while True:
            if search == '':
                search = input('Enter Property ID: ')        
            reader = self.dlapi.list_properties()
            for row in reader:
                print(row.property_id)
                if search == row.property_id:
                    print('nice')
                    print(row.property_id)
                    return row
                # if self.location == "All Locations":
                #     if search == row.property_id:
                #         return row
                # elif row.location == self.location:
                #     if search == row.property_id:
                #         return row
                else:
                    print(LINE)
                    print('Property not found')
                    print(LINE)
                    return
 

