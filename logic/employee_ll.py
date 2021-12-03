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

    def edit_employee(self, empno, col, newvalue):
        return self.dlapi.edit_employee(empno, col, newvalue)

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
