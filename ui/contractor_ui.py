from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class ContractorUI:
    def __init__(self, contractor, destination, user_type):
        self.destination = destination
        self.llapi= LLAPI(self.destination)
        self.contractor = contractor
        self.user_type = user_type

    def start(self):
        print(LINE)
        print(self.contractor)
        print(LINE)
        
        if self.user_type == 'Manager':
            self.manager_start()
        elif self.user_type == 'Employee':
            self.employee_start()
        

    def manager_start(self):
        options = """1: Edit \nB: Back"""
        input_str = "Choose Options edit or back: "
        print(options)
        print(LINE)
        command = input(input_str).upper()
        print(LINE)
        if command == "1":
                self.llapi.edit_contractor(self.contractor)
                edited_contractor = self.llapi.search_contractor(self.contractor.id)
                print(LINE)
                print(edited_contractor)
                print(LINE)
        elif command == "B":
            return
        else:
            print("Invalid option, try again ")
        
    def employee_start(self):
        options = """B: Back"""
        input_str = "Press B for back: "
        print(options)
        print(LINE)
        command = input(input_str).upper()
        print(LINE)
        if command == "B":
            return
        else:
            print("Invalid option, try again ")