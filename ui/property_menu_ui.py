from Extra.texttableFile.texttable import Texttable
from Extra.acci import propAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI

LINE = '------------------------------------------'

class PropertyMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
        propAscii()
        while True:
            operations =  ['Search by ID', 'See list']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'Properties in {self.destination}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            if operation  == 'Search by ID':
                search = input('Enter property ID: ')
                found_property = self.llapi.search_property(search, self.destination)
                if found_property is None:
                    print(f'{LINE}\nProperty not found\n{LINE}')
                else:
                    self.individual_property_ui(found_property)

            elif operation == 'See list':
                prop_list = self.list_properties()
                while True:
                    command = input("Enter number of property to open or B to Back:").upper()
                    if command == "B":
                        return
                    if not command.isdigit():
                        print("Invalid input, try again!")
                    else:
                        nr = int(command)
                        for index, property in enumerate(prop_list):
                            if index+1 == nr:
                                self.individual_property_ui(property, nr)
                        break

            elif operation == 'Add new':
                self.create_property()
                print(f'{LINE}\nProperty successfully created!\n{LINE}')


    def create_property(self):
        print('Enter the following information: ')
        print(LINE)
        fieldnames = ['Address', 'Squarefoot', 'Rooms', 'Type', 'Property_ID', 'Facilities']
        if self.destination != 'All destinations':
            prop = [self.destination]
        else:
            prop = []
            fieldnames.insert(0, 'Destination')        
        for field in fieldnames:
            val = input(f'{field}: ')
            prop.append(val)
        return self.llapi.create_property(prop)


    def list_properties(self):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(300)
        prop_list = self.llapi.list_properties(self.destination)
        for item in range(len(prop_list)):
            prop = prop_list[item]
            table.add_rows([["Number","Destination", "Address","Squarefoot","Rooms","Type","Property_ID","Facilites"], 
                            [item+1,prop.destination, prop.address, prop.squarefoot, prop.rooms, prop.type, prop.property_id, prop.facilities]])
        print(table.draw())
        return prop_list


    def individual_property_ui(self, property, nr=None):
        self.print_property_table(property, nr)
        if self.user_type == 'Employee':
            return
        while True:
            print("1: Edit\nB: Back")
            print(LINE)
            command = input("Choose Options edit or back: ").upper()
            print(LINE)
            if command == "1":
                self.edit_property(property)
                self.print_property_table(property)
            elif command == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)

    def print_property_table(self, property, nr=None):
        property_table = Texttable()
        if nr is not None:
            property_table.add_row(["Number",nr])
        property_table.add_row(["Destination",property.destination])
        property_table.add_row(["Address",property.address])
        property_table.add_row(["Squarefoot",property.squarefoot])
        property_table.add_row(["Rooms",property.rooms])
        property_table.add_row(["Type",property.type])
        property_table.add_row(["Property_id",property.property_id])
        property_table.add_row(["Facilities",property.facilities])
        print(property_table.draw())

    def edit_property(self, prop):
        while True:
            fieldnames = ['Destination', 'Address', 'Squarefoot', 'Rooms', 'Type', 'Facilities']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                setattr(prop, fieldnames[col-1].lower(), newval)
                return self.llapi.edit_property(prop)
            except:
                print('Invalid input, try again!')



