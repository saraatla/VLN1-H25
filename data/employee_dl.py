import csv
from models.employee_model import Employee

class EmployeeDL:
    """Employee data layer class; Contains 4 functions: lists, 
    makes new and changes information about an employee"""
    def __init__(self,location):
        self.filepath = "csv/Employees.csv"
        self.location = location
    
    def list_employees(self):
        """This function reads the csv file and makes a list with 
        all the employees along with their information"""
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                emp = Employee([row["Name"], row["SSN"], row["Email"], row["Address"], row["Phone"], 
                row["GSM"], row["Location"], row["Airport"], row["Title"]]) # Make an instance of Employee# Make an instance of Employee
                return_list.append(emp)
        return return_list

    def create_employee(self,emp):
        "This function appends a new employee to the csv file"
        with open(self.filepath,'a', newline='') as csvfile:
            fieldnames = ['Name', 'SSN', 'Email', 'Address', 'Phone', 'GSM', 'Location', 'Airport', 'Title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Name': emp.name, 'SSN': emp.ssn, 'Email': emp.email, 'Address': emp.address, 
            'Phone':emp.phone, 'GSM':emp.gsm, 'Location':emp.location, 'Airport':emp.airport, 'Title':emp.title})
    
    def edit_employee(self, emp, col, newvalue): 
        """This function edits a certain value for a certain employee (input by supervisor)"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader)
            if col == 1:
                col = 0
            data_list[emp][col] = newvalue
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile) # converts the value into delimited string on the csvfile
            writer.writerows(data_list)



    