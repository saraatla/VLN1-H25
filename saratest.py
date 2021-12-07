import datetime

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


from datetime import date
from datetime import timedelta

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
            last_id = self.dlapi.find_last_id()
            new_id = int(last_id[1:])+1
            workreq = [f'w{new_id}']
            fieldnames = ["Title", "Property_ID"] #, "Destination", "Contractor", "Date", "Status", "Priority", "Description", "Workreport_ID"
            for field in fieldnames:
                val = input(f'{field}: ')
                workreq.append(val)
            workreq.append(self.destination)
            contractor = input('Is a contractor needed for this work request: ')
            workreq.append(contractor)
            # gera date
            start_date = input('Start date, dd/mm/yyyy: ')
            workreq.append(start_date)
            if start_date == date.today():
                status = 'open'
            else:
                status = 'closed'
            workreq.append(status)
            priority_options  = ['Emergengy', 'Now', 'ASAP']
            for i, option in enumerate(priority_options):
                print(f"{i+1}: {option}")
            index = int(input('Choose priority:'))
            workreq.append(priority_options[index-1])
            description = input('Description:  ')
            workreq.append(description)
            report_id = 'None'
            workreq.append(report_id)
            intro = print('Do you want to repeat this work request?')
            options = ['Do no repeat', 'Daily', 'Weekly', 'Monthly', 'Yearly']
            for i, option in enumerate(options):
                print(f"{i+1}: {option}")
            repeat = int(input('Choose option: '))
            print(repeat)
            if repeat > 1:
                self.repeat_work_request(start_date, repeat, workreq)
            else:
                self.dlapi.create_work_request(WorkRequest(workreq))
                print(f'{LINE}\nWork request successfully created!\n{LINE}')

            


    def repeat_work_request(self,start_date, repeat, workreq):
        dates = start_date.split('/')
        x = date(int(dates[2]),int(dates[1]),int(dates[0]))
        if date.today() <= x:
            if repeat == 2:
                how_many = int(input('for how many days?:'))
                for i in range(how_many):
                    new_date = timedelta(days = 1*i)
                    date_work_req = x + new_date
                    date_work_req = date_work_req.strftime('%d/%m/%Y')
                    workreq[5] = date_work_req
                    self.dlapi.create_work_request(WorkRequest(workreq))
            elif repeat == 3:
                how_many = int(input('for how many weeks?:'))
                for i in range(how_many):
                    new_date = timedelta(weeks = 1*i)
                    date_work_req = x + new_date
                    date_work_req = date_work_req.strftime("%D/%M/%Y")
                    workreq[5] = date_work_req
                    self.dlapi.create_work_request(WorkRequest(workreq))
            elif repeat == 4:
                how_many = input('for how many months?:')
                for i in range(how_many):
                    new_date = timedelta(months = 1*i)
                    date_work_req = x + new_date
                    date_work_req.strftime("%D/%M/%Y")
                    workreq[5] = date_work_req
                    self.dlapi.create_work_request(WorkRequest(workreq))
            elif repeat == 5:
                how_many = input('for how many years?:')
                for i in range(how_many):
                    new_date = timedelta(years = 1*i)
                    date_work_req = x + new_date   
                    date_work_req.strftime("%D/%M/%Y")
                    workreq[5] = date_work_req
                    self.dlapi.create_work_request(WorkRequest(workreq))  
        else:
            print("Can not create work request in the past")

        
    """def repeat_work_request(self,start_date, repeat, workreq):
        dates = start_date.split('/')
        x = date(int(dates[2]),int(dates[1]),int(dates[0]))
        if date.today() <= x:
            if repeat == 2:
                how_many = int(input('for how many days?:'))
                time_val = 'days'
                
            elif repeat == 3:
                how_many = int(input('for how many weeks?:'))
                time_val = 'weeks'
                
            elif repeat == 4:
                how_many = input('for how many months?:')
                time_val = 'months'
                
            elif repeat == 5:
                how_many = input('for how many years?:')
                time_val = 'years'
                
            for i in range(how_many):
                    new_date = timedelta(time_val = 1*i)
                    date_work_req = x + new_date
                    date_work_req.strftime("%D/%M/%Y")
                    workreq[5] = date_work_req
                    self.dlapi.create_work_request(WorkRequest(workreq))
            
        else:
            print("Can not create work request in the past")"""


wLL  = WorkRequestLL('Svalbard')

wLL.create_work_request()