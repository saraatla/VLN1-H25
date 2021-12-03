from data.DLAPI import DLAPI

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

    def edit_employee(self):
        emp = input('Which employee would you like to change?: ')
        col = input('What wolud you want to change? ')
        try:
            emp = int(emp)
            col = int(col)
        except:
            print('TYPE FUCKING NUMBERS!!')
        newval = input(f'What is the new {col}? ')
        return self.dlapi.edit_employee(emp, col, newval)
    

    def search_employee(self, search):
        reader = self.dlapi.list_employees()
        for row in reader:
            if self.location == "All Locations":
                if search == row.ssn:
                    return row
            elif row.location == self.location:
                if search == row.ssn:
                    return row

        return False
