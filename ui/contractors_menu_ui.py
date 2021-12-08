from Extra.texttableFile.texttable import Texttable
from Extra.acci import contAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI

LINE = '------------------------------------------'

class ContractorMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
        contAscii()
        while True:
            operations =  ['Search by ID', 'See list']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'Contractors in {self.destination}\nChoose options',operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            if operation  == 'Search by ID':
                search = input('Enter contractor ID: ')
                found_contractor = self.llapi.search_contractor(search)
                if found_contractor is None:
                    print(f'{LINE}\nContractor not found\n{LINE}')
                else:
                    self.individual_contractor_ui(found_contractor)

            elif operation == 'See list':
                cont_list = self.list_contractors()
                while True:
                    command = input("Enter number of contractor to open or B to Back:").upper()
                    if command == "B":
                        return
                    if not command.isdigit():
                        print("Invalid input, try again!")
                    else:
                        nr = int(command)
                        for index, contractor in enumerate(cont_list):
                            if index+1 == nr:
                                self.individual_contractor_ui(contractor,nr)
                        break

            elif operation == 'Add new':
                self.create_contractor()
                print(f'{LINE}\nContractor successfully created!\n{LINE}')


    def create_contractor(self):
        print('Enter the following information: ')
        print(LINE)
        new_id = self.llapi.get_new_cont_id()
        cont = [new_id]
        fieldnames = ["Name", "Type", "Contact", "Contact's phone", "Address", "Open_hours", "Review"]
        for field in fieldnames:
            val = input(f'{field}: ')
            cont.append(val)
        return self.llapi.create_contractor(cont)

    def list_contractors(self):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(118)
        cont_list = self.llapi.list_contractors(self.destination)
        for item in range(len(cont_list)):
            cont = cont_list[item]
            self.table.add_rows([["Number", "Contractor_ID", "Name", "Type", "Contact", "Contact's phone", "Address", "Open_hours", "Review"], 
            [item+1, cont.id, cont.name, cont.type, cont.contact, cont.contacts_phone, cont.address, cont.open_hours, cont.review]])
        print(table.draw())
        return cont_list

    def individual_contractor_ui(self, contractor, nr=None):
        self.print_contractor_table(contractor, nr)
        if self.user_type == 'Employee':
            return
        while True:
            print("1: Edit\nB: Back")
            print(LINE)
            command = input("Choose Options edit or back: ").upper()
            print(LINE)
            if command == "1":
                self.edit_contractor(contractor)
                self.print_contractor_table(contractor)
            elif command == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)

    def print_contractor_table(self, contractor, nr=None):
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

    def edit_contractor(self, cont):
        while True:
            fieldnames = ["Name", "Type", "Contact", "Contact's phone", "Address", "Open_hours", "Review"]
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                setattr(cont, fieldnames[col-1].lower(), newval)
                return self.llapi.edit_contractor(cont)
            except:
                print('Invalid input, try again!')
