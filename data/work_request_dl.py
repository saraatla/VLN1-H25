"""Workrequest_ID,Title,Property_ID,Destination_ID,Contractor,Date,Status,Priority,Description"""
import datetime
import csv
from models.work_request import WorkRequest

class WorkRequestDL:
    """WorkRequest data layer class; Contains 4 functions: lists, 
    makes new and changes information about a work request"""
    def __init__(self, destination):
        self.filepath = "csv/Workrequest.csv"
        self.destination = destination
    
    def list_work_requests(self):
        """This function reads the csv file and makes a list with 
        all the work requests along with their information"""
        ret_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                work_reqdate = datetime.strptime(row["Date"],'%d/%m/%Y')
                work_req = WorkRequest([row["Workrequest_ID"], row["Title"], row["Property_ID"], row["Destination"],
                row["Contractor"], work_reqdate.date(),row["Status"], row["Priority"], row["Description"], row["Workreport_ID"]])
                ret_list.append(work_req)
        return ret_list

    def create_work_request(self,work_req):
        "This function appends a new work request to the csv file"
        with open(self.filepath, 'a', newline='') as csvfile:
            fieldnames = ['Workrequest_ID', 'Title', 'Property_ID', 'Destination', 'Contractor', 'Date', 'Status','Priority','Description','Workreport_ID']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Workrequest_ID': work_req.workrequest_id, 'Title': work_req.title, 'Property_ID': work_req.property_id, 
            'Destination': work_req.destination, 'Contractor':work_req.contractor, 'Date':work_req.date, 
            'Status':work_req.status, 'Priority':work_req.priority, 'Description':work_req.description, 'Workreport_ID':work_req.workreport_id})
    
    def edit_work_request(self, workreq):  
        """This function edits a certain value for a certain work request (input by Manager)"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader)
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)  # converts the value into delimited string on the csvfile
            for row in data_list:
                if workreq.workrequest_id == row[0]:
                    writer.writerow([workreq.workrequest_id, 
                                     workreq.title, 
                                     workreq.property_id, 
                                     workreq.destination, 
                                     workreq.contractor, 
                                     workreq.date, 
                                     workreq.status, 
                                     workreq.priority,
                                     workreq.description,
                                     workreq.workreport_id])
                else:
                    writer.writerow(row)


    def find_last_id(self):
        req_list = self.list_work_requests()
        return req_list[-1].workrequest_id



    

