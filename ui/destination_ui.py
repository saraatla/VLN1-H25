LINE = '------------------------------------------'

class DestinationUI:
    def __init__(self, destination):
        self.destination = destination
        self.options = """B: Back"""

    def start(self):
        print(LINE)
        print(self.destination)
        print(LINE)
        while True:
            command = input("Enter B to go back:").upper()
            if command == "B":
                return
            else:
                print("Invalid input, try again!")

