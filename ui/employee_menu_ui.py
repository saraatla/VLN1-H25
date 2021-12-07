from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.employee_ui import EmployeeUI

LINE = '------------------------------------------'

class EmployeeMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
        while True:
            operations =  ['Search by SSN', 'See list']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'Employees in {self.destination}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Search by SSN':
                found_employee, data = self.llapi.search_employee()
                if found_employee is not None: 
                    employee_ui = EmployeeUI(found_employee, self.destination, data)
                    employee_ui.start()
            elif operation == 'See list':
                table, data, nr = self.llapi.list_employees()
                if table is not None:
                    employee_ui = EmployeeUI(table, self.destination, data, nr)
                    employee_ui.start()
            elif operation == 'Add new':
                self.llapi.create_employee()
