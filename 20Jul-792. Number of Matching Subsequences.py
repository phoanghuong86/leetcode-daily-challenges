class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        d = {}
        for word in words:
            if self.helper(s, word, d):
                res+=1
        return res
    
    def helper(self, s: str, word: str, d: dict) -> bool:
        if word in d:
            if d[word]: return True
            return False
        p = 0
        for i in range(len(s)):
            if s[i] == word[p]:
                p+=1
            if p == len(word):
                d[word] = True
                return True
        d[word] = False
        return False
    
