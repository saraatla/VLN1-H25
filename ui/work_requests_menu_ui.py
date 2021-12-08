from datetime import date, timedelta, datetime
from Extra.pythondateutil.dateutil.relativedelta import relativedelta
from Extra.texttableFile.texttable import Texttable
from Extra.acci import workAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI

from ui.work_report_ui import WorkReportUI


LINE = '------------------------------------------'

class WorkRequestMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
        workAscii()
        while True:
            operations = ['Search by work request ID', 'Search by property ID', 'Search by SSN', 'Search by contractor ID', 'See list of all requests', 'See list of requests by status']
            if self.user_type == 'Manager':
                operations.append('Add new')
            operations_menu = Menu(f'Work Requests in {self.destination}\nChoose options', operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            if operation == 'Search by work request ID':
                search = input('Enter work request ID: ')
                found_request = self.llapi.search_work_requests_id(search, self.destination)
                if found_request is None:
                    print(f'{LINE}\nWork request not found\n{LINE}')
                else:
                    self.individual_work_request_ui(found_request)

            elif operation == 'Search by property ID':
                search = input('Enter property ID: ')
                found_requests = self.llapi.search_work_requests_prop(search, self.destination)
                if found_requests == []:
                    print(f'{LINE}\nNo work requests found\n{LINE}')
                else:
                    self.list_work_requests_ui(found_requests)
                    self.open_request_from_list(found_requests)

            elif operation == 'Search by SSN': # EKKI RETT ÞETTA SKILAR LISTA
                search = input('Enter SSN: ')
                found_requests = self.llapi.search_work_request_ssn(search, self.destination)
                if found_requests == []:
                    print(f'{LINE}\nNo work requests found\n{LINE}')
                else:
                    self.list_work_requests_ui(found_requests)
                    self.open_request_from_list(found_requests)

            elif operation == 'Search by contractor ID':
                search = input('Enter contractor ID: ')
                found_requests = self.llapi.search_work_requests_cont(search, self.destination)
                if found_requests == []:
                    print(f'{LINE}\nNo work requests found\n{LINE}')
                else:
                    self.list_work_requests_ui(found_requests)
                    self.open_request_from_list(found_requests)

            elif operation == 'See list of all requests':
                start_date = input('Enter date to search from:')
                end_date = input('Enter date to end:')
                request_list = self.llapi.list_all_work_requests(self.destination)
                request_list_by_date = self.llapi.get_list_of_workreq_on_period(request_list,start_date,end_date)
                
                self.list_work_requests_ui(request_list_by_date)
                self.open_request_from_list(request_list_by_date)
                

            elif operation == "See list of requests by status":
                while True:
                    status = input('Enter status: ').lower()
                    request_list = self.llapi.workrequests_by_status(status, self.destination) 
                    if request_list == []:
                        print('No {} work request found.\nPlease enter "open", "closed", "ready for closing" or "completed".'.format(status))
                    else:
                        break
                self.list_work_requests_ui(request_list)
                self.open_request_from_list(request_list)
                

            elif operation == 'Add new':
                self.create_work_request()

    def open_request_from_list(self, request_list):
        while True:
            command = input("Enter Number of request to open or B to Back:").upper()
            if command == "B":
                return
            if not command.isdigit():
                print("Invalid input, try again!")
            else:
                nr = int(command)
                for index, request in enumerate(request_list):
                    if index+1 == nr:
                        self.individual_work_request_ui(request,nr)
                break



    def list_work_requests_ui(self, request_list):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(300)
        for item in range(len(request_list)):
            workreq = request_list[item]
            table.add_rows([["Number.","Workrequest_ID", "Title", "Date", "Status", "Priority"], 
                            [item+1, workreq.workrequest_id, workreq.title, workreq.date, workreq.status, workreq.priority]])
        print(table.draw())


    def individual_work_request_ui(self, request, nr=None):
        self.print_work_request_table(request, nr)
        if self.user_type == 'Employee':
            if request.status == 'open':
                while True:
                    print('1: Add report\nB: Back')
                    print(LINE)
                    command = input("Choose Options: ").upper()
                    print(LINE)
                    if command == "1":
                        self.create_work_report(request)
                    elif command == "B":
                        return
                    else:
                        print("Invalid option, try again ")
                        print(LINE)
            else:
                while True:
                    command = input('Press B for Back: ').upper()
                    print(LINE)
                    if command == 'B':
                        return
                    else:
                        print("Invalid option, try again ")
                        print(LINE)
        elif self.user_type == 'Manager':
            while True:
                print("1: Edit\nB: Back")
                print(LINE)
                command = input("Choose Options edit or back: ").upper()
                print(LINE)
                if command == "1":
                    self.edit_work_request(request)
                    self.print_work_request_table(request)
                elif command == "B":
                    return
                else:
                    print("Invalid option, try again ")
                    print(LINE)
    

    def print_work_request_table(self, request, nr=None):
        work_request_table = Texttable()
        if nr is not None:
            work_request_table.add_row(["Number.",nr])
        work_request_table.add_row(["Workrequest_ID",request.workrequest_id])
        work_request_table.add_row(["Title",request.title])
        work_request_table.add_row(["Property_ID",request.property_id])
        work_request_table.add_row(["Destination",request.destination])
        work_request_table.add_row(["Contractor",request.contractor])
        work_request_table.add_row(["Date",request.date])
        work_request_table.add_row(["Status",request.status])
        work_request_table.add_row(["Priority",request.priority])
        work_request_table.add_row(["Description",request.description])
        work_request_table.add_row(["Workreport ID",request.workreport_id])
        print(work_request_table.draw())
    

    def edit_work_request(self, req):
        while True:
            fieldnames = ['Title', 'Property_ID', 'Destination', 'Contractor', 'Date', 'Status', 'Priority', 'Description']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            try:
                col = int(col)
                newval = input(f'What is the new {fieldnames[col-1]}? ')
                setattr(req, fieldnames[col-1].lower(), newval)
                return self.llapi.edit_work_request(req)
            except:
                print('Invalid input, try again!')




    def individual_work_report_ui(self, report, nr=None):
        pass


    def create_work_report(self, request):
        pass









    
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


