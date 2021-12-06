import csv
from models.work_report import WorkReport

class WorkReportDL:
    """Work report data layer class; Contains 4 functions: lists, 
    makes new and changes information about a work report"""
    def __init__(self, destination):
        self.filepath = 'csv/Workreport.csv'
        self.destination = destination

    def list_work_reports(self):
        return_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile) # reader maps the information in each row to a dict whose keys 
                                             # are given by the optional fieldnames parameter.
            for row in reader:
                work_rep = WorkReport([row['Workreport_ID'], row['SSN'], row['Contractor'], row['Contractor_review'],
                row['Contractor_remuneration'], row['Total_cost'], row['Description'], row['Approved']])
                return_list.append(work_rep)
            return return_list

    def create_work_report(self, work_rep):
        "This function appends a new work report to the csv file"
        with open(self.filepath, 'a', newline='') as csvfile:
            fieldnames = ['Workreport_ID', 'SSN', 'Contractor', 'Contractor_review', 'Contractor_remuneration', 'Total_cost', 'Description', 'Open']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Workreport_ID': work_rep.workreport_id, 'SSN': work_rep.ssn, 'Contractor': work_rep.contractor, 
            'Contractor_review': work_rep.contractor_review, 'Contractor_remuneration':work_rep.contractor_remuneration,
            'Total_cost':work_rep.total_cost, 'Description':work_rep.description, 'Approved':work_rep.approved})

    def edit_work_report(self, rep_no, col, newval):
        """This function edits a certain value for a certain work report (input by employee)"""
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile) # iterates over lines in the csvfile.
            data_list = list(reader)
            data_list[rep_no][col] = newval
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)  # converts the value into delimited string on the csvfile
            writer.writerows(data_list)