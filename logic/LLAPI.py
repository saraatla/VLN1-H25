from logic.destination_ll import DestinationLL
from logic.employee_ll import EmployeeLL
from logic.property_ll import PropertyLL
from logic.contractor_ll import ContractorLL
from logic.work_request_ll import WorkRequestLL
from logic.work_report_ll import WorkReportLL

class LLAPI:
    """Logic Layer API fetches all the functions in the logic layer"""
    def __init__(self,destination):
        self.destination = destination
        self.destinationLL = DestinationLL(self.destination)
        self.employeeLL  = EmployeeLL(self.destination)
        self.propertyLL = PropertyLL(self.destination)
        self.contractorLL  = ContractorLL(destination)
        self.work_requestLL = WorkRequestLL(self.destination)
        self.work_reportLL = WorkReportLL(self.destination)

    # Destination LL
    def _list_of_destinations(self):
        return self.destinationLL._list_of_destinations()
    
    def _search_destination(self, destination):
        return self.destinationLL._search_destination(destination)

    def create_destination(self, destination):
        return self.destinationLL.create_destination(destination)

    # Employee LL
    def create_employee(self, employee):
        return self.employeeLL.create_employee(employee)

    def list_employees(self, destination):
        return self.employeeLL.list_employees(destination)

    def _search_employee(self, ssn, destination):
        return self.employeeLL._search_employee(ssn, destination)
    
    def edit_employee(self,employee):
        return self.employeeLL.edit_employee(employee)

    # Property LL
    def create_property(self, property):
        return self.propertyLL.create_property(property)

    def list_properties(self, destination):
        return self.propertyLL.list_properties(destination)

    def _search_property(self, id, destination):
        return self.propertyLL._search_property(id, destination)

    def edit_property(self,property):
        return self.propertyLL.edit_property(property)

    # Contractor LL
    def create_contractor(self, contractor):
        return self.contractorLL.create_contractor(contractor)

    def list_contractors(self):
        return self.contractorLL.list_contractors()

    def _search_contractor(self,contractor):
        return self.contractorLL._search_contractor(contractor)

    def edit_contractor(self,cont_id):
        return self.contractorLL.edit_contractor(cont_id)

    def _get_new_cont_id(self):
        return self.contractorLL._get_new_cont_id()

    # Work Request LL
    def create_work_request(self, work_req):
        return self.work_requestLL.create_work_request(work_req)

    def _list_all_work_requests(self, destination):
        return self.work_requestLL._list_all_work_requests(destination)
    
    def _workrequests_by_status(self, status, destination):
        return self.work_requestLL._workrequests_by_status(status, destination)

    def _search_work_requests_id(self, workrequest_id, destination):
        return self.work_requestLL._search_work_request_id(workrequest_id, destination)

    def _search_work_requests_prop(self, prop_id, destination):
        return self.work_requestLL._search_work_request_prop(prop_id, destination)

    def _search_work_requests_cont(self, cont_id, destination):
        return self.work_requestLL._search_work_request_cont(cont_id, destination)

    def edit_work_request(self,work_request):
        return self.work_requestLL.edit_work_request(work_request)

    def _search_work_request_ssn(self, ssn, destination):
        return self.work_requestLL._search_work_request_ssn(ssn, destination)
    
    def _get_new_request_id(self):
        return self.work_requestLL._get_new_request_id()

    def _get_list_of_workreq_on_period(self,request_list,start_date,end_date):
        return self.work_requestLL._get_list_of_workreq_on_period(request_list,start_date,end_date)

    # Work Report LL
    def _create_report(self, work_rep):
        return self.work_reportLL._create_report(work_rep)

    def list_work_reports(self):
        return self.work_reportLL.list_work_reports()

    def _search_work_report(self,work_rep):
        return self.work_reportLL._search_work_report(work_rep)

    def edit_work_report(self,work_rep):
        return self.work_reportLL.edit_work_report(work_rep)
    
    def _get_new_report_id(self):
        return self.work_reportLL._get_new_id()

    
        

