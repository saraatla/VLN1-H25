from data.DLAPI import DLAPI

class LocationLL:
    def __init__(self):
        self.dlapi = DLAPI()

    def make_list(self):
        loc = self.dlapi.list_locations()
        temp = []
        for i in range(len(loc)):
            new = loc[i]
            for j in new.strip().split(','):
                if j not in temp:
                    temp.append(j)
        location_dict = { str(i+1) : temp[i] for i in range(0, len(temp))}
        return location_dict
    
    def list(self):
        location_dict = self.make_list()
        loc_list = []
        for value in location_dict.values():
            loc_list.append(value)
        return loc_list
