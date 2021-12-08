from data.DLAPI import DLAPI

class DestinationLL:
    """destination logic layer class; Contains X functions: fetches the functions in the data layer API,"""
    def __init__(self,destination):
        self.destination = destination
        self.dlapi = DLAPI(self.destination)


    def destination_dict(self):
        all_destinations = self.dlapi.list_destinations()
        temp = []
        loc = all_destinations
        for i in range(len(all_destinations)):
            loc = all_destinations[i]
            for j in (loc.destination).strip().split(','):
                if j not in temp:
                    temp.append(j)
        destination_dict = { str(i+1) : temp[i] for i in range(0, len(temp))}

        return destination_dict
    

    def list_of_destinations(self):
        destination_dict = self.destination_dict()
        loc_list = []
        for value in destination_dict.values():
            loc_list.append(value)
        return loc_list
    
    
    def search_destination(self, dest):
        while True:
            reader = self.dlapi.list_destinations()
            for row in reader:
                if dest == row.destination:
                    return row

