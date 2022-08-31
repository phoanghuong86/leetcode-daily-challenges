class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n =  len(heights)
        m = len(heights[0])
         #initial -> these will touch Pacific 
        Pac = [[False]* m for _ in range(n) ] 
        for i in range(m):
            Pac[0][i] = True
            
        for j in range(n):
            Pac[j][0] = True
        #initial -> these will touch altlantic 
        Alt = [[False]* m for _ in range(n) ]
        for i in range(n):
            Alt[i][m-1] = True       
        for j in range(m):
            Alt[n-1][j] = True
        
        #DFS to find where can reach 
        def FindPac(x,y , now_height):
            for nx,ny in [[0,1],[0,-1], [1,0], [-1,0]]:
                if 0<= x+nx< n and 0<= y+ny <m and Pac[x+nx][y+ny] == False and heights[x+nx][y+ny] >=now_height:
                    Pac[x+nx][y+ny] = True
                    FindPac(x+nx, y+ny, heights[x+nx][y+ny])
        for i in range(n):
            for j in range(m):
                if Pac[i][j] == True:
                    FindPac(i,j, heights[i][j])
        #DFS to find where can reach 
        def FindAlt(x,y , now_height):
            for nx,ny in [[0,1],[0,-1], [1,0], [-1,0]]:
                if 0<= x+nx< n and 0<= y+ny <m and Alt[x+nx][y+ny] == False and heights[x+nx][y+ny] >=now_height:
                    Alt[x+nx][y+ny] = True
                    FindAlt(x+nx, y+ny, heights[x+nx][y+ny])
        for i in range(n):
            for j in range(m):
                if Alt[i][j] == True:
                    FindAlt(i,j, heights[i][j])
        # only record the both can reach point 
        ans = []
        for i in range(n):
            for j in range(m):
                if Alt[i][j] and Pac[i][j]:
                    ans.append([i,j])
        return ans 
        
        
