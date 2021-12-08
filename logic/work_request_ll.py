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
   
    # def list_work_requests(self):
    #     # return self.dlapi.list_work_requests()
    #     self.table.set_deco(Texttable.HEADER)
    #     self.table.set_max_width(300)
    #     workreq_list = self.dlapi.list_work_requests()
    #     for item in range(len(workreq_list)):
    #         workreq = workreq_list[item]
    #         # table.add_rows([["Nr","Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"], [item+1, workreq.workreport_id, workreq.title, workreq.property_id, workreq.destination_id, workreq.contractor, workreq.repeat, workreq.when, workreq.status, workreq.priority, workreq.description, workreq.workreport_id]])
    #         self.table.add_rows([["Nr","Workrequest_ID", "Title", "Status", "Priority"], [item+1, workreq.workrequest_id, workreq.title, workreq.status, workreq.priority]])
    #     print(self.table.draw())
    #     while True:
    #         command = input("Enter Nr of report to open or B to Back:").upper()
    #         if command == "B":
    #             return
    #         elif command.isdigit():
    #             nr = int(command)  
    #             try:
    #                 self.format_for_single_workrequest(workreq_list,nr)   
    #             except:
    #                 print("Nr out of range try again")
    #         else:
    #             print("Invalid input, try again!")
    #         self.table.reset()

    def workrequests_by_status(self):
        """Prints a table of all request baised on their status. Requests that are ready to be closed
        are open and have a report signed to them."""
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_requests()
        while True:
            status = input('Enter status: ').lower()
            retlist = []
            if status == 'ready for closing':
                for row in reader_report:
                    for line in reader_request:
                        if row.workreport_id == line.workreport_id and line.status == status:
                            retlist.append(line)
            else:
                for line in reader_request:
                    if line.status == status:
                        retlist.append(line)
            if retlist:
                self.list_works(retlist)
                return True
            else:
                print('No {} work request found.\nPlease enter "open", "closed", "ready for closing" or "completed".'.format(status))


    def list_work_requests(self):
        """Prints all work request in the system"""
        workreq_list = self.dlapi.list_work_requests()
        retlist = []
        for item in workreq_list:
            retlist.append(item)
        if retlist:
            self.list_works(retlist)
            return True
        else:
            print('No request registered in the system')


    def create_work_request(self,workreq):
        """Creates new work requests"""
        self.dlapi.create_work_request(WorkRequest(workreq))


    def edit_work_request(self, req):
        """Edits workrequest"""
        while True:
            id = req.workrequest_id
            fieldnames = ['Title', 'Property_ID', 'Destination', 'Contractor', 'Date', 'Status', 'Priority', 'Description']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                return self.dlapi.edit_work_request(id,col,newval)
            except:
                print('Invalid input, try again!')

    def search_work_request_id(self):
        """Returns workrequests baised on their id"""
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
        """Returns workrequests baised on the property they are assigned to"""
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
        """Returns workrequests baised on the ssn of the employee that worked on the associated report"""
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
                    if row.workreport_id == line.workreport_id:
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

    # def get_all_work_requests_by_status(self, status):
    #     the_list = []
    #     reader = self.dlapi.list_work_requests()
    #     for row in reader:
    #         if status == row.status:
    #             the_list.append(row)
    #     return the_list

    def format_for_single_workrequest(self,retlist,nr):
        for item in range(len(retlist)):
            workreq = retlist[item]
            if item+1 == nr:
                # self.item = nr
                self.table2.add_row(["No.",nr])
                self.table2.add_row(["Workrequest_ID",workreq.workrequest_id])
                self.table2.add_row(["Title",workreq.title])
                self.table2.add_row(["Property_ID",workreq.property_id])
                self.table2.add_row(["Destination",workreq.destination])
                self.table2.add_row(["Contractor",workreq.contractor])
                self.table2.add_row(["Date",workreq.date])
                self.table2.add_row(["Status",workreq.status])
                self.table2.add_row(["Priority",workreq.priority])
                self.table2.add_row(["Description",workreq.description])
                self.table2.add_row(["Workreport ID",workreq.workreport_id])
                print(self.table2.draw())
            self.table2.reset()
        
    def list_works(self,retlist):
        # return self.dlapi.list_work_requests()
        self.table.set_deco(Texttable.HEADER)
        self.table.set_max_width(300)
        self.table.reset()
        workreq_list = self.dlapi.list_work_requests()
        for item in range(len(retlist)):
            workreq = retlist[item]
            # list_from_table.append(workreq)
            # table.add_rows([["Nr","Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"], [item+1, workreq.workreport_id, workreq.title, workreq.property_id, workreq.destination_id, workreq.contractor, workreq.repeat, workreq.when, workreq.status, workreq.priority, workreq.description, workreq.workreport_id]])
            self.table.add_rows([["No.","Workrequest_ID", "Title", "Date", "Status", "Priority"], [item+1, workreq.workrequest_id, workreq.title, workreq.date, workreq.status, workreq.priority]])
        print(self.table.draw())
        while True:
            command = input("Enter No. of report to open or B to Back:").upper()
            if command == "B":
                return
            elif command.isdigit():
                nr = int(command)
                self.format_for_single_workrequest(retlist,nr)
            else:
                print("Invalid input, try again!")
            self.table.reset()
    
    def get_new_id(self):
        last_id = self.dlapi.find_last_id()
        new_id = int(last_id[1:])+1
        return f'w{new_id}'
