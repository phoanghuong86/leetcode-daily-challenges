
"""
if s is not palindrome, wee can remove all 'b'(1 step), and all 'a' (2 step)
"""
class Solution:
    def is_palindrome(self, s):
        for i in range(len(s)//2):
            if s[i] != s[-1 -i]:
                return False
        
        return True
    
    def removePalindromeSub(self, s: str) -> int:
        return 1 if self.is_palindrome(s) else 2
