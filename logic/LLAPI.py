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
        self.destinations = DestinationLL(self.destination)
        self.employeeLL  = EmployeeLL(self.destination)
        self.propertyLL = PropertyLL(self.destination)
        self.contractorLL  = ContractorLL(destination)
        self.work_requestLL = WorkRequestLL(self.destination)
        self.work_reportLL = WorkReportLL(self.destination)

    # destination LL
    
    def destination_dict(self):
        return self.destinations.destination_dict()
    
    def list_of_destinations(self):
        return self.destinations.list_of_destinations()

    # Employee LL
    def create_employee(self):
        return self.employeeLL.create_employee()

    def list_employees(self):
        return self.employeeLL.list_employees()

    def search_employee(self, emp=''):
        return self.employeeLL.search_employee(emp)

    def edit_employee(self,emp):
        return self.employeeLL.edit_employee(emp)

    # Property LL
    def create_property(self):
        return self.propertyLL.create_property()

    def list_properties(self):
        return self.propertyLL.list_properties()

    def search_property(self,prop=''):
        return self.propertyLL.search_property(prop)

    def edit_property(self,prop):
        return self.propertyLL.edit_property(prop)

    # Contractor LL
    def create_contractor(self):
        return self.contractorLL.create_contractor()

    def list_contractors(self):
        return self.contractorLL.list_contractors()

    def search_contractor(self,cont=''):
        return self.contractorLL.search_contractor(cont)

    def edit_contractor(self,id):
        return self.contractorLL.edit_contractor(id)

    # Work Request LL
    def create_work_request(self, work_req):
        return self.work_requestLL.create_work_request(work_req)

    def list_work_requests(self):
        return self.work_requestLL.list_work_requests()
    
    def get_all_work_requests_by_status(self, status):
        return self.work_requestLL.get_all_work_requests_by_status(status)

    def search_work_requests_id(self):
        return self.work_requestLL.search_work_request_id()

    def search_work_requests_prop(self):
        return self.work_requestLL.search_work_request_prop()

    def search_work_requests_cont(self):
        return self.work_requestLL.search_work_request_cont()

    def edit_work_request(self,work_req):
        return self.work_requestLL.edit_work_request(work_req)

    def search_work_request_ssn(self):
        return self.work_requestLL.search_work_request_SSN()

    # Work Report LL
    def create_report(self, work_rep):
        return self.work_reportLL.create_report(work_rep)

    def list_work_reports(self):
        return self.work_reportLL.list_work_reports()

    def search_work_report(self,work_rep):
        return self.work_reportLL.search_work_report(work_rep)

    def edit_work_report(self,work_rep):
        return self.work_reportLL.edit_work_report(work_rep)

    def approve_report(self, workreport_id):
        return self.work_reportLL.approve_report(workreport_id)

    
        

