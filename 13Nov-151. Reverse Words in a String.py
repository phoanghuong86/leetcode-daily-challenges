class Solution:
    def reverseWords(self, s: str) -> str:
        ans = s.split()
        b = ''
        for i in ans[::-1]:
            b += i + ' '
        return b.strip()
