class WorkReport:
        def __init__(self,ssn,contractor, contractor_review, contractor_remuneration, total_cost,description, approved = False):
                self.report_id
                self.ssn = ssn
                self.contractor = contractor 
                self.contractor_review = contractor_review
                self.contractor_remuneration = contractor_remuneration
                self.total_cost = total_cost
                self.description = description
                self.approved = approved

        def __str__(self):
                return f"Workrequest_ID: {self.workrequest_id}, Title: {self.title}, Property_ID: {self.property_id}, Destination_ID: {self.destination_id}, Contractor: {self.contractor}, Repeat: {self.repeat}, When: {self.when}, Status: {self.status}, Priority: {self.priority}, Description: {self.description}"


            
    