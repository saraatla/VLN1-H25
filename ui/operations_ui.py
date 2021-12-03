from ui.menu import Menu
from ui.employee_menu_ui import EmployeeMenu

class OperationsUI:
    def __init__(self, location, user_type):
        self.location = location
        self.user_type = user_type

    def start(self):
        while True:
            operations =  ['Employees', 'Properties', 'Work requests', 'Contractors']
            operations_menu = Menu(f'Welcome to {self.location}\nMain menu for {self.user_type}',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation  == 'Employees':
                employee_menu  = EmployeeMenu(self.location,self.user_type)
                employee_menu.start()
            elif operation == 'Properties':
                print('property ui')
            elif operation == 'Work requests':
                print('Work request ui')
            elif operation == 'Contractor':
                print('contractor ui')
