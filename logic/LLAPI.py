from logic.location_ll import LocationLL
from logic.employee_ll import EmployeeLL
from logic.property_ll import PropertyLL
from logic.contractor_ll import ContractorLL
from logic.work_request_ll import WorkRequestLL
from logic.work_report_ll import WorkReportLL

class LLAPI:
    """Logic Layer API fetches all the functions in the logic layer"""
    def __init__(self,location):
        self.location = location
        self.locations = LocationLL(self.location)
        self.employeeLL  = EmployeeLL(self.location)
        self.propertyLL = PropertyLL(self.location)
        self.contractorLL  = ContractorLL(self.location)
        self.work_requestLL = WorkRequestLL(self.location)
        self.work_reportLL = WorkReportLL(self.location)

    # Location LL
    def list_locations(self):
        return self.locations.list_locations()
    
    def location_dict(self):
        return self.locations.location_dict()
    
    def print_location(self):
        return self.locations.print_location()
    
    def list_of_locations(self):
        return self.locations.list_of_locations()

    # Employee LL
    def create_employee(self, emp):
        return self.employeeLL.create_employee(emp)

    def list_employees(self):
        return self.employeeLL.list_employees()

    def search_employee(self, emp=''):
        return self.employeeLL.search_employee(emp)

    def edit_employee(self,emp):
        return self.employeeLL.edit_employee(emp)

    # Property LL
    def create_property(self, prop):
        return self.propertyLL.create_property(prop)

    def list_properties(self):
        return self.propertyLL.list_properties()

    def search_property(self,prop=''):
        return self.propertyLL.search_property(prop)

    def edit_property(self,prop):
        return self.propertyLL.edit_property(prop)

    # Contractor LL
    def create_contractor(self, cont):
        return self.contractorLL.create_contractor(cont)

    def list_contractors(self):
        return self.contractorLL.list_contractors()

    def search_contractor(self,cont):
        return self.contractorLL.search_contractor(cont)

    def edit_contractor(self,cont):
        return self.contractorLL.edit_contractor(cont)

    # Work Request LL
    def create_work_request(self, work_req):
        return self.work_requestLL.create_work_request(work_req)

    def list_work_requests(self):
        return self.work_requestLL.list_work_requests()
    
    def get_all_work_requests_by_status(self, status):
        return self.work_requestLL.get_all_work_requests_by_status(status)

    def search_work_requests(self,work_req):
        return self.work_requestLL.search_work_request(work_req)

    def edit_work_request(self,work_req):
        return self.work_requestLL.edit_work_request(work_req)

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

    
        

