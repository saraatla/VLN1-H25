from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class ContractorUI:
    def __init__(self, contractor, destination, user_type):
        self.destination = destination
        self.llapi= LLAPI(self.destination)
        self.contractor = contractor
        self.user_type = user_type
        if self.user_type == 'Manager':
            self.options = """1: Edit
B: Back"""
            self.input_str = "Choose Options edit or back: "
        else:
            self.options = """B: Back"""
            self.input_str = "Press B for back: "

    def start(self):
        print(LINE)
        print(self.contractor)
        print(LINE)
        while True:
            print(self.options)
            print(LINE)

            commands2 = input(self.input_str).upper()
            print(LINE)
            if commands2 == "1":
                self.llapi.edit_contractor(self.contractor)
                edited_contractor = self.llapi.search_contractor(self.contractor.id)
                print(LINE)
                print(edited_contractor)
                print(LINE)
            elif commands2 == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)