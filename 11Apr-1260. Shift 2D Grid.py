class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        k%=(n*m)
        c = k//m
        k%=m
        grid = grid[-c:]+grid[:-c]
        if k==0:
            return grid
        x = grid[-1][-k:]
        for i in range(n):
            grid[i],x = x+grid[i][:-k],grid[i][-k:]
        return grid
