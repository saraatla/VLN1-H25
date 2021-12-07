from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.employee_model import Employee
LINE = '------------------------------------------'

class EmployeeLL:
    """Employee logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self, destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)
        self.table = Texttable()
        self.table2 = Texttable()

    def list_employees(self):
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(300)
        emp_list = self.dlapi.list_employees()
        for item in range(len(emp_list)):
            emp = emp_list[item]
            if emp.destination == self.destination:
                self.table.add_rows([["Nr","Name", "SSN","Email","Gsm","Destination","Title"], [item+1,emp.name, emp.ssn, emp.email, emp.gsm, emp.destination, emp.title]])
            elif self.destination == "All destinations":
                self.table.add_rows([["Nr","Name", "SSN","Email","Gsm","Destination","Title"], [item+1,emp.name, emp.ssn, emp.email, emp.gsm, emp.destination, emp.title]])
        print(self.table.draw())
        self.table.reset()
        while True:
            command = input("Enter Nr of report to open or B to Back:").upper()
            if command == "B":
                return
            elif command.isdigit():
                nr = int(command)
                self.format_for_single_workrequest(emp_list,nr)
            else:
                print("Invalid input, try again!")
        
    def create_employee(self):
        print('Enter the following information: ')
        print(LINE)
        ID = len(self.dlapi.list_employees())
        emp = []
        fieldnames = ['Name', 'SSN', 'Email', "Address", 'Phone', 'GSM', 'Destination', 'Airport', 'Title']
        for field in fieldnames:
            val = input(f'{field}: ')
            emp.append(val)
        self.dlapi.create_employee(Employee(emp),ID)
        print(f'{LINE}\nEmployee successfully created!\n{LINE}')



    def edit_employee(self, emp):
        while True:
            ssn = emp.ssn
            fieldnames = ['Name', 'Email', 'Address', 'Phone', 'GSM', 'destination', 'Airport', 'Title']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                if col == 1:
                    col = 0
                return self.dlapi.edit_employee(ssn, col, newval)
            except:
                print('Invalid input, try again!')

    def search_employee(self, search):
        while True:
            if search == '':
                search = input('Enter SSN: ')
            reader = self.dlapi.list_employees()
            nr= 1
            for row in reader:
                if row.destination == self.destination:
                    if search == row.ssn:
                        self.get_table(row,nr)
                        return
                elif search == row.ssn:
                        self.get_table(row,nr)
                        print(f"This Employee is in {row.destination}")
                        return
                else:
                    print(f'{LINE}\nEmployee not found\n{LINE}')
                    return
        
    def format_for_single_workrequest(self,retlist,nr):
        if retlist:
            for item in range(len(retlist)):
                workreq = retlist[item]
                if item+1 == nr:
                    self.get_table(workreq,nr)
                self.table2.reset()


    def get_table(self,workreq, nr):
        self.table2.add_row(["Nr",nr])
        self.table2.add_row(["Name",workreq.name])
        self.table2.add_row(["Ssn",workreq.ssn])
        self.table2.add_row(["Email",workreq.email])
        self.table2.add_row(["Adress",workreq.address])
        self.table2.add_row(["Phone",workreq.phone])
        self.table2.add_row(["Gsm",workreq.gsm])
        self.table2.add_row(["Destination",workreq.destination])
        self.table2.add_row(["Title",workreq.title])
        print(self.table2.draw())