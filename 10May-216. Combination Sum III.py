class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        #do it by bitmasking
        #there are a total of 2^9 = 512 bitmasks
        #for example, if 1 3 4 is used, then the corresponding bitmask has the 0th, 2nd, 3rd bit set
        
        ans = []
        
        for mask in range(512):
            tmp = []
            total = 0
            for j in range(9):
                if mask & (1 << j):
                    tmp.append(j+1)
                    total += j+1
            
            if total == n and len(tmp) == k:
                ans.append(tmp)
        
        
        return ans
