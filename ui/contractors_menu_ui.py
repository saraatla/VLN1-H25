from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.contractor_ui import ContractorUI

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
                found_contractor = self.llapi.search_contractor(self.location)
                if found_contractor is not None:
                    contractor_ui = ContractorUI(found_contractor)
                    contractor_ui.start()
            elif operation == 'See list':
                contractor_list = self.llapi.list_contractors(self.location)
                for contractor in contractor_list: #eh svona veit ekki
                    print(contractor)
            elif operation == 'Add new':
                new_contractor = self.llapi.create_contractor()
                contractor_ui = ContractorUI(new_contractor)
                contractor_ui.start()