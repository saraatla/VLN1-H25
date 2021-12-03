from ui.menu import Menu
from logic.LLAPI import llapi
from ui.property_ui import PropertyUI

class PropertyMenu:
    def __init__(self, location, user_type):
        self.location = location
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
                search = input('Enter property ID:')
                found_property = llapi.search_properties(search)
                if found_property is not None:
                    property_ui = PropertyUI(found_property)
                    property_ui.start()
            elif operation == 'See list':
                property_list = llapi.list_properties(self.location)
                for property in property_list: #eh svona veit ekki
                    print(property)
            elif operation == 'Add new':
                new_property = llapi.create_property()
                property_ui = PropertyUI(new_property)
                property_ui.start()