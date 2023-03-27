class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_len, col_len  = len(grid), len(grid[0])
    
        table = [float(inf)] * col_len
        table[-1] = grid[row_len-1][col_len-1]

        for r in range(row_len -1, -1, -1):
            for c in range(col_len-1, -1, -1):

                if r== row_len -1 and c==col_len -1:
                    continue

                down_value = table[c] if r + 1 < row_len else float(inf)
                right_value = table[c + 1] if c + 1 < col_len else float(inf)

                table[c] = grid[r][c] + min(down_value, right_value)

        return table[0] 
