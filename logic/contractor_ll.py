from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.contractor_model import Contractor
LINE = '------------------------------------------'

class ContractorLL:
    """Contractor logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,destination):
        self.dlapi = DLAPI(destination)
        self.table = Texttable()

    def list_contractors(self):
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(118)
        cont_list = self.dlapi.list_contractors()
        for item in range(len(cont_list)):
            cont = cont_list[item]
            self.table.add_rows([["Nr","Name","Type","Contact","Contact's phone","Address","Open_hours","Review"], [item+1,cont.name, cont.type, cont.contact, cont.contacts_phone, cont.address, cont.open_hours, cont.review]])
        print(self.table.draw())
        while True:
            print(LINE)
            command = input("Enter B to go back:").upper()
            if command == "B":
                return
            else:
                print("Invalid input, try again!")

    def create_contractor(self):
        print('Enter the following information: ')
        print(LINE)
        cont = []
        fieldnames = ["Name","Type","Contact","Contact's phone","Address","Open_hours","Review"]
        for field in fieldnames:
            val = input(f'{field}: ')
            cont.append(val)
        self.dlapi.create_contractor(Contractor(cont))
        print(f'{LINE}\nContractor successfully created!\n{LINE}')


    def edit_contractor(self, cont):
        while True:
            cont_name = cont.name
            fieldnames = ["Name","Type","Contact","Contact's phone","Address","Open_hours","Review"]
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                col = col-1
                return self.dlapi.edit_contractor(cont_name, col, newval)
            except:
                print('Invalid input, try again!')

    def search_contractor(self, search):
        while True:
            if search == '':
                search = input('Enter name: ')
            reader = self.dlapi.list_contractors()
            for row in reader:
                if search == row.name:
                    return row
                else:
                    print(f'{LINE}\nContractor not found\n{LINE}')
                    return
