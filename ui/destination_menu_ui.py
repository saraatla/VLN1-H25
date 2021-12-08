from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.operations_ui import OperationsUI
from Extra.acci import locAscii
from Extra.TermcolorFile.termcolor import colored, cprint
class DestinationMenu:
    def __init__(self,user_type,destination=""):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.colored_user_type = colored(self.user_type, 'green' ,attrs=['bold', 'underline'])
        
    def start(self):
        while True:
            locAscii()
            options = self.llapi.list_of_destinations()
            options.append('All destinations')                      #{colored(self.location, attrs=['bold'])}
            destination_menu = Menu(f"Welcome you are signed in as {self.colored_user_type}\nPlease choose destination", options)
            selection  = destination_menu.draw_options()
            if selection < 0:
                return
            selection_str = options[selection]
            operations = OperationsUI(selection_str, self.user_type)
            operations.start()
    

    

            

        


        

        