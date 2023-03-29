class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        if satisfaction[-1] <= 0:
            return 0
        
        if satisfaction[0] >= 0:
            res = 0
            for idx, val in enumerate(satisfaction):
                res += (idx+1) * val
            return res
        
        i = 0
        out = float('-inf')
        while i < len(satisfaction):
            j = i
            currRes = 0
            time = 1
            while j < len(satisfaction):
                currRes += (time) * satisfaction[j]
                j += 1
                time+=1
            
            out = max(out, currRes)
            i += 1
        
        return out
