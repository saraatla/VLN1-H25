from Extra.texttableFile.texttable import Texttable, get_color_string, bcolors
from Extra.acci import propAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI
from Extra.TermcolorFile.termcolor import colored
LINE = '------------------------------------------'

class PropertyUI:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.destination_collor = colored(self.destination, 'blue' ,attrs=['bold', 'underline'])
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.color_format = colored("{}",'green' ,attrs=['bold', 'underline'])
        self.colored_user_type = colored(self.user_type, 'green' ,attrs=['bold', 'underline'])
        self.Properties_menu_color = colored("Properties Menu",'red' ,attrs=['bold', 'underline'])
        
        

    def _property_menu_start(self):
        propAscii()
        while True:
            operations =  ['Search by property ID', 'See list']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'{self.Properties_menu_color} in {self.destination_collor}\nSign in as {self.colored_user_type}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            if operation  == 'Search by ID':
                search = input(self.color_format.format('Enter property ID: ')).upper()
                found_property = self.llapi._search_property(search, self.destination)
                if found_property is None:
                    print(f'{LINE}\nProperty not found\n{LINE}')
                else:
                    self.__individual_property_ui(found_property)

            elif operation == 'See list':
                prop_list = self.__list_properties()
                while True:
                    command = input(self.color_format.format("Enter number of property to open or B to Back: ")).upper()
                    if command == "B":
                        break
                    if not command.isdigit():
                        print("Invalid input, please try again")
                    else:
                        nr = int(command)
                        for index, property in enumerate(prop_list):
                            if index+1 == nr:
                                self.__individual_property_ui(property, nr)
                        break

            elif operation == 'Add new':
                self.__create_property()
                print(f'{LINE}\nProperty successfully created!\n{LINE}')


    def __create_property(self):
        print('Enter the following information: ')
        print(LINE)
        fieldnames = ['Address', 'Squarefoot', 'Rooms', 'Type', 'Property_ID', 'Facilities']
        if self.destination != 'All destinations':
            prop = [self.destination]
        else:
            prop = []
            fieldnames.insert(0, 'Destination')        
        for field in fieldnames:
            val = input(self.color_format.format(f'{field}: '))
            prop.append(val)
        return self.llapi._create_property(prop)


    def __list_properties(self):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(0)
        prop_list = self.llapi._list_properties(self.destination)
        for item in range(len(prop_list)):
            prop = prop_list[item]                                                                                                             
            table.add_rows([[get_color_string(bcolors.GREEN, "Number"),get_color_string(bcolors.GREEN,"Property_ID"),get_color_string(bcolors.GREEN,"Type"),get_color_string(bcolors.GREEN,"Address"),get_color_string(bcolors.GREEN,"Destination")], 
                            [get_color_string(bcolors.GREEN,item+1),prop.property_id, prop.type,prop.address, prop.destination]])
                                    
        print(table.draw())
        return prop_list


    def __individual_property_ui(self, property, nr=None):
        self.__print_property_table(property, nr)
        if self.user_type == 'Employee':
            return
        while True:
            print("1: Edit\nB: Back")
            print(LINE)
            command = input(colored("Choose Options edit or back: ",'green' ,attrs=['bold', 'underline'])).upper()
            print(LINE)
            if command == "1":
                self.__edit_property(property)
                self.__print_property_table(property)
            elif command == "B":
                return
            else:
                print("Invalid option, please try again")
                print(LINE)

    def __print_property_table(self, property, nr=None):
        property_table = Texttable()
        if nr is not None:
            property_table.add_row([get_color_string(bcolors.GREEN,"Number"),nr])
        property_table.add_row([get_color_string(bcolors.GREEN,"Destination"),property.destination])
        property_table.add_row([get_color_string(bcolors.GREEN,"Address"),property.address])
        property_table.add_row([get_color_string(bcolors.GREEN,"Squarefoot"),property.squarefoot])
        property_table.add_row([get_color_string(bcolors.GREEN,"Rooms"),property.rooms])
        property_table.add_row([get_color_string(bcolors.GREEN,"Type"),property.type])
        property_table.add_row([get_color_string(bcolors.GREEN,"Property_id"),property.property_id])
        property_table.add_row([get_color_string(bcolors.GREEN,"Facilities"),property.facilities])
        print(property_table.draw())

    def __edit_property(self, prop):
        while True:
            fieldnames = ['Destination', 'Address', 'Squarefoot', 'Rooms', 'Type', 'Facilities']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input(colored('What do you want to change? ','green' ,attrs=['bold', 'underline']))
            try:
                col = int(col)
                newval = input(colored(f'What is the new {fieldnames[col-1]}? ','green' ,attrs=['bold', 'underline']))
                setattr(prop, fieldnames[col-1].lower(), newval)
                return self.llapi._edit_property(prop)
            except:
                print('Invalid input, please try again')



