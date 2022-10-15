class Solution:
    # 1 <= s.length <= 100, N^2 algorithm should be ok
    # As we cannot deduce easily whether to keep or delete a certain character when scanning from left to right, we have to use DP
    # dp(i, l, c, count): minimum length of run-length encoded version of s[:i], after deleting l characters, in which the string after modifications ends with c repeated count times
    # We want to look for min (dp(n, 0:k+1, :, :))
    
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        dp = {('', 0, k): 0}
        
        for c in s:
            dp_new = {}
            for prev, count, l in dp.keys():
                # increment = increase in text length
                # count_new = new count
                increment = 0
                # not do anything, just attach the previous words
                if c == prev:
                    count_new = count + 1
                    # the previous character either appeared 0, 1, 9, 99 times
                    if count in (0, 1, 9, 99):
                        increment += 1                    
                else:
                    increment += 1
                    count_new = 1
                if (c, count_new, l) not in dp_new:
                    dp_new[(c, count_new, l)] = float('Inf')
                dp_new[(c, count_new, l)] = min(dp_new[(c, count_new, l)], dp[(prev, count, l)] + increment)
                
                # Delete the current character
                if l > 0:
                    if (prev, count, l-1) not in dp_new:
                        dp_new[(prev, count, l-1)] = float('Inf')
                    dp_new[(prev, count, l-1)] = min(dp_new[(prev, count, l-1)], dp[(prev, count, l)])            
            dp = dp_new
        return min(dp.values())
