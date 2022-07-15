class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        out=0
        visited=set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # if the grid is 1 and we haven't visited this grid before
                if grid[r][c]==1 and (r,c) not in visited:
                    stack=[(r,c)]
                    cnt=0
                    # DFS
                    while stack:
                        current=stack.pop(0)
                        if current in visited:
                            continue
                        cnt+=1
                        row=current[0]
                        col=current[1]
                        visited.add((row,col))
                        if row<len(grid)-1 and grid[row+1][col]==1 and (row+1,col) not in visited:
                            stack.append((row+1,col))
                        if row>0 and grid[row-1][col]==1 and (row-1,col) not in visited:
                            stack.append((row-1,col)) 
                        if col<len(grid[0])-1 and grid[row][col+1]==1 and (row,col+1) not in visited:
                            stack.append((row,col+1))
                        if col>0 and grid[row][col-1]==1 and (row,col-1) not in visited:
                            stack.append((row,col-1))
                    if cnt>out:
                        out=cnt
        return out
