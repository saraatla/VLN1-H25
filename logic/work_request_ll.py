from data.DLAPI import DLAPI

class WorkRequestLL:
    def __init__(self):
        self.dlapi = DLAPI()

    def get_all_work_requests(self):
        return self.dlapi.get_all_work_requests()
        
    def create_work_request(self,work_req):
        return self.dlapi.create_work_request(work_req)

    def edit_work_request(self,work_reqno,col,value):
        return self.dlapi.edit_work_request(work_reqno,col,value)

    def search_work_request(self, search):
        reader = self.dlapi.get_all_work_requests()
        for row in reader:
            if search == row.workrequest_id:
                return row
        return False

    def get_all_work_requests_by_status(self, status):
        the_list = []
        reader = self.dlapi.get_all_work_requests()
        for row in reader:
            if status == row.status:
                the_list.append(row)
        return the_list
