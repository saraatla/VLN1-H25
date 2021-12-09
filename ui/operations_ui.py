from ui.menu import Menu
from ui.employee_ui import EmployeeUI
from ui.property_ui import PropertyUI
from ui.contractors_ui import ContractorUI
from ui.work_requests_ui import WorkRequestUI
from ui.destination_ui import DestinationUI
from logic.LLAPI import LLAPI
from Extra.TermcolorFile.termcolor import colored


class OperationsUI:
    """Operations UI class. Contains 2 functions. The class contains an instance of the LLAPI class.
    Args:
        destination (str): destination chosen by user
        user_type (str): user type chosen by user (manager/employee)"""

    def __init__(self, destination, user_type):
        self.destination = destination
        self.destination_collor = colored(self.destination, 'blue' ,attrs=['bold', 'underline'])
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.colored_user_type = colored(self.user_type, 'green' ,attrs=['bold', 'underline'])

    def start(self):
        """This function prompts the main menu. 
        Employees: leads to the employee menu
        Properties: -||- property menu
        Work requests: -||- work request menu where the work reports can also be found
        Contractors: -||- contractor menu
        Destination info: -||- destination menu if the user chose a specific destination (not All destinations)"""
        
        while True:
            if self.destination == 'All destinations':
                operations =  ['Employees', 'Properties', 'Work requests', 'Contractors',]
            else:
                operations =  ['Employees', 'Properties', 'Work requests', 'Contractors','Destination info']
            operations_menu = Menu(f'Welcome to {self.destination_collor}\nMain menu for {self.colored_user_type}',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Employees':
                employee_menu  = EmployeeUI(self.destination,self.user_type)
                employee_menu._employee_menu_start()
            elif operation == 'Properties':
                property_menu  = PropertyUI(self.destination,self.user_type)
                property_menu._property_menu_start()
            elif operation == 'Work requests':
                work_request_menu  = WorkRequestUI(self.destination,self.user_type)
                work_request_menu._workrequest_menu_start()
            elif operation == 'Contractors':
                contractor_menu  = ContractorUI(self.destination,self.user_type)
                contractor_menu._contractor_menu_start()
            elif operation == 'Destination info':
                destination = self.llapi._search_destination(self.destination)
                destination_ui = DestinationUI(destination)
                destination_ui._destination_info_ui()

