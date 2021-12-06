from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from models.work_request import WorkRequest
class test:
    def __init__(self):
        self.dlapi = DLAPI("All destinations")
        self.workreq_list = self.dlapi.list_work_requests()
        self.table = Texttable()
        
    def print_function(self,row):
        self.item = row-1
        workreq = self.workreq_list[self.item]
        self.table.add_row(["Nr",self.item+1])
        self.table.add_row(["Workrequest_ID",workreq.workrequest_id])
        self.table.add_row(["Title",workreq.title])
        self.table.add_row(["Property_ID",workreq.property_id])
        self.table.add_row(["Destination_ID",workreq.destination_id])
        self.table.add_row(["Contractor",workreq.contractor])
        self.table.add_row(["Repeat",workreq.repeat])
        self.table.add_row(["When",workreq.when])
        self.table.add_row(["Status",workreq.status])
        self.table.add_row(["Priority",workreq.priority])
        self.table.add_row(["Description",workreq.description])
        self.table.add_row(["Workreport ID",workreq.workreport_id])
        print(self.table.draw())
            
        
    
 
