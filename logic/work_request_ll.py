from data.DLAPI import DLAPI

class WorkRequestLL:
    """Work Request logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,location):
        self.location = location
        self.dlapi = DLAPI(self.location)

    def list_work_requests(self):
        return self.dlapi.list_work_requests()
        
    def create_work_request(self,work_req):
        return self.dlapi.create_work_request(work_req)

    def edit_work_request(self,work_reqno,col,value):
        return self.dlapi.edit_work_request(work_reqno,col,value)

    def search_work_request(self, search):
        reader = self.dlapi.list_work_requests()
        for row in reader:
            if search == row.workrequest_id:
                return row
        return False

    def get_all_work_requests_by_status(self, status):
        the_list = []
        reader = self.dlapi.list_work_requests()
        for row in reader:
            if status == row.status:
                the_list.append(row)
        return the_list
