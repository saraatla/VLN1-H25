from Extra.acci import empAscii, locAscii, contAscii, propAscii, workAscii

while True:
    v = input('1. emp\n2. dest\n3. cont\n4. prop\n5. work\nYour input: ')
    if v == '1':
        empAscii()
    elif v == '2':
        locAscii()
    elif v == '3':
        contAscii()
    elif v == '4':
        propAscii()
    elif v == '5':
        workAscii()
    else:
        print('nicetry')