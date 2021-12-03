from data.DLAPI import DLAPI

class WorkReportLL:
    """Work Report logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    APPROVED_INDEX = 7

    def __init__(self):
        self.dlapi = DLAPI()

    def list_work_reports(self):
        return self.dlapi.list_work_reports()

    def edit_work_report(self,):
        return self.dlapi.edit_work_report()

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
        request = self.dlapi.list_work_reports()
        for row in request:
            if row.workreport_id == work_rep:
                if row.status == 'Open':
                    return self.dlapi.create_work_report(work_rep)
        return 'This workrequest is not open'