from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.operations_ui import OperationsUI

class destinationUI:
    def __init__(self,user_type,destination=""):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
        while True:
            options = self.llapi.list_of_destinations()
            options.append('All destinations')
            destination_menu = Menu(f'Welcome you are signed in as {self.user_type}\nPlease choose destination', options)
            selection  = destination_menu.draw_options()
            if selection < 0:
                return
            selection_str = options[selection]
            operations = OperationsUI(selection_str, self.user_type)
            operations.start()

            

        


        

        