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


    def _list_work_reports(self):
        return self.dlapi._list_work_reports()


    def _edit_work_report(self, rep):
        return self.dlapi._edit_work_report(rep)
    

    def _search_work_report(self, search):
        reader = self._list_work_reports()
        for report in reader:
            if search == report.workreport_id:
                return report
        return False


    def _create_report(self, work_rep):
        return self.dlapi.create_work_report(WorkReport(work_rep))


    def _get_new_id(self):
        last_id = self.dlapi._find_last_report_id()
        new_id = int(last_id[4:])+1
        return f'wrep{new_id}'