from logic.LLAPI import llapi
LINE = '--------'

class PropertyUI:
    def __init__(self, property):
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
            commands2 = input("Choose Options edit or back: ")
            if commands2 == "1":
                llapi.edit_property(self, self.property)
                print(LINE)
                edited_property = llapi.search_property(self.property)
                print(edited_property)
                print(LINE)
            elif commands2 == "b":
                return
            else:
                print("Invalid option, try again ")
