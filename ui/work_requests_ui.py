import datetime
from Extra.TermcolorFile.termcolor import colored, cprint
from Extra.texttableFile.texttable import Texttable, get_color_string, bcolors
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from Extra.acci import workAscii
from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.work_report_ui import WorkReportUI
from time import sleep


LINE = '------------------------------------------'

class WorkRequestUI:
    """Work Request UI layer class. Contains 14 functions. 
    The class contains an instance of the LLAPI and WorkReportUI class
    Args: 
        destination (str): destination chosen by user
        user_type (str): user type chosen by user (manager/employee)"""

    def __init__(self, destination, user_type):
        self.user_type = user_type
        self.destination = destination
        self.color_format = colored("{}",'green' ,attrs=['bold', 'underline'])
        self.Work_Requests_menu_color = colored("Work Requests Menu",'red' ,attrs=['bold', 'underline'])
        self.destination_collor = colored(self.destination, 'blue' ,attrs=['bold', 'underline'])
        self.llapi = LLAPI(self.destination)
        self.report_ui = WorkReportUI(self.destination, self.user_type)


    def workrequest_menu_start(self):
        """This function makes the work request menu function. It depends on the inputs by user"""
        while True: 
            workAscii() 
            operations = ['Search by work request ID', 'Search by property ID', 'Search by employee SSN', 'Search by contractor ID', 'See list of all requests', 'See list of requests by status']

            # If the user logged in as a Manager he also sees
            if self.user_type == 'Manager':
                operations.append('Create new')
            operations_menu = Menu(f'{LINE}\n{self.Work_Requests_menu_color} in {self.destination_collor}\nChoose options', operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]

            # Search by work request ID: allows the user to search a work request by it's ID
            if operation == 'Search by work request ID':
                search = input(self.color_format.format('Enter work request ID: ')).lower()
                found_request = self.llapi.search_work_requests_id(search, self.destination)
                if found_request is None:
                    print(f'{LINE}\nWork request not found\n{LINE}')
                    sleep(2)
                else:
                    self.__individual_work_request_ui(found_request)

            # Search by property ID: allows the user to search a work request by property ID
            elif operation == 'Search by property ID':
                search = input(self.color_format.format('Enter property ID: ')).upper()
                found_requests = self.llapi.search_work_requests_prop(search, self.destination)
                if found_requests == []:
                    print(f'{LINE}\nNo work requests found\n{LINE}')
                    sleep(2)
                else:
                    self.__print_request_list(found_requests)

            # Search by employee SSN: allows the user to search a work request by employee SSN,
            elif operation == 'Search by employee SSN':
                search = input(self.color_format.format('Enter employee SSN: '))
                found_requests = self.llapi.search_work_request_ssn(search, self.destination)
                if found_requests == []:
                    print(f'{LINE}\nNo work requests found\n{LINE}')
                    sleep(2)
                else:
                    self.__print_request_list(found_requests)

            # Search by contractor ID: allows the user to search a work request by contractor ID,
            elif operation == 'Search by contractor ID':
                search = input(self.color_format.format('Enter contractor ID: ')).upper()
                found_requests = self.llapi.search_work_requests_cont(search, self.destination)
                if found_requests == []:
                    print(f'{LINE}\nNo work requests found\n{LINE}')
                    sleep(2)
                else:
                    self.__print_request_list(found_requests)

            # See list of all requests: prompts a list of work requests on a specific period chosen by user or all of them
            elif operation == 'See list of all requests':
                request_list = self.llapi.list_all_work_requests(self.destination)
                self.__print_request_list(request_list)

            # See list of requests by status: prompts a list of requests by status
            elif operation == "See list of requests by status":
                while True:
                    status = input(self.color_format.format('Enter status: ')).lower()
                    if status == 'b':
                        break
                    request_list = self.llapi.workrequests_by_status(status, self.destination)
                    if request_list == []:
                        print('No {} work request found.\nPlease enter "open", "closed", "ready for closing",\n"completed" or "B" to go back'.format(status))
                        sleep(2)
                    else:
                        break
                if status != 'b':
                    self.__list_work_requests_ui(request_list)
                    self.__open_request_from_list(request_list)

            # Create new: makes it possible to create new work request
            elif operation == 'Create new':
                self.__create_work_request()


    def __print_request_list(self, request_list):
        """This function calls 3 functions in this class"""

        request_list_by_date = self.__find_date_range(request_list)
        self.__list_work_requests_ui(request_list_by_date)
        self.__open_request_from_list(request_list_by_date)


    def __open_request_from_list(self, request_list):
        """This function allows the user to choose a work request to see more information about 
        in a list of work requests
        Args: 
            request_list (list): list of work requests"""

        while True:
            print(LINE)
            command = input(self.color_format.format("Enter Number of request to open or B to Back: ")).upper()
            if command == "B":
                break
            try:
                nr = int(command)
                if nr > len(request_list) or nr == 0:
                    raise ValueError
            except:
                print("Invalid input, please try again")
            else:
                nr = int(command)
                for index, request in enumerate(request_list):
                    if index+1 == nr:
                        self.__individual_work_request_ui(request,nr)
                break


    def __find_date_range(self, request_list):
        """This function finds work requests on a specific period input by user
        Args: 
            request_list (list): list of all requests
        Returns:
            request_list_by_date (list): list of requests on a specific period"""

        while True:
            print(f'Enter date range for list of work requests or leave blank to see all\n{LINE}')
            start_date = self.__check_date('date to search from')
            end_date = self.__check_date('date to end')
            request_list_by_date = self.llapi.get_list_of_workreq_on_period(request_list,start_date,end_date)
            if request_list_by_date is None:
                print('The inputs are not valid, please try again')
            else:
                return request_list_by_date
                    

    def __list_work_requests_ui(self, request_list):
        """This function runs when the user chooses to see work requests.
        It will show the list of work requests in a printable template format."""

        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(300)
        for item in range(len(request_list)):
            workreq = request_list[item]
            table.add_rows([[get_color_string(bcolors.GREEN,"Number"),get_color_string(bcolors.GREEN,"Workrequest_ID"), get_color_string(bcolors.GREEN,"Title"), get_color_string(bcolors.GREEN,"Date"), get_color_string(bcolors.GREEN,"Status"), get_color_string(bcolors.GREEN,"Priority")], 
                            [get_color_string(bcolors.GREEN,item+1), workreq.workrequest_id, workreq.title, workreq.date.strftime('%d/%m/%Y'), workreq.status, workreq.priority]])
        print(f'\n{table.draw()}\n')


    def __individual_work_request_ui(self, request, nr=None):
        """This function runs when the user chooses 'Search by X' and inputs an ID that's in the system.
        It will show information of a work request along with options.
        The options depend on the user (Manager/Employee) and also the work request status.
        Args:
            request (class instance): request model class,
            nr : either None or int. """

        # If the user is an Employee and the status of request is 'open' he can add a report
        if self.user_type == 'Employee':
            if request.status == 'open' and not request.workreport_id:
                while True:
                    self.__print_work_request_table(request, nr)
                    print('1: Add report\nB: Back')
                    print(LINE)
                    command = input(self.color_format.format("Choose Options: ")).upper()
                    print(LINE)
                    if command == "1":
                        work_report = self.report_ui.create_work_report(request)
                        self.report_ui.individual_work_report_ui(work_report, request)
                        break
                    elif command == "B":
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)

            # if the status is 'closed' he can only view it
            elif request.status == 'closed':
                while True:
                    self.__print_work_request_table(request, nr)
                    command = input(self.color_format.format('Press B for back: ')).upper()
                    if command == 'B':
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)

            # if the status is 'completed' he can see report
            else:
                while True:
                    self.__print_work_request_table(request, nr)
                    print('1: See report\nB: Back ')
                    print(LINE)
                    command = input(self.color_format.format("Choose Options: ")).upper()
                    if command == '1':
                        report = self.llapi.search_work_report(request.workreport_id)
                        self.report_ui.individual_work_report_ui(report, request)
                    if command == 'B':
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)

        # If the user is a Manager and the status of request is 'completed' he can see report or reopen request
        elif self.user_type == 'Manager':
            if request.status == 'completed':
                while True:
                    self.__print_work_request_table(request, nr)
                    print("1: See report\n2:Reopen request\nB: Back")
                    print(LINE)
                    command = input(self.color_format.format("Choose Options see report,reopen or back: ")).upper()
                    print(LINE)
                    if command == '1':
                        report = self.llapi.search_work_report(request.workreport_id)
                        self.report_ui.individual_work_report_ui(report, request)
                    if command == "2":
                        request.status = 'open'
                        self.llapi.edit_work_request(request)
                        break
                    elif command == "B":
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)

            # if the statust is 'open' and there is a report assigned to it he can see report and choose what to do with it
            elif request.status == 'open' and request.workreport_id:
                while True:
                    self.__print_work_request_table(request, nr)
                    print(f"{LINE}\n1: See report\nB: Back")
                    command = input(self.color_format.format('Choose options: ')).upper()
                    if command == '1':
                        report = self.llapi.search_work_report(request.workreport_id)
                        self.report_ui.individual_work_report_ui(report, request)
                    elif command == 'B':
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)

            # if the status is 'open' or 'closed' he can edit the request
            else:
                while True:
                    self.__print_work_request_table(request, nr)
                    print("1: Edit\nB: Back")
                    print(LINE)
                    command = input(self.color_format.format("Choose Options edit or back: ")).upper()
                    print(LINE)
                    if command == "1":
                        self.__edit_work_request(request)
                    elif command == "B":
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)


    def __print_work_request_table(self, request, nr=None):
        """This function prints work request info in a printable template format.
        Args:
            request (class instance): work request model class,
            nr : either None or int. """

        work_request_table = Texttable()
        work_request_table.add_row([get_color_string(bcolors.BLUE,"Work request\n???????????????"),get_color_string(bcolors.BLUE,"Work request\n???????????????")])
        if nr is not None:
            work_request_table.add_row([get_color_string(bcolors.GREEN,"Number"),nr])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Workrequest_ID"),request.workrequest_id])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Title"),request.title])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Property_ID"),request.property_id])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Destination"),request.destination])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Contractor"),request.contractor])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Date"),request.date.strftime('%d/%m/%Y')])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Status"),request.status])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Priority"),request.priority])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Description"),request.description])
        work_request_table.add_row([get_color_string(bcolors.GREEN,"Workreport ID"),request.workreport_id])
        print(f'{work_request_table.draw()}')
    

    def __edit_work_request(self, request):
        """This function runs if the user is a Manager and chooses to Edit work request.
        The user chooses what to edit according to the available options.
        Args:
            request (class instance): work request model class."""

        while True:
            fieldnames = ['Title', 'Property_ID', 'Destination', 'Contractor', 'Date', 'Status', 'Priority', 'Description']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input('What do you want to change? ')
            if col == '0':
                print('Invalid input, please try again')
            else:
                try:
                    col = int(col)
                    newval = input(self.color_format.format(f'What is the new {fieldnames[col-1]}? '))
                    setattr(request, fieldnames[col-1].lower(), newval)
                    return self.llapi.edit_work_request(request)
                except:
                    print('Invalid input, please try again')


    def __create_work_request(self):
        """This function runs when the user (manager) chooses 'Create new' . 
        The work request will be given a destination according to the user's choice in the destination menu."""
        
        print('Enter the following information: ')
        print(LINE)
        start_date, workreq = self.__create_work_req_list()
        print('Do you want to repeat this work request? ')
        options = ['Do no repeat', 'Daily', 'Weekly', 'Monthly', 'Yearly']
        for index, option in enumerate(options):
            print(f"{index+1}: {option}")
        while True:
            repeat = int(input(self.color_format.format('Choose option: ')))
            try:
                repeat = int(repeat)
                if repeat > 1:
                    self.__repeat_work_request(start_date, repeat, workreq)
                    break
                elif repeat == 1:
                    self.llapi.create_work_request(workreq)
                    print(f'{LINE}\nWork request successfully created!\n{LINE}')
                    sleep(2)
                    break
                else:
                    print('Invalid option, please try again')
            except:
                print('Invalid option, please try again')


    def __create_work_req_list(self):
        """This function lists the inputs and options needed to make a work request.
        Returns: 
            start_date (str): date when request opens
            workreq (list(str)): info of new work request"""

        new_id = self.llapi.get_new_request_id()
        workreq = [new_id]
        fieldnames = ["Title", "Property_ID"]
        for field in fieldnames:
            val = input(self.color_format.format(f'{field}: '))
            workreq.append(val)
        
        workreq.append(self.destination)
        contractor = input(self.color_format.format('Is a contractor needed for this work request: '))
        workreq.append(contractor)
        while True:
            start_date = self.__check_date('start date')
            date_var = datetime.strptime(start_date,'%d/%m/%Y').date()
            if date.today() > date_var:
                print('Can not create work request in the past')
            else:
                break
        workreq.append(start_date)
        if start_date == date.today():
            status = 'open'
        else:
            status = 'closed'
        workreq.append(status)
        priority_options  = ['Emergengy', 'Now', 'ASAP']
        for i, option in enumerate(priority_options):
            print(f"{i+1}: {option}")
        # The manager can choose the urgency of the request 
        while True:
            index = input(self.color_format.format('Choose priority: '))
            try:
                index = int(index)
                priority = priority_options[index-1]
                break
            except:
                print('Invalid option, please try again')
        workreq.append(priority)
        description = input(self.color_format.format('Description: '))
        workreq.append(description)
        report_id = None
        workreq.append(report_id)
        return start_date, workreq


    def __repeat_work_request(self,start_date, repeat, workreq):
        """This function makes the number of work requests according do the start date, end date
        and how it is repeated (daily/weekly/monthly/yearly)
        Args:
            start_date (str): 
            repeat (int): option int for daily/weekly/monthly/yearly
            workreq (list): info of new work request"""

        date_var = datetime.strptime(start_date,'%d/%m/%Y').date()
        print(date_var)
        if date.today() <= date_var:
            i = 0
            if repeat == 2:
                how_many = int(input(self.color_format.format('for how many days: ')))
                for i in range(how_many):
                    new_date = timedelta(days = 1*i)
                    self.__create_repeated(workreq, date_var, new_date)
            elif repeat == 3:
                how_many = int(input(self.color_format.format('for how many weeks: ')))
                for i in range(how_many):
                    new_date = timedelta(weeks = 1*i)
                    self.__create_repeated(workreq, date_var, new_date)
            elif repeat == 4:
                how_many = int(input(self.color_format.format('for how many months: ')))
                for i in range(how_many):
                    new_date = relativedelta(months =+1*i)
                    self.__create_repeated(workreq, date_var, new_date)
            elif repeat == 5:
                how_many = int(input(self.color_format.format('for how many years: ')))
                for i in range(how_many):
                    new_date = relativedelta(years =+1*i)
                    self.__create_repeated(workreq, date_var, new_date)
            print(f'{LINE}\nWork request successfully created!\n{LINE}')
            sleep(2)
        else:
            print("Can not create work request in the past")


    def __create_repeated(self, workreq, date_var, new_date):
        """This function creates the new work requests
        Args:
            workreq (list): info of new work request
            date_var (datetime.date): date variable for the start date of work request
            new_date (datetime.timedelta): timedelta variable for number of days/weeks/months/years """

        date_work_req = date_var + new_date
        date_work_req = date_work_req.strftime('%d/%m/%Y')
        workreq[5] = date_work_req
        self.llapi.create_work_request(workreq)
        old_id = workreq[0]
        new_id = int(old_id[1:])+1
        workreq[0] = f'w{new_id}'


    def __check_date(self, date_str):
        """This function checks if the format of a input date is right
        Args:
            date_str (str): type of date (start/end)
        Returns:
            date_string (str): input date"""

        while True:
            date_string = input(self.color_format.format(f'Enter {date_str}, dd/mm/yyyy: '))
            if date_string == '' and date_str is not 'start date':
                return date_string
            format = "%d/%m/%Y"
            try:
                datetime.strptime(date_string, format)
                return date_string
            except ValueError:
                print("This is the incorrect date format. It should be dd/mm/yyyy")
        
            


