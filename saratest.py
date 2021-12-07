from data.work_report_dl import WorkReportDL
from models.work_report import WorkReport


repDL = WorkReportDL('Svalbard')

"""
x = []
for i in range(10, 141): 
    x.append(i*3)

for i in x:
    work_rep = WorkReport([f'wrep{i}','123456-0004','N/A','N/A','N/A','10.000.-','Gekk rosa vel','False'])
    repDL.create_work_report(work_rep)
    work_rep = WorkReport([f'wrep{i+1}','123456-0005','N/A','N/A','N/A','10.000.-','Gekk vel!','False'])
    repDL.create_work_report(work_rep)
    work_rep = WorkReport([f'wrep{i+2}','123456-0006','N/A','N/A','N/A','10.000.-','Gekk þokkalega','False'])
    repDL.create_work_report(work_rep)


x = []
for i in range(144, 214): 
    x.append(i*3)

for i in x:
    work_rep = WorkReport([f'wrep{i}','123456-0008','N/A','N/A','N/A','15.000.-','Gekk mjög vel','False'])
    repDL.create_work_report(work_rep)
    work_rep = WorkReport([f'wrep{i+1}','123456-0009','N/A','N/A','N/A','15.000.-','Allt gekk vel!','False'])
    repDL.create_work_report(work_rep)
    work_rep = WorkReport([f'wrep{i+2}','123456-0007','N/A','N/A','N/A','15.000.-','Allt gekk eins og í sögu','False'])
    repDL.create_work_report(work_rep)"""

from os import read
from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.work_request import WorkRequest
LINE = '------------------------------------------'

class WorkRequestLL:
    """Work Request logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self, destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)
        self.table = Texttable()
        self.table2 = Texttable()

def create_work_request(self):
        # return self.dlapi.create_work_request(work_req)
        print('Enter the following information: ')
        print(LINE)
        last_id = find_last_id()
        new_id = last_id + 1
        workreq = [new_id]
        fieldnames = ["Title", "Property_ID", "Destination", "Contractor", "Date", "Status", "Priority", "Description", "Workreport_ID"]
        for field in fieldnames:
            val = input(f'{field}: ')
            workreq.append(val)
        self.dlapi.create_work_request(WorkRequest(workreq))
        print(f'{LINE}\nWork request successfully created!\n{LINE}')