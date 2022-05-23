def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = {}  # str : [0's, 1's]
        
        same = collections.Counter(strs)
        for cur in strs:
            count[cur] = [cur.count("0"), cur.count("1")]
            
            
        @lru_cache(None)    
        def getMax(i, zero, one):
            if i == len(strs):
                return 0
            
            best = 0
            if zero >= count[strs[i]][0] and one >= count[strs[i]][1]:
                best = max(best, getMax(i + 1, zero - count[strs[i]][0], one - count[strs[i]][1]) + 1)
            
            best = max(best, getMax(i + 1, zero, one))
            
            return best
        
        return getMax(0, m, n)
