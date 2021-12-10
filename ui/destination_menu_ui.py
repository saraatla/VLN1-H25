from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.operations_ui import OperationsUI
from Extra.acci import locAscii
from Extra.TermcolorFile.termcolor import colored

LINE = '------------------------------------------'

class DestinationMenu:
    """Destination Menu UI class: contains 2 functions. The class contains an instance of the LLAPI class
    Args:
        user_type (str): user 
        destination (str): destination chosen by user."""

    def __init__(self,user_type,destination=""):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.colored_user_type = colored(self.user_type, 'green' ,attrs=['bold', 'underline'])
        self.color_format = colored("{}",'green' ,attrs=['bold', 'underline'])
        
    def destination_menu_start(self):
        """This function makes the destination menu function. The user chooses which destination
        he wants to see.  After choosing a destination all the information later on in the
        program will only show employees, work requests, contractors and properties in that
        destination.
        Add new destination: makes it possible for the manager to add a new destination to the system."""

        locAscii()
        while True:
            options = self.llapi.list_of_destinations()
            options.append('All destinations')
            if self.user_type == "Manager":
                options.append('Add new destination')        
            destination_menu = Menu(f"Welcome you are signed in as {self.colored_user_type}\nPlease choose destination", options)
            selection  = destination_menu.draw_options()
            if selection < 0:
                return
            option = options[selection]
            if option == 'Add new destination':
                if self.user_type == "Manager":
                    self.__create_destination()
                    print(f'{LINE}\nDestination successfully created!\n{LINE}')
                    while True:
                        command = input(self.color_format.format('Press B for back: ')).upper()
                        if command == 'B':
                            break
                        else:
                            print("Invalid option, please try again")
                            print(LINE)
            else:
                selection_str = options[selection]
                operations = OperationsUI(selection_str, self.user_type)
                operations.start()


    def __create_destination(self):
        print('Enter the following information: ')
        print(LINE)
        fieldnames = ['Destination', 'Phone number', 'Opening hours']
        dest = []
        for field in fieldnames:
            val = input(self.color_format.format(f'{field}: '))
            dest.append(val)
        while True:
            ssn_input = input(self.color_format.format('Manager SSN: '))
            found_ssn = self.llapi.search_employee(ssn_input, 'All destinations')
            if found_ssn is None:
                print('Manager SSN not found')
            elif found_ssn.title == 'Manager':
                dest.append(ssn_input)
                break
            else:
                print('Manager SSN not found')
        return self.llapi.create_destination(dest)
    

    

            

        


        

        