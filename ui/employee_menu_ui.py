from Extra.texttableFile.texttable import Texttable, get_color_string, bcolors
from Extra.acci import empAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI
from Extra.TermcolorFile.termcolor import colored, cprint

LINE = '------------------------------------------'

class EmployeeMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.destination_collor = colored(self.destination, 'blue' ,attrs=['bold', 'underline'])
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.colored_user_type = colored(self.user_type, 'green' ,attrs=['bold', 'underline'])

    def start(self):
        empAscii()
        while True:
            operations =  ['Search by SSN', 'See list']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'Employees in {self.destination_collor}\nSign in as {self.colored_user_type}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            if operation  == 'Search by SSN':
                search = input(colored('Enter SSN: ','green' ,attrs=['bold', 'underline']))
                found_employee = self.llapi.search_employee(search, self.destination)
                if found_employee is None: 
                    print(f'{LINE}\nEmployee not found\n{LINE}')
                else:
                    self.individual_employee_ui(found_employee)

            elif operation == 'See list':
                emp_list = self.list_employees()
                while True:
                    command = input(colored("Enter number of employee to open or B to Back: ",'green' ,attrs=['bold', 'underline'])).upper()
                    if command == "B":
                        break
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
        fieldnames = ['Name', 'SSN', 'Email', "Address", 'Phone', 'GSM', 'Title']
        emp = []
        if self.destination == 'All destinations':
            fieldnames.insert(6, 'Destination')
        for field in fieldnames:
            val = input(colored(f'{field}: ','green' ,attrs=['bold', 'underline']))
            emp.append(val)
        if self.destination != 'All destinations':
            emp.insert(6, self.destination)
        return self.llapi.create_employee(emp) 


    def list_employees(self):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(300)
        emp_list = self.llapi.list_employees(self.destination)
        for item in range(len(emp_list)):
            emp = emp_list[item]
            table.add_rows([[get_color_string(bcolors.GREEN,"Number"),get_color_string(bcolors.GREEN,"Name"),get_color_string(bcolors.GREEN,"SSN"),get_color_string(bcolors.GREEN,"Destination"),get_color_string(bcolors.GREEN,"Title")], 
                            [get_color_string(bcolors.GREEN,item+1),emp.name, emp.ssn, emp.destination, emp.title]])
        print(table.draw())
        return emp_list

    
    def individual_employee_ui(self, employee, nr=None):
        self.print_employee_table(employee, nr)
        while True: 
            if self.user_type == 'Employee':
                command = input(colored("Press B for back: ",'green' ,attrs=['bold', 'underline'])).upper()
                print(LINE)
                if command == "B":
                    return
                else:
                    print("Invalid option, try again ")
                    print(LINE)
            else:
                print("1: Edit\nB: Back")
                print(LINE)
                command = input(colored("Choose Options edit or back: ",'green' ,attrs=['bold', 'underline'])).upper()
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
            employee_table.add_row([get_color_string(bcolors.GREEN,"Number"),nr])
        employee_table.add_row([get_color_string(bcolors.GREEN,"Name"),employee.name])
        employee_table.add_row([get_color_string(bcolors.GREEN,"SSN"),employee.ssn])
        employee_table.add_row([get_color_string(bcolors.GREEN,"Email"),employee.email])
        employee_table.add_row([get_color_string(bcolors.GREEN,"Address"),employee.address])
        employee_table.add_row([get_color_string(bcolors.GREEN,"Phone"),employee.phone])
        employee_table.add_row([get_color_string(bcolors.GREEN,"GSM"),employee.gsm])
        employee_table.add_row([get_color_string(bcolors.GREEN,"Destination"),employee.destination])
        employee_table.add_row([get_color_string(bcolors.GREEN,"Title"),employee.title])
        print(employee_table.draw())


    def edit_employee(self,emp):
        while True:
            fieldnames = ['Name', 'Email', 'Address', 'Phone', 'GSM', 'Destination', 'Title']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input(colored('What do you want to change? ','green' ,attrs=['bold', 'underline']))
            try:
                col = int(col)
                newval = input(colored(f'What is the new {fieldnames[col-1]}? ','green' ,attrs=['bold', 'underline']))
                setattr(emp, fieldnames[col-1].lower(), newval)
                return self.llapi.save_employee(emp)
            except:
                print('Invalid input, try again!')


