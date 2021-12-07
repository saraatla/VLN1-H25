from Extra.acci import empAscii, locAscii, contAscii, propAscii

while True:
    v = input('1. emp\n2. dest\n3. cont\n4. prop\nYour input: ')
    if v == '1':
        empAscii()
    elif v == '2':
        locAscii()
    elif v == '3':
        contAscii()
    elif v == '4':
        propAscii()
    else:
        print('nicetry')