class Solution:
    def minFallingPathSum(self, matrix):
        n, m = len(matrix), len(matrix[0])

        dp = [[0]*m for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]


        for i in range(1,n):
            for j in range(n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j+1])
                elif j == n-1:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j],dp[i-1][j-1])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])


        return min(dp[-1])
