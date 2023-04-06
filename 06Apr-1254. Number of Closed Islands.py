class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n,m=len(grid),len(grid[0])
        def dfs(i,j):
            if ( i<0 or i>=n or j <0
             or j >=m or grid[i][j]!=0 ):
             return 
            # indicated that it is visisted 
            grid[i][j]=1

            for x,y in ((0,1) ,(0,-1) ,(1,0),(-1,0)):
                new_i , new_j = x+i , y+j
                dfs(new_i , new_j)
        
        for i in range(n):
            for j in range(m):
                # check if it is border to discaed non closed island 
                if i==0 or j ==0 or i==n-1 or j==m-1:
                    dfs(i,j)
        res =0
        for i in range(n):
            for j in range(m):
                # visit all islan nodes 
                if grid[i][j]==0:
                    dfs(i,j)
                    res +=1
        return res
