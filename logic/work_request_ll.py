from data.DLAPI import DLAPI
from models.work_request import WorkRequest
from datetime import datetime

class WorkRequestLL:
    """Work Request logic layer class; Contains 11 functions: fetches the functions in the data layer API,
    lists work requests on a specific period or not according to the users choice, lists all information about a work request 
    chosen by user, lists work requests by status chosen by user, creates the id for a new work request.
    Args:
        destination (str): destination chosen by user"""
        
    def __init__(self, destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)
   

    def _workrequests_by_status(self, status, destination): 
        """Prints a table of all request baised on their status. Requests that are ready to be closed
        are open and have a report signed to them
        Args:
            status (str): status of work request input by user
            destination (str): destination chosen by user
        Returns:
            request_list (list): list 
        
        """
        reader_report = self.dlapi._list_work_reports()
        reader_request = self.dlapi._list_work_requests()
        request_list = []
        if status == 'ready for closing':
            for report in reader_report:
                for request  in reader_request:
                    if report.workreport_id == request.workreport_id and request.status == 'open':
                        if destination == 'All destinations' or destination == request.destination:
                            request_list.append(request)
        else:
            for request in reader_request:
                if request.status == status:
                    if destination == 'All destinations' or destination == request.destination:
                        request_list.append(request)
        return request_list
       

    def _list_all_work_requests(self, destination):
        """This function lists work requests according to destination.
        Args:
            destination (str) : destination chosen by user
        Returns:
            request_list (list): list of work requests in given destination"""
        request_list = []
        for request in self.dlapi._list_work_requests():
            if destination == 'All destinations' or destination == request.destination:
                request_list.append(request)
        return request_list


    def _create_work_request(self,workrequest):
        """Creates new work requests"""
        self.dlapi._create_work_request(WorkRequest(workrequest))


    def _edit_work_request(self, workrequest):
        """Edits work request info"""
        return self.dlapi._edit_work_request(workrequest)


    def _search_work_request_id(self, workreq_id, destination):
        """This function searches for a work request by it's id in list of all work requests.
        Args:
            workreq_id (str): work request id input by user
            destination (str) : destination chosen by user
        Returns: 
            request (class instance): work request model class, or
            None"""
        reader = self.dlapi._list_work_requests()
        for request in reader:
            if request.workrequest_id == workreq_id:
                if destination == 'All destinations' or destination == request.destination:
                    return request
        return None     


    def _search_work_request_prop(self, prop_id, destination):
        """This function returns workrequests based on the property they are assigned to
        Args:
            prop_id (str): property id input by user
            destination (str) : destination chosen by user
        Returns: 
            request_list (list): list of work requests according to property id"""
        reader = self.dlapi._list_work_requests()
        request_list = []
        for request in reader:
            if request.property_id == prop_id:
                if destination == 'All destinations' or destination == request.destination:
                    request_list.append(request)
        return request_list


    def _search_work_request_ssn(self, ssn, destination):
        """This function returns work requests based on the ssn of the employee that worked on the associated report
        Args:
            ssn (str): ssn input by user
            destination (str) : destination chosen by user
        Returns: 
            request_list (list): list of work requests according to ssn"""
        reader_report = self.dlapi._list_work_reports()
        reader_request = self.dlapi._list_work_requests()
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


    def _search_work_request_cont(self, cont_id, destination):
        """This function returns work requests based on the contractor that worked with the employee who wrote
        the workreport.
        Args:
            cont_id (str): contractor id input by user
            destination (str) : destination chosen by user
        Returns: 
            request_list (list): list of work requests according to contractor id"""
        reader_report = self.dlapi._list_work_reports()
        reader_request = self.dlapi._list_work_requests()
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

    def _get_new_request_id(self):
        """This function finds the last workrequest id and returns the next one 
        if a new one is made.
        Returns:
            the next work request id (str)"""
        last_id = self.dlapi._find_last_request_id()
        new_id = int(last_id[1:])+1
        return f'w{new_id}'

    def _get_list_of_workreq_on_period(self,request_list,start_date,end_date):
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



    