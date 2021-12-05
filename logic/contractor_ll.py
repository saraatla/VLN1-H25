from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.employee_model import Employee
LINE = '------------------------------------------'

class ContractorLL:
    """Contractor logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,location):
        self.location = location
        self.dlapi = DLAPI(self.location)
        self.table = Texttable()

    def list_contractors(self):
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(118)
        cont_list = self.dlapi.list_contractors()
        for item in range(len(cont_list)):
            cont = cont_list[item]
            if cont.location == self.location:
                self.table.add_rows([["Nr","Name", "Type","Contact","Contact's phone","Address","Open_hours","Review"], [item+1,emp.name, emp.ssn, emp.email, emp.gsm, emp.location, emp.airport, emp.title]])
            elif self.location == "All locations":
                self.table.add_rows([["Nr","Name", "SSN","Email","Gsm","Location","Airport","Title"], [item+1,emp.name, emp.ssn, emp.email, emp.gsm, emp.location, emp.airport, emp.title]])
        print(self.table.draw())
        while True:
            print(LINE)
            command = input("Enter B to go back:").upper()
            if command == "B":
                return
            else:
                print("Invalid input, try again!")

    def create_contractor(self, cont):
        return self.dlapi.create_contractor(cont)

    def edit_contractor(self, contno, col, newvalue):
        return self.dlapi.edit_contractor(contno, col, newvalue)

    def search_contractor(self, search):

        reader = self.dlapi.list_contractors()
        for row in reader:
            if search == row.name:
                return row
        return False
