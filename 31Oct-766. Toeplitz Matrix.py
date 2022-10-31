from scipy.linalg import toeplitz

class Solution:
    def isToeplitzMatrix(self, m: List[List[int]]) -> bool:
	    # construct Toeplitz matrix using first row and first column, then compare
        return (toeplitz(list(zip(*m))[0], m[0]) == m).all()
