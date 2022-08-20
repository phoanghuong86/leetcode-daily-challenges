class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        bag = []
        next_stop = startFuel
        ans = 0
        stations.append([target,0])
        for station in stations:
            while station[0] > next_stop:
                if not bag:
                    return -1
                else: 
                    next_stop -= heapq.heappop(bag)
                    ans += 1
            if station[0] <= next_stop:
                heapq.heappush(bag,-1*station[1])
                
        return ans
