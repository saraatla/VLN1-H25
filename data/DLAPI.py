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

    # Destination DL
    def list_destinations(self):
        return self.destinationDL.list_destinations()
    
    # Employee DL
    def _create_employee(self, emp):
        return self.employeeDL._create_employee(emp)

    def _list_employees(self):
        return self.employeeDL._list_employees()
    
    def _edit_employee(self,emp):
        return self.employeeDL._edit_employee(emp)

    # Property DL
    def _create_property(self, prop):
        return self.propertyDL._create_property(prop)

    def _list_properties(self):
        return self.propertyDL._list_properties()

    def _edit_property(self,prop):
        return self.propertyDL._edit_property(prop)

    # Contractor DL
    def _create_contractor(self, cont):
        return self.contractorDL._create_contractor(cont)

    def _list_contractors(self):
        return self.contractorDL._list_contractors()

    def _edit_contractor(self, contractor):
        return self.contractorDL._edit_contractor(contractor)

    # Work Request DL
    def _create_work_request(self, work_req):
        return self.work_requestDL._create_work_request(work_req)

    def _list_work_requests(self):
        return self.work_requestDL._list_work_requests()

    def _edit_work_request(self,work_req):
        return self.work_requestDL._edit_work_request(work_req)

    def _find_last_request_id(self):
        return self.work_requestDL._find_last_request_id()

    # Work Report DL
    def _create_work_report(self, work_rep):
        self.work_reportDL._create_work_report(work_rep)
        return work_rep

    def _list_work_reports(self):
        return self.work_reportDL._list_work_reports()

    def _edit_work_report(self,work_rep):
        return self.work_reportDL._edit_work_report(work_rep)
    
    def _find_last_report_id(self):
        return self.work_reportDL._find_last_report_id()
