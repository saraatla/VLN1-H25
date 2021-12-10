from Extra.texttableFile.texttable import Texttable, get_color_string, bcolors
from Extra.acci import propAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI
from Extra.TermcolorFile.termcolor import colored
from time import sleep
LINE = '------------------------------------------'

class PropertyUI:
    """Property UI layer class. Contains 7 functions. The class contains an instance of the LLAPI class.
    Args: 
        destination (str): destination chosen by user
        user_type (str): user type chosen by user (manager/employee)"""

    def __init__(self, destination, user_type):
        self.destination = destination
        self.destination_collor = colored(self.destination, 'blue' ,attrs=['bold', 'underline'])
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.color_format = colored("{}",'green' ,attrs=['bold', 'underline'])
        self.colored_user_type = colored(self.user_type, 'green' ,attrs=['bold', 'underline'])
        self.Properties_menu_color = colored("Properties Menu",'red' ,attrs=['bold', 'underline'])
        

    def property_menu_start(self):
        """This function makes the property menu function. It depends on the inputs by user: 
        Search by property ID: allows the user to search a property by it's ID, 
        See list: prompts a list of all the property along with their information,
        if the user logged in as a manager he also sees
        Add new: makes it possible to add a new property to the system."""
        
        while True:
            propAscii()
            operations =  ['Search by property ID', 'See list']
            if self.user_type == 'Manager':
                operations.append('Create new')
            operations_menu = Menu(f'{self.Properties_menu_color} in {self.destination_collor}\nSign in as {self.colored_user_type}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            if operation  == 'Search by property ID':
                search = input(self.color_format.format('Enter property ID: ')).upper()
                found_property = self.llapi.search_property(search, self.destination)
                if found_property is None:
                    print(f'{LINE}\nProperty not found\n{LINE}')
                    sleep(2)
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

            elif operation == 'Create new':
                self.__create_property()
                print(f'{LINE}\nProperty successfully created!\n{LINE}')
                sleep(2)


    def __create_property(self):
        """This function runs when the user (manager) chooses 'Add new' . 
        The property will be given a destination according to the user's choice in the destination menu."""

        print('Enter the following information: ')
        print(LINE)
        fieldnames = ['Address', 'Squarefoot', 'Rooms', 'Type', 'Facilities']
        if self.destination != 'All destinations':
            prop = [self.destination]
        else:
            destination_options = self.llapi.list_of_destinations()
            for i, option in enumerate(destination_options):
                print(f"{i+1}: {option}")
            holdon = True
            while holdon == True:
                index = input(self.color_format.format('Choose destination: '))
                try:
                    int(index)
                    destination = destination_options[index-1]
                    holdon = False
                except:
                    print('Invalid input, please try again')
            prop = [destination]   
        for field in fieldnames:
            val = input(self.color_format.format(f'{field}: '))
            prop.append(val)
        new_id = self.llapi.get_new_property_id(prop[0])
        prop.insert(5, new_id)  
        return self.llapi.create_property(prop)


    def __list_properties(self):
        """This function runs when the user chooses 'See list'.
        It will show the list of properties in a printable template format."""

        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(0)
        prop_list = self.llapi.list_properties(self.destination)
        for item in range(len(prop_list)):
            prop = prop_list[item]                                                                                                             
            table.add_rows([[get_color_string(bcolors.GREEN, "Number"),get_color_string(bcolors.GREEN,"Property_ID"),get_color_string(bcolors.GREEN,"Type"),get_color_string(bcolors.GREEN,"Address"),get_color_string(bcolors.GREEN,"Destination")], 
                            [get_color_string(bcolors.GREEN,item+1),prop.property_id, prop.type,prop.address, prop.destination]])
                                    
        print(table.draw())
        return prop_list


    def __individual_property_ui(self, property, nr=None):
        """This function runs when the user chooses 'Search by property ID' and inputs an ID that's in the system.
        It will show information about a property and also the option to edit if the user is a Manager.
        Args:
            property (class instance): property model class,
            nr : either None or int. """

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
        """This function prints property info in a printable template format.
        Args:
            property (class instance): property model class,
            nr : either None or int. """

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

    def __edit_property(self, property):
        """This function runs if the user is a Manager and chooses to Edit property.
        The user chooses what to edit according to the available options.
        Args:
            property (class instance): property model class."""

        while True:
            fieldnames = ['Destination', 'Address', 'Squarefoot', 'Rooms', 'Type', 'Facilities']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input(colored('What do you want to change? ','green' ,attrs=['bold', 'underline']))
            try:
                col = int(col)
                newval = input(colored(f'What is the new {fieldnames[col-1]}? ','green' ,attrs=['bold', 'underline']))
                setattr(property, fieldnames[col-1].lower(), newval)
                return self.llapi.edit_property(property)
            except:
                print('Invalid input, please try again')



