from Extra.texttableFile.texttable import Texttable, get_color_string, bcolors
from Extra.TermcolorFile.termcolor import colored, cprint
from logic.LLAPI import LLAPI
LINE = '------------------------------------------'

class WorkReportUI:
    def __init__(self, destination, user_type):
        self.destination = destination
        self.user_type = user_type
        self.llapi= LLAPI(self.destination)
        self.color_format = colored("{}",'green' ,attrs=['bold', 'underline'])


    def _create_work_report(self, request):
        print('Enter the following information: ')
        print(LINE)
        new_id = self.llapi._get_new_report_id()
        workrep = [new_id]
        fieldnames = ['Eployee SSN', 'Contractor_ID', 'Contractor_review', 'Contractor_remuneration', 'Total_cost', 'Description']
        for field in fieldnames:
            val = input(self.color_format.format(f'{field}: '))
            workrep.append(val)
        approved = False
        workrep.append(approved)
        manager_comment = None
        workrep.append(manager_comment)
        work_report = self.llapi._create_report(workrep)
        print(f'{LINE}\nWork report successfully created!\n{LINE}')
        request.workreport_id = new_id
        self.llapi._edit_work_request(request)
        return work_report

    
    def _individual_work_report_ui(self, report, request, nr=None):
        if self.user_type == 'Employee':
            if request.status == 'open' and request.workreport_id is not None:
                while True:
                    self.__print_work_report_table(report)
                    print("1: Edit\nB: Back")
                    print(LINE)
                    command = input(self.color_format.format("Choose Options edit or back: ")).upper()
                    print(LINE)
                    if command == "1":
                        self.__edit_work_report(report)
                    elif command == "B":
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)
            else:
                while True:
                    self.__print_work_report_table(report)
                    command = input(self.color_format.format('Press B for back')).upper()
                    if command == 'B':
                        return
                    else:
                        print("Invalid option, please try again")
                        print(LINE)
        if self.user_type == 'Manager':
            while True:
                self.__print_work_report_table(report)
                print(f'{LINE}\n1: Approve report and close request\n2: Add comment on report\nB: Back')
                print(LINE)
                command = input(self.color_format.format("Choose Options: ")).upper()
                print(LINE)
                if command == 'B':
                    return
                if not command.isdigit():
                    print("Invalid option, please try again")
                    print(LINE)
                if command == '1':
                    self._approve_report(report.workreport_id, request)
                    return
                elif command == '2':
                    report.manager_cmt = input(self.color_format.format('Enter comment: '))
                    self.llapi._edit_work_report(report)


    def _approve_report(self, report_id, request):
        reader = self.llapi._list_work_reports()
        for report in reader:
            if report_id == report.workreport_id:
                request.status = 'completed'
                report.approved = True
                self.llapi._edit_work_report(report)
                self.llapi._edit_work_request(request)
                print('Report has been marked approved and request has been closed!') 


    def __edit_work_report(self, report):
        while True:
            fieldnames = ['Employee_SSN','Contractor_ID','Contractor_review','Contractor_remuneration','Total_cost','Description']
            for index, field in enumerate(fieldnames):
                print(f"{index+1}: {field}")
            col = input(self.color_format.format('What do you want to change? '))
            try:
                col = int(col)
                newval = input(self.color_format.format(f'What is the new {fieldnames[col-1]}? '))
                setattr(report, fieldnames[col-1].lower(), newval)
                return self.llapi._edit_work_report(report)
            except:
                print('Invalid input, please try again')

                
    def __print_work_report_table(self, report, nr=None):
        work_report_table = Texttable()
        work_report_table.add_row([get_color_string(bcolors.BLUE,"Work report\n⬇⬇⬇⬇⬇"),get_color_string(bcolors.BLUE,"Work report\n⬇⬇⬇⬇⬇")])
        if nr is not None:
            work_report_table.add_row([get_color_string(bcolors.GREEN,"Number"),nr])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Workreport_ID"),report.workreport_id])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Employee_SSN"),report.employee_ssn])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Contractor_ID"),report.contractor_id])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Contractor_review"),report.contractor_review])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Contractor_remuneration"),report.contractor_remuneration])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Total_cost"),report.total_cost])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Description"),report.description])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Approved"),report.approved])
        work_report_table.add_row([get_color_string(bcolors.GREEN,"Manager_comment"),report.manager_comment])
        print(f'{work_report_table.draw()}')
