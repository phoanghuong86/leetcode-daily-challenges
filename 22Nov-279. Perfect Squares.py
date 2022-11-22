class Solution:
    def numSquares(self, n: int) -> int:
        dp=[float('inf') for i in range(n+1)]
        dp[0]=0
        v=int(n**0.5)
        arr=[i*i for i in range(v+1)]
        for i in range(1,n+1):
            for j in arr:
                if(i-j>=0):
                    dp[i]=min(dp[i],dp[i-j]+1)
        return dp[-1]
