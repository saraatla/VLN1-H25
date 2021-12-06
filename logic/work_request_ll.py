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
            self.table.add_rows([["Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"], [item+1, workreq.workreport_id, workreq.title, workreq.property_id, workreq.destination_id, workreq.contractor, workreq.repeat, workreq.when, workreq.status, workreq.priority, workreq.description, workreq.workreport_id]])
        print(self.table.draw())
        while True:
            print(LINE)
            command = input("Enter B to go back:").upper()
            if command == "B":
                return
            else:
                print("Invalid input, try again!")
    def create_work_request(self,work_req):
        return self.dlapi.create_work_request(work_req)

    def edit_work_request(self,work_reqno,col,value):
        return self.dlapi.edit_work_request(work_reqno,col,value)

    def search_work_request(self, search):
        reader = self.dlapi.list_work_requests()
        for row in reader:
            if search == row.workrequest_id:
                return row
        return False

    def get_all_work_requests_by_status(self, status):
        the_list = []
        reader = self.dlapi.list_work_requests()
        for row in reader:
            if status == row.status:
                the_list.append(row)
        return the_list
