class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        ROWS,COLS = len(grid)-1,len(grid[0])-1
        q = deque([(0,0,k,0)])
        visited = set((0,0,k))
        while q:
            r,c,m,st = q.popleft()
            if r == ROWS and c == COLS:
                return st
            st+=1
            if (r,c,m) in visited:
                continue
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if (not 0<=nr<=ROWS 
                    or not 0<= nc<=COLS 
                    or (grid[nr][nc] ==1 and m == 0) 
                   ):
                    continue
                if grid[nr][nc] == 1: 
                    q.append((nr,nc,m-1,st))
                else:
                    q.append((nr,nc,m,st))
            visited.add((r,c,m))
            
        return -1
