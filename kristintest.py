from data.employee_dl import EmployeeDL
from models.employee_model import Employee
from logic.employee_ll import EmployeeLL
"""
# d1 < d2
import datetime

x = datetime.datetime(2021, 12, 12)
12/12/21

print(x)
# dd/mm/yy
12/12/21
from datetime import datetime
from datetime import date
from datetime import timedelta


print(x.strftime("%A"))
print(x.strftime("%D"))

answer = int(input(("Do you want to repeat this work request?")))
# Svarmöguleikar : 1. do not repeat
#                  2. daily
#                  3. weekly
#                  4. monthly
#                  5. yearly
date_ = input("When do yo want this to start? dd/mm/yyyy: ")
date__ = date_.split('/')
x = date(int(date__[2]),int(date__[1]),int(date__[0]))
print(date.today())
if date.today() < x:
    
    if answer == 1:
        pass
    # create_work_request()

    elif answer == 2:
        
        how_many = int(input('for how many days?:'))
        for i in range(how_many):
            new_date = timedelta(days = 1*i)
            date_work_req = x + new_date
            print(date_work_req)
            # create_work_request()

    elif answer == 3:
        how_many = int(input('for how many weeks?:'))
        for i in range(how_many):
            new_date = timedelta(weeks = 1*i)
            date_work_req = x + new_date

    elif answer == 4:
        how_many = input('for how many months?:')
        for i in range(how_many):
            new_date = timedelta(months = 1*i)
            date_work_req = x + new_date

    elif answer == 5:
        how_many = input('for how many years?:')
        for i in range(how_many):
            new_date = timedelta(years = 1*i)
            date_work_req = x + new_date

else:
    print("This date has already taken place")

"""
"""
from datetime import datetime
year = 2021
month = 12
day = 26
date = datetime(year, month, day)
date_search_from = datetime(2021, 12, 10)
date_search_to = datetime(2021, 12, 31)
if date_search_from <= date <= date_search_to:
    print("date inbetween")
else:
    print("date out of range")
date = datetime(2021, 12, 1)

if date_search_from <= date <= date_search_to:
    print("date inbetween")
else:
    print("date out of range")
"""
from datetime import datetime,date,timedelta
"""
from os import read
from Extra.texttableFile.texttable import Texttable
from data.DLAPI import DLAPI
from logic.LLAPI import LLAPI
from models.work_request import WorkRequest
from logic.work_request_ll import WorkRequestLL

dlapi = DLAPI('Svalbard - Longyearbyen')
llapi = LLAPI('Svalbard - Longyearbyen')
work_requestLL = WorkRequestLL('Faroe Islands - Tórshavn')

reader = llapi.list_all_work_requests('Faroe Islands - Tórshavn')
request_list = []
for request in reader:
    request_list.append(request)

start_date = '01/05/2021'
end_date = '31/12/2021'

def check_if_date_is_between(request_list,start_date,end_date):
    date_search_from = datetime.strptime(start_date,'%d/%m/%Y')
    date_search_to = datetime.strptime(end_date,'%d/%m/%Y')
    request_list_by_date = []
    for request in request_list:
        if request.status == 'completed':
            if date_search_from.date() <= request.date <= date_search_to.date():
                request_list_by_date.append(request)
    return request_list_by_date


def list_work_requests_ui(request_list):
        table = Texttable()
        table.set_deco(Texttable.HEADER)
        table.set_max_width(300)
        for item in range(len(request_list)):
            workreq = request_list[item]
            table.add_rows([["Number.","Workrequest_ID", "Title", "Date", "Status", "Priority"], 
                            [item+1, workreq.workrequest_id, workreq.title, workreq.date, workreq.status, workreq.priority]])
        print(table.draw())

# bla = check_if_date_is_between(request_list,start_date,end_date)
# list_work_requests_ui(check_if_date_is_between(request_list,start_date,end_date))


# dlapi = DLAPI('Svalbard - Longyearbyen')
string = 'hwllo'         
# reader = dlapi.list_contractors()
for contractor in reader:
    print(type(contractor))
    print(type(string))
    print(type(dlapi))





# date = 
# Repeat = 
# daglega
# d = d + 1
# vikulega
# d = d + 7
#mánaðarlega 
# m = m+1
# árlega
# y = y+1





# empDL = EmployeeDL()
# emp = Employee('kristin', '123456-3456', 'kristinb20@ru.is','Stigahlíð 84', '564-2728', '824-3732', 'Reykjavik', "L1","keflavik", "yfirmaður")
# empDL = EmployeeDL('Svalbard')
# listi = ['Jan Jacobsen','123456-0001','jan.jacobsen@nanair.is','Vei 230 12. Longyearbyen','+47 92 09 77 00','+354 777 1337','Svalbard','Lonyearbyen','Manager']
# emp = Employee(listi)
# edit_employee = empDL.edit_employee('123456-0001',3,'hrauntunga23')

# def create_work_request(self,work_req):
#         # return self.dlapi.create_work_request(work_req)
#         print('Enter the following information: ')
#         print(LINE)
#         workreq = []
#         fieldnames = ["Workrequest_ID", "Title", "Property_ID", "Destination_ID", "Contractor_ID", "Repeat", "When", "Status", "Priority", "Description", "Workreport_ID"]
#         for field in fieldnames:
#             val = input(f'{field}: ')
#             workreq.append(val)
#         self.dlapi.create_contractor(WorkRequest(workreq))
#         print(f'{LINE}\nWork request successfully created!\n{LINE}')
"""
start_date = '12/12/2021'
repeat = 2
date_var = datetime.strptime(start_date,'%d/%m/%Y').date()
print(date_var)
if date.today() <= date_var:
    i = 0
    if repeat == 2:
        # how_many = int(input(self.color_format.format('for how many days: ')))
        for i in range(4):
            new_date = timedelta(days = 1*i)
            # self.__create_repeated(workreq, date_var, new_date)
print(type(date_var))
print(new_date)
print(type(new_date))