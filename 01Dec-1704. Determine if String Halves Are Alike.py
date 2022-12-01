class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        return sum([Counter(s[:len(s)//2])[v]-Counter(s[len(s)//2:])[v] for v in set('aeiouAEIOU')])==0
