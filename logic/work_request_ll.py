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

    def list_work_requests(self):
        # return self.dlapi.list_work_requests()
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(118)
        workreq_list = self.dlapi.list_work_requests()
        for item in range(len(workreq_list)):
            workreq = workreq_list[item]
            self.table.add_rows([["Nr","Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor_ID", "Repeat", "When", "Status", "Priority", "Workreport_ID"], [item+1, workreq.workreport_id, workreq.title, workreq.property_id, workreq.destination_id, workreq.contractor, workreq.repeat, workreq.when, workreq.status, workreq.priority, workreq.workreport_id]])
        print(self.table.draw())
        while True:
            print(LINE)
            command = input("Enter B to go back:").upper()
            if command == "B":
                return
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
        for row in reader:
            if search == row.workrequest_id:
                return row
        return False

    def search_work_request_prop(self):
        reader = self.dlapi.list_work_requests()
        search = input('Enter property ID: ')
        retlist = []
        for row in reader:
            if search == row.property_id:
                retlist.append(row)
        if retlist:
            self.print_resaults(retlist)
        else:
            return False

    def search_work_request_SSN(self):
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_reports()
        search = input('Enter SSN: ')
        ssn_list = []
        for row in reader_report:
            if search == row.ssn:
                ssn_list.append(row)
        if ssn_list:
            retlist = []
            for row in ssn_list:
                for line in reader_request:
                    if row.workreport_id == line.workreport_id:
                        retlist.append(line)
            self.print_resaults(retlist)
        else:
            return False

    def search_work_request_cont(self):
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_reports()
        search = input('Enter contractor ID: ')
        contr_list = []
        for row in reader_report:
            if search == row.contractor:
                contr_list.append(row)
        if contr_list:
            retlist = []
            for row in contr_list:
                for line in reader_request:
                    if row.workreport_id == line.workreport_id:
                        retlist.append(line)
            self.print_resaults(retlist)
        else:
            return False

    def get_all_work_requests_by_status(self, status):
        the_list = []
        reader = self.dlapi.list_work_requests()
        for row in reader:
            if status == row.status:
                the_list.append(row)
        return the_list

    def print_resaults(self, retlist):
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(118)
        for item in range(len(retlist)):
            req = retlist[item]
            self.table.add_rows([["no.", "Workrequest ID", "Title", "Date", "Status", "Priority"], [item+1,req.workrequest_id, req.title, req.date, req.status, req.priority]])
        print(self.table.draw())
