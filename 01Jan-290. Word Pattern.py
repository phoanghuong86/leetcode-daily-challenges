class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        arr = s.split()
        if len(pattern) != len(arr): return False
        for i,c in enumerate(pattern):
            w = arr[i]
            if w not in dic.values() and not dic.get(c):
                dic[c] = w
            elif dic.get(c) != w:
                return False
        return True
                
