from logic.LLAPI import llapi
LINE = '--------'

class EmployeeUI:
    def __init__(self, employee):
        self.employee = employee
        self.options = """[1].Edit
[B].Back"""

    def start(self):
        print(LINE)
        print(self.employee)
        print(LINE)
        while True:
            print(self.options)
            print(LINE)
            commands2 = input("Choose Options edit or back: ").upper()
            if commands2 == "1":
                llapi.edit_employee(self, self.employee)
                print(LINE)
                edited_employee = llapi.search_employee(self.employee)
                print(edited_employee)
                print(LINE)
            elif commands2 == "B":
                return
            else:
                print("Invalid option, try again ")

