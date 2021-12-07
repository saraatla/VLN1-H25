from data.DLAPI import DLAPI
from models.work_request import WorkRequest

class WorkReportLL:
    """Work Report logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    APPROVED_INDEX = 7

    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)

    def list_work_reports(self):
        return self.dlapi.list_work_reports()

    def edit_work_report(self, rep):
        while True:
            id = rep.workrequest_id
            fieldnames = ['Title', 'Property_ID', 'Destination', 'Contractor', 'Date', 'Status', 'Priority', 'Description']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                return self.dlapi.edit_work_report(id, col, newval)
            except:
                print('Invalid input, try again!')

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