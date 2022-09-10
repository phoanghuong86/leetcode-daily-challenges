class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = [[-1]*(2*k+1) for x in range(len(prices))]
        
        def dp(i, tno) :
            if i==len(prices) or tno == 0 : return 0
            
            if memo[i][tno] != -1 : return memo[i][tno]
            
            if(tno%2 == 0) :
                memo[i][tno] = max(-prices[i]+dp(i+1, tno-1), dp(i+1, tno));
            else : memo[i][tno] = max(prices[i]+dp(i+1, tno-1), dp(i+1, tno));
            return memo[i][tno]
        
        return dp(0, 2*k)
