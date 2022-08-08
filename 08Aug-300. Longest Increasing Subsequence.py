class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        i,j = 0,1
        result = 1 
        while j<=len(nums)-1:
            while(i<j):
                if(nums[j]>nums[i]):
                    dp[j] = max(dp[j],1+dp[i])
                    result = max(dp[j],result)
                i+=1
            i = 0
            j+=1
        return result
