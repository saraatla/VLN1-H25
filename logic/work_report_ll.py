from data.DLAPI import DLAPI
from models.work_report import WorkReport
from models.work_request import WorkRequest

class WorkReportLL:
    def __init__(self):
        self.dlapi = DLAPI()
        self.approved_index = 7

    def get_all_work_reports(self):
        return self.dlapi.get_all_reports()

    def search_report(self, search):
        reader = self.dlapi.get_all_reports()
        for row in reader:
            if search == row.workreport_id:
                return row
        return False

    def approve_report(self, wrep_id):
        reader = self.dlapi.get_all_reports()
        i = 0
        for row in reader:
            if wrep_id == row.workreport_id:
                self.dlapi.edit_work_report(i, self.approved_index, True)
                return 'Report has been marked approved!'
            i += 1    
        return 'No report found'

    def create_report(self, wrep):
        request = self.dlapi.get_all_work_requests()
        for row in request:
            if row.workreport_id == wrep:
                if row.status == 'Open':
                    return self.dlapi.create_work_report(wrep)
        return 'This workrequest is not open'