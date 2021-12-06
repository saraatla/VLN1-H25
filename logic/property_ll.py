from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.property_model import Property
LINE = '------------------------------------------'

class PropertyLL:
    """Property logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)
        self.table = Texttable()
    
    def list_properties(self):
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(130)
        prop_list = self.dlapi.list_properties()
        for item in range(len(prop_list)):
            prop = prop_list[item]
            if prop.destination == self.destination:
                self.table.add_rows([["Nr","Destination", "Address","Squarefoot","Rooms","Type","Property_ID","Facilites"], [item+1,prop.destination, prop.address, prop.squarefoot, prop.rooms, prop.type, prop.property_id, prop.facilities]])
            elif self.destination == "All destinations":
                self.table.add_rows([["Nr","Destination", "Address","Squarefoot","Rooms","Type","Property_ID","Facilites"], [item+1,prop.destination, prop.address, prop.squarefoot, prop.rooms, prop.type, prop.property_id, prop.facilities]])
        print(self.table.draw())
        while True:
            print(LINE)
            command = input("Enter B to go back:").upper()
            if command == "B":
                return
            else:
                print("Invalid input, try again!")

    def create_property(self):
        print('Enter the following information: ')
        print(LINE)
        prop = []
        fieldnames = ['Destination', 'Address', 'Squarefoot', 'Rooms', 'Type', 'Property_ID', 'Facilities']
        for field in fieldnames:
            val = input(f'{field}: ')
            prop.append(val)
        self.dlapi.create_property(Property(prop))
        print(f'{LINE}\nProperty successfully created!\n{LINE}')
 
    


    def edit_property(self, prop):
        while True:
            fieldnames = ['Destination', 'Address', 'Squarefoot', 'Rooms', 'Type', 'Property_ID', 'Facilities']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
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
                if self.destination == "All destinations":
                    if search == row.property_id:
                        return row
                elif row.destination == self.destination:
                    if search == row.property_id:
                        return row
                else:
                    print(f'{LINE}\nProperty not found\n{LINE}')
                    return
 

