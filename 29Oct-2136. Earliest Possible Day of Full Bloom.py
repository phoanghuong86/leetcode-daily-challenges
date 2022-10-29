class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        v = []
        for i in range(len(plantTime)):
            v.append((growTime[i], plantTime[i]))
        
        v.sort(reverse = True)
        day, lpd = 0, 0
        for p in v:
            lpd += p[1]
            day = max(day, lpd + p[0])
        
        return day
