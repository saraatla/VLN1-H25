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

    def edit_employee(self, emp):
        while True:
            emp = input('Which employee would you like to change?: ')
            fieldnames = ['Name', 'Email', 'Address', 'Phone', 'GSM', 'Location', 'Airport', 'Title']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What would you want to change? ')
            try:
                emp = int(emp)
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                return self.dlapi.edit_employee(emp, col, newval)
            except:
                print('Invalid input, try again!')

    def search_employee(self, search):
        while True:
            if search == '':
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
                    print(LINE)
                    print('Employee not found')
                    print(LINE)
                    return