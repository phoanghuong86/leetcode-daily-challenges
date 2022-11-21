class Solution:
    def nearestExit(self, maze: List[List[str]], e: List[int]) -> int:
        
        m, n = len(maze), len(maze[0])
        
        # this lambda checks the exit conditions specified in the problem
        is_exit = lambda i, j : (i!=e[0] or j!=e[1]) and (i*j==0 or i==m-1 or j==n-1)
        
        # this generator yields (!) allowed directions
        def adj(i,j, dirs=[1, 0, -1, 0, 1]):
            for d in range(4):
                ii, jj = i + dirs[d], j + dirs[d+1]
                if 0 <= ii < m and 0 <= jj < n and maze[ii][jj] != "+":
                    yield ii,jj
            
        dq = deque([(e[0],e[1],0)])                # [1] start from the entrance                       
        while dq:                                  # [2] while there are still places to go...
            i, j, s = dq.popleft()                 #     ...try going there (don't try, do it!)
            for ii,jj in adj(i,j):                 # [3] look around and make a step
                maze[ii][jj] = "+"                 # [4] (and mark as visited)
                if is_exit(ii,jj) : return s+1     # [5] great, it's the exit!
                dq.append((ii,jj,s+1))             # [6] or maybe not, continue searching
                
        return -1                                  # [7] BFS failed, there is no escape
