class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        
        def dfs(indx):
            if indx >= len(nums):
                return 0
            if indx in dp:
                return dp[indx]
            dp[indx] = max(dfs(indx+2) + nums[indx],dfs(indx+1))
            return dp[indx]
        return dfs(0)
