
from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.work_request import WorkRequest
from einartest2 import test
LINE = '------------------------------------------'
dlapi = DLAPI("All destinations")
table = Texttable()
testid = test()
def list_work_requests():
        # return self.dlapi.list_work_requests()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(180)
        workreq_list = dlapi.list_work_requests()
        for item in range(len(workreq_list)):
            workreq = workreq_list[item]
            # table.add_rows([["Nr","Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"], [item+1, workreq.workreport_id, workreq.title, workreq.property_id, workreq.destination_id, workreq.contractor, workreq.repeat, workreq.when, workreq.status, workreq.priority, workreq.description, workreq.workreport_id]])
            table.add_rows([["Nr","Workrequest_ID", "Title", "Status", "Priority"], [item+1, workreq.workrequest_id, workreq.title, workreq.status, workreq.priority]])
        print(table.draw())
        while True:
            command = input("Enter Nr of report to open or B to Back:").upper()
            if command == "B":
                return
            elif command.isdigit():
                nr = int(command)
                try:
                    testid.print_function(nr)
                except:
                    print("Nr out of range try again")
            else:
                print("Invalid input, try again!")
list_work_requests()