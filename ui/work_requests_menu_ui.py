from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.employee_ui import EmployeeUI

class WorkRequestMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
         while True:
            operations =  ['Search by Work Request ID', 'Search by Property ID', 'Search by SSN', 'Search by Contractor Name' ,'See list of all requests', 'See list of requests ready to close' ,'Add new']
            operations_menu = Menu(f'Work Requests in {self.destination}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Search by SSN': # HALDA ÁFRAM HÉR SARA
                found_employee = self.llapi.search_employees(self.destination)
                if found_employee is not None:
                    employee_ui = EmployeeUI(found_employee)
                    employee_ui.start()
            elif operation == 'See list':
                employee_list = self.llapi.list_employees(self.destination)
                for employee in employee_list: #eh svona veit ekki
                    print(employee)
            elif operation == 'Add new':
                new_employee = self.llapi.create_employee()
                employee_ui = EmployeeUI(new_employee)
                employee_ui.start()