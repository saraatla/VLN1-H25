from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.property_ui import PropertyUI

LINE = '------------------------------------------'

class PropertyMenu:
    def __init__(self, location, user_type):
        self.location = location
        self.llapi = LLAPI(self.location)
        self.user_type = user_type

    def start(self):
        while True:
            operations =  ['Search by ID', 'See list', 'Add new']
            operations_menu = Menu(f'Properties in {self.location}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Search by ID':
                found_property = self.llapi.search_property()
                if found_property is not None:
                    property_ui = PropertyUI(found_property, self.location)
                    property_ui.start()
            elif operation == 'See list':
                self.llapi.list_properties()
                print(LINE)
            elif operation == 'Add new':
                self.llapi.create_property()