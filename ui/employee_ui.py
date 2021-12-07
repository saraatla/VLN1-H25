from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class EmployeeUI:
    def __init__(self, employee, destination, data, nr=""):
        self.destination = destination
        self.llapi= LLAPI(self.destination)
        self.employee = employee
        self.data = data
        self.nr = nr
        self.options = """1: Edit
B: Back"""

    def start(self):
        print(LINE)
        print(self.employee)
        print(LINE)
        while True:
            print(self.options)
            print(LINE)
            commands2 = input("Choose Options edit or back: ").upper()
            print(LINE)
            if commands2 == "1":
                self.llapi.edit_employee(self.data)
                edited_employee = self.llapi.search_employee(self.data.ssn,self.nr)
                print(LINE)
                print(edited_employee)
                print(LINE)
            elif commands2 == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)

