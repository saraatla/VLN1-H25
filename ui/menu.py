from Extra.TermcolorFile.termcolor import colored, cprint
LINE = '------------------------------------------'

class Menu:
    """Menu UI Layer class. Contains 2 functions.
    Args:
        intro (str): Welcomes the user to the program
        options (list): Manager, Employee """

    def __init__(self, intro, options):
        self.intro = intro
        self.options = options

    def draw_options(self):
        """This function is used in all the other UI layers. It prints out the options and 
        checks if the user's input is correct."""
        
        print(self.intro)
        print(LINE)
        for i, option in enumerate(self.options):
            print(f"{i+1}: {option}")
        print("B: Back")
        print(LINE)
        while True:
            command = input(colored("Select option: ",'green' ,attrs=['bold', 'underline'])).upper()
            print(LINE)
            if command == 'B':
                return -1
            try:
                command = int(command)
                if command > len(self.options):
                    print("Invalid option, please try again")
                else:
                    return command - 1
            except:
                print("Invalid option, please try again")
    