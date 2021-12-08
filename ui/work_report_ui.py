from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class WorkReportUI:
    def __init__(self, destination):
        self.destination = destination
        self.llapi= LLAPI(self.destination)
        self.options = """1: Edit
B: Back"""

    def start(self):
        print(LINE)
        print(self.work_report)
        print(LINE)
        while True:
            print(self.options)
            print(LINE)
            commands2 = input("Choose Options edit or back: ").upper()
            print(LINE)
            if commands2 == "1":
                self.llapi.edit_employee(self.work_report)
                edited_request = self.llapi.search_work_requests(self.work_request.workreport_id)
                print(LINE)
                print(edited_request)
                print(LINE)
            elif commands2 == "B":
                return
            else:
                print("Invalid option, try again ")
                print(LINE)
    
    def create_work_report(self, request):
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