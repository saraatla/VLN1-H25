"""Workrequest_ID,Title,Property_ID,Destination_ID,Contractor,Repeat,When,Status,Priority,Description"""

import csv
from models.work_request import WorkRequest

class WorkRequestDL:
    """WorkRequest data layer class; Contains 4 functions: lists, 
    makes new and changes information about a work request"""
    def __init__(self, location):
        self.filepath = "csv_files/Workrequest.csv"
        self.location = location
    
    def list_work_requests(self):
        """This function reads the csv file and makes a list with 
        all the work requests along with their information"""
        ret_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                work_req = WorkRequest(row["Workrequest_ID"], row["Title"], row["Property_ID"], row["Destination_ID"],
                row["Contractor"], row["Repeat"], row["When"], row["Status"], row["Priority"], row["Description"])
                ret_list.append(work_req)
        return ret_list

    def create_work_request(self,work_req):
        "This function appends a new work request to the csv file"
        with open(self.filepath, 'a', newline='') as csvfile:
            fieldnames = ['Workrequest_ID', 'Title', 'Property_ID', 'Destination_ID', 'Contractor', 'Repeat', 'When', 'Status','Priority','Description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # writer maps dictionaries onto output rows.
            writer.writerow({'Workrequest_ID': work_req.workrequest_id, 'Title': work_req.title, 'Property_ID': work_req.property_id, 
            'Destination_ID': work_req.destination_id, 'Contractor':work_req.contractor, 'Repeat':work_req.repeat, 'When':work_req.when, 
            'Status':work_req.status, 'Priority':work_req.priority, 'Description':work_req.description})

    # def search_work_request(self, search):

    #     with open(self.filepath, "r", newline="", encoding='utf-8') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             if search == row[0]:
    #                 return row
    #         return False
    
    def edit_work_request(self, work_reqno, col,newvalue ):  
        """This function edits a certain value for a certain work request (input by supervisor)"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader)
            data_list[work_reqno][col] = newvalue
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)  # converts the value into delimited string on the csvfile
            writer.writerows(data_list)


    

