from data.DLAPI import DLAPI
LINE = '------------------------------------------'

class EmployeeLL:
    """Employee logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self, location):
        self.location = location
        self.dlapi = DLAPI(self.location)
        

    def list_employees(self):
        return self.dlapi.list_employees()
        
    def create_employee(self,emp):
        return self.dlapi.create_employee(emp)

    #def edit_employee(self, empno, col, newvalue):
        #return self.dlapi.edit_employee(empno, col, newvalue)

    def edit_employee(self, emp):
        emp = input('Which employee would you like to change?: ')
        col = input('What wolud you want to change? ')
        try:
            emp = int(emp)
            col = int(col)
        except:
            print('TYPE FUCKING NUMBERS!!')
        newval = input(f'What is the new {col}? ')
        return self.dlapi.edit_employee(emp, col, newval)
    

    def search_employee(self):
        while True:
            search = input('Enter SSN: ')
            reader = self.dlapi.list_employees()
            for row in reader:
                if self.location == "All Locations":
                    if search == row.ssn:
                        return row
                elif row.location == self.location:
                    if search == row.ssn:
                        return row
                else:
                    print('Employee not found')
                    print(LINE)
                    break

"""if found_employee is not None: 
    return found_employee
    employee_ui = EmployeeUI(found_employee, self.location)
    employee_ui.start()
    hold_on = False
else:
    print('Invalid option, choose try again or go back')
return None"""
