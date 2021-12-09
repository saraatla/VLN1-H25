from data.DLAPI import DLAPI
from models.employee_model import Employee

class EmployeeLL:
    """Employee logic layer class; Contains 5 functions: fetches the functions in the data layer API,
    search for a employee by ssn and lists employees in the destination the user wants to see"""
    def __init__(self, destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)


    def _list_employees(self, destination):
        """This function lists employees according to destination.
        Args:
            destination (str) : destination chosen by user
        Returns:
            employee_list (list): list of employees in given destination"""
        employee_list = []
        for employee in self.dlapi._list_employees():
            if destination == 'All destinations' or destination == employee.destination:
                employee_list.append(employee)
        return employee_list
        

    def _create_employee(self, employee):
        """Creates new employee"""
        self.dlapi._create_employee(Employee(employee)) 


    def _search_employee(self, ssn, destination):
        """This function searches for a employee by his ssn in list of all employees.
        Args:
            ssn (str): employee ssn input by user
            destination (str) : destination chosen by user
        Returns: 
            employee (class instance): employee model class"""
        reader = self.dlapi._list_employees()
        for employee in reader:
            if employee.ssn == ssn:
                if destination == 'All destinations' or destination == employee.destination:
                    return employee
        return None


    def _edit_employee(self, employee):
        """Edits employee info"""
        return self.dlapi._edit_employee(employee)

