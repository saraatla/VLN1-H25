from data.destination_dl import DestinationDL
from data.employee_dl import EmployeeDL
from data.property_dl import PropertyDL
from data.contractor_dl import ContractorDL
from data.work_request_dl import WorkRequestDL
from data.work_report_dl import WorkReportDL

class DLAPI:
    """Data Layer API, fetches all the functions in the data layer"""
    def __init__(self, destination):
        self.destination = destination
        self.destinationDL = DestinationDL()
        self.employeeDL  = EmployeeDL(self.destination)
        self.propertyDL = PropertyDL(self.destination)
        self.contractorDL  = ContractorDL()
        self.work_requestDL = WorkRequestDL(self.destination)
        self.work_reportDL = WorkReportDL(self.destination)

    # destination DL
    def list_destinations(self):
        return self.destinationDL.list_destinations()
    
    # Employee DL
    def create_employee(self, emp):
        return self.employeeDL.create_employee(emp)

    def list_employees(self):
        return self.employeeDL.list_employees()

    def edit_employee(self,ssn,col,newval):
        return self.employeeDL.edit_employee(ssn,col,newval)

    # Property DL
    def create_property(self, prop):
        return self.propertyDL.create_property(prop)

    def list_properties(self):
        return self.propertyDL.list_properties()

    def edit_property(self,id,col,newval):
        return self.propertyDL.edit_property(id,col,newval)

    # Contractor DL
    def create_contractor(self, cont):
        return self.contractorDL.create_contractor(cont)

    def list_contractors(self):
        return self.contractorDL.list_contractors()

    def edit_contractor(self,id,col,newval):
        return self.contractorDL.edit_contractor(id,col,newval)

    # Work Request DL
    def create_work_request(self, work_req):
        return self.work_requestDL.create_work_request(work_req)

    def list_work_requests(self):
        return self.work_requestDL.list_work_requests()

    def edit_work_request(self,work_req):
        return self.work_requestDL.edit_work_request(work_req)

    def find_last_id(self):
        return 'w644' #self.work_requestDL.find_last_id()

    # Work Report DL
    def create_work_report(self, work_rep):
        return self.work_reportDL.create_work_report(work_rep)

    def list_work_reports(self):
        return self.work_reportDL.list_work_reports()

    def edit_work_report(self,work_rep):
        return self.work_reportDL.edit_work_report(work_rep)
