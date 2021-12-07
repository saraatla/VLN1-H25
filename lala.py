


for line in .splitlines():
    if "wrep2" in line:
        print(line.replace("wrep2", "wrep" + str(bla)))
    elif "wrep3" in line:
        print(line.replace("wrep3", "wrep" + str(bla)))
    bla += 1