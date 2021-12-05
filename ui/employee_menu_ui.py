from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.employee_ui import EmployeeUI

LINE = '------------------------------------------'

class EmployeeMenu:
    def __init__(self, location, user_type):
        self.location = location
        self.llapi = LLAPI(self.location)
        self.user_type = user_type

    def start(self):
        while True:
            operations =  ['Search by SSN', 'See list', 'Add new']
            operations_menu = Menu(f'Employees in {self.location}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Search by SSN':
                found_employee = self.llapi.search_employee()
                if found_employee is not None: 
                    employee_ui = EmployeeUI(found_employee, self.location)
                    employee_ui.start()
            elif operation == 'See list':
                self.llapi.list_employees()
                print(LINE)
            elif operation == 'Add new':
                self.llapi.create_employee()
