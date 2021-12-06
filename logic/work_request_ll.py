from os import read
from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.work_request import WorkRequest
LINE = '------------------------------------------'

class WorkRequestLL:
    """Work Request logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self, destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)
        self.table = Texttable()
        self.table2 = Texttable()
   
    def list_work_requests(self):
        # return self.dlapi.list_work_requests()
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(180)
        workreq_list = self.dlapi.list_work_requests()
        for item in range(len(workreq_list)):
            workreq = workreq_list[item]
            # table.add_rows([["Nr","Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"], [item+1, workreq.workreport_id, workreq.title, workreq.property_id, workreq.destination_id, workreq.contractor, workreq.repeat, workreq.when, workreq.status, workreq.priority, workreq.description, workreq.workreport_id]])
            self.table.add_rows([["Nr","Workrequest_ID", "Title", "Date", "Status", "Priority"], [item+1, workreq.workrequest_id, workreq.title, workreq.date, workreq.status, workreq.priority]])
        print(self.table.draw())
        while True:
            command = input("Enter Nr of report to open or B to Back:").upper()
            if command == "B":
                return
            elif command.isdigit():
                nr = int(command)  
                try:
                    print(self.format_for_single_workrequest(nr))
                except:
                    print("Nr out of range try again")

            else:
                print("Invalid input, try again!")
   
    def create_work_request(self,work_req):
        # return self.dlapi.create_work_request(work_req)
        print('Enter the following information: ')
        print(LINE)
        workreq = []
        fieldnames = ["Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor_ID", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"]
        for field in fieldnames:
            val = input(f'{field}: ')
            workreq.append(val)
        self.dlapi.create_contractor(WorkRequest(workreq))
        print(f'{LINE}\nWork request successfully created!\n{LINE}')

    def edit_work_request(self, workreq):
        # return self.dlapi.edit_work_request(work_reqno,col,value)
        while True:
            workreq = input('Which contractor would you like to change?: ')
            fieldnames = ["Name","Type","Contact","Contact's phone","Address","Open_hours","Review"]
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                workreq = int(workreq)
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                col = col-1
                return self.dlapi.edit_work_request(workreq,col,newval)
            except:
                print('Invalid input, try again!')

    def search_work_request_id(self):
        reader = self.dlapi.list_work_requests()
        search = input('Enter request ID: ')
        retlist = []
        for row in reader:
            if search == row.workrequest_id:
                retlist.append(row)
        if retlist:
            self.list_works(retlist)
        else:
            return False

    def search_work_request_prop(self):
        reader = self.dlapi.list_work_requests()
        search = input('Enter property ID: ')
        retlist = []
        for row in reader:
            if search == row.property_id:
                retlist.append(row)
        if retlist:
            self.list_works(retlist)
        else:
            return False

    def search_work_request_SSN(self):
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_requests()
        search = input('Enter SSN: ')
        ssn_list = []
        for row in reader_report:
            if search == row.ssn:
                ssn_list.append(row)
        if ssn_list:
            retlist = []
            for row in ssn_list:
                for line in reader_request:
                    if row.workreport_id == line.workrequest_id:
                        retlist.append(line)
            self.list_works(retlist)
        else:
            return False

    def search_work_request_cont(self):
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_requests()
        search = input('Enter contractor ID: ')
        contr_list = []
        for row in reader_report:
            if search == row.contractor:
                contr_list.append(row)
        if contr_list:
            retlist = []
            for row in contr_list:
                for line in reader_request:
                    if row.workreport_id == line.workrequest_id:
                        retlist.append(line)
            self.list_works(retlist)
        else:
            return False

    def get_all_work_requests_by_status(self, status):
        the_list = []
        reader = self.dlapi.list_work_requests()
        for row in reader:
            if status == row.status:
                the_list.append(row)
        return the_list

    def format_for_single_workrequest(self,data):
        self.workreq_list = self.dlapi.list_work_requests()
        self.item = data-1
        workreq = self.workreq_list[self.item]
        self.table2.add_row(["Nr",self.item+1])
        self.table2.add_row(["Workrequest_ID",workreq.workrequest_id])
        self.table2.add_row(["Title",workreq.title])
        self.table2.add_row(["Property_ID",workreq.property_id])
        self.table2.add_row(["Destination_ID",workreq.destination_id])
        self.table2.add_row(["Contractor",workreq.contractor])
        self.table2.add_row(["Date",workreq.date])
        self.table2.add_row(["Status",workreq.status])
        self.table2.add_row(["Priority",workreq.priority])
        self.table2.add_row(["Description",workreq.description])
        self.table2.add_row(["Workreport ID",workreq.workreport_id])
        return self.table2.draw()
    


    def print_resaults(self, retlist):
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(118)
        for item in range(len(retlist)):
            req = retlist[item]
            self.table2.add_row(["Workrequest_ID",req.workrequest_id])
            self.table2.add_row(["Title",req.title])
            self.table2.add_row(["Property_ID",req.property_id])
            self.table2.add_row(["Destination_ID",req.destination_id])
            self.table2.add_row(["Contractor",req.contractor])
            self.table2.add_row(["Date",req.date])
            self.table2.add_row(["Status",req.status])
            self.table2.add_row(["Priority",req.priority])
            self.table2.add_row(["Description",req.description])
            self.table2.add_row(["Workreport ID",req.workreport_id])
        print(self.table2.draw())
        
    def list_works(self,retlist):
        # return self.dlapi.list_work_requests()
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(180)
        workreq_list = self.dlapi.list_work_requests()
        for item in range(len(retlist)):
            workreq = retlist[item]
            # table.add_rows([["Nr","Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"], [item+1, workreq.workreport_id, workreq.title, workreq.property_id, workreq.destination_id, workreq.contractor, workreq.repeat, workreq.when, workreq.status, workreq.priority, workreq.description, workreq.workreport_id]])
            self.table.add_rows([["Nr","Workrequest_ID", "Title", "Date", "Status", "Priority"], [item+1, workreq.workrequest_id, workreq.title, workreq.date, workreq.status, workreq.priority]])
        print(self.table.draw())
        while True:
            command = input("Enter Nr of report to open or B to Back:").upper()
            if command == "B":
                return
            elif command.isdigit():
                nr = int(command)  
                try:
                    print(self.format_for_single_workrequest(nr))
                except:
                    print("Nr out of range try again")

            else:
                print("Invalid input, try again!")