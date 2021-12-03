from data.location_dl import LocationDL
from data.employee_dl import EmployeeDL
from data.property_dl import PropertyDL
from data.contractor_dl import ContractorDL
from data.work_request_dl import WorkRequestDL
from data.work_report_dl import WorkReportDL

class DLAPI:
    """Data Layer API, Fetching all the functions"""
    def __init__(self):
        self.locationDL = LocationDL()
        self.employeeDL  = EmployeeDL()
        self.propertyDL = PropertyDL()
        self.contractorDL  = ContractorDL()
        self.work_requestDL = WorkRequestDL()
        self.work_reportDL = WorkReportDL()

    # Location DL
    def list_locations(self):
        return self.locationDL.list_locations()
    
    # Employee DL
    def create_employee(self, emp):
        return self.employeeDL.create_employee(emp)

    def list_employees(self):
        return self.employeeDL.list_employees()

    def edit_employee(self,emp):
        return self.employeeDL.edit_employee(emp)

    # Property DL
    def create_property(self, prop):
        return self.propertyDL.create_property(prop)

    def list_properties(self):
        return self.propertyDL.list_properties()

    def edit_property(self,prop):
        return self.propertyDL.edit_property(prop)

    # Contractor DL
    def create_contractor(self, cont):
        return self.contractorDL.create_contractor(cont)

    def list_contractors(self):
        return self.contractorDL.list_contractors()

    def edit_contractor(self,cont):
        return self.contractorDL.edit_contractor(cont)

    # Work Request DL
    def create_work_request(self, work_req):
        return self.work_requestDL.create_work_request(work_req)

    def list_work_requests(self):
        return self.work_requestDL.list_work_requests()

    def edit_work_request(self,work_req):
        return self.work_requestDL.edit_work_request(work_req)

    # Work Report DL
    def create_work_report(self, work_req):
        return self.work_reportDL.create_work_report(work_req)

    def list_work_reports(self):
        return self.work_reportDL.list_work_reports()

    def edit_work_report(self,work_req):
        return self.work_reportDL.edit_work_report(work_req)

dlapi = DLAPI()
