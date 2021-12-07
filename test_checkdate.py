input_date = input('Date:')

try:
    int(input_date[0:2])
    input_date[2] == '/'
    int(input_date[3:5])
    input_date[5] == '/'
    int(input_date[6:])
except:
    print('no')