from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.employee_ui import EmployeeUI

class EmployeeMenu:
    def __init__(self, location, user_type):
        self.llapi = LLAPI()
        self.location = location
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
                search = input('Enter SSN:')
                found_employee = self.llapi.search_employee(search)
                print(f'This is {found_employee}')
                if found_employee is not None:
                    employee_ui = EmployeeUI(found_employee)
                    employee_ui.start()
            elif operation == 'See list':
                employee_list = self.llapi.list_employees(self.location)
                for employee in employee_list: #eh svona veit ekki
                    print(employee)
            elif operation == 'Add new':
                new_employee = self.llapi.create_employee()
                employee_ui = EmployeeUI(new_employee)
                employee_ui.start()