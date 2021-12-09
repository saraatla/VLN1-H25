
from Extra.texttableFile.texttable import Texttable, get_color_string, bcolors
from Extra.acci import contAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI
from Extra.TermcolorFile.termcolor import colored
LINE = '------------------------------------------'

class ContractorUI:
    """Contractor UI layer class. Contains 7 functions.
    Args:
        destination (str): destination chosen by user
        user_type (str): user type chosen by user (manager/employee)"""

    def __init__(self, destination, user_type):
        self.destination = destination
        self.destination_collor = colored(self.destination, 'blue' ,attrs=['bold', 'underline'])
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.table = Texttable
        self.color_format = colored("{}",'green' ,attrs=['bold', 'underline'])
        self.Contractors_menu_color = colored("Contractors Menu",'red' ,attrs=['bold', 'underline'])

    def _contractor_menu_start(self):
        """This function makes the contractor menu function. It depends on the inputs by user: 
        Search by ID: allows the user to search a contractor by their ID, 
        See list: prompts a list of all the contractors along with their information,
        if the user logged in as a manager he also sees
        Add new: makes it possible to add a new contractor to the system."""

        contAscii()
        while True:
            operations =  ['Search by contractor ID', 'See list']
            if self.user_type == 'Manager':
                operations.append('Create new')
            operations_menu = Menu(f'{self.Contractors_menu_color} in {self.destination_collor}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            if operation  == 'Search by contractor ID':
                search = input(self.color_format.format('Enter contractor ID: ')).upper()
                found_contractor = self.llapi._search_contractor(search)
                if found_contractor is None:
                    print(f'{LINE}\nContractor not found\n{LINE}')
                else:
                    self.__individual_contractor_ui(found_contractor)

            elif operation == 'See list':
                cont_list = self.__list_contractors()
                while True:
                    command = input(self.color_format.format("Enter number of contractor to open or B to Back: ")).upper()
                    if command == "B":
                        break
                    if not command.isdigit():
                        print("Invalid input, please try again")
                    else:
                        nr = int(command)
                        for index, contractor in enumerate(cont_list):
                            if index+1 == nr:
                                self.__individual_contractor_ui(contractor,nr)
                        break

            elif operation == 'Create new':
                self.__create_contractor()
                print(f'{LINE}\nContractor successfully created!\n{LINE}')


    def __create_contractor(self):
        """This function runs when the user (manager) chooses 'Add new' . 
        The contractor will be given a destination according to the user's choice in the destination menu."""

        print('Enter the following information: ')
        print(LINE)
        new_id = self.llapi._get_new_cont_id()
        cont = [new_id]
        fieldnames = ["Name", "Type", "Contact", "Contact's phone", "Address", "Open_hours", "Review"]
        for field in fieldnames:
            val = input(f'{field}: ')
            cont.append(val)
        return self.llapi._create_contractor(cont)

    def __list_contractors(self):
        """This function runs when the user chooses 'See list'.
        It will show the list of contractors in a printable template format."""

        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(160)
        cont_list = self.llapi._list_contractors()
        for item in range(len(cont_list)):
            cont = cont_list[item]
            table.add_rows([[get_color_string(bcolors.GREEN,"Number"), get_color_string(bcolors.GREEN,"Contractor_ID"), get_color_string(bcolors.GREEN,"Name"), get_color_string(bcolors.GREEN,"Type"), get_color_string(bcolors.GREEN,"Address"), get_color_string(bcolors.GREEN,"Open_hours"), get_color_string(bcolors.GREEN,"Review")], 
                                [get_color_string(bcolors.GREEN,item+1), cont.id, cont.name, cont.type, cont.address, cont.open_hours, cont.review]])
        print(table.draw())
        return cont_list

    def __individual_contractor_ui(self, contractor, nr=None):
        """This function runs when the user chooses 'Search by contractor ID' and inputs an ID that's in the system.
        It will show information about a contractor and also the option to edit if the user is a Manager.
        Args:
            contractor (class instance): contractor model class
            nr : either None or int."""

        self.__print_contractor_table(contractor, nr)
        while True:
            if self.user_type == 'Employee':
                    command = input(self.color_format.format("Press B for back: ")).upper()
                    print(LINE)
                    if command == "B":
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)
            else:
                print("1: Edit\nB: Back")
                print(LINE)
                command = input(self.color_format.format("Choose Options edit or back: ")).upper()
                print(LINE)
                if command == "1":
                    self.__edit_contractor(contractor)
                    self.__print_contractor_table(contractor)
                elif command == "B":
                    return
                else:
                    print("Invalid option, please try again")
                    print(LINE)

    def __print_contractor_table(self, contractor, nr=None):
        """This function prints contractor info in a printable template format.
        Args:
            contractor (class instance): contractor model class
            nr : either None or int."""

        contractor_table = Texttable()
        if nr is not None:
            contractor_table.add_row([get_color_string(bcolors.GREEN,"Number"),nr])
        contractor_table.add_row([get_color_string(bcolors.GREEN,"ID"),contractor.id])
        contractor_table.add_row([get_color_string(bcolors.GREEN,"Name"),contractor.name])
        contractor_table.add_row([get_color_string(bcolors.GREEN,"Type"),contractor.type])
        contractor_table.add_row([get_color_string(bcolors.GREEN,"Contact"),contractor.contact])
        contractor_table.add_row([get_color_string(bcolors.GREEN,"Contacts_phone"),contractor.contacts_phone])
        contractor_table.add_row([get_color_string(bcolors.GREEN,"Address"),contractor.address])
        contractor_table.add_row([get_color_string(bcolors.GREEN,"Open_hours"),contractor.open_hours])
        contractor_table.add_row([get_color_string(bcolors.GREEN,"Review"),contractor.review])
        print(contractor_table.draw())

    def __edit_contractor(self, contractor):
        """This function runs if the user is a Manager and chooses to Edit contractor.
        The user chooses what to edit according to the available options.
        Args: 
            contractor (class instance): contractor model class"""
        
        while True:
            fieldnames = ["Name", "Type", "Contact", "Contact's phone", "Address", "Open_hours", "Review"]
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input(self.color_format.format('What do you want to change?'))
            try:
                col = int(col)
                newval = input(self.color_format.format(f'What is the new {fieldnames[col-1]}? '))
                setattr(contractor, fieldnames[col-1].lower(), newval)
                return self.llapi._edit_contractor(contractor)
            except:
                print('Invalid input, please try again')
