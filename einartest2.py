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
        #self.table.add_rows([["Nr","Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"],[self.item+1, workreq.workreport_id, workreq.title, workreq.property_id, workreq.destination_id, workreq.contractor, workreq.repeat, workreq.when, workreq.status, workreq.priority, workreq.description, workreq.workreport_id]])
        #self.table.add_rows([["Nr"],[self.item+1],["Workrequest_ID"],[workreq.workreport_id],["Title"],[workreq.title],["Property_ID"],[workreq.property_id]])
        self.table.add_row([["Nr"],[self.item+1]])
        self.table.add_row([["Workrequest_ID"],[workreq.workreport_id]])#,["Title"],[workreq.title],["Property_ID"],[workreq.property_id]])
        print(self.table.draw())
 
