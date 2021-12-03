class WorkRequest:
    def __init__(self,workrequest_id, title, property_id, destination_id, contractor, repeat, when, status, priority, description, workreport_id):
        self.workrequest_id = workrequest_id
        self.title = title
        self.property_id = property_id
        self.destination_id = destination_id
        self.contractor = contractor
        self.repeat = repeat
        self.when = when
        self.status = status
        self.priority = priority
        self.description = description
        self.workreport_id = workreport_id

    def __str__(self):
        return f"Workrequest_ID: {self.workrequest_id}, Title: {self.title}, Property_ID: {self.property_id}, Destination_ID: {self.destination_id}, Contractor: {self.contractor}, Repeat: {self.repeat}, When: {self.when}, Status: {self.status}, Priority: {self.priority}, Description: {self.description}"





