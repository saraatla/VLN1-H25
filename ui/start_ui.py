from ui.location_ui import LocationUI
from ui.menu import Menu

class StartUI:
    def __init__(self):
        pass

    def start(self):
        while True:
            intro = 'Welcome to NaN Air \nPlease Enter your status in the company'
            options = ['Supervisor', 'Employee']
            menu = Menu(intro, options)
            selection  = menu.draw_options()
            if selection < 0:
                return
            selection_str = options[selection]
            location_menu  = LocationUI(selection_str)
            location_menu.start()

        

