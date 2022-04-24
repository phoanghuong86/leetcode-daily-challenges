class UndergroundSystem:

    def __init__(self):
        self.checkin_map = {}
        self.all_times_map = collections.defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_map[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.checkin_map[id]
        duration = t - checkin_time
        agg_time, num_elems = self.all_times_map[(checkin_station, stationName)]
        self.all_times_map[(checkin_station, stationName)] = (agg_time + duration, num_elems + 1)
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.all_times_map[(startStation, endStation)][0] / self.all_times_map[(startStation, endStation)][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
