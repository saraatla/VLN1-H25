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
    def list_of_destinations(self):
        return self.destinationLL.list_of_destinations()
    
    def search_destination(self, destination):
        return self.destinationLL.search_destination(destination)

    def create_destination(self, destination):
        return self.destinationLL.create_destination(destination)

    # Employee LL
    def create_employee(self, employee):
        return self.employeeLL.create_employee(employee)

    def list_employees(self, destination):
        return self.employeeLL.list_employees(destination)

    def search_employee(self, ssn, destination):
        return self.employeeLL.search_employee(ssn, destination)
    
    def edit_employee(self,employee):
        return self.employeeLL.edit_employee(employee)

    # Property LL
    def create_property(self, property):
        return self.propertyLL.create_property(property)

    def list_properties(self, destination):
        return self.propertyLL.list_properties(destination)

    def search_property(self, id, destination):
        return self.propertyLL.search_property(id, destination)

    def edit_property(self,property):
        return self.propertyLL.edit_property(property)
    
    def get_new_property_id(self, destination):
        return self.propertyLL.get_new_property_id(destination)

    # Contractor LL
    def create_contractor(self, contractor):
        return self.contractorLL.create_contractor(contractor)

    def list_contractors(self):
        return self.contractorLL.list_contractors()

    def search_contractor(self,contractor):
        return self.contractorLL.search_contractor(contractor)

    def edit_contractor(self,cont_id):
        return self.contractorLL.edit_contractor(cont_id)

    def get_new_cont_id(self):
        return self.contractorLL.get_new_cont_id()

    # Work Request LL
    def create_work_request(self, work_req):
        return self.work_requestLL.create_work_request(work_req)

    def list_all_work_requests(self, destination):
        return self.work_requestLL.list_all_work_requests(destination)
    
    def workrequests_by_status(self, status, destination):
        return self.work_requestLL.workrequests_by_status(status, destination)

    def search_work_requests_id(self, workrequest_id, destination):
        return self.work_requestLL.search_work_request_id(workrequest_id, destination)

    def search_work_requests_prop(self, prop_id, destination):
        return self.work_requestLL.search_work_request_prop(prop_id, destination)

    def search_work_requests_cont(self, cont_id, destination):
        return self.work_requestLL.search_work_request_cont(cont_id, destination)

    def edit_work_request(self,work_request):
        return self.work_requestLL.edit_work_request(work_request)

    def search_work_request_ssn(self, ssn, destination):
        return self.work_requestLL.search_work_request_ssn(ssn, destination)
    
    def get_new_request_id(self):
        return self.work_requestLL.get_new_request_id()

    def get_list_of_workreq_on_period(self,request_list,start_date,end_date):
        return self.work_requestLL.get_list_of_workreq_on_period(request_list,start_date,end_date)

    # Work Report LL
    def create_work_report(self, work_rep):
        return self.work_reportLL.create_work_report(work_rep)

    def list_work_reports(self):
        return self.work_reportLL.list_work_reports()

    def search_work_report(self,work_rep):
        return self.work_reportLL.search_work_report(work_rep)

    def edit_work_report(self,work_rep):
        return self.work_reportLL.edit_work_report(work_rep)
    
    def get_new_report_id(self):
        return self.work_reportLL.get_new_id()

    
        

