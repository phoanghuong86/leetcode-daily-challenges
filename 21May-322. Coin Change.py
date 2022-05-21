class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [-1]*(amount+1)
        
        dp[0] = 0
        
        for i in range(1,amount+1):
            minimum = 10**4
            for ele in coins:
                
                if i - ele >= 0 and dp[i - ele] != -1:
                    minimum = min(minimum,1 + dp[i - ele])
            
            dp[i] = minimum if minimum != 10**4 else -1
        #print(dp)
        return dp[amount]
