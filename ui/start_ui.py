from Extra.acci import acci
from ui.destination_ui import destinationUI
from ui.menu import Menu

class StartUI:
    def __init__(self):
        pass

    def start(self):
        while True:
            acci()
            intro = 'Welcome to NaN Air \nPlease Enter your status in the company'
            options = ['Supervisor', 'Employee']
            menu = Menu(intro, options)
            selection  = menu.draw_options()
            if selection < 0:
                return
            selection_str = options[selection]
            destination_menu  = destinationUI(selection_str)
            destination_menu.start()

        

