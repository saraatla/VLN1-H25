from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.operations_ui import OperationsUI
from Extra.acci import locAscii
from Extra.TermcolorFile.termcolor import colored

LINE = '------------------------------------------'

class DestinationMenu:
    def __init__(self,user_type,destination=""):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.colored_user_type = colored(self.user_type, 'green' ,attrs=['bold', 'underline'])
        
    def destination_menu_start(self):
        while True:
            locAscii()
            options = self.llapi.list_of_destinations()
            options.append('All destinations')
            if self.user_type == 'Manager':
                options.append('Add new destination')                          #{colored(self.location, attrs=['bold'])}
            destination_menu = Menu(f"Welcome you are signed in as {self.colored_user_type}\nPlease choose destination", options)
            selection  = destination_menu.draw_options()
            if selection < 0:
                return
            option = options[selection]
            if option == 'Add new destination':
                print('Enter the following information: ')
                print(LINE)
                fieldnames = ['Destination', 'Phone number', 'Opening hours', "Manager SSN"]
                dest = []
                for field in fieldnames:
                    val = input(f'{field}: ')
                    dest.append(val)
                return self.llapi.create_destination(dest)
            selection_str = options[selection]
            operations = OperationsUI(selection_str, self.user_type)
            operations.start()
    

    

            

        


        

        