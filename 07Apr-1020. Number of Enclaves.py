class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row, col, seen):
            if row < 0 or row >= n or col < 0 or col >= m:
                return True, 0
            
            if seen[row][col] or grid[row][col] == 0:
                return False, 0
            
            seen[row][col] = True
            lands = 1
            reached_boundry = False
            for i, j in ((0, 1),(0, -1), (1, 0), (-1, 0)):
                b, l = dfs(row + i, col + j, seen)
                reached_boundry |= b
                lands += l
            return reached_boundry, lands

        n, m = len(grid), len(grid[0])
        seen = [[False] * m for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m):
                reached_boundry, lands = dfs(i, j, seen)
                ans = ans + lands if not reached_boundry else ans
        return ans
