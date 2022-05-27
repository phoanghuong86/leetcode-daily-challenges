class Solution:
    def numberOfSteps (self, num: int) -> int:
        
        ans = 0
        
        while num:
            ans += (num & 1) + 1
            num >>= 1
        return ans-1
