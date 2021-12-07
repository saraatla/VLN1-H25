import datetime
from datetime import datetime
from datetime import date
from datetime import timedelta


intro = print('Do you want to repeat this work request?')
options = ['Do no repeat', 'Daily', 'Weekly', 'Monthly', 'Yearly']
for i, option in enumerate(options):
            print(f"{i+1}: {option}")

repeat = input('Choose option: ')

start_date = input("Enter start date of work request, dd/mm/yyyy: ")
date = start_date.split('/')
xDate = date(int(date[2]),int(date[1]),int(date[0]))

if date.today() < xDate:
    if repeat == '1':
        pass

elif repeat == 2:
    howmany = int(input("how many days: "))
    for i in range(howmany):
        new_date = timedelta(days = i)
        date_work_req = xDate + new_date
        print(date_work_req)


#aDate = datetime.datetime.strptime(date,"%Y-%m-%d")

#Weeks = datetime.timedelta(weeks = howmany)

#print(xDate + Weeks)