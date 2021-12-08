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
    
    def search_destination(self, dest):
        return self.destinations.search_destination(dest)

    # Employee LL
    def create_employee(self, emp):
        return self.employeeLL.create_employee(emp)

    def list_employees(self, destination):
        return self.employeeLL.list_employees(destination)

    def search_employee(self, ssn, destination):
        return self.employeeLL.search_employee(ssn, destination)
    
    def edit_employee(self,emp):
        return self.employeeLL.edit_employee(emp)


    # Property LL
    def create_property(self, prop):
        return self.propertyLL.create_property(prop)

    def list_properties(self, destination):
        return self.propertyLL.list_properties(destination)

    def search_property(self, id, destination):
        return self.propertyLL.search_property(id, destination)

    def edit_property(self,prop):
        return self.propertyLL.edit_property(prop)

    # Contractor LL
    def create_contractor(self, cont):
        return self.contractorLL.create_contractor(cont)

    def list_contractors(self):
        return self.contractorLL.list_contractors()

    def search_contractor(self,cont):
        return self.contractorLL.search_contractor(cont)

    def edit_contractor(self,id):
        return self.contractorLL.edit_contractor(id)

    def get_new_cont_id(self):
        return self.contractorLL.get_new_cont_id()


    # Work Request LL
    def create_work_request(self, work_req):
        return self.work_requestLL.create_work_request(work_req)

    def list_all_work_requests(self, destination):
        return self.work_requestLL.list_all_work_requests(destination)
    
    def workrequests_by_status(self, status, destination):
        return self.work_requestLL.workrequests_by_status(status, destination)

    def search_work_requests_id(self, id, destination):
        return self.work_requestLL.search_work_request_id(id, destination)

    def search_work_requests_prop(self, id, destination):
        return self.work_requestLL.search_work_request_prop(id, destination)

    def search_work_requests_cont(self, id, destination):
        return self.work_requestLL.search_work_request_cont(id, destination)

    def edit_work_request(self,work_req):
        return self.work_requestLL.edit_work_request(work_req)

    def search_work_request_ssn(self, ssn, destination):
        return self.work_requestLL.search_work_request_SSN(ssn, destination)
    
    def get_new_id(self):
        return self.work_requestLL.get_new_id()

    def get_list_of_workreq_on_period(self,request_list,start_date,end_date):
        return self.work_requestLL.get_list_of_workreq_on_period(request_list,start_date,end_date)

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

    
        

