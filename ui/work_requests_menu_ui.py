from datetime import date, timedelta, datetime
#from dateutil.relativedelta import relativedelta

from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.work_request_ui import WorkRequestUI
from ui.work_report_ui import WorkReportUI
from Extra.acci import workAscii

LINE = '------------------------------------------'

class WorkRequestMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
         while True:
            workAscii()
            operations = ['Search by work request ID', 'Search by property ID', 'Search by SSN', 'Search by contractor Name', 'See list of all requests', 'See list of requests by status']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'Work Requests in {self.destination}\nChoose options', operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation == 'Search by work request ID':
                found_request = self.llapi.search_work_requests_id()
                print('HEEEELLLOOOOOO')
                if found_request is not None:
                    print('HÆÆÆÆÆÆÆÆÆÆÆÆ')
                    work_request_ui = WorkRequestUI(found_request, self.destination, self.user_type)
                    work_request_ui.start()

            elif operation == 'Search by property ID':
                found_request = self.llapi.search_work_requests_prop()
                if found_request is not None:
                    work_request_ui = WorkRequestUI(found_request, self.destination)
                    work_request_ui.start()

            elif operation == 'Search by SSN':
                found_request = self.llapi.search_work_request_ssn()
                if found_request is not None:
                    work_request_ui = WorkRequestUI(found_request, self.destination)
                    work_request_ui.start()

            elif operation == 'Search by contractor name':
                found_report = self.llapi.search_work_requests_cont()
                if found_report is not None:
                    work_request_ui = WorkRequestUI(found_request, self.destination)
                    work_request_ui.start()

            elif operation == 'See list of all requests':
                self.llapi.list_work_requests()

            elif operation == "See list of requests by status":
                self.llapi.workrequests_by_status()

            elif operation == 'Add new':
                self.create_work_request()
    
    def create_work_request(self):
        print('Enter the following information: ')
        print(LINE)
        start_date, workreq = self.create_work_req_list()
        print('Do you want to repeat this work request?')
        options = ['Do no repeat', 'Daily', 'Weekly', 'Monthly', 'Yearly']
        for i, option in enumerate(options):
            print(f"{i+1}: {option}")
        repeat = int(input('Choose option: '))
        if repeat > 1:
            self.repeat_work_request(start_date, repeat, workreq)
        else:
            self.llapi.create_work_request(workreq)
            print(f'{LINE}\nWork request successfully created!\n{LINE}')
    

    def create_work_req_list(self):
        new_id = self.llapi.get_new_id()
        workreq = [new_id]
        fieldnames = ["Title", "Property_ID"]
        for field in fieldnames:
            val = input(f'{field}: ')
            workreq.append(val)
        workreq.append(self.destination)
        contractor = input('Is a contractor needed for this work request: ')
        workreq.append(contractor)
        start_date = self.check_date()
        workreq.append(start_date)
        if start_date == date.today():
            status = 'open'
        else:
            status = 'closed'
        workreq.append(status)
        priority_options  = ['Emergengy', 'Now', 'ASAP']
        for i, option in enumerate(priority_options):
            print(f"{i+1}: {option}")
        index = int(input('Choose priority: '))
        priority = priority_options[index-1]
        workreq.append(priority)
        description = input('Description: ')
        workreq.append(description)
        report_id = 'None'
        workreq.append(report_id)
        return start_date, workreq


    def repeat_work_request(self,start_date, repeat, workreq):
        dates = start_date.split('/')
        x = date(int(dates[2]),int(dates[1]),int(dates[0]))
        if date.today() <= x:
            i = 0
            if repeat == 2:
                how_many = int(input('for how many days: '))
                for i in range(how_many):
                    new_date = timedelta(days = 1*i)
                    self.create_repeated(workreq, x, new_date)
            elif repeat == 3:
                how_many = int(input('for how many weeks: '))
                for i in range(how_many):
                    new_date = timedelta(weeks = 1*i)
                    self.create_repeated(workreq, x, new_date)
            elif repeat == 4:
                how_many = int(input('for how many months: '))
                for i in range(how_many):
                    new_date = relativedelta(months =+1*i)
                    self.create_repeated(workreq, x, new_date)
            elif repeat == 5:
                how_many = int(input('for how many years: '))
                for i in range(how_many):
                    new_date = relativedelta(years =+1*i)
                    self.create_repeated(workreq, x, new_date)
            print(f'{LINE}\nWork request successfully created!\n{LINE}')
        else:
            print("Can not create work request in the past")


    def create_repeated(self, workreq, x, new_date):
        date_work_req = x + new_date
        date_work_req = date_work_req.strftime('%d/%m/%Y')
        workreq[5] = date_work_req
        self.llapi.create_work_request(workreq)
        old_id = workreq[0]
        new_id = int(old_id[1:])+1
        workreq[0] = f'w{new_id}'


    def check_date(self):
        while True:
            date_string = input('Start date, dd/mm/yyyy: ')
            format = "%d/%m/%Y"
            try:
                datetime.strptime(date_string, format)
                return date_string
            except ValueError:
                print("This is the incorrect date format. It should be dd/mm/yyyy")


