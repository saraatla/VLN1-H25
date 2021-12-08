from Extra.TermcolorFile.termcolor import colored, cprint
LINE = '------------------------------------------'

class Menu:
    def __init__(self, intro, options):
        self.intro = intro
        self.options = options

    def draw_options(self):
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
                    print("Invalid option, try again!")
                else:
                    return command - 1
            except:
                print("Invalid option, try again!")
    