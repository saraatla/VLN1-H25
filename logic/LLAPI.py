from logic.location_ll import LocationLL
from logic.employee_ll import EmployeeLL
from logic.property_ll import PropertyLL
from logic.contractor_ll import ContractorLL
from logic.work_request_ll import Work_requestLL

class LLAPI:
    def __init__(self):
        self.locations = LocationLL()
        self.employeeLL  = EmployeeLL()
        self.propertyLL = PropertyLL()
        self.contractorLL  = ContractorLL()
        self.work_requestLL = Work_requestLL()

    def list_locations(self):
        return self.locations.list()

    # employee
    def create_employee(self, emp):
        return self.employeeLL.create_employee(emp)

    def list_employees(self):
        return self.employeeLL.list_employees()

    def search_employees(self,emp):
        return self.employeeLL.search_employees(emp)

    def edit_employee(self,emp):
        return self.employeeLL.edit_employee(emp)

    # property
    def create_property(self, prop):
        return self.propertyLL.create_property(prop)

    def list_properties(self):
        return self.propertyLL.list_properties()

    def search_properties(self,prop):
        return self.propertyLL.search_properties(prop)

    def edit_property(self,prop):
        return self.propertyLL.edit_property(prop)

    # work request
    def create_work_request(self, work_req):
        return self.work_requestLL.create_work_request(work_req)

    def list_work_requests(self):
        return self.work_requestLL.list_work_requests()

    def search_work_requests(self,work_req):
        return self.work_requestLL.search_work_requests(work_req)

    def edit_work_request(self,work_req):
        return self.work_requestLL.edit_work_request(work_req)

    # contractor
    def create_contractor(self, cont):
        return self.contractorLL.create_contractor(cont)

    def list_contractors(self):
        return self.contractorLL.list_contractors()

    def search_contractors(self,cont):
        return self.contractorLL.search_contractors(cont)

    def edit_contractor(self,cont):
        return self.contractorLL.edit_contractor(cont)


llapi = LLAPI()

    
        

