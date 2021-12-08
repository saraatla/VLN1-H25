from data.DLAPI import DLAPI
from models.employee_model import Employee
LINE = '------------------------------------------'

class EmployeeLL:
    """Employee logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self, destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)


    def list_employees(self, destination):
        employee_list = []
        for employee in self.dlapi.list_employees():
            if destination == 'All destinations' or destination == employee.destination:
                employee_list.append(employee)
        return employee_list
        

    def create_employee(self, emp):
        self.dlapi.create_employee(Employee(emp)) 
        


    def search_employee(self, ssn, destination):
        reader = self.dlapi.list_employees()
        for employee in reader:
            if employee.ssn == ssn:
                if destination == 'All destinations' or destination == employee.destination:
                    return employee
        return None


    def save_employee(self, emp):
        return self.dlapi.save_employee(emp)

