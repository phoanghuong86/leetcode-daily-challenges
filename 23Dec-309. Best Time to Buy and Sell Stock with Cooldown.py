# except cool down, there are three states: sell or buy or have to cool down after sell
# three inputs: current day, holding stock or not, just sold the stock or not
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(i,HoldLabel,CoolDownLabel):
            if i == len(prices):
                return 0
            Cooldown = dp(i+1,HoldLabel,0)
            if CoolDownLabel:
                Action = dp(i+1,HoldLabel,0)
                
            else:
                if HoldLabel:
                    Action = prices[i] + dp(i+1,0,1)
                else:
                    Action = -prices[i] +dp(i+1,1,0)
            return max(Cooldown,Action)
        return dp(0,0,0)
