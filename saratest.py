from data.work_report_dl import WorkReportDL
from models.work_report import WorkReport


repDL = WorkReportDL('Svalbard')

"""
x = []
for i in range(10, 141): 
    x.append(i*3)

for i in x:
    work_rep = WorkReport([f'wrep{i}','123456-0004','N/A','N/A','N/A','10.000.-','Gekk rosa vel','False'])
    repDL.create_work_report(work_rep)
    work_rep = WorkReport([f'wrep{i+1}','123456-0005','N/A','N/A','N/A','10.000.-','Gekk vel!','False'])
    repDL.create_work_report(work_rep)
    work_rep = WorkReport([f'wrep{i+2}','123456-0006','N/A','N/A','N/A','10.000.-','Gekk þokkalega','False'])
    repDL.create_work_report(work_rep)


x = []
for i in range(144, 214): 
    x.append(i*3)

for i in x:
    work_rep = WorkReport([f'wrep{i}','123456-0008','N/A','N/A','N/A','15.000.-','Gekk mjög vel','False'])
    repDL.create_work_report(work_rep)
    work_rep = WorkReport([f'wrep{i+1}','123456-0009','N/A','N/A','N/A','15.000.-','Allt gekk vel!','False'])
    repDL.create_work_report(work_rep)
    work_rep = WorkReport([f'wrep{i+2}','123456-0007','N/A','N/A','N/A','15.000.-','Allt gekk eins og í sögu','False'])
    repDL.create_work_report(work_rep)"""