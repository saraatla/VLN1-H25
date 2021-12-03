import csv
from models.work_report import WorkReport

class WorkReportDL:
    def __init__(self):
        self.filepath = 'The_Code/csv_files/Workreport.csv'

    def get_all_reports(self):
        ret_list = []
        with open(self.filepath, newline="", encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                work_rep = WorkReport(row['Workreport_ID'], row['SSN'], row['Contractor'], row['Contractor_review'],
                row['Contractor_remuneration'], row['Total_cost'], row['Description'], row['Approved'])
                ret_list.append(work_rep)
            return ret_list

    def create_work_report(self, work_rep):
        with open(self.filepath, 'a', newline='') as csvfile:
            fieldnames = ['Workreport_ID', 'SSN', 'Contractor', 'Contractor_review', 'Contractor_remuneration', 'Total_cost', 'Description', 'Open']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'Workreport_ID': work_rep.workreport_id, 'SSN': work_rep.ssn, 'Contractor': work_rep.contractor, 
            'Contractor_review': work_rep.contractor_review, 'Contractor_remuneration':work_rep.contractor_remuneration,
            'Total_cost':work_rep.total_cost, 'Description':work_rep.description, 'Approved':work_rep.approved})


    def edit_work_report(self, rep_no, col, newval):
        with open(self.filepath, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            data_list = list(reader)
            data_list[rep_no][col] = newval
        with open(self.filepath, "w", newline="", encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_list)