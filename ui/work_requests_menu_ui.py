from ui.menu import Menu
from logic.LLAPI import llapi
from employee_ui import EmployeeUI

class WorkRequestMenu:
    def __init__(self, location, user_type):
        self.location = location
        self.user_type = user_type

    def start(self):
         while True:
            operations =  ['Search by Work Request ID', 'Search by Property ID', 'Search by SSN', 'Search by Contractor Name' ,'See list of all requests', 'See list of requests ready to close' ,'Add new']
            operations_menu = Menu(f'Work Requests in {self.location}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Search by SSN': # HALDA ÁFRAM HÉR SARA
                found_employee = llapi.search_employees(self.location)
                if found_employee is not None:
                    employee_ui = EmployeeUI(found_employee)
                    employee_ui.start()
            elif operation == 'See list':
                employee_list = llapi.list_employees(self.location)
                for employee in employee_list: #eh svona veit ekki
                    print(employee)
            elif operation == 'Add new':
                new_employee = llapi.create_employee()
                employee_ui = EmployeeUI(new_employee)
                employee_ui.start()