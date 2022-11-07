class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for i,c in enumerate(s):
            if c=='6': return int(s[:i]+'9'+s[i+1:])
        return num
