from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class PropertyUI:
    def __init__(self, propertytable, destination,data,nr=""):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.propertytable = propertytable
        self.data = data
        self.nr = nr
        self.options = """1: Edit
B: Back"""
    
    def starttest(self):
        print(LINE)
        print(self.propertytable)
        print(LINE)
        while True:
            print(self.options)
            print(LINE)
            commands2 = input("Choose Options edit or back: ").upper()
            print(LINE)
            if commands2 == "1":
                self.llapi.edit_property(self.data)
                edited_property = self.llapi.search_property(self.data.property_id,self.nr)
                print(LINE)
                print(edited_property)
                print(LINE)
            elif commands2 == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)

    # def start(self):
    #     print(LINE)
    #     print(self.property)
    #     print(LINE)
    #     if self.user_type == 'Manager':
    #         self.manager_start()
    #     elif self.user_type == 'Employee':
    #         self.employee_start()
    #     print(LINE)

    # def manager_start(self):
    #     options = """1: Edit \nB: Back"""
    #     input_str = "Choose Options edit or back: "
    #     while True:
    #         print(options)
    #         print(LINE)
    #         command = input(input_str).upper()
    #         print(LINE)
    #         if command == "1":
    #             self.llapi.edit_property(self.property)
    #             edited_property = self.llapi.search_property(self.property.property_id)
    #             print(LINE)
    #             print(edited_property)
    #             print(LINE)
    #         elif command == "B":
    #             return
    #         else:
    #             print("Invalid option, try again ")
        
    # def employee_start(self):
    #     options = """B: Back"""
    #     input_str = "Press B for back: "
    #     while True:
    #         print(options)
    #         print(LINE)
    #         command = input(input_str).upper()
    #         print(LINE)
    #         if command == "B":
    #             return
    #         else:
    #             print("Invalid option, try again ")
