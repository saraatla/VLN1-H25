import csv
from models.employee_model import Employee


class EmployeeDL:
    def __init__(self):
        self.filepath = "csv/Employees.csv"
    
    def list_employees(self):
        ret_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["Name"], row["SSN"], row["Email"], row["Address"], row["Phone"], 
                row["GSM"], row["Location"], row["Airport"], row["Title"])
                ret_list.append(emp)
        return ret_list

    def create_employee(self,emp):
        with open(self.filepath,'a', newline='') as csvfile:
            fieldnames = ['Name', 'SSN', 'Email', 'Address', 'Phone', 'GSM', 'Location', 'Airport', 'Title']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Name': emp.name, 'SSN': emp.ssn, 'Email': emp.email, 'Address': emp.address, 
            'Phone':emp.phone, 'GSM':emp.gsm, 'Location':emp.location, 'Airport':emp.airport, 'Title':emp.title})
    
    def edit_employee(self, empno, col, newvalue):  
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data_list = list(reader)
            if empno == 1:
                data_list[empno-1][col] = newvalue
            else:
                data_list[empno][col] = newvalue
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_list)



    