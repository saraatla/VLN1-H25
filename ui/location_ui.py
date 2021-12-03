from ui.menu import Menu
from logic.LLAPI import llapi
from ui.operations_ui import OperationsUI

class LocationUI:
    def __init__(self, user_type):
        self.user_type = user_type

    def start(self):
        while True:
            options = llapi.list_locations()
            options.append('All locations')
            location_menu = Menu(f'Welcome you are signed in as {self.user_type}\nPlease choose location', options)
            selection  = location_menu.draw_options()
            if selection < 0:
                return
            selection_str = options[selection]
            operations = OperationsUI(selection_str, self.user_type)
            operations.start()

            

        


        

        