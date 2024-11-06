class UndergroundSystem:

    def __init__(self):
        self.people = {} # id: ((),()). 1 for checkin, another for checkout
        self.stations = {} # station1 : { station2 : (# customers, total commute time) } # avg = total/#customers 
         

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # we will just save info into people 
        self.people[id] = [(stationName, t), ()] # second tuple for checkout info

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # we also update stations hashMap
        self.people[id][1] = (stationName, t)
        checkIn_station, checkIn_time = self.people[id][0]
        if checkIn_station not in self.stations:
            self.stations[checkIn_station] = {stationName : (1, t - checkIn_time)}
        else: 
            # update the existing record between stations
            checkOut_stations = self.stations[checkIn_station]
            tup = checkOut_stations.get(stationName, (0, 0))  
            tup = (tup[0] + 1, tup[1] + t - checkIn_time)
            checkOut_stations[stationName] = tup
            self.stations[checkIn_station] = checkOut_stations

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # we will use stations hashMap 
        num_customers, total_time = self.stations[startStation][endStation]
        return total_time/num_customers


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)