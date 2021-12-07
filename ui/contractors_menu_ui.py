from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.contractor_ui import ContractorUI
from Extra.acci import contAscii

LINE = '------------------------------------------'

class ContractorMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
        while True:
            # contAscii()
            operations =  ['Search by ID', 'See list']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'Contractors in {self.destination}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Search by ID':
                found_contractor = self.llapi.search_contractor()
                if found_contractor is not None:
                    contractor_ui = ContractorUI(found_contractor, self.destination, self.user_type)
                    contractor_ui.start()
            elif operation == 'See list':
                self.llapi.list_contractors()
                print(LINE)
            elif operation == 'Add new':
                self.llapi.create_contractor()
