from os import read
from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.work_request import WorkRequest
from datetime import datetime,date
LINE = '------------------------------------------'

class WorkRequestLL:
    """Work Request logic layer class; Contains 11 functions: fetches the functions in the data layer API,"""
    def __init__(self, destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)
        self.table = Texttable()
        self.table2 = Texttable()
   

    def workrequests_by_status(self, status, destination): 
        """Prints a table of all request baised on their status. Requests that are ready to be closed
        are open and have a report signed to them
        Args:
        
        Returns:
        
        """
        reader_report = self.dlapi.list_work_reports()
        reader_request = self.dlapi.list_work_requests()
        request_list = []
        if status == 'ready for closing':
            for row in reader_report:
                for line in reader_request:
                    if row.workreport_id == line.workreport_id and line.status == 'open':
                        if destination == 'All destinations' or destination == line.destination:
                            request_list.append(line)
        else:
            for line in reader_request:
                if line.status == status:
                    request_list.append(line)
        return request_list
       

    def list_all_work_requests(self, destination):
        """This function lists work requests according to destination.
        Args:
            destination (str) : destination chosen by user
        Returns:
            request_list (list): list of work requests in given destination"""
        request_list = []
        for request in self.dlapi.list_work_requests():
            if destination == 'All destinations' or destination == request.destination:
                request_list.append(request)
        return request_list


    def create_work_request(self,workrequest):
        """Creates new work requests"""
        self.dlapi.create_work_request(WorkRequest(workrequest))


    def edit_work_request(self, workrequest):
        """Edits work request info"""
        return self.dlapi.edit_work_request(workrequest)


    def search_work_request_id(self, workreq_id, destination):
        """This function searches for a work request by it's id in list of all work requests.
        Args:
            workreq_id (str): work request id input by user
            destination (str) : destination chosen by user
        Returns: 
            request (class instance): work request model class, or
            None"""
        reader = self.dlapi.list_work_requests()
        for request in reader:
            if request.workrequest_id == workreq_id:
                if destination == 'All destinations' or destination == request.destination:
                    return request
        return None     


    def search_work_request_prop(self, prop_id, destination):
        """This function returns workrequests based on the property they are assigned to
        Args:
            prop_id (str): property id input by user
            destination (str) : destination chosen by user
        Returns: 
            request_list (list): list of work requests according to property id"""
        reader = self.dlapi.list_work_requests()
        request_list = []
        for request in reader:
            if request.property_id == prop_id:
                if destination == 'All destinations' or destination == request.destination:
                    request_list.append(request)
        return request_list


    def search_work_request_ssn(self, ssn, destination):
        """This function returns work requests based on the ssn of the employee that worked on the associated report
        Args:
            ssn (str): ssn input by user
            destination (str) : destination chosen by user
        Returns: 
            request_list (list): list of work requests according to ssn"""
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
        """This function returns work requests based on the contractor that worked with the employee who wrote
        the workreport.
        Args:
            cont_id (str): contractor id input by user
            destination (str) : destination chosen by user
        Returns: 
            request_list (list): list of work requests according to contractor id"""
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

    def get_new_request_id(self):
        """This function finds the last workrequest id and returns the next one 
        if a new one is made.
        Returns:
            the next work request id (str)"""
        last_id = self.dlapi.find_last_request_id()
        new_id = int(last_id[1:])+1
        return f'w{new_id}'

    def get_list_of_workreq_on_period(self,request_list,start_date,end_date):
        """This function fetches a list of work requests on a period input by user
        Args:
            request_list (list): 
            start_date (str) : start date input by user
            end_date (str) : end date input by user
        Returns:
            request_list_by_date (list): list of workrequests for certain period"""
        if start_date == '' and end_date == '':
            request_list_by_date = request_list
            return request_list_by_date
        elif len(start_date) > 0 and len(end_date)>0:
            date_search_from = datetime.strptime(start_date,'%d/%m/%Y')
            date_search_to = datetime.strptime(end_date,'%d/%m/%Y')
            request_list_by_date = []
            for request in request_list:
                if date_search_from.date() <= request.date <= date_search_to.date():
                    request_list_by_date.append(request)
            return request_list_by_date
        return None



    