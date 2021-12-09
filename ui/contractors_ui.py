from Extra.texttableFile.texttable import Texttable
from Extra.acci import contAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI
from Extra.TermcolorFile.termcolor import colored, cprint
LINE = '------------------------------------------'

class ContractorUI:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.destination_collor = colored(self.destination, 'blue' ,attrs=['bold', 'underline'])
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type
        self.table = Texttable

    def _contractor_menu_start(self):
        contAscii()
        while True:
            operations =  ['Search by ID', 'See list']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'Contractors in {self.destination_collor}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            if operation  == 'Search by ID':
                search = input(colored('Enter contractor ID: ','green' ,attrs=['bold', 'underline']))
                found_contractor = self.llapi._search_contractor(search)
                if found_contractor is None:
                    print(f'{LINE}\nContractor not found\n{LINE}')
                else:
                    self.__individual_contractor_ui(found_contractor)

            elif operation == 'See list':
                cont_list = self.__list_contractors()
                while True:
                    command = input(colored("Enter number of contractor to open or B to Back: ",'green' ,attrs=['bold', 'underline'])).upper()
                    if command == "B":
                        return
                    if not command.isdigit():
                        print("Invalid input, try again!")
                    else:
                        nr = int(command)
                        for index, contractor in enumerate(cont_list):
                            if index+1 == nr:
                                self.__individual_contractor_ui(contractor,nr)
                        break

            elif operation == 'Add new':
                self.__create_contractor()
                print(f'{LINE}\nContractor successfully created!\n{LINE}')


    def __create_contractor(self):
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
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(160)
        cont_list = self.llapi._list_contractors()
        for item in range(len(cont_list)):
            cont = cont_list[item]
            table.add_rows([["Number", "Contractor_ID", "Name", "Type", "Contact", "Contact's phone", "Address", "Open_hours", "Review"], 
                                [item+1, cont.id, cont.name, cont.type, cont.contact, cont.contacts_phone, cont.address, cont.open_hours, cont.review]])
        print(table.draw())
        return cont_list

    def __individual_contractor_ui(self, contractor, nr=None):
        self.__print_contractor_table(contractor, nr)
        while True:
            if self.user_type == 'Employee':
                    command = input("Press B for back: ").upper()
                    print(LINE)
                    if command == "B":
                        return
                    else:
                        print("Invalid option, try again ")
                        print(LINE)
            else:
                print("1: Edit\nB: Back")
                print(LINE)
                command = input("Choose Options edit or back: ").upper()
                print(LINE)
                if command == "1":
                    self.__edit_contractor(contractor)
                    self.__print_contractor_table(contractor)
                elif command == "B":
                    return
                else:
                    print("Invalid option, try again ")
                    print(LINE)

    def __print_contractor_table(self, contractor, nr=None):
        contractor_table = Texttable()
        if nr is not None:
            contractor_table.add_row(["Number",nr])
        contractor_table.add_row(["ID",contractor.id])
        contractor_table.add_row(["Name",contractor.name])
        contractor_table.add_row(["Type",contractor.type])
        contractor_table.add_row(["Contact",contractor.contact])
        contractor_table.add_row(["Contacts_phone",contractor.contacts_phone])
        contractor_table.add_row(["Address",contractor.address])
        contractor_table.add_row(["Open_hours",contractor.open_hours])
        contractor_table.add_row(["Review",contractor.review])
        print(contractor_table.draw())

    def __edit_contractor(self, cont):
        while True:
            fieldnames = ["Name", "Type", "Contact", "Contact's phone", "Address", "Open_hours", "Review"]
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                setattr(cont, fieldnames[col-1].lower(), newval)
                return self.llapi._edit_contractor(cont)
            except:
                print('Invalid input, try again!')
