from data.DLAPI import DLAPI

class LocationLL:
    def __init__(self):
        self.dlapi = DLAPI()

    def list(self):
        loc = self.dlapi.list_locations()
        temp = []
        for i in range(len(loc)):
            new = loc[i]
            for 

            ret_list.append(row[1])
        return ret_list
        