from Extra.acci import acci
from ui.destination_menu_ui import DestinationMenu
from ui.menu import Menu
import time


class LogInUI:
    """Log In UI class. Contains 2 functions."""
    def __init__(self):
        pass

    def _log_in(self):
        """This function shows the opening menu of the program. It welcoms the user and asks
        him to choose what status he has inside the company. """
        while True:
            acci()
            print("%s" % time.ctime())
            intro = 'Welcome to NaN Air \nPlease Enter your status in the company'
            options = ['Manager', 'Employee']
            menu = Menu(intro, options)
            selection = menu.draw_options()
            if selection < 0:
                return
            selection_str = options[selection]
            destination_menu = DestinationMenu(selection_str)
            destination_menu.destination_menu_start()

        

