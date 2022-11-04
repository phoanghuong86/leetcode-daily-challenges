class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s)-1
        v = ["a", "e", "i", "o", "u"]
        s = list(s)
        while l < r:
            while s[l].lower() not in v and l < r:
                l += 1
            while s[r].lower() not in v and l < r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return "".join(s)
