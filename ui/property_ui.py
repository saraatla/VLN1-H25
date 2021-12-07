from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class PropertyUI:
    def __init__(self, property, destination):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.property = property
    
    def start(self):
        print(LINE)
        print(self.property)
        print(LINE)
        while True:
            if self.user_type == 'Manager':
                self.manager_start()
            elif self.user_type == 'Employee':
                self.employee_start()
            print(LINE)

    def manager_start(self):
        options = """1: Edit \nB: Back"""
        input_str = "Choose Options edit or back: "
        print(options)
        print(LINE)
        command = input(input_str).upper()
        print(LINE)
        if command == "1":
            self.llapi.edit_property(self.property)
            edited_property = self.llapi.search_property(self.property.property_id)
            print(LINE)
            print(edited_property)
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
