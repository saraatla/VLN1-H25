import csv
from models.employee_model import Employee

class EmployeeDL:
    """Employee data layer class; Contains 4 functions: lists, 
    makes new and changes information about an employee"""
    def __init__(self,destination):
        self.filepath = "csv/Employees.csv"
        self.destination = destination
    
    def list_employees(self):
        """This function reads the csv file and makes a list with 
        all the employees along with their information
        Returns:
            return_list: list of employee info."""
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                employee = Employee([row["Name"], row["SSN"], row["Email"], row["Address"], row["Phone"], 
                row["GSM"], row["Destination"], row["Title"]]) # Make an instance of Employee# Make an instance of Employee
                return_list.append(employee)
        return return_list

    def create_employee(self,employee):
        """This function appends a new employee to the csv file
        Args:
            employee (class instance): employee model class"""
        with open(self.filepath,'a', newline='') as csvfile:
            fieldnames = ['Name', 'SSN', 'Email', 'Address', 'Phone', 'GSM', 'Destination', 'Title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Name': employee.name, 'SSN': employee.ssn, 'Email': employee.email, 'Address': employee.address, 
            'Phone':employee.phone, 'GSM':employee.gsm, 'Destination':employee.destination, 'Title':employee.title})
    

    def edit_employee(self, employee): 
        """This function edits a certain value for a certain employee (input by supervisor)
        Args:
            employee (class): model class attributes"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader)
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile) # converts the value into delimited string on the csvfile
            for row in data_list:
                if employee.ssn == row[1]:
                    writer.writerow([employee.name, 
                                     employee.ssn, 
                                     employee.email, 
                                     employee.address, 
                                     employee.phone, 
                                     employee.gsm, 
                                     employee.destination, 
                                     employee.title])
                else:
                    writer.writerow(row)





    