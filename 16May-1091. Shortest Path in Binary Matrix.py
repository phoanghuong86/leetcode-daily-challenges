class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)

        if grid[0][0] or grid[n-1][n-1]:
            return -1

        if len(grid) == 1:
            return 1

        ans = [(0,0,1)]

        visited = set([(0,0)])

        while ans:
            i, j, dist = ans.pop(0)

            if (i,j) == (n-1,n-1):
                return dist

            for ni, nj in [(i+1,j),(i+1,j+1),(i+1,j-1),(i,j+1),(i,j-1),(i-1,j+1),(i-1,j),(i-1,j-1)]:
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0 and (ni,nj) not in visited:
                    visited.add((ni,nj))
                    ans.append((ni,nj,dist+1))

        return -1
