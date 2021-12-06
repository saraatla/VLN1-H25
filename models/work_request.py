class WorkRequest:
    def __init__(self, parameters):
        self.workrequest_id = parameters[0]
        self.title = parameters[1]
        self.property_id = parameters[2]
        self.destination_id = parameters[3]
        self.contractor = parameters[4]
        self.repeat = parameters[5]
        self.when = parameters[6]
        self.status = parameters[7]
        self.priority = parameters[8]
        self.description = parameters[9]
        self.workreport_id = parameters[10]

    def __str__(self):
        return f"Workrequest_ID: {self.workrequest_id}, Title: {self.title}, Property_ID: {self.property_id}, Destination_ID: {self.destination_id}, Contractor: {self.contractor}, Repeat: {self.repeat}, When: {self.when}, Status: {self.status}, Priority: {self.priority}, Description: {self.description}"





