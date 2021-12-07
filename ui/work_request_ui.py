from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class WorkRequestUI:
    def __init__(self, work_request, destination, user_type):
        self.destination = destination
        self.llapi= LLAPI(self.destination)
        self.work_request = work_request
        self.user_type = user_type
        self.options = """1: Edit
B: Back"""

    def start(self):
        print(LINE)
        print(self.work_request)
        print(LINE)
        if self.user_type == 'Manager':
            self.manager_start()
        elif self.user_type == 'Employee':
            self.employee_start()
        print(LINE)

    def manager_start(self):
        options = """1: Edit \nB: Back"""
        input_str = "Choose Options edit or back: "
        while True:
            print(options)
            print(LINE)
            command = input(input_str).upper()
            print(LINE)
            if command == "1":
                self.llapi.edit_work_request(self.work_request)
                edited_request = self.llapi.search_work_requests_id(self.work_request.workrequest_id)
                print(LINE)
                print(edited_request)
                print(LINE)
            elif command == "B":
                return
            else:
                print("Invalid option, try again ")
        
    def employee_start(self):
        options = """B: Back"""
        input_str = "Press B for back: "
        while True:
            print(options)
            print(LINE)
            command = input(input_str).upper()
            print(LINE)
            if command == "B":
                return
            else:
                print("Invalid option, try again ")

