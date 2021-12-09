from data.DLAPI import DLAPI
from models.work_report import WorkReport
 
class WorkReportLL:
    """Work Report logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    APPROVED_INDEX = 7

    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)


    def list_work_reports(self):
        return self.dlapi.list_work_reports()


    def edit_work_report(self, rep):
        return self.dlapi.edit_work_report(rep)
    

    def search_work_report(self, search):
        reader = self.list_work_reports()
        for row in reader:
            if search == row.workreport_id:
                return row
        return False


    def approve_report(self, workreport_id):
        reader = self.list_work_reports()
        i = 0
        for row in reader:
            if workreport_id == row.workreport_id:
                self.dlapi.edit_work_report(i, self.APPROVED_INDEX, True)
                return 'Report has been marked approved!'
            i += 1    
        return 'No report found'


    def create_report(self, work_rep):
        return self.dlapi.create_work_report(WorkReport(work_rep))


    def get_new_id(self):
        last_id = self.dlapi.find_last_report_id()
        new_id = int(last_id[4:])+1
        return f'wrep{new_id}'