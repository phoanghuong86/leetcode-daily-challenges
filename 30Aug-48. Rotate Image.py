class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # in place transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                
        # reverse rows
        for row in matrix:
            row = row.reverse()
