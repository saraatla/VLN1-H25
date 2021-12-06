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
        all the employees along with their information"""
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                emp = Employee([row["Name"], row["SSN"], row["Email"], row["Address"], row["Phone"], 
                row["GSM"], row["Destination"], row["Airport"], row["Title"]]) # Make an instance of Employee# Make an instance of Employee
                return_list.append(emp)
        return return_list

    def create_employee(self,emp, ID):
        "This function appends a new employee to the csv file"
        with open(self.filepath,'a', newline='') as csvfile:
            fieldnames = ['Name', 'SSN', 'Email', 'Address', 'Phone', 'GSM', 'destination', 'Airport', 'Title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Name': emp.name, 'SSN': emp.ssn, 'Email': emp.email, 'Address': emp.address, 
            'Phone':emp.phone, 'GSM':emp.gsm, 'destination':emp.destination, 'Airport':emp.airport, 'Title':emp.title})
    
    def edit_employee(self, ssn, col, newvalue): 
        """This function edits a certain value for a certain employee (input by supervisor)"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader)
            for employee_value in data_list:
                for i,value in enumerate(employee_value):
                    if value == ssn:
                        data_list[i][col] = newvalue
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile) # converts the value into delimited string on the csvfile
            writer.writerows(data_list)



    