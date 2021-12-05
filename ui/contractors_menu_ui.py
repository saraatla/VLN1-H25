from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.contractor_ui import ContractorUI

LINE = '------------------------------------------'

class ContractorMenu:
    def __init__(self, location, user_type):
        self.location = location
        self.llapi = LLAPI(self.location)
        self.user_type = user_type

    def start(self):
        while True:
            operations =  ['Search by name', 'See list', 'Add new']
            operations_menu = Menu(f'Contractors in {self.location}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Search by name':
                found_contractor = self.llapi.search_contractor()
                if found_contractor is not None:
                    contractor_ui = ContractorUI(found_contractor, self.location)
                    contractor_ui.start()
            elif operation == 'See list':
                self.llapi.list_contractors()
                print(LINE)
            elif operation == 'Add new':
                self.llapi.create_contractor()
