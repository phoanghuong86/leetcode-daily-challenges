class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[0]*n
        for j in range(n-1,-1,-1):
            if obstacleGrid[m-1][j]==1:
                break
            dp[j]=1
        for i in range(len(obstacleGrid)-2,-1,-1):
            if obstacleGrid[i][n-1]==1:
                dp[n-1]=0
            for j in range(n-2,-1,-1):
                if not obstacleGrid[i][j]==1:
                    dp[j]+=dp[j+1]
                else:
                    dp[j]=0
        
        return dp[0]
