from Extra.acci import acci
from ui.destination_ui import DestinationUI
from ui.menu import Menu
import time

class StartUI:
    def __init__(self):
        pass

    def start(self):
        while True:
            acci()
            print("%s" % time.ctime())
            intro = 'Welcome to NaN Air \nPlease Enter your status in the company.'
            options = ['Supervisor', 'Employee']
            menu = Menu(intro, options)
            selection = menu.draw_options()
            if selection < 0:
                return
            selection_str = options[selection]
            destination_menu = DestinationUI(selection_str)
            destination_menu.start()

        

