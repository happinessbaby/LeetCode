from statistics import mean

class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.avgTravelTimes = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id]=[stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.customers.pop(id)
        travelTime = t-startTime
        self.avgTravelTimes[(startStation, stationName)].append(travelTime)
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return float(mean(self.avgTravelTimes[(startStation, endStation)]))
        
            
            


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)