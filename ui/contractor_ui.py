from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class ContractorUI:
    def __init__(self, contractor, destination):
        self.destination = destination
        self.llapi= LLAPI(self.destination)
        self.contractor = contractor
        self.options = """1: Edit
B: Back"""

    def start(self):
        print(LINE)
        print(self.contractor)
        print(LINE)
        while True:
            print(self.options)
            print(LINE)
            commands2 = input("Choose Options edit or back: ").upper()
            print(LINE)
            if commands2 == "1":
                self.llapi.edit_contractor(self.contractor)
                edited_contractor = self.llapi.search_contractor(self.contractor.name)
                print(LINE)
                print(edited_contractor)
                print(LINE)
            elif commands2 == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)