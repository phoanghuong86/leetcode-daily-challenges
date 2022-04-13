class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return
        if n == 1:
            return [[1]]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        board = [[0 for _ in range(n)] for _ in range(n)]
        
        def next_cell(row, col, direct):
            row1 = row + directions[direct][0]
            col1 = col + directions[direct][1]
            if row1 < 0 or row1 >= n or col1 < 0 or col1 >= n or board[row1][col1] != 0:
                direct = (direct + 1) % 4
                row1 = row + directions[direct][0]
                col1 = col + directions[direct][1]
            
            return (row1, col1, direct)
        
        row = col = direct = 0
        board[0][0] = 1
        i = 2        
        while i <= n**2:
            row, col, direct = next_cell(row, col, direct)
            board[row][col] = i
            i += 1
            
        return board
