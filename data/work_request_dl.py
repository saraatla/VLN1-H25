"""Workrequest_ID,Title,Property_ID,Destination_ID,Contractor,Repeat,When,Status,Priority,Description"""

import csv
from models.work_request import WorkRequest

class WorkRequestDL:
    def __init__(self):
        self.filepath = "csv_files/Workrequest.csv"
    
    def list_work_requests(self):
        ret_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                work_req = WorkRequest(row["Workrequest_ID"], row["Title"], row["Property_ID"], row["Destination_ID"],
                row["Contractor"], row["Repeat"], row["When"], row["Status"], row["Priority"], row["Description"])
                ret_list.append(work_req)
        return ret_list

    def create_work_request(self,work_req):
        with open(self.filepath, 'a', newline='') as csvfile:
            fieldnames = ['Workrequest_ID', 'Title', 'Property_ID', 'Destination_ID', 'Contractor', 'Repeat', 'When', 'Status','Priority','Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Workrequest_ID': work_req.workrequest_id, 'Title': work_req.title, 'Property_ID': work_req.property_id, 
            'Destination_ID': work_req.destination_id, 'Contractor':work_req.contractor, 'Repeat':work_req.repeat, 'When':work_req.when, 
            'Status':work_req.status, 'Priority':work_req.priority, 'Description':work_req.description})

    def search_work_request(self, search):
        with open(self.filepath, "r", newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if search == row[0]:
                    return row
            return False
    
    def edit_work_request(self, work_reqno, col,newvalue ):  
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data_list = list(reader)
            data_list[work_reqno][col] = newvalue
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_list)


    

