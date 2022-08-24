class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1: return True
        
        if n%3 != 0: return False
        
        pow = 3
        
        while pow <= n:
            if pow == n: return True
            pow = pow*3
        
        return False
