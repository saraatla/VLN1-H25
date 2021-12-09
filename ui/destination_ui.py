from Extra.TermcolorFile.termcolor import colored
from Extra.texttableFile.texttable import Texttable, get_color_string, bcolors
LINE = '------------------------------------------'
class DestinationUI:
    def __init__(self, destination):
        self.table = Texttable
        self.destination = destination
        self.options = """B: Back"""
        self.color_format = colored("{}",'green' ,attrs=['bold', 'underline'])


    def _destination_info_ui(self):
        self.__print_destination_info_table(self.destination)
        print(LINE)
        while True:
            command = input(self.color_format.format("Enter B to go back: ")).upper()
            print(LINE)
            if command == "B":
                return
            else:
                print("Invalid input, please try again")
    

    def __print_destination_info_table(self, destination):
        destination_table = Texttable()
        destination_table.add_row([get_color_string(bcolors.GREEN,"Destination"),destination.destination])
        destination_table.add_row([get_color_string(bcolors.GREEN,"Phone"),destination.phone])
        destination_table.add_row([get_color_string(bcolors.GREEN,"Open Hours"),destination.open_hours])
        destination_table.add_row([get_color_string(bcolors.GREEN,"Manager SSN"),destination.manager])
        print(destination_table.draw())