from data.DLAPI import DLAPI
from models.work_report import WorkReport
 
class WorkReportLL:
    """Work Report logic layer class; Contains 6 functions: fetches the functions in the data layer API,
    lists information of work report, creates the id for a new work report.
    Args: 
        destination (str): destination chosen by user"""

    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)


    def list_work_reports(self):
        return self.dlapi.list_work_reports()


    def edit_work_report(self, rep):
        return self.dlapi.edit_work_report(rep)
    

    def search_work_report(self, search):
        reader = self.list_work_reports()
        for report in reader:
            if search == report.workreport_id:
                return report
        return False


    def create_work_report(self, work_rep):
        return self.dlapi.create_work_report(WorkReport(work_rep))


    def get_new_id(self):
        last_id = self.dlapi.find_last_report_id()
        new_id = int(last_id[4:])+1
        return f'wrep{new_id}'