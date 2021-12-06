from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class WorkReportUI:
    def __init__(self, work_request, destination):
        self.destination = destination
        self.llapi= LLAPI(self.destination)
        self.work_request = work_request
        self.options = """[1].Edit
[B].Back"""

    def start(self):
        print(LINE)
        print(self.work_request)
        print(LINE)
        while True:
            print(self.options)
            print(LINE)
            commands2 = input("Choose Options edit or back: ").upper()
            print(LINE)
            if commands2 == "1":
                self.llapi.edit_employee(self.work_request)
                edited_request = self.llapi.search_work_requests(self.work_request.workrequest_id)
                print(LINE)
                print(edited_request)
                print(LINE)
            elif commands2 == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)

