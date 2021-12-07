from ui.menu import Menu
from ui.employee_menu_ui import EmployeeMenu
from ui.property_menu_ui import PropertyMenu
from ui.contractors_menu_ui import ContractorMenu
from ui.work_requests_menu_ui import WorkRequestMenu
from ui.destination_ui import DestinationUI
from logic.LLAPI import LLAPI


class OperationsUI:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
        while True:
            if self.destination == 'All destinations':
                operations =  ['Employees', 'Properties', 'Work requests', 'Contractors',]
            else:
                operations =  ['Employees', 'Properties', 'Work requests', 'Contractors','Destination info']
            operations_menu = Menu(f'Welcome to {self.destination}\nMain menu for {self.user_type}',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Employees':
                employee_menu  = EmployeeMenu(self.destination,self.user_type)
                employee_menu.start()
            elif operation == 'Properties':
                property_menu  = PropertyMenu(self.destination,self.user_type)
                property_menu.start()
            elif operation == 'Work requests':
                work_request_menu  = WorkRequestMenu(self.destination,self.user_type)
                work_request_menu.start()
            elif operation == 'Contractors':
                contractor_menu  = ContractorMenu(self.destination,self.user_type)
                contractor_menu.start()
            elif operation == 'Destination info':
                destination = self.llapi.search_destination(self.destination)
                destination_ui = DestinationUI(destination)
                destination_ui.start()

