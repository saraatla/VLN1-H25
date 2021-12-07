class WorkReport:
        def __init__(self,parameters):
                self.workreport_id = parameters[0]
                self.ssn = parameters[1]
                self.contractor = parameters[2] 
                self.contractor_review = parameters[3]
                self.contractor_remuneration = parameters[4]
                self.total_cost = parameters[5]
                self.description = parameters[6]
                self.approved = parameters[7]
                self.manager_cmt = parameters[8]

        def __str__(self):
                return f"""Workreport_ID: {self.workreport_id} 
                SSN: {self.ssn}
                Contractor: {self.contractor}
                Contractor_review: {self.contractor_review}
                Contractor_remuneration: {self.contractor_remuneration}
                Total_cost: {self.total_cost}
                Desctiption: {self.description}
                Approved: {self.approved}
                Manager_comment: {self.manager_cmt}"""


            
    