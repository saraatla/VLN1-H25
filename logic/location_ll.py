from data.DLAPI import DLAPI

class LocationLL:
    """Location logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self):
        self.dlapi = DLAPI()

    def list_locations(self):
        return self.dlapi.list_locations()

    def location_dict(self):
        all_locations = self.dlapi.list_locations()
        temp = []
        loc = all_locations
        for i in range(len(all_locations)):
            loc = all_locations[i]
            for j in (loc.destination).strip().split(','):
                if j not in temp:
                    temp.append(j)
        location_dict = { str(i+1) : temp[i] for i in range(0, len(temp))}
        return location_dict
    
    def print_location(self):
        self.location_dict = self.location_dict()
        self.string = ""
        for key, valu in self.location_dict.items():
            self.string += f"{key}. {valu}\n"
        return self.string
        
    # Hvað gerir þetta?
    def list(self):
        location_dict = self.location_dict()
        loc_list = []
        for value in location_dict.values():
            loc_list.append(value)
        return loc_list
