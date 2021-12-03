class WorkReport:
        def __init__(self,workreport_id,ssn,contractor,contractor_review,contractor_remuneration,total_cost,description,approved = False):
                self.workreport_id = workreport_id
                self.ssn = ssn
                self.contractor = contractor 
                self.contractor_review = contractor_review
                self.contractor_remuneration = contractor_remuneration
                self.total_cost = total_cost
                self.description = description
                self.approved = approved

        def __str__(self):
                return f"""Workreport_ID: {self.workreport_id} 
SSN: {self.ssn}
Contractor: {self.contractor}
Contractor_review: {self.contractor_review}
Contractor_remuneration: {self.contractor_remuneration}
Total_cost: {self.total_cost}
Desctiption: {self.description}
Approved: {self.approved}"""


            
    