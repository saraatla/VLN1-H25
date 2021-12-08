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
   

    def workrequests_by_status(self, status, destination): 
        """Prints a table of all request baised on their status. Requests that are ready to be closed
        are open and have a report signed to them."""
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_requests()
        request_list = []
        if status == 'ready for closing':
            for row in reader_report:
                for line in reader_request:
                    if row.workreport_id == line.workreport_id and line.status == status:
                        if destination == 'All destinations' or destination == line.destination:
                            request_list.append(line)
        else:
            for line in reader_request:
                if line.status == status:
                    request_list.append(line)
        return request_list
       

    def list_all_work_requests(self, destination):
        """Prints all work request in the system according to destination"""
        request_list = []
        for request in self.dlapi.list_work_requests():
            if destination == 'All destinations' or destination == request.destination:
                request_list.append(request)
        return request_list


    def create_work_request(self,workreq):
        """Creates new work requests"""
        self.dlapi.create_work_request(WorkRequest(workreq))


    def edit_work_request(self, req):
        """Edits workrequest"""
        return self.dlapi.edit_work_request(req)
 


    def search_work_request_id(self, req_id, destination):
        """Returns workrequests based on their id"""
        reader = self.dlapi.list_work_requests()
        for request in reader:
            if request.workrequest_id == req_id:
                if destination == 'All destinations' or destination == request.destination:
                    return request
        return None     


    def search_work_request_prop(self, prop_id, destination):
        """Returns workrequests baised on the property they are assigned to"""
        reader = self.dlapi.list_work_requests()
        request_list = []
        for request in reader:
            if request.property_id == prop_id:
                if destination == 'All destinations' or destination == request.destination:
                    request_list.append(request)
        return request_list


    def search_work_request_SSN(self, ssn, destination):
        """Returns workrequests baised on the ssn of the employee that worked on the associated report"""
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_requests()
        report_list = []
        for report in reader_report:
            if report.ssn == ssn:
                report_list.append(report)
        request_list = []
        for report in report_list:
            for request in reader_request: 
                if report.workreport_id == request.workreport_id:
                    if destination == 'All destinations' or destination == request.destination:
                        request_list.append(request)
        return request_list


    def search_work_request_cont(self, cont_id, destination):
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_requests()
        report_list = []
        for report in reader_report:
            if report.contractor_id == cont_id:
                report_list.append(report)
        request_list = []
        for report in report_list:
            for request in reader_request: 
                if report.workreport_id == request.workreport_id:
                    if destination == 'All destinations' or destination == request.destination:
                        request_list.append(request)
        return request_list


    def get_new_id(self):
        last_id = self.dlapi.find_last_id()
        new_id = int(last_id[1:])+1
        return f'w{new_id}'
