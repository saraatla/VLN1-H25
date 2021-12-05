from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class PropertyUI:
    def __init__(self, property, location):
        self.location = location
        self.llapi = LLAPI(self.location)
        self.property = property
        self.options = """[1].Edit
[B].Back"""

    def start(self):
        print(LINE)
        print(self.property)
        print(LINE)
        while True:
            print(self.options)
            print(LINE)
            commands2 = input("Choose Options edit or back: ").upper()
            print(LINE)
            if commands2 == "1":
                self.llapi.edit_property(self.property)
                edited_property = self.llapi.search_property(self.property.property_id)
                print(LINE)
                print(edited_property)
                print(LINE)
            elif commands2 == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)
