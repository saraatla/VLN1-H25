from Extra.texttableFile.texttable import Texttable
from Extra.texttableFile.texttable import Texttable
from ui.menu import Menu
from logic.LLAPI import LLAPI

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
                search = input('Enter SSN: ')
                found_employee = self.llapi.search_employee(search, self.destination)
                if found_employee is None: 
                    print(f'{LINE}\nEmployee not found\n{LINE}')
                else:
                    self.individual_employee_ui(found_employee)

            elif operation == 'See list':
                emp_list = self.list_employees()
                while True:
                    command = input("Enter number of report to open or B to Back:").upper()
                    if command == "B":
                        return
                    if not command.isdigit():
                        print("Invalid input, try again!")
                    else:
                        nr = int(command)
                        for index, employee in enumerate(emp_list):
                            if index+1 == nr:
                                self.individual_employee_ui(employee,nr)
                        break
            elif operation == 'Add new':
                self.create_employee()
                print(f'{LINE}\nEmployee successfully created!\n{LINE}')


    def create_employee(self):
        print('Enter the following information: ')
        print(LINE)
        emp = []
        fieldnames = ['Name', 'SSN', 'Email', "Address", 'Phone', 'GSM', 'Destination', 'Title']
        for field in fieldnames:
            val = input(f'{field}: ')
            emp.append(val)
        return self.llapi.create_employee(emp) 


    def list_employees(self):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(300)
        emp_list = self.llapi.list_employees(self.destination)
        for item in range(len(emp_list)):
            emp = emp_list[item]
            table.add_rows([["Nr","Name","SSN","Email","Gsm","Destination","Title"], 
                            [item+1,emp.name, emp.ssn, emp.email, emp.gsm, emp.destination, emp.title]])
        print(table.draw())
        return emp_list

    
    def individual_employee_ui(self, employee, nr=None):
        self.print_employee_table(employee, nr)
        if self.user_type == 'Employee':
            return
        while True:
            print("1: Edit\nB: Back")
            print(LINE)
            command = input("Choose Options edit or back: ").upper()
            print(LINE)
            if command == "1":
                self.edit_employee(employee)
                self.print_employee_table(employee)
            elif command == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)
    

    def print_employee_table(self, employee, nr=None):
        employee_table = Texttable()
        if nr is not None:
            employee_table.add_row(["Number",nr])
        employee_table.add_row(["Name",employee.name])
        employee_table.add_row(["SSN",employee.ssn])
        employee_table.add_row(["Email",employee.email])
        employee_table.add_row(["Address",employee.address])
        employee_table.add_row(["Phone",employee.phone])
        employee_table.add_row(["GSM",employee.gsm])
        employee_table.add_row(["Destination",employee.destination])
        employee_table.add_row(["Title",employee.title])
        print(employee_table.draw())


    def edit_employee(self,emp):
        while True:
            ssn = emp.ssn
            fieldnames = ['Name', 'Email', 'Address', 'Phone', 'GSM', 'Destination', 'Title']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                setattr(emp, fieldnames[col-1].lower(), newval)
                return self.llapi.save_employee(emp)
            except:
                print('Invalid input, try again!')


