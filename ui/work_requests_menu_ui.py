from ui.menu import Menu
from logic.LLAPI import LLAPI
from ui.work_request_ui import WorkRequestUI
from ui.work_report_ui import WorkReportUI

class WorkRequestMenu:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.llapi = LLAPI(self.destination)
        self.user_type = user_type

    def start(self):
         while True:
            operations = ['Search by Work Request ID', 'Search by Property ID', 'Search by SSN', 'Search by Contractor Name', 'See list of all requests', 'See list of requests ready to close', 'Add new']
            operations_menu = Menu(f'Work Requests in {self.destination}\nChoose options', operations)
            selected_operation = operations_menu.draw_options()
            if selected_operation < 0:
                return
            operation = operations[selected_operation]
            if operation == 'Search by Work Request ID':
                found_request = self.llapi.search_work_requests_id()
                if found_request is not None:
                    work_request_ui = WorkRequestUI(found_request, self.destination)
                    work_request_ui.start()

            elif operation == 'Search by Property ID':
                found_request = self.llapi.search_work_requests_prop()
                if found_request is not None:
                    work_request_ui = WorkRequestUI(found_request, self.destination)
                    work_request_ui.start()

            elif operation == 'Search by SSN':
                found_report = self.llapi.search_work_request_ssn()
                if found_report is not None:
                    # pass
                    work_request_ui = WorkRequestUI(found_request, self.destination)
                    work_request_ui.start()


            elif operation == 'Search by Contractor Name':
                found_report = self.llapi.search_work_requests_cont()
                if found_report is not None:
                    # pass
                    work_request_ui = WorkRequestUI(found_request, self.destination)
                    work_request_ui.start()


            elif operation == 'See list of all requests':
                workreq_list = self.llapi.list_work_requests()
                for request in workreq_list:
                    print(request)


            elif operation == "See list of requests ready to close":
                workreq_list = self.llapi.get_all_work_requests_by_status()
                print(workreq_list)

            elif operation == 'Add new':
                self.llapi.create_work_request()