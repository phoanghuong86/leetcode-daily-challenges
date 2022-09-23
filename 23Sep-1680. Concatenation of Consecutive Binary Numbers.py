class Solution:
    def concatenatedBinary(self, n: int) -> int:
        val , mod = 0 , 10**9 + 7
        for num in range(1 , n+1):
            val <<= len(bin(num)) - 2
            val += num
            val %= mod
        return val
    
    
