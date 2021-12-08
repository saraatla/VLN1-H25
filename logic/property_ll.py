from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.property_model import Property
LINE = '------------------------------------------'

class PropertyLL:
    """Property logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)
        self.table = Texttable()
        self.table2 = Texttable()
    
    def list_properties(self):
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(300)
        prop_list = self.dlapi.list_properties()
        for item in range(len(prop_list)):
            prop = prop_list[item]
            if prop.destination == self.destination:
                self.table.add_rows([["Nr","Destination", "Address","Squarefoot","Rooms","Type","Property_ID","Facilites"], [item+1,prop.destination, prop.address, prop.squarefoot, prop.rooms, prop.type, prop.property_id, prop.facilities]])
            elif self.destination == "All destinations":
                self.table.add_rows([["Nr","Destination", "Address","Squarefoot","Rooms","Type","Property_ID","Facilites"], [item+1,prop.destination, prop.address, prop.squarefoot, prop.rooms, prop.type, prop.property_id, prop.facilities]])
        print(self.table.draw())
        self.table.reset()
        while True:
            command = input("Enter Nr of report to open or B to Back:").upper()
            if command == "B":
                return
            elif command.isdigit():
                nr = int(command)
                return self.format_for_single_workrequest(prop_list,nr)
            else:
                print("Invalid input, try again!")

    def format_for_single_workrequest(self,retlist,nr):

        if retlist:
            for item in range(len(retlist)):
                workreq = retlist[item]
                if item+1 == nr:
                    return self.get_table(workreq,nr),workreq ,nr


    def create_property(self):
        print('Enter the following information: ')
        print(LINE)
        prop = []
        fieldnames = ['Destination', 'Address', 'Squarefoot', 'Rooms', 'Type', 'Property_ID', 'Facilities']
        for field in fieldnames:
            val = input(f'{field}: ')
            prop.append(val)
        self.dlapi.create_property(Property(prop))
        print(f'{LINE}\nProperty successfully created!\n{LINE}')
 
    def get_table(self,workreq, nr=""):
        self.table2.reset()
        if nr:
            self.table2.add_row(["Nr",nr])
            self.table2.add_row(["Destination",workreq.destination])
            self.table2.add_row(["Address",workreq.address])
            self.table2.add_row(["Squarefoot",workreq.squarefoot])
            self.table2.add_row(["Rooms",workreq.rooms])
            self.table2.add_row(["Type",workreq.type])
            self.table2.add_row(["Property_id",workreq.property_id])
            self.table2.add_row(["Facilities",workreq.facilities])
            return self.table2.draw()
        else:
            self.table2.add_row(["Destination",workreq.destination])
            self.table2.add_row(["Address",workreq.address])
            self.table2.add_row(["Squarefoot",workreq.squarefoot])
            self.table2.add_row(["Rooms",workreq.rooms])
            self.table2.add_row(["Type",workreq.type])
            self.table2.add_row(["Property_id",workreq.property_id])
            self.table2.add_row(["Facilities",workreq.facilities])
            return self.table2.draw()


    def edit_property(self, prop):
        while True:
            id = prop.property_id
            fieldnames = ['Destination', 'Address', 'Squarefoot', 'Rooms', 'Type', 'Facilities']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                if col < 6:
                    col = col -1
                return self.dlapi.edit_property(id, col, newval)
            except:
                print('Invalid input, try again!')
            # #try:
            # col = int(col)
            # newval = input(f'What is the new {fieldnames[col-1]}? ')
            # if col < 6:
            #     col = col - 1
            # return self.dlapi.edit_property(id, col, newval)
            #except:
                #print('Invalid input, try again!')
        

    def search_property(self, search,nr=""):
        while True:
            reader = self.dlapi.list_properties()
            if nr:
                if search:
                    for row in reader:
                        # if self.destination == "All destinations":
                        #     if search == row.property_id:
                        #         return self.get_table(row,nr)
                        if row.destination == self.destination:
                            if search == row.property_id:
                                return self.get_table(row,nr)
            else:
                if search:
                    for row in reader:
                        if search == row.property_id:
                            return self.get_table(row)
                elif search == '':
                    search = input('Enter Property ID: ')
                    for row in reader:
                        if row.destination == self.destination:
                            if search == row.property_id:
                                return self.get_table(row)
                else:
                    print(f'{LINE}\nProperty not found\n{LINE}')
                    return

    # def search_property(self, search,nr=""):
    #     while True:
    #         if search == '':
    #             search = input('Enter Property ID: ')        
    #         reader = self.dlapi.list_properties()
    #         for row in reader:
    #             if self.destination == "All destinations":
    #                 if search == row.property_id:
    #                     return row
    #             elif row.destination == self.destination:
    #                 if search == row.property_id:
    #                     return row
    #             else:
    #                 print(f'{LINE}\nProperty not found\n{LINE}')
    #                 return
 

